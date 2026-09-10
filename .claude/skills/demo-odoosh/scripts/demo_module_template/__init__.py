import logging

from . import demo_config as cfg
from . import models  # noqa: F401

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Rulează o singură dată, la instalarea build-ului de dev pe odoo.sh.

    1. Pune pe admin parola aleasă de script (implicit `admin`). odoo.sh o rescrie DUPĂ instalare,
       de aceea cronul din data/ir_cron.xml o reimpune la primul minut după pornire.
    2. Dezactivează userul demo, ca să nu existe a doua intrare cunoscută public.
    3. Pregătește contextul românesc, dacă a fost cerut (`--ro` sau `--ro-fiscal`).
    """
    admin = env.ref("base.user_admin")
    admin.write({"password": cfg.ADMIN_PASSWORD})
    _logger.info("terrabit_demo: parola admin setată din demo_config")

    demo_user = env.ref("base.user_demo", raise_if_not_found=False)
    if demo_user:
        demo_user.write({"active": False})

    if cfg.RO_MODE:
        _setup_ro(env, admin)


def _setup_ro(env, admin):
    """Compania românească pe care se face demonstrația, plus datele de pornire.

    În modul „fiscal" refolosim compania demo a localizării (`base.demo_company_ro`), fiindcă pe
    ea stau facturile fiscale din `l10n_ro_anaf_base` (taxare inversă, intracomunitar, TVA la
    încasare). Dacă build-ul a fost făcut fără date demo, compania aceea nu există și cădem pe
    modul „own": creăm noi o companie RO cu planul de conturi românesc.
    """
    company = False
    if cfg.RO_MODE == "fiscal":
        company = env.ref("base.demo_company_ro", raise_if_not_found=False)
        if company:
            demo_moves = env["account.move"].search_count(
                [("company_id", "=", company.id), ("move_type", "!=", "entry")]
            )
            _logger.info(
                "terrabit_demo: folosesc compania demo RO '%s' cu %d facturi demo, "
                "între care cazurile fiscale din l10n_ro_anaf_base",
                company.name, demo_moves,
            )
        else:
            _logger.warning(
                "terrabit_demo: base.demo_company_ro lipsește (build fără date demo); creez o companie RO proprie"
            )

    if not company:
        ron = env.ref("base.RON")
        if not ron.active:
            ron.write({"active": True})
        company = env["res.company"].create(
            {
                "name": cfg.RO_COMPANY_NAME,
                "country_id": env.ref("base.ro").id,
                "currency_id": ron.id,
            }
        )
        if "account.chart.template" in env:
            env["account.chart.template"].try_loading("ro", company, install_demo=False)
        _logger.info("terrabit_demo: companie RO '%s' creată cu planul de conturi ro", company.name)

    admin.write({"company_ids": [(4, company.id)], "company_id": company.id})

    # Seed-ul comercial e opțional: dacă pică, instalarea (și parola admin) nu trebuie să pice cu el.
    try:
        with env.cr.savepoint():
            from . import demo_seed_ro

            demo_seed_ro.seed(env, company)
    except Exception:  # noqa: BLE001 — logăm și mergem mai departe
        # Rollback-ul savepoint-ului șterge înregistrările seed-ului, dar callback-urile
        # post-commit deja înregistrate (ex. rangul de client pe parteneri) le mai referă
        # și ar rupe încărcarea registry-ului. Le abandonăm.
        env.cr.postcommit.clear()
        _logger.exception("terrabit_demo: seed-ul RO a eșuat; compania rămâne fără facturi demo")
