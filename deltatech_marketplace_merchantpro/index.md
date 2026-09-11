# Conector Marketplace MerchantPro (localizat la `deltatech_marketplace_merchantpro/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_merchantpro`
- **Versiune:** `18.0.0.0.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/18.0/deltatech_marketplace_merchantpro
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_merchantpro`
- **Ultima Ingestie:** `2026-09-11`

#### 1. Sumar

Un magazin MerchantPro lângă Odoo, fără conector, înseamnă catalog, stoc și comenzi ținute manual în două locuri: o schimbare de preț sau de stoc făcută în Odoo nu ajunge singură pe vitrină, iar fiecare comandă plasată pe magazin trebuie reintrodusă manual înainte de a putea fi onorată. Acest modul închide golul: produsele, categoriile, stocul și comenzile circulă automat între Odoo și MerchantPro prin API-ul V2 al platformei, iar pentru că se leagă de același framework comun (`deltatech_marketplace`) folosit și de conectorii eMAG, Shopify sau alți conectori din suită, adăugarea MerchantPro lângă un canal deja folosit nu înseamnă învățarea unui al doilea sistem.

#### 2. Funcționalități Cheie

- **Sincronizare produse**: exportă produse noi din Odoo către MerchantPro cu înregistrare completă (nume, descriere, categorie, preț, greutate, cod de bare, plus imaginile suplimentare din galerie) și actualizează produsele existente; imaginea principală (`image_1920`) și atributele de variantă NU sunt trimise în versiunea actuală (cod comentat/dezactivat).
- **Import produse**: import paginat, cu opțiunea `only_missing` pentru a aduce doar produsele lipsă fără a atinge legăturile existente; lista paginată aduce doar câmpuri minime (id/nume/SKU/cod de bare/preț) — descrierea și imaginile ajung doar la un import individual sau prin *Only Missing*. Orice import de produs **suprascrie** `list_price`-ul Odoo cu `price_net` de la MerchantPro, dacă opțiunea **Ignore Price** nu e bifată pe backend.
- **Sincronizare categorii**: import și export al categoriilor de produse cu ierarhia părinte/copil păstrată în ambele direcții. Importul de produse **nu** leagă automat categoria pe legătura Odoo (bug de cod cunoscut, semnalat separat, nereparat) — de aceea se recomandă import categorii ÎNAINTE de import produse.
- **Export stoc**: nivelurile de stoc pot fi trimise către MerchantPro prin butonul manual **Export Stock**, sau automat doar dacă e activat explicit cronul **Marketplace: export stock** (livrat dezactivat implicit) — o mișcare de stoc doar declanșează cronul, nu apelează API-ul direct.
- **Export preț**: prețul trimis (`price_net`, fără TVA) este întotdeauna `list_price` al produsului Odoo — **lista de prețuri a backend-ului (`pricelist_id`) NU e sursa valorii exportate**, ea decide doar ce produse sunt considerate „modificate" (candidate la export).
- **Import comenzi**: webhook în timp real pentru comenzi noi, plus un job paginat de siguranță (fereastră configurabilă, implicit 2 zile). Jobul paginat **filtrează pe `shipping_status`** și importă/actualizează doar comenzi aflate deja în stările `cancelled`, `delivered`, `shipped` sau `returned` — **nu recuperează** o comandă nouă sau „în procesare" ratată de webhook, indiferent de câte ori rulează.
- **Sincronizare stare comandă**: starea de plată (`paid`/`awaiting`) și de livrare (`shipped`/`delivered`/`cancelled`) primite de la MerchantPro declanșează automat înregistrarea plății, confirmarea livrării/recepției sau anularea comenzii în Odoo.
- **Respectarea limitelor de rată**: limitele publicate de MerchantPro (4/s, 80/min, 3600/oră, 60000/zi) sunt respectate printr-un token-bucket comun; la HTTP 429 se citește timpul de așteptare din `error.details.reset_time` (sau se folosește un fallback de 60s) și jobul se reprogramează prin `queue_job` în loc să eșueze definitiv.

**Corecții față de versiunea anterioară a acestei pagini:** nu există niciun buton „Import All" pentru Product Template/Sale Order/Public category (framework-ul îl afișează doar dacă există o metodă `mp_import_all`, pe care acest conector nu o implementează pentru niciun tip); importul de produse nu atașează categoria pe legătura Odoo (bug de cod cunoscut, nu funcționalitate); lista de prețuri a backend-ului nu este sursa prețului exportat, ci doar filtrul de selecție a produselor „modificate"; importul paginat de comenzi nu este o plasă de siguranță completă, fiind limitat de `shipping_status`.

#### 3. Dependențe

- `deltatech_marketplace`
- `deltatech_marketplace_sale`
- `deltatech_marketplace_payment`
- `deltatech_marketplace_delivery`
- `deltatech_marketplace_website`
- `queue_job` (dependență tehnică, folosită pentru import/export paginat și pentru `RetryableJobError` la limita de rată)

#### 4. Componente Cheie

*Conform fluxului de ingestie, secțiunile 'Sumar' și 'Funcționalități Cheie' au fost preluate din `readme/DESCRIPTION.md` (corectat unde textul original nu mai reflecta comportamentul real al codului — vezi nota din secțiunea 2), iar analiza detaliată a codului pentru componente a fost omisă deoarece Readme-ul nu o solicită explicit.*

**Diferențe față de seria 19.0**

- Prețul net exportat se obține în această serie prin helperul `_get_price_without_and_with_taxes()`; pe 19.0 se cheamă direct `taxes_id.compute_all()`. Câmpul trimis rămâne `price_net`.
- Restul fluxurilor (import/export produse și categorii, export stoc și preț, import comenzi, tratarea limitelor de rată) sunt identice între serii.

**Mapare câmpuri produs**

Documentată integral în `readme/USAGE.md` (secțiunea „Product field mapping"), derivată din `mp_import_by_values()`, `mp_convert_from_odoo()` și `mp_call_inventory()`. Payload-ul de export se construiește din câmpurile listate în `mp_get_export_fields()`, deci un export parțial (la scriere) trimite doar ce s-a schimbat.

| Câmp | Câmp Odoo | Câmp MerchantPro | Direcție |
|------|-----------|------------------|----------|
| ID produs | `external_id` (legătură) | `id` | ambele |
| Denumire produs | `name` | `name` | ambele |
| SKU | `default_code` | `sku` | ambele |
| Referință externă | `external_code` (legătură) | `ext_ref` | MerchantPro → Odoo |
| Cod de bare | `barcode` | `ean` | ambele |
| Preț de vânzare | `list_price` | `price_net` (fără TVA; recalculat la export cu `taxes_id.compute_all()`) | ambele |
| Cost | `standard_price` | `cost_net` | Odoo → MerchantPro |
| Greutate | `weight` | `weight` | Odoo → MerchantPro |
| Descriere site | `website_description` | `description` | ambele |
| Publicat | `active` | `status` (`active` / `inactive`) | Odoo → MerchantPro |
| Poate fi vândut | `sale_ok` | `visibility` (`visible` / `hidden`) | Odoo → MerchantPro |
| Sfârșit de viață | `eol` împreună cu `qty_available` zero | `status` forțat pe `inactive` | Odoo → MerchantPro |
| Categorii eCommerce | `public_categ_ids` | `category_id` (prima) și `categories[]` | ambele (o categorie fără legătură e creată întâi în MerchantPro) |
| Imagine principală | `image_1920` | intrarea din `images[]` cu `default` true (`base64`) | MerchantPro → Odoo |
| Imagini suplimentare | înregistrări `product.image` | `images[]` (`caption`, `base64`, `url`) | ambele |
| Tip produs | `product_variant_count` | `type` (`basic` / `multi_variant`) | Odoo → MerchantPro (la creare) |
| Stoc | `odoo_stock` (legătură) | `stock`, prin `/api/v2/inventory/id/{id}` | Odoo → MerchantPro |

#### 5. Conexiuni

- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): conector marketplace analog, pentru Shopify.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector marketplace analog, pentru eMAG.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): conector marketplace analog, pentru PrestaShop.
- [deltatech_marketplace_woocommerce](../deltatech_marketplace_woocommerce/index.md): conector marketplace analog, pentru WooCommerce.
- [deltatech_marketplace_trendyol](../deltatech_marketplace_trendyol/index.md): conector marketplace analog, pentru Trendyol.
- `deltatech_marketplace`: cadrul de bază (backend, indicator de sănătate, job-uri, rate-limiting, webhook).
- `deltatech_marketplace_sale` / `_payment` / `_delivery` / `_website`: comanda generată, jurnalul „Marketplace Payment", potrivirea transportatorului (fallback pe „Free Delivery") și legătura de categorie publică.
- `deltatech_marketplace_purchase`: modul înrudit din suită, pentru fluxul de achiziții.
