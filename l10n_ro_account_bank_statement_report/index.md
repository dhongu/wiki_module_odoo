# Romania - Bank Statement Report

- **Nume Tehnic:** `l10n_ro_account_bank_statement_report`
- **Versiune:** `20.0.0.2.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_account_bank_statement_report
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_account_bank_statement_report
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite tipărirea registrului de casă și de bancă pentru o zi sau pentru o perioadă, pornind de la extrasele jurnalelor de numerar și bancare.

#### 2. Funcționalități Cheie

- Raport „Romania - Cash - Bank Register” disponibil din lista sau formularul extraselor.
- Variante de raport zilnic și pe perioadă.
- Utilizare: se deschide extrasul unui jurnal bancar sau de numerar și se tipărește raportul din meniul Tipărire.

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `account.bank.statement`: extins cu mixinul de localizare `l10n.ro.mixin`, ca suport pentru rapoarte.

**Vizualizări**

- `report_l10n_ro_statement_daily`: șablon QWeb pentru registrul zilnic.
- `report_l10n_ro_statement_period`: șablon QWeb pentru registrul pe perioadă.
- `report_statement` și `action_report_l10n_ro_account_statement`: raportul și acțiunea de tipărire.

**Acțiuni Automate / Acțiuni Server**

- Nu există (doar acțiunea de raport).

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): setările de localizare.
