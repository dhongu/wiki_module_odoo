# Deltatech Product Secondary UoM (localizat la `deltatech_secondary_uom/index.md`)

- **Nume Tehnic:** `deltatech_secondary_uom`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_secondary_uom
- **Cale Locală:** `odoo-addons/deltatech/deltatech_secondary_uom`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul adaugă factori de conversie între unități de măsură definiți **per produs**, după modelul SAP MARM. În Odoo standard, factorul de conversie aparține unității de măsură în sine (ex: "1 cutie = 12 bucăți" e valabil global pentru toate produsele care folosesc acea unitate). Cu acest modul, factorul se definește direct pe fișa produsului, în tabul "Unități Alternative" (ex: „3 m² = 4 Bucăți” sau „1 kg = 2 Bucăți”), fără a fi nevoie de crearea unor unități de măsură dedicate per produs, ceea ce ține tabelul global de UoM curat și nu afectează rapoartele standard sau valorizarea stocului.

#### 2. Funcționalități Cheie

- Definirea, pe fiecare produs, a uneia sau mai multor conversii cantitate-alternativă ↔ cantitate-bază (ex: 3 m² = 4 bucăți, 1 kg = 2 bucăți).
- Stocul este ținut mereu în unitatea de bază a produsului; unitatea alternativă este doar un ajutor de introducere/afișare a cantității.
- Pe liniile de comandă de vânzare, liniile de comandă de achiziție și pe mutările de stoc, utilizatorul poate introduce cantitatea într-o unitate alternativă (kg, m² etc.), iar cantitatea liniei se calculează automat — și invers: modificarea cantității liniei actualizează cantitatea secundară.
- Prețul rămâne mereu în unitatea de bază: cantitatea secundară este doar informativă/de input și nu afectează niciodată prețul, facturarea sau valorizarea stocului.
- Rotunjirea cantității de bază la numărul întreg de bucăți atunci când se introduce cantitatea în unitatea alternativă (nu se pot livra fracțiuni de bucată).
- Propagarea unității secundare alese pe linia de vânzare/achiziție către mutarea de stoc generată (inclusiv la regulile de aprovizionare `stock.rule`) și păstrarea acesteia ca și criteriu distinct la comasarea mutărilor de stoc.

#### 3. Dependențe

- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `deltatech.product.uom.conversion`: model nou care ține conversia specifică unui produs între o unitate alternativă (`uom_id`, cu cantitatea `uom_qty`) și unitatea de bază a produsului (`base_qty`); calculează factorul de conversie și validează unicitatea per produs/unitate, cantitățile strict pozitive și faptul că unitatea alternativă diferă de unitatea de bază.
- `deltatech.secondary.uom.mixin`: model abstract reutilizabil care adaugă câmpurile `secondary_uom_id` și `secondary_uom_qty` (cu compute/inverse bidirecțional) pe modelele care îl moștenesc; expune hook-uri (`_get_secondary_product`, `_get_line_qty_and_uom`, `_set_line_qty`) pe care fiecare model concret trebuie să le implementeze.
- `product.template` (extins): adaugă câmpul `secondary_uom_ids` (Alternative Units) și metoda de căutare a conversiei pentru o unitate dată.
- `sale.order.line` (extins cu mixin-ul): permite alegerea unei unități secundare și a cantității secundare pe linia de vânzare, propagate mai departe la aprovizionare (`_prepare_procurement_values`).
- `purchase.order.line` (extins cu mixin-ul): permite alegerea unei unități secundare și a cantității secundare pe linia de achiziție, propagate la mutarea de stoc generată (`_prepare_stock_move_vals`).
- `stock.move` (extins cu mixin-ul): permite alegerea unei unități secundare și a cantității secundare pe mutarea de stoc; unitatea secundară este inclusă între câmpurile care disting mutările la comasare (`_prepare_merge_moves_distinct_fields`).
- `stock.rule` (extins): propagă `secondary_uom_id` din valorile de procurare către mutarea de stoc creată.

**Vizualizări**

- `product_template_views.xml`: adaugă tabul "Unități Alternative" pe fișa produsului, unde se editează lista de conversii `deltatech.product.uom.conversion`.
- `sale_order_views.xml`: adaugă câmpurile de unitate și cantitate secundară pe liniile comenzii de vânzare.
- `purchase_order_views.xml`: adaugă câmpurile de unitate și cantitate secundară pe liniile comenzii de achiziție.
- `stock_picking_views.xml`: adaugă câmpurile de unitate și cantitate secundară pe liniile de transfer de stoc.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `sale_stock`: sursa liniilor de comandă de vânzare și a procurării de stoc pe care modulul le extinde cu unitatea secundară.
- `purchase_stock`: sursa liniilor de comandă de achiziție și a mutărilor de stoc generate din achiziție pe care modulul le extinde cu unitatea secundară.
