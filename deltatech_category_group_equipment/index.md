# Equipment Category Group (localizat la `deltatech_category_group_equipment/index.md`)

- **Nume Tehnic:** `deltatech_category_group_equipment`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_category_group_equipment
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_category_group_equipment`
- **Ultima Ingestie:** `2026-11-02`

#### 1. Sumar

Modulul adaugă elemente de grupare pentru echipamente, preluate din grupurile definite pe categoria internă a produsului asociat echipamentului. Astfel, echipamentele pot fi organizate și filtrate după „tipul categoriei" și „clasa categoriei", facilitând clasificarea și raportarea parcului de echipamente în mod consecvent cu categoriile de produse.

#### 2. Funcționalități Cheie

- Adaugă două elemente de grupare pentru echipamente: „tipul categoriei" (Category type) și „clasa categoriei" (Category class), legate de categoria internă a produsului echipamentului.
- Filtre și grupări suplimentare în ecranul de echipamente (grupare după *Category Type* și *Category Class*), astfel încât un tehnician găsește mai repede echipamentele unei categorii.
- Coloanele și câmpurile de căutare pentru tip și clasă sunt ascunse implicit și se pot afișa din selectorul de coloane.

#### 3. Dependențe

- [deltatech_category_group](../deltatech_category_group/index.md)
- [deltatech_service_equipment](../deltatech_service_equipment/index.md)

#### 4. Componente Cheie

**Modele**

- `service.equipment`: extins cu `category_group_type` și `category_group_class`, câmpuri `related` stocate, doar citire, preluate din categoria internă a produsului echipamentului (`product_id.categ_id`).

**Vizualizări**

- `equipment_category_group_list`: adaugă coloanele tip și clasă (opționale, ascunse implicit) în lista de echipamente.
- `view_service_equipment_filter`: adaugă câmpurile de căutare și grupările *Category Type* / *Category Class* în căutarea echipamentelor.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- [deltatech_category_group](../deltatech_category_group/index.md): furnizează grupurile de categorii (tip și clasă) pe care acest modul le propagă la nivel de echipament.
- [deltatech_service_equipment](../deltatech_service_equipment/index.md): definește modelul de echipamente extins de acest modul cu cele două elemente de grupare.
