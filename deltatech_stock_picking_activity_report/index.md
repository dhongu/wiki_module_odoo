# Stock Picking Activity Report (localizat la `deltatech_stock_picking_activity_report/index.md`)

- **Nume Tehnic:** `deltatech_stock_picking_activity_report`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_picking_activity_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_picking_activity_report`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul ține evidența activității pe fiecare transfer de stoc (recepție, livrare sau transfer intern): înregistrează automat modificările de câmpuri, mesajele din chatter și evenimentele de validare, cu numărul de produse procesate. Managerii de depozit văd astfel cine a lucrat pe fiecare document și ce s-a schimbat. Înregistrările mai vechi de 2 luni se șterg automat prin Data Recycle.

#### 2. Funcționalități Cheie

- Înregistrează modificările detaliate pe transferuri, inclusiv schimbările de câmpuri și actualizările liniilor.
- Captează mesajele postate în chatter pentru un istoric complet.
- Urmărește evenimentele de validare și clasifică numărul de produse procesate (intrare, ieșire sau intern).
- Raport de activitate în `Inventar > Raportare` (meniul *Activity Records*), cu vizualizări listă, pivot și grafic, pentru analiză statistică.
- Șterge automat înregistrările mai vechi de 2 luni, prin regula Data Recycle livrată cu modulul.

#### 3. Dependențe

- `stock`
- `data_recycle`

#### 4. Componente Cheie

**Modele**

- `stock.picking.activity.record`: o înregistrare de activitate pe transfer (data, utilizator, stare, mesaje în chatter, validări, număr de produse intrate/ieșite/interne, jurnal de activitate).
- `stock.picking` (extins): generează înregistrările de activitate la modificări, mesaje și validare.

**Vizualizări**

- `view_stock_picking_activity_record_tree`, `_pivot`, `_graph`, `_form`, `_search`: interfețele raportului, deschise din meniul de raportare al Inventarului.

**Acțiuni Automate / Acțiuni Server**

- `data_recycle_model_stock_picking_activity`: regulă Data Recycle care șterge înregistrările de activitate mai vechi de 2 luni.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte module cu pagină wiki.
