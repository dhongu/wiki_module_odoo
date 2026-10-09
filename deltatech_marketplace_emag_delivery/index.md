# EMAG Marketplace Delivery (localizat la `deltatech_marketplace_emag_delivery/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_emag_delivery`
- **Versiune:** `19.0.1.4.1`
- **Cale:** [https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_emag_delivery](https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_emag_delivery)
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_emag_delivery`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul emite AWB-uri (etichete de livrare) prin **eMAG Courier**, serviciul de curierat pe care eMAG îl pune la dispoziția vânzătorilor din marketplace, direct din livrarea Odoo. eMAG nu transportă efectiv coletele: le rezervă la un curier partener (Sameday, FAN Courier și alții) în numele vânzătorului. Modulul înregistrează `eMAG` ca metodă de livrare, astfel încât o livrare poate cere un AWB, poate descărca eticheta în A4/A5/A6 sau ZPL și poate urmări coletul prin fluxul de stări al eMAG — în timp ce numărul de AWB lizibil și curierul care transportă efectiv coletul rămân vizibile pe livrare.

#### 2. Funcționalități Cheie

- Emiterea AWB-ului prin eMAG Courier direct din livrarea Odoo (**Send to Shipper**, în română *Trimite la curier*; butonul apare după ce operatorul confirmă **Detalii transportator**). Suma de încasat ramburs se recalculează live în acel moment și urmează modul de plată eMAG păstrat pe comandă (`external_payment_code`: 1 ramburs, 2 transfer bancar, 3 card online), nu furnizorul Odoo asociat: doar rambursul se încasează, cardul și transferul rămân la 0. Pentru ramburs, suma este ce rămâne de plată pe factura emisă (postată); înainte de factură, totalul comenzii minus voucherul suportat de eMAG (**Voucher Paid on the Invoice**), care nu mai este linie a comenzii.
- **Verificarea voucherului înainte de AWB:** dacă lipsește de pe comandă partea de voucher acordată de vânzător (backend fără produs de discount), AWB-ul este refuzat în Odoo cu motivul exact, nu cu mesajul eMAG „cash on delivery value cannot be greater...". Se setează produsul pe backend și se reimportă comanda.
- **Protecție la comenzi cu anulare cerută:** înainte de AWB comanda este citită din nou de la eMAG; dacă clientul a cerut anularea, AWB-ul este refuzat până se rezolvă cererea pe eMAG (se poate ocoli cu cheia de context `emag_awb_despite_cancellation`).
- **Fără AWB dublu:** apelul de salvare AWB nu se mai reîncearcă după timeout sau eroare 5xx (nu e idempotent); eroarea cere verificarea în eMAG înainte de o nouă emitere.
- Comenzile cu ridicare din locker se trimit cu locker-ul returnat de eMAG pe comandă (`locker_id` transmis separat față de adresa destinatarului).
- **Print label** descarcă eticheta și o atașează pe livrare, denumită după numărul de AWB, astfel încât fluxul de printare ZPL o poate prelua.
- Livrarea afișează, pe tabul *Istoric*, **eMAG AWB Number** / *Număr AWB eMAG* (numărul de AWB lizibil pentru client) și **eMAG Courier** / *Curier eMAG* (curierul partener care transportă efectiv coletul) — referința de urmărire internă rămâne id-ul eMAG.
- Starea coletului este interogată periodic la eMAG (sau pe loc, cu *Reîmprospătează*) și scrisă în istoricul de livrare, un rând pe status, cu curierul ca locație. Eticheta vine automat la trimitere și se vede în previzualizarea din dreapta livrării; *Tipărire AWB* o cere din nou.
- Eticheta ZPL a unui AWB cu mai multe colete conține acum toate coletele (fiecare etichetă este decodată, ZPL-ul concatenat și recodat), nu doar primul.
- Eticheta poate fi re-descărcată de la API doar pe baza AWB-ului (`label_refetch`), deci o etichetă ștearsă local este recuperabilă.
- Statusul AWB `CAN` (anulat, adesea reemis) nu mai duce livrarea în starea **Refuzat**: starea rămâne neschimbată (se loghează), deoarece `deltatech_delivery_status` nu are stare de livrare anulată; `RTS` și `REF` rămân Refuzat. Un cod de status necunoscut păstrează starea și scrie un avertisment în log. Ultimul cod primit de la eMAG se păstrează pe AWB (**eMAG AWB Status Code** pe `delivery.awb`, coloană ascunsă în listă).
- Modulul are acum traducere în română (`i18n/ro.po` și `.pot`): termenii din configurare, formatul etichetei și mesajele de eroare AWB/localitate apar în română.
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

- `delivery.carrier` (extins): adaugă tipul de livrare `emag`, câmpurile `backend_id` (backend-ul eMAG folosit) și `emag_label_format` (A4/A5/A6/ZPL); implementează emiterea AWB-ului (`emag_send_shipping`, cu verificarea voucherului `_emag_check_voucher_on_order`, a cererii de anulare și alegerea contului de curier `_emag_courier_account_id`), preluarea etichetei, importul localităților și pollul de stare. Declară explicit capabilitățile `cities`, `ship`, `tracking`, `label_refetch`.
- `stock.picking` (extins): adaugă `emag_awb_number` (numărul de AWB lizibil) și `emag_courier_name` (curierul partener real); suprascrie `carrier_generate_label` pentru a genera automat AWB-ul dacă lipsește și a redenumi atașamentul etichetei după AWB.
- `marketplace.delivery.carrier` (extins): `emag_import` aduce conturile de curier din `/courier_accounts` și le leagă de un produs de tip serviciu.
- `delivery.awb` (extins): adaugă `emag_status_code`, ultimul cod de status eMAG, exact cum a fost trimis.
- `marketplace.backend` (extins): adaugă `delivery_carrier` la lista de tipuri de obiecte importabile atunci când provider-ul este `emag`.

**Vizualizări**

- Listă `delivery.awb` extinsă cu coloana ascunsă `emag_status_code`.
- `view_delivery_carrier_form_with_provider_emag`: adaugă tab-ul „EMag Configuration” pe formularul metodei de livrare (`delivery.carrier`), vizibil doar când `delivery_type = emag`.
- `view_picking_form_emag`: adaugă pe formularul livrării (`stock.picking`) câmpurile `emag_awb_number` și `emag_courier_name`, afișate doar când sunt completate.

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron`, `base.automation` sau `ir.actions.server` proprii — polling-ul de stare rulează prin infrastructura de livrare a `deltatech_marketplace_delivery`.

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conectorul eMAG de bază; păstrează `res.city.emag_id` și importul de localități, necesare acestui modul pentru validarea adreselor la emiterea AWB-ului.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): oferă infrastructura generică de curierat pentru marketplace (istoricul livrării, importul de curieri) pe care acest modul o specializează pentru eMAG.
- [deltatech_delivery](../deltatech_delivery/index.md): oferă contractul de capabilități de livrare (`_delivery_api_capabilities`) și fluxul de generare/printare a etichetelor pe care acest modul îl implementează pentru eMAG.
- Modul separat, extras din `deltatech_marketplace_emag` (începând cu 19.0.2.5.0), pentru ca vânzătorii care livrează cu propriul curier să nu primească ecranele de configurare eMAG; se auto-instalează când `deltatech_marketplace_emag` și `deltatech_delivery` sunt ambele prezente.
- Pe Odoo Apps (preț 200 EUR, licență OPL-1) achiziția acoperă întreaga stivă: acest modul, conectorul `deltatech_marketplace_emag`, baza de livrare `deltatech_delivery` și framework-ul marketplace; conectorii pentru curieri specifici (FAN Courier, Sameday etc.) sunt module separate, construite pe aceeași bază de livrare. Cu fiecare AWB, Odoo trimite la eMAG datele expeditorului și destinatarului, numărul de colete, greutatea, valoarea declarată, rambursul și, la ridicare, locker-ul. Tarifele de transport nu sunt suportate (costul vine cu comanda eMAG).
