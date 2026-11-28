# Delivery – Distance Pricing (localizat la `deltatech_delivery_transport/index.md`)

- **Nume Tehnic:** `deltatech_delivery_transport`
- **Versiune:** `20.0.2.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_transport
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_transport`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite folosirea unei firme de transport ca metodă de livrare, cu calculul prețului pe baza distanței dintre depozit și adresa clientului. Prețul transportului se stabilește automat pe comanda de vânzare din regulile de preț ale metodei. Modulul nu rezervă expedierea la un curier: nu generează AWB și nu setează referință de urmărire.

#### 2. Funcționalități Cheie

- Calcul de tarif pentru o expediere pe baza regulilor de preț ale metodei de livrare.
- Tip de livrare *Transport company*, cu **partener de transport** și reguli de preț în fila **Transport Configuration** (**Inventar → Configurare → Livrare → Metode de livrare**).
- Reguli cu variabila **Distance**: prețul este *preț de bază + preț unitar × factor*, unde factorul este **Distance** (kilometrii comenzii) sau **Distance Plus** (diferența dintre distanța comenzii și valoarea maximă a regulii); se aplică prima regulă potrivită.
- Câmpul **Distance** (doar citire) pe cotație, calculat cu Google Maps între depozit și adresa de livrare și recalculat la schimbarea adresei sau a depozitului; **Update shipping cost** reîmprospătează costul.
- Cerințe: biblioteca Python `googlemaps` și o cheie API Google Maps cu Distance Matrix API, în parametrul `base_geolocalize.google_map_api_key`; fără cheie, distanța rămâne goală.
- Limitare cunoscută: validarea unei livrări al cărei curier are reguli pe distanță eșuează cu o eroare generică; soluție: nivelul de integrare al metodei setat pe **Get Rate**.
- Pașii cu capturi în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `stock_delivery`
- `base_address_extended`
- `purchase`

Dependență externă Python: `googlemaps`.

#### 4. Componente Cheie

**Modele**

- `delivery.price.rule` (extins): opțiunile `distance` și `distance_plus` pentru variabilă și factor.
- `delivery.carrier` (extins): tipul `transport`, câmpul `transport_partner_id` și metodele `transport_rate_shipment`, `_transport_get_price_available`, `_transport_get_price_from_picking`, `transport_send_shipping`, `transport_get_tracking_link`, `transport_cancel_shipment` (neimplementată).
- `sale.order` (extins): câmpul calculat `distance`, obținut din Google Maps Distance Matrix.
- `stock.picking` (extins): câmpul `transport_order_id`, legătură către comanda de achiziție a serviciului de transport.

**Vizualizări**

- `views/delivery_view.xml`: opțiunile tipului „Transport company” pe metoda de livrare.
- `views/sale_order_view.xml`: câmpul `distance` pe comanda de vânzare.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): suita de bază pentru gestionarea livrărilor și a curierilor Deltatech.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea stării expedierilor, complementară gestiunii transportatorilor.
