# Conector Shopify Marketplace (localizat la `deltatech_marketplace_shopify/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_shopify`
- **Versiune:** `18.0.0.5.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/18.0/deltatech_marketplace_shopify
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_shopify`
- **Ultima Ingestie:** `2026-09-11`

#### 1. Sumar

Conectorul Shopify Marketplace leagă Odoo de un magazin Shopify, astfel încât catalogul, clienții, comenzile și stocul să fie gestionate dintr-un singur backend, fără introducere manuală în două locuri. În această serie (18.0) conectorul comunică cu Shopify **exclusiv prin REST Admin API** (biblioteca `ShopifyAPI`); stratul GraphQL, retururile (RMA) și editarea liniilor de comandă există doar pe seria 19.0. Modulul se instalează On-Premise sau pe Odoo.sh (nu pe Odoo Online/SaaS) și folosește același nucleu comun `deltatech_marketplace` ca și conectoarele eMAG, PrestaShop sau WooCommerce.

#### 2. Funcționalități Cheie

- **Sincronizare produse**:
  - Export de șabloane și variante din Odoo către Shopify (creare și actualizare), cu imagine principală și stoc inițial.
  - Import de șabloane, variante și imagini din Shopify, plus actualizări prin webhook-ul `products/update`.
  - Sincronizarea prețului și a datelor de bază (SKU, cod de bare, greutate) pe fiecare variantă.
  - Import al codului vamal și al țării de origine din `InventoryItem` (`harmonized_system_code`, `country_code_of_origin`), inclusiv codurile Intrastat când modulul Enterprise e instalat.
  - Un produs cu mai multe variante Shopify importat fără **Options as Attributes** activ tot se importă, dar variantele lui sunt sărite cu avertisment în log — niciodată fuzionate tăcut.
  - Exportul REST creează variantele **fără opțiuni**, deci maparea opțiune ↔ atribut funcționează la import; pentru produse cu mai multe variante exportul complet al opțiunilor există doar pe 19.0 (prin `productSet`).

- **Atribute de produs**: import al opțiunilor Shopify ca atribute și valori Odoo, cu control asupra modului de creare a variantelor (`shopify_option_create_variant`).

- **Clienți**: import al clienților Shopify ca contacte Odoo, cu actualizare prin webhook.

- **Comenzi**:
  - Import al comenzilor din fereastra **Sale Order Days** a backend-ului (nu există în această serie filtre pe status/plată/livrare — acelea apar pe 19.0).
  - Webhook-uri `orders/create`, `orders/updated`, `orders/paid`, `orders/cancelled` pentru actualizare fără cron.
  - Aplicarea fazelor de vânzare din etichetele (tags) comenzii, la fiecare import.
  - Rutarea depozitului pe baza locației Shopify, prin binding-ul `marketplace.warehouse`; locațiile nemapate cad pe depozitul implicit.
  - Suport pentru comenzi în altă monedă decât moneda magazinului (`presentment_currency`).
  - Protecție la re-import pe comenzile marcate „discarded" (`only_missing` / „No Refresh"): se mai actualizează doar locker-ul, curierul și liniile de livrare deschise.
  - Sincronizarea anulării comenzii din Odoo către Shopify.

- **Plăți și livrare**:
  - Import și mapare a metodelor de plată; starea financiară a comenzii (`financial_status`) se reflectă în tranzacția de plată din Odoo.
  - Maparea curierilor și liniile de livrare pe comandă, cu suport pentru puncte de ridicare (lockere) citite din notele Shopify.
  - Trimiterea numerelor de tracking (AWB) prin `FulfillmentV2`, cu declanșator configurabil (`shopify_fulfillment_trigger`: la crearea AWB sau la validarea transferului), inclusiv onorări parțiale, asincron prin `queue_job`.

- **Stoc și prețuri**:
  - Export de stoc prin `InventoryLevel`, cu suport multi-locație (o locație Shopify = un depozit Odoo).
  - Export de preț per variantă sau la nivel de șablon, din lista de prețuri a backend-ului, cu `compare_at_price` setat automat la discount; pornește doar pentru variantele cu diferență de preț.
  - Import de preț la cerere (`Import Price`), citit de pe prima variantă a produsului.

- **Depozite / locații**: import al locațiilor Shopify ca binding-uri `marketplace.warehouse`; depozitele Odoo trebuie create *înainte* de acest import.

- **Autentificare și operații automate**:
  - Două moduri de autentificare: Legacy Private Apps (token permanent) și Dev Dashboard Apps (OAuth `client_credentials`, token cu expirare la 24h, reîmprospătat automat sub 30 de minute rămase și proactiv prin cron-ul „Shopify: Refresh Access Tokens").
  - `Client Secret` e folosit și la verificarea semnăturii HMAC a webhook-urilor primite.
  - Sincronizare asincronă prin `queue_job`, cu retry automat la limitări de rată (HTTP 429) și erori de server.
  - Import de colecții Shopify (custom și smart) ca și categorii publice de produs.
  - Wizard **Check webhooks** (buton de antet) care compară webhook-urile înregistrate în Shopify cu cele așteptate de Odoo (Matched / Missing / Orphan), cu remediere directă.
  - Indicator de sănătate pe cardul kanban al backend-ului, moștenit din framework.

#### 3. Dependențe

- `deltatech_marketplace`
- `deltatech_marketplace_payment`
- `deltatech_marketplace_delivery`
- `deltatech_marketplace_sale`
- `deltatech_marketplace_sale_stage`
- `deltatech_marketplace_website`

Dependență externă Python: `ShopifyAPI`.

#### 4. Componente Cheie

**Modele**

- `marketplace.backend` (extins, `backend.py`): configurarea Shopify a backend-ului — credențiale și `Access Type`, reîmprospătarea token-ului OAuth, `shopify_product_type_as_category`, `shopify_option_as_attribute`, `shopify_option_create_variant`, `shopify_fulfillment_trigger`.
- `backend_adapter.py`: adaptorul REST (autentificare, apeluri cu retry la rate-limit și erori de server).
- `binding_product_template.py` / `binding_product.py`: binding-uri de șablon și variantă — import/export de date de bază, opțiuni, imagini, preț (`shopify_export_price`, `shopify_import_price`) și stoc (`shopify_import_stock`, `shopify_stock_export`), plus importul informațiilor vamale.
- `binding_product_image.py`: imaginile de produs, cu asociere pe variante.
- `binding_attribute.py`: atributele de produs (opțiunile Shopify).
- `binding_customers.py`: clienții și adresele lor.
- `binding_sale_order.py`: comenzile — import, rutare depozit, monedă de prezentare, stare financiară, protecția comenzilor „discarded".
- `binding_sale_stage.py`: fazele de vânzare (tags Shopify → `marketplace.sale.phase`).
- `binding_payment_acquirer.py`: metodele de plată.
- `binding_public_category.py`: colecțiile importate ca categorii publice.
- `binding_warehouse.py`: locațiile Shopify mapate la depozite Odoo.
- `stock_picking.py`: trimiterea AWB-ului și a onorării către Shopify.
- `marketplace.shopify.webhook.checker` (+ `.line`, `wizard/shopify_webhook_checker.py`): wizard-ul de verificare a webhook-urilor.

**Vizualizări**

- `backend_views.xml`: formularul backend-ului Shopify (opțiunile de sincronizare, declanșatorul de onorare, butonul **Check webhooks**).
- `shopify_webhook_checker_views.xml`: wizard-ul Matched / Missing / Orphan.

**Acțiuni Automate / Acțiuni Server**

- `cron_shopify_refresh_tokens` (`data/cron.xml`): reînnoiește token-urile OAuth ale backend-urilor Dev Dashboard Apps.
- `data/job_function.xml`: canalele `shopify_inbound` / `shopify_outbound` și funcțiile de job pentru importul comenzilor, clienților și produselor.

**Diferențe față de seria 19.0**

- Transport: doar **REST Admin API**. Toate modulele `shopify_graphql_*.py` și comutatoarele GraphQL per subsistem (produse, stoc, onorare, clienți, comenzi, webhook-uri) sunt doar pe 19.0.
- Nu există retururi/RMA (`binding_return_request.py`), editare de linii de comandă (`shopify_graphql_order_edit.py`), traducerea filtrelor de comandă (`shopify_order_filters.py`) și opțiunea **Update Price Only**.
- **Test connection** validează credențialele printr-un apel REST, nu printr-un query GraphQL `shop`.

**Mapare câmpuri produs**

Documentată integral în `readme/USAGE.md` (secțiunea „Product field mapping"), derivată din cod: `shopify_convert_result_to_values()`, `shopify_write()`, `shopify_create()`, `shopify_export_price()`. Numele de mai jos sunt cheile din payload-ul REST. „ambele" = câmpul circulă în ambele direcții, fiecare pe acțiunea ei (import, export, export preț).

| Câmp | Câmp Odoo | Câmp Shopify (REST) | Direcție |
|------|-----------|---------------------|----------|
| Denumire produs | `name` | `title` | ambele |
| Referință internă (SKU) | `default_code` | `variants[].sku` | ambele |
| Cod extern | `external_code` (legătură) | `variants[0].sku` | Shopify → Odoo |
| ID extern | `external_id` (legătură) | `id` (produs / variantă) | ambele |
| Preț de vânzare | `list_price`, `odoo_price` (legătură) | `variants[].price` | ambele |
| Preț de catalog | `list_price`, când lista de prețuri a backend-ului dă discount | `compare_at_price` | Odoo → Shopify |
| Cod de bare | `barcode` | `barcode` | ambele |
| Greutate | `weight` (kg) | `weight`, `weight_unit` | ambele |
| Descriere vânzare | `description_sale` | `body_html` | Odoo → Shopify |
| Categorie produs | `categ_id` | `product_type` | ambele (import doar cu **Product Type as Category**) |
| Marcă | `get_brand_name()` (`deltatech_marketplace_brand`) | `vendor` | Odoo → Shopify |
| Categorii eCommerce | `public_categ_ids` | colecții `CustomCollection` și `SmartCollection` | Shopify → Odoo |
| Atribute și valori | `attribute_line_ids` | `options[].name`, `options[].values`, `variants[].option1`..`option3` | Shopify → Odoo (doar cu **Options as Attributes**) |
| Imagine principală | `image_1920` | `images[0].src`; `images[].attachment` la export | ambele |
| Imagini suplimentare | înregistrări `product.image` | `images[1..]` | Shopify → Odoo |
| Stoc | `odoo_stock`, `external_stock` (legătură) | `InventoryLevel.available`, per locație | ambele |
| Articol de inventar | `shopify_inventory_item_id` (legătură) | `inventory_item_id` | Shopify → Odoo |
| Urmărire stoc | — (fix la creare) | `inventory_management` = `shopify`, `inventory_policy` = `deny` | Odoo → Shopify |
| Stare publicare | — (mereu activ la creare) | `status` | Odoo → Shopify |
| Cod vamal | `hs_code` | `harmonized_system_code` (InventoryItem) | Shopify → Odoo |
| Țară de origine | `country_of_origin` | `country_code_of_origin` (InventoryItem) | Shopify → Odoo |

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector marketplace analog, pentru eMAG.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): conector marketplace analog, pentru PrestaShop.
- [deltatech_marketplace_woocommerce](../deltatech_marketplace_woocommerce/index.md): conector marketplace analog, pentru WooCommerce.
- [deltatech_marketplace_merchantpro](../deltatech_marketplace_merchantpro/index.md): conector marketplace analog, pentru MerchantPro.
- [deltatech_marketplace_trendyol](../deltatech_marketplace_trendyol/index.md): conector marketplace analog, pentru Trendyol.
- `deltatech_marketplace`: cadrul de bază (backend, job-uri, rate-limiting, indicator de sănătate).
- `deltatech_marketplace_sale` / `_sale_stage` / `_payment` / `_delivery` / `_website`: comenzile importate, fazele de vânzare pe care se mapează tag-urile, plățile, curierii și fluxurile de e-commerce.
