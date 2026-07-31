# Terrabit Picking Flow (localizat la `terrabit_picking_flow/index.md`)

- **Nume Tehnic:** `terrabit_picking_flow`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_picking_flow`
- **Cale Locală:** `odoo-addons/bitshop/terrabit_picking_flow`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul permite urmărirea unei livrări/ridicări (picking) printr-o secvență ordonată și predefinită de locații fizice — un „flux de ridicare" (picking flow). În multe depozite o comandă nu trece direct din stoc la doc-ul de expediere, ci parcurge stații intermediare (de exemplu: *Pregătire → Control calitate → Ambalare → Doc de încărcare*). Modulul modelează acest traseu ca o rută reutilizabilă formată din locații ordonate, atribuie o rută unei comenzi de vânzare și urmărește apoi fiecare picking asociat pe măsură ce avansează de la o locație la următoarea.

#### 2. Funcționalități Cheie

- **Vizibilitate operațională** — un board Kanban grupat după locația din flux arată dintr-o privire unde se află fizic fiecare comandă pe hala de producție/depozit și care este următoarea stație pe care trebuie să o atingă.
- **Progres controlat** — utilizatorii non-manageri pot avansa un picking doar către locația *următoare* definită în rută. Sărirea peste stații sau mutarea înapoi este respinsă, ceea ce menține disciplina fluxului fizic.
- **Trasee reutilizabile** — rutele sunt definite o singură dată și reutilizate pe mai multe comenzi; locația din flux a unei comenzi de vânzare se propagă automat către picking-urile sale.

#### 3. Dependențe

- `stock`
- `sale_management`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `picking.flow.location`: locație individuală dintr-un flux (stație fizică); expune metoda `get_next_location()` care determină locația următoare dintr-o rută dată, pornind de la locația curentă.
- `picking.flow.route`: ruta/traseul — o listă ordonată de locații (`line_ids`), reutilizabilă pe mai multe comenzi de vânzare.
- `picking.flow.route.line`: linia de ordine dintr-o rută, leagă o rută de o locație și de secvența ei de parcurgere.
- `sale.order` (extindere): adaugă câmpurile `flow_route_id` (rută flux) și `flow_location_id` (locație flux); la selectarea rutei, locația se setează automat pe prima locație din rută (`_onchange_flow_route`).
- `stock.picking` (extindere): adaugă `flow_location_id` (related, editabil, stocat, cu `group_expand` pentru afișarea tuturor locațiilor în Kanban), `flow_route_id` (related din comandă) și `next_flow_location_id` (calculat). Suprascrie `write()` pentru a bloca, pentru utilizatorii fără grupul de manager, mutarea unui picking altundeva decât pe locația următoare validă din rută (ridică `UserError` „Location is not valid").

**Vizualizări**

- `view_picking_form`: adaugă câmpurile `flow_route_id` și `flow_location_id` pe formularul de picking, lângă `owner_id`.
- `view_picking_internal_search`: adaugă filtrul de grupare „Flow location" în căutarea internă a picking-urilor.
- `stock_picking_kanban`: adaugă pe cardul Kanban un badge evidențiat cu „Next location" (`next_flow_location_id`).
- `picking_flow_action` + meniul „Picking flow" (sub Inventar → Operațiuni): Kanban/formular pe `stock.picking`, grupat implicit după locația din flux.
- `picking_flow_routes_form`: formular pentru definirea unei rute (nume, activ/inactiv, linie de locații ordonate cu widget `handle` pentru drag&drop).
- `action_picking_flow_locations` / `action_picking_flow_routes` + meniul de configurare „Picking flow" (sub Inventar → Configurare, vizibil doar grupului `group_flow_manager`): administrarea locațiilor și rutelor.
- `sale_order_view_form`: adaugă `flow_route_id` și `flow_location_id` (needitabil) pe formularul comenzii de vânzare, în secțiunea „Alte informații".

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul. Controlul progresiei se face direct în `write()` pe `stock.picking` (validare sincronă, nu acțiune programată).

#### 5. Conexiuni

Nu au fost identificate în cod alte module din monorepo care referențiază acest modul sau modelele sale (`picking.flow.*`); nu sunt incluse conexiuni pentru a evita legături neverificate.

---

**Securitate:** definește grupul `group_flow_manager` („Picking Flow Manager", cu `base.user_root` și `base.user_admin` incluși implicit), care are drepturi depline de mutare a picking-urilor și acces la meniul de configurare a rutelor/locațiilor.
