# Conector Marketplace PrestaShop (localizat la `deltatech_marketplace_prestashop/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_prestashop`
- **Versiune:** `18.0.0.2.9`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/18.0/deltatech_marketplace_prestashop`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_prestashop`
- **Ultima Ingestie:** `2026-09-11`

#### 1. Sumar

Conectorul Deltatech pentru marketplace PrestaShop permite integrarea directă între sistemul ERP Odoo și PrestaShop, una dintre cele mai populare platforme open-source de comerț electronic. Modulul asigură sincronizarea datelor esențiale de business, astfel încât magazinele online PrestaShop pot fi administrate direct din Odoo. Rezultatul este o soluție unificată pentru gestionarea produselor, a clienților și a comenzilor, eliminând introducerea dublă de date și păstrând o singură sursă de adevăr pentru informațiile comerciale.

#### 2. Funcționalități Cheie

- **Gestionarea completă a produselor:** sincronizarea catalogului de produse între Odoo și PrestaShop, suport pentru variante, atribute și caracteristici, import/export de imagini și conținut multimedia, gestionarea categoriilor de produse și a categoriilor publice. Exportul (creare/actualizare pe PrestaShop) trimite preț, denumire, EAN, greutate și categorii publice, la cerere sau automat la scriere (comutatorul *Active On Write*). Stocul circulă într-un singur sens: **doar din PrestaShop către Odoo** — modulul nu implementează export de stoc către PrestaShop.
- **Integrare avansată a clienților:** importul clienților PrestaShop în baza de contacte Odoo, sincronizarea datelor de client, a adreselor și a istoricului de cumpărături, gestionarea grupurilor de clienți și a asocierilor.
- **Gestionarea cuprinzătoare a comenzilor:** importul comenzilor de vânzare din PrestaShop în Odoo, cu posibilitatea de a filtra importul după statusul comenzii (pe baza statusurilor deja sincronizate prin Sale Stage), crearea automată a comenzilor de vânzare Odoo și urmărirea îndeplinirii și livrării comenzilor.
- **Push dinspre Odoo spre PrestaShop:** statusul comenzii se trimite către PrestaShop doar dacă *Active On Write* e activat pe elementul „Sale Order"; în schimb, numărul de tracking (la trimiterea coletului către curier) și legătura facturii (la postarea facturii) se trimit **necondiționat**, indiferent de acest comutator.
- **Webhook de intrare (nu ieșire):** fiecare tip de date sincronizat expune un link de webhook pe care **PrestaShop îl apelează către Odoo** (nu invers) pentru a declanșa imediat importul unei comenzi, fără a aștepta cron-ul orar.
- **Wizard „Marketplace sync":** acțiune contextuală de pe produse/șabloane de produs pentru export la cerere (implicit `Direction = Export`, `Update Mode = Stock`; comutat manual pe `All` include și preț/nume) — ignoră comutatorul Active On Write.
- **Capabilități internaționale:** suport multilingv prin legături de limbă, gestionarea multi-valută, sincronizarea țărilor și a județelor (regiuni/state), gestionarea livrărilor și a taxelor internaționale.
- **Integrare livrare și plată:** suport pentru curierii de livrare PrestaShop, sincronizarea metodelor de plată și a procesatorilor, integrarea cu depozitele pentru îndeplinirea comenzilor.
- **Îmbunătățirea procesului de vânzare:** suport pentru etapele de vânzare și urmărirea statusului comenzilor, sincronizarea etichetelor de vânzare, atribuirea comenzilor pe echipe cu asociere de depozit.
- **Operațiuni automatizate:** sarcini programate de sincronizare (cron comun „Marketplace: Get Orders"), procesare în fundal cu gestionare prin coadă (queue_job) și opțiuni de sincronizare incrementală (bifa „Only Missing").
- **API pentru facturi:** ruta `/marketplace/sale_order/get_invoice`, autentificată cu token-ul de securitate al backend-ului, prin care PrestaShop (sau alt sistem extern) poate cere URL-ul PDF-ului facturii unei comenzi importate.

#### 3. Dependențe

- `deltatech_marketplace`
- `deltatech_marketplace_website`
- `deltatech_marketplace_sale_stage`
- `deltatech_marketplace_delivery`
- `deltatech_marketplace_payment`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de componente nu au fost extrase din cod deoarece fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie. Pentru context, descrierea menționează că implementarea folosește API-ul de servicii web PrestaShop (autentificare HTTP Basic Auth pe o singură cheie) și un sistem de binding-uri (legături) care conectează entitățile Odoo cu corespondentele lor din PrestaShop (șabloane și variante de produs, categorii și atribute, clienți și adrese, comenzi și linii de comandă, stoc, metode de plată și livrare, țări, limbi, valute), plus un controller (`controller/main.py`) pentru webhook-ul de intrare (apelat de PrestaShop către Odoo) și pentru ruta de facturi, cu procesare de joburi în fundal prin `queue_job`.

**Modele**

- Nu au fost extrase din cod (vezi nota de mai sus).

**Vizualizări**

- Nu au fost extrase din cod (vezi nota de mai sus). Modulul include `views/backend_views.xml` și `views/menu.xml`.

**Acțiuni Automate / Acțiuni Server**

- Nu au fost extrase din cod (vezi nota de mai sus). Descrierea menționează existența unor joburi programate de sincronizare și procesare în fundal; cron-ul comun „Marketplace: Get Orders" (inactiv implicit) importă comenzile pentru backend-urile fără „Disable Import Sale Order" bifat.

**Diferențe față de seria 19.0**

- Structura multilingvă trimisă la export are aici forma `{"language": [{"attrs": {"id": "<id_limbă>"}, "value": ...}]}`; pe 19.0 a fost simplificată la `{"id": ..., "value": ...}`.
- Conversia prețului importat la preț cu TVA (opțiunea **Tax included**) folosește în această serie helperul `_get_price_without_and_with_taxes()`; pe 19.0 se cheamă direct `taxes_id.compute_all()`. Câmpurile schimbate rămân aceleași.
- Structura de modele, controllerul de webhook și ruta de facturi sunt identice între serii.

**Mapare câmpuri produs**

Documentată integral în `readme/USAGE.md` (secțiunea „Product field mapping”), derivată din `prestashop_import_by_id()`, `prestashop_create()`, `prestashop_write()` și binderul de stoc. Câmpurile traductibile circulă pe fiecare limbă din `marketplace.lang` (structura multilingvă construită de `prestashop_get_translatable_payload()`); fără nicio limbă mapată se trimit ca șiruri simple, în limba backend-ului.

| Câmp | Câmp Odoo | Câmp PrestaShop | Direcție |
|------|-----------|-----------------|----------|
| ID produs | `external_id` (legătură) | `id` | ambele |
| Denumire produs | `name` | `name` (traductibil) | ambele |
| Referință internă | `default_code`, `external_code` (legătură) | `reference` | ambele |
| Preț de vânzare | `list_price` | `price` (fără TVA) | ambele (importul adaugă TVA cu **Tax included**; exportul ia prețul din lista backend-ului) |
| Cod de bare | `barcode` | `ean13` | ambele |
| Greutate | `weight` | `weight` | ambele |
| Publicat | `active` | `active` | Odoo → PrestaShop |
| Descriere site | `website_description` | `description` (traductibil) | ambele |
| Descriere scurtă | `description_sale` | `description_short` (traductibil) | Odoo → PrestaShop |
| Meta titlu | `website_meta_title` | `meta_title` (traductibil) | ambele |
| Meta descriere | `website_meta_description` | `meta_description` (traductibil) | ambele |
| Meta cuvinte-cheie | `website_meta_keywords` | `meta_keywords` (traductibil) | ambele |
| Categorii eCommerce | `public_categ_ids` | `associations.categories` | ambele (cu **Use public category**) |
| Caracteristici | valori `product.attribute.value`, prin `marketplace.product.attribute.value` (`product_feature_values`) | `associations.product_features` | PrestaShop → Odoo |
| Atribute de variantă | `attribute_line_ids`, prin `marketplace.product.attribute.value` (`product_option_values`) | `associations.product_option_values` | PrestaShop → Odoo |
| Variante | legături `marketplace.product` | `associations.combinations`, `/combinations` | PrestaShop → Odoo |
| Referință variantă | `default_code`, `external_code` (legătură) | `/combinations` `reference` | PrestaShop → Odoo |
| Preț variantă | `list_price` | `/combinations` `price` | PrestaShop → Odoo |
| Accesorii | `accessory_product_ids` | `associations.accessories` | PrestaShop → Odoo |
| Imagine principală | `image_1920` | `id_default_image`, `/images/products/{id}` | ambele |
| Imagini suplimentare | înregistrări `product.image` | `associations.images` | ambele |
| Stoc | `odoo_stock` (legătură), `external_quantity` (`marketplace.stock`) | `/stock_availables` `quantity` | ambele |

#### 5. Conexiuni

- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): conector marketplace analog, pentru Shopify.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector marketplace analog, pentru eMAG.
- [deltatech_marketplace_woocommerce](../deltatech_marketplace_woocommerce/index.md): conector marketplace analog, pentru WooCommerce.
- [deltatech_marketplace_merchantpro](../deltatech_marketplace_merchantpro/index.md): conector marketplace analog, pentru MerchantPro.
- [deltatech_marketplace_trendyol](../deltatech_marketplace_trendyol/index.md): conector marketplace analog, pentru Trendyol.
- `deltatech_marketplace`: cadrul de bază marketplace (backend, job-uri, rate-limiting, indicator de sănătate).
- `deltatech_marketplace_sale` / `_sale_stage` / `_delivery` / `_payment` / `_website`: comenzile importate, fazele de vânzare pe care se mapează statusurile PrestaShop, curierii, metodele de plată și integrarea de site.
- `deltatech_marketplace_purchase`: latura de achiziții a ecosistemului de conectori.
