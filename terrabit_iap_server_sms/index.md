# IAP Server - Service SMS (localizat la `terrabit_iap_server_sms/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_sms`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_server_sms
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_sms`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Implementează pe serverul IAP Terrabit serviciul de SMS: instanțele client trimit mesajele către server, iar acesta le expediază printr-un furnizor de SMS și taxează creditele contului. Modulul nu are fișier `readme/DESCRIPTION.md`, deci descrierea provine din manifest și cod.

#### 2. Funcționalități Cheie

- Serviciu „SMS” (`sms`) cu credite partajate în portofelul bazei de date client.
- Furnizori acceptați: SMS 4Pay și SMS Wapi; pe serviciu se setează furnizorul, secretul și gateway-ul.
- Rută JSON-RPC `/api/sms/3/send` pentru trimitere în lot: câte un rezultat per destinatar, cu uuid-ul propriu și starea `success`, `insufficient_credit` sau `server_error`.
- Taxare: un SMS al unui cont legat costă „Wallet Rate” al serviciului (0,04 EUR), iar un cont pe sold propriu plătește 1 credit SMS. Rezervarea se confirmă după trimitere reușită și se anulează la eroare.
- Soldul disponibil (credite minus rezervările în așteptare) se verifică înainte de fiecare mesaj; un destinatar fără credit nu oprește lotul.
- Erorile de parametri (lipsă) sau de cont necunoscut se întorc ca erori JSON-RPC, pentru ca clientul SMS Odoo să le interpreteze corect.
- La legarea contului, creditele SMS cumpărate și nefolosite intră în portofel la 0,04 EUR bucata.

#### 3. Dependențe

- `iap`
- `terrabit_iap_server`

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): codul `sms`, câmpurile `sms_provider`, `sms_secret`, `sms_gateway` și metoda `send_sms`, care alege furnizorul.

**Vizualizări**

- Formularul serviciului IAP, extins cu câmpurile furnizorului SMS (`views/iap_server_service_views.xml`).

**Acțiuni Automate / Acțiuni Server**

- Fără cron sau acțiuni server; serviciul „SMS” și prețul din portofel (0,04 EUR, doar la instalare) vin din `iap_server_service_data.xml`.

#### 5. Conexiuni

- `terrabit_iap_server`: serverul IAP pe care rulează serviciul.
