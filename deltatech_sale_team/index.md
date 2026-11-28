# Sale Team Access Control (localizat la `deltatech_sale_team/index.md`)

- **Nume Tehnic:** `deltatech_sale_team`
- **Versiune:** `20.0.1.0.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_team`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_team`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Companiile organizate pe magazine, sucursale sau canale vor, de regulă, ca fiecare echipă de vânzări să lucreze doar pe documentele ei și să livreze din propriul depozit. Modulul adaugă un nivel de acces „Team Manager” și un depozit implicit pentru fiecare echipă de vânzări, astfel încât agenții văd doar ce le aparține, iar șefii de echipă văd documentele întregii echipe.

#### 2. Funcționalități Cheie

- Grupul „Team Manager”: include grupul de agent de vânzări (`sales_team.group_sale_salesman`) și este inclus în `sales_team.group_sale_salesman_all_leads`. Membrii lui văd ofertele, comenzile, liniile de comandă, analiza vânzărilor și facturile propriei echipe, plus pe cele fără echipă; regula pe facturi este doar de citire.
- Echipă proprie: membrii „Team Manager” fără `sales_team.group_sale_salesman_all_leads` văd în lista echipelor de vânzări doar echipa lor.
- Facturi și contacte personale: utilizatorii grupului de agent văd doar facturile la care sunt vânzători sau la care nu e setat niciunul; cei din `sales_team.group_sale_salesman_all_leads` văd toate facturile. Agenții din afara `sales_team.group_sale_manager` văd doar contactele care le sunt atribuite, neatribuite sau proprii.
- Depozit implicit pe echipă: formularul echipei are câmpul „Default Warehouse”; la alegerea echipei pe o ofertă în formular, comanda preia depozitul echipei, dacă există.
- Limitări: depozitul echipei nu se aplică pe comenzile create prin import sau API; regulile de grup se cumulează, deci o regulă mai largă a altui grup al aceluiași utilizator rămâne valabilă.
- Fluxul pas-cu-pas (configurare echipă, agent, șef de echipă) este în fișa consultantului.

#### 3. Dependențe

- `sales_team`
- `account`
- `stock`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `crm.team` (extins): adaugă `team_type` (Sales/Website), `warehouse_id` (depozit implicit) și metode pentru afișarea ofertelor validate și a produselor din depozitul echipei.
- `sale.order` (extins): la schimbarea echipei (`team_id`), setează `warehouse_id` cu depozitul implicit al echipei.

**Vizualizări**

- `crm_team_view_form`: extinde formularul echipei cu `warehouse_id` și, doar în mod developer, cu `team_type`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

Accesul este implementat prin grupul `group_sale_team_manager` (`security/sales_team_security.xml`) și prin înregistrările `ir.access` din `security/ir.access.csv`: `sale_order_team_rule`, `sale_order_line_team_rule`, `sale_order_report_team_rule`, `account_invoice_team_rule`, `account_invoice_personal_rule`, `account_invoice_see_all`, `sales_team_team_rule` și `res_partner_personal_rule`.

#### 5. Conexiuni

- Nu au fost identificate module cu pagină wiki existentă legate funcțional de acest modul.
