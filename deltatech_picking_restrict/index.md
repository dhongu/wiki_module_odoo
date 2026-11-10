# Picking Validation Restrict (localizat la `deltatech_picking_restrict/index.md`)

- **Nume Tehnic:** `deltatech_picking_restrict`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_restrict
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_restrict`
- **Ultima Ingestie:** `2026-11-10`

#### 1. Sumar

Acest modul permite restricționarea validării transferurilor de stoc (picking-uri) pe baza unui grup de securitate atașat tipului de operațiune, astfel încât doar utilizatorii autorizați să poată confirma anumite tipuri de transferuri (de exemplu livrări sau recepții sensibile). În plus, oferă două opțiuni de control al calității datelor la validare: blocarea confirmării dacă cantitatea efectuată diferă de cererea inițială și blocarea confirmării dacă apar produse noi, care nu au fost comandate.

#### 2. Funcționalități Cheie

- Atașarea unui grup de securitate unui tip de operațiune (`stock.picking.type`, câmpul „Group for validation") — doar utilizatorii din acel grup pot valida transferuri de acest tip; dacă nu este setat niciun grup, nu există nicio restricție. Câmpul este vizibil doar administratorilor (`base.group_system`).
- Opțiunea **Restrict done quantities to reserved** pe tipul de operațiune: dacă este activată, un transfer nu poate fi validat când cantitatea efectuată a unei mișcări diferă de cantitatea cerută (cererea), comparate în aceeași unitate de măsură (o linie în duzini nu mai blochează o validare corectă, iar o cantitate modificată este refuzată).
- Opțiunea **Restrict new products** pe tipul de operațiune: dacă este activată, un transfer nu poate fi validat când are cantitate efectuată pe un produs care nu a fost comandat (mișcare adăugată după confirmare sau fără cerere), indiferent de cantitate.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Secțiunile Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md`; mai jos este o referință tehnică rapidă, verificată în cod.

**Modele**

- `stock.picking.type` (extins): câmpurile `validate_group_id`, `restrict_quantities` și `restrict_new_products`.
- `stock.picking` (extins): `button_validate()` este suprascris și aplică cele trei verificări (grupul, cantitățile, produsele noi) înainte de validarea standard; la încălcare ridică `UserError`.

**Vizualizări**

- `view_picking_type_form`: moștenește `stock.view_picking_type_form` și adaugă cele trei câmpuri după `sequence_code`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_picking_restrict_entry_exit](../deltatech_picking_restrict_entry_exit/index.md): modul înrudit, care suprascrie tot `stock.picking.button_validate` pentru a bloca validarea recepțiilor și livrărilor fără linie de comandă sau peste cantitatea comandată; nu există dependență între cele două (ambele depind doar de `stock`).
