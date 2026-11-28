# MT940 ING Format Bank Statements Import

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_mt940_ing`
- **Versiune:** `20.0.0.2.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_account_bank_statement_import_mt940_ing
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_account_bank_statement_import_mt940_ing
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite importul în Odoo, ca extrase de cont, a fișierelor MT940 emise de banca ING România, ușurând reconcilierea fără introducere manuală.

#### 2. Funcționalități Cheie

- Adaugă formatul de import `mt940_ro_ing` pe jurnalele bancare.
- Parser specific dialectului ING, construit peste parserul MT940 generic.
- Formularul contului bancar afișează un exemplu de pattern pentru Tag 86 (partener, CUI, IBAN), ca ajutor la configurare.
- Folosește fluxul standard de import de extrase (`account.statement.import`).

#### 3. Dependențe

- [l10n_ro_account_bank_statement_import_mt940_base](../l10n_ro_account_bank_statement_import_mt940_base/index.md)

#### 4. Componente Cheie

**Modele**

- `account.journal`: adaugă formatul `mt940_ro_ing`.
- `account.statement.import`: extins pentru fișierele ING.
- `l10n.ro.account.bank.statement.import.mt940.parser`: extins cu logica ING.

**Vizualizări**

- `view_partner_bank_form`: afișează un exemplu de pattern sub câmpul Tag 86.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_account_bank_statement_import_ing_csv](../l10n_ro_account_bank_statement_import_ing_csv/index.md): import de extrase ING din CSV, alternativă la MT940.
