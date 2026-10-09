# Stock Orderpoint Qty Multiple (localizat la `deltatech_stock_orderpoint_multiple/index.md`)

- **Nume Tehnic:** `deltatech_stock_orderpoint_multiple`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_orderpoint_multiple
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_orderpoint_multiple`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Odoo 19 a eliminat câmpul „Cantitate multiplă" de pe regulile de aprovizionare (reordering rules), înlocuindu-l cu o unitate de măsură de reaprovizionare care trebuie configurată per produs sau furnizor. Acest modul readuce câmpul ca în Odoo 18 și anterior, astfel încât un multiplu simplu (de exemplu 100 buc/cutie) să poată fi completat direct pe regulă, fără nicio unitate de măsură suplimentară. Cantitatea de comandat se rotunjește automat la multiplul respectiv.

#### 2. Funcționalități Cheie

- Câmpul `Multiple Quantity` (`qty_multiple`) pe regula de aprovizionare, vizibil în formular și în lista editabilă (în listă este ascuns implicit, se activează din selectorul de coloane opționale), lângă „Replenishment UoM".
- Dacă `qty_multiple` este setat, cantitatea de comandat se rotunjește direct la un multiplu al acestei valori; dacă este 0, rămâne mecanismul nativ (`replenishment_uom_id`) sau nicio rotunjire.
- Sensul rotunjirii urmează Odoo <= 18.0: în jos când regula are cantitate maximă (`product_max_qty`), ca plafonul să nu fie depășit, în sus în rest.
- Abatere deliberată: rotunjirea nu ajunge niciodată la zero. Dacă necesarul este mai mic decât un multiplu, se comandă un multiplu întreg, pentru ca regula să nu devină inactivă în tăcere (depășirea plafonului e preferabilă unei reguli moarte).
- Valoarea nu poate fi negativă (constrângere SQL).
- Nu necesită configurarea de unități de măsură per produs/furnizor.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse.orderpoint` (extins): adaugă `qty_multiple` și suprascrie `_get_multiple_rounded_qty` pentru rotunjirea prin multiplu; fără multiplu apelează `super()`.

**Vizualizări**

- `view_warehouse_orderpoint_tree_editable_qty_multiple`: adaugă `qty_multiple` în lista editabilă a regulilor de aprovizionare (opțional, ascuns implicit).
- `view_warehouse_orderpoint_form_qty_multiple`: adaugă `qty_multiple` în formularul regulii.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_replenishment_explain](../deltatech_replenishment_explain/index.md): explicația reaprovizionării citește `qty_multiple` dacă acest modul este instalat (prin `getattr`).
- [deltatech_auto_reorder_rule](../deltatech_auto_reorder_rule/index.md): generează reguli de aprovizionare automate; același tip de model (`stock.warehouse.orderpoint`), fără dependență în manifest.
