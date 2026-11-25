# IAP Server - eCommerce Credits (localizat la `terrabit_iap_server_sale/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_sale`
- **Versiune:** `19.0.1.8.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_sale
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_sale`
- **Ultima Ingestie:** `2026-11-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul care permite achiziția de credite IAP direct prin magazinul eCommerce (`website_sale`). Se instalează pe **serverul** IAP al Terrabit (nu la clienți) și transformă produsele obișnuite în pachete de credite ce pot fi cumpărate online: cumpărătorul alege un pachet, parcurge checkout-ul standard, iar la confirmarea comenzii contul IAP asociat (sau portofelul bazei Odoo indicate) este creditat automat cu numărul de credite achiziționate. Creditele se vând doar firmelor cu cod fiscal.

#### 2. Funcționalități Cheie

- Serviciul **Credite Terrabit** (cod `terrabit_credits`, credite comune) este creat la instalare: pachetele lui încarcă portofelul bazei, pentru toate serviciile cu credite comune (1 credit = 1 EUR).
- Marchează produse drept „pachete de credite IAP" (`is_iap_credit`, `iap_service_code`, `iap_credit_amount`, `iap_credit_bonus`), cu câmpurile sub prețul de vânzare; bonusul apare pe pagini ca „Bonus: +5 credite", la fel ca pe pagina produsului.
- Pagina de credite a contului (deschisă cu **Cumpără credite** din baza clientului) arată soldul cu zecimale, pachetele cu preț fără TVA, prețul pe operație și butonul de cumpărare.
- **Cumpără** pune pachetul în coșul magazinului și leagă comanda (`sale.order`) de contul IAP care a deschis pagina (token păstrat în sesiune).
- Cumpărare direct din magazin: coșul fără cont IAP cere adresa bazei Odoo care primește creditele (**Adresa bazei Odoo** pe comandă). Fără cont și fără adresă, plata este refuzată.
- Lista de prețuri a pachetelor se alege pe serviciu (**Listă de prețuri pentru credite**, de exemplu în EUR): pagina de credite îi arată prețurile, iar coșul cumpărătorului venit de acolo o folosește, oricare ar fi lista implicită a site-ului.
- Catalog public al serviciilor (`/iap/all-in-app-services`) și o pagină pe serviciu (`/iap/in-app-services/<cod>`), pentru serviciile bifate **Publicat în catalog**: preț pe operație, credite gratuite, pachete cu „cel mai bun preț" și întrebări frecvente. Pachetele publicate pe site au butonul **Cumpără**, spre pagina produsului din magazin.
- Creditele se vând doar firmelor: la plată, adresa de facturare trebuie să aibă o firmă cu cod fiscal (CUI sau cod TVA), în orice țară; altfel plata e refuzată cu un mesaj clar.
- Taxarea inversă se aplică doar firmelor din alt stat UE cu cod TVA valid în VIES (*Verify VAT Numbers* activ pe companie); firmele UE neînregistrate în VIES plătesc TVA-ul românesc (21%).
- La confirmarea comenzii, creditează automat contul IAP cu numărul de credite cumpărate, o singură dată (idempotent prin `iap_credited`), cu o linie **Cumpărare** în istoricul contului, legată de comandă. O comandă pentru o bază încă neconectată la Terrabit așteaptă și primește creditele când baza intră în portofel.
- Pagina de confirmare a comenzii arată creditele adăugate, soldul nou și valabilitatea (12 luni, prelungită la fiecare cumpărare); cumpărătorul primește emailul **IAP: Credits Added**.

#### 3. Dependențe

- [terrabit_iap_server](../terrabit_iap_server/index.md)
- `website_sale`
- `base_vat`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`, care nu solicită analiza codului pentru Componente Cheie; secțiunea de mai jos listează doar extensiile evidente din structura modulului.

**Modele**

- `product.template` (extins): câmpurile pachetului de credite (`is_iap_credit`, `iap_credit_amount`, `iap_credit_bonus`, `iap_service_code`).
- `sale.order` (extins): contul IAP al comenzii, adresa bazei Odoo, verificările de la plată și creditarea la confirmare (`iap_credited`).
- `iap.server.service` (extins): lista de prețuri pentru credite și publicarea în catalog.
- `iap.server.account` (extins): extensii ale contului IAP pentru achiziții.
- `iap.server.transaction` (extins): legătura liniei **Cumpărare** cu comanda de vânzare.

**Vizualizări**

- `product_template_form_view_iap_credit`: câmpurile de credit pe formularul produsului.
- `view_iap_server_service_form_credit_pricelist`: lista de prețuri pe formularul serviciului.
- `view_iap_server_transaction_form_sale`: comanda pe formularul tranzacției.
- `catalog_page`, `catalog_service_page`, `catalog_unit`: catalogul public al serviciilor (șabloane QWeb).

**Rute**

- `/iap/buy_credits`: adaugă pachetul în coș și duce la checkout.
- `/iap/cart/database`: reține adresa bazei Odoo care primește creditele coșului (POST).
- `/iap/all-in-app-services` și `/iap/in-app-services/<cod>`: catalogul public.

**Acțiuni Automate / Acțiuni Server**

- Niciuna definită în modul.

#### 5. Conexiuni

- [terrabit_iap_server](../terrabit_iap_server/index.md): serverul IAP pe care rulează acest modul; furnizează serviciile IAP și conturile de credite creditate la confirmarea comenzii.
