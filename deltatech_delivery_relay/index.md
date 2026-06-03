# Relay Delivery Shipping (localizat la `deltatech_delivery_relay/index.md`)

- **Nume Tehnic:** `deltatech_delivery_relay`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_relay
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_relay`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul optimizează operațiunile de expediere prin atașarea automată a etichetelor AWB (Air Waybill) în format PDF direct din sistemele externe de logistică sau ale curierilor în Odoo. Din punct de vedere de business, această integrare asigură gestionarea și accesibilitatea centralizată a întregii documentații de expediere, reducând timpul petrecut de personalul din depozit pentru descărcarea manuală a etichetelor din portalurile externe.

#### 2. Funcționalități Cheie

- Documentație de expediere automatizată: primește și stochează instantaneu etichetele AWB în Odoo, pentru tipărire și utilizare imediată.
- Viteză operațională îmbunătățită: elimină nevoia personalului din depozit de a comuta între platforme diferite pentru a obține etichetele de expediere.
- Management logistic centralizat: menține o evidență completă și ușor de căutat a tuturor etichetelor de expediere în cadrul ERP-ului Odoo.
- Acuratețe sporită a livrării: asigură asocierea corectă a etichetelor generate de curier cu comenzile de livrare potrivite.
- Integrare logistică scalabilă: integrare facilă cu o varietate de furnizori externi de livrare printr-un sistem consistent de gestionare a etichetelor.

#### 3. Dependențe

- `sale`
- `delivery`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, componentele tehnice nu sunt detaliate deoarece modulul dispune de un fișier `readme/DESCRIPTION.md` care acoperă Sumarul și Funcționalitățile Cheie, iar acesta nu solicită explicit analiza codului pentru această secțiune.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modul de bază pentru livrare pe care se sprijină gestionarea curierilor și a comenzilor de livrare extinse de acest modul.
