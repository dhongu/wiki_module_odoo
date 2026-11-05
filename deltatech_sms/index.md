# SMS Custom Gateway (localizat la `deltatech_sms/index.md`)

- **Nume Tehnic:** `deltatech_sms`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sms
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sms`
- **Ultima Ingestie:** `2026-11-05`

#### 1. Sumar

Modulul trimite SMS-urile generate de Odoo prin propriul cont la un furnizor de SMS, în locul creditelor Odoo IAP. Sunt suportați doi furnizori: **4Pay** (sms.4pay.ro) și **Wapi** (smswapi.com). Astfel tot fluxul nativ de SMS din Odoo folosește contul comercial al clientului la un furnizor local.

#### 2. Funcționalități Cheie

- **Furnizorul înlocuiește IAP pentru SMS**: fiecare SMS pus în coadă de Odoo (din chatter, SMS marketing, șabloane SMS, acțiuni automate) este trimis pe rând prin furnizorul setat pe contul IAP de tip SMS; nu se consumă credite IAP.
- **4Pay**: mesajul se trimite printr-un HTTP GET către API-ul de clienți 4Pay, cu ID-ul serviciului și parola contului 4Pay.
- **Wapi**: mesajul se trimite printr-un HTTP POST către API-ul Wapi, prin unul dintre dispozitivele Android legate la contul Wapi (SIM 1).
- **Text fără diacritice**: accentele sunt eliminate înainte de trimitere (de ex. „ă" devine „a"), ca textul să se potrivească setului de caractere GSM.
- **Stare de trimitere**: un mesaj acceptat de furnizor trece în starea standard Odoo *Pending* și este șters din coadă ca orice SMS trimis; un mesaj respins trece în *Error*, cu motivul returnat de furnizor.
- **Configurare**: *Settings > Technical > IAP > IAP Accounts* (modul developer), contul serviciului **SMS** (se creează dacă lipsește), cu câmpurile **SMS Provider** (*SMS 4Pay* sau *SMS Wapi*), **SMS Secret** (parola 4Pay sau secretul API Wapi) și **SMS Gateway** (ID-ul serviciului servID la 4Pay sau ID-ul dispozitivului la Wapi).
- **Limitări**: adresele furnizorilor sunt fixe în cod, deci alte gateway-uri sau URL-uri personalizate nu se pot configura; rapoartele de livrare nu sunt primite de la furnizor, un SMS trimis rămâne *Pending* și nu ajunge niciodată *Delivered*; fluxurile Odoo IAP de înregistrare a contului SMS și de verificare a numelui expeditorului nu funcționează cât timp modulul e instalat.

#### 3. Dependențe

- `sms`

Dependență externă Python: `unidecode`.

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; câmpurile și metodele de mai jos au fost confirmate în `models/iap.py`, restul sunt păstrate din ingestia anterioară.

**Modele**

- `iap.account` (extins): câmpurile `sms_provider` (selecție `4pay` / `wapi`, implicit `4pay`), `sms_secret`, `sms_gateway` și metoda `send_sms`, cu `_send_sms_4pay` și `_send_sms_wapi`.
- `sms.sms` (extins): suprascrie `_send` pentru a trimite prin gateway-ul propriu și a actualiza stările.
- `SmsApi` (extinde `odoo.addons.sms.tools.sms_api.SmsApi`): redefinește `_contact_iap` pentru a apela contul IAP propriu în loc de serviciul IAP Odoo.

**Vizualizări**

- `iap_account_view_form` (`views/iap_views.xml`): extinde formularul contului IAP cu `sms_provider`, `sms_secret` și `sms_gateway`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. `data/neutralize.sql` este scriptul de neutralizare al bazei de date.

#### 5. Conexiuni

- Nicio conexiune suplimentară verificată în afara dependențelor declarate.
