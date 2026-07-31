# Sale order picking status (localizat la `deltatech_sale_picking_status/index.md`)

- **Nume Tehnic:** `deltatech_sale_picking_status`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_picking_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_picking_status`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă pe comanda de vânzare un indicator de stare a livrării (recepțiilor/expedițiilor), calculat automat pe baza stării transferurilor de stoc asociate. Astfel, echipa de vânzări poate vedea dintr-o privire, direct din lista sau formularul comenzii, dacă marfa a fost complet livrată sau dacă procesul de picking este încă în desfășurare, fără să mai deschidă fiecare transfer în parte.

#### 2. Funcționalități Cheie

- Adaugă un câmp de stare a livrării (`picking_status`) pe comanda de vânzare.
- Starea devine **Efectuat (Done)** atunci când toate transferurile (pickings) comenzii sunt în starea „Efectuat" sau „Anulat".
- Starea rămâne **În curs (In Progress)** dacă cel puțin un transfer nu este încă finalizat sau anulat.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): adaugă câmpul stocat `picking_status` (selecție Done/In Progress, cu urmărire/`tracking`) și metoda `_compute_picking_status()`, care determină starea în funcție de `state`-ul comenzii și de starea transferurilor din `picking_ids`.
- `stock.picking` (extindere): adaugă metoda `update_sale_order_status()` (declanșată `@api.onchange("state")`) care recalculează `picking_status` pe comanda de vânzare aferentă; este apelată explicit din `action_assign()`, `action_cancel()`, `action_confirm()` și `_action_done()` pentru a ține starea sincronizată la fiecare tranziție relevantă a transferului.

**Vizualizări**

- `view_quotation_tree_picking_status`: adaugă câmpul `picking_status` (widget `badge`) în lista de oferte, după `invoice_status`.
- `view_order_tree_picking_status`: adaugă `picking_status` (widget `badge`) în lista de comenzi de vânzare, după `invoice_status`.
- `view_order_form_picking_status`: adaugă `picking_status` (widget `badge`) în formularul comenzii, după `payment_term_id`.
- `view_sales_order_filter_picking_status`: adaugă filtrele „Done" și „In progress" în bara de căutare a comenzilor de vânzare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul; recalcularea stării se face prin suprascrierea metodelor de tranziție ale `stock.picking` (vezi Modele, mai sus).

#### 5. Conexiuni

- `sale_stock`: modulul standard Odoo pe care se bazează integrarea vânzări–stoc; `deltatech_sale_picking_status` extinde direct fluxul acestuia.
- `sale`: modulul de bază al comenzilor de vânzare, ale cărui vizualizări (listă ofertă, listă comandă, formular, filtru) sunt extinse.
- `stock`: modulul de gestiune stoc, ale cărui tranziții de transfer (`action_assign`, `action_confirm`, `action_cancel`, `_action_done`) declanșează recalcularea stării pe comanda de vânzare.
