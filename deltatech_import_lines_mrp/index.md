# Import Lines in Manufacturing Orders

- **Nume Tehnic:** `deltatech_import_lines_mrp`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_import_lines_mrp
- **Cale Locală:** `odoo-addons/deltatech/deltatech_import_lines_mrp`
- **Ultima Ingestie:** `2026-10-27`

#### 1. Sumar

Modulul permite încărcarea componentelor unui ordin de producție dintr-un fișier (XLSX, XLS, CSV sau TXT), în loc de adăugarea lor manuală, rând cu rând. Se instalează automat când sunt prezente atât Producția, cât și modulul `deltatech_import_lines`, și economisește timp la ordinele de producție cu liste lungi de componente.

#### 2. Funcționalități Cheie

- Buton **Import Components** în antetul ordinului de producție, vizibil doar în stările Ciornă și Confirmat; deschide wizardul din [deltatech_import_lines](../deltatech_import_lines/index.md).
- În wizard se alege fișierul, se mapează coloanele de produs și cantitate (opțional și unitatea de măsură), se apasă **Preview**, apoi **Import**.
- Fiecare rând devine o mișcare de componentă, pregătită ca o componentă adăugată manual (locații, operație, metodă de aprovizionare).
- Pe un ordin confirmat, componentele noi sunt confirmate la import.
- Produsul care se fabrică nu poate fi importat drept propria componentă (rândul este respins cu mesaj).
- Sunt acceptate doar produse de tip consumabil (`consu`); unitatea de măsură implicită este cea a produsului, dacă lipsește din fișier.
- Importul este refuzat pentru ordinele aflate în alte stări decât Ciornă sau Confirmat.

#### 3. Dependențe

- [deltatech_import_lines](../deltatech_import_lines/index.md)
- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins, cu mixinul `import.lines.mixin`): definește câmpurile țintă ale importului (produs, cantitate, UM), verificarea stării, domeniul produselor, validarea rândurilor și crearea mișcărilor `move_raw_ids`.

**Vizualizări**

- `mrp_production_form_view`: moștenește formularul `mrp.mrp_production_form_view` și adaugă butonul **Import Components**.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_import_lines](../deltatech_import_lines/index.md): oferă wizardul și mixinul generic de import, folosite aici pentru ordinele de producție.
