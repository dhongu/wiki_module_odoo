# Modul generat de scripts/demo_branch.py — există doar pe branch-ul de demo.
{
    "name": "Terrabit Demo - __CLIENT_NAME__",
    "summary": "Instanță de demo pentru __CLIENT_NAME__: __MODULES_HUMAN__",
    "version": "19.0.1.0.0",
    "author": "Terrabit",
    "website": "https://www.terrabit.ro",
    "license": "LGPL-3",
    "category": "Hidden",
    "depends": __DEPENDS__,
    "data": ["data/ir_cron.xml"],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "auto_install": False,
}
