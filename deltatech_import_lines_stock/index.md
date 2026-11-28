# Import Lines in Transfers and Inventory (localizat la `deltatech_import_lines_stock/index.md`)

- **Nume Tehnic:** `deltatech_import_lines_stock`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_import_lines_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_import_lines_stock`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Încarcă mișcările de stoc ale transferurilor și cantitățile numărate la inventar dintr-un fișier XLSX, XLS, CSV sau TXT, folosind asistentul din [deltatech_import_lines](../deltatech_import_lines/index.md). Se instalează automat când sunt prezente Inventarul și modulul de bază.

#### 2. Funcționalități Cheie

- **Transferuri** (recepții, livrări, transferuri interne): buton **Importă linii** pe transferurile nefinalizate și neanulate; fiecare rând devine o mișcare între locațiile transferului. Mișcările adăugate la un transfer confirmat sunt confirmate, iar Odoo le unește cu cele existente ale aceluiași produs.
- **Loturi și numere de serie**: coloana **Lot/Serie** setează lotul rândului. Pe recepțiile al căror tip de operațiune permite loturi noi, lotul inexistent se creează la validare; la celelalte operațiuni lotul trebuie să existe. Un număr de serie cere cantitatea 1.
- **Numărători de inventar**: butonul **Importă numărători** din *Inventar > Operațiuni > Inventar fizic* setează cantitatea numărată pentru produse (și loturi) în locația aleasă; rândurile cu același produs și lot se adună. Un produs urmărit pe lot/serie cere un lot existent. Numărătoarea se aplică de utilizator, cu **Aplică** sau **Aplică tot**.
- Fluxul pas cu pas e în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_import_lines](../deltatech_import_lines/index.md)
- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking`, `stock.quant`: extinse cu `import.lines.mixin` pentru importul de linii și de numărători.
- `import.lines.wizard`: extins cu logica specifică stocurilor (loturi, locație numărată).

**Vizualizări**

- `views/stock_picking_view.xml`: butonul **Importă linii** pe transferuri.
- `views/stock_quant_view.xml`: butonul **Importă numărători** pe inventarul fizic.
- `wizard/import_lines_wizard_view.xml`: câmpurile suplimentare ale asistentului (locația numărată).

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_import_lines](../deltatech_import_lines/index.md): oferă asistentul și mapările salvate.
