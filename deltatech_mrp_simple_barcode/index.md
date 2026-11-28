# Simple MRP barcode (localizat la `deltatech_mrp_simple_barcode/index.md`)

- **Nume Tehnic:** `deltatech_mrp_simple_barcode`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp_simple_barcode
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_simple_barcode`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul extinde producția simplă ([deltatech_mrp_simple](../deltatech_mrp_simple/index.md)) cu suport pentru scanarea codurilor de bare, pentru a accelera introducerea componentelor consumate. În loc să caute manual fiecare produs, operatorul scanează codul de bare sau codul intern, iar linia de produs consumat este adăugată sau cantitatea existentă este majorată automat.

#### 2. Funcționalități Cheie

- Extensie pentru [deltatech_mrp_simple](../deltatech_mrp_simple/index.md), cu suport de scanare a codurilor de bare.
- La scanare, produsul se adaugă pe o linie nouă din *Consume* sau, dacă există deja, i se crește cantitatea; operatorul primește o notificare.
- Dacă codul scanat nu este găsit ca barcode, produsul se caută după referința internă (`default_code`); dacă nu există nici așa, apare o eroare.
- Scanarea este permisă doar cât timp documentul este în starea ciornă (`draft`).

#### 3. Dependențe

- [deltatech_mrp_simple](../deltatech_mrp_simple/index.md)
- `barcodes`

#### 4. Componente Cheie

**Modele**

- `mrp.simple` (extins): adaugă câmpul tehnic nestocat `_barcode_scanned`, cu onchange care apelează `on_barcode_scanned` (caută produsul după `barcode`, apoi după `default_code`) și `_add_product` (adaugă o linie nouă în `product_out_ids` sau incrementează cantitatea).

**Vizualizări**

- `your_module_view_mrp_simple_form_inherit`: extinde formularul producției simplă (`deltatech_mrp_simple.view_mrp_simple_form`) cu câmpul `_barcode_scanned` și widgetul `barcode_handler`, definit în `static/src/js/barcode_handler_field.esm.js`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_mrp_simple](../deltatech_mrp_simple/index.md): modulul de bază pe care acesta îl extinde cu scanare.
- `barcodes`: furnizează infrastructura de captare a evenimentelor de scanare.
