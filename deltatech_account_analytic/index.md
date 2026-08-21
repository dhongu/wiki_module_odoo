# Deltatech Account Analytic (localizat la `deltatech_account_analytic/index.md`)

- **Nume Tehnic:** `deltatech_account_analytic`
- **Versiune:** `19.0.0.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_account_analytic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_analytic`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

`deltatech_account_analytic` îmbunătățește contabilitatea analitică din Odoo cu două direcții complementare. Pe de o parte, leagă automat liniile analitice și distribuțiile analitice de pe facturi de **echipa de vânzări** (client sau furnizor) și adaugă o categorie de produs pe fiecare linie analitică, pentru rapoarte mai fine pe echipe și categorii. Pe de altă parte, oferă un asistent de **împărțire manuală a sumelor pe mai multe conturi analitice**, pe baza unor șabloane procentuale reutilizabile — util atunci când o sumă (comision, cost partajat, alocare de marjă) trebuie distribuită după o cheie fixă, fără a mai calcula manual fiecare linie.

#### 2. Funcționalități Cheie

- **Echipă de vânzări pe liniile analitice** (`team_id` pe `account.analytic.line`): la creare, se determină automat din comanda de vânzare a expedierii (pentru notele contabile generate din stoc) sau direct din factura de vânzare, nota de credit **sau chitanța de vânzare** (`out_invoice`/`out_refund`/`out_receipt`).
- **Categorie de produs pe linia analitică** (`product_category_id`, câmp `related` stocat din `product_id.categ_id`) — permite gruparea și filtrarea liniilor analitice după categoria produsului.
- **Selecție automată a modelului de distribuție analitică** pe liniile facturilor de client/notă de credit/chitanță, în funcție de echipa de vânzări a facturii — dacă există exact un `account.analytic.distribution.model` configurat pentru acea echipă, distribuția lui e aplicată automat, inclusiv atunci când echipa se schimbă ulterior pe o factură existentă (nu doar la creare).
- **Determinare echipă de vânzări pe facturile de furnizor**: la generarea liniilor analitice dintr-o factură/notă de credit de furnizor, se caută o echipă CRM al cărei nume coincide cu numele contului analitic și se completează `team_id`.
- **Filtre suplimentare** în vizualizarea liniilor analitice: grupare după echipă de vânzări și după categoria de produs.
- **Șabloane de împărțire analitică** (`account.analytic.split.template`): un set ordonat de conturi analitice, fiecare cu un procent, reutilizabil pe mai multe împărțiri.
- **Asistent de împărțire** (`account.analytic.split`): pornind de la o sumă introdusă manual sau de la o linie analitică existentă selectată, generează automat linii analitice noi conform procentelor din șablon; flux `draft` → `confirmed`, cu buton de resetare care șterge liniile generate și revine la starea de ciornă.
- **Grup de securitate dedicat** ("Analitic split user") care controlează accesul la șabloane, la asistentul de împărțire și la liniile aferente.

**Corecție de conținut:** `readme/DESCRIPTION.md` descrie o funcționalitate diferită și mai veche — împărțirea *automată* a liniilor analitice de pe facturile de vânzare în valoare de stoc și marjă, condiționată de instalarea modulului `deltatech_sale_commission`, plus câmpuri de configurare pe contul analitic ("This rule is for splitting", "Stock Analytic Account", "Margin Analytic Account") și o opțiune în Setări ("Split Sale Analytic"). În codul actual (19.0.0.0.6) această funcționalitate este **dezactivată/eliminată**: view-ul din `views/res_config_settings.xml` este complet comentat, iar câmpurile aferente din `models/res_config_settings.py` sunt comentate; `models/account_analytic.py` nu mai extinde `account.analytic.account` cu acele câmpuri. `deltatech_sale_commission` nu apare nicăieri în cod sau manifest. Sumarul și funcționalitățile de mai sus reflectă comportamentul real din cod, nu textul din DESCRIPTION.md.

#### 3. Dependențe

- `account`
- `analytic`
- `sale`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `account.analytic.line` (extins): adaugă `product_category_id` (related, stocat) și `team_id`; la `create()`, deduce automat echipa de vânzări din picking-ul de stoc legat (pentru intrări generate din mișcări de stoc) sau din factura de vânzare/nota de credit/chitanța de vânzare (`out_invoice`/`out_refund`/`out_receipt`).
- `account.move.line` (extins): suprascrie `_compute_analytic_distribution` (cu dependența declarată pe `move_id.team_id`, astfel încât recalculul se face și când echipa se schimbă ulterior, nu doar la creare) pentru a aplica automat un `account.analytic.distribution.model` potrivit echipei facturii (facturi/note de credit/chitanțe de client); suprascrie `_prepare_analytic_lines` pentru a determina `team_id` pe facturile de furnizor prin potrivirea numelui contului analitic cu numele echipei CRM.
- `account.analytic.distribution.model` (extins): adaugă `team_id` (echipă de vânzări), folosit ca și criteriu de selecție automată descris mai sus.
- `account.analytic.split.template` / `account.analytic.split.template.line`: șablon reutilizabil de împărțire procentuală pe conturi analitice (nume, activ/inactiv, linii cu procent).
- `account.analytic.split` / `account.analytic.split.line`: asistentul de împărțire propriu-zis — sumă sau linie analitică sursă, tip de împărțire (`amount`/`line`), stare (`draft`/`confirmed`), acțiuni de calcul, confirmare (generează liniile analitice) și resetare.

**Vizualizări**

- `view_account_analytic_default_form`: adaugă câmpul echipă de vânzări pe formularul modelului de distribuție analitică (`account.analytic.distribution.model`).
- `view_account_analytic_line_filter`: adaugă filtrele de grupare „Sale team” și „Product category” pe liniile analitice.
- `view_account_analytic_split_form` / `view_account_analytic_split_tree` + `action_analytic_split`: interfața asistentului de împărțire, cu meniu „Analytic splits” sub **Contabilitate → Analitic**.
- `view_account_analytic_split_t_form` / `view_account_analytic_split_t_tree` + `action_analytic_split_template`: interfața șabloanelor de împărțire, cu meniu „Analytic split templates”.
- `res_config_settings.xml`: conține doar un view comentat integral — nicio opțiune activă în Setări în versiunea curentă.

**Acțiuni Automate / Acțiuni Server**

Nu au fost identificate `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale reale, verificate în cod, către alte module cu pagină în acest wiki. Modulul folosește modelul `crm.team` (adus deja de `sale`/`sales_team`) și extinde modele standard din `account`/`analytic`, dar nu depinde de și nu referă în cod niciun modul suplimentar din suita Terrabit.
