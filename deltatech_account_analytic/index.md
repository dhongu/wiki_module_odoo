# Account Analytic Split (localizat la `deltatech_account_analytic/index.md`)

- **Nume Tehnic:** `deltatech_account_analytic`
- **Versiune:** `19.0.0.0.11`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_account_analytic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_analytic`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

`deltatech_account_analytic` îmbunătățește contabilitatea analitică din Odoo cu două direcții complementare. Pe de o parte, leagă automat liniile analitice și distribuțiile analitice de pe facturi de **echipa de vânzări** și adaugă categoria produsului pe fiecare linie analitică, pentru rapoarte mai fine pe echipe și categorii. Pe de altă parte, oferă un asistent de **împărțire a sumelor pe mai multe conturi analitice**, pe baza unor șabloane procentuale reutilizabile — util atunci când o sumă (comision, cost partajat, alocare de marjă) trebuie distribuită după o cheie fixă, fără a calcula manual fiecare linie.

#### 2. Funcționalități Cheie

- **Echipă de vânzări pe distribuția analitică**: modelul de distribuție analitică primește câmpul *Sale team*. Pe facturile de client, notele de credit și chitanțele de vânzare, liniile de produs preiau distribuția modelului a cărui echipă este echipa facturii, dacă există exact un astfel de model; distribuția se recalculează și când se schimbă echipa facturii.
- **Echipă de vânzări pe liniile analitice** (`team_id`): se preia de pe factura de client, nota de credit sau chitanța de vânzare (`out_invoice`/`out_refund`/`out_receipt`); pentru notele contabile ale unui transfer de stoc (când sunt instalate modulele de stoc și `sale_stock`), de pe comanda de vânzare a transferului; pe facturile și notele de credit de furnizor, de la echipa al cărei nume este identic cu numele contului analitic.
- **Categorie de produs pe linia analitică** (`product_category_id`, related stocat din `product_id.categ_id`).
- **Grupări noi**: în *Contabilitate → Tranzacții → Analytic Items* și în *Raportare → Analytic Report*, meniul *Group By* oferă *Sale team* și *Product category*.
- **Șabloane de împărțire** (`account.analytic.split.template`): conturi analitice cu procent fiecare; procentele trebuie să însumeze 100.
- **Împărțiri analitice** (`account.analytic.split`): distribuie fie o *sumă* fixă, fie o linie analitică existentă (tip *Line*) după un șablon. *Compute* completează liniile din șablon; *Confirm* creează câte o linie analitică per linie de împărțire, la data împărțirii, și verifică totalul; la tipul *Line* linia originală este ștearsă și înlocuită; *Reset* șterge liniile create și readuce împărțirea de tip *Amount* în ciornă (o împărțire *Line* nu poate fi resetată). O împărțire fără *Name* nu poate fi confirmată.
- **Configurare**: *Sale team* se setează pe modelele de distribuție folosite la vânzări (*Contabilitate → Configurare → Contabilitate analitică → Analytic Distribution Models*); meniurile *Analytic split templates* și *Analytic splits* sunt vizibile administratorilor contabili când setarea *Analytic Accounting* este activă, iar accesul la ele îl au doar membrii grupului *Analitic split user*. În Community aplicația se numește *Invoicing*.
- **Limitare**: pe facturile de furnizor echipa e găsită doar prin potrivire exactă între numele contului analitic și numele echipei.

#### 3. Dependențe

- `account`
- `analytic`
- `sale`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `account.analytic.line` (extins): adaugă `product_category_id` (related, stocat) și `team_id`; la `create()`, deduce echipa din picking-ul de stoc legat sau din factura/nota de credit/chitanța de vânzare.
- `account.move.line` (extins): suprascrie `_compute_analytic_distribution` (dependență declarată pe `move_id.team_id`) pentru a aplica modelul de distribuție potrivit echipei facturii; suprascrie `_prepare_analytic_lines` pentru a determina `team_id` pe facturile de furnizor prin numele contului analitic.
- `account.analytic.distribution.model` (extins): adaugă `team_id` (echipă de vânzări), criteriu de selecție automată.
- `account.analytic.split.template` / `account.analytic.split.template.line`: șablon reutilizabil de împărțire procentuală (nume, activ/inactiv, linii cu procent).
- `account.analytic.split` / `account.analytic.split.line`: asistentul de împărțire — sumă sau linie sursă, tip (`amount`/`line`), stare (`draft`/`confirmed`), acțiuni de calcul (`action_prepare_lines`), confirmare (`action_create_analytic_lines`) și resetare (`action_reset_split`).

**Vizualizări**

- `view_account_analytic_default_form`: adaugă echipa de vânzări pe formularul modelului de distribuție analitică.
- `view_account_analytic_line_filter`: adaugă gruparea „Sale team" și „Product category" pe liniile analitice.
- `view_account_analytic_split_form` / `view_account_analytic_split_tree` + `action_analytic_split`: interfața împărțirilor, meniu „Analytic splits".
- `view_account_analytic_split_t_form` / `view_account_analytic_split_t_tree` + `action_analytic_split_template`: interfața șabloanelor, meniu „Analytic split templates".
- `res_config_settings.xml`: conține doar un view comentat integral; nicio opțiune activă în Setări.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate în cod către alte module cu pagină în acest wiki. Modulul folosește modelul `crm.team` (adus de `sale`) și extinde modele standard din `account`/`analytic`.
