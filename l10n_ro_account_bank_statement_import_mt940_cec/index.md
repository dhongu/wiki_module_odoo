# MT940 CEC Format Bank Statements Import (localizat la `l10n_ro_account_bank_statement_import_mt940_cec/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_mt940_cec`
- **Versiune:** `19.0.0.2.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_account_bank_statement_import_mt940_cec
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_bank_statement_import_mt940_cec`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite importul în Odoo, ca extrase de cont, a fișierelor în format MT940 generate de banca CEC Bank din România. Contabilul încarcă fișierul primit de la bancă, iar tranzacțiile ajung direct în extras, fără introducere manuală, cu partenerul identificat automat după codul fiscal acolo unde este posibil.

#### 2. Funcționalități Cheie

- Import de extrase de cont în format MT940 specific CEC Bank, ca variantă suplimentară de import pe jurnalele bancare (format `mt940_ro_cec`).
- Detectarea automată a băncii: parserul CEC se aplică atunci când contul bancar al jurnalului are codul BIC `CECEROBU`; altfel importul continuă cu parserele celorlalte bănci.
- Interpretarea specifică a formatului CEC: antet pe `:20:`, cuvinte-cheie în detalii (Referință, Plătitor, Beneficiar, Detalii, CODFISC), tag `:61:` cu dată, sens (credit/debit), sumă și referință, iar `:28:` ca nume al extrasului.
- Preluarea contrapartidei (cont, nume partener) din tag-ul `:86:`.
- Asocierea automată a partenerului: după codul fiscal din tranzacție se caută o companie din Odoo cu acel CUI, iar dacă este găsită, tranzacția primește partenerul respectiv.

#### 3. Dependențe

- `l10n_ro_account_bank_statement_import_mt940_base`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): adaugă formatul `mt940_ro_cec` în lista formatelor de import disponibile.
- `account.statement.import` (wizard extins): alege parserul CEC pe baza BIC-ului contului jurnalului și asociază partenerii după CUI.
- `l10n.ro.account.bank.statement.import.mt940.parser` (model abstract extins): suprascrie regulile de parsare (antet, regex tag 61, cuvinte-cheie, tag 28 și 86, contrapartidă) doar pentru tipul `mt940_ro_cec`.

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `l10n_ro_account_bank_statement_import_mt940_base`: parserul MT940 de bază, specializat aici pentru CEC (este și dependență directă).
