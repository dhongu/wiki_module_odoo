# Conector Marketplace MerchantPro (localizat la `deltatech_marketplace_merchantpro/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_merchantpro`
- **Versiune:** `19.0.0.0.17`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_merchantpro
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_merchantpro`
- **Ultima Ingestie:** `2026-08-26`
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
- **Respectarea limitelor de rată**: limitele publicate de MerchantPro (4/s, 80/min, 3600/oră, 60000/zi) sunt respectate printr-un token-bucket comun; la HTTP 429 se citește timpul de așteptare din `error.details.reset_time` (sau se folosește un fallback de 60s) și jobul se reprogramează prin `queue_job` în loc să eșueze definitiv.

**Corecții față de versiunea anterioară a acestei pagini:** nu există niciun buton „Import All" pentru Product Template/Sale Order/Public category (framework-ul îl afișează doar dacă există o metodă `mp_import_all`, pe care acest conector nu o implementează pentru niciun tip); importul de produse nu atașează categoria pe legătura Odoo (bug de cod cunoscut, nu funcționalitate); lista de prețuri a backend-ului nu este sursa prețului exportat, ci doar filtrul de selecție a produselor „modificate"; importul paginat de comenzi nu este o plasă de siguranță completă, fiind limitat de `shipping_status`.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- `queue_job` (dependență tehnică, folosită pentru import/export paginat și pentru `RetryableJobError` la limita de rată)

#### 4. Componente Cheie

*Conform fluxului de ingestie, secțiunile 'Sumar' și 'Funcționalități Cheie' au fost preluate din `readme/DESCRIPTION.md` (corectat unde textul original nu mai reflecta comportamentul real al codului — vezi nota din secțiunea 2), iar analiza detaliată a codului pentru componente a fost omisă deoarece Readme-ul nu o solicită explicit.*

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază pentru conectori de marketplace (backend, indicator de sănătate, job-uri, rate-limiting, webhook) pe care acest modul îl specializează pentru MerchantPro.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): comanda de vânzare Odoo generată din comanda MerchantPro, politica de confirmare, repararea prețurilor de import (`action_fix_import_prices`).
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): metoda de plată și jurnalul „Marketplace Payment" (`MRPY`) create automat la prima comandă plătită importată.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): potrivirea transportatorului după nume exact, cu fallback pe „Free Delivery".
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): legătura de categorie publică (`marketplace.public.category`) pentru integrarea cu website-ul Odoo.
- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md): modul înrudit din suita de conectori marketplace pentru fluxul de achiziții.
