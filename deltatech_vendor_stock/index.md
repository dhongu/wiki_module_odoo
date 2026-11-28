# Stoc Furnizor (localizat la `deltatech_vendor_stock/index.md`)

- **Nume Tehnic:** `deltatech_vendor_stock`
- **Versiune:** `20.0.1.2.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_vendor_stock`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_vendor_stock`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Când stocul propriu nu ajunge, vânzătorul vrea să știe dacă furnizorul mai poate livra produsul și dacă alt depozit al companiei îl are. Modulul reține stocul raportat de furnizor și îl afișează, împreună cu stocul liber pe depozit, pe comanda de vânzare.

#### 2. Funcționalități Cheie

- **Stoc furnizor pe linia de listă de prețuri furnizor** (`product.supplierinfo`): câmpul **Cantitate disponibilă**, în formular și ca coloană opțională. Stocul furnizor al unui produs este suma liniilor companiei curente, ale companiilor părinte și ale liniilor fără companie; o linie pe o variantă numără doar pentru acea variantă.
- **Stoc furnizor pe linia comenzii**: fereastra de disponibilitate (pictograma grafic de lângă cantitate) arată rândul **Stoc furnizor**, convertit în unitatea de măsură a liniei; **Cantitate disponibilă furnizor** este și coloană opțională.
- **Pictogramă colorată după disponibilitate**: verde (cererea va fi satisfăcută), cyan (va fi satisfăcută, dar fără cantitate liberă azi), roșu (nu va fi satisfăcută), galben (nu va fi satisfăcută, dar furnizorul are stoc).
- **Stoc liber pe depozit**: cu mai multe depozite, fereastra listează stocul liber din fiecare depozit cu stoc (întâi depozitul comenzii) și deschide raportul de prognoză la click; disponibil și în coloana opțională **Stoc/WH**.
- **Configurare**: culorile se setează în *Vânzări > Configurare > Setări*, secțiunea *Oferte și comenzi*; parametrul de sistem `deltatech_vendor_stock.use_only_main_location` = `1` limitează stocul pe depozit la locația principală.
- **Limitare**: **Alte cantități disponibile** (rândul *Alt stoc*) nu e completat de acest modul.

#### 3. Dependențe

- `product`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.supplierinfo` (extins): cantitatea disponibilă la furnizor.
- `product.product` (extins): stocul furnizor al produsului.
- `sale.order.line` (extins): stocul furnizor și stocul pe depozit pe linia comenzii.
- `res.config.settings` (extins): culorile pictogramei de disponibilitate.

**Vizualizări**

- `product_supplierinfo_form_view` / `product_supplierinfo_tree_view`: câmpul pe linia furnizorului.
- `view_order_form_inherit_sale_stock_qty`: coloanele opționale pe linia comenzii.
- `res_config_settings_view_form_deltatech_vendor_stock`: culorile din Setări.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale suplimentare în afara dependențelor declarate.
