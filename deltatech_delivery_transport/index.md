# Delivery – Distance Pricing (localizat la `deltatech_delivery_transport/index.md`)

- **Nume Tehnic:** `deltatech_delivery_transport`
- **Versiune:** `19.0.2.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_transport
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_transport`
- **Ultima Ingestie:** `2026-11-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite folosirea unei firme de transport pe post de curier (carrier) în Odoo, oferind livrare cu transportatori diferiți și calcularea prețului de livrare în funcție de distanță. Astfel, costul de transport poate fi estimat automat pentru o expediere, ajutând la stabilirea corectă a tarifului facturat clientului în comenzile de vânzare.

#### 2. Funcționalități Cheie

- Calcularea prețului de livrare pe baza distanței între adrese.
- Folosirea unei firme de transport ca metodă de livrare (carrier).
- Obținerea tarifelor (rates) pentru o expediere.
- Metodă de livrare: în **Inventar → Configurare → Livrare → Metode de livrare** se creează o metodă cu **Provider** = **Transport company**, se alege **Delivery Product** pentru linia de transport, apoi în fila **Transport Configuration** se alege **Transport partner** și se adaugă regulile de preț.
- Reguli de preț pe distanță: o regulă poate folosi **Distance** ca variabilă; prețul este *preț de bază + preț unitar × factor*, unde factorul este **Distance** (kilometrii comenzii) sau **Distance Plus** (diferența dintre distanța comenzii și valoarea maximă a regulii); se aplică prima regulă potrivită.
- Distanța pe comandă: câmpul read-only **Distance** de sub adresa de livrare arată distanța dintre depozitul comenzii și adresa de livrare, calculată cu Google Maps și recalculată la schimbarea adresei sau a depozitului.
- Adăugarea transportului: pe ofertă, **Add shipping** → alegerea metodei → **Get rate** → **Add**; dacă adresa se schimbă ulterior, **Update shipping cost** reîmprospătează costul.
- Limite: modulul nu rezervă expedierea — nu setează referință de urmărire și nu poate anula expedieri.
- Limitare cunoscută: validarea unei livrări al cărei curier are reguli de preț pe distanță eșuează momentan cu o eroare generică; soluție: se setează **Integration Level** = **Get Rate** pe metoda de livrare, caz în care prețul pe distanță din comandă se păstrează, iar livrarea se validează normal.
- Cerințe: biblioteca Python `googlemaps` și o cheie Google Maps API cu Distance Matrix activat, în parametrul de sistem `base_geolocalize.google_map_api_key`; fără cheie, distanța rămâne goală.

Funcționalități neacoperite (lista „Without Features" din readme): generare AWB în format PDF/ZPL/HTML, ștergere AWB, listă de orașe și județe, istoric de status al expedierii, expediere cu mai multe colete, valoare declarată (asigurare), ramburs (cash on delivery), expediere cu id oraș/județ sau cu nume oraș fără id, listă de lockere și puncte de ridicare, expediere cu dimensiuni, notă de retur în AWB, opțiune livrare sâmbăta, opțiune colet deschis, ridicare doar din punctul de pickup indicat, trimitere id locker în AWB.

#### 3. Dependențe

- `delivery`
- `stock_delivery`
- `base_address_extended`
- `purchase`

Dependență externă Python: `googlemaps`.

#### 4. Componente Cheie

Componentele tehnice nu sunt detaliate extensiv, deoarece secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md` (completat cu `readme/USAGE.md`), conform fluxului de ingestie. Pe scurt, din analiza codului:

**Modele**

- `delivery.price.rule` (extindere): adaugă opțiunile `distance` și `distance_plus` la câmpurile `variable`/`variable_factor`, permițând reguli de preț bazate pe distanța de livrare.
- `delivery.carrier` (extindere): adaugă tipul de livrare `transport` (firmă de transport) și câmpul `transport_partner_id`; implementează metodele `transport_rate_shipment`, `_transport_get_price_available`, `_transport_get_price_from_picking`, `transport_send_shipping` (fără număr de urmărire) și `transport_get_tracking_link` (returnează `False`); `transport_cancel_shipment` nu e implementată — ridică `NotImplementedError`.
- `sale.order` (extindere): adaugă câmpul calculat `distance`, obținut prin API-ul Google Maps (Distance Matrix) între depozitul de expediere și adresa de livrare a clientului, folosind cheia API configurată în `base_geolocalize.google_map_api_key`.
- `stock.picking` (extindere): adaugă câmpul `transport_order_id` (legătură către `purchase.order`), pentru asocierea comenzii de achiziție a serviciului de transport cu ridicarea/livrarea de stoc.

**Vizualizări**

- `views/delivery_view.xml`: expune în formularul de metodă de livrare (`delivery.carrier`) opțiunile specifice tipului „Transport company" (partener de transport, reguli de preț pe distanță).
- `views/sale_order_view.xml`: afișează câmpul `distance` pe comanda de vânzare.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): suita de bază pentru gestionarea livrărilor și a curierilor Deltatech.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea statusului expedierilor, complementară gestiunii transportatorilor.
