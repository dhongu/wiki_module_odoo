# Import Lines in Purchase Orders (localizat la `deltatech_import_lines_purchase/index.md`)

- **Nume Tehnic:** `deltatech_import_lines_purchase`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_import_lines_purchase
- **Cale Locală:** `odoo-addons/deltatech/deltatech_import_lines_purchase`
- **Ultima Ingestie:** `2026-10-27`

#### 1. Sumar

Adaugă pe cererile de ofertă (comenzi de achiziție în stadiul ciornă sau trimise) butonul **Import Lines**, care încarcă liniile comenzii dintr-un fișier XLSX, XLS, CSV sau TXT, folosind expertul din [deltatech_import_lines](../deltatech_import_lines/index.md). Produsele pot fi regăsite și după codul produsului la furnizor, ceea ce permite importul direct al ofertelor sau listelor primite de la furnizor. Se instalează automat când sunt instalate atât Achiziții, cât și `deltatech_import_lines`.

#### 2. Funcționalități Cheie

- Buton **Import Lines** în antetul cererii de ofertă, vizibil doar în stările ciornă și trimisă; în alte stări importul este refuzat.
- Fluxul de lucru: se deschide cererea de ofertă, se alege fișierul furnizorului, se mapează coloanele, se apasă **Preview**, se verifică rândurile și apoi **Import**.
- Potrivire suplimentară a produsului după **Vendor Product Code**: codul din lista de prețuri a furnizorului comenzii (sau a companiei sale comerciale), în compania comenzii. Opțiunea se alege în câmpul **Match Product By** (alături de referința internă, codul de bare și denumire).
- Sunt potrivite doar produsele care pot fi achiziționate.
- Prețul unitar provine din lista de prețuri a furnizorului, ca la o linie adăugată manual, cu excepția cazului în care fișierul are mapată o coloană **Unit Price** sau **Discount**.
- Maparea se poate salva **Only For This Partner**, pentru a fi propusă la următoarele fișiere ale aceluiași furnizor.
- Meniu **Achiziții > Configurare** pentru gestionarea mapărilor de import salvate.

#### 3. Dependențe

- [deltatech_import_lines](../deltatech_import_lines/index.md)
- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins, cu mixinul `import.lines.mixin`): permite importul doar în ciornă/trimisă; adaugă țintele `price_unit` și `discount`; furnizorul și compania vin din comandă; filtrează produsele cu `purchase_ok`; caută produse după codul furnizorului în `product.supplierinfo`; creează liniile comenzii din rândurile importate.
- `import.lines.wizard` (extins): adaugă opțiunea `vendor_code` în **Match Product By**.
- `import.lines.mapping` (extins): aceeași opțiune `vendor_code` pentru mapările salvate.

**Vizualizări**

- `purchase_order_form`: moștenește formularul comenzii de achiziție și adaugă butonul **Import Lines** în antet.
- `menu_import_lines_mapping`: meniu în configurarea Achizițiilor către mapările de import.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_import_lines](../deltatech_import_lines/index.md): oferă expertul, mixinul și mapările pe care acest modul le extinde pentru comenzile de achiziție.
