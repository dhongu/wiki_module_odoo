# Deltatech Putaway Strategy (localizat la `deltatech_putaway_strategy/index.md`)

- **Nume Tehnic:** `deltatech_putaway_strategy`
- **Versiune:** `19.0.1.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_putaway_strategy`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_putaway_strategy`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul extinde locațiile din Inventarul Odoo cu o evidență simplă a capacității și îmbunătățește logica de decizie pentru depozitare (putaway). Practic, fiecărei locații i se poate seta o capacitate maximă, iar sistemul urmărește automat cât este ocupată și cât urmează să intre, astfel încât atunci când se sugerează unde să fie depozitate produsele, destinațiile pline să fie evitate, iar mărfurile să fie dirijate către locații libere. Valoarea de afaceri constă într-o utilizare mai bună a spațiului de depozit și sugestii de amplasare mai inteligente la recepții și transferuri interne.

#### 2. Funcționalități Cheie

- Adaugă câmpuri de capacitate pe locațiile de stoc:
  - `Max products (leaf)`: capacitatea manuală pentru locațiile terminale (frunză).
  - `Max products`: capacitate calculată pentru orice locație (suma copiilor pentru locațiile non-terminale).
  - `Current quantity`: cantitatea calculată existentă în stoc pe locație.
  - `Planned quantity`: cantitatea calculată ce urmează să intre, pe baza mișcărilor în așteptare.
  - `Occupancy`: gradul de ocupare calculat ca raport `current/max` (limitat la intervalul [0, 1]).
- Calcul optimizat pentru ierarhii mari de locații (citire grupată unică pe `stock.quant` și `stock.move.line`, agregare în memorie de jos în sus pentru locațiile părinte).
- Putaway mai inteligent:
  - Respectă capacitatea locațiilor terminale când sugerează destinații.
  - Împarte automat liniile de mișcare dacă o locație de destinație atinge capacitatea maximă.
  - Preferă locațiile copil goale atunci când este posibil (dacă este activată căutarea în sublocații).
  - Căutare optimizată a regulilor de putaway prin indexuri de bază de date.
  - Păstrează compatibilitatea completă cu regulile de categorie de stocare din Odoo (greutate maximă, capacități produs/pachet, reguli pentru produse noi etc.).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

*Notă: secțiunea de mai jos reflectă componentele menționate explicit în `readme/DESCRIPTION.md`.*

**Modele**

- `stock.location`: extins cu câmpurile de capacitate (`Max products (leaf)`, `Max products`, `Current quantity`, `Planned quantity`, `Occupancy`) și cu logica de calcul optimizată al gradului de ocupare.
- `stock.putaway.rule`: optimizat prin indexuri de bază de date pe `product_id` și `sequence` pentru căutarea mai rapidă a regulilor.

**Vizualizări**

- `views/stock_location_views.xml`: expune câmpurile de capacitate și ocupare pe locație.
- `views/stock_picking_type_views.xml`: opțiuni legate de strategia de putaway la nivel de tip de operație.

**Metode cheie (acoperite de teste)**

- `_check_can_be_used`: aplică limita de capacitate pe locațiile terminale.
- `_get_putaway_strategy`: preferința pentru locații copil goale și împărțirea automată a liniilor de mișcare la atingerea capacității.

#### 5. Conexiuni

- [deltatech_warehouse_map](../deltatech_warehouse_map/index.md): poate depinde de acest modul pentru a afișa indicatorii (KPI) de capacitate și ocupare pe harta vizuală a depozitului.
