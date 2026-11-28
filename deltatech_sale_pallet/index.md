# Sale Pallet (localizat la `deltatech_sale_pallet/index.md`)

- **Nume Tehnic:** `deltatech_sale_pallet`
- **Versiune:** `20.0.1.0.13`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_pallet`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_pallet`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaugă automat paleți pe comenzile de vânzare, în funcție de cantitatea de produs comandată. Când un produs care necesită paletizare atinge cantitatea minimă pentru un palet, sistemul introduce în comandă produsul de tip palet și îi ajustează cantitatea pe măsură ce se depășește fiecare multiplu al minimului. Vânzarea reflectă astfel corect ambalarea, fără liniile de palet adăugate manual.

#### 2. Funcționalități Cheie

- Categorie de produs cu opțiunea „Pallet" activată, în care se încadrează produsul de tip palet.
- Selectarea produsului palet și a cantității minime pentru un palet pe produs.
- Adăugarea automată a produsului palet pe comandă la atingerea cantității minime.
- Creșterea automată a numărului de paleți la fiecare multiplu următor al cantității minime.
- Starea paleților afișată și pe factură.

#### 3. Dependențe

- `sale_margin`
- `account`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.category`: câmpul `pallet`, opțiunea de palet la nivel de categorie.
- `product.template`: `pallet_product_id`, `pallet_qty_min` și `pallet_price` (calculat).
- `sale.order` / `sale.order.line`: recalcularea liniilor de palet (`recompute_pallet_lines`, `compute_pallet_number`) la modificarea comenzii.
- `account.move`: `show_pallets_status` pentru paleți pe factură.
- `sale.report`: extinde raportarea vânzărilor.

**Vizualizări**

- `product_template_form_view` / `product_category_form_view`: configurarea paletului pe produs și pe categorie.
- `view_move_form`: paleții pe formularul facturii.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, cron sau acțiuni server.

#### 5. Conexiuni

- `sale_margin`: baza liniilor de comandă extinse de modul.
- `account`: tratarea paleților la nivel de factură.
- `stock`: folosit de teste pentru actualizarea cantităților disponibile.
