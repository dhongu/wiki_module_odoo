# MT940 Revolut Format Bank Statements Import (localizat la `l10n_ro_account_bank_statement_import_mt940_revolut/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_mt940_revolut`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_account_bank_statement_import_mt940_revolut
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_bank_statement_import_mt940_revolut`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite importul în Odoo, ca extrase de cont, a fișierelor MT940 exportate din Revolut Business. Un singur export Revolut conține câte un bloc pentru fiecare portofel valutar, toate sub același IBAN; fiecare bloc este importat în jurnalul bancar al monedei respective, iar portofelele fără jurnal corespunzător (de exemplu un portofel în valută fără tranzacții) sunt ignorate, fără a bloca importul.

#### 2. Funcționalități Cheie

- Import de fișiere MT940 Revolut Business ca extrase de cont bancar, prin fluxul standard de import din jurnal.
- Format de import nou, `mt940_ro_revolut`, disponibil pe jurnalele bancare; importul se aplică și automat când contul bancar al jurnalului are BIC-ul care începe cu `REVO`.
- Împărțirea exportului pe monede: fiecare bloc valutar (portofel) devine un extras separat, asociat jurnalului bancar de aceeași monedă.
- Mai multe jurnale pot partaja același IBAN Revolut (câte unul pe monedă), astfel încât toate portofelele unui cont să poată fi importate dintr-un singur fișier.
- Portofelele pentru care nu există jurnal pe IBAN-ul și moneda respectivă sunt omise în tăcere, nu opresc importul.
- Monedele inactive în Setări, dar folosite de un jurnal, sunt recunoscute corect la potrivire.
- Parser MT940 dedicat Revolut (etichetele 60F, 61, 86), peste parserul de bază MT940.

#### 3. Dependențe

- `l10n_ro_account_bank_statement_import_mt940_base`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): adaugă formatul `mt940_ro_revolut` la formatele de import disponibile.
- `account.statement.import` (extins, wizard): detectează Revolut (`_is_revolut`), împarte datele pe monedă (`_split_by_currency`), verifică existența jurnalului pe IBAN și monedă (`_revolut_journal_exists`) și suprascrie `_match_journal` pentru a alege jurnalul monedei potrivite când mai multe jurnale au același IBAN.
- `l10n.ro.account.bank.statement.import.mt940.parser` (extins): parser pentru fișierele MT940 Revolut (antet, tag 60F, 61 și 86).

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește wizardul standard de import extras.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `l10n_ro_account_bank_statement_import_mt940_base`: baza comună de parsare MT940 pentru localizarea română (dependență directă, fără pagină wiki).
- `account_statement_import_file`: wizardul de import extrase, extins aici (fără pagină wiki).
