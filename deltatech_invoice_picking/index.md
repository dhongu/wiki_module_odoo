# Invoice Pickings (localizat la `deltatech_invoice_picking/index.md`)

- **Nume Tehnic:** `deltatech_invoice_picking`
- **Versiune:** `20.0.1.0.18`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_picking
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_picking`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite crearea facturilor direct din transferurile de stoc (livrări, recepții, retururi) sau din loturi de transferuri. Pe factură ajung doar produsele din transferurile alese, cu cantitățile efectiv livrate sau recepționate, astfel încât documentul fiscal rămâne aliniat cu mișcarea reală a stocului.

#### 2. Funcționalități Cheie

- Factură creată dintr-unul sau mai multe transferuri, sau dintr-un lot de transferuri (butonul **Invoice** pe lot).
- Pe factură intră doar produsele din transferuri, cu cantitățile efectuate; se pot factura doar transferuri provenite dintr-o comandă de vânzare sau de achiziție, aflate în starea „efectuat".
- Câmpul **To invoice** pe transfer (filtru): se bifează la validarea transferului și se debifează la crearea facturii; la anularea sau ștergerea facturii se bifează la loc și legătura se șterge. Un transfer parțial facturat rămâne *To invoice*, pentru facturarea restului.
- Câmp cu legătura către factura generată din transfer (fila *Additional Info*).
- Pe o factură creată din transferuri, cantitatea sau produsul liniilor de produs stocabil nu pot fi modificate, iar liniile nu pot fi șterse.
- Facturare livrări: *Inventory → Operations → Transfers → Deliveries*, filtrul **To invoice**, acțiunea **Create Sale Invoices** (pe selecție) sau butonul **Invoice** pe livrare; asistentul standard **Create invoice(s)**.
- Facturare recepții: se completează **Supplier Invoice No** și se apasă **Bill** (sau **Create Purchase Invoices** din listă); factura de furnizor se creează în ciornă, iar numărul se copiază ca **Vendor Reference** pe comanda de achiziție.
- Retur: un retur validat al unei livrări facturate este *To invoice*; butonul **Invoice** creează nota de credit cu cantitatea returnată și o leagă de retur.
- **Force Invoice Order** pe comanda de vânzare (fila *Other Info*): liniile se facturează pe cantitățile comandate, indiferent de politica de facturare a produsului.

Fluxul pas-cu-pas, cu capturi, se găsește în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `sale_management`
- `stock`
- `sale_stock`
- `purchase`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): câmpurile *To invoice* și factura generată, acțiunile de facturare.
- `stock.picking.batch` (extins): facturarea unui lot de transferuri.
- `account.move` / `account.move.line` (extinse): legătura cu transferul și blocarea modificării liniilor de produs stocabil.
- `sale.order` / `sale.order.line` (extinse): *Force Invoice Order* și cantitatea facturată pe linie.
- `purchase.order.line` (extins): cantitatea facturată pentru facturarea recepțiilor.
- `sale.advance.payment.inv` (extins): asistentul standard de facturare, adaptat pentru facturarea din transferuri.

**Vizualizări**

- `view_picking_form`: butoanele Invoice / Bill și legătura către factură pe transfer.
- `stock_tree_invoice`: lista transferurilor cu starea de facturare.
- `view_picking_internal_search_inherit_invoice_picking`: filtrul **To invoice**.
- `view_batch_form_invoice`: butonul Invoice pe lotul de transferuri.
- `view_order_form`: câmpul Force Invoice Order pe comanda de vânzare.
- `view_account_move_from_picking_form`: factura creată din transferuri.

**Acțiuni Automate / Acțiuni Server**

- `action_picking_invoice` (*Create Sale Invoices*): acțiune server pe selecția de livrări.
- `action_picking_supplier_invoice` (*Create Purchase Invoices*): acțiune server pe selecția de recepții.

#### 5. Conexiuni

- [deltatech_invoice_picking_automatically](../deltatech_invoice_picking_automatically/index.md): automatizează facturarea transferurilor validate, peste fluxul manual din acest modul.
