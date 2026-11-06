# Warehouse Arrangement (localizat la `deltatech_warehouse_arrangement/index.md`)

- **Nume Tehnic:** `deltatech_warehouse_arrangement`
- **Versiune:** `19.0.0.1.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_warehouse_arrangement
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warehouse_arrangement`
- **Ultima Ingestie:** `2026-11-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența așezării fizice a mărfurilor în depozit, în paralel cu locațiile standard din Odoo, pe cinci niveluri: magazie, zonă, raft, secțiune și grilă (rack). Marfa este găsită pe grila potrivită fără a crea câte o locație de stoc Odoo pentru fiecare. Amplasamentul se asociază produselor și loturilor/numerelor de serie, iar personalul de depozit vede rapid unde se află fizic un lot, fără a modifica structura logistică standard a stocului.

#### 2. Funcționalități Cheie

- **Ierarhie pe cinci niveluri** — Magazie (Storehouse) → Zonă (Zone) → Raft (Shelf) → Secțiune (Section) → Grilă (Rack), în **Inventar → Locații** (în Odoo, meniul se numește *Locations*); fiecare nivel arată calea completă. Magazia se leagă de locația principală de stoc Odoo (de exemplu `WH/Stock`).
- **Cod de bare și etichete**: grila are cod de bare; etichetele tipăribile (Code128 și calea completă) se tipăresc din listă (**Print → Rack Labels**) sau din formularul grilei.
- **Amplasament implicit pe produs**, în fila **Locations** a produsului; fiecare lot/serie își păstrează propriul amplasament, preluat de la produs la creare (valorile date explicit pentru lot nu sunt înlocuite).
- **Actualizare la recepție**: un lot recepționat în locația principală a magaziei primește din nou amplasamentul produsului.
- **Eliberare la epuizare**: când cantitatea lotului din locația principală ajunge la zero, amplasamentul lotului se golește (doar pentru ieșiri din locația principală însăși, nu din sublocațiile ei).
- **Stoc pe amplasamente**: coloane, câmpuri de căutare și grupări după magazie/zonă/raft/secțiune/grilă în lista de stoc (**Inventar → Raportare → Locații**; vizibilă cu opțiunea de locații de stocare, cu consignația sau în modul dezvoltator; altfel, butonul **On Hand** al produsului deschide aceeași listă).
- **Relocare prin scanare**: ecranul **Inventar → Operațiuni → Ajustări → Change lot** — se scanează lotul, apoi grila nouă. Scanarea unui lot nou golește grila aleasă pentru lotul anterior; un nume de lot ambiguu dă eroare. Conform fișei, în Odoo 19 ecranul se deschide pe pagină întreagă, iar butoanele **Apply** / **Reset** nu se afișează, deci scanarea nu modifică lotul: până la remediere, grila se alege direct pe lot (fila **Locations**, câmpul **Rack Location**).
- **Drepturi**: doar grupul **Warehouse Locations manager** poate crea sau modifica ierarhia; ceilalți utilizatori interni o pot citi.
- Amplasamentul este doar informativ: nu schimbă locațiile de stoc Odoo, cantitățile sau evaluarea stocului.

#### 3. Dependențe

- `stock`
- `barcodes`

#### 4. Componente Cheie

> Notă: `readme/DESCRIPTION.md` și `readme/USAGE.md` acoperă funcționalitățile; componentele de mai jos au fost sintetizate din cod.

**Modele**

- `warehouse.location.storehouse`: Nivelul superior al ierarhiei; legat de o `stock.location` (locația principală a magaziei).
- `warehouse.location.zone`: Zonă în cadrul unei magazii.
- `warehouse.location.shelf`: Raft în cadrul unei zone.
- `warehouse.location.section`: Secțiune în cadrul unui raft.
- `warehouse.location.rack`: Grila (nivelul cel mai fin), cu câmp `barcode` folosit la relocarea prin scanare.
- `product.template` (extins): amplasamentul implicit (`loc_storehouse_id`, `loc_zone_id`, `loc_shelf_id`, `loc_section_id`, `loc_rack_id`).
- `stock.lot` (extins): amplasamentul efectiv al lotului/seriei, preluat de la produs la creare (`create`); metoda `check_if_depleted` golește amplasamentul când stocul ajunge la zero.
- `stock.quant` (extins): câmpuri `related` stocate (`loc_*_id`) pentru afișarea și filtrarea amplasamentului în stoc.
- `stock.move.line` (extins): `_action_done` propagă amplasamentul produsului la intrarea lotului în locația principală și îl eliberează la epuizare.
- `lot.change.location` (TransientModel): ecran de relocare a lotului, bazat pe `barcodes.barcode_events_mixin` (scanare lot + grilă; metodele `on_barcode_scanned`, `do_change`, `reset`).

**Vizualizări**

- `view_storehouse_tree` / `view_storehouse_form`, `view_zone_tree` / `view_zone_form`, `view_shelf_tree` / `view_shelf_form`, `view_section_tree` / `view_section_form`, `view_rack_tree` / `view_rack_form`: interfețele de gestiune pentru fiecare nivel.
- `product_template_form_view`: amplasamentul implicit pe fișa produsului.
- `view_production_lot_form`: amplasamentul pe fișa lotului/seriei.
- `view_stock_quant_tree_editable` / `quant_search_view`: afișarea și filtrarea/gruparea amplasamentului în stoc.
- `view_lot_change_location_form`: formularul ecranului de relocare prin scanare (meniul `menu_change_lot_location`, în **Ajustări**).
- `action_report_rack`: raport tipăribil cu etichetele grilelor.
- Meniuri: `menu_locations` (în **Inventar**) cu intrările magazie, `menu_zone`, `menu_shelf`, `menu_section`, `menu_rack`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. Automatizarea amplasamentelor este realizată prin suprascrierea `_action_done` pe `stock.move.line` și prin `create` pe `stock.lot`.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale verificate către alte module documentate în wiki. [deltatech_warehouse_map](../deltatech_warehouse_map/index.md) este o hartă a ocupării bazată pe locațiile standard `stock.location`, nu pe aceste amplasamente, deci nu depinde de acest modul.
