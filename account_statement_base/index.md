# Bank Statement Base (localizat la `account_statement_base/index.md`)

- **Nume Tehnic:** `account_statement_base`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/others_addons/tree/20.0/account_statement_base
- **Cale Locală:** `odoo-addons/others_addons/account_statement_base`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Acest modul tehnic readuce în interfața Odoo vizualizările dedicate liniilor de extras de cont bancar (*Bank Statement Lines*), care începând cu Odoo 16.0 nu mai fac parte din modulul standard `account`. Practic, oferă contabililor un ecran clasic (listă, formular, kanban) pentru a vedea, filtra și corecta rapid tranzacțiile bancare importate, fără a fi nevoie de instalarea unui modul Enterprise pentru asta.

#### 2. Funcționalități Cheie

- Adaugă o acțiune și un meniu dedicat pentru **Bank Statement Lines** (`account.bank.statement.line`), cu vizualizări listă, formular și kanban.
- Pe formularul extrasului de cont (`account.bank.statement`) adaugă un buton statistic „Transactions” care deschide direct liniile extrasului curent, plus un buton „Journal Items” către notele contabile aferente (validate, grupate pe operațiune).
- În lista de extrase de cont adaugă un buton rapid „Open Statement Lines” pentru fiecare rând și permite crearea directă de extrase din listă.
- Linia de extras (formular) expune sold reconciliere, tip tranzacție, cont bancar al partenerului și plățile asociate (`payment_ids`) pe o filă tehnică separată.
- Lista de linii de extras oferă editare inline (`editable="top"`, `multi_edit`), evidențiere vizuală a liniilor deja reconciliate, sold curent (`running_balance`) și butoane rapide pentru „Revert reconciliation” și deschiderea notei contabile aferente.
- Căutarea liniilor de extras permite filtrare după partener, jurnal, sumă, stare de reconciliere și stare de verificare (`to_check`), plus grupări după partener, jurnal, tip de tranzacție sau dată.
- Suprascrie acțiunea de creare a extraselor de tip „cash” (`create_cash_statement`) astfel încât să funcționeze fără mesajul standard care cere modulul Enterprise.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.bank.statement` (extindere): adaugă `action_open_statement_lines()` (deschide liniile extrasului curent) și `open_entries()` (deschide notele contabile validate ale extrasului).
- `account.bank.statement.line` (extindere): adaugă `action_open_journal_entry()`, care deschide nota contabilă (`account.move`) generată de linia extrasului.
- `account.journal` (extindere): suprascrie `create_cash_statement()` pentru a deschide direct acțiunea `account_bank_statement_line_action` filtrată pe jurnalul curent, în loc de mesajul standard Enterprise.

**Vizualizări**

- `view_bank_statement_form`: formular al extrasului de cont, cu butoane statistice „Transactions” și „Journal Items”, secțiune sold inițial/final și mesaj de avertizare (`problem_description`) când extrasul are o problemă.
- `view_bank_statement_tree` (extindere `account.view_bank_statement_tree`): permite crearea din listă și adaugă butonul „Open Statement Lines” pe fiecare rând.
- `account_bank_statement_line_form`: formular al liniei de extras, cu date principale (dată, referință plată, partener, sumă, cont bancar) și filă tehnică (tip tranzacție, nume partener, cont, stare reconciliere, plăți asociate).
- `account_bank_statement_line_tree`: listă editabilă a liniilor de extras, cu sold curent, evidențiere linii reconciliate și butoane de acțiune rapidă.
- `account_bank_statement_line_search`: filtre și grupări pentru liniile de extras (partener, jurnal, sumă, reconciliat/nereconciliat, „de verificat”, dată).
- `account_bank_statement_line_action`: acțiunea fereastră principală „Bank Statement Lines” (listă/formular/kanban).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server — logica este expusă exclusiv prin acțiuni de fereastră și metode apelate din butoanele vizualizărilor.

#### 5. Conexiuni

- `account`: extinde direct modelele contabile standard (`account.bank.statement`, `account.bank.statement.line`, `account.journal`) fără a introduce module noi de business — este un modul suport, folosit de obicei de alte module OCA de reconciliere bancară (ex. `account_reconcile_oca`) ca bază pentru interfața de linii de extras.
