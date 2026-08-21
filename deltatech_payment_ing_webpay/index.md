# ING WebPay Payment Acquirer (localizat la `deltatech_payment_ing_webpay/index.md`)

- **Nume Tehnic:** `deltatech_payment_ing_webpay`
- **Versiune:** `19.0.0.0.4`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_ing_webpay`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_ing_webpay`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul conectează Odoo cu ING WebPay (platforma de plăți online cu cardul a ING Bank România), permițând încasarea securizată a plăților cu cardul atât pentru comenzile din magazinul online, cât și pentru facturile clienților și, prin fluxul standard de plată online la POS, pentru vânzările din Point of Sale. Este gândit pentru comercianții care vând online în România și doresc să centralizeze fluxul comandă-încasare în Odoo, oferind în același timp cumpărătorilor o experiență de plată locală, de încredere, cu 3-D Secure 2 impus la fiecare tranzacție.

#### 2. Funcționalități Cheie

- Opțiunea „Plată cu cardul (ING WebPay)" la finalizarea comenzii în eCommerce Odoo.
- Buton de plată expresă **Google Pay** direct în coșul eCommerce (opțional, necesită parametrii Google Pay furnizați de ING): portofelul preia adresa de facturare/livrare, metodele de livrare și totalurile se recalculează live, iar plata se procesează direct prin endpointul Google Pay al ING.
- Plata facturilor deschise direct din portalul de clienți Odoo, prin linkurile standard de plată Odoo.
- Încasare cu cardul în **Point of Sale**: clientul scanează codul QR afișat de casier și plătește pe pagina ING de pe propriul telefon — nu necesită configurare suplimentară în acest modul, folosește fluxul standard `pos_online_payment`, care acceptă orice furnizor de plată publicat a cărui monedă corespunde punctului de vânzare.
- Urmărirea tentativelor de plată și a stării finale pe comenzi/facturi.
- Reducerea reconcilierii manuale prin legarea automată a tranzacțiilor reușite de documentele corecte.
- Verificare server-la-server a rezultatului plății (`getOrderStatusExtended.do`) — starea raportată de browser nu este niciodată de încredere.
- Sincronizare periodică (job programat) a tranzacțiilor nerezolvate, respectând regulile de interogare ale ING (prima verificare automată la 10 minute după înregistrare, maximum două tentative automate per comandă).
- Măsuri de siguranță: validarea URL-ului de checkout primit de la ING (host, `mdOrder`) înainte de redirecționare; reutilizarea unei comenzi ING deja înregistrate în loc de o nouă înregistrare (evită duplicate în back office-ul ING); verificarea sumei și monedei unei plăți reușite față de tranzacția Odoo; o plată confirmată nu este retrogradată automat de un status ulterior de reversal/refund — se loghează un avertisment pentru verificare manuală.
- Datele cardului nu sunt niciodată stocate în Odoo — introducerea și securitatea lor sunt gestionate integral de ING.
- Suportă doar contractul standard-sale (o singură fază, fără capturare manuală); rambursările se gestionează în back office-ul ING.
- Monede suportate: RON și EUR — se creează câte un furnizor de plată per monedă, fiecare cu propriile credențiale ING.

#### 3. Dependențe

- `payment`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie au fost preluate din `readme/DESCRIPTION.md`. Pentru context tehnic suplimentar (util deoarece modulul e un integrator de plăți cu logică non-trivială), s-au reținut totuși componentele de bază identificate în cod:

**Modele**

- `payment.provider` (extins): adaugă codul de furnizor `ing_webpay`, câmpurile de credențiale (`ing_webpay_username`, `ing_webpay_password`), opțiunea de trimitere a `orderNumber` propriu și parametrii de tokenizare Google Pay (`ing_webpay_google_pay_gateway`, `ing_webpay_google_pay_gateway_merchant_id`, `ing_webpay_google_pay_merchant_id`); activează expunerea butonului Google Pay doar când parametrii de tokenizare sunt configurați și declară contractul standard-sale (fără capturare manuală, fără rambursare, fără tokenizare a cardului); filtrează monedele suportate la RON/EUR și construiește URL-urile API de producție/test.
- `payment.transaction` (extins): construiește payload-ul de înregistrare a comenzii ING (`register.do`), reutilizează comanda deja înregistrată pentru a evita duplicatele, validează URL-ul de checkout returnat, procesează plata expresă Google Pay (`google/payment.do`), interoghează starea comenzii server-la-server (`getOrderStatusExtended.do`), caută tranzacția după `orderId`, extrage suma/moneda doar la status de succes și aplică actualizările de stare (confirmată, anulată, în așteptare, preautorizare în afara contractului, eroare); expune și un job programat de sincronizare a tranzacțiilor nerezolvate, cu limitare a numărului de tentative automate.
- `account.payment.method` (extins): înregistrează metoda de plată `ing_webpay` ca fiind de tip „multi", restricționată la conturi de tip bancă.

**Vizualizări**

- `payment_provider_form_ing_webpay`: extinde formularul standard al furnizorului de plată (`payment.payment_provider_form`) cu câmpurile specifice ING WebPay (utilizator, parolă, opțiunea `orderNumber`, parametrii Google Pay).
- `payment_transaction_form_ing_webpay`: extinde formularul tranzacției de plată cu butonul manual „Refresh ING Status" și câmpurile de diagnostic (`ing_webpay_last_status_check`, `ing_webpay_status_attempts`), vizibile doar administratorilor de sistem.
- `redirect_form` (`payment_templates.xml`): șablonul QWeb de redirecționare către pagina de plată găzduită ING WebPay.
- `express_checkout_form` (`payment_templates.xml`): șablonul QWeb pentru butonul de plată expresă Google Pay din eCommerce.

**Controller-e**

- `/payment/ing_webpay/return` (GET/POST): punctul de revenire după finalizarea/anularea plății pe pagina ING; declanșează verificarea server-la-server a stării și redirecționează clientul către pagina de status a plății.
- `/payment/ing_webpay/express_pay` (JSON-RPC): procesează plata expresă Google Pay pentru tranzacția deja creată, folosind tokenul primit de la portofel.

**Acțiuni Automate / Acțiuni Server**

- `cron_ing_webpay_sync_status`: rulează la fiecare 5 minute, sincronizând tranzacțiile ING WebPay nerezolvate (`draft`/`pending`) cu regulile de interogare ale ING (întârziere minimă după înregistrare, răcire între verificări, număr maxim de tentative automate, fereastră de timp limitată).

#### 5. Conexiuni

- [deltatech_pos_online_payment](../deltatech_pos_online_payment/index.md): recomandat pentru plățile la Point of Sale prin ING WebPay — previne marcarea de către casier a unei plăți ca finalizată înainte ca ING să o confirme.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): controlează la nivel de eCommerce ce furnizori de plată (inclusiv ING WebPay) sunt afișați clientului în funcție de metoda de livrare aleasă sau de etichetele partenerului.
- `payment` (nucleul de plăți Odoo, fără pagină wiki proprie): furnizează modelele `payment.provider` și `payment.transaction` extinse de acest modul.
- `pos_online_payment` (Community, fără pagină wiki proprie): oferă fluxul standard de plată online la POS folosit de ING WebPay, fără configurare suplimentară în acest modul.
