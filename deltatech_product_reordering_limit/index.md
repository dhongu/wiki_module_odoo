# Product Reordering Limits (localizat la `deltatech_product_reordering_limit/index.md`)

- **Nume Tehnic:** `deltatech_product_reordering_limit`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_reordering_limit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_reordering_limit`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul introduce un mod simplificat de a gestiona pragurile de reaprovizionare a stocului direct pe fișa articolului (produsului) în Odoo. Este gândit pentru gestionarii de stoc care au nevoie de un minim și un maxim global valabil pentru întregul produs (inclusiv toate variantele sale), fără complexitatea regulilor de reaprovizionare individuale pe fiecare locație/depozit.

#### 2. Funcționalități Cheie

- Adaugă câmpurile **Total Minimum** și **Total Maximum** pe fișa produsului (în secțiunea de limite de reaprovizionare, din **Inventar > Produse > Produse**), aplicabile întregului articol, inclusiv variantelor.
- Calculează automat dacă un produs este **Sub Minim** (Below Minimum), pe baza cantității totale disponibile în toate locațiile interne de stoc.
- Adaugă un filtru de căutare dedicat („Below Minimum") în lista de produse, pentru identificarea rapidă a articolelor care necesită reaprovizionare.
- Oferă un raport Excel (generat printr-un wizard din meniul Acțiuni al listei de produse) cu produsele selectate: cantitatea sub minim, cantitatea necesară până la maxim și intervalul minim-maxim. Decizia de comandă rămâne la utilizator; modulul nu creează comenzi.

#### 3. Dependențe

- `product`
- `stock`

Dependență externă Python: `xlsxwriter`.

#### 4. Componente Cheie

**Modele**

- `product.template` (extindere): câmpurile `total_minimum` și `total_maximum` (Float), câmpul calculat `is_below_min` (Boolean, cu logică de căutare proprie `_search_is_below_min`, care agregă cantitățile din `stock_quant` pentru locațiile interne).
- `product.reordering.report.wizard` (`TransientModel`): wizard care generează raportul Excel (`xlsxwriter`) pentru produsele selectate; fără selecție ridică o eroare clară.

**Vizualizări**

- `product_template_form_view`: adaugă `total_minimum` și `total_maximum` în formularul de produs.
- `product_template_search_view`: adaugă filtrul **Below Minimum**.
- `product_reordering_report_wizard_view_form`: formularul wizard-ului, cu buton de generare și fișierul rezultat.

**Acțiuni Automate / Acțiuni Server**

- `action_product_reordering_report_wizard`: acțiune de fereastră legată de `product.template`, disponibilă din lista de produse, care deschide wizard-ul de raport.

Acces: wizard-ul este permis grupului `base.group_user` prin `security/ir.access.csv`.

#### 5. Conexiuni

- `product`: extinde direct modelul de bază al produsului.
- `stock`: folosește `stock_quant` și locațiile interne pentru calculul cantității disponibile.
