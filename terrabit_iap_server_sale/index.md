# IAP Server - eCommerce Credits (localizat la `terrabit_iap_server_sale/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_sale`
- **Versiune:** `19.0.1.7.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_sale
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_sale`
- **Ultima Ingestie:** 2026-11-20

#### 1. Sumar

Modul care permite achiziția de credite IAP direct prin magazinul eCommerce (`website_sale`). Se instalează pe **serverul** IAP al Terrabit (nu la clienți) și transformă produsele obișnuite în pachete de credite ce pot fi cumpărate online: cumpărătorul alege un pachet de pe pagina de credite a serviciului, parcurge checkout-ul standard, iar la confirmarea comenzii contul IAP asociat este creditat automat cu numărul de credite achiziționate.

#### 2. Funcționalități Cheie

- Marchează produse drept „pachete de credite IAP" (`is_iap_credit`, `iap_credit_amount`, `iap_service_code`), legate de un serviciu de pe serverul IAP.
- Afișează dinamic pachetele disponibile pe pagina de credite a serviciului (`credit_page`), cu preț și buton de cumpărare.
- Adaugă pachetul în coș și conduce cumpărătorul la checkout-ul standard `website_sale`.
- Leagă comanda (`sale.order`) de contul IAP care a inițiat achiziția (token păstrat în sesiune).
- Lista de prețuri a pachetelor se alege pe serviciu (**Credit Pricelist**, de exemplu în EUR): pagina de credite îi arată prețurile, iar coșul cumpărătorului venit de acolo o folosește, oricare ar fi lista implicită a site-ului.
- Pagina de credite arată soldul cu zecimale și, la serviciile online, câte operații înseamnă creditele (de exemplu „≈ 1.000 AWB"), plus prețul pe operație (sau pe credit) al fiecărui pachet; insigna merge la cel mai ieftin pachet pe credit.
- Catalog public al serviciilor (`/iap/all-in-app-services`) și o pagină pe serviciu (`/iap/in-app-services/<cod>`), pentru serviciile bifate **Published in Catalog**: preț pe operație, credite gratuite, pachete cu „cel mai bun preț" și întrebări frecvente. Paginile nu vând: cumpărarea pornește din baza clientului.
- Cumpărătorii din UE din afara țării companiei plătesc doar ca firmă cu cod TVA (taxare inversă); fără cod TVA, plata e refuzată cu un mesaj clar.
- La confirmarea comenzii, creditează automat contul IAP cu numărul de credite cumpărate, o singură dată (idempotent prin `iap_credited`).
- Creditele acordate apar ca linie **Purchase** în istoricul contului IAP, cu comanda asociată (**Sale Order**); istoricul din portal trimite la comandă, iar pagina de credite are link către istoricul contului.
- Conturile legate de un portofel comun de credite primesc pachetele tuturor serviciilor cu credite partajate; coșul acceptă astfel pachete de la mai multe servicii cu credite partajate în aceeași comandă.

#### 3. Dependențe

- [terrabit_iap_server](../terrabit_iap_server/index.md)
- `website_sale`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`, care nu solicită analiza codului pentru Componente Cheie; secțiunea de mai jos listează doar extensiile evidente din structura modulului.

**Modele**

- `product.template` (extins): câmpurile pachetului de credite (`is_iap_credit`, `iap_credit_amount`, `iap_service_code`).
- `sale.order` (extins): contul IAP al comenzii și creditarea la confirmare (`iap_credited`).
- `iap.server.service` (extins): lista de prețuri pentru credite (**Credit Pricelist**) și publicarea în catalog.
- `iap.server.transaction` (extins): legătura liniei **Purchase** cu comanda de vânzare.

**Vizualizări**

- `product_template_form_view_iap_credit`: câmpurile de credit pe formularul produsului.
- `view_iap_server_service_form_credit_pricelist`: lista de prețuri pe formularul serviciului.
- `view_iap_server_transaction_form_sale`: comanda pe formularul tranzacției.
- `catalog_page`, `catalog_service_page`, `catalog_unit`: catalogul public al serviciilor (șabloane QWeb).

**Rute**

- `/iap/buy_credits`: adaugă pachetul în coș și duce la checkout.
- `/iap/all-in-app-services` și `/iap/in-app-services/<cod>`: catalogul public.

**Acțiuni Automate / Acțiuni Server**

- Niciuna definită în modul.

#### 5. Conexiuni

- [terrabit_iap_server](../terrabit_iap_server/index.md): serverul IAP pe care rulează acest modul; furnizează serviciile IAP și conturile de credite creditate la confirmarea comenzii.
