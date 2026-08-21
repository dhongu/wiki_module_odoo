# Deltatech Delivery Auto Transport (localizat la `deltatech_delivery_transport/index.md`)

- **Nume Tehnic:** `deltatech_delivery_transport`
- **Versiune:** `19.0.2.0.4`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_transport`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_transport`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul permite folosirea unei firme de transport pe post de curier (carrier) în Odoo, oferind livrare cu transportatori diferiți și calcularea prețului de livrare în funcție de distanță. Astfel, costul de transport poate fi estimat automat pentru o expediere, ajutând la stabilirea corectă a tarifului facturat clientului în comenzile de vânzare.

#### 2. Funcționalități Cheie

- Calcularea prețului de livrare pe baza distanței între adrese.
- Folosirea unei firme de transport ca metodă de livrare (carrier).
- Obținerea tarifelor (rates) pentru o expediere.

Funcționalități neacoperite (lista „Without Features" din readme): generare AWB în format PDF/ZPL/HTML, ștergere AWB, listă de orașe și județe, istoric de status al expedierii, expediere cu mai multe colete, valoare declarată (asigurare), ramburs (cash on delivery), expediere cu id oraș/județ sau cu nume oraș fără id, listă de lockere și puncte de ridicare, expediere cu dimensiuni, notă de retur în AWB, opțiune livrare sâmbăta, opțiune colet deschis, ridicare doar din punctul de pickup indicat, trimitere id locker în AWB.

#### 3. Dependențe

- `delivery`
- `stock_delivery`
- `base_address_extended`
- `purchase`

Dependență externă Python: `googlemaps`.

#### 4. Componente Cheie

Componentele tehnice nu sunt detaliate extensiv, deoarece secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Pe scurt, din analiza codului:

**Modele**

- `delivery.price.rule` (extindere): adaugă opțiunile `distance` și `distance_plus` la câmpurile `variable`/`variable_factor`, permițând reguli de preț bazate pe distanța de livrare.
- `delivery.carrier` (extindere): adaugă tipul de livrare `transport` (firmă de transport) și câmpul `transport_partner_id`; implementează metodele `transport_rate_shipment`, `_transport_get_price_available`, `_transport_get_price_from_picking`, `transport_send_shipping`, `transport_get_tracking_link` și `transport_cancel_shipment` (nu e implementată — ridică `NotImplementedError`).
- `sale.order` (extindere): adaugă câmpul calculat `distance`, obținut prin API-ul Google Maps (Distance Matrix) între depozitul de expediere și adresa de livrare a clientului, folosind cheia API configurată în `base_geolocalize.google_map_api_key`.
- `stock.picking` (extindere): adaugă câmpul `transport_order_id` (legătură către `purchase.order`), pentru asocierea comenzii de achiziție a serviciului de transport cu ridicarea/livrarea de stoc.

**Vizualizări**

- `views/delivery_view.xml`: expune în formularul de metodă de livrare (`delivery.carrier`) opțiunile specifice tipului „Transport company" (partener de transport, reguli de preț pe distanță).
- `views/sale_order_view.xml`: afișează câmpul `distance` pe comanda de vânzare.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): suita de bază pentru gestionarea livrărilor și a curierilor Deltatech.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea statusului expedierilor, complementară gestiunii transportatorilor.
</content>
