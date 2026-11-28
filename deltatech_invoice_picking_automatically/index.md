# Auto-Invoice from Delivery (localizat la `deltatech_invoice_picking_automatically/index.md`)

- **Nume Tehnic:** `deltatech_invoice_picking_automatically`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_picking_automatically
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_picking_automatically`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul facturează automat transferurile de stoc validate, fiecare pe propriul document și cu cantitățile mutate efectiv. Elimină munca manuală de facturare a livrărilor și recepțiilor și tratează separat erorile, fără să blocheze depozitul.

#### 2. Funcționalități Cheie

- Livrare → factură de client, postată automat dacă este bifat **Post Invoice Automatically**; retur de la client → notă de credit; recepție → factură de furnizor, mereu în ciornă; retur către furnizor → refund de furnizor, în ciornă.
- Configurare pe tipul de operațiune: **Create Invoice Automatically**, **Invoice Moment** și **Post Invoice Automatically**.
- **Invoice Moment**: *Scheduled* (implicit; acțiunea programată zilnică facturează transferurile aflate la coadă) sau *On validation* (transferul se facturează imediat după validare).
- Backorder-urile și livrările parțiale se facturează separat, cu cantitățile fiecărui transfer; un transfer deja facturat nu se mai facturează. Se pun la coadă doar transferurile provenite dintr-o comandă de vânzare sau de achiziție.
- Facturarea rulează cu drepturi de sistem, deci un utilizator de depozit fără drepturi de facturare poate valida transferuri care se facturează la validare.
- Tratarea erorilor: fiecare transfer se facturează într-un savepoint propriu; la eșec transferul rămâne efectuat, este marcat **Failed** și păstrează motivul, iar butonul **Retry Invoicing** reia facturarea după remedierea cauzei.
- Starea **Automatic Invoicing** pe formularul transferului și ca coloană opțională în listă, plus filtrele **Automatic Invoicing Failed** și **To Invoice Automatically**.

Fluxul pas-cu-pas se găsește în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md)
- `stock_account`
- `sale_stock`
- `sale`
- `stock`
- `account`

#### 4. Componente Cheie

**Modele**

- `stock.picking.type` (extins): opțiunile de facturare automată pe tipul de operațiune.
- `stock.picking` (extins): starea Automatic Invoicing, motivul eșecului, coada de facturare și butonul Retry Invoicing.

**Vizualizări**

- `view_picking_type_form`: opțiunile de facturare automată pe tipul de operațiune.
- `view_picking_form`: starea facturării automate, motivul eșecului și butonul Retry Invoicing.
- `vpicktree`: coloana opțională Automatic Invoicing în lista transferurilor.
- `view_picking_internal_search`: filtrele Automatic Invoicing Failed și To Invoice Automatically.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_generate_invoices` (*Generate Invoices from Pickings*): rulează zilnic și facturează transferurile aflate la coadă pe tipurile de operațiune cu momentul *Scheduled*.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): dependență funcțională; modulul adaugă automatizarea (configurare pe tip de operațiune și cron) peste facturarea manuală din transferuri.
