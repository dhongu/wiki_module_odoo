# Banca Transilvania iPay Payment Acquirer (localizat la `deltatech_payment_bt_ipay/index.md`)

- **Nume Tehnic:** `deltatech_payment_bt_ipay`
- **Versiune:** `19.0.0.0.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_bt_ipay`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_bt_ipay`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul conectează Odoo cu BT iPay (platforma de plăți online cu cardul a Băncii Transilvania), permițând încasarea securizată a plăților cu cardul atât pentru comenzile din magazinul online, cât și pentru facturile clienților. Este gândit pentru comercianții care vând online în România și doresc să centralizeze fluxul comandă-încasare în Odoo, oferind în același timp cumpărătorilor o experiență de plată locală, de încredere.

#### 2. Funcționalități Cheie

- Opțiunea „Plată cu cardul (BT iPay)" la finalizarea comenzii în eCommerce Odoo.
- Plata facturilor deschise direct din portalul de clienți Odoo.
- Urmărirea tentativelor de plată și a stării finale de autorizare pe comenzi/facturi.
- Reducerea reconcilierii manuale prin legarea automată a tranzacțiilor reușite de documentele corecte.
- Două moduri de operare configurabile pe furnizorul de plată BT iPay:
  - **1‑Phase (un pas)** — recomandat pentru servicii online: cardul este autorizat și suma este capturată imediat la finalizarea comenzii (bunuri digitale, abonamente, servicii cu livrare instantă).
  - **2‑Phase (doi pași)** — recomandat pentru produse fizice: cardul este autorizat la checkout, iar suma este capturată ulterior, după expediere sau confirmarea livrării, oferind echipei operaționale control asupra sumei efectiv capturate.
- Redirecționare către pagina de plată găzduită de BT iPay, atât din linkul de plată al portalului de clienți, cât și din checkout-ul eCommerce, cu revenire automată pe site după finalizarea/anularea plății.
- Datele cardului nu sunt stocate niciodată în Odoo — introducerea și securitatea lor sunt gestionate integral de BT iPay.

#### 3. Dependențe

- `payment`
- `website_sale`
- `phone_validation`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie au fost preluate din `readme/DESCRIPTION.md`. Pentru context tehnic suplimentar (util deoarece modulul e un integrator de plăți cu logică non-trivială), s-au reținut totuși componentele de bază identificate în cod:

**Modele**

- `payment.provider` (extins): adaugă codul de furnizor `bt_ipay`, câmpurile de credențiale (`bt_ipay_user`, `bt_ipay_pass`) și modul de operare (`bt_mode`: 1 Phase / 2 Phase), plus autentificarea Basic Auth și URL-urile API (producție/sandbox) către iPay.
- `payment.transaction` (extins): construiește payload-ul de înregistrare a tranzacției (`register.do` / `registerPreAuth.do` în funcție de modul 1‑Phase/2‑Phase), interoghează starea tranzacției (`getOrderStatusExtended.do`), tratează codurile de eroare/refuz specifice BT iPay (card blocat, fonduri insuficiente, 3DS2 etc.) și trimite cereri de capturare (`deposit.do`) și de anulare/reversare (`reverse.do`).
- `account.payment.method` (extins): înregistrează metoda de plată `bt_ipay` ca fiind de tip "multi", restricționată la conturi bancare.
- `sale.order` (extins): la capturarea manuală a plății (`payment_action_capture`), recalculează suma de capturat scăzând din totalul comenzii sumele deja facturate.

**Vizualizări**

- `acquirer_form_ipay`: extinde formularul standard al furnizorului de plată (`payment.payment_provider_form`) cu câmpurile specifice BT iPay (utilizator, parolă, mod 1/2 Phase).
- `bt_ipay_form`: șablonul QWeb al formularului de redirecționare către pagina de plată găzduită BT iPay (`orderId`, `amount`, `currency`, `returnUrl` etc.).

**Controller-e**

- `/payment/bt_ipay/payment` (POST): redirecționează clientul către URL-ul de plată (`formUrl`) primit de la BT iPay.
- `/payment/bt_ipay/return/<ref>/`: punctul de revenire după finalizarea/anularea plății pe pagina băncii; declanșează procesarea tranzacției (`_process`) și redirecționează către starea plății.

**Date**

- `payment_provider_data.xml`: creează înregistrarea `payment.provider` „BT iPay" (cod `bt_ipay`, sigla, mesaj pre-plată).
- `payment_method_data.xml`: creează metoda de plată `payment.method` „BT iPay".

#### 5. Conexiuni

- [deltatech_payment](../deltatech_payment/index.md): modulul de bază al suitei de plăți Terrabit; extinde generic `payment.transaction` (confirmare automată a comenzii la finalizarea plății) și `payment.provider`, mecanisme din care beneficiază și tranzacțiile procesate prin BT iPay.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): controlează la nivel de eCommerce ce furnizori de plată (inclusiv BT iPay) sunt afișați clientului în funcție de metoda de livrare aleasă sau de etichetele partenerului.
