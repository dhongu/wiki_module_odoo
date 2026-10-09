# MT940 BT Format Bank Statements Import (localizat la `l10n_ro_account_bank_statement_import_mt940_bt/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_mt940_bt`
- **Versiune:** `19.0.0.2.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_account_bank_statement_import_mt940_bt
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_bank_statement_import_mt940_bt`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite importul în Odoo, ca extrase de cont, a fișierelor MT940 generate de banca Banca Transilvania (BT). Contabilul nu mai introduce manual tranzacțiile bancare: încarcă fișierul de la bancă, iar liniile extrasului sunt create automat, cu partenerul recunoscut după codul fiscal, acolo unde este posibil.

#### 2. Funcționalități Cheie

- Import de extrase în format MT940 specific BT, prin wizardul standard de import extras (`account.statement.import`); jurnalul bancar oferă formatul `mt940_ro_bt` printre formatele disponibile.
- Parserul BT se activează automat când BIC-ul băncii contului din jurnal este `BTRLRO22` (sau când contextul conține `mt940_ro_bt`); pentru orice alt fișier sau altă bancă se revine la parserii standard, deci nu interferează cu alte formate.
- Numărul contului (tag 25) și numele extrasului (tag 28) sunt preluate din fișier, curățate de puncte.
- Tranzacțiile (tag 61) sunt recunoscute după data, sensul (credit/debit), suma și referința; linia de tranzacție păstrează conținutul brut ca identificator unic de import, pentru evitarea dublurilor la reimport.
- Descrierea (tag 86) este analizată pentru a extrage codul fiscal (C.I.F.), numele partenerului și IBAN-ul; partenerul este asociat automat în Odoo după CIF (companii), iar dacă nu există eticheta de referință, se folosește textul complet al descrierii.
- Antetul fișierului BT (blocul `{1:`) este ignorat la citire.
- Fișier de test inclus în `test_files/test_bt_940.txt`; modulul are teste automate pentru parsare, potrivirea partenerului și comportamentul de rezervă.

#### 3. Dependențe

- `l10n_ro_account_bank_statement_import_mt940_base`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): adaugă formatul `mt940_ro_bt` la formatele de import disponibile pentru extrase.
- `account.statement.import` (extins, tranzient): detectează dacă jurnalul aparține BT (`_is_bt`) și folosește parserul BT în `_parse_file`, cu revenire la parserul standard.
- `l10n.ro.account.bank.statement.import.mt940.parser` (extins, abstract): suprascrie expresiile regulate pentru tag 61 și 86, antetul și handlerele pentru tag 25, 28, 61 și 86 când tipul este `mt940_ro_bt`.

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește wizardul standard de import extras.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `account_statement_import` (modulul standard de import extrase): wizardul extins de acest modul.
- `l10n_ro_account_bank_statement_import_mt940_base`: parserul MT940 de bază al localizării, extins pentru formatul BT (fără pagină wiki încă).
