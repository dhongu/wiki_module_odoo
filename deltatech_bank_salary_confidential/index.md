# Confidential Salary Payments in Bank Statements (localizat la `deltatech_bank_salary_confidential/index.md`)

- **Nume Tehnic:** `deltatech_bank_salary_confidential`
- **Versiune:** `19.0.1.0.1`
- **Cale:** [https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_bank_salary_confidential](https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_bank_salary_confidential)
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_bank_salary_confidential`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul păstrează confidențialitatea plăților de salarii atunci când liniile de extras bancar sunt importate (fișier, sincronizare online sau introducere manuală). Liniile care se potrivesc cu un model de reconciliere marcat drept "Anonymize Matched Transactions" sunt anonimizate automat — eticheta liniei, numele partenerului, contul bancar și notele sunt înlocuite cu o etichetă configurabilă (de ex. "Plata salarii") — astfel încât identitatea angajatului nu mai apare în contabilitate, iar linia poate fi reconciliată automat cu contul de contrapartidă (de ex. 421 "Personal - salarii datorate").

#### 2. Funcționalități Cheie

- Anonimizarea automată a etichetei, numelui partenerului, contului bancar, notelor și detaliilor brute ale tranzacției pentru liniile de extras care se potrivesc unui model de reconciliere marcat corespunzător.
- Reconciliere automată a liniei anonimizate cu contul de contrapartidă configurat pe modelul de reconciliere (ex. 421), când validarea automată este activată pe model.
- Anonimizarea rulează la crearea liniei de extras (import, sincronizare online sau creare manuală), nu doar la cron-ul de reconciliere, astfel încât detaliile personale nu rămân niciodată vizibile.
- Jurnalul contabil generat folosește de asemenea eticheta anonimizată, fără detalii personale pe nota contabilă.
- Mesaj automat pe factură/notă contabilă care confirmă anonimizarea și validarea automată prin modelul de reconciliere folosit.
- Excludere din procesare via cheia de context `skip_salary_anonymization`.
- Suport pentru modele cu declanșator manual: anonimizarea și reconcilierea au loc când utilizatorul aplică modelul din widget-ul de reconciliere bancară.

#### 3. Dependențe

- `account_accountant`

#### 4. Componente Cheie

**Modele**

- `account.bank.statement.line` (extins): la creare, aplică automat modelele de reconciliere marcate pentru anonimizare (`_salary_apply_anonymize_models`) asupra liniilor nereconciliate; metoda `_salary_anonymize` înlocuiește eticheta, numele partenerului, contul bancar, notele și detaliile tranzacției cu eticheta anonimizată configurată.
- `account.reconcile.model` (extins): adaugă câmpurile `anonymize_matched` (Boolean — activează anonimizarea) și `anonymize_label` (Char — textul de înlocuire); suprascrie `_trigger_reconciliation_model` pentru a anonimiza linia înainte de aplicarea modelului, astfel încât liniile jurnalului generate să preia deja eticheta anonimizată.

**Vizualizări**

- `view_account_reconcile_model_form`: extinde formularul standard al modelelor de reconciliere (`account.view_account_reconcile_model_form`) adăugând câmpurile `anonymize_matched` și `anonymize_label` (vizibil/obligatoriu doar când anonimizarea e activată).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul; anonimizarea rulează sincron la crearea liniei de extras bancar, nu printr-un job programat.

#### 5. Conexiuni

- `account_accountant`: modelele de reconciliere (`account.reconcile.model`) și widget-ul de reconciliere bancară pe care le extinde acest modul provin din `account_accountant`.
