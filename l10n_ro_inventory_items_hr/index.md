# Romania - Obiecte de inventar pe salariat (localizat la `l10n_ro_inventory_items_hr/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_items_hr`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_inventory_items_hr
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_items_hr`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul extinde obiectele de inventar cu darea în folosință pe salariat (`hr.employee`), nu doar pe un utilizator Odoo. Astfel, și salariații care nu au cont în Odoo pot primi obiecte de inventar, iar bonul de dare în folosință se tipărește cu numele salariatului. Modulul se instalează explicit, pentru ca actualizarea modulului de bază să nu instaleze aplicația Angajați la firmele care nu o folosesc.

#### 2. Funcționalități Cheie

- Câmpul **Salariat** pe fișa obiectului de inventar, în listă și în căutare; lista poate fi filtrată și grupată după salariat.
- Câmpul **Salariat** în wizardul de dare în folosință (lot), de la Inventar → Obiecte de inventar → **Dare în folosință (lot)**; dacă salariatul are utilizator Odoo, acesta devine și responsabilul.
- Bonul de dare în folosință, PV-ul de scoatere din gestiune și Registrul obiectelor de inventar afișează salariatul; registrul grupează pe salariat, cu subtotal.
- La scoaterea din gestiune cu lipsă imputată salariatului, partenerul pentru contul 4282 se completează automat cu contactul de serviciu al salariatului (dacă toate obiectele selectate aparțin aceluiași salariat).

#### 3. Dependențe

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md)
- `hr`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.inventory.item` (extins): adaugă `employee_id` (`hr.employee`, urmărit, verificare companie); `onchange` care preia utilizatorul salariatului; `_get_holder_name` întoarce numele salariatului.
- `l10n.ro.inventory.item.use.wizard` (extins): câmpul `employee_id`; la confirmare scrie salariatul pe fișe și setează responsabilul.
- `l10n.ro.inventory.item.dispose.wizard` (extins): precompletează partenerul imputat din contactul salariatului.

**Vizualizări**

- `view_l10n_ro_inventory_item_form_hr`, `view_l10n_ro_inventory_item_list_hr`, `view_l10n_ro_inventory_item_search_hr`: câmpul Salariat în formular, listă, căutare/grupare.
- `view_l10n_ro_inventory_item_use_wizard_form_hr`: câmpul Salariat în wizardul de dare în folosință.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): modulul de bază extins (obiecte de inventar, bon, PV, registru).
