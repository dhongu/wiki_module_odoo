# EMAG Marketplace Connector (localizat la `deltatech_marketplace_emag/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_emag`
- **Versiune:** `19.0.2.13.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_emag
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_emag`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un cont de seller eMAG lângă Odoo, fără conector, înseamnă catalog, comenzi și stoc ținute manual în două locuri — și, spre deosebire de un magazin propriu, prețul afișat pe eMAG nu e neapărat cel pe care îl vede primul cumpărătorul: o ofertă mai bine clasată pe același produs câștigă butonul „Adaugă în coș" (buy box). Modulul închide acest gol pentru piața din România specific: produsele, categoriile (cu caracteristicile lor obligatorii), comenzile, retururile și stocul circulă automat între Odoo și eMAG, iar adresele de livrare cu geografia românească (județe, localități, sectoarele Bucureștiului) se potrivesc automat cu identificatorii eMAG. Conectorul se leagă de același framework comun (`deltatech_marketplace`) folosit și de conectorii Shopify, WooCommerce sau Magento, deci adăugarea eMAG lângă un canal deja folosit nu înseamnă învățarea unui al doilea sistem.

Începând cu `19.0.2.5.0`, emiterea propriu-zisă a AWB-urilor (etichete, urmărire, conturile de curier) a fost mutată într-un modul separat, [deltatech_marketplace_emag_delivery](../deltatech_marketplace_emag_delivery/index.md), care se instalează automat alături de acest conector oriunde e prezent `deltatech_delivery` — un seller care livrează cu propriul curier nu mai primește ecranele eMAG de AWB.

#### 2. Funcționalități Cheie

- **Sincronizare bidirecțională**: produsele, comenzile și informațiile de livrare circulă automat între Odoo și eMAG; stocul se exportă periodic, la un interval configurabil, nu instantaneu la fiecare mișcare.
- **Gestiune produse**:
  - Export detalii produs, specificații și imagini către eMAG (câmpurile de documentație sunt acceptate de eMAG doar cât timp oferta e nouă sau încă editabilă)
  - **Map Products** (din 19.0.2.9.0, meniul cardului **Products**): leagă produsele Odoo de ofertele deja existente pe eMAG fără import — referința internă ca part number (și ca PNK, cu *Mapping product code* = SKU), codul de bare prin catalogul eMAG (`find_by_eans`), apoi oferta seller-ului după PNK; doar coduri exacte și oferte active; legătura primește id-ul ofertei, PNK, part number și prețurile, deci exporturile de stoc/preț merg imediat
  - Gestionarea variantelor de produs și a categoriilor; importul aduce **întregul arbore eMAG** (câteva mii de categorii, un job per categorie) — recomandarea Terrabit e maparea manuală: un **Default category** unic pe backend, apoi maparea de mână (sau prin import Excel) doar a categoriilor efectiv folosite
  - Configurarea atributelor de produs specifice eMAG (caracteristicile obligatorii/opționale ale categoriei)
  - Crearea automată a ofertelor de produs pe eMAG, condiționată de existența unei categorii mapate
  - **Potrivirea ofertă → produs Odoo** la import, în ordine: legătura deja existentă pe backend, EAN/cod de bare, referința internă (PNK sau part number, după **Mapping product code**), PNK deja legat pe alt backend eMAG (același produs pe RO/BG/HU), în final numele exact (dacă **Strict variant match** nu e activ)
  - **Conflicte de cod de bare/SKU la import**: opțiunea backend **Refuse barcode/SKU conflicts on import** (dezactivată implicit) decide dacă o ofertă nouă cu EAN/SKU deja legat de alt produs e atașată totuși produsului (comportament vechi) sau refuzată explicit; o ofertă refuzată nu mai blochează restul paginii de import — primește propriul job (**Import Product Variant from eMAG**) care rămâne vizibil eșuat în Jobs și se reia la fiecare import următor până se corectează catalogul
- **Gestiune comenzi**:
  - Import comenzi din eMAG aflate în starea `NEW`, `IN_PROGRESS` sau `PREPARED` (filtru fix în cod, valabil și pe calea webhook) — comenzile `CANCELED`, `FINALIZED` sau `RETURNED` nu se creează niciodată ca comenzi noi în Odoo; dacă o comandă deja importată trece într-una din aceste stări, importul periodic (și webhook-ul) o preia: cea `CANCELED` e anulată în Odoo (după **Cancel Sale Order**), celelalte își actualizează doar **eMAG Status**
  - Creare automată a comenzilor de vânzare în Odoo, cu județe, localități și sectoarele Bucureștiului mapate la geografia eMAG
  - Confirmarea comenzii la import urmează setarea globală **Confirm Sale Order** a backend-ului; dezactivată, comanda rămâne ca ofertă trimisă, de confirmat manual
  - Comenzile noi sunt confirmate automat înapoi la eMAG (`/order/acknowledge`) dacă bifa **Active On Write** e activă; altfel rămân *Nouă* pe eMAG și se acceptă manual din tabloul marketplace (pasul *De acceptat*, butonul *Acceptă*) — formularul comenzii nu are un buton de acceptare
  - **Anulări venite de la eMAG** (din 19.0.2.9.4): o comandă deja importată care trece în `CANCELED` pe eMAG e anulată în Odoo conform politicii backend-ului (**Cancel Sale Order**), inclusiv la importul unei singure comenzi (callback, import după id, job); importul periodic citește în plus comenzile anulate în ultima zi, în caz că s-a pierdut callback-ul. O comandă care sosește deja anulată și nu a fost importată niciodată nu se creează. Liniile în status 0 (produs scos din comandă) nu se mai importă cu cantitate — pe o comandă confirmată se postează doar o notă. O comandă cu `cancellation_request` și fără picking făcut e anulată automat la orice import, inclusiv webhook
  - **Starea eMAG pe comanda marketplace** (19.0.2.11.0): **eMAG Status** (0 Canceled ... 5 Returned) și **eMAG Status Since** (când a văzut-o Odoo prima oară în acea stare), reîmprospătate la fiecare citire a comenzii și după fiecare stare setată de Odoo. Apar ca badge pe formular și listă, cu grupare după **eMAG Status** și filtrele **Returned on eMAG** / **Returned on eMAG, No Credit Note** (returnată pe eMAG, fără notă de credit postată). Citirea periodică a comenzilor anulate acoperă acum stările 0, 4 și 5, doar pentru comenzile deja din Odoo: cele finalizate (4) sau returnate (5) își actualizează doar starea eMAG, comanda Odoo rămâne neschimbată
  - **Termen de expediere și cerere de anulare** (19.0.2.13.0): **eMAG Shipping Deadline** (`maximum_date_for_shipment`, în UTC) și **Cancellation Requested on eMAG**; cu **Only Missing** activ, comenzile deja importate își reîmprospătează starea, termenul și cererea de anulare
  - **Trimiterea stării înapoi la eMAG** (`/order/save`, din 19.0.2.10.0): doar pentru comenzi livrate de seller (`type` 3) și doar cu **Active On Write**. Când toate livrările sunt făcute, comanda devine **Finalized** (4) dacă o factură postată e deja atașată pe eMAG, altfel **Prepared** (3); o factură trimisă ulterior o finalizează. **Cancel & Notify Marketplace** anulează comanda pe eMAG (status 0) cu **motivul** ales în dialog (câmp doar pentru comenzi eMAG, fără valoare implicită); o comandă anulată în Odoo la cererea clientului (`cancellation_request`) se anulează pe eMAG cu motivul 24 „By customer request". Fiecare salvare re-citește comanda și o trimite ca citită, cu doar `status` (și `reason_cancellation`) schimbat; nu se trimite nimic dacă eMAG are deja comanda în acea stare sau peste ea, dacă e anulată/returnată sau livrată de eMAG; o comandă încă nouă e mai întâi confirmată (acknowledge). „Cancel in Odoo Only" și anulările venite de la eMAG nu trimit nimic. eMAG acceptă anularea unei comenzi finalizate doar în primele 48 de ore
  - **Termen de retur / storno** (19.0.2.12.0): **eMAG Return Time (days)** pe backend (RT acordat clienților, gol/0 dacă e necunoscut), **Finalized on eMAG by Odoo** pe comandă (când a acceptat eMAG starea Finalized trimisă de Odoo; nesetat dacă eMAG a finalizat singur comanda) și **eMAG Storno Deadline** (calculat, nestocat: finalizare + RT + 5 zile, ultimul moment în care eMAG acceptă un storno). Deocamdată nimic nu îl folosește — e ceasul fluxului viitor colet refuzat → storno
  - **Dashboard** (`deltatech_marketplace_dashboard`, 19.0.2.13.0): pași și contoare *To acknowledge* (în română *De acceptat*, din 19.0.2.13.3; butonul de pe rând *Accept* / *Acceptă*), *Late* și *Cancellation requested*
  - **Vouchere eMAG** (carduri cadou): partea suportată de eMAG ajunge pe o linie de comandă cu valoare, pe produsul **Voucher Product** (fără taxă, cotă TVA 0 — eMAG decontează diferența separat, printr-un „decont de voucher"); partea suportată de vânzător merge pe **Discount Product**, cu TVA, ca o reducere comercială obișnuită; un voucher mixt primește ambele linii; la livrare prin locker, partea alocată taxei de transport nu apare pe factură
- **Retururi (RMA)**: `/rma/read` alimentează registrul comun `marketplace.return.request` din `deltatech_marketplace_sale` — status, ce a cerut cumpărătorul, motivul, liniile returnate cu cantități, legătura la comandă și la linia pe care a fost vândut articolul; se păstrează și tipul de fulfilment eMAG (**Fulfilled by eMAG** / **Fulfilled by seller**). Fereastra de import e limitată pe dată, nu pe status (API-ul RMA acceptă un singur status de filtru); o cerere deja în bază e re-citită la fiecare import până ajunge într-o stare finală (Refuzat/Anulat/Finalizat) — webhook-ul eMAG nu anunță acele tranziții. **Doar citire, intenționat**: `/rma/save` există, dar documentația eMAG nu clarifică cine trebuie să deschidă un retur, așa că modulul nu scrie niciodată înapoi; nu se creează picking de retur, notă de credit sau rambursare din această citire — acelea rămân manuale (vezi și puntea [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md), pentru retururile care trebuie să treacă prin fluxul de depozit).
- **Rambursări** (19.0.2.8.0): un RMA cu `return_type = 3` care are `refund_value` pe produse aduce o rambursare în `marketplace.refund`, legată de retur — câte o linie pe produs, total însumat (*Total Computed*), moneda și contul bancar al cumpărătorului. `refund_value` e text opțional, parsat defensiv; un RMA fără sume nu aduce rambursare. `return_tax_value` (taxa suportată de client la un retur refuzat) nu se mapează.
- **Traducere**: din 19.0.2.13.1 traducerea RO este completă (termenii adăugați recent — Import Localities, eMAG Warehouse ID, Import only active offers, eMAG Return Time, stările și motivele de anulare eMAG, mesajele de preț și voucher — apăreau în engleză).
- **Integrare stocuri**:
  - Export periodic, configurabil, al nivelurilor de stoc către eMAG (nu în timp real), prin API-ul „light" de ofertă (`POST /offer/save`), în loturi de 50 de oferte per request — nu câte un `PATCH` per ofertă — pentru a nu epuiza bugetul comun de 3 cereri/secundă al contului (partajat cu AWB și RMA); un lot respins de eMAG e reluat ofertă cu ofertă, ca o singură eroare să nu blocheze restul lotului
  - Un stoc Odoo negativ se trimite ca 0, nu e respins de eMAG; exportul complet respectă plafonul eMAG de 65535
  - Depozitul eMAG față de care se raportează stocul e configurabil per backend (**eMAG Warehouse ID**, implicit 1 — convenția eMAG pentru un seller cu un singur depozit)
  - Actualizări automate de stoc pentru a preveni supravânzarea
- **Buy Box Auto-Pricing**:
  - Cron opțional, dezactivat implicit (**EMAG: Set Price**), care ajustează prețul unei oferte în funcție de rangul ei în buy box-ul eMAG, plafonat între **Min sale price**/**Max sale price** configurate pe produs; reajustările sub 0,5 unități monetare sunt sărite
  - **Atenție**: dacă Min/Max sale price rămân necompletate (0) pe un produs cu Auto Price activ și rang cunoscut, cron-ul nu sare produsul — trimite efectiv prețul 0 la eMAG (și îl scrie înapoi în Odoo); limitele trebuie completate ÎNAINTE de activarea Auto Price
  - Re-ajustare recursivă limitată la 10 pași, ca să nu ruleze necontrolat; verificarea rangului se face la 15 minute după schimbarea prețului și se oprește când nu mai apare nicio modificare
  - Corecții 19.0.2.9.1: în afara buy box-ului prețul coboară cu 0,01 sub oferta care îl deține (`best_offer_sale_price`) sau la jumătatea drumului spre minim dacă acea ofertă nu e mai ieftină; exportul de preț și exportul complet nu mai anulează prețul auto-calculat; trimite 50 de oferte per request, un job per backend, fără oferte fără stoc
  - **Validarea prețurilor** (19.0.2.9.6): înainte de trimitere, toate prețurile trebuie să fie pozitive și `min_sale_price` < `sale_price` < `max_sale_price`; o ofertă care pică nu se trimite și primește o eroare în jurnalul marketplace (operația Price), nu un job reluat la nesfârșit; prețul recomandat se trimite doar dacă e peste prețul de vânzare. Intervalul ±10% la crearea ofertei se păstrează pe binding
- **Facturare**:
  - Push automat al unui **link** către PDF-ul facturii din portalul Odoo (nu conținutul PDF-ului) când o factură legată de o comandă eMAG e validată, dacă backend-ul are activă bifa **Enable Order Push Invoice** ȘI **Active On Write**; cere ca `web.base.url` să fie public — nu e depunere e-Factura/SPV
  - Fără duplicate (19.0.2.9.5): înainte de trimitere comanda e citită de la eMAG, iar un document deja atașat sub același nume nu se retrimite; dacă citirea eșuează, nu se trimite nimic și jobul se reia. Notele de credit se trimit ca facturile (`type: 1`), fiecare o singură dată
- **Plăți**:
  - Metodele de plată eMAG sunt mapate la payment provideri Odoo; metodele nerecunoscute cad pe Wire Transfer, ca o comandă să nu rămână fără metodă de plată
  - **Fără borderou/decontare prin API**: eMAG Marketplace API (v4.x) nu expune nicio resursă pentru raportul de decontare/comisioane — borderoul se obține doar prin descărcare manuală (Excel/CSV) din panoul de vânzător eMAG (Financiar > Rapoarte); conectorul nu îl importă/reconciliază automat
- **Robustețe API** (19.0.2.9.3): erorile HTTP sunt clasificate — se reiau doar 429, 5xx și erorile de transport (la 429 jobul e amânat cu `Retry-After`); 400/401/403/404/422 devin UserError cu motivul eMAG, fără a consuma limita comună. Un timeout în job dă RetryableJobError. Mesajele citesc atât `messages`, cât și `errors`. Secretele conexiunii se citesc cu `sudo()` (vizibile doar pentru Marketplace Manager)
- **Plăți eMAG** (19.0.2.8.3): cele trei moduri fixe (1 COD, 2 transfer bancar, 3 card online) sunt create de **Import basic data** pe backend, COD pe un provider Cash On Delivery ([deltatech_payment_on_delivery](../deltatech_payment_on_delivery/index.md)) când există, restul pe wire transfer; cu `keep_partner_address`, contactul de livrare se cheiază pe adresa de livrare, nu doar pe clientul eMAG
- **Geografie românească**: import al județelor (create automat ca `res.country.state`) și al localităților/sectoarelor Bucureștiului de pe `/locality`, prin butonul **Get city** de pe metoda de livrare eMAG (din `deltatech_marketplace_emag_delivery`) — pas manual, unic per backend, obligatoriu înainte de primul AWB
- **Operațiuni programate**:
  - Sincronizare în fundal prin job-uri cron și coada de job-uri comună; joburile de import paginat, webhook-ul de rezervă, acknowledge-ul comenzii și exportul de măsurători folosesc `identity_key`, ca un import reluat să nu dubleze job-uri
  - Intervale de sincronizare configurabile; cron-ul de auto-pricing pe buy box vine dezactivat implicit

#### 3. Dependențe

- `sale`
- `delivery`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Modulul este construit peste cadrul marketplace al Deltatech și implementează adaptoare și binder-e specifice cerințelor API ale eMAG. Conform documentației din `readme/DESCRIPTION.md`, implementarea urmează o abordare modulară cu separarea responsabilităților:

- **Backend Adapter**: gestionează comunicarea API cu eMAG (`https://marketplace-api.emag.ro/api-3`), autentificare Basic Auth (nu API key, nu OAuth); rate-limiting-ul (3 apeluri/secundă cumulat, per cont eMAG) e generic, moștenit din `deltatech_marketplace` (token bucket) — partajat între catalog, comenzi, stoc, RMA și AWB.
- **Modele de binding (binding)**: leagă entitățile Odoo de omoloagele lor din eMAG — binding de produs (`binding_product.py`), comandă (`binding_sale_order.py`), categorie (`binding_product_category.py`), cerere de retur (`binding_return_request.py`) și metodă de plată (`binding_payment_acquirer.py`); AWB și transportator eMAG au fost mutate în `deltatech_marketplace_emag_delivery`.
- **Servicii de sincronizare**: gestionează fluxul de date între sisteme; webhook-ul care primește push-uri de comenzi de la eMAG este un controller comun din `deltatech_marketplace`, nu unul definit de acest modul.
- **Job-uri programate**: automatizează sincronizarea în fundal — `ir_cron_emag_set_price` (definit în `data/ir_cron_data.xml`) rulează auto-pricing-ul pe buy box (dezactivat implicit).

Pentru detalii suplimentare de configurare și operare, modulul include un manual de utilizare („Manual utilizare eMAG Marketplace.docx"), un ghid `readme/CONFIGURE.md` și un ghid pas-cu-pas `readme/USAGE.md`.

**Mapare câmpuri produs**

Documentată integral în `readme/USAGE.md` (secțiunea „Product field mapping"), derivată din `emag_job_import()`, `emag_get_price()`, `emag_write()`, `emag_export_stock()` și `emag_export_price()`. eMAG lucrează cu *oferte* pe un catalog existent: câmpurile de documentație (denumire, marcă, descriere, imagini, caracteristici) sunt acceptate doar cât timp oferta e nouă sau încă editabilă.

| Câmp | Câmp Odoo | Câmp eMAG | Direcție |
|------|-----------|-----------|----------|
| ID ofertă | `external_id` (legătură) | `id` | ambele |
| Denumire ofertă | `name` | `name` | ambele |
| PNK | `external_code` (legătură, **PNK**) | `part_number_key` | eMAG → Odoo |
| Part number | `external_part_number` (legătură) | `part_number` | ambele (export doar la crearea ofertei) |
| Referință internă | `default_code` | `part_number_key` sau `part_number`, după **Mapping product code** | eMAG → Odoo |
| Cod de bare (EAN) | `barcode` | `ean[]` | ambele (export doar la crearea ofertei) |
| Preț de vânzare | `sale_price` (legătură), `list_price` | `sale_price` | ambele |
| Preț minim / maxim | `min_sale_price`, `max_sale_price` (legătură) | `min_sale_price`, `max_sale_price` | ambele (la creare, ±10% din prețul Odoo) |
| Preț recomandat | `recommended_price` (legătură, doar citire); exportul trimite `list_price` | `recommended_price` | ambele |
| Cea mai bună ofertă | `best_offer_sale_price`, `best_offer_recommended_price` (legătură) | aceleași | eMAG → Odoo |
| Poziție buy-box | `buy_button_rank` (legătură) | `buy_button_rank` | eMAG → Odoo |
| Stare ofertă | `emag_active` (legătură) | `status` (1 = activă) | ambele (exportul trimite mereu 1) |
| Stoc | `odoo_stock`, `external_stock` (legătură) | `stock[].value` (`/offer_stock` sau `/offer/save`, în loturi de 50), `general_stock` | ambele |
| Categorie | `categ_id`, prin `marketplace.product.category` | `category_id` | ambele (exportul eșuează dacă nu e mapată) |
| Marcă | `get_brand_name()` (`deltatech_brand_field`), altfel numele companiei | `brand` | Odoo → eMAG |
| Greutate | `weight` (kg) | `weight`; `/measurements` `weight` (g) | Odoo → eMAG |
| Dimensiuni | `product_length`, `product_width`, `product_height` (cm) | `/measurements` `length`, `width`, `height` (mm) | Odoo → eMAG |
| Descriere | `website_description` | `description` | ambele |
| Imagine principală | `image_1024` (trimisă ca URL Odoo) | `images[]` cu `display_type` 1 | ambele |
| Imagini suplimentare | înregistrări `product.image` | `images[]` cu `display_type` 0 | ambele |
| Caracteristici | `attribute_line_ids`, prin `marketplace.product.attribute(.value)` | `characteristics[].id`, `characteristics[].value` | ambele (valorile nemapate sunt sărite și logate) |
| Familie (variante) | legătura de șablon `marketplace.product.template` | `family.id`, `family.name` | eMAG → Odoo |
| URL produs | URL-ul de site al produsului (`/shop/...`) | `url` | Odoo → eMAG |
| Cotă TVA | fix (`vat_id` 1) | `vat_id` | Odoo → eMAG |
| Monedă | fix (RON) | `currency_type` | Odoo → eMAG |

**Retururi (RMA) — mapare de status**

Din `binding_return_request.py`: cele șapte statusuri eMAG sunt mapate pe vocabularul comun `marketplace.return.request` — `1 Incomplete`/`2 New` → *Requested*, `3 Acknowledged` → *Approved*, `4 Refused` → *Rejected*, `5 Canceled` → *Cancelled*, `6 Received` → *Received*, `7 Finalized` → *Done*. Un status necunoscut e logat și păstrat vizibil pe **External Status**, nu ascuns în valoarea implicită.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace peste care este construit conectorul (backend, indicator de sănătate, job-uri, rate-limiting).
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): comanda de vânzare Odoo generată din comanda eMAG importată, și registrul comun `marketplace.return.request` alimentat de importul de retururi.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): maparea transportatorului și linia de livrare pe comandă.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): maparea metodei de plată eMAG către payment provider Odoo (fallback pe Wire Transfer).
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): link-ul de produs eMAG folosește rutele website-ului Odoo la export.
- [deltatech_delivery](../deltatech_delivery/index.md): contractul de capabilități al curierilor (`cities`, `ship`, `tracking`) folosit de metoda de livrare eMAG.
- [deltatech_marketplace_emag_delivery](../deltatech_marketplace_emag_delivery/index.md): emiterea efectivă a AWB-urilor (etichete PDF/ZPL, urmărire, conturi de curier), scoasă din acest modul în `19.0.2.5.0`; se instalează automat alături de acest conector oriunde e prezent `deltatech_delivery`.
- [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md): puntea care duce retururile eMAG importate aici (`marketplace.return.request`) pe fluxul de depozit al [deltatech_rma](../deltatech_rma/index.md) — recepție prin scanare, verificare, transfer de retur, notă de credit — fără ca acest conector să scrie vreodată înapoi în eMAG.
- `l10n_ro_edi` / `l10n_ro_edi_stock`: e-Factura (SPV) și eTransport — rămân neatinse de acest conector; push-ul de factură eMAG e doar un link către PDF, nu o depunere SPV.
- [deltatech_marketplace_dashboard](../deltatech_marketplace_dashboard/index.md): tabloul de bord comun primește de la acest conector pașii și contoarele *To acknowledge*, *Late* și *Cancellation requested* (legătură opțională, nu dependență).
