# Picking Flow Routes (localizat la `terrabit_picking_flow/index.md`)

- **Nume Tehnic:** `terrabit_picking_flow`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_picking_flow
- **Cale Locală:** `odoo-addons/bitshop/terrabit_picking_flow`
- **Ultima Ingestie:** `2026-11-14`

#### 1. Sumar

Modulul permite urmărirea unei livrări/ridicări (picking) printr-o secvență ordonată și predefinită de locații fizice — un „flux de ridicare" (picking flow). În multe depozite o comandă nu trece direct din stoc la doc-ul de expediere, ci parcurge stații intermediare (de exemplu: *Pregătire → Control calitate → Ambalare → Doc de încărcare*). Modulul modelează acest traseu ca o rută reutilizabilă formată din locații ordonate, atribuie o rută unei comenzi de vânzare și urmărește apoi fiecare picking asociat pe măsură ce avansează de la o locație la următoarea.

#### 2. Funcționalități Cheie

- **Vizibilitate operațională** — un board Kanban grupat după locația din flux (**Inventar → Operațiuni → Picking flow**) arată dintr-o privire unde se află fiecare comandă și care este următoarea stație; fiecare card are un badge cu locația următoare.
- **Progres controlat** — un utilizator obișnuit poate avansa un picking doar către locația *următoare* din rută; sărirea peste stații sau mutarea înapoi dă eroarea „Location is not valid". Un *Picking Flow Manager* poate muta pickingul în orice locație.
- **Aceeași regulă și pe comanda de vânzare** — restricția se aplică și locației din flux a comenzii în sine, indiferent de punctul de intrare (formular, import, API): un utilizator obișnuit poate muta comanda doar la locația următoare, iar o comandă nouă (sau una care își schimbă ruta) pornește mereu de la prima locație a rutei. O comandă duplicată pornește din nou de la prima locație.
- **Trasee reutilizabile** — rutele se definesc o singură dată și se reutilizează pe mai multe comenzi; pe comanda de vânzare (secțiunea *Alte informații*) se alege *Flow Route*, locația se setează automat pe prima din rută, iar ambele câmpuri se propagă pe pickingurile comenzii.
- **Configurare** — locațiile și rutele se administrează din **Inventar → Configurare → Picking flow** (*Picking flow locations* / *Picking flow routes*), meniu vizibil doar grupului *Picking Flow Manager*; ordinea locațiilor dintr-o rută se stabilește prin handle-ul de secvență de pe linii, iar o rută nefolosită poate fi arhivată.
- **Grupare personalizată** — căutarea pe pickinguri oferă gruparea „Flow location" pentru vizualizări proprii ale fluxului.

#### 3. Dependențe

- `stock`
- `sale_management`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `picking.flow.location`: locație individuală dintr-un flux (stație fizică); expune `get_next_location()` (locația următoare dintr-o rută, pornind de la cea curentă) și `_check_flow_transition()`, verificarea comună a mutărilor, ocolită de superuser și de managerii de flux.
- `picking.flow.route`: ruta/traseul — o listă ordonată de locații (`line_ids`), reutilizabilă pe mai multe comenzi de vânzare, arhivabilă (`active`).
- `picking.flow.route.line`: linia de ordine dintr-o rută, leagă o rută de o locație și de secvența ei de parcurgere.
- `sale.order` (extindere): adaugă `flow_route_id` și `flow_location_id` (`copy=False`); `create()` și `write()` verifică tranziția locației, iar `_onchange_flow_route` setează prima locație din rută.
- `stock.picking` (extindere): adaugă `flow_location_id` (related din comandă, editabil, stocat, cu `group_expand` pentru afișarea tuturor locațiilor în Kanban), `flow_route_id` (related din comandă) și `next_flow_location_id` (calculat); `write()` și onchange-ul pe locație aplică aceeași verificare de tranziție.

**Vizualizări**

- `view_picking_form`: adaugă `flow_route_id` și `flow_location_id` pe formularul de picking.
- `view_picking_internal_search`: adaugă gruparea „Flow location" în căutarea pickingurilor.
- `stock_picking_kanban`: adaugă pe cardul Kanban badge-ul „Next location" (`next_flow_location_id`).
- `picking_flow_action` + meniul „Picking flow" (Inventar → Operațiuni): Kanban/formular pe `stock.picking`, grupat implicit după locația din flux.
- `picking_flow_routes_form`: formular pentru definirea unei rute (nume, activ, linii de locații ordonate prin drag&drop).
- `action_picking_flow_locations` / `action_picking_flow_routes` + meniul de configurare „Picking flow" (Inventar → Configurare, doar `group_flow_manager`).
- `sale_order_view_form`: adaugă `flow_route_id` și `flow_location_id` (needitabil) pe comanda de vânzare, în „Alte informații".

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. Controlul progresiei se face sincron, în `create()`/`write()` pe `sale.order` și `stock.picking`.

#### 5. Conexiuni

- `sale_stock`: pickingurile generate din comanda de vânzare moștenesc ruta și locația din flux.

---

**Securitate:** definește grupul `group_flow_manager` („Picking Flow Manager", cu `base.user_root` și `base.user_admin` incluși implicit), care poate muta liber pickingurile și comenzile între locații și vede meniul de configurare a rutelor/locațiilor. Utilizatorii obișnuiți (`base.group_user`) pot citi rutele și locațiile și pot avansa doar la locația următoare.
