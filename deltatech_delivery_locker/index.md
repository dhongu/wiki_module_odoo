# Delivery in locker - Base (localizat la `deltatech_delivery_locker/index.md`)

- **Nume Tehnic:** `deltatech_delivery_locker`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_locker
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_locker`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul oferă structura de date de bază și logica pentru gestionarea livrărilor în lockere (puncte fixe de ridicare a coletelor) în Odoo. El servește drept fundație comună, independentă de curier, pe care se construiesc integrările specifice fiecărui transportator (de exemplu Sameday, DPD, Packeta) și instrumentele de selecție de pe website. Modulul introduce un model unitar pentru stocarea informațiilor despre lockere, leagă punctele de ridicare de adresele clienților și de comenzile de vânzare și pune la dispoziție operatorilor din backend o hartă interactivă pentru alegerea sau corectarea punctului de livrare.

#### 2. Funcționalități Cheie

- **Model unitar de lockere**: introduce modelul `delivery.locker` pentru a stoca toate informațiile despre lockere într-un mod structurat și independent de curier.
- **Gestionare din backend**: vizualizări dedicate (listă, formular și căutare) în meniul Inventar pentru administrarea și vizualizarea lockerelor disponibile.
- **Integrare cu transportatorii**: adaugă opțiunea „Use Locker” pe metodele de livrare și oferă un hook generic `action_import_lockers` pentru importurile specifice fiecărui furnizor.
- **Configurare automată**: sincronizează automat opțiunea „Use Locker” cu câmpurile de locații specifice curierului (de exemplu `sd_use_locations` pentru Sameday).
- **Integrare cu adresele**: extinde `res.partner` cu un câmp `locker_id` care leagă adresele de livrare ale clienților direct de punctele fixe de ridicare.
- **Suport pentru comenzi de vânzare**: include un câmp `locker` pe comanda de vânzare pentru a stoca codul lockerului selectat și îl sincronizează cu datele standard Odoo despre locația de ridicare.
- **Selecție locker din backend**: un buton „Choose Locker on map” este disponibil în wizardul „Add Shipping” (`choose.delivery.carrier`) și în wizardul „Delivery Carrier Details” (generare AWB), permițând operatorilor să selecteze sau să corecteze punctul de livrare folosind aceeași hartă interactivă ca și clienții de pe website.
- **Indicatori vizuali**: feedback vizual clar pe comenzile de vânzare cu livrare în locker, inclusiv un ribbon „Locker”, un banner informativ cu codul lockerului și o coloană dedicată „Locker” în liste.
- **Compatibilitate produse**: permite restricționarea metodelor de livrare cu locker dacă în comandă există produse nepotrivite pentru livrarea în locker (prin câmpul `for_locker` de pe produse).
- **Logică de upsert**: o metodă robustă `upsert_from_data` pentru sincronizarea simplă a datelor despre lockere din API-uri externe ale curierilor.
- **Compatibilitate retroactivă**: menține legăturile cu stocarea istorică a lockerelor bazată pe `res.partner`, oferind în același timp un strat de date modern.

Configurare (din `readme/CONFIGURE.md`): activarea suportului pentru locker se face per curier, din Inventar > Configurare > Livrare > Metode de livrare — se bifează „Use Locker” pe curierul dorit (Sameday, Fan Curier, Cargus, Packeta etc.) și apoi se apasă „Get Lockers” pentru a importa lockerele disponibile.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `delivery`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`. DESCRIPTION.md descrie explicit următoarele componente, redate mai jos pentru claritate.

**Modele**

- `delivery.locker`: modelul nou, central, care stochează informațiile despre lockere independent de curier (strat de date modern, cu metoda `upsert_from_data`).
- `delivery.carrier` (extins): adaugă opțiunea „Use Locker” și hook-ul generic `action_import_lockers`, cu sincronizare către câmpurile specifice curierului.
- `res.partner` (extins): adaugă câmpul `locker_id` pentru a lega adresa de livrare de un punct fix de ridicare.
- `sale.order` (extins): adaugă câmpul `locker` și sincronizarea cu locația de ridicare standard Odoo.
- `product.template` / `product.product` (extins): adaugă câmpul `for_locker` pentru compatibilitatea produselor cu livrarea în locker.

**Vizualizări**

- `locker_view.xml`: vizualizările de listă, formular și căutare pentru `delivery.locker`, accesibile din Inventar > Configurare > Livrare > Delivery Lockers.
- `sale_order_view.xml`: indicatorii vizuali pe comanda de vânzare (ribbon „Locker”, banner cu codul lockerului, coloana „Locker”).
- `wizard/choose_delivery_carrier_views.xml` și `wizard/delivery_carrier_details_view.xml`: butonul „Choose Locker on map” în wizardurile de adăugare livrare și de generare AWB.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_cron_data.xml`: definește o sarcină programată pentru sincronizarea/actualizarea periodică a datelor despre lockere.

#### 5. Conexiuni

- [deltatech_delivery_relay](../deltatech_delivery_relay/index.md): modul soră din aceeași familie de livrare, construit tot pe baza `deltatech_delivery`, ca strat alternativ de puncte de ridicare (relay).
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): oferă selecția metodei de livrare și de plată pe website, context în care se folosește alegerea lockerului.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): extinde acest modul cu selecția lockerului pe harta interactivă din website (frontend).
- [deltatech_delivery_sd_easybox](../deltatech_delivery_sd_easybox/index.md): integrarea specifică Sameday Easybox, construită peste stratul de date al acestui modul.
