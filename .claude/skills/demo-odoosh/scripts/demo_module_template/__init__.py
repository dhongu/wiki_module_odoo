import logging

from . import demo_config as cfg
from . import models  # noqa: F401

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Rulează o singură dată, la instalarea build-ului de dev pe odoo.sh.

    1. Pune pe admin parola aleasă de script (implicit `admin`). odoo.sh o rescrie DUPĂ instalare,
       de aceea cronul din data/ir_cron.xml o reimpune la primul minut după pornire.
    2. Dezactivează userul demo, ca să nu existe a doua intrare cunoscută public.
    3. Opțional creează o companie RO cu planul de conturi românesc și o pune implicită pe admin.
    """
    admin = env.ref("base.user_admin")
    admin.write({"password": cfg.ADMIN_PASSWORD})
    _logger.info("terrabit_demo: parola admin setată din demo_config")

    demo_user = env.ref("base.user_demo", raise_if_not_found=False)
    if demo_user:
        demo_user.write({"active": False})

    if cfg.RO_COMPANY_NAME:
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
        admin.write({"company_ids": [(4, company.id)], "company_id": company.id})
        if "account.chart.template" in env:
            env["account.chart.template"].try_loading("ro", company, install_demo=False)
            _logger.info("terrabit_demo: companie RO '%s' creată cu planul de conturi ro", company.name)
            # Seed-ul e opțional: dacă pică, instalarea (și parola admin) nu trebuie să pice cu el.
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
