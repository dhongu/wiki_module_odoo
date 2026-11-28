# Warehouse Arrangement (localizat la `deltatech_warehouse_arrangement/index.md`)

- **Nume Tehnic:** `deltatech_warehouse_arrangement`
- **Versiune:** `20.0.0.1.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_warehouse_arrangement`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warehouse_arrangement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține aranjarea fizică a depozitului în paralel cu locațiile standard de stoc din Odoo, pe cinci niveluri: magazie, zonă, raft, secțiune și poliță (rack). Marfa se găsește astfel pe polița corectă, fără a crea câte o locație de stoc Odoo pentru fiecare poliță. Aranjarea este doar informativă: nu modifică locațiile de stoc, cantitățile sau evaluarea stocului.

#### 2. Funcționalități Cheie

- Ierarhie Magazie → Zonă → Raft → Secțiune → Poliță (meniul *Inventar > Locații*), fiecare nivel afișând calea completă; magazia se leagă de locația principală de stoc Odoo.
- Cod de bare pe poliță și etichete tipăribile pentru polițe (cod Code128 și calea completă).
- Aranjare implicită pe produs (tab *Locații*); fiecare lot / număr de serie își păstrează propria aranjare.
- Un lot nou preia aranjarea produsului; un lot recepționat în locația principală a magaziei o preia din nou, iar aranjarea se golește când lotul se epuizează în acea locație.
- Coloane, câmpuri de căutare și grupări după aranjare în lista de stoc (*Inventar > Raportare > Locații*).
- Ecran cu scanare pentru lot și noua poliță (*Inventar > Operațiuni > Ajustări > Schimbare lot*).
- Doar grupul *Manager locații depozit* poate crea sau modifica ierarhia; ceilalți utilizatori interni o pot citi.
- Fluxul pas cu pas este descris în fișa consultantului.

#### 3. Dependențe

- `stock`
- `barcodes`

#### 4. Componente Cheie

> Notă: `readme/DESCRIPTION.md` acoperă doar Sumarul și Funcționalitățile; componentele de mai jos au fost sintetizate din cod și manifest.

**Modele**

- `warehouse.location.storehouse`: Nivelul superior al ierarhiei de amplasamente; legat de o `stock.location` (locația-master a depozitului).
- `warehouse.location.zone`: Zonă în cadrul unei magazii.
- `warehouse.location.shelf`: Raft în cadrul unei zone.
- `warehouse.location.section`: Secțiune în cadrul unui raft.
- `warehouse.location.rack`: Grila (nivelul cel mai fin), cu câmp `barcode` folosit la relocarea prin scanare.
- `product.template` (extins): Adaugă câmpurile de amplasament implicit (`loc_storehouse_id`, `loc_zone_id`, `loc_shelf_id`, `loc_section_id`, `loc_rack_id`).
- `stock.lot` (extins): Stochează amplasamentul efectiv al lotului/seriei; le moștenește de la produs la creare și are metoda `check_if_depleted` care golește amplasamentul când stocul ajunge la zero.
- `stock.quant` (extins): Câmpuri `related` stocate (`loc_*_id`) pentru afișarea și filtrarea amplasamentului direct în vizualizarea de stoc.
- `stock.move.line` (extins): Suprascrie `_action_done` pentru a propaga amplasamentul la intrarea lotului în locația-master și a-l elibera la ieșire/epuizare.
- `lot.change.location` (TransientModel): Wizard de relocare a lotului bazat pe `barcodes.barcode_events_mixin` (scanare lot + grilă).

**Vizualizări**

- `view_storehouse_tree` / `view_storehouse_form`, `view_zone_tree` / `view_zone_form`, `view_shelf_tree` / `view_shelf_form`, `view_section_tree` / `view_section_form`, `view_rack_tree` / `view_rack_form`: Interfețele de gestiune pentru fiecare nivel al ierarhiei de amplasamente.
- `product_template_form_view`: Adaugă câmpurile de amplasament pe fișa produsului.
- `view_production_lot_form`: Afișează amplasamentul pe fișa lotului/seriei.
- `view_stock_quant_tree_editable` / `quant_search_view`: Afișarea și filtrarea/gruparea amplasamentului în stoc.
- `view_lot_change_location_form`: Formularul wizardului de relocare prin scanare.
- `action_report_rack`: Raport tipăribil pentru grile (rack).
- Meniuri: `menu_locations` (rădăcină) cu `menu_zone`, `menu_shelf`, `menu_section`, `menu_rack`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. Automatizarea amplasamentelor este realizată prin suprascrierea metodei `_action_done` pe `stock.move.line` (la finalizarea mișcărilor de stoc) și prin `create` pe `stock.lot`.

#### 5. Conexiuni

- [deltatech_warehouse_map](../deltatech_warehouse_map/index.md): hartă vizuală a locațiilor de depozit, complementară organizării fizice.
