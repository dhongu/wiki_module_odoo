# Invoice Pickings (localizat la `deltatech_invoice_picking/index.md`)

- **Nume Tehnic:** `deltatech_invoice_picking`
- **Versiune:** `19.0.1.0.16`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_picking
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_picking`
- **Ultima Ingestie:** `2026-10-26`

#### 1. Sumar

Acest modul permite generarea facturilor direct din livrări (pickings), oferind o alternativă la facturarea pornind de la comanda de vânzare sau de achiziție. Pe factură sunt preluate doar produsele din livrare împreună cu cantitățile efectiv realizate (done), ceea ce asigură o corelare exactă între ce s-a livrat și ce se facturează. Modulul aduce valoare în special în fluxurile unde cantitatea livrată poate diferi de cea comandată, simplificând munca echipelor de logistică și facturare.

#### 2. Funcționalități Cheie

- O factură poate fi creată dintr-una sau mai multe livrări (acțiuni server „Create Sale Invoices" și „Create Purchase Invoices" pe transferuri, plus butoane „Invoice"/„Bill" în formularul livrării).
- O factură poate fi creată dintr-un lot de livrări (batch), cu buton „Invoice" în formularul lotului.
- Pe factură sunt adăugate doar produsele din livrare, cu cantitățile lor realizate (done).
- Pot fi facturate doar livrările care provin dintr-o comandă de vânzare sau de achiziție.
- O livrare trebuie să fie în starea „done" pentru a putea fi facturată.
- Pe livrări este adăugat un câmp „to invoice", util pentru filtrare (filtrul „To invoice" în căutare): este setat pe True la crearea unei livrări de vânzare, devine False la crearea facturii și revine la True dacă factura este anulată sau ștearsă.
- Pe livrări este adăugat un câmp cu legătură către factură, calculat pentru a indica factura generată din livrarea respectivă.
- **Dacă se fac modificări asupra facturii (linii șterse, cantități modificate), câmpurile facturii din livrările asociate nu vor fi actualizate.**

#### 3. Dependențe

- `account`
- `sale_management`
- `stock`
- `sale_stock`
- `stock_picking_batch`
- `purchase`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): câmpul „to invoice" și legătura către factură; metodele `action_create_invoice` și `action_create_supplier_invoice`; `button_validate` suprascris.
- `stock.picking.batch` (extins): `action_create_invoice` pentru facturarea unui lot de livrări.
- `account.move` și `account.move.line` (extinse): actualizarea livrărilor legate (`update_pickings`) la crearea, anularea, resetarea la ciornă sau ștergerea facturii.
- `sale.order` și `sale.order.line` (extinse) și `purchase.order.line` (extins): legătura cu cantitățile livrate/facturate.
- `sale.advance.payment.inv` (extins, `wizard/sale_make_invoice_advance.py`): adaptarea wizardului de facturare a comenzii de vânzare.

**Vizualizări**

- `views/stock_view.xml`: butoanele de facturare pe formularul livrării (`view_picking_form`) și al lotului (`view_batch_form_invoice`), filtrul „To invoice" (`view_picking_internal_search_inherit_invoice_picking`) și lista de transferuri (`stock_tree_invoice`).
- `views/sale_view.xml` (`view_order_form`): extinderi pe comanda de vânzare.
- `views/account_move.xml` (`view_account_move_from_picking_form`): extinderi pe formularul facturii.

**Acțiuni Automate / Acțiuni Server**

- `action_picking_invoice` („Create Sale Invoices") și `action_picking_supplier_invoice` („Create Purchase Invoices"): acțiuni server pe transferuri, pentru facturarea în masă. Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_invoice_picking_automatically](../deltatech_invoice_picking_automatically/index.md): automatizează crearea facturilor din transferuri de stoc.
- [deltatech_stock_delivery](../deltatech_stock_delivery/index.md): butoane Livrare/Recepție în factură, pentru a ajunge din factură la transferurile asociate.
- [deltatech_invoice_receipt](../deltatech_invoice_receipt/index.md): creează recepția pornind de la factură, fluxul invers.
