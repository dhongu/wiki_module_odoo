# Deltatech Warehouse Arrangement (localizat la `deltatech_warehouse_arrangement/index.md`)

- **Nume Tehnic:** `deltatech_warehouse_arrangement`
- **Versiune:** `19.0.0.1.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_warehouse_arrangement`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warehouse_arrangement`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul oferă un sistem propriu de organizare fizică a depozitului, în paralel cu locațiile standard din Odoo. Permite definirea unei ierarhii de amplasamente — magazie, zonă, raft, secțiune și grilă (rack) — și asocierea acestora la produse, loturi/numere de serie și cantitățile din stoc. Astfel, personalul de depozit poate ști rapid unde anume este așezat fizic un produs sau un lot, fără a modifica structura logistică standard a stocului.

#### 2. Funcționalități Cheie

- Gestionează amplasamentele de depozit în paralel cu locațiile standard Odoo, printr-o ierarhie pe cinci niveluri: Magazie (Storehouse) → Zonă (Zone) → Raft (Shelf) → Secțiune (Section) → Grilă (Rack).
- Asociază amplasamentul implicit la nivel de produs (pe fișa produsului), care este apoi propagat automat către loturi/numere de serie la crearea acestora.
- Actualizează automat amplasamentul lotului la recepție: când un lot/serie intră în locația-master a produsului, primește amplasamentul definit pe produs.
- Eliberează automat amplasamentul lotului la epuizare: când cantitatea lotului în locația-master ajunge la zero, câmpurile de amplasament sunt golite.
- Wizard de relocare prin scanare cod de bare: se scanează lotul/seria, apoi codul de bare al grilei (rack), iar amplasamentul lotului este reasignat.
- Vizualizează amplasamentul fizic direct în stoc (`stock.quant`), cu posibilitatea de filtrare/grupare după nivelurile ierarhiei.
- Raport tipăribil pentru grile (rack), util pentru etichetare.

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

- [deltatech_warehouse_map](../deltatech_warehouse_map/index.md): modul complementar pentru reprezentarea/harta amplasamentelor de depozit; folosește același concept de organizare fizică a locațiilor.
