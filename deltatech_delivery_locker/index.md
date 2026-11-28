# Delivery in locker - Base (localizat la `deltatech_delivery_locker/index.md`)

- **Nume Tehnic:** `deltatech_delivery_locker`
- **Versiune:** `20.0.1.8.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_locker
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_locker`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Acest modul oferă structura de date de bază și logica pentru gestionarea livrărilor în lockere (puncte fixe de ridicare a coletelor) în Odoo. Este fundația comună, independentă de curier, pe care se construiesc integrările fiecărui transportator (Sameday, DPD, Packeta ș.a.) și instrumentele de selecție de pe website. Introduce un model unitar pentru lockere, leagă punctele de ridicare de adresele clienților și de comenzile de vânzare și oferă operatorilor o hartă interactivă pentru alegerea sau corectarea punctului de livrare.

#### 2. Funcționalități Cheie

- **Model unitar de lockere:** modelul `delivery.locker` stochează informațiile despre lockere independent de curier.
- **Gestionare din backend:** listă, formular și căutare în *Inventar > Configurare > Livrare > Delivery Lockers*, cu filtrare după furnizor, oraș sau curier.
- **Integrare cu transportatorii:** opțiunea **Use Locker** pe metoda de livrare, butonul **Get Lockers** (hook generic `action_import_lockers`) pentru importul specific fiecărui furnizor și sincronizarea cu câmpurile proprii ale curierilor (ex. `sd_use_locations` la Sameday).
- **Actualizare programată:** cataloagele de lockere se reîmprospătează periodic (la 7 zile), iar AWB-urile eșuate pentru un locker prea nou sunt reîncercate automat.
- **Integrare cu adresele și comenzile:** câmpul `locker_id` pe partener și câmpul `locker` pe comanda de vânzare, sincronizat cu locația standard Odoo de ridicare.
- **Selecție din backend:** butonul „Choose Locker on map" în wizardul „Add Shipping" și în „Delivery Carrier Details" (generare AWB), cu aceeași hartă ca pe website.
- **Indicatori vizuali:** ribbon „Locker", banner cu codul lockerului și coloană „Locker" în liste.
- **Compatibilitate produse:** câmpul `for_locker` pe produse permite restricționarea metodelor cu locker pentru comenzile cu produse nepotrivite.
- **Județul AWB-ului:** județul lockerului (nu al clientului) pleacă pe AWB, preluat de la curier acolo unde îl comunică, altfel dedus din localitate și cod poștal.
- **Upsert și compatibilitate:** metoda `upsert_from_data` sincronizează datele din API-urile curierilor; legăturile cu stocarea istorică pe `res.partner` se păstrează.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `delivery`
- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `delivery.locker`: modelul central de lockere, independent de curier (metoda `upsert_from_data`).
- `delivery.carrier` (extins): opțiunea **Use Locker**, hook-ul `action_import_lockers` și importul periodic.
- `res.partner` (extins): câmpul `locker_id`.
- `sale.order` (extins): câmpul `locker` și sincronizarea cu locația de ridicare standard.
- `product.template` / `product.product` (extinse): câmpul `for_locker`.
- `stock.picking` (extins): tratarea lockerului la emiterea AWB-ului.
- `choose.delivery.carrier`, `delivery.carrier.details` (wizarduri extinse): butonul de alegere a lockerului pe hartă.

**Vizualizări**

- `views/locker_view.xml`: listă, formular și căutare pentru `delivery.locker`.
- `views/sale_order_view.xml`: ribbon, banner și coloană „Locker" pe comanda de vânzare.
- `wizard/choose_delivery_carrier_views.xml`, `wizard/delivery_carrier_details_view.xml`: „Choose Locker on map".

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_import_lockers` („Delivery: Refresh locker catalogs"): reîmprospătează cataloagele de lockere, la 7 zile.
- `ir_cron_retry_locker_shipments` („Delivery: retry AWB for a locker too new"): reîncearcă la 3 minute AWB-urile respinse pentru un locker prea nou în catalogul curierului.

#### 5. Conexiuni

- [deltatech_delivery_relay](../deltatech_delivery_relay/index.md): modul soră din familia de livrare, strat alternativ de puncte de ridicare.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): selecția metodei de livrare și de plată pe website, context în care se alege lockerul.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): selecția lockerului pe harta din website.
- [deltatech_delivery_sd_easybox](../deltatech_delivery_sd_easybox/index.md): integrarea Sameday Easybox, construită peste stratul de date al acestui modul.
- [deltatech_delivery_fc](../deltatech_delivery_fc/index.md), [deltatech_delivery_gls](../deltatech_delivery_gls/index.md), [deltatech_delivery_innoship](../deltatech_delivery_innoship/index.md): curieri care își importă lockerele în catalogul comun.
