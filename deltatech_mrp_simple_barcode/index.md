# Simple MRP barcode (localizat la `deltatech_mrp_simple_barcode/index.md`)

- **Nume Tehnic:** `deltatech_mrp_simple_barcode`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_simple_barcode
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_simple_barcode`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul extinde producția simplă ([deltatech_mrp_simple](../deltatech_mrp_simple/index.md)) cu suport pentru scanarea codurilor de bare, pentru a accelera introducerea componentelor consumate direct pe ecranul de producție. În loc să caute manual fiecare produs, operatorul scanează codul de bare sau codul intern, iar linia de produs consumat este adăugată sau cantitatea existentă este majorată automat.

#### 2. Funcționalități Cheie

- Extensie pentru [deltatech_mrp_simple](../deltatech_mrp_simple/index.md).
- Adaugă suport de scanare a codurilor de bare pentru producția simplă.
- La scanare, adaugă produsul într-o linie nouă de consum sau, dacă produsul există deja, îi crește cantitatea consumată.
- Dacă barcode-ul scanat nu este găsit, caută produsul după referința internă (`default_code`).

#### 3. Dependențe

- [deltatech_mrp_simple](../deltatech_mrp_simple/index.md)
- `barcodes`

#### 4. Componente Cheie

**Modele**

- `mrp.simple`: extinde modelul din `deltatech_mrp_simple` cu mixin-ul `barcodes.barcode_events_mixin`; implementează `on_barcode_scanned`, care caută produsul scanat (după `barcode` sau, ca alternativă, după `default_code`) și `_add_product`, care adaugă o linie nouă în `product_out_ids` sau incrementează cantitatea unei linii existente. Scanarea este permisă doar cât timp producția este în starea `draft`.

**Vizualizări**

- `your_module_view_mrp_simple_form_inherit` (mrp.simple.form.inherit): extensie a formularului de producție simplă (`deltatech_mrp_simple.view_mrp_simple_form`), care adaugă câmpul tehnic `_barcode_scanned` cu widget-ul `barcode_handler` pentru capturarea scanărilor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_mrp_simple](../deltatech_mrp_simple/index.md): modulul de bază de producție simplă pe care acesta îl extinde cu scanare.
- `barcodes`: furnizează mixin-ul și infrastructura de captare a evenimentelor de scanare.
