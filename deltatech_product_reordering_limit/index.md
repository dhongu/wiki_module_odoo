# Product Reordering Limit (localizat la `deltatech_product_reordering_limit/index.md`)

- **Nume Tehnic:** `deltatech_product_reordering_limit`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_reordering_limit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_reordering_limit`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul introduce un mod simplificat de a gestiona pragurile de reaprovizionare a stocului direct pe fișa articolului (produsului) în Odoo. Este gândit pentru gestionarii de stoc care au nevoie de un minim și un maxim global valabil pentru întregul produs (inclusiv toate variantele sale), fără complexitatea regulilor de reaprovizionare individuale pe fiecare locație/depozit.

#### 2. Funcționalități Cheie

- Adaugă câmpurile **Total Minimum** și **Total Maximum** direct pe fișa produsului (șablon de produs), aplicabile la nivelul întregului articol, inclusiv toate variantele.
- Calculează automat dacă un produs este **Sub Minim** (Below Minimum), pe baza cantității totale disponibile în toate locațiile interne de stoc.
- Adaugă un filtru de căutare dedicat („Below Minimum") în lista de produse, pentru identificarea rapidă a articolelor care necesită reaprovizionare.
- Oferă un raport Excel (generat printr-un wizard) cu produsele selectate, indicând cantitatea sub minim, cantitatea necesară până la maxim și intervalul minim-maxim definit.

#### 3. Dependențe

- `product`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.template` (extindere): adaugă câmpurile `total_minimum` și `total_maximum` (Float), câmpul calculat `is_below_min` (Boolean, cu logică de căutare proprie `_search_is_below_min` bazată pe o interogare SQL care agregă cantitățile din `stock_quant` pentru locațiile de tip `internal`), și metoda de calcul `_compute_is_below_min` care compară `qty_available` cu `total_minimum`.
- `product.reordering.report.wizard` (`TransientModel`): wizard care generează un raport Excel (`xlsxwriter`) cu produsele selectate din lista de articole — coloane Cod, Nume, Cantitate sub minim, Cantitate necesară și Interval minim-maxim.

**Vizualizări**

- `product_template_form_view`: adaugă câmpurile `total_minimum` și `total_maximum` în grupul general al formularului de produs.
- `product_template_search_view`: adaugă filtrul de căutare **Below Minimum** (`is_below_min = True`) în vizualizarea de căutare a produselor.
- `product_reordering_report_wizard_view_form`: formularul wizard-ului, cu buton de generare a raportului Excel și afișarea fișierului rezultat.

**Acțiuni Automate / Acțiuni Server**

- `action_product_reordering_report_wizard`: acțiune `ir.actions.act_window` legată (`binding_model_id`) de `product.template`, disponibilă din vizualizarea listă de produse, care deschide wizard-ul de generare a raportului de reaprovizionare.

#### 5. Conexiuni

- `product`: extinde direct modelul de bază al produsului.
- `stock`: folosește `stock_quant` și `stock_location` pentru calculul cantității disponibile în locațiile interne.
