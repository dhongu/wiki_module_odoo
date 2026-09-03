# EMAG Marketplace Delivery (localizat la `deltatech_marketplace_emag_delivery/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_emag_delivery`
- **Versiune:** `19.0.1.0.1`
- **Cale:** [https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_emag_delivery](https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_emag_delivery)
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_emag_delivery`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Modulul emite AWB-uri (etichete de livrare) prin **eMAG Courier**, serviciul de curierat pe care eMAG îl pune la dispoziția vânzătorilor din marketplace, direct din livrarea Odoo. eMAG nu transportă efectiv coletele: le rezervă la un curier partener (Sameday, FAN Courier și alții) în numele vânzătorului. Modulul înregistrează `eMAG` ca metodă de livrare, astfel încât o livrare poate cere un AWB, poate descărca eticheta în A4/A5/A6 sau ZPL și poate urmări coletul prin fluxul de stări al eMAG — în timp ce numărul de AWB lizibil și curierul care transportă efectiv coletul rămân vizibile pe livrare.

#### 2. Funcționalități Cheie

- Emiterea AWB-ului prin eMAG Courier direct din livrarea Odoo (**Send to shipper**); suma de încasat ramburs se recalculează live din comandă în acel moment, astfel încât o plată deja capturată online nu mai apare de încasat.
- Comenzile cu ridicare din locker se trimit cu locker-ul returnat de eMAG pe comandă (`locker_id` transmis separat față de adresa destinatarului).
- **Print label** descarcă eticheta și o atașează pe livrare, denumită după numărul de AWB, astfel încât fluxul de printare ZPL o poate prelua.
- Livrarea afișează **eMAG AWB Number** (numărul de AWB lizibil pentru client) și **eMAG Courier** (curierul partener care transportă efectiv coletul) — referința de urmărire internă rămâne id-ul eMAG.
- Starea coletului este interogată periodic la eMAG și scrisă în istoricul de livrare al comenzii.
- Eticheta poate fi re-descărcată de la API doar pe baza AWB-ului (`label_refetch`), deci o etichetă ștearsă local este recuperabilă.
- Anularea unui AWB nu e posibilă din Odoo — se face din interfața de vânzător eMAG, care nu oferă API pentru asta.
- Configurare metodă de livrare: în *Inventar > Configurare > Metode de Livrare*, se creează o metodă cu **Provider** `EMAG`; pe tab-ul **EMag Configuration** se aleg Backend-ul (contul eMAG pe care se rezervă AWB-ul), formatul etichetei (A4/A5/A6 sau ZPL pentru imprimante Zebra), adresa companiei folosită ca expeditor și metodele de plată considerate ramburs.
- Localitățile eMAG se importă din formularul backend-ului (*Import Localities*) — atât expeditorul, cât și destinatarul trebuie să corespundă unui oraș cunoscut de eMAG, altfel AWB-ul este refuzat.
- Conturile de curier eMAG (care decid care curier partener rezervă efectiv coletul) se aduc prin *Import* pe backend.

#### 3. Dependențe

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins): adaugă tipul de livrare `emag`, câmpurile `backend_id` (backend-ul eMAG folosit) și `emag_label_format` (A4/A5/A6/ZPL); implementează emiterea AWB-ului (`emag_send_shipping`), preluarea etichetei, importul localităților și pollul de stare. Declară explicit capabilitățile `cities`, `ship`, `tracking`, `label_refetch`.
- `stock.picking` (extins): adaugă `emag_awb_number` (numărul de AWB lizibil) și `emag_courier_name` (curierul partener real); suprascrie `carrier_generate_label` pentru a genera automat AWB-ul dacă lipsește și a redenumi atașamentul etichetei după AWB.
- `marketplace.delivery.carrier` (extins): `emag_import` aduce conturile de curier din `/courier_accounts` și le leagă de un produs de tip serviciu.
- `marketplace.backend` (extins): adaugă `delivery_carrier` la lista de tipuri de obiecte importabile atunci când provider-ul este `emag`.

**Vizualizări**

- `view_delivery_carrier_form_with_provider_emag`: adaugă tab-ul „EMag Configuration” pe formularul metodei de livrare (`delivery.carrier`), vizibil doar când `delivery_type = emag`.
- `view_picking_form_emag`: adaugă pe formularul livrării (`stock.picking`) câmpurile `emag_awb_number` și `emag_courier_name`, afișate doar când sunt completate.

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron`, `base.automation` sau `ir.actions.server` proprii — polling-ul de stare rulează prin infrastructura de livrare a `deltatech_marketplace_delivery`.

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conectorul eMAG de bază; păstrează `res.city.emag_id` și importul de localități, necesare acestui modul pentru validarea adreselor la emiterea AWB-ului.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): oferă infrastructura generică de curierat pentru marketplace (istoricul livrării, importul de curieri) pe care acest modul o specializează pentru eMAG.
- [deltatech_delivery](../deltatech_delivery/index.md): oferă contractul de capabilități de livrare (`_delivery_api_capabilities`) și fluxul de generare/printare a etichetelor pe care acest modul îl implementează pentru eMAG.
- Modul separat, extras din `deltatech_marketplace_emag` (versiunea 19.0.2.4.4), pentru ca vânzătorii care livrează cu propriul curier să nu primească ecranele de configurare eMAG; se auto-instalează când `deltatech_marketplace_emag` și `deltatech_delivery` sunt ambele prezente.
