# Lot Generation & Selection (localizat la `deltatech_lot/index.md`)

- **Nume Tehnic:** `deltatech_lot`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_lot
- **Cale Locală:** `odoo-addons/deltatech/deltatech_lot`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează automat numerele de lot la recepțiile de la furnizor și arată unde este depozitat fiecare lot. Elimină introducerea manuală a codului de lot pentru produsele urmărite pe loturi și păstrează o evidență clară a locației lor.

#### 2. Funcționalități Cheie

- La validarea unei recepții de la furnizor (sau dropship), fiecare linie a unui produs urmărit pe loturi, fără număr de lot, primește următorul număr din secvența **Serial Numbers**, câte un lot pe linie; loturile introduse de utilizator se păstrează.
- Câmpul **Location** al lotului arată locația care deține tot stocul lotului (gol dacă lotul este împărțit pe mai multe locații), în formular și ca coloană în lista de loturi.
- Loturile pot fi căutate după **Location**.
- Generarea se face doar la recepții și dropship, doar pentru loturi (nu serii) și mereu din secvența generală, nu din prefixul personalizat al produsului. Pașii detaliați sunt în fișa consultant.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.lot` (extins): câmpul `location_id`, calculat din cantitățile (`quant_ids`) lotului.
- `stock.move.line` (extins): `_default_lot_name()` generează numele lotului la recepții; `onchange_location_id()` restrânge loturile selectabile la locația aleasă.
- `stock.picking` (extins): `button_validate()` completează numele de lot lipsă pe liniile recepțiilor.

**Vizualizări**

- `view_stock_move_line_operation_tree`: context pe `lot_id` pentru filtrarea loturilor propuse.
- `view_production_lot_form`, `view_production_lot_tree`, `search_product_lot_filter`: adaugă locația în formular, listă și căutare.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server`; generarea este sincronă, la validare.

#### 5. Conexiuni

Nu au fost identificate module cu pagină wiki conectate funcțional, în afara dependenței `stock`.
