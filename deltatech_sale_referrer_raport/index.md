# Sale Referrer Report (localizat la `deltatech_sale_referrer_raport/index.md`)

- **Nume Tehnic:** `deltatech_sale_referrer_raport`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_referrer_raport
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_referrer_raport`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul extinde funcționalitatea de vânzări cu urmărirea și raportarea comisioanelor pentru recomandatori (referrer). Permite calcularea automată a comisionului pe liniile comenzii de vânzare, în funcție de planul de comision ales, oferă vizibilitate rapidă asupra vânzărilor generate de fiecare partener recomandator și urmărește dacă respectivul comision a fost plătit.

#### 2. Funcționalități Cheie

- Calculează automat comisioanele pe liniile comenzii de vânzare, pe baza planului de comision selectat.
- Adaugă un buton inteligent pe fișa partenerului pentru a vizualiza rapid toate comenzile de vânzare unde acel partener este recomandator (referrer).
- Permite urmărirea stării de plată a comisionului de recomandare pentru fiecare comandă de vânzare.
- Integrează informațiile despre recomandator și valoarea comisionului în raportul de Analiză Vânzări.
- Transmite informațiile despre comision din comenzile de vânzare către facturile generate.

#### 3. Dependențe

- `sale_management`
- `website_crm_partner_assign`
- `partner_commission`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): adaugă câmpurile `commission` (comision total, monetary) și `referrer_is_paid` (bifă plată comision); suprascrie `_compute_commission()` pentru a calcula comisionul pe fiecare linie conform regulilor planului de comision (`commission_plan_id`), inclusiv plafonare (`is_capped`/`max_commission`); suprascrie `_prepare_invoice()` pentru a propaga `commission_po_line_id` către factură; expune `action_set_referrer_paid()` pentru marcarea comisionului ca plătit.
- `sale.order.line` (extindere): adaugă câmpul `line_commission` (comisionul calculat pe linie).
- `res.partner` (extindere): adaugă câmpul calculat `sale_order_commission_count` și acțiunea `action_view_referrer_sales()` care deschide lista comenzilor unde partenerul este recomandator.
- `sale.report` (extindere): adaugă `referrer_id` și `referrer_commission` în raportul de analiză vânzări, pentru grupare și măsurători pe recomandator.

**Vizualizări**

- `view_partner_form_inherit_referrer`: adaugă pe fișa partenerului butonul inteligent "Referrer Sales" (icon USD) cu numărul de comenzi unde e recomandator.
- `view_order_list_inherit` / `view_quotation_list_inherit`: adaugă coloana `commission` (cu total) în listele de comenzi și oferte.
- `act_res_partner_2_sale_order_referrer`: acțiune fereastră care afișează comenzile/ofertele unui recomandator, cu contextul `show_referrer_paid`.
- `view_sale_order_tree_inherit_commission`: adaugă în listă butonul "Pay" (`action_set_referrer_paid`) și câmpul `referrer_is_paid`, vizibile doar în contextul `show_referrer_paid`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `sale_management`: modulul extinde direct modelele de vânzări (comandă, linie) definite aici.
- `website_crm_partner_assign`: furnizează conceptul de partener recomandator (referrer) folosit pentru calculul comisionului.
- `partner_commission`: furnizează planurile de comision (`commission_plan_id`) și regulile de calcul (`_match_rules`) pe care le utilizează modulul.
