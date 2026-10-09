# Warehouse Access (localizat la `deltatech_warehouse_access/index.md`)

- **Nume Tehnic:** `deltatech_warehouse_access`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_warehouse_access
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warehouse_access`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă un control mai fin asupra operațiunilor de depozit, restricționând accesul la anumite depozite doar pentru utilizatorii autorizați. Pentru fiecare depozit se poate defini lista persoanelor care au voie să valideze transferurile, iar orice altă încercare este blocată cu un mesaj clar de eroare.

#### 2. Funcționalități Cheie

- **Restricție pe utilizatori:** în configurarea depozitului apare o filă **Users**, în care administratorul definește utilizatorii autorizați (doar utilizatori interni, nu portal).
- **Securitate la validare:** un utilizator care nu e în listă nu poate valida transferurile (picking) ale unui depozit restricționat; primește o eroare de acces (`Access Error`) cu numele utilizatorului și al depozitului.
- **Reguli flexibile:** dacă lista de utilizatori e goală, rămân valabile drepturile standard Odoo; de la primul utilizator adăugat, accesul este limitat strict la listă.
- **Configurare:** meniul **Inventory > Configuration > Warehouses**, fila **Users** (vizibilă în modul dezvoltator sau pentru utilizatori cu drepturi tehnice).
- Verificarea acoperă și validarea prin wizard-ul de comandă restantă (backorder), care apelează din nou `button_validate`.

#### 3. Dependențe

- `stock`
- `product`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse` (extins): adaugă câmpul `user_ids` (Many2many către `res.users`, doar utilizatori interni).
- `stock.picking` (extins): `button_validate` verifică dacă utilizatorul curent este în `user_ids` al depozitului tipului de operațiune și ridică `AccessError` în caz contrar.

**Vizualizări**

- `view_warehouse`: moștenește `stock.view_warehouse` și adaugă fila **Users** (grup `base.group_no_one`) cu lista utilizatorilor ca kanban.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `deltatech_picking_restrict_entry_exit`: dacă este instalat, testele adaugă utilizatorii în grupul său de bypass pentru a testa doar accesul pe depozit.
