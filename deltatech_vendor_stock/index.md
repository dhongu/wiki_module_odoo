# Stoc Furnizor (localizat la `deltatech_vendor_stock/index.md`)

- **Nume Tehnic:** `deltatech_vendor_stock`
- **Versiune:** `19.0.1.2.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_vendor_stock`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_vendor_stock`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul aduce vizibilitate asupra stocului disponibil la furnizor direct în Odoo. Cantitatea disponibilă la furnizor este reținută în datele de bază ale produsului și afișată în comenzile de vânzare, ajutând echipa de vânzări să știe dacă un produs poate fi adus de la furnizor chiar dacă stocul propriu este zero. Astfel, agenții pot confirma mai ușor disponibilitatea către client fără verificări manuale separate.

#### 2. Funcționalități Cheie

- Actualizarea cantității disponibile la furnizor în datele de bază ale produsului (pe fiecare rând de furnizor, în fișa produsului).
- Afișarea cantității disponibile la furnizor în comanda de vânzare, convertită în unitatea de măsură a liniei.
- Afișarea unui indicator (pictogramă galbenă) atunci când stocul curent este zero, dar produsul urmează să fie aprovizionat de la furnizor.
- Stocul furnizorului se însumează doar din rândurile aparținând companiei curente (sau a comenzii), companiilor-părinte și rândurilor fără companie; stocul înregistrat pentru altă companie nu este adăugat.
- Fereastra de disponibilitate (popover) de pe linia comenzii listează stocul liber pe fiecare depozit al companiei, într-un tabel citit la deschiderea ferestrei: depozitul comenzii apare primul și marcat, chiar și fără stoc; cantitățile care acoperă necesarul sunt verzi, iar depozitul comenzii este roșu dacă nu îl acoperă. Un clic pe depozit deschide prognoza produsului în acel depozit. Stocul furnizorului apare sub depozite, doar dacă nu este zero.
- Culorile indicatorilor de stoc (acoperit, acoperit fără stoc liber azi, neacoperit, disponibil la furnizor, implicit) sunt configurabile din Setări Vânzări, în zona comenzilor/ofertelor.
- Opțional, stocul pe depozit se poate calcula doar din locația principală a depozitului (parametru de sistem `deltatech_vendor_stock.use_only_main_location`).
- Coloane opționale în lista liniilor comenzii: cantitate la furnizor, alt stoc și stoc pe depozite.

#### 3. Dependențe

- `product`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.supplierinfo` (extins): adaugă câmpul `qty_available` (cantitatea disponibilă la furnizor).
- `product.product` (extins): câmpurile calculate `vendor_qty_available` și `other_qty_available`, în funcție de compania curentă.
- `sale.order.line` (extins): câmpurile calculate `vendor_qty_available`, `other_qty_available` și `warehouse_stock`; metode pentru stocul liber pe depozit (`get_warehouse_stock`) și pentru culorile indicatorilor (`get_stock_colors`).
- `res.config.settings` (extins): cele cinci culori de stare, salvate ca parametri de sistem `deltatech_vendor_stock.color_*`.

**Vizualizări**

- `product_supplierinfo_form_view` / `product_supplierinfo_tree_view`: afișează `qty_available` în formularul și lista rândurilor de furnizor.
- `view_order_form_inherit_sale_stock_qty`: adaugă câmpurile de stoc pe liniile comenzii de vânzare, folosite de widgetul de disponibilitate.
- `res_config_settings_view_form_deltatech_vendor_stock`: selectoare de culoare în Setări.
- Frontend (OWL): `qty_at_date_widget_extended.esm.js`, `vendor_stock_colors_service.esm.js`, `qty.xml` pentru popover-ul extins.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `stock`: stocul liber pe depozit și prognoza provin din logica de stoc standard.
- `purchase`: rândurile de furnizor (`product.supplierinfo`) sunt cele din fișa produsului, folosite și la aprovizionare.
