# Romania - Fișă de Cont (localizat la `l10n_ro_account_fisa_cont/index.md`)

- **Nume Tehnic:** `l10n_ro_account_fisa_cont`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_fisa_cont
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_fisa_cont`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul oferă un raport nativ „Fișă de Cont" integrat în framework-ul `account_reports` Enterprise, conform **OMFP 1802/2014**. Acesta afișează pentru fiecare cont: sold inițial, mișcări cu cont corespondent, sold progresiv și sold final.

#### 2. Funcționalități Cheie

- Sold inițial calculat automat de framework (tranzacții anterioare perioadei selectate).
- Coloana **Cont Corespondent**: cont unic → cod cont; conturi multiple → „Diverși".
- Sold progresiv acumulat per linie (running balance).
- Export **PDF** landscape și **XLSX** nativ.
- Drill-down la nota contabilă (opțiuni caret moștenite din Grand Livre).
- Filtre: perioadă, jurnale, analitic, căutare cont/partener.
- Suport multi-companie cu selector de companie.
- Vizibil automat doar pentru companiile cu **Țara = România**.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fisa.cont.report.handler` (model abstract, extinde `account.general.ledger.report.handler`): calculează coloana „Cont Corespondent" printr-un batch SQL pe `account_move_line` — cont unic pe partea opusă a notei → codul contului; conturi multiple → „Diverși"; injectează valorile în liniile raportului la expandare și la postprocesare.

**Vizualizări**

- `l10n_ro_fisa_cont_report` (`account.report`): definește raportul „Fișă de Cont", cu coloanele Dată, Partener, Debit, Credit, Sold (running balance) și handler-ul custom pentru coloana Cont Corespondent.
- `action_account_report_l10n_ro_fisa_cont` (`ir.actions.client`): acțiunea de meniu care deschide raportul (Contabilitate → Rapoarte → Registre → Fișă de Cont).

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate.*

#### 5. Conexiuni

- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md): folosește planul de conturi românesc (`code_store` per companie) pentru determinarea codului contului corespondent.
