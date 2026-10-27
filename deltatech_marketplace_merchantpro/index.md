# Conector Marketplace MerchantPro (localizat la `deltatech_marketplace_merchantpro/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_merchantpro`
- **Versiune:** `19.0.0.0.23`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_merchantpro`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_merchantpro`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

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
- **Reparare la cerere a prețurilor importate**: acțiunea `action_fix_import_prices` reia comenzile dintr-un interval și rescrie prețurile de produs și de transport (rulare în gol disponibilă); nu este programată automat.
- **Cozi de lucru per magazin**: importurile sunt identificate pe backend și pagină, deci un magazin nu le blochează pe ale altuia; secretele conexiunii sunt vizibile doar managerilor de marketplace, iar fluxurile rulează oricum pentru ceilalți utilizatori.
- **Respectarea limitelor de rată**: limitele publicate de MerchantPro (4/s, 80/min, 3600/oră, 60000/zi) sunt respectate printr-un token-bucket comun; la HTTP 429 se citește timpul de așteptare din `error.details.reset_time` (sau se folosește un fallback de 60s) și jobul se reprogramează prin `queue_job` în loc să eșueze definitiv.

**Corecții față de versiunea anterioară a acestei pagini:** nu există niciun buton „Import All" pentru Product Template/Sale Order/Public category (framework-ul îl afișează doar dacă există o metodă `mp_import_all`, pe care acest conector nu o implementează pentru niciun tip); importul de produse nu atașează categoria pe legătura Odoo (bug de cod cunoscut, nu funcționalitate); lista de prețuri a backend-ului nu este sursa prețului exportat, ci doar filtrul de selecție a produselor „modificate"; importul paginat de comenzi nu este o plasă de siguranță completă, fiind limitat de `shipping_status`.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)

`queue_job` nu este declarat în manifestul acestui modul, dar codul îl folosește (`RetryableJobError`, canale și funcții de job); vine tranzitiv prin cadrul `deltatech_marketplace`.

#### 4. Componente Cheie

*Conform fluxului de ingestie, secțiunile 'Sumar' și 'Funcționalități Cheie' au fost preluate din `readme/DESCRIPTION.md` și `readme/USAGE.md` (corectate unde textul original nu reflecta comportamentul real al codului — vezi nota din secțiunea 2), iar analiza detaliată a codului pentru componente nu este cerută explicit de Readme; mai jos este doar structura modulului.*

**Modele** (toate extind modele ale cadrului `deltatech_marketplace`)

- `marketplace.backend`: conexiunea MerchantPro (API V2, limite de rată); include `action_fix_import_prices(days, dry_run)`, reparare la cerere a prețurilor de produs și de transport importate greșit, rulată ca job-uri, livrată fără cron activ.
- `marketplace.product.template`: legătura de produs, import/export, `mp_export_price` (export de preț pe traseul standard) și `mp_call_inventory` (stoc).
- `marketplace.public.category`: legătura de categorie, import/export cu ierarhie.
- `marketplace.sale.order`: importul comenzilor din webhook sau din jobul paginat și sincronizarea stărilor.
- `marketplace.payment.provider`: potrivirea metodei de plată.
- `backend_adapter.py`: clientul API, cu tratarea HTTP 429 prin `RetryableJobError`.

**Vizualizări**

Modulul nu adaugă vizualizări XML; datele conțin doar `data/job_function.xml`.

**Acțiuni Automate / Acțiuni Server**

- `data/job_function.xml`: canalele de job `channel_mp_inbound` și `channel_mp_outbound` și funcțiile de job pentru importul comenzilor, importul produselor și categoriilor după id și exportul de stoc. Modulul nu livrează cron-uri proprii; cronul „Marketplace: export stock” este al cadrului și vine dezactivat.

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

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază pentru conectori de marketplace (backend, indicator de sănătate, job-uri, rate-limiting, webhook) pe care acest modul îl specializează pentru MerchantPro.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): comanda de vânzare Odoo generată din comanda MerchantPro, politica de confirmare, repararea prețurilor de import (`action_fix_import_prices`).
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): metoda de plată și jurnalul „Marketplace Payment" (`MRPY`) create automat la prima comandă plătită importată.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): potrivirea transportatorului după nume exact, cu fallback pe „Free Delivery".
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): legătura de categorie publică (`marketplace.public.category`) pentru integrarea cu website-ul Odoo.
