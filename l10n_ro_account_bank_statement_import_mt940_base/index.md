# Romania - MT940 Bank Statements Import

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_mt940_base`
- **Versiune:** `20.0.0.4.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_account_bank_statement_import_mt940_base
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_account_bank_statement_import_mt940_base
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Oferă un parser generic pentru fișiere MT940 (extras de cont bancar). Deoarece fiecare bancă interpretează formatul în felul ei, modulul nu importă singur extrase: este destinat să fie folosit de modulele specifice fiecărei bănci, care implementează dialectul respectiv.

#### 2. Funcționalități Cheie

- Parser generic MT940, reutilizabil de modulele pentru bănci.
- Adaugă formatul de import `mt940_general` în lista formatelor disponibile pe jurnalele bancare.
- Pe contul bancar al partenerului apare câmpul „Romania - MT940 Unstructured Tag 86 Pattern”, în care se definește modelul (pattern) pentru interpretarea câmpului nestructurat Tag 86.
- Se integrează în fluxul standard de import de extrase (`account.statement.import`).

#### 3. Dependențe

- `account_statement_import_file`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `account.journal`: adaugă formatul `mt940_general`.
- `res.partner.bank`: câmpul `l10n_ro_unstructured_tag86`.
- `account.statement.import`: extins pentru a recunoaște fișierele MT940.
- `l10n.ro.account.bank.statement.import.mt940.parser`: parserul MT940.

**Vizualizări**

- `view_partner_bank_form`: adaugă câmpul pattern Tag 86 în formularul contului bancar (moștenește `l10n_ro_config.view_partner_bank_form`).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_account_bank_statement_import_mt940_ing](../l10n_ro_account_bank_statement_import_mt940_ing/index.md): dialectul ING construit peste acest parser.
- [l10n_ro_config](../l10n_ro_config/index.md): mixin și vizualizarea contului bancar.
