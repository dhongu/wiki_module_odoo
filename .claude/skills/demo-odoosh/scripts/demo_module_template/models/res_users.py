import logging

from odoo import models
from odoo.exceptions import AccessDenied

from .. import demo_config as cfg

_logger = logging.getLogger(__name__)

MODULE = "__MODULE__"


class ResUsers(models.Model):
    _inherit = "res.users"

    def _terrabit_demo_enforce_password(self):
        """Rulat de cronul modulului, la fiecare minut, până când parola configurată e acceptată.

        odoo.sh rescrie parola admin DUPĂ instalarea modulelor pe build-urile de dev, deci
        `post_init_hook` singur nu e suficient. Cronul verifică, rescrie doar dacă e nevoie
        și se dezactivează la prima verificare reușită, ca să nu suprascrie o parolă
        schimbată ulterior de client.
        """
        admin = self.env.ref("base.user_admin").sudo()
        cron = self.env.ref(f"{MODULE}.cron_enforce_admin_password", raise_if_not_found=False)
        credential = {"type": "password", "login": admin.login, "password": cfg.ADMIN_PASSWORD}
        try:
            admin.with_user(admin).sudo()._check_credentials(credential, {"interactive": False})
        except AccessDenied:
            admin.write({"password": cfg.ADMIN_PASSWORD})
            _logger.info("terrabit_demo: parola admin a fost rescrisă (fusese schimbată după instalare)")
            return
        if cron:
            cron.sudo().write({"active": False})
            _logger.info("terrabit_demo: parola admin e cea configurată, cronul s-a dezactivat")
