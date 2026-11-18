# Product Reordering Limits (localizat la `deltatech_product_reordering_limit/index.md`)

- **Nume Tehnic:** `deltatech_product_reordering_limit`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_reordering_limit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_reordering_limit`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul introduce un mod simplificat de a gestiona pragurile de reaprovizionare a stocului direct pe fișa produsului. Este gândit pentru gestionarii de stoc care au nevoie de un minim și un maxim global valabil pentru întregul produs (inclusiv toate variantele), fără complexitatea regulilor de reaprovizionare individuale pe fiecare locație sau depozit.

#### 2. Funcționalități Cheie

- Adaugă câmpurile **Total Minimum** și **Total Maximum** direct pe fișa produsului (șablon de produs), aplicabile întregului articol, inclusiv variantelor.
- Calculează automat dacă un produs este **Below Minimum**, pe baza cantității totale disponibile în toate locațiile interne de stoc.
- Adaugă filtrul de căutare **Below Minimum** în lista de produse, pentru identificarea rapidă a articolelor care necesită reaprovizionare; informația se folosește apoi pentru a declanșa comenzi de achiziție sau de producție.
- Oferă un raport Excel (generat printr-un wizard) pentru produsele selectate, cu cantitatea sub minim, cantitatea necesară până la maxim și intervalul minim-maxim.
- Se folosește din **Inventory > Products > Products**, în secțiunea **Reordering Limits** a produsului.

#### 3. Dependențe

- `product`
- `stock`

Dependență externă Python: `xlsxwriter`.

#### 4. Componente Cheie

**Modele**

- `product.template` (extindere): câmpurile `total_minimum` și `total_maximum`, câmpul calculat `is_below_min` (căutare proprie `_search_is_below_min`, bazată pe agregarea cantităților din `stock_quant` pentru locațiile `internal`) și `_compute_is_below_min`, care compară `qty_available` cu `total_minimum`.
- `product.reordering.report.wizard` (`TransientModel`): generează raportul Excel (`xlsxwriter`) pentru produsele selectate din listă.

**Vizualizări**

- `product_template_form_view`: adaugă `total_minimum` și `total_maximum` pe formularul produsului.
- `product_template_search_view`: adaugă filtrul **Below Minimum** (`is_below_min = True`).
- `product_reordering_report_wizard_view_form`: formularul wizard-ului, cu butonul de generare a raportului Excel.

**Acțiuni Automate / Acțiuni Server**

- `action_product_reordering_report_wizard`: acțiune `ir.actions.act_window` legată (`binding_model_id`) de `product.template`, disponibilă din lista de produse, care deschide wizard-ul raportului de reaprovizionare.

#### 5. Conexiuni

- `product`: extinde modelul de bază al produsului.
- `stock`: folosește `stock_quant` și locațiile de stoc pentru calculul cantității disponibile.
