# eCommerce Warehouse Stock (localizat la `deltatech_website_warehouse_stock/index.md`)

- **Nume Tehnic:** `deltatech_website_warehouse_stock`
- **Versiune:** `19.0.0.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_warehouse_stock`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_warehouse_stock`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul îmbunătățește experiența de eCommerce afișând disponibilitatea în stoc, în timp real, pentru fiecare depozit, direct pe pagina produsului din website. Clienții văd dacă un produs este în stoc, are stoc redus sau este indisponibil la anumite locații, ceea ce îi ajută să ia decizii de cumpărare informate, în funcție de proximitatea sau disponibilitatea depozitului. Spre deosebire de funcția standard „Click & Collect" din Odoo 18/19 (bazată pe selector pe hartă), acest modul oferă o abordare complementară, cu vizibilitate ridicată: starea stocului este afișată static pe pagina produsului, fără clicuri sau popup-uri, iar datele exacte de inventar sunt protejate printr-un prag configurabil.

#### 2. Funcționalități Cheie

- Adaugă stocul locației principale a fiecărui depozit pe pagina produsului (product template) din website.
- Dacă stocul este < 0, afișează „Out of stock" (indisponibil) pentru acel depozit.
- Dacă stocul este între 0 și 10 (inclusiv), afișează cantitatea efectivă a produsului.
- Dacă stocul este > 10, afișează „Available" (disponibil) pentru acel depozit, fără a dezvălui cantitatea exactă.
- Pragul de stoc (implicit 10) este configurabil din setările site-ului, protejând datele de inventar și imaginea brandului.
- Numele depozitului afișat este preluat din formularul depozitului (stock.warehouse).
- Există o bifă pe depozit pentru a alege dacă stocul respectiv este afișat pe pagina produsului.
- Funcționează ca addon informativ complementar funcției standard Odoo „Click & Collect" (`website_sale_collect`), oferind clienților vizibilitate asupra distribuției stocului înainte de a începe procesul de checkout.

#### 3. Dependențe

- `website`
- `website_sale_stock`

#### 4. Componente Cheie

DESCRIPTION.md acoperă scopul și funcționalitățile modulului. Conform fluxului de ingestie, această secțiune nu detaliază componente tehnice suplimentare, deoarece nu sunt menționate explicit în Readme ca fiind necesare.

#### 5. Conexiuni

- `website_sale_collect`: funcția standard Odoo 18/19 „Click & Collect" (selector pe hartă, alegere punct de ridicare), pe care acest modul o completează cu afișarea informativă a stocului pe depozite, direct pe pagina produsului.
