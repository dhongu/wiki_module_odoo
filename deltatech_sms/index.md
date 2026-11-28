# SMS Custom Gateway (localizat la `deltatech_sms/index.md`)

- **Nume Tehnic:** `deltatech_sms`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sms
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sms`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul trimite SMS-urile generate de Odoo prin contul propriu la un furnizor de SMS (4Pay sau Wapi), în loc de creditele IAP Odoo. Toate mesajele puse în coadă de Odoo (din chatter, marketing SMS, șabloane, acțiuni automate) sunt expediate pe rând prin furnizorul configurat, astfel că firma folosește contractul propriu la un provider local.

#### 2. Funcționalități Cheie

- Furnizorul înlocuiește IAP pentru SMS: nu se consumă credite IAP, iar furnizorul Twilio din Odoo 20, dacă este configurat, este ocolit.
- Doi furnizori: **4Pay** (cerere HTTP GET către API-ul de client, cu ID-ul serviciului și parola) și **Wapi** (cerere HTTP POST, printr-unul dintre dispozitivele Android legate de cont, SIM 1).
- Configurare în *Setări > Tehnic > IAP > Conturi In-App Purchase* (mod dezvoltator), pe contul serviciului **SMS**: **SMS Provider**, **SMS Secret** (parola 4Pay sau secretul API Wapi) și **SMS Gateway** (servID 4Pay sau ID-ul dispozitivului Wapi).
- Textul se trimite fără diacritice (ex. „ă” devine „a”), pentru a se încadra în setul de caractere GSM.
- Stare de expediere: mesajul acceptat de furnizor trece în starea standard *Pending* și este scos din coadă; mesajul respins trece în *Error* (eroare de server), cu motivul returnat de furnizor afișat în notificarea de eșec, și rămâne în coadă pentru retrimitere.
- Limitări: adresele furnizorilor sunt fixe în cod; nu se primesc rapoarte de livrare (SMS-ul rămâne *Pending*); fluxurile Odoo IAP de înregistrare a contului și de verificare a numelui expeditorului nu funcționează cât timp modulul este instalat.

#### 3. Dependențe

- `sms`

Dependență externă Python: `unidecode`.

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): câmpurile de configurare a furnizorului (`sms_provider`, `sms_secret`, `sms_gateway`) și metodele de trimitere pentru 4Pay și Wapi.
- `sms.sms` (extins): suprascrie expedierea pentru a o ruta prin furnizorul configurat și a actualiza stările.
- `SmsApi` (extinde `odoo.addons.sms.tools.sms_api.SmsApi`): apelul către IAP este înlocuit cu apelul către contul IAP configurat.

**Vizualizări**

- `views/iap_views.xml`: extinde formularul contului IAP cu câmpurile furnizorului de SMS.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_delivery_send_sms](../deltatech_delivery_send_sms/index.md): trimite SMS la livrare, folosind infrastructura de SMS expusă de acest modul.
- [deltatech_sms_sale](../deltatech_sms_sale/index.md): modul soră care extinde funcționalitatea SMS pe zona de vânzări.
