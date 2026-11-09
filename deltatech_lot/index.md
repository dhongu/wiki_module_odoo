# Lot Generation & Selection (localizat la `deltatech_lot/index.md`)

- **Nume Tehnic:** `deltatech_lot`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_lot
- **Cale Locală:** `odoo-addons/deltatech/deltatech_lot`
- **Ultima Ingestie:** `2026-11-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează generarea numerelor de lot la recepția produselor de la furnizor și adaugă vizibilitate asupra locației de stoc unde se află fiecare lot. Este util companiilor care lucrează cu produse trasabile pe loturi (tracking pe lot) și vor să elimine introducerea manuală a codului de lot la fiecare recepție, păstrând în același timp o evidență clară a locației curente a fiecărui lot.

#### 2. Funcționalități Cheie

- **Loturi generate la validare:** la validarea unei recepții de la furnizor (sau a unui dropship), fiecare linie a unui produs urmărit pe loturi care nu are număr de lot primește următorul număr din secvența **Serial Numbers**, câte un lot pe linie; loturile tastate de utilizator se păstrează. Condiția: tipul de operațiune de recepție are bifat **Create New** în grupul **Lots/Serial Numbers** (implicit la recepții). Numerele se generează doar la recepții și dropship, doar pentru produse urmărite pe loturi (nu pe serii) și mereu din secvența generală, nu din prefixul personalizat al produsului.
- **Locația lotului:** câmpul **Location** arată locația care deține tot stocul lotului (gol dacă lotul e împărțit pe mai multe locații), în formularul lotului și ca coloană în lista de loturi; schimbarea lui mută stocul lotului când acesta e într-o singură locație (*Inventar > Produse > Loturi/Numere de serie*).
- **Căutare după locație:** lista de loturi se poate căuta după **Location**; sunt afișate doar loturile ținute integral în acea locație.
- Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.lot` (extins): câmpul calculat și stocat `location_id`, determinat din locația cantităților (`quant_ids`) cu stoc pozitiv asociate lotului; dacă lotul este prezent în mai multe locații simultan, câmpul rămâne gol.
- `stock.move.line` (extins): metoda `_default_lot_name()` generează automat numele lotului (din secvența `stock.lot.serial`) când produsul are tracking pe lot și operațiunea este de tip recepție (`incoming`); metoda `onchange_location_id()` restrânge domeniul loturilor selectabile la cele prezente în locația aleasă.
- `stock.picking` (extins): suprascrie `button_validate()` pentru a genera automat numele de lot pe liniile de mișcare ale operațiunilor de recepție (`incoming`, `dropship`) care folosesc loturi (creare sau selecție), dacă acesta lipsește.

**Vizualizări**

- `view_stock_move_line_operation_tree` (moștenește `stock.view_stock_move_line_operation_tree`): adaugă context dinamic pe câmpul `lot_id` (locație implicită de căutare, comandă activă, companie și produs impliciți) pentru a filtra corect loturile propuse la operațiunile de stoc.
- `view_production_lot_form` (moștenește `stock.view_production_lot_form`): adaugă câmpul `location_id` în formularul lotului.
- `view_production_lot_tree` (moștenește `stock.view_production_lot_tree`): adaugă coloana `location_id` în lista de loturi.
- `search_product_lot_filter` (moștenește `stock.search_product_lot_filter`): adaugă `location_id` ca opțiune de căutare/filtrare pe loturi.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; generarea numelui de lot are loc sincron, prin suprascrierea metodelor Python `_default_lot_name()` și `button_validate()` la recepția produselor.

#### 5. Conexiuni

Nu au fost identificate module Terrabit cu pagină wiki care depind funcțional de `deltatech_lot` sau de care acesta depinde, în afara dependenței directe `stock` (nucleu Odoo, fără pagină wiki proprie).
