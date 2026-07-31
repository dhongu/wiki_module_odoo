# Picking Validation Restrict (localizat la `deltatech_picking_restrict/index.md`)

- **Nume Tehnic:** `deltatech_picking_restrict`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_restrict`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_restrict`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul permite restricționarea validării transferurilor de stoc (picking-uri) pe baza unui grup de securitate atașat tipului de operațiune, astfel încât doar utilizatorii autorizați să poată confirma anumite tipuri de transferuri (de exemplu livrări sau recepții sensibile). În plus, oferă două opțiuni de control al calității datelor la validare: blocarea confirmării dacă cantitatea efectivă diferă de cantitatea rezervată și blocarea confirmării dacă apar produse noi, nerezervate inițial, cu cantitate efectivă diferită de zero.

#### 2. Funcționalități Cheie

- Atașarea unui grup de securitate unui tip de operațiune (`stock.picking.type`) — doar utilizatorii din acel grup pot valida transferuri de acest tip; dacă nu este setat niciun grup, nu există nicio restricție.
- Opțiunea „Restrict done quantities to reserved" pe tipul de operațiune: dacă este activată, nu se poate valida un transfer în care cantitatea efectivă diferă de cantitatea rezervată.
- Opțiunea „Restrict new products" pe tipul de operațiune: dacă este activată, nu se poate valida un transfer în care apar produse cu cantitate rezervată zero dar cantitate efectivă diferită de zero (produse „nerecunoscute"/neplanificate).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile pentru Componente Cheie au fost acoperite în mare parte de `readme/DESCRIPTION.md`. Pentru referință tehnică rapidă: modulul extinde `stock.picking.type` cu câmpurile `validate_group_id`, `restrict_quantities` și `restrict_new_products` (expuse în vizualizarea `view_picking_type_form`, care moștenește `stock.view_picking_type_form`), și suprascrie `button_validate()` pe `stock.picking` pentru a aplica cele trei verificări la momentul confirmării transferului.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale reale cu alte module documentate în wiki (nicio altă suită nu referențiază câmpurile `validate_group_id`, `restrict_quantities` sau `restrict_new_products`).
