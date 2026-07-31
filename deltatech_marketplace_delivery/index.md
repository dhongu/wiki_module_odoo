# Marketplace Delivery addon (localizat la `deltatech_marketplace_delivery/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_delivery`
- **Versiune:** `19.0.0.0.6`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_marketplace_delivery`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_delivery`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul optimizează procesul de logistică și onorare a comenzilor pentru vânzările din marketplace, integrând gestionarea avansată a livrărilor și a lockerelor în ecosistemul marketplace. Din punct de vedere business, permite companiilor să ofere o gamă mai largă de opțiuni de expediere și asigură o urmărire superioară a comenzilor din marketplace, ceea ce duce la creșterea satisfacției clienților.

#### 2. Funcționalități Cheie

- Onorare avansată: gestionează unitar curierii și opțiunile de locker pentru comenzile importate din mai multe marketplace-uri.
- Experiență îmbunătățită pentru client: oferă informații exacte de urmărire și locații de locker cumpărătorilor din marketplace.
- Eficiență crescută: automatizează selecția și asignarea metodelor de livrare pentru comenzile de vânzare specifice marketplace-ului.
- Flexibilitate operațională: integrează ușor noi servicii de livrare și rețele de locker în fluxul de lucru al marketplace-ului.
- Logistică centralizată: monitorizează și gestionează toate expedierile legate de marketplace din tabloul de bord de livrări integrat al Odoo.

#### 3. Dependențe

- `deltatech_marketplace_sale`
- `delivery`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Documentația de business este preluată din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru componente este omisă, întrucât Readme-ul nu o solicită explicit. La nivel de structură, modulul cuprinde modele în `models/` (`backend.py`, `binding_delivery.py`, `binding_sale_order.py`, `delivery.py`), vizualizări în `views/` (`backend_views.xml`, `delivery_carrier_view.xml`, `sale_order_view.xml`) și teste în `tests/test_marketplace.py`.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): modulul de bază al ecosistemului marketplace, în care se integrează gestionarea livrărilor.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea stării livrărilor, complementară onorării comenzilor din marketplace.
