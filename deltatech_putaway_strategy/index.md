# Putaway Strategy (localizat la `deltatech_putaway_strategy/index.md`)

- **Nume Tehnic:** `deltatech_putaway_strategy`
- **Versiune:** `20.0.1.1.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_putaway_strategy`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_putaway_strategy`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Regulile standard de depozitare (putaway) trimit un produs către un raft fix, indiferent dacă mai are loc sau nu, iar livrările pot rezerva marfă recepționată dar încă neașezată pe raft. Acest modul oferă rafturilor o capacitate, ține depozitarea în limita ei și adaugă, pe tipul de operație, opțiuni de control al depozitării și rezervării. Valoarea de afaceri: utilizare mai bună a spațiului, sugestii de amplasare mai inteligente la recepții și transferuri interne, livrări care alocă preferențial marfa deja pusă la raft.

#### 2. Funcționalități Cheie

- **Capacitatea raftului:** pe formularul locației (**Inventar > Configurare > Locații**), secțiunea **Capacity**, câmpul **Max products (leaf)** setează cantitatea maximă (în unitatea de măsură a produsului, toate produsele însumate). Zero înseamnă fără limită.
- **Indicatori calculați** pe fiecare locație: **Max products**, **Current quantity** (în stoc), **Planned quantity** (pe liniile de mișcare nefinalizate) și **Occupancy** (current / max, între 0 și 1). Pentru locațiile părinte, maximul și cantitatea curentă sunt suma copiilor. Câmpurile nu sunt afișate în vizualizările modulului; sunt destinate rapoartelor sau unei hărți de depozit.
- **Putaway care respectă capacitatea:** un raft plin (sau care ar deveni plin cu cantitatea deja planificată) nu mai este propus. Dacă o linie rezervată depășește spațiul liber, linia este împărțită: raftul primește ce încape, restul merge pe un alt raft ales de putaway. Cantitățile în alte unități sunt convertite în unitatea produsului. La validare, un transfer care ar supraîncărca un raft este blocat cu eroare explicită. Verificările standard ale categoriilor de depozitare (greutate, capacități de produs și pachet, amestec de produse) rămân active.
- **Căutare în sublocații:** cu parametrul de sistem `deltatech_putaway_strategy.search_sublocation` = `True`, când locația din regulă are sublocații, se propune întâi o sublocație care conține deja produsul, apoi primul raft (alfabetic) cu loc liber.
- **Preferă raftul care conține deja produsul:** cu parametrul `deltatech_putaway_strategy.prefer_existing_stock_location` = `True`, se caută rafturile de sub locația de intrare care au stoc liber din produs (chiar în afara locației din regulă) și se propune cel cu cea mai mare cantitate care mai are loc. Raftul sursă al unui transfer intern nu este niciodată propus ca destinație. Implicit dezactivat.
- **Opțiuni pe tipul de operație** (**Inventar > Configurare > Tipuri de operații**):
  - `Avoid Putaway Rules`: transferurile păstrează locația de destinație, fără reguli de putaway.
  - `Avoid Root Location on Reservation` (doar livrări): livrarea nu rezervă niciodată stocul aflat direct în locația sursă (de regulă rădăcina depozitului, ex. `WH/Stock`); marfa neașezată pe raft nu e alocată comenzilor de vânzare, iar sublocațiile rămân eligibile.
- **Optimizare:** indexuri de bază de date pe `product_id` și `sequence` pentru `stock.putaway.rule`.
- **Limitare:** `Planned quantity` se calculează doar pentru rafturile cu capacitate setată; pentru locațiile părinte este mereu zero, nu suma copiilor.
- Parametrii de sistem se setează în **Setări > Tehnic > Parametri de sistem** (mod dezvoltator).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

*Notă: secțiunea reflectă componentele menționate în `readme/DESCRIPTION.md`.*

**Modele**

- `stock.location`: extins cu câmpurile de capacitate și ocupare și cu calculul lor.
- `stock.putaway.rule`: indexuri pe `product_id` și `sequence`.
- `stock.picking.type`: opțiunile `Avoid Putaway Rules` și `Avoid Root Location on Reservation`.
- `stock.move`, `stock.move.line`, `stock.quant`: logica de împărțire a liniilor la capacitate maximă și excluderea locației-rădăcină la rezervare (cheia de context `exclude_location_ids`, consumată în `stock.quant._get_gather_domain`).

**Vizualizări**

- `views/stock_location_views.xml`: capacitatea pe locație.
- `views/stock_picking_type_views.xml`: opțiunile de putaway pe tipul de operație.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau server.

#### 5. Conexiuni

- [deltatech_warehouse_map](../deltatech_warehouse_map/index.md): poate afișa indicatorii de capacitate și ocupare pe harta vizuală a depozitului.
- [deltatech_stock_removal_priority](../deltatech_stock_removal_priority/index.md): modul complementar pentru prioritizarea locațiilor la rezervare; nu mai este necesar pentru opțiunea `Avoid Root Location on Reservation`.
