# Relay Delivery – AWB Attach (localizat la `deltatech_delivery_relay/index.md`)

- **Nume Tehnic:** `deltatech_delivery_relay`
- **Versiune:** `20.0.0.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_relay
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_relay`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul atașează automat etichetele AWB în format PDF, primite din sisteme externe de logistică sau de la curieri, direct în Odoo. Documentele de expediere sunt astfel centralizate și accesibile, iar personalul din depozit nu mai caută etichetele pe portaluri externe.

#### 2. Funcționalități Cheie

- Tip de metodă de livrare care nu apelează niciun curier: eticheta AWB (PDF) se atașează comenzii de vânzare, la alegerea metodei de livrare, automat dintr-un fișier `awb_…` primit pe comandă sau din **Detalii transportator** pe livrare.
- Eticheta trece pe livrare și se tipărește cu **Tipărire AWB**; clientul o poate descărca din portal.
- Documentație AWB centralizată: etichete căutabile în Odoo, asociate corect livrărilor.
- Integrare simplă cu diverși furnizori externi printr-un mecanism comun de gestionare a etichetelor.
- Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale`
- `delivery`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, deoarece există `readme/DESCRIPTION.md`, analiza codului pentru această secțiune este omisă. Pentru orientare, modulul extinde `delivery.carrier`, `delivery.carrier.service`, `sale.order`, `stock.package.type` și `stock.picking`, și adaugă șabloanele de portal din `views/portal_templates.xml`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modul de bază pentru livrare, pe care se sprijină gestionarea curierilor și a livrărilor.
