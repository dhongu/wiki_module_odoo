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
