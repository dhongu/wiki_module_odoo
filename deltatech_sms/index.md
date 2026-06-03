# Deltatech SMS (localizat la `deltatech_sms/index.md`)

- **Nume Tehnic:** `deltatech_sms`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sms`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sms`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul permite trimiterea de mesaje SMS din Odoo prin furnizori (gateway-uri) externi proprii, ca alternativă la serviciul IAP implicit oferit de Odoo. Practic, înlocuiește mecanismul standard de expediere a SMS-urilor cu apeluri directe către un endpoint configurabil, astfel încât întregul flux nativ de SMS din Odoo (notificări, marketing, confirmări) să folosească contul comercial al clientului la un provider local. Sunt suportați din cofigurare doi furnizori: SMS 4Pay și SMS Wapi.

#### 2. Funcționalități Cheie

- Trimitere SMS prin endpoint extern configurabil, fără a depinde de creditele IAP native Odoo.
- Suport pentru doi furnizori: SMS 4Pay și SMS Wapi (selectabili la nivelul contului IAP).
- Configurare directă în contul IAP de tip „sms" a parametrilor de acces: furnizor, secret (parolă/cheie) și gateway (servID / device).
- Integrare transparentă cu fluxul nativ `sms.sms`: toate SMS-urile trimise din Odoo sunt rutate automat către providerul configurat.
- Normalizarea conținutului mesajului prin eliminarea diacriticelor (unidecode) înainte de expediere.
- Gestionarea stărilor de livrare (succes / eroare server) și actualizarea corespunzătoare a înregistrărilor SMS.

#### 3. Dependențe

- `sms`

Dependență externă Python: `unidecode`.

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): adaugă câmpurile de configurare a furnizorului de SMS (`sms_provider`, `sms_secret`, `sms_gateway`) și metoda `send_sms`, cu implementări separate pentru 4Pay (`_send_sms_4pay`) și Wapi (`_send_sms_wapi`).
- `sms.sms` (extins): suprascrie metoda `_send` pentru a ruta expedierea prin gateway-ul custom și a actualiza stările de livrare.
- `SmsApi` (extinde `odoo.addons.sms.tools.sms_api.SmsApi`): redefinește `_contact_iap` pentru a apela contul IAP custom în locul serviciului IAP Odoo.

**Vizualizări**

- `iap_account_view_form`: extinde formularul contului IAP pentru a expune câmpurile `sms_provider`, `sms_secret` și `sms_gateway`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- [deltatech_delivery_send_sms](../deltatech_delivery_send_sms/index.md): trimite SMS la livrare, folosind infrastructura de SMS expusă de acest modul.
- `deltatech_sms_sale`: modul soră care extinde funcționalitatea SMS pe zona de vânzări.
