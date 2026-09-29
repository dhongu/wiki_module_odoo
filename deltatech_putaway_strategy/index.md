# Deltatech Putaway Strategy (localizat la `deltatech_putaway_strategy/index.md`)

- **Nume Tehnic:** `deltatech_putaway_strategy`
- **Versiune:** `19.0.1.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_putaway_strategy`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_putaway_strategy`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Acest modul extinde locațiile din Inventarul Odoo cu o evidență simplă a capacității și îmbunătățește logica de decizie pentru depozitare (putaway). Practic, fiecărei locații i se poate seta o capacitate maximă, iar sistemul urmărește automat cât este ocupată și cât urmează să intre, astfel încât atunci când se sugerează unde să fie depozitate produsele, destinațiile pline să fie evitate, iar mărfurile să fie dirijate către locații libere. Modulul mai adaugă, la nivel de tip de operație, opțiuni pentru a sări peste regulile de putaway sau pentru a evita rezervarea automată a stocului care nu a fost încă depozitat pe raft (rămas în locația-rădăcină a depozitului) la livrări. Valoarea de afaceri constă într-o utilizare mai bună a spațiului de depozit, sugestii de amplasare mai inteligente la recepții și transferuri interne, și livrări care alocă preferențial marfa deja pusă la raft.

#### 2. Funcționalități Cheie

- Adaugă câmpuri de capacitate pe locațiile de stoc:
  - `Max products (leaf)`: capacitatea manuală pentru locațiile terminale (frunză).
  - `Max products`: capacitate calculată pentru orice locație (suma copiilor pentru locațiile non-terminale).
  - `Current quantity`: cantitatea calculată existentă în stoc pe locație.
  - `Planned quantity`: cantitatea calculată ce urmează să intre, pe baza mișcărilor în așteptare.
  - `Occupancy`: gradul de ocupare calculat ca raport `current/max` (limitat la intervalul [0, 1]).
- Calcul optimizat pentru ierarhii mari de locații: o singură citire grupată (`read_group`) pe `stock.quant` pentru toate locațiile terminale din lot, respectiv pe `stock.move.line` pentru cantitățile planificate, cu agregare în memorie de jos în sus pentru locațiile părinte.
- Putaway mai inteligent:
  - Respectă capacitatea locațiilor terminale când sugerează destinații.
  - Împarte automat liniile de mișcare dacă o locație de destinație atinge capacitatea maximă.
  - Preferă locațiile copil goale atunci când este posibil (dacă este activată căutarea în sublocații).
  - Opțional (parametru de sistem `deltatech_putaway_strategy.prefer_existing_stock_location`, dezactivat implicit; Setări → Tehnic → Parametri de sistem): preferă raftul pe care produsul este deja stocat, oriunde sub locația de intrare (ex. `D1/S`), în locul raftului dat de regula de putaway. Se propune raftul cu cea mai mare cantitate care mai are capacitate; regula se aplică normal dacă raftul ei conține deja produsul, dacă raftul preferat e plin, iar locația de intrare în sine este ignorată (marfă încă neamplasată). Acoperă produsele mutate fizic pe alt raft fără actualizarea regulii.
  - Un raft nu este niciodată propus ca destinație a mărfii care îl părăsește: se numără doar stocul liber (cantitate minus rezervat), iar locațiile sursă ale liniilor de mișcare sunt transmise putaway-ului prin cheia de context `putaway_exclude_location_ids`.
  - Căutare optimizată a regulilor de putaway prin indexuri de bază de date pe `product_id` și `sequence` pentru `stock.putaway.rule`.
  - Păstrează compatibilitatea completă cu regulile de categorie de stocare din Odoo (greutate maximă, capacități produs/pachet, reguli pentru produse noi etc.).
- Opțiuni noi pe tipul de operație (`stock.picking.type`):
  - `Avoid Putaway Rules`: sare peste redirecționarea prin reguli de putaway pentru acest tip de operație.
  - `Avoid Root Location on Reservation` (doar livrări): nu rezervă niciodată stocul aflat direct în locația sursă a operației — de regulă rădăcina depozitului (`lot_stock`, ex. `D1/S`). Astfel, marfa care nu a fost încă pusă la raft nu este alocată automat comenzilor de vânzare; sublocațiile (rafturile) rămân eligibile. Această opțiune necesită instalarea modulului `deltatech_stock_removal_priority` (vezi Compatibilitate).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

*Notă: secțiunea de mai jos reflectă componentele menționate explicit în `readme/DESCRIPTION.md`.*

**Modele**

- `stock.location`: extins cu câmpurile de capacitate (`Max products (leaf)`, `Max products`, `Current quantity`, `Planned quantity`, `Occupancy`) și cu logica de calcul optimizată al gradului de ocupare.
- `stock.putaway.rule`: optimizat prin indexuri de bază de date pe `product_id` și `sequence` pentru căutarea mai rapidă a regulilor.
- `stock.picking.type`: extins cu opțiunile `Avoid Putaway Rules` și `Avoid Root Location on Reservation`.

**Vizualizări**

- `views/stock_location_views.xml`: expune câmpurile de capacitate și ocupare pe locație.
- `views/stock_picking_type_views.xml`: opțiunile legate de strategia de putaway la nivel de tip de operație.

**Metode cheie (acoperite de teste)**

- `_check_can_be_used`: aplică limita de capacitate pe locațiile terminale.
- `_get_putaway_strategy`: preferința pentru raftul cu stoc existent (când parametrul e activ), preferința pentru locații copil goale și împărțirea automată a liniilor de mișcare la atingerea capacității.
- `exclude_location_ids`: cheie de context publicată de opțiunea `Avoid Root Location on Reservation`, citită de `stock.quant._get_gather_domain` (implementată în `deltatech_stock_removal_priority`) pentru a exclude locația-rădăcină la rezervare, doar pentru livrări.

#### 5. Conexiuni

- [deltatech_warehouse_map](../deltatech_warehouse_map/index.md): poate depinde de acest modul pentru a afișa indicatorii (KPI) de capacitate și ocupare pe harta vizuală a depozitului.
- [deltatech_stock_removal_priority](../deltatech_stock_removal_priority/index.md): nu este dependență strictă, dar opțiunea `Avoid Root Location on Reservation` nu are niciun efect decât dacă acest modul este instalat — el consumă cheia de context `exclude_location_ids` în `stock.quant._get_gather_domain`.
