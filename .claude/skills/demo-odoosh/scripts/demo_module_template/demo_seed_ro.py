"""Seed de date românești pentru compania de demo creată cu `--ro`.

Rulează din `post_init_hook`, după încărcarea planului de conturi `ro`. Creează parteneri cu CUI valid,
produse, facturi de vânzare și de achiziție postate (o parte încasate/plătite), ca modulele fiscale
și de export contabil să aibă ce arăta. Totul e în RON, cu TVA 21% și 11%, pe ultimele două luni.
"""
import logging
from datetime import date, timedelta

_logger = logging.getLogger(__name__)


def _cui(base):
    """Completează un CUI românesc cu cifra de control (algoritmul ANAF: ponderi 753217532)."""
    digits = [int(d) for d in str(base).rjust(9, "0")]
    total = sum(d * w for d, w in zip(digits, [7, 5, 3, 2, 1, 7, 5, 3, 2]))
    check = (total * 10) % 11
    return f"{int(base)}{0 if check == 10 else check}"


PARTNERS = [
    # (nume, bază CUI, oraș, județ, client/furnizor)
    ("Agro Prod Vest SRL", 1234567, "Arad", "Arad", "customer"),
    ("Delta Comerț Impex SRL", 2345678, "Cluj-Napoca", "Cluj", "customer"),
    ("Mecanica Fină Brașov SA", 3456789, "Brașov", "Brașov", "customer"),
    ("Utilaje Agricole Distribuție SRL", 4567891, "Timișoara", "Timiș", "supplier"),
    ("Servicii Logistice Transilvania SRL", 5678912, "Sibiu", "Sibiu", "supplier"),
]

PRODUCTS = [
    # (nume, tip, preț vânzare, cost, cotă TVA)
    ("Filtru hidraulic HF-6177", "consu", 185.0, 120.0, 21),
    ("Set curele transmisie B-1250", "consu", 96.0, 58.0, 21),
    ("Ulei hidraulic HLP 46, bidon 20 l", "consu", 410.0, 290.0, 21),
    ("Manual tehnic utilaje (tipărit)", "consu", 45.0, 20.0, 11),
    ("Servicii montaj și punere în funcțiune", "service", 350.0, 250.0, 21),
]


def _tax(env, company, xmlid):
    return env["account.chart.template"].with_company(company).ref(xmlid, raise_if_not_found=False)


def seed(env, company):
    env = env(context=dict(env.context, allowed_company_ids=company.ids, tracking_disable=True))
    ro = env.ref("base.ro")
    ct = env["account.chart.template"].with_company(company)
    taxes = {
        ("sale", 21): _tax(env, company, "tvac_21"),
        ("sale", 11): _tax(env, company, "tvac_11"),
        ("purchase", 21): _tax(env, company, "tvad_21"),
        ("purchase", 11): _tax(env, company, "tvad_11"),
    }
    if not all(taxes.values()):
        _logger.warning("terrabit_demo: taxele RO nu au fost găsite (%s); seed-ul de facturi e sărit", taxes)
        return

    partners = {}
    for name, base, city, county, role in PARTNERS:
        state = env["res.country.state"].search([("country_id", "=", ro.id), ("name", "=", county)], limit=1)
        partners[name] = env["res.partner"].create(
            {
                "name": name,
                "is_company": True,
                "vat": f"RO{_cui(base)}",
                "company_registry": f"J{base % 40 + 1:02d}/{base % 9000 + 100}/2015",
                "street": f"Str. Industriilor nr. {base % 90 + 1}",
                "city": city,
                "state_id": state.id,
                "country_id": ro.id,
                "email": f"office@{name.split()[0].lower()}-demo.ro",
                "customer_rank": 1 if role == "customer" else 0,
                "supplier_rank": 1 if role == "supplier" else 0,
            }
        )

    products = []
    for name, ptype, price, cost, rate in PRODUCTS:
        products.append(
            env["product.product"].with_company(company).create(
                {
                    "name": name,
                    "type": ptype,
                    "list_price": price,
                    "standard_price": cost,
                    "taxes_id": [(6, 0, taxes[("sale", rate)].ids)],
                    "supplier_taxes_id": [(6, 0, taxes[("purchase", rate)].ids)],
                }
            )
        )

    today = date.today()
    customers = [p for (n, _b, _c, _j, r) in PARTNERS if r == "customer" for p in [partners[n]]]
    suppliers = [p for (n, _b, _c, _j, r) in PARTNERS if r == "supplier" for p in [partners[n]]]

    # (tip, index partener, zile în urmă, [(index produs, cantitate)], plătită?)
    plan = [
        ("out_invoice", 0, 52, [(0, 4), (2, 2)], True),
        ("out_invoice", 1, 45, [(1, 10), (3, 3)], True),
        ("out_invoice", 2, 38, [(4, 1), (0, 2)], True),
        ("out_invoice", 0, 24, [(2, 5)], False),
        ("out_invoice", 1, 12, [(0, 6), (1, 4), (3, 1)], False),
        ("out_invoice", 2, 4, [(4, 2)], False),
        ("in_invoice", 0, 50, [(0, 20), (1, 30)], True),
        ("in_invoice", 1, 33, [(4, 1)], True),
        ("in_invoice", 0, 18, [(2, 12)], False),
        ("in_invoice", 1, 6, [(4, 2)], False),
    ]
    moves = env["account.move"]
    for mtype, pidx, days_ago, lines, paid in plan:
        partner = (customers if mtype == "out_invoice" else suppliers)[pidx]
        inv_date = today - timedelta(days=days_ago)
        vals = {
            "move_type": mtype,
            "partner_id": partner.id,
            "invoice_date": inv_date,
            "date": inv_date,
            "invoice_line_ids": [
                (0, 0, {"product_id": products[i].id, "quantity": qty}) for i, qty in lines
            ],
        }
        if mtype == "in_invoice":
            vals["ref"] = f"FF-{inv_date:%y%m}-{pidx + 1:03d}"
        move = moves.with_company(company).create(vals)
        if not move.amount_total:
            raise ValueError(f"factura de seed {mtype} pentru {partner.name} are total 0; verifică prețurile produselor")
        move.action_post()
        moves |= move
        if paid:
            env["account.payment.register"].with_company(company).with_context(
                active_model="account.move", active_ids=move.ids
            ).create({"payment_date": inv_date + timedelta(days=7)})._create_payments()

    _logger.info(
        "terrabit_demo: seed RO pe '%s': %d parteneri, %d produse, %d facturi (%d încasate/plătite)",
        company.name, len(partners), len(products), len(moves), sum(1 for p in plan if p[4]),
    )
