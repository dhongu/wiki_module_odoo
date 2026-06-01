# IAP Server - eCommerce Credits (localizat la `terrabit_iap_server_sale/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_sale`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/terrabit/tree/19.0/terrabit_iap_server_sale
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_sale`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modul care permite achiziția de credite IAP direct prin magazinul eCommerce (`website_sale`). Se instalează pe **serverul** IAP al Terrabit (nu la clienți) și transformă produsele obișnuite în pachete de credite ce pot fi cumpărate online: cumpărătorul alege un pachet de pe pagina de credite a serviciului, parcurge checkout-ul standard, iar la confirmarea comenzii contul IAP asociat este creditat automat cu numărul de credite achiziționate.

#### 2. Funcționalități Cheie

- Marchează produse drept „pachete de credite IAP" (`is_iap_credit`, `iap_credit_amount`, `iap_service_code`), legate de un serviciu de pe serverul IAP.
- Afișează dinamic pachetele disponibile pe pagina de credite a serviciului (`credit_page`), cu preț și buton de cumpărare.
- Adaugă pachetul în coș și conduce cumpărătorul la checkout-ul standard `website_sale`.
- Leagă comanda (`sale.order`) de contul IAP care a inițiat achiziția (token păstrat în sesiune).
- La confirmarea comenzii, creditează automat contul IAP cu numărul de credite cumpărate, o singură dată (idempotent prin `iap_credited`).

#### 3. Dependențe

- `terrabit_iap_server`
- `website_sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`, care nu solicită explicit analiza codului pentru Componente Cheie. Această secțiune este intenționat omisă.

#### 5. Conexiuni

- `terrabit_iap_server`: serverul IAP pe care rulează acest modul; furnizează serviciile IAP și conturile de credite creditate la confirmarea comenzii.
