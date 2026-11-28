# Stock Orderpoint Qty Multiple (localizat la `deltatech_stock_orderpoint_multiple/index.md`)

- **Nume Tehnic:** `deltatech_stock_orderpoint_multiple`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_orderpoint_multiple
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_orderpoint_multiple`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Odoo a eliminat în versiunea 19.0 câmpul „Multiplu cantitate” de pe regulile de aprovizionare, înlocuindu-l cu o unitate de reaprovizionare legată de produs sau de furnizor. Modulul readuce câmpul simplu din versiunile anterioare, fără unități de măsură suplimentare: cantitatea de comandat se rotunjește la un multiplu al valorii introduse direct pe regulă (de exemplu 100 buc/cutie).

#### 2. Funcționalități Cheie

- Câmpul `qty_multiple` pe regula de aprovizionare, vizibil în lista editabilă și în formular.
- Dacă multiplul este setat, cantitatea de comandat se rotunjește la un multiplu al lui; altfel rămâne comportamentul nativ (`replenishment_uom_id`).
- Rotunjirea urmează Odoo 18.0 și anterioare: în jos când există un plafon (`product_max_qty`), ca plafonul să nu fie depășit, în sus în rest.
- Abatere deliberată: niciodată până la zero. Când necesarul e mai mic decât multiplul se comandă un multiplu întreg, ca regula să nu fie dezactivată în tăcere.
- Fără dependențe de unități de măsură configurate per produs sau furnizor.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse.orderpoint`: extins cu `qty_multiple` și cu logica de rotunjire a cantității de comandat.

**Vizualizări**

- `view_warehouse_orderpoint_tree_editable_qty_multiple`: coloana „Multiplu” în lista editabilă a regulilor.
- `view_warehouse_orderpoint_form_qty_multiple`: câmpul în formularul regulii.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- Fără conexiuni funcționale directe verificate în cod.
