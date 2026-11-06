# Sale Team Access Control (localizat la `deltatech_sale_team/index.md`)

- **Nume Tehnic:** `deltatech_sale_team`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_team
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_team`
- **Ultima Ingestie:** `2026-11-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul restricționează accesul utilizatorilor la documentele asociate echipei de vânzări din care fac parte. Un agent de vânzări vede doar propriile documente, în timp ce un șef de echipă obține un grup dedicat (Team Manager) ce îi oferă vizibilitate asupra tuturor documentelor echipei sale. Suplimentar, modulul permite asocierea unui depozit implicit fiecărei echipe, astfel încât comenzile de vânzare preiau automat depozitul echipei selectate.

#### 2. Funcționalități Cheie

- Restricționarea accesului la documentele de vânzare (comenzi, linii de comandă, analiza vânzărilor) la echipa de vânzări a utilizatorului, plus documentele fără echipă.
- Restricționarea accesului la facturi (`account.move`): agentul vede doar facturile proprii, șeful de echipă pe cele ale echipei, iar utilizatorii cu **Vânzări: Utilizator: Toate documentele** le văd pe toate.
- Grup de securitate nou **Team Manager**, care include drepturile de agent de vânzări; grupul **Toate documentele** îl include automat. Nu are categorie proprie în formularul utilizatorului (se atribuie din **Grupuri**, cu modul dezvoltator activ).
- Un șef de echipă vede doar propria echipă în lista echipelor de vânzări.
- Partenerii: agenții de vânzări văd partenerii proprii (cei urmăriți de ei, cu ei ca responsabil sau fără responsabil), iar managerii de vânzări pe cei care nu sunt de tip privat.
- Setarea unui depozit implicit (**Default Warehouse**) la nivel de echipă de vânzări, în formularul echipei.
- Preluarea automată a depozitului echipei pe comanda de vânzare la schimbarea echipei.
- Tip de echipă (`Team Type`: Sales / Website), vizibil doar în modul dezvoltator, pentru diferențierea resurselor folosite de echipă.
- La atribuire manuală: alocarea membrilor pe echipe și a grupului **Team Manager** rămân în sarcina administratorului.

#### 3. Dependențe

- `sales_team`
- `account`
- `stock`
- `sale_stock`

#### 4. Componente Cheie

Modulul are `readme/DESCRIPTION.md` minimal, care nu detaliază componentele; ele sunt descrise după codul modulului.

**Modele**

- `crm.team` (extins): adaugă câmpurile `team_type` (Sales/Website) și `warehouse_id` (depozit implicit), plus metodele `show_validated_quotations`, `action_sale_order_button` și `show_products` (produse disponibile în depozitul echipei).
- `sale.order` (extins): la modificarea echipei (`team_id`), setează automat `warehouse_id` cu depozitul implicit al echipei.

**Vizualizări**

- `crm_team_view_form`: extinde formularul echipei de vânzări cu câmpul `warehouse_id` și, în modul dezvoltator, `team_type`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

Regulile de acces sunt implementate prin grupul `group_sale_team_manager` și reguli de înregistrare (`ir.rule`) din `security/sales_team_security.xml`:

- `sale_order_team_rule`, `sale_order_line_team_rule`, `sale_order_report_team_rule`: limitează comenzile, liniile și analizele la echipa utilizatorului sau fără echipă.
- `account_invoice_team_rule`, `account_invoice_personal_rule`, `account_invoice_see_all`: acces la facturi pe echipă / personal / toate.
- `sales_team_team_rule`: limitează vizualizarea echipelor la cea proprie.
- `res_partner_personal_rule`, `res_partner_manager_rule`: acces la parteneri pentru agenți, respectiv manageri de vânzări.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module documentate în wiki.
