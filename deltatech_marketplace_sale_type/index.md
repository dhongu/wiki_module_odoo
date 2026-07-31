# Tip comandă de vânzare Marketplace (localizat la `deltatech_marketplace_sale_type/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale_type`
- **Versiune:** `19.0.0.0.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_marketplace_sale_type`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_sale_type`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul introduce un sistem specializat de clasificare pentru comenzile de vânzare provenite din marketplace, permițând companiilor să categorisească și să analizeze vânzările în funcție de diferite tipuri de comandă. Din perspectivă de business, această categorisire este esențială pentru înțelegerea tiparelor de vânzare specifice fiecărui marketplace și pentru optimizarea strategiilor de vânzare pentru fiecare canal conectat.

#### 2. Funcționalități Cheie

- Analiză detaliată a vânzărilor: grupare și raportare a vânzărilor din marketplace în funcție de tipul comenzii, pentru o perspectivă mai granulară asupra performanței.
- Strategii de vânzare adaptate: dezvoltarea și implementarea de tactici specifice fiecărui marketplace, pe baza tipurilor de comandă și a tendințelor identificate.
- Claritate operațională îmbunătățită: distincție clară între comenzile din marketplace și vânzările directe sau alte categorii de comenzi în Odoo.
- Integrare fluidă a proceselor: alinierea tipurilor de comandă din marketplace cu fluxurile integrate de vânzări, stocuri și raportare.
- Gestionare scalabilă a marketplace-urilor: adaptare facilă la noi marketplace-uri prin definirea și gestionarea de tipuri de comandă personalizate pentru fiecare platformă.

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- `deltatech_record_type`

#### 4. Componente Cheie

Documentația de business este furnizată prin `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a componentelor tehnice (modele, vizualizări, acțiuni) este omisă întrucât readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): nucleul suitei de integrare cu marketplace-uri, peste care se construiește clasificarea comenzilor.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionează comenzile de vânzare din marketplace, extinse de acest modul cu tipuri de comandă.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): modul soră care adaugă etape (stadii) comenzilor de vânzare din marketplace, complementar clasificării pe tipuri.
