# Confidential Salary Payments in Bank Statements (localizat la `deltatech_bank_salary_confidential/index.md`)

- **Nume Tehnic:** `deltatech_bank_salary_confidential`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_bank_salary_confidential
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_bank_salary_confidential`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul păstrează confidențialitatea plăților de salarii atunci când liniile de extras bancar sunt importate (fișier, sincronizare online sau creare manuală). Liniile care se potrivesc cu un model de reconciliere marcat **Anonymize Matched Transactions** sunt anonimizate automat — eticheta, numele partenerului, contul bancar și notele sunt înlocuite cu o etichetă configurabilă (de ex. „Plată salarii”) — astfel încât identitatea angajatului nu apare în contabilitate, iar linia se reconciliază automat cu contul de contrapartidă (de ex. 421 „Personal - salarii datorate”).

#### 2. Funcționalități Cheie

- **Anonimizare la crearea liniei**: eticheta, numele partenerului, contul bancar, notele și detaliile brute ale tranzacției se înlocuiesc imediat ce linia este creată (import, sincronizare online sau creare manuală), nu abia la cron-ul de reconciliere, deci datele personale nu rămân vizibile.
- **Reconciliere automată** cu contul de contrapartidă din modelul de reconciliere (ex. 421), când validarea automată (*Auto-validate*) este activă pe model; nota contabilă generată folosește tot eticheta anonimizată, fără partener.
- **Mesaj automat** în chatter-ul notei contabile, care confirmă anonimizarea și validarea prin modelul folosit.
- **Configurare**: din tabloul de bord *Contabilitate*, meniul ⋮ al cardului jurnalului bancar → *Reconciliation: Models*; modelul are *Trigger* = *Automated* (necesar pentru anonimizare la import), *Anonymize Matched Transactions* bifat, *Anonymized Label* (ex. `Plată salarii`), condiții pe etichetă (*Contains* sau *Match Regex*, de ex. `^VIRARE SALARIU`), pe sumă (*Is lower than or equal to* `0`, pentru plăți de ieșire) și pe jurnalul bancar de salarii, plus un rând de contrapartidă pe contul `421` cu 100% din sold.
- **Condiții stricte**: potrivirea ignoră majusculele și se uită și în detaliile tranzacției, deci un text larg (`salar`, chiar `SALARIU`) prinde și avansuri, popriri sau taxe salariale plătite Trezoreriei, care ar fi anonimizate și înregistrate pe 421; pentru acestea se folosesc modele separate, fără anonimizare, cu contul potrivit.
- **Excepții**: liniile create cu cheia de context `skip_salary_anonymization` nu sunt procesate; butonul **Test** din wizardul de import CSV doar simulează importul (fără anonimizare), efectul apare la **Import**; un model cu trigger *Manual* nu rulează la import, ci anonimizează și reconciliază linia când utilizatorul îl aplică din widget-ul de reconciliere bancară.
- **Atenție la atașamente**: anonimizarea rescrie linia de extras, nu și fișierul original, care, dacă este păstrat ca atașament, conține în continuare datele inițiale — accesul la atașamente se poate restricționa.

#### 3. Dependențe

- `account_accountant`

#### 4. Componente Cheie

**Modele**

- `account.bank.statement.line` (extins): la `create()`, aplică modelele de reconciliere marcate pentru anonimizare (`_salary_apply_anonymize_models`, doar cele cu trigger automat) liniilor nereconciliate; sare peste cheia `skip_salary_anonymization` și peste importul de test (`auto_statement_processing` fals); `_salary_anonymize` înlocuiește eticheta și golește partenerul, contul bancar, notele și detaliile tranzacției.
- `account.reconcile.model` (extins): adaugă `anonymize_matched` (Boolean) și `anonymize_label` (Char, implicit „Salary payment”); suprascrie `_trigger_reconciliation_model` pentru a anonimiza linia înainte de aplicarea modelului și a posta mesajul de confirmare.

**Vizualizări**

- `view_account_reconcile_model_form`: extinde formularul modelelor de reconciliere cu `anonymize_matched` și `anonymize_label` (vizibil/obligatoriu doar când anonimizarea e activă).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`; anonimizarea rulează sincron la crearea liniei de extras.

#### 5. Conexiuni

- `account_accountant`: modelele de reconciliere și widget-ul de reconciliere bancară extinse de modul provin de aici.
