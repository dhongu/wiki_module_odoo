# Romania - Fișă de cont (localizat la `l10n_ro_account_fisa_cont/index.md`)

- **Nume Tehnic:** `l10n_ro_account_fisa_cont`
- **Versiune:** `20.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_account_fisa_cont
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_fisa_cont`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul oferă un raport nativ „Fișă de Cont" integrat în framework-ul `account_reports` Enterprise, conform **OMFP 1802/2014** (formular după OMFP 2634/2015). Afișează pentru fiecare cont: sold inițial, mișcări cu cont corespondent, sold progresiv și sold final.

#### 2. Funcționalități Cheie

- Sold inițial calculat automat de framework (tranzacții anterioare perioadei selectate).
- Coloana **Cont Corespondent**: cont unic → cod cont; conturi multiple → „Diverși".
- Sold progresiv acumulat per linie (running balance).
- Export **PDF** landscape și **XLSX** nativ.
- Drill-down la nota contabilă (opțiuni caret moștenite din Cartea Mare).
- Filtre: perioadă, jurnale, căutare după cont și filtru **Parteneri**, care listează și contactele de sub firmă (de exemplu fișa contului 542 pe un angajat). În Odoo 20, filtrul analitic e înlocuit de gruparea analitică standard (coloane pe cont analitic).
- Suport multi-companie cu selector de companie.
- Vizibil automat doar pentru companiile cu **Țara = România**; meniu: Contabilitate → Raportare → Registre → Fișă de Cont.
- Spre deosebire de Cartea Mare standard, include nativ contul corespondent.

#### 3. Dependențe

- `account_reports`
- `accountant`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fisa.cont.report.handler` (model abstract, extinde `account.general.ledger.report.handler`): calculează coloana „Cont Corespondent" printr-un batch SQL pe `account_move_line` și o injectează în liniile raportului prin postprocesorul de linii (inclusiv la desfășurarea conturilor).

**Vizualizări**

- `l10n_ro_fisa_cont_report` (`account.report`): definește raportul „Fișă de Cont", cu coloanele Dată, Partener, Debit, Credit, Cont Corespondent, Sold și handler-ul custom.
- `action_account_report_l10n_ro_fisa_cont` (`ir.actions.client`): acțiunea de meniu care deschide raportul.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate.* Drepturile de acces sunt definite în `security/ir.access.csv`.

#### 5. Conexiuni

- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md): planul de conturi românesc folosit pentru codurile conturilor corespondente.
- [l10n_ro_account_correspondence](../l10n_ro_account_correspondence/index.md): persistă contul corespondent la nivel de linie contabilă (aceeași logică „cont unic / Diverși").
- [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md): afișează contul corespondent în Cartea Mare.
