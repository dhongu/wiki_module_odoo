# Conector Shopify Marketplace (localizat la `deltatech_marketplace_shopify/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_shopify`
- **Versiune:** `19.0.0.12.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_shopify
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_shopify`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Conectorul Shopify Marketplace dezvoltat de Terrabit creează o integrare directă și fluidă între sistemul ERP Odoo și platforma de magazine online Shopify. Modulul permite companiilor să sincronizeze și să gestioneze magazinele lor Shopify direct din Odoo, oferind o soluție unificată pentru administrarea produselor, clienților și comenzilor. Astfel, echipele pot opera magazinul online fără a comuta între platforme, păstrând o singură sursă de adevăr pentru informațiile despre produse și clienți, reducând introducerea manuală a datelor și eliminând discrepanțele.

#### 2. Funcționalități Cheie

- **Sincronizare produse**:
  - Export de șabloane și variante de produs din Odoo către Shopify (creare și actualizare).
  - Import de șabloane de produs, variante și imagini din Shopify.
  - Sincronizarea bidirecțională a prețurilor și a informațiilor de bază (cod de bare, greutate, SKU), pe fiecare variantă.
  - Suport pentru imagini multiple per șablon de produs și asocierea imaginilor cu variante specifice.
  - Actualizări în timp real ale produselor prin webhook (`products/update`).

- **Atribute de produs**:
  - Import al atributelor de produs (opțiuni Shopify) și al valorilor lor.
  - Maparea opțiunilor/variantelor Shopify la atributele de produs din Odoo, cu control asupra modului de creare a variantelor (dinamic sau instant).

- **Integrare clienți**:
  - Import al clienților Shopify în baza de contacte Odoo, cu actualizări în timp real prin webhook.
  - Menținerea unor înregistrări de client consistente între platforme.
  - Detectarea automată a companiilor pe baza atributelor din nota Shopify sau a câmpului de companie.

- **Gestionarea comenzilor**:
  - Import al comenzilor de vânzare din Shopify în Odoo (creare automată a comenzilor Odoo).
  - Aplicarea automată a fazelor de vânzare (Sale Phases) din etichetele (tags) comenzii Shopify, la fiecare import/reîmprospătare — fără pas manual de import separat.
  - Sincronizarea anulării comenzilor între Odoo și Shopify.
  - Suport pentru webhook-uri Shopify (`orders/create`, `orders/updated`, `orders/paid`, `orders/cancelled`) pentru actualizarea automată a comenzilor în Odoo.
  - Rutarea depozitului comenzii pe baza locației Shopify (`location_id` / locația de onorare), prin binding-ul `marketplace.warehouse`.
  - Verificarea totalului comenzii importate față de totalul Shopify, cu raportare a diferențelor în chatter.
  - Reguli de protecție la re-import: pe o comandă ale cărei valori sunt marcate ca „discarded" (backend `only_missing` sau „No Refresh" pe comandă), doar locker-ul, curierul și liniile de livrare deschise mai sunt actualizate — restul (linii, sume, fază, adrese) rămân neatinse.

- **Plăți și livrare**:
  - Import și mapare a metodelor de plată (payment acquirers) din Shopify.
  - Sincronizarea stării financiare a comenzii (`financial_status`) cu tranzacția de plată din Odoo.
  - Maparea automată a curierilor și crearea/actualizarea liniilor de livrare pe comenzi.
  - Suport pentru puncte de ridicare (lockere) preluate din notele Shopify.
  - Trimiterea numerelor de tracking (AWB) către Shopify prin API-ul `FulfillmentV2`, cu declanșator configurabil (la crearea AWB sau la validarea transferului) și suport pentru onorări parțiale.

- **Stoc și prețuri**:
  - Export al cantităților de stoc din Odoo către Shopify prin API-ul `InventoryLevel`, cu suport multi-locație (o locație Shopify = un depozit Odoo).
  - Export al prețurilor per variantă din lista de prețuri Odoo, cu setare automată a `compare_at_price` la discount.
  - Suport pentru comenzi în monedă diferită de moneda magazinului (multi-valută), prin binding-uri `marketplace.product.pricelist` pe cod ISO de monedă.

- **Autentificare și operații automate**:
  - Suport pentru două moduri de autentificare: Legacy Private Apps (token permanent) și Dev Dashboard Apps (OAuth `client_credentials`, token cu expirare la 24h, cu reîmprospătare automată).
  - Job programat („Shopify: Refresh Access Tokens") care reînnoiește proactiv token-urile OAuth la fiecare 23 de ore.
  - Sincronizare programată și asincronă prin `queue_job`, cu retry automat la limitări de rată (HTTP 429) și erori de server.
  - Autentificarea webhook-urilor primite prin semnătura `X-Shopify-Hmac-Sha256`.
  - Import de colecții Shopify (custom și smart) ca și categorii publice de produs.
  - Wizard de verificare a webhook-urilor înregistrate în Shopify față de cele așteptate, cu remediere directă (înregistrare/ștergere).

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

- `marketplace.backend` (extins, `backend.py`): configurarea specifică Shopify a backend-ului marketplace — credențiale (token permanent sau OAuth), opțiuni de import/export (atribute din opțiuni, creare variante, categorie publică, tip produs ca și categorie internă), declanșator de onorare, reîmprospătare token.
- `backend_adapter.py`: adaptorul de comunicare cu API-ul REST Shopify (autentificare, apeluri cu retry la rate-limit/erori de server).
- `binding_product_template.py` / `binding_product.py`: binding-uri de șablon și variantă de produs, inclusiv import/export atribute, opțiuni, imagini, stoc (`shopify_import_stock`, `shopify_stock_export`) și preț.
- `binding_product_image.py`: binding pentru imaginile de produs, cu asociere pe variante.
- `binding_attribute.py`: binding pentru atributele de produs (opțiunile Shopify).
- `binding_customers.py`: binding pentru clienți și adresele lor.
- `binding_sale_order.py`: binding pentru comenzi de vânzare — import, rutare depozit, verificare total, protecție la re-import pe comenzi „discarded".
- `binding_sale_stage.py`: binding pentru fazele de vânzare (etichete/tags Shopify → `marketplace.sale.phase`).
- `binding_payment_acquirer.py`: binding pentru metodele de plată.
- `binding_public_category.py`: binding pentru colecțiile Shopify importate ca și categorii publice.
- `binding_warehouse.py`: binding pentru locațiile Shopify mapate la depozitele Odoo (`marketplace.warehouse`).
- `stock_picking.py`: extensie pentru trimiterea AWB-urilor și a onorărilor (fulfillment) către Shopify la validarea transferului.

**Vizualizări**

- `backend_views.xml`: formularul backend-ului Shopify (configurare credențiale, opțiuni de sincronizare, acțiuni de import/export).
- `shopify_webhook_checker_views.xml`: wizard-ul de comparare a webhook-urilor înregistrate în Shopify cu cele așteptate din configurația backend-ului.

**Acțiuni Automate / Acțiuni Server**

- `cron_shopify_refresh_tokens` (`data/cron.xml`): rulează la fiecare 23 de ore, reînnoiește token-urile OAuth pentru backend-urile Dev Dashboard Apps active.
- `job_function_sale_order_job_shopify_import` și `job_function_sale_order_shopify_job_from_webhook` (`data/job_function.xml`): joburi `queue_job` pentru importul comenzilor, pe canalele `shopify_inbound`/`shopify_outbound`, cu tipar de retry configurat.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace pe care se construiește conectorul.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): importul, sincronizarea și corecția fiscală a comenzilor de vânzare.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): fazele de vânzare (Sale Phases) pe care se mapează etichetele Shopify.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): integrarea metodelor de plată și crearea plăților.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): maparea curierilor și liniile de livrare.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): integrarea cu website-ul Odoo pentru fluxurile de e-commerce ale marketplace-ului.
