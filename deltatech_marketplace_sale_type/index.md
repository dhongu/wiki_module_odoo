# Marketplace Order Types (localizat la `deltatech_marketplace_sale_type/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale_type`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_sale_type
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_sale_type`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul introduce un sistem specializat de clasificare pentru comenzile de vânzare provenite din marketplace, permițând companiilor să categorisească și să analizeze vânzările în funcție de diferite tipuri de comandă. Din perspectivă de business, această categorisire este esențială pentru înțelegerea tiparelor de vânzare specifice fiecărui marketplace și pentru optimizarea strategiilor de vânzare pentru fiecare canal conectat.

#### 2. Funcționalități Cheie

- Analiză detaliată a vânzărilor: grupare și raportare a vânzărilor din marketplace în funcție de tipul comenzii, pentru o perspectivă mai granulară asupra performanței.
- Strategii de vânzare adaptate: dezvoltarea și implementarea de tactici specifice fiecărui marketplace, pe baza tipurilor de comandă și a tendințelor identificate.
- Claritate operațională îmbunătățită: distincție clară între comenzile din marketplace și vânzările directe sau alte categorii de comenzi în Odoo.
- Integrare fluidă a proceselor: alinierea tipurilor de comandă din marketplace cu fluxurile integrate de vânzări, stocuri și raportare.
- Gestionare scalabilă a marketplace-urilor: adaptare facilă la noi marketplace-uri prin definirea și gestionarea de tipuri de comandă personalizate pentru fiecare platformă.
- Tipul de comandă se alege pe backend-ul de marketplace, în câmpul **Order Type** din grupul **Orders** al formularului backend-ului, și se aplică comenzilor importate prin acel backend.

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_record_type](../deltatech_record_type/index.md)

#### 4. Componente Cheie

Documentația de business este furnizată prin `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a componentelor tehnice (modele, vizualizări, acțiuni) este omisă întrucât readme-ul nu o solicită explicit. Din inspecția rapidă a codului: modulul adaugă câmpul `so_type_id` (cu urmărire în chatter) pe `marketplace.backend`, folosind tipul de înregistrare din `deltatech_record_type`, și extinde formularul `deltatech_marketplace.view_marketplace_backend_form` cu acest câmp; la pregătirea valorilor unei comenzi importate (`marketplace.sale.order`), tipul backend-ului se scrie în câmpul `so_type` al comenzii.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): nucleul suitei de integrare cu marketplace-uri, peste care se construiește clasificarea comenzilor.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionează comenzile de vânzare din marketplace, extinse de acest modul cu tipuri de comandă.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): modul soră care mapează statusurile comenzilor din marketplace pe fazele comenzii de vânzare, complementar clasificării pe tipuri.
