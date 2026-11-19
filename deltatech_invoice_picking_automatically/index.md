# Auto-Invoice from Delivery (localizat la `deltatech_invoice_picking_automatically/index.md`)

- **Nume Tehnic:** `deltatech_invoice_picking_automatically`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_picking_automatically
- **Cale Locală:** odoo-addons/deltatech/deltatech_invoice_picking_automatically
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul facturează automat transferurile de stoc validate, fiecare transfer pe documentul lui și cu cantitățile pe care le-a mișcat: livrarea devine factură de client, returul de la client devine notă de credit, recepția devine factură de furnizor (lăsată mereu în ciornă, până sosește documentul furnizorului), iar returul către furnizor devine storno de furnizor. Comportamentul se configurează pe tipul de operațiune de stoc, iar facturarea se face fie imediat după validare, fie de o acțiune planificată zilnică. Valoarea pentru afacere: fluidizarea ciclului comandă → livrare → factură și eliminarea riscului ca o livrare să rămână nefacturată.

#### 2. Funcționalități Cheie

- Configurare pe tipul de operațiune: **Create Invoice Automatically**, **Invoice Moment** și **Post Invoice Automatically** (meniu: Inventar → Configurare → Tipuri de operațiuni).
- **Invoice Moment**: *Scheduled* (implicit, acțiunea planificată zilnică facturează transferurile aflate la coadă) sau *On validation* (transferul e facturat imediat după validare).
- Facturile de client și notele de credit se postează automat dacă este bifat **Post Invoice Automatically**; facturile și storno-urile de furnizor rămân mereu în ciornă.
- Backorder-urile și livrările parțiale se facturează separat, cu cantitățile fiecărui transfer; un transfer deja facturat nu se mai facturează a doua oară.
- Intră la coadă doar transferurile provenite dintr-o comandă de vânzare sau de achiziție.
- Facturarea rulează cu drepturi de sistem, deci un utilizator de depozit fără drepturi de facturare poate valida transferuri pe tipuri de operațiune care facturează la validare.
- Tratarea erorilor: fiecare transfer e facturat într-un savepoint propriu; la eșec, transferul rămâne finalizat, este marcat **Failed** și păstrează motivul, afișat pe transfer. Butonul **Retry Invoicing** reîncearcă facturarea după remedierea cauzei.
- Starea **Automatic Invoicing** pe formularul transferului și ca coloană opțională în listă, plus filtrele **Automatic Invoicing Failed** și **To Invoice Automatically**.

#### 3. Dependențe

- `stock_account`
- `sale_stock`
- `sale`
- `stock`
- `account`
- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking.type` (extins): câmpurile `create_invoice_automatically`, `post_invoice_automatically` și `invoice_moment` (Scheduled / On validation).
- `stock.picking` (extins): câmpurile `invoice_state` (To Invoice / Invoiced / Failed) și `invoice_error`; metodele `_run_auto_invoicing`, `_auto_invoice_picking` și `action_retry_auto_invoice`.

**Vizualizări**

- `view_picking_type_form`: opțiunile de facturare automată pe tipul de operațiune.
- `view_picking_form`: starea facturării automate, motivul eșecului și butonul **Retry Invoicing** pe transfer.
- `vpicktree`: coloana opțională **Automatic Invoicing** în lista transferurilor.
- `view_picking_internal_search`: filtrele **Automatic Invoicing Failed** și **To Invoice Automatically**.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_generate_invoices` (Generate Invoices from Pickings): acțiune planificată zilnică, apelează `_cron_generate_invoices()` și facturează (până la 100 de transferuri pe rulare) transferurile aflate în starea **To Invoice**.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): oferă mecanismul de facturare din transferuri (și este dependență directă); acest modul adaugă automatizarea (configurare pe tip de operațiune și cron) peste el.
