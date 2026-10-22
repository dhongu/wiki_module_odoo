# POS Stock in Other Shops (Stoc din alte magazine în POS)

- **Nume Tehnic:** `deltatech_pos_stock_shops`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_stock_shops
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_stock_shops`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Răspunde la întrebarea „Aveți produsul și în alt magazin?” direct la casă, fără ca vânzătorul să sune la celălalt magazin. Modulul extinde `deltatech_pos_stock` cu stocul celorlalte magazine ale companiei, încărcat odată cu sesiunea POS, astfel încât informația este disponibilă și când serverul nu poate fi contactat.

#### 2. Funcționalități Cheie

- **Pe cardul produsului:** sub cantitatea magazinului curent, insigna afișează totalul celorlalte magazine (ex. `+12`). Stocul negativ dintr-un magazin nu reduce ce poate livra altul.
- **Filtru în lista de produse:** *All products*, *In stock here*, *In other shops*; a doua atingere a filtrului activ îl dezactivează. Filtrul rămâne accesibil și când lista este goală.
- **Popup de informații produs:** popup-ul standard listează toate depozitele companiei; modulul îl limitează la magazinul curent și la magazinele alese, astfel încât depozitul central sau o locație de tranzit să nu apară ca stoc de predat de casier.
- **Funcționează offline:** cifrele sunt încărcate cu sesiunea; fără conexiune, butonul de informații deschide un popup cu stocul pe magazine, construit din datele sesiunii.
- **Actualizare continuă:** o vânzare, o recepție sau un transfer din alt magazin este transmis către casele deschise, pe canalul deja folosit de `deltatech_pos_stock`.
- **O singură interogare:** stocul tuturor magazinelor se citește cu o interogare grupată pe quanturi, nu una per magazin.
- **Aceeași cifră ca insigna:** stoc fizic sau disponibil (fizic minus rezervări), conform setării *Quantity shown* din `deltatech_pos_stock`.
- **Configurare:** *Point of Sale > Configuration > Settings*, blocul *Product Stock*: se bifează *Show stock*, apoi *Show the stock of the other shops*. Opțional se aleg *Shops*; dacă rămâne gol, se folosesc depozitele celorlalte puncte de vânzare ale companiei (depozitul casei curente nu apare niciodată ca alt magazin). Sesiunea POS se redeschide pentru a încărca stocul.

#### 3. Dependențe

- [deltatech_pos_stock](../deltatech_pos_stock/index.md)

#### 4. Componente Cheie

**Modele**

- `pos.config` (extins): câmpurile `display_shop_stock`, `stock_shop_warehouse_ids` și `stock_shop_list` (calculat), plus determinarea depozitelor „celorlalte magazine”.
- `product.template` (extins): câmpul JSON `pos_shop_stock` și calculul stocului pe magazine; încarcă câmpul în datele POS.
- `res.config.settings` (extins): câmpuri related către setările din `pos.config`.

**Vizualizări**

- `res_config_settings_view_form`: moștenește vizualizarea din `deltatech_pos_stock` și adaugă opțiunile pentru stocul altor magazine.
- Front-end POS (OWL, asset-uri `point_of_sale._assets_pos`): popup stoc pe magazine, extindere card produs, extindere ecran produse (filtre) și `PosStore`.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_pos_stock](../deltatech_pos_stock/index.md): modul de bază; canalul de actualizare și setarea *Quantity shown* sunt preluate de acolo.
