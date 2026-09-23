# Extended Marketplace Connector (localizat la `deltatech_marketplace_extended/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_extended`
- **Versiune:** `19.0.0.0.19`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_extended`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_extended`
- **Ultima Ingestie:** `2026-09-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este conectorul specific care leagă platforma de e-commerce externă „Extended.ro" de Odoo, folosind cadrul generic de marketplace al suitei Terrabit. El adaugă providerul „Extended" la configurarea backend-ului și sincronizează automat, în ambele sensuri, datele comerciale: produse, furnizori, clienți, comenzi, curieri de livrare, metode de plată, categorii publice de site și etape de vânzare. Conectorul poate lucra fie pe API-ul vechi (V1), fie pe noul **Extended API V2**, ales per magazin: pe V2 comenzile pot fi preluate în câteva secunde prin webhook-uri semnate, în loc de importul programat, iar limitele de ritm ale platformei sunt respectate automat. Produsele și stocul rămân pe API-ul vechi în ambele cazuri, deoarece V2 nu oferă informațiile necesare pentru ele. La exportul de stoc, conectorul poate trimite un mesaj de termen de livrare calculat în Odoo și poate mapa mesajele proprii pe dicționarul de disponibilitate al platformei Extended, astfel încât textele afișate clienților în magazinul online să corespundă realității din stoc.

#### 2. Funcționalități Cheie

- Adaugă providerul „Extended" la configurarea backend-ului de marketplace, cu opțiuni proprii (data de start a importului, numărul de produse importate, codul de furnizor propriu, versiunea de API).
- **Extended API V2, la alegere per backend** (câmpul **Extended API Version**, implicit V1): cu o cheie V2 (`ev2_<selector>_<secret>`, generată în Extended Manager, *Integrations - Extended API V2*, introdusă separat de cheia legacy din *Client Secret / API key*), conectorul citește prin V2 comenzile și nomenclatoarele magazinului (stadii de comandă, metode de livrare și de plată, furnizori, categorii) și trimite prin V2 factura, AWB-ul și statusul comenzii. Cheia V2 are nevoie de permisiunile `orders:read`, `orders:update`, `shop:read`, `suppliers:read`, `categories:read` și, pentru webhook-uri, `webhooks:read`, `webhooks:create`, `webhooks:update`, `webhooks:delete`.
- **Produsele, exportul de stoc și dicționarul de mesaje de disponibilitate rămân pe API-ul vechi (V1)** chiar și cu V2 activ, pentru că V2 nu expune liniile de furnizor ale unui produs și nu are mesaj de stoc cu text liber; cheia V1 rămâne deci obligatorie pe orice backend, indiferent de versiunea aleasă.
- Comenzile citite prin V2 trec prin aceeași rutină de import ca cele din V1 (potrivire client, reduceri, linie de transport, plată identice); reducerea globală a comenzii, care pe V2 nu are linie proprie, este reconstituită din `totals.total` și redevine linia obișnuită de discount, iar **taxa de ramburs (cash-on-delivery) ajunge pe linia de transport**, la fel ca pe API-ul vechi.
- **Webhook-uri de comandă semnate (V2):** butonul **Register Webhooks** abonează `order.created` și `order.status_changed` în Extended și salvează secretul de semnare; fiecare notificare primită este verificată după semnătura `X-Extended-Signature` (HMAC-SHA256), iar importul comenzii este pus în coadă ca job, la câteva secunde după plasare — importul programat rămâne activ, ca plasă de siguranță. **Unregister Webhooks** anulează abonamentul. Extended livrează webhook-uri doar către o adresă publică și doar dacă modulul de webhook face parte din pachetul magazinului.
- Limitele de ritm ale cheii V2 (4 cereri/secundă, 80/minut, 3.600/oră, 60.000/zi) sunt aliniate automat de limitatorul de ritm al backend-ului la trecerea pe V2; erorile 429 și 5xx reprogramează job-ul în loc să-l oprească.
- Import de produse de pe platforma Extended, paginat și procesat asincron prin cozi de joburi.
- Import de furnizori (legacy `/?furnizori`, V2 `/suppliers`) în maparea `marketplace.supplier`, folosită pentru identificarea sursei de stoc la export.
- Import de clienți pe intervale de timp (segmente de 15 zile), pornind de la o dată configurabilă.
- Sincronizarea curierilor de livrare și a metodelor de plată între Extended și Odoo (cu mapare către produse de tip serviciu, respectiv către providerul de plată prin transfer bancar).
- **Import al categoriilor publice** din cardul dedicat al tab-ului Objects (arbore, legacy `/?categorii` / V2 `/categories`, cu păstrarea ierarhiei părinte-copil) și al etapelor/statusurilor de vânzare.
- Export de stoc (`update_stoc`) sub codul de furnizor configurat pe backend (**Extended Supplier Code**, implicit `1` = stocul propriu al magazinului); furnizorii externi (drop-ship, gestionați direct în Extended) nu sunt atinși de export.
- Mesaj de termen de livrare la export de stoc, opțional (**Send Delivery Term**), pentru produsele fără stoc disponibil: dată de reaprovizionare formatată pe jumătate de lună (dacă există o mișcare de intrare programată, plus o marjă configurabilă — **Delivery Term Margin**, implicit 14 zile) sau interval săptămânal derivat din timpul de livrare al produsului (*Customer Lead Time*), cu recurgere opțională (**Fall Back on Supplier Lead Time**) la timpul de livrare al furnizorului principal când produsul nu are unul propriu; punct de extensie (`_extended_availability_date`) pentru module de feed furnizor care vor să-și aducă propria sursă de dată.
- Dicționar de mesaje de disponibilitate Extended (`stoc_informativ_id`), învățat automat la importul de produse și editabil pe formularul backend-ului; fiecărei intrări i se poate atribui un rol (în stoc / fără stoc / interval de livrare / perioadă de livrare), folosit apoi la exportul de stoc pentru a trimite mesajul corect către Extended.
- **Reaprovizionare automată** (opțiune pe backend): produsele importate din Extended devin stocabile și primesc regulile de reaprovizionare Odoo, fără intervenție manuală per produs.
- Comunicare cu API-ul Extended pe bază de cheie API, cu documentație publicată (specificație Swagger pentru V1, specificație OpenAPI 3.1 pentru V2).

#### 3. Dependențe

- `sale`
- `purchase_stock`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este sintetizată din `readme/DESCRIPTION.md`, care documentează în detaliu comportamentul (nu lista de modele). Detaliile tehnice de configurare pas-cu-pas sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md); pe scurt, modulul este structurat în:

- Modele (`models`) — extind `marketplace.backend` cu providerul `extended` (câmpuri de configurare V1/V2, webhook, reaprovizionare automată) și extind modelele de produs, furnizor, client, comandă de vânzare, curier de livrare, provider de plată și categorie publică ale familiei de marketplace; adaugă modelul propriu `marketplace.extended.stock.info` pentru dicționarul de mesaje de disponibilitate.
- Vizualizări (`views`) — extind formularul backend-ului de marketplace cu câmpurile specifice Extended și butoanele de înregistrare/dezînregistrare a webhook-urilor.
- Securitate (`security`) — drepturi de acces pentru modelul propriu de dicționar de stoc informativ.
- Internaționalizare (`i18n`).

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază al familiei de marketplace; furnizează modelul `marketplace.backend` și mecanica generică de conectare extinsă aici pentru providerul „Extended".
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): furnizează modelul `marketplace.sale.order` extins aici pentru importul de comenzi (V1 și V2) și webhook-uri.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): furnizează modelul `marketplace.public.category` extins aici pentru importul categoriilor publice de site.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): furnizează modelul `marketplace.delivery.carrier` extins aici pentru maparea curierilor.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): furnizează modelul `marketplace.payment.provider` extins aici pentru maparea metodelor de plată.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): furnizează modelul `marketplace.sale.phase` extins aici pentru importul etapelor de vânzare.
