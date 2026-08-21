# Checklist Închidere Perioadă (localizat la `l10n_ro_period_close_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_period_close_enhanced`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_period_close_enhanced
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_period_close_enhanced`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de localizare românească care implementează un checklist lunar de închidere a perioadei contabile, folosind infrastructura Enterprise `account.return.type` din modulul `account_reports`. Se adresează contabililor care efectuează închiderea lunară și doresc un flux structurat cu verificări automate, conform cerințelor OMFP 1802/2014.

#### 2. Funcționalități Cheie

- Checklist interactiv de tip `audit` cu flux **New → Review → Submit**, creat automat pentru fiecare lună.
- Verificări automate evaluate de sistem: facturi/avize în stare Schiță, extrase bancare nereconciliate.
- Verificări condiționale (active doar dacă modulul opțional este instalat): Coeficient K, CMP Periodic, Reevaluare Valutară (665/765), Regularizare TVA (4426/4427 → 44231/4424), WIP producție (331/711), provizioane stocuri slow-moving (39x), contabilizare completă a inventarelor de stoc.
- Verificări manuale confirmate de contabil: registru de casă, inventar stocuri, reconciliere clienți/furnizori (411x/401x).
- Blocare perioadă la validare: la închiderea lunii decembrie se setează automat data de blocare a exercițiului financiar (`fiscalyear_lock_date`), avansând doar (nu retrage o blocare existentă mai recentă).
- Raport unic de pre-închidere (PDF): proces-verbal cu toate verificările (verificate / anomalii / în așteptare), observații și semnături — generat automat la validare și retipăribil oricând (`action_print_preclose_report`).
- Termen implicit de 5 zile după sfârșitul lunii, configurabil pe tipul de return (`RO – Checklist Închidere Perioadă`).
- Blocare per-jurnal (`l10n_ro_lock_date` pe `account.journal`): permite blocarea jurnalelor TVA/vânzări după depunerea D300, ținând alte jurnale (ex. salarii) deschise.
- Reguli de reconciliere pentru plățile lunare la buget (TVA 4423, impozit profit 4411, micro 4418, CAS 4315, CASS 4316, CAM 436, impozit salarii 444, alte impozite 446) — livrate ca șablon `account.reconcile.model` la instalare/upgrade și pentru companii noi, cu propunere automată a contrapartidei pe baza narațiunii extrasului bancar; activare opt-in a reconcilierii complet automate din `res.company.l10n_ro_budget_auto_reconcile`.
- Integrare nativă cu checklistele de closing din celelalte module RO (K, CMP, reevaluare, regularizare TVA, WIP, provizioane stoc, D300).

#### 3. Dependențe

- `account_reports`
- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.return` (extins): definește checklist-ul RO de închidere lunară — verificările Python condiționate (`_check_ro_k_coefficient`, `_check_ro_cmp_periodic`, `_check_ro_currency_revaluation`, `_check_ro_period_vat_regularization`, `_check_ro_wip_closing`, `_check_ro_stock_provision`, `_check_ro_inventory_closing`), blocarea exercițiului la validarea din decembrie (`_l10n_ro_apply_period_lock`) și generarea raportului de pre-închidere (`_l10n_ro_generate_preclose_report`, `action_print_preclose_report`).
- `account.chart.template` (extins): livrează șablonul de reguli de reconciliere `account.reconcile.model` pentru plățile bugetare RO (`_get_ro_budget_reconcile_model`), pe baza mapării `RO_BUDGET_RECO_RULES`/`RO_BUDGET_RECO_NAMES`.
- `account.journal` (extins): câmpul `l10n_ro_lock_date` pentru blocare de postare per-jurnal.
- `res.company` / `res.config.settings` (extinse): configurarea opt-in a reconcilierii automate a plăților bugetare (`l10n_ro_budget_auto_reconcile`) și sincronizarea regulilor (`action_l10n_ro_sync_budget_reconcile`).
- `account.move` (extins): suport pentru verificările de checklist legate de facturi/avize în stare Schiță.

**Vizualizări / Date**

- `data/period_close_return_type.xml`: definește tipul de return `return_type_ro_period_close` (categorie `audit`, flux `generic_state_review_submit`, periodicitate lunară, termen 5 zile) și cele 8 șabloane de verificare (`account.return.check.template`).
- `data/menu.xml`: intrarea de meniu pentru checklist-ul de închidere perioadă.
- `report/report_period_close.xml`: raportul PDF de pre-închidere (proces-verbal).
- `views/res_config_settings_views.xml`: setările de configurare pentru reconcilierea automată a plăților bugetare.
- `views/account_journal_views.xml`: câmpul de blocare per-jurnal pe formularul de jurnal contabil.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`_l10n_ro_period_close_post_init`): rulează la instalare pentru inițializarea regulilor/datelor specifice RO.
- Verificările automate (model + domeniu) și cele Python condiționate sunt evaluate la refresh/review, prin `_run_checks()` suprascris pe `account.return`.
- La `action_validate()` pe checklist se declanșează automat blocarea exercițiului (decembrie) și generarea/atașarea raportului PDF de pre-închidere.

#### 5. Conexiuni

- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md): verificare condiționată — coeficientul K postat pentru luna curentă.
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): verificare condiționată — nota de corecție CMP periodic postată.
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): verificare condiționată — reevaluarea valutară postată.
- [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md): verificare condiționată — WIP-ul de producție finalizat în perioadă.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): checklist complementar de închidere P&L, în același ecosistem de closing bazat pe `account.return`.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarația D300 TVA, pas de closing conex înaintea checklist-ului.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): registrul de inventar, legat de verificarea manuală/condiționată a inventarului de stocuri.
- [l10n_ro_mrp_labour_account](../l10n_ro_mrp_labour_account/index.md): parte din ecosistemul de contabilitate de producție/stoc verificat la closing.
