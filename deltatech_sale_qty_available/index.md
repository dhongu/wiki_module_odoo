# Sale Qty Available (localizat la `deltatech_sale_qty_available/index.md`)

- **Nume Tehnic:** `deltatech_sale_qty_available`
- **Versiune:** `20.0.1.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_qty_available`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_qty_available`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul ajută echipa de vânzări să vadă rapid care comenzi pot fi livrate imediat, pe baza stocului disponibil. În lista de comenzi de vânzare, comenzile gata de livrare sunt evidențiate cu verde, iar pe formularul comenzii fiecare linie poate afișa o sinteză a disponibilității produsului. *readme/DESCRIPTION.md* este minimal, deci detaliile provin din manifest și cod.

#### 2. Funcționalități Cheie

- Evidențierea cu verde a comenzilor gata de livrare în listele de comenzi și de oferte.
- Indicator *Is ready*, calculat și stocat, în funcție de starea comenzii, starea de facturare, politica de livrare (directă sau completă) și stocul disponibil. Pentru comenzile confirmate se verifică suplimentar rezervarea pe transferurile de livrare.
- Filtrul *Is Ready* în căutarea comenzilor (în 20.0 a fost corectat: returna comenzile care nu sunt gata).
- Coloană opțională *Available* pe linia comenzii, plasată înaintea cantității, cu disponibilul virtual, stocul curent și ieșirile/intrările prognozate, calculate pe locația din ruta liniei, dacă există.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): câmpul `is_ready` (calculat, stocat, cu `_search_is_ready`).
- `sale.order.line` (extins): câmpul `qty_available_text`; `_compute_qty_at_date` ia în calcul toate depozitele.

**Vizualizări**

- `view_order_tree` și `view_quotation_tree`: decorare verde (`decoration-success`) pentru comenzile gata de livrare.
- `view_order_form`: coloana opțională `qty_available_text` pe liniile comenzii.
- `view_sales_order_filter`: filtrul *Is Ready*.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `sale_stock`: integrarea vânzări–stoc pe care se bazează calculul disponibilității și al rezervărilor.
