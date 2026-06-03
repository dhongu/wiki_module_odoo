# Sale Team Access (localizat la `deltatech_sale_team/index.md`)

- **Nume Tehnic:** `deltatech_sale_team`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_team`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_team`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul restricționează accesul utilizatorilor la documentele asociate echipei de vânzări din care fac parte. Un agent de vânzări vede doar ofertele, comenzile și facturile propriei echipe, în timp ce un coordonator de echipă obține un grup dedicat ce îi oferă vizibilitate asupra tuturor documentelor echipei sale. Suplimentar, modulul permite asocierea unui depozit implicit fiecărei echipe, astfel încât comenzile de vânzare preiau automat depozitul echipei selectate.

#### 2. Funcționalități Cheie

- Restricționarea accesului la documentele de vânzare (oferte, comenzi, linii de comandă, analize vânzări) în funcție de echipa de vânzări a utilizatorului.
- Restricționarea accesului la facturi (`account.move`) pe baza echipei de vânzări.
- Grup de securitate nou „Team Manager", care oferă acces la documentele echipei din care face parte utilizatorul.
- Setarea unui depozit implicit (`Default Warehouse`) la nivel de echipă de vânzări.
- Preluarea automată a depozitului echipei pe comanda de vânzare la schimbarea echipei.
- Tip de echipă (`Team Type`: Sales / Website) pentru diferențierea resurselor folosite de echipă.

#### 3. Dependențe

- `sales_team`
- `account`
- `stock`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `crm.team` (extins): adaugă câmpul `team_type` (Sales/Website), câmpul `warehouse_id` (depozit implicit) și metode pentru afișarea ofertelor validate și a produselor disponibile în depozitul echipei.
- `sale.order` (extins): la modificarea echipei (`team_id`), setează automat `warehouse_id` cu depozitul implicit al echipei.

**Vizualizări**

- `crm_team_view_form`: extinde formularul echipei de vânzări pentru a afișa câmpul `warehouse_id` și (vizibil doar în mod developer) câmpul `team_type`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

Regulile de acces sunt implementate prin reguli de înregistrare (`ir.rule`) și un grup de securitate definite în `security/sales_team_security.xml`:

- `group_sale_team_manager`: grup „Team Manager", implică `sales_team.group_sale_salesman`.
- `sale_order_team_rule`, `sale_order_line_team_rule`, `sale_order_report_team_rule`: limitează comenzile, liniile și analizele la echipa utilizatorului.
- `account_invoice_team_rule`, `account_invoice_personal_rule`, `account_invoice_see_all`: control acces facturi pe echipă / personal / toate.
- `sales_team_team_rule`: limitează vizualizarea echipei proprii.

#### 5. Conexiuni

- Nu au fost identificate module cu pagină wiki existentă legate funcțional de acest modul.
