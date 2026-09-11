# Conector Trendyol Marketplace (localizat la `deltatech_marketplace_trendyol/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_trendyol`
- **Versiune:** `18.0.1.1.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/18.0/deltatech_marketplace_trendyol`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_trendyol`
- **Ultima Ingestie:** `2026-09-11`

#### 1. Sumar

Un cont de seller Trendyol lângă Odoo, fără conector, înseamnă catalog, stoc, preț și comenzi ținute manual în două locuri: fiecare actualizare de stoc sau preț trebuie repetată pe panoul de seller, fiecare comandă nouă trebuie reintrodusă, iar numerele de tracking trebuie urmărite manual astfel încât cumpărătorul să vadă statusul livrării chiar pe pagina Trendyol. Pe un marketplace de această dimensiune, o actualizare de preț ratată sau un import întârziat costă vânzări, nu doar timp. Conectorul Trendyol Marketplace închide acest gol: produsele, comenzile, stocul, prețul și facturile circulă automat între Odoo și Trendyol prin API-ul propriu V2 al Trendyol și endpoint-urile lui asincrone de tip batch — mecanismul pe care Trendyol îl cere de la un seller cu volum real, nu apeluri produs cu produs — iar pentru că se leagă de același framework comun `deltatech_marketplace` folosit și de conectorii Shopify, eMAG sau alții din suită, adăugarea Trendyol lângă un canal deja folosit nu înseamnă învățarea unui al doilea sistem.

#### 2. Funcționalități Cheie

- Import produse (oferte) existente din Trendyol, potrivite automat după cod de bare (barcode), cu status de aprobare, preț de vânzare/listă și cantitate de stoc
- Export asincron de preț și stoc prin API-ul batch `price-and-inventory`, cu verificare automată a rezultatului până când Trendyol raportează batch-ul finalizat, iar articolele respinse sunt înregistrate cu motivul exact dat de Trendyol
- Creare și actualizare de produse pe Trendyol (Product V2 API), cu categorie, atribute, cod de bare și imagine mapate din fișa produsului Odoo
- Import comenzi (pachete de expediție) cu client, adrese de livrare/facturare și linii de comandă complete, gata de pregătit și facturat ca orice altă vânzare
- Notificări de comenzi în timp real printr-un webhook Trendyol, pe lângă importul programat
- Trimiterea numărului de tracking AWB către Trendyol la validarea expedierii — **condiționată**: se declanșează doar dacă transferul are deja atribuit manual un transportator Odoo real cu integrare „rate and ship" (nu transportatorul generic „Free delivery" pe care cade implicit orice comandă Trendyol importată) și dacă tracking-ul nu a fost deja completat manual înainte de validare
- Actualizarea explicită a stării pachetului pe Trendyol (de exemplu Picking/Invoiced) — disponibilă doar ca apel de server/dezvoltator, fără declanșator automat din nicio tranziție Odoo
- Trimiterea automată a link-ului facturii către Trendyol după postarea facturii Odoo (dacă opțiunea e activă pe backend)
- Import al arborelui complet de categorii Trendyol dintr-un singur apel; atributele obligatorii și valorile permise ale unei categorii de nivel frunză se importă separat, abia la prima referire (de exemplu la importul unui produs care o folosește), nu automat odată cu arborele

#### 3. Dependențe

- `sale`
- `delivery`
- `deltatech_marketplace`
- `deltatech_marketplace_sale`
- `deltatech_marketplace_delivery`
- `deltatech_marketplace_payment`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea Sumar/Funcționalități a fost preluată din `readme/DESCRIPTION.md`; componentele de mai jos rezultă din configurarea backend-ului (`readme/CONFIGURE.md`), din fișa de consultant (`readme/FISA_CONSULTANT.md`) și din job-urile programate (`data/ir_cron_data.xml`):

- **Backend Trendyol**: se configurează pe `marketplace.backend` selectând provider-ul Trendyol, cu Seller ID, Username (API Key), Password (API Secret) și Storefront Code; locația API se setează automat (`https://apigw.trendyol.com`, respectiv gateway-ul de staging `https://stageapigw.trendyol.com` dacă mediul de producție e dezactivat — IP-urile serverului trebuie whitelistate de Trendyol pentru staging).
- **Legătura curier neautomată**: la import, conectorul creează întotdeauna o legătură `marketplace.delivery.carrier`, dar payload-ul Trendyol nu trimite un nume pe care căutarea automată (`save_from_marketplace`) să-l poată folosi — orice comandă importată cade pe transportatorul generic „Free delivery"; asocierea la un transportator Odoo real (Cargus, Sameday etc.) se face manual pe comandă.
- **`trendyol_write` pe comandă**: stub neimplementat (doar scrie un avertisment în jurnal) — nu există niciun push generic al modificărilor comenzii înapoi spre Trendyol, nici chiar cu „Active on write" bifat pe tipul de articol `orders`.
- **Marcă produs (`brandId`)**: fără câmp de mapare în interfață; valoarea se citește doar dintr-o cheie de context (`trendyol_brand_id`) pe care nimic din UI standard nu o setează.
- `ir_cron_trendyol_import_orders`: sarcină programată „Trendyol: Import Orders", la fiecare 30 de minute, dezactivată implicit (se activează manual după validarea configurării).
- `ir_cron_trendyol_export_stock`: sarcină programată „Trendyol: Export Stock", la fiecare oră, dezactivată implicit.

**Diferențe față de seria 19.0**

- Fluxurile și câmpurile sunt identice; diferă doar detalii interne (apelurile de traducere `self.env._()` și canalele de job), fără efect asupra datelor schimbate cu Trendyol.

**Mapare câmpuri produs**

Documentată integral în `readme/USAGE.md` (secțiunea „Product field mapping”), derivată din `trendyol_job_import()`, `trendyol_write()`, `trendyol_export_price()` și `trendyol_stock_export()`. Pe Trendyol listarea e identificată prin **cod de bare** — acela e `external_id` pe legătură, deci un produs fără cod de bare nu poate fi exportat. Exporturile de produs, preț și stoc trec toate prin API-ul batch asincron: conectorul reține `batchRequestId` și îi verifică rezultatul după un minut.

| Câmp | Câmp Odoo | Câmp Trendyol | Direcție |
|------|-----------|---------------|----------|
| Cod de bare (ID listare) | `external_id` (legătură), `barcode` | `barcode` | ambele |
| Cod de stoc | `external_code` (legătură, **Stock Code**), `default_code` | `stockCode` | ambele |
| Denumire produs | `name` | `title` | ambele |
| ID produs principal | `default_code` al șablonului | `productMainId` | Odoo → Trendyol |
| Categorie | `categ_id`, prin `marketplace.product.category` | `categoryId`; `pimCategoryId` la import | ambele (exportul eșuează dacă nu e mapată) |
| Preț de vânzare | `sale_price` (legătură), `list_price` | `salePrice` | ambele |
| Preț tăiat | `trendyol_list_price` (legătură) | `listPrice` | ambele |
| Cotă TVA | `taxes_id` (procentul primei taxe) | `vatRate` | Odoo → Trendyol |
| Monedă | moneda backend-ului | `currencyType` | Odoo → Trendyol |
| Stoc | `odoo_stock`, `external_stock` (legătură) | `quantity` | ambele |
| Greutate volumetrică | `weight` (1 dacă lipsește) | `dimensionalWeight` | Odoo → Trendyol |
| Descriere | `description_sale`, cu revenire pe denumire | `description` | Odoo → Trendyol |
| Marcă | `trendyol_brand_id` din context | `brandId` | Odoo → Trendyol |
| Aprobat | `trendyol_approved` (legătură, doar citire) | `approved` | Trendyol → Odoo |
| În vânzare | `trendyol_on_sale` (legătură, doar citire) | `onSale` | Trendyol → Odoo |
| Atribute | `attribute_line_ids`, prin `marketplace.product.attribute(.value)` | `attributes[].attributeId`, `attributes[].attributeValueId`; `attributeValue` / `customAttributeValue` la import | ambele (valorile nemapate sunt sărite și logate) |
| Imagini | `image_1024` (trimisă ca URL Odoo); `main_image` și restul la import | `images[].url` | ambele |

#### 5. Conexiuni

- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): conector marketplace analog, pentru Shopify.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector marketplace analog, pentru eMAG.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): conector marketplace analog, pentru PrestaShop.
- [deltatech_marketplace_woocommerce](../deltatech_marketplace_woocommerce/index.md): conector marketplace analog, pentru WooCommerce.
- [deltatech_marketplace_merchantpro](../deltatech_marketplace_merchantpro/index.md): conector marketplace analog, pentru MerchantPro.
- `deltatech_marketplace`: cadrul de bază marketplace peste care e construit conectorul.
- `deltatech_marketplace_sale` / `_delivery` / `_payment`: comenzile importate, infrastructura de mapare a curierilor (legătura creată la import nu se mapează automat la un transportator real) și metoda de plată „Trendyol".
