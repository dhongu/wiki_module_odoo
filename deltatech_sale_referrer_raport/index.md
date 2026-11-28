# Referrer Commission Report (localizat la `deltatech_sale_referrer_raport/index.md`)

- **Nume Tehnic:** `deltatech_sale_referrer_raport`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_sale_referrer_raport
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_referrer_raport`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde vânzările cu urmărirea și raportarea comisioanelor pentru recomandatori (referrer). Calculează comisionul pe liniile comenzii de vânzare după planul de comision ales, arată rapid vânzările generate de fiecare recomandator și urmărește dacă respectivul comision a fost plătit.

#### 2. Funcționalități Cheie

- Calculează automat comisionul pe liniile comenzii, după planul de comision; cât timp documentul este ofertă, planul este preluat de la recomandator.
- Buton inteligent **Referrer Sales** pe fișa partenerului, cu toate comenzile în care acesta este recomandator; pentru a putea fi ales pe o comandă, recomandatorul are nevoie de un nivel de partener.
- Stare de plată a comisionului pe comandă: doar Administratorul de vânzări o marchează plătită (**Pay**) sau o resetează (**Reset to Unpaid**); comisionul plătit este înghețat, iar recomandatorul și planul devin doar citire. Marcajul este intern și nu creează o plată; comisionul se decontează prin factura furnizor a recomandatorului.
- Filtrul **Commission to Pay** (**Vânzări > Comenzi > Comenzi**) listează comenzile confirmate cu comision neplătit.
- Raportul Analiză Vânzări include recomandatorul și comisionul, însumat pe liniile comenzii și convertit în moneda companiei, ca restul coloanelor monetare.
- Nota de credit creată din comandă (bunuri returnate, cantitate redusă) retrage comisionul de pe comanda de achiziție a comisionului, la fel ca nota de credit care inversează o factură. Suma facturată de recomandator vine din comanda de achiziție a comisionului din aplicația Partner Commissions.

Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_management`
- `website_crm_partner_assign`
- `partner_commission`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): câmpurile `commission` și `referrer_is_paid`; `_compute_commission()` calculează comisionul pe linii după regulile planului; `action_set_referrer_paid()` / `action_reset_referrer_unpaid()`; `_check_referrer_paid_access()` restricționează marcarea la Administratorul de vânzări; `create` / `write` blochează modificarea comisionului plătit.
- `sale.order.line` (extins): `line_commission`, comisionul pe linie.
- `res.partner` (extins): `sale_order_commission_count` și `action_view_referrer_sales()`.
- `account.move` (extins): `_invoice_paid_hook()` pentru comisionul la plata facturii.
- `sale.report` (extins): `referrer_id` și `referrer_commission` în Analiza Vânzări.

**Vizualizări**

- `view_partner_form_inherit_referrer`: butonul inteligent „Referrer Sales" pe partener.
- `view_order_list_inherit` / `view_quotation_list_inherit` / `view_order_tree_referrer`: coloana de comision în liste.
- `view_sale_order_tree_inherit_commission`: butoanele Pay / Reset și coloana Paid, în contextul `show_referrer_paid`.
- `sale_order_form_inherit_referrer_paid`: câmpul de plată pe comandă.
- `view_sales_order_filter_inherit_referrer`: filtrul Commission to Pay.
- `act_res_partner_2_sale_order_referrer`: acțiunea cu comenzile unui recomandator.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `sale_management`: comanda și linia de vânzare extinse.
- `website_crm_partner_assign`: conceptul de partener recomandator și nivelul de partener.
- `partner_commission`: planurile de comision, regulile de calcul și comanda de achiziție a comisionului.
