# Deltatech Delivery Auto Transport (localizat la `deltatech_delivery_transport/index.md`)

- **Nume Tehnic:** `deltatech_delivery_transport`
- **Versiune:** `19.0.2.0.2`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_transport`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_transport`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul permite folosirea unei firme de transport pe post de curier (carrier) în Odoo, oferind livrare cu transportatori diferiți și calcularea prețului de livrare în funcție de distanță. Astfel, costul de transport poate fi estimat automat pentru o expediere, ajutând la stabilirea corectă a tarifului facturat clientului în comenzile de vânzare.

#### 2. Funcționalități Cheie

- Calcularea prețului de livrare pe baza distanței între adrese.
- Folosirea unei firme de transport ca metodă de livrare (carrier).
- Obținerea tarifelor (rates) pentru o expediere.

Funcționalități neacoperite (lista „Without Features" din readme): generare AWB în format PDF/ZPL/HTML, ștergere AWB, listă de orașe și județe, istoric de status al expedierii, expediere cu mai multe colete, valoare declarată (asigurare), ramburs (cash on delivery), expediere cu id oraș/județ sau cu nume oraș fără id, listă de lockere și puncte de ridicare, expediere cu dimensiuni, notă de retur în AWB, opțiune livrare sâmbăta, opțiune colet deschis, ridicare doar din punctul de pickup indicat, trimitere id locker în AWB.

#### 3. Dependențe

- `delivery`
- `base_address_extended`
- `purchase`

Dependență externă Python: `googlemaps`.

#### 4. Componente Cheie

Componentele tehnice nu sunt detaliate, deoarece secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Pe scurt, modulul extinde metodele de livrare (`delivery.carrier`) și comenzile de vânzare (`sale.order`) prin vizualizările `views/delivery_view.xml` și `views/sale_order_view.xml`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): suita de bază pentru gestionarea livrărilor și a curierilor Deltatech.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea statusului expedierilor, complementară gestiunii transportatorilor.
