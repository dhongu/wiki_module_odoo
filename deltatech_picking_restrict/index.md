# Picking Validation Restrict (localizat la `deltatech_picking_restrict/index.md`)

- **Nume Tehnic:** `deltatech_picking_restrict`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_picking_restrict
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_restrict`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul restricționează validarea transferurilor de stoc pe baza unui grup de securitate atașat tipului de operațiune, astfel încât doar utilizatorii autorizați să poată valida anumite transferuri. În plus, oferă două opțiuni de control la validare: cantitățile efectuate trebuie să corespundă celor rezervate și nu se acceptă produse noi, nerezervate.

#### 2. Funcționalități Cheie

- Un grup de securitate atașat tipului de operațiune: doar utilizatorii din grup pot valida transferurile de acest tip; dacă nu e setat niciun grup, nu există restricție.
- Opțiunea „Restrict done quantities to reserved”: transferul nu se poate valida dacă cantitatea efectuată diferă de cea rezervată.
- Opțiunea „Restrict new products”: transferul nu se poate valida dacă există produse cu cantitate rezervată zero și cantitate efectuată diferită de zero.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Modulul extinde `stock.picking.type` cu câmpurile `validate_group_id`, `restrict_quantities` și `restrict_new_products` și suprascrie `button_validate()` pe `stock.picking`, pentru a aplica verificările la validare.

#### 5. Conexiuni

- Nu există conexiuni funcționale către alte module din wiki.
