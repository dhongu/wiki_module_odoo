# Conector Shopify Marketplace (localizat la `deltatech_marketplace_shopify/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_shopify`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_shopify
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_shopify`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectorul Shopify Marketplace dezvoltat de Terrabit creează o integrare directă și fluidă între sistemul ERP Odoo și platforma de magazine online Shopify. Modulul permite companiilor să sincronizeze și să gestioneze magazinele lor Shopify direct din Odoo, oferind o soluție unificată pentru administrarea produselor, clienților, comenzilor și retururilor. Astfel, echipele pot opera magazinul online fără a comuta între platforme, păstrând o singură sursă de adevăr pentru informațiile despre produse și clienți, reducând introducerea manuală a datelor și eliminând discrepanțele. Modulul rulează integral pe API-ul modern GraphQL Admin al Shopify (versiunea API declarată `2026-07`, cu avertizare automată înainte ca versiunea să expire), fiind gândit ca produs vandabil pe Odoo Apps Store — se instalează doar On-Premise sau pe Odoo.sh (nu pe Odoo Online/SaaS) și se integrează în același framework comun `deltatech_marketplace` folosit și de conectoarele eMAG, WooCommerce ș.a.

#### 2. Funcționalități Cheie

- **Sincronizare produse**:
  - Export de șabloane și variante de produs din Odoo către Shopify (creare și actualizare), cu imagini și stoc inițial.
  - Import de șabloane de produs, variante și imagini din Shopify.
  - Sincronizarea bidirecțională a prețurilor și a informațiilor de bază (cod de bare, greutate, SKU), pe fiecare variantă.
  - Suport pentru imagini multiple per șablon de produs și asocierea imaginilor cu variante specifice.
  - Actualizări în timp real ale produselor prin webhook (`products/update`).
  - Un produs cu mai multe variante Shopify, importat fără opțiunea **Options as Attributes** activată, tot se importă — dar variantele lui sunt sărite (avertisment doar în log-ul serverului), niciodată fuzionate tăcut într-o singură variantă.
  - Potrivirea unui produs Shopify cu un șablon Odoo deja existent se face acum și prin SKU/cod de bare al oricărei variante, înainte de a recurge la potrivirea exactă pe nume — evită duplicate atunci când același produs a fost creat independent în cele două sisteme (ex. produs importat din eMAG în Odoo, creat manual în Shopify cu SKU/cod de bare identic pe variante).

- **Atribute de produs**:
  - Import al atributelor de produs (opțiuni Shopify) și al valorilor lor.
  - Maparea opțiunilor/variantelor Shopify la atributele de produs din Odoo, cu control asupra modului de creare a variantelor (dinamic sau instant).

- **Integrare clienți**:
  - Import al clienților Shopify în baza de contacte Odoo, cu actualizări în timp real prin webhook (`customers/update`).
  - Menținerea unor înregistrări de client consistente între platforme.
  - Detectarea automată a companiilor pe baza atributelor din nota Shopify sau a câmpului de companie.

- **Gestionarea comenzilor**:
  - Import al comenzilor de vânzare din Shopify în Odoo (creare automată a comenzilor Odoo).
  - Filtrarea comenzilor importate după status (deschisă/arhivată/anulată), stare de plată și stare de livrare, configurabile per magazin — traduse separat pentru fiecare transport, deoarece REST și GraphQL folosesc cuvinte diferite pentru aceeași stare (o alegere netradusă ar fi ignorată tăcut de Shopify).
  - Aplicarea automată a fazelor de vânzare (Sale Phases) din etichetele (tags) comenzii Shopify, la fiecare import/reîmprospătare — fără pas manual de import separat; doar tag-urile deja mapate la o fază sunt luate în calcul.
  - Sincronizarea anulării comenzilor în ambele sensuri: o comandă anulată în Odoo se anulează și în Shopify, iar o comandă anulată în Shopify (câmpul `cancelledAt`) e citită și aplică anularea și în Odoo la următorul import/reîmprospătare.
  - O comandă deja încasată (`PAID`/`PARTIALLY_PAID`/`PARTIALLY_REFUNDED` sau tranzacție Odoo capturată) nu mai este anulată automat în Shopify — `orderCancel` ar rambursa încasarea, ceea ce ar trimite o rambursare neceruta clientului; comanda rămâne anulată doar în Odoo, cu motivul în chatter. O comandă doar autorizată (`AUTHORIZED`) se anulează în continuare (Shopify anulează autorizarea, fără rambursare).
  - Suport pentru webhook-uri Shopify (`orders/create`, `orders/updated`, `orders/paid`, `orders/cancelled`) pentru actualizarea automată a comenzilor în Odoo.
  - Rutarea depozitului comenzii pe baza locației Shopify (`location_id` / locația de onorare), prin binding-ul `marketplace.warehouse` — comenzile din locații nemapate cad pe depozitul implicit; opțiunea **Skip location lookup** de pe backend sare peste interogarea locației atunci când aplicația nu are permisiunea `read_locations`, ca să nu mai apară o cerere refuzată la fiecare restart de worker.
  - Verificarea totalului comenzii importate față de totalul Shopify, cu raportare a diferențelor în chatter.
  - Reguli de protecție la re-import: pe o comandă ale cărei valori sunt marcate ca „discarded" (backend `only_missing` sau „No Refresh" pe comandă), doar locker-ul, curierul și liniile de livrare deschise mai sunt actualizate — restul (linii, sume, fază, adrese) rămân neatinse.
  - **Export opțional al liniilor de comandă** (**Export Order Lines**, oprit implicit): o cantitate schimbată, o linie adăugată sau ștearsă în Odoo se trimite înapoi în Shopify prin API-ul de editare a comenzii (`orderEditBegin` → `orderEditSetQuantity`/`orderEditAddVariant` → `orderEditCommit`). Necesită permisiunea `write_order_edits`, separată de `write_orders` și care trebuie acordată explicit magazinului (re-autorizare); fără ea exportul e inert și motivul apare în chatter, fără reîncercare. Nu se trimite nimic dacă modificarea nu poate fi exprimată de API (cantitate sub ce e deja onorat/rambursat, produs fără variantă Shopify mapată, comandă cu peste 250 de linii) sau dacă pe o comandă deja plătită editarea ar lăsa un sold necompensat (Shopify nu încasează/rambursează diferența la editare) — o modificare care se echilibrează la zero trece și pe o comandă plătită. Prețul unitar al unei linii existente nu poate fi trimis (API-ul Shopify oferă doar o reducere peste prețul original); o schimbare de preț în Odoo e semnalată pe comandă, dar nu blochează exportul cantităților/liniilor.

- **Retururi (RMA)**:
  - Import al retururilor Shopify în registrul comun `marketplace.return.request` din `deltatech_marketplace_sale`: status, motive și cantități pe fiecare linie, legătura la comandă și la linia pe care a fost vândut articolul.
  - Cele cinci stări Shopify se mapează pe vocabularul comun folosit de toate conectoarele (`REQUESTED` → Solicitat, `OPEN` → Aprobat, `CLOSED` → Finalizat, `DECLINED` → Respins, `CANCELED` → Anulat).
  - Shopify nu are un query de retururi la nivel de magazin — un retur e accesibil doar prin `Order.returns` — așa că importul listează comenzile (filtrate cu `-return_status:no_return`) și citește retururile din interiorul aceleiași interogări, în loc de un apel per comandă; fereastra de import se bazează pe data ultimei actualizări (`updated_at`), nu pe data creării, ca să nu piardă retururile deschise târziu.
  - **Doar citire, intenționat**: mutațiile de retur (`returnApproveRequest`, `returnDeclineRequest`, `returnProcess`) decid ce se întâmplă cu banii clientului, iar rularea lor automată ar lua decizia comercială în locul magazinului — aprobarea rămâne în Shopify. Nu se creează picking de retur, notă de credit sau rambursare din retur; partea de stoc și contabilitate rămâne gestionată manual.
  - Produsul returnat se ia din linia vândută (`fulfillmentLineItem.lineItem`), nu prin potrivire pe cod, deci o comandă cu același articol pe două linii nu e ambiguă. Tipul de retur e marcat *Schimb* când returul are linii de schimb; absența lor nu e citită automat ca rambursare — câmpul rămâne gol dacă returul nu e încă decis.
  - Nu există import al unui singur retur după id (Shopify nu expune un asemenea query) — reîmprospătarea se face prin importul pe fereastră, care recitește oricum tot ce nu s-a închis încă.

- **Registru de permisiuni (scopes)**:
  - Permisiunile pe care Shopify le raportează pentru instalare sunt citite la fiecare test de conexiune și la fiecare reîmprospătare de token și păstrate pe backend: **Granted Access Scopes** e lista efectivă, **Missing Scopes** numește ce cer opțiunile pornite pe acest magazin dar nu au fost acordate — o permisiune lipsă devine o propoziție pe backend, nu doar un „Access denied" descoperit la prima utilizare.
  - Permisiunile aparțin *instalării*, nu versiunii aplicației: publicarea unei versiuni cu o permisiune nouă nu o acordă automat — instalarea existentă păstrează drepturile vechi până când magazinul aprobă actualizarea de acces la date.

- **Plăți și livrare**:
  - Import și mapare a metodelor de plată (payment acquirers) din Shopify.
  - Sincronizarea stării financiare a comenzii (`financial_status`) cu tranzacția de plată din Odoo.
  - Maparea automată a curierilor și crearea/actualizarea liniilor de livrare pe comenzi.
  - Suport pentru puncte de ridicare (lockere) preluate din notele Shopify, stocate pe `marketplace.sale.order.marketplace_locker` — conectorul nu mai depinde de suita de curierat Terrabit pentru a importa punctul de ridicare; unde suita e instalată, codul e replicat pe comandă și pus pe AWB ca înainte.
  - Trimiterea numerelor de tracking (AWB) către Shopify prin API-ul `FulfillmentV2`, cu declanșator configurabil (la crearea AWB sau la validarea transferului) și suport pentru onorări parțiale; rulează asincron prin `queue_job`, cu reîncercare automată la eșec.

- **Stoc și prețuri**:
  - Export al cantităților de stoc din Odoo către Shopify prin API-ul `InventoryLevel`, cu suport multi-locație (o locație Shopify = un depozit Odoo, mapare 1-la-1, fără granularitate suplimentară pe `stock.location`).
  - Export al prețurilor per variantă sau la nivel de șablon de produs (un magazin sincronizat la nivel de șablon nu mai trebuie să sincronizeze și variantele doar ca să trimită un preț) din lista de prețuri Odoo, cu setare automată a `compare_at_price` la discount; pornește doar pentru variantele cu diferență de preț. Un backend cu propria listă de prețuri (`pricelist_id` + `price_per_product`, setarea Shopify obișnuită) exportă din acea listă, niciodată din prețul simplu de vânzare al produsului — modificarea prețului pe formularul obișnuit de produs nu are niciun efect vizibil asupra exportului; prețul trimis se schimbă doar prin câmpul **Odoo Price** al binding-ului sau direct pe lista de prețuri.
  - Import de preț: cu **Update Price Only** activat pe backend, webhook-ul `products/update` scrie doar prețul, lăsând referința internă, codul de bare și greutatea neatinse — util când Odoo rămâne proprietarul datelor de produs, dar prețul se decide în Shopify; **Ignore Price** are prioritate, atât pe produs cât și în lista de prețuri.
  - Suport pentru comenzi în monedă diferită de moneda magazinului (multi-valută), prin binding-uri `marketplace.product.pricelist` pe cod ISO de monedă.
  - Import al Codului Vamal (HS Code) și al Țării de Origine de pe `InventoryItem` Shopify, direct pe `product.template`; când e instalat modulul Enterprise `account_intrastat`, se completează la fel și `intrastat_code_id`/`intrastat_origin_country_id`.

- **Depozite / locații**:
  - Import al locațiilor Shopify ca binding-uri de depozit (`marketplace.warehouse`), o locație Shopify = un depozit Odoo — mapare pe care se bazează atât exportul de stoc, cât și rutarea comenzilor; depozitele Odoo trebuie create *înainte* de acest import.

- **Autentificare și operații automate**:
  - Suport pentru două moduri de autentificare, alese din câmpul **Access Type**: Legacy Private Apps (token permanent, `Access Token` completat manual — de la 1 ianuarie 2026 Shopify nu mai permite crearea de aplicații legacy noi, doar cele existente anterior rămân utilizabile) și Dev Dashboard Apps (OAuth `client_credentials`, `Client Id`/`Client Secret`, token cu expirare la 24h, cu reîmprospătare automată sub 30 minute rămase și proactiv la fiecare 23 de ore prin job-ul „Shopify: Refresh Access Tokens").
  - `Client Secret` este necesar și pentru verificarea semnăturii HMAC (`X-Shopify-Hmac-Sha256`) a webhook-urilor primite — fără el, verificarea eșuează silențios (doar avertisment în log).
  - Sincronizare programată și asincronă prin `queue_job`, cu retry automat la limitări de rată (HTTP 429 / GraphQL `THROTTLED`) și erori de server.
  - Import de colecții Shopify (custom și smart) ca și categorii publice de produs.
  - Fiecare subsistem (produse, stoc, expediere, clienți, comenzi, webhook-uri) are propriul comutator GraphQL/REST pe backend, implicit oprit — tranziția se face treptat, subsistem cu subsistem, reversibilă dintr-un singur comutator.
  - Indicator de sănătate (verde/portocaliu/roșu/gri) pe cardul kanban al backend-ului, cu ora ultimei sincronizări și linkuri către log-uri/job-uri eșuate din ultimele 24h.
  - Wizard **Check webhooks** (buton de antet) care compară webhook-urile efectiv înregistrate în Shopify cu cele așteptate de Odoo (Matched/Missing/Orphan), cu remediere directă (înregistrare sau ștergere din Shopify). Un webhook blocat pe „Missing" la nesfârșit este aproape mereu parametrul de sistem `web.base.url` setat pe `http://` în loc de `https://` — API-ul Admin al Shopify refuză tăcut să înregistreze un webhook a cărui adresă de callback nu e HTTPS, fără nicio eroare vizibilă în Odoo.
  - Buton **Test connection** care validează credențialele printr-un query GraphQL `shop`, înainte de orice import.

- **Rambursări** (19.0.1.3.0): import din `Order.refunds` pe comenzile rambursate / parțial rambursate din fereastra de retururi, câte un `marketplace.refund` per `Refund` — totalul raportat (`totalRefundedSet`), TVA-ul, transportul rambursat și, pe linie, suma, TVA-ul și dacă marfa s-a întors în stoc (`restockType`). Legat de retur când îl numește; o rambursare fără retur (cazul normal la Shopify) rămâne fără. Rulează din același cron ca retururile.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)

Dependență externă Python: `ShopifyAPI`.

#### 4. Componente Cheie

**Modele**

- `marketplace.backend` (extins, `backend.py`): configurarea specifică Shopify a backend-ului — credențiale (token permanent sau OAuth, `Access Type`), opțiuni de import/export (atribute din opțiuni, creare variante, categorie publică, tip produs ca și categorie internă), comutatoare GraphQL per subsistem, filtre de comandă, declanșator de onorare, reîmprospătare token, permisiuni acordate/lipsă (`Granted Access Scopes`/`Missing Scopes`), opțiunea `shopify_skip_location_lookup`, indicator de sănătate.
- `backend_adapter.py`: adaptorul de comunicare REST cu API-ul Shopify (autentificare, apeluri cu retry la rate-limit/erori de server).
- `shopify_graphql.py` și modulele `shopify_graphql_*.py` (`catalog`, `customer`, `fulfillment`, `inventory`, `order`, `order_edit`, `product`, `return`, `webhook`): mixin-uri cu interogările/mutațiile GraphQL Admin API pentru fiecare subsistem, folosite ca alternativă la transportul REST, activabile per comutator pe backend. `order_edit` conține mutațiile Order Editing API (`orderEditBegin`/`orderEditSetQuantity`/`orderEditAddVariant`/`orderEditCommit`) pentru exportul opțional de linii; `return` conține query-ul de retururi (`Order.returns`, doar citire).
- `shopify_order_filters.py`: traducerea filtrelor de listare a comenzilor (status/plată/livrare) între vocabularul REST și cel GraphQL.
- `binding_product_template.py` / `binding_product.py`: binding-uri de șablon și variantă de produs, inclusiv import/export atribute, opțiuni, imagini, stoc (`shopify_import_stock`, `shopify_stock_export`), preț și potrivirea unui produs Shopify cu un șablon Odoo existent prin SKU/cod de bare al variantelor.
- `binding_product_image.py`: binding pentru imaginile de produs, cu asociere pe variante.
- `binding_attribute.py`: binding pentru atributele de produs (opțiunile Shopify).
- `binding_customers.py`: binding pentru clienți și adresele lor.
- `binding_sale_order.py`: binding pentru comenzi de vânzare — import, rutare depozit, verificare total, anulare bidirecțională (cu protecție pe comenzi deja încasate), export opțional de linii, protecție la re-import pe comenzi „discarded".
- `binding_sale_stage.py`: binding pentru fazele de vânzare (etichete/tags Shopify → `marketplace.sale.phase`).
- `binding_payment_acquirer.py`: binding pentru metodele de plată.
- `binding_public_category.py`: binding pentru colecțiile Shopify importate ca și categorii publice.
- `binding_warehouse.py`: binding pentru locațiile Shopify mapate la depozitele Odoo (`marketplace.warehouse`).
- `binding_return_request.py` (extinde `marketplace.return.request` din `deltatech_marketplace_sale`): importul retururilor Shopify pe fereastră de dată, potrivirea liniei vândute, marcarea stărilor „settled" ca să nu se recitească la nesfârșit — fără cale de import după id, doar pe fereastră.
- `stock_picking.py`: extensie pentru trimiterea AWB-urilor și a onorărilor (fulfillment) către Shopify la validarea transferului.

**Vizualizări**

- `backend_views.xml`: formularul backend-ului Shopify (tab-uri Credentials, Price, Other Info, GraphQL, Objects — configurare credențiale, filtre, opțiuni de sincronizare, acțiuni de import/export, buton Test connection).
- `shopify_webhook_checker_views.xml`: wizard-ul de comparare a webhook-urilor înregistrate în Shopify cu cele așteptate din configurația backend-ului (Matched/Missing/Orphan).

**Acțiuni Automate / Acțiuni Server**

- `cron_shopify_refresh_tokens` (`data/cron.xml`): rulează la fiecare 23 de ore, reînnoiește token-urile OAuth pentru backend-urile Dev Dashboard Apps active (vizibilă doar în Settings → Technical → Scheduled Actions, nu în meniul Marketplace → Configuration → Crons).
- `job_function_sale_order_job_shopify_import` și `job_function_sale_order_shopify_job_from_webhook` (`data/job_function.xml`): joburi `queue_job` pentru importul comenzilor, pe canalele `shopify_inbound`/`shopify_outbound`, cu tipar de retry configurat.

**Mapare câmpuri produs**

Documentată integral în `readme/USAGE.md` (secțiunea „Product field mapping"), derivată din cod: `shopify_convert_result_to_values()`, `shopify_write()`, `product_set_input()`, `variant_bulk_input()`. „ambele" = câmpul circulă în ambele direcții, fiecare pe acțiunea ei (import, export, export preț).

| Câmp | Câmp Odoo | Câmp Shopify | Direcție |
|------|-----------|--------------|----------|
| Denumire produs | `name` | `title` | ambele |
| Referință internă (SKU) | `default_code` | `variants[].sku` (`inventoryItem.sku`) | ambele |
| Cod extern | `external_code` (legătură) | `variants[0].sku` | Shopify → Odoo |
| ID extern | `external_id` (legătură) | `id` (Product / ProductVariant) | ambele |
| Preț de vânzare | `list_price`, `odoo_price` (legătură) | `variants[].price` | ambele |
| Preț de catalog | `list_price`, când lista de prețuri a backend-ului dă discount | `compareAtPrice` | Odoo → Shopify |
| Cod de bare | `barcode` | `barcode` | ambele |
| Greutate | `weight` (kg) | `inventoryItem.measurement.weight` | ambele |
| Descriere vânzare | `description_sale` | `descriptionHtml` (`body_html`) | Odoo → Shopify |
| Categorie produs | `categ_id` | `productType` | ambele (import doar cu **Product Type as Category**) |
| Marcă | `get_brand_name()` (`deltatech_marketplace_brand`) | `vendor` | Odoo → Shopify |
| Categorii eCommerce | `public_categ_ids` | colecții (manuale și inteligente) | Shopify → Odoo |
| Atribute și valori | `attribute_line_ids` | `options[].name` / `options[].values`, `optionValues` | ambele (import doar cu **Options as Attributes**) |
| Imagine principală | `image_1920` | `images[0].src`, `files` | ambele |
| Imagini suplimentare | înregistrări `product.image` | `images[1..]` | Shopify → Odoo |
| Stoc | `odoo_stock`, `external_stock` (legătură) | `InventoryLevel.available`, per locație | ambele |
| Articol de inventar | `shopify_inventory_item_id` (legătură) | `inventoryItem.id` | Shopify → Odoo |
| Stare publicare | — (mereu activ la creare) | `status` | Odoo → Shopify |
| Cod vamal | `hs_code` | `harmonized_system_code` | Shopify → Odoo |
| Țară de origine | `country_of_origin` | `country_code_of_origin` | Shopify → Odoo |

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace pe care se construiește conectorul.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): importul, sincronizarea și corecția fiscală a comenzilor de vânzare, precum și registrul comun `marketplace.return.request` în care se importă retururile Shopify.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): fazele de vânzare (Sale Phases) pe care se mapează etichetele Shopify.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): integrarea metodelor de plată și crearea plăților.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): maparea curierilor și liniile de livrare.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): integrarea cu website-ul Odoo pentru fluxurile de e-commerce ale marketplace-ului.
- [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md): puntea care duce retururile importate din Shopify (`marketplace.return.request`) pe fluxul de depozit al `deltatech_rma` — conectorul importă doar registrul de retur, această punte îl leagă de picking-urile RMA.
