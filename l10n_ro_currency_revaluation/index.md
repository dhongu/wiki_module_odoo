# Romania - Reevaluare Valutară (OMFP 1802) (localizat la `l10n_ro_currency_revaluation/index.md`)

- **Nume Tehnic:** `l10n_ro_currency_revaluation`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_currency_revaluation
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_currency_revaluation`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Modul pentru reevaluarea lunară a soldurilor în valută, cu generarea automată de diferențe de curs (conturi 665/765) fără stornare automată, conform OMFP 1802/2014 (pct. 340–345). Spre deosebire de abordarea IFRS din Enterprise, nota contabilă rezultată nu se stornează automat la începutul lunii următoare, respectând tratamentul contabil românesc.

## 2. Funcționalități Cheie

- **Model audit trail** `l10n.ro.currency.revaluation` cu state machine (ciornă → postată → anulată).
- **Calcul automat al soldurilor reziduale valutare** la data balanței (SQL cu reconcilieri parțiale).
- **Generare notă contabilă fără stornare automată** — comportament corect pentru OMFP 1802 vs. IFRS.
- **Override wizard Enterprise** `account.multicurrency.revaluation.wizard` cu checkbox „Fără stornare automată".
- **Conturi RO incluse:** 5124, 5314, 4111, 401, 451, 461, 462, 267, 508.

## 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`

## 4. Componente Cheie

### Modele

- `l10n.ro.currency.revaluation`: modelul audit trail al reevaluării valutare, cu state machine și nota contabilă asociată.
- `account.multicurrency.revaluation.wizard`: wizardul Enterprise extins cu opțiunea „Fără stornare automată".

### Vizualizări / Date

- `views/l10n_ro_currency_revaluation_views.xml`: vizualizările modelului de reevaluare.
- `wizard/account_multicurrency_revaluation_wizard_views.xml`: wizardul de reevaluare extins.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate acțiuni automate; reevaluarea se lansează manual prin wizard.*

## 5. Conexiuni

- `[[l10n_ro_expense_currency]]`
- `[[l10n_ro_deferred_entries]]`
