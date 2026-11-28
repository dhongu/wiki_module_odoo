# Invoice Delivery / Reception (localizat la `deltatech_stock_delivery/index.md`)

- **Nume Tehnic:** `deltatech_stock_delivery`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_delivery
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_delivery`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă acces rapid, direct din factură, la operațiunile de depozit asociate. Adaugă în formularul facturii un buton „Delivery” sau „Reception”, după tipul documentului, astfel că contabilii și gestionarii de depozit verifică ușor livrările fizice față de documentele financiare.

#### 2. Funcționalități Cheie

- Buton „Delivery” pe factura client sau „Reception” pe factura furnizor.
- Deschide lista transferurilor de stoc legate de comenzile de vânzare/cumpărare ale facturii.
- Îmbunătățește trasabilitatea și reduce timpul de căutare a documentelor conexe.

#### 3. Dependențe

- `account`
- `stock`
- `purchase`
- `sale`
- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): acțiunea butonului către transferurile asociate.

**Vizualizări**

- `invoice_view_form_saleorder_button`: butonul de acces rapid în formularul facturii (`views/account_invoice_view.xml`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): leagă facturile de transferurile de stoc.
- [deltatech_invoice_picking_automatically](../deltatech_invoice_picking_automatically/index.md): automatizează crearea facturilor din transferuri de stoc.
- [deltatech_invoice_receipt](../deltatech_invoice_receipt/index.md): creează recepția pornind de la factură.
- [deltatech_account](../deltatech_account/index.md): grupul de butoane din factură (dependență opțională, comentată în manifest).
