# Referrer Commission Report (localizat la `deltatech_sale_referrer_raport/index.md`)

- **Nume Tehnic:** `deltatech_sale_referrer_raport`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_referrer_raport
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_referrer_raport`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde funcționalitatea de vânzări cu urmărirea și raportarea comisioanelor pentru recomandatori (referrer). Calculează automat comisionul pe liniile comenzii de vânzare, în funcție de planul de comision ales, oferă vizibilitate rapidă asupra vânzărilor generate de fiecare partener recomandator, urmărește dacă respectivul comision a fost plătit și îl integrează în raportul de Analiză Vânzări.

#### 2. Funcționalități Cheie

- **Calcul de comision:** comisionul se calculează automat pe liniile comenzii, pe baza planului de comision. Cât timp documentul e ofertă, **Commission Plan** se preia de la recomandator (câmpul **Referrer**, sub client); **Referrer Commission** apare sub totaluri și urmărește liniile comenzii. Un recomandator are nevoie de un **Partner Level** ca să poată fi ales pe o comandă.
- **Vânzările unui recomandator:** pe fișa partenerului, butonul inteligent **Referrer Sales** (pictogramă USD) deschide toate ofertele și comenzile cu acel partener ca recomandator.
- **Stare de plată a comisionului:** doar un Sales Administrator poate marca comisionul ca plătit (butonul **Pay**, doar pe comenzi confirmate) sau îl poate readuce la neplătit (**Reset to Unpaid**); vânzătorii văd coloana **Paid**, dar nu butoanele. Filtrul **Commission to Pay** (*Sales > Orders > Orders*) listează comenzile confirmate cu comisionul încă nemarcat ca plătit.
- **Comision plătit = înghețat:** după marcarea ca plătit, modificarea liniilor nu mai schimbă comisionul, iar **Referrer** și **Commission Plan** devin doar-citire până la resetarea la neplătit.
- **Raportare:** în *Sales > Reporting > Sales* (vizualizare pivot) se alege măsura **Referrer Commission** și se grupează după **Referrer**. Comisionul se însumează pe liniile comenzii și se convertește în moneda companiei, ca măsurile monetare standard, deci comenzile în valută sunt comparabile. Un plafon (regulă cu plafon) se aplică pe totalul regulii, ca pe comandă.
- **Note de credit:** o notă de credit creată din comanda de vânzare (marfă returnată, cantitate mai mică) preia înapoi comisionul pe comanda de achiziție de comision, după ce e plătită, ca în cazul unei note de credit care stornează o factură.
- **Comanda de achiziție de comision:** suma facturată de recomandator provine din comanda de achiziție de comision din aplicația **Partner Commissions**: fiecare factură client plătită adaugă linia ei de comision, iar fiecare notă de credit plătită o scade. Indicatorul **Paid** e doar un marcaj intern: nu creează o plată, iar comisionul se decontează prin factura de furnizor a recomandatorului.
- Informațiile de comision din comenzile de vânzare se transmit către facturile generate.

#### 3. Dependențe

- `sale_management`
- `website_crm_partner_assign`
- `partner_commission`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): câmpurile `commission` (monetar, stocat) și `referrer_is_paid` (bifă de plată, nu se copiază); suprascrie `_compute_commission()` pentru a calcula comisionul pe fiecare linie conform regulilor planului (`commission_plan_id`), cu plafonare pe totalul regulii (`is_capped`/`max_commission`, repartizată proporțional pe linii) și cu comision înghețat la comenzile plătite; `create`/`write` verifică accesul de Sales Administrator pentru `referrer_is_paid` și blochează schimbarea recomandatorului sau a planului la un comision plătit; `action_set_referrer_paid()` și `action_reset_referrer_unpaid()` marchează comisionul ca plătit, respectiv neplătit.
- `sale.order.line` (extindere): câmpul `line_commission` (comisionul calculat pe linie).
- `account.move` (extindere): `_invoice_paid_hook()` creează comisionul de stornare (`_make_commission()`) pentru o notă de credit plătită, creată din comandă și nelegată de o factură stornată, când comanda a câștigat deja comision; reia stornarea unei note de credit plătite înaintea facturii, după ce factura câștigă comision.
- `res.partner` (extindere): câmpul calculat `sale_order_commission_count` și acțiunea `action_view_referrer_sales()` care deschide comenzile unde partenerul este recomandator.
- `sale.report` (extindere): `referrer_id` și `referrer_commission` în analiza vânzărilor, pentru grupare și măsurători pe recomandator.

**Vizualizări**

- `view_partner_form_inherit_referrer`: butonul inteligent „Referrer Sales” pe fișa partenerului.
- `view_order_list_inherit` / `view_quotation_list_inherit`: coloana `commission` (cu total) în listele de comenzi și oferte.
- `view_order_tree_referrer`: lista comenzilor unui recomandator.
- `view_sale_order_tree_inherit_commission`: butoanele „Pay” / „Reset to Unpaid” și câmpul `referrer_is_paid` în listă, vizibile doar în contextul `show_referrer_paid`.
- `sale_order_form_inherit_referrer_paid`: bifa **Commission Paid** pe formularul comenzii.
- `view_sales_order_filter_inherit_referrer`: filtrul „Commission to Pay”.
- `act_res_partner_2_sale_order_referrer`: acțiune fereastră „Quotations and Sales” pentru comenzile unui recomandator, cu contextul `show_referrer_paid`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `sale_management`: modulul extinde direct modelele de vânzări (comandă, linie) definite aici.
- `website_crm_partner_assign`: furnizează conceptul de partener recomandator (referrer) și nivelul de partener.
- `partner_commission`: furnizează planurile de comision (`commission_plan_id`), regulile de calcul (`_match_rules`) și comanda de achiziție de comision (aplicația Partner Commissions).
