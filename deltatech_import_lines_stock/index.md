# Import linii în transferuri și inventar fizic (localizat la `deltatech_import_lines_stock/index.md`)

- **Nume Tehnic:** `deltatech_import_lines_stock`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_import_lines_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_import_lines_stock`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă dintr-un fișier (XLSX, XLS, CSV sau TXT) liniile transferurilor de stoc și cantitățile numărate la inventar, folosind asistentul de import din [deltatech_import_lines](../deltatech_import_lines/index.md). Gestionarul nu mai introduce manual, rând cu rând, avizul furnizorului sau lista de numărătoare din Excel, iar produsele, loturile și numerele de serie sunt verificate înainte de import. Se instalează automat când sunt prezente Inventarul și `deltatech_import_lines`.

#### 2. Funcționalități Cheie

- **Transferuri** (recepții, livrări, transferuri interne): buton **Import linii** pe transferurile nefinalizate și neanulate. Fiecare rând devine o mișcare între locațiile transferului; mișcările adăugate la un transfer confirmat sunt confirmate, iar Odoo le unește cu cele existente ale aceluiași produs.
- **Loturi și numere de serie**: o coloană **Lot/Număr de serie** setează lotul rândului. Pe recepțiile al căror tip de operațiune permite loturi noi, lotul inexistent se creează la validare; pe celelalte operațiuni lotul trebuie să existe. Un număr de serie are cantitatea 1 și nu se repetă.
- **Inventar fizic**: buton **Import cantități numărate** în **Inventar → Operațiuni → Inventariere fizică**; completează cantitatea numărată (**Faptic**) pe produs și lot, în **Locația inventariată** aleasă în asistent (implicit stocul primului depozit). Rândurile aceluiași produs și lot se adună; un produs urmărit are nevoie de un lot existent; cantitatea 0 este acceptată.
- Importul doar pregătește documentul: recepția se validează și numărătoarea se aplică de utilizator (**Aplică** / **Aplică tot**), ca în fluxul standard. Nu se generează note contabile proprii.
- Fluxul detaliat pas-cu-pas, mesajele de eroare frecvente și verificările rămân în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_import_lines](../deltatech_import_lines/index.md)
- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins, cu `import.lines.mixin`): validarea rândurilor (produs, lot, serie) și crearea mișcărilor din fișier.
- `stock.quant` (extins, cu `import.lines.mixin`): validarea rândurilor și setarea cantităților numărate în inventarul fizic.
- `import.lines.wizard` (extins): câmpul pentru locația inventariată și valorile implicite pentru stoc.
- `lot_lookup` (funcții utilitare, nu model): căutarea loturilor după nume și detectarea numerelor de serie duplicate.

**Vizualizări**

- `view_picking_form`: adaugă butonul **Import linii** pe formularul transferului.
- `view_stock_quant_tree_inventory_editable`: adaugă butonul **Import cantități numărate** pe lista inventarului fizic.
- `import_lines_wizard_form`: extinde asistentul cu locația inventariată.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_import_lines](../deltatech_import_lines/index.md): asistentul de import, citirea fișierului, maparea coloanelor și previzualizarea; modulul de față este puntea către stoc.
