# Import Lines in Sale Orders (localizat la `deltatech_import_lines_sale/index.md`)

- **Nume Tehnic:** `deltatech_import_lines_sale`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_import_lines_sale
- **Cale Locală:** `odoo-addons/deltatech/deltatech_import_lines_sale`
- **Ultima Ingestie:** `2026-10-27`

#### 1. Sumar

Modulul adaugă pe ofertele de vânzare butonul **Import Lines**, care încarcă liniile comenzii dintr-un fișier (XLSX, XLS, CSV sau TXT), folosind asistentul din [deltatech_import_lines](../deltatech_import_lines/index.md). Se instalează automat când sunt prezente atât Vânzările, cât și `deltatech_import_lines`, iar utilizatorul nu mai introduce manual sute de linii de ofertă.

#### 2. Funcționalități Cheie

- Butonul **Import Lines** apare doar pe ofertele în stările ciornă și trimisă. Comenzile confirmate nu pot primi linii importate, iar o încercare forțată dă eroare.
- Fluxul: se deschide oferta, se apasă **Import Lines**, se alege fișierul și se mapează coloanele (produs și cantitate obligatorii; opțional preț unitar, discount, unitate de măsură și descriere). Apoi **Preview**, verificarea rândurilor și **Import**.
- Se potrivesc doar produsele care pot fi vândute.
- Prețul unitar, taxele și descrierea vin din lista de prețuri și din produs, ca la o linie adăugată manual. Dacă în fișier sunt mapate coloanele **Unit Price** sau **Discount**, valorile din fișier le înlocuiesc.
- Unitatea de măsură din fișier trebuie să fie înrudită cu cea a produsului.
- Meniu pentru configurarea mapărilor salvate: Vânzări > Configurare > mapări de import (sub `sale.menu_sale_config`).
- Partenerul și compania comenzii sunt folosite în contextul importului.

#### 3. Dependențe

- [deltatech_import_lines](../deltatech_import_lines/index.md)
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): moștenește `import.lines.mixin`; verifică starea (doar `draft`/`sent`), adaugă țintele `price_unit` și `discount`, filtrează produsele după `sale_ok` și creează liniile `sale.order.line` (cantitate, unitate, preț, discount, descriere).

**Vizualizări**

- `view_order_form` (moștenește `sale.view_order_form`): butonul **Import Lines** în antet, vizibil doar în `draft` și `sent`.
- `menu_import_lines_mapping`: meniu în Vânzări > Configurare către mapările de import.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_import_lines](../deltatech_import_lines/index.md): oferă asistentul, mixinul și mapările pe care le folosește acest modul.
