# Romania - Enterprise Localization Config (localizat la `l10n_ro_ent_config/index.md`)

- **Nume Tehnic:** `l10n_ro_ent_config`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_ent_config
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_ent_config`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Acest modul oferă un punct unic de instalare și configurare pentru suita **l10n_ro_ent**
(localizarea enterprise Terrabit pentru România). Din **Setări → România Enterprise** poți
bifa direct modulele de care ai nevoie (declarații ANAF, e-Factura/e-Transport, contabilitate
și închidere de lună, rapoarte contabile și SAF-T, gestiuni de stoc, trezorerie, salarizare,
fiscalitate specială, conformitate & audit, POS), grupate pe categorii — fără să cauți fiecare
modul individual în Aplicații.

#### 2. Funcționalități Cheie

- Pagină dedicată "România Enterprise" în **Setări → General Settings**, vizibilă doar pentru
  companiile a căror țară este România (`country_code == 'RO'`).
- Zece categorii de setări, fiecare corespunzând unui grup funcțional din suita l10n_ro_ent:
  ANAF - Declarații & SPV, e-Factura & e-Transport, Contabilitate & Închidere de Lună, Rapoarte
  Contabile & SAF-T, Stoc & Gestiuni Contabile, Bănci & Trezorerie, Salarizare & HR,
  Fiscalitate Specială & Mediu, Conformitate & Audit, Puncte de Vânzare (POS).
- Bifarea unei setări instalează automat modulul corespunzător (și dependențele lui);
  debifarea îl dezinstalează, la apăsarea butonului **Salvează**.
- Fiecare setare are un text de ajutor (`help`) care explică pe scurt rolul modulului asociat,
  direct în interfață.
- Modulele care se instalează automat ca punte între alte două module (`auto_install`) nu apar
  în listă — se activează singure când ambele module conexe sunt prezente.
- Accesul la pagină este restricționat prin grupul `group_ro_ent_menus` ("Romania Enterprise
  Menus"), atribuit implicit administratorului (`base.user_admin`).

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extindere, tranzient): adaugă peste 90 de câmpuri booleene de tip
  `module_<nume_modul>`, câte unul pentru fiecare modul instalabil din suita l10n_ro_ent;
  bifarea/debifarea lor declanșează instalarea/dezinstalarea modulului corespunzător prin
  mecanismul standard Odoo de setări.

**Vizualizări**

- `res_config_settings_view_form`: extinde formularul de setări generale cu fila (app)
  "Romania Enterprise", organizată în blocuri (`block`) pe categorii funcționale, fiecare bloc
  conținând câte o `setting` per modul opțional.

**Securitate**

- `group_ro_ent_menus` ("Romania Enterprise Menus"): grup de securitate ce controlează
  vizibilitatea filei "Romania Enterprise" din setări; membru implicit `base.user_admin`.

#### 5. Conexiuni

Acest modul nu adaugă funcționalitate proprie, ci activează/dezactivează, prin pagina de
setări, oricare dintre modulele suitei l10n_ro_ent, grupate pe categorii:

**ANAF - Declarații & SPV**

- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md)
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md)
- [l10n_ro_anaf_d101](../l10n_ro_anaf_d101/index.md)
- [l10n_ro_anaf_d103](../l10n_ro_anaf_d103/index.md)
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md)
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md)
- [l10n_ro_anaf_d205](../l10n_ro_anaf_d205/index.md)
- [l10n_ro_anaf_d207](../l10n_ro_anaf_d207/index.md)
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)
- [l10n_ro_anaf_d318](../l10n_ro_anaf_d318/index.md)
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md)
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md)
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md)
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md)
- [l10n_ro_anaf_fiscal_status](../l10n_ro_anaf_fiscal_status/index.md)
- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md)

**e-Factura & e-Transport**

- [l10n_ro_efactura_b2c](../l10n_ro_efactura_b2c/index.md)
- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md)
- [l10n_ro_efactura_import_assist](../l10n_ro_efactura_import_assist/index.md)
- [l10n_ro_esigiliu](../l10n_ro_esigiliu/index.md)
- [l10n_ro_etransport_block](../l10n_ro_etransport_block/index.md)

**Contabilitate & Închidere de Lună**

- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md)
- [l10n_ro_account_counterpart](../l10n_ro_account_counterpart/index.md)
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md)
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md)
- [l10n_ro_advance_invoice](../l10n_ro_advance_invoice/index.md)
- [l10n_ro_cost_centers](../l10n_ro_cost_centers/index.md)
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md)
- [l10n_ro_deferred_entries](../l10n_ro_deferred_entries/index.md)
- [l10n_ro_dividends](../l10n_ro_dividends/index.md)
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md)
- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md)
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md)
- [l10n_ro_force_reconcile](../l10n_ro_force_reconcile/index.md)
- [l10n_ro_leasing](../l10n_ro_leasing/index.md)
- [l10n_ro_micro_tax](../l10n_ro_micro_tax/index.md)
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md)
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md)
- [l10n_ro_provisions](../l10n_ro_provisions/index.md)
- [l10n_ro_receivables_enhanced](../l10n_ro_receivables_enhanced/index.md)
- [l10n_ro_vat_deductibility](../l10n_ro_vat_deductibility/index.md)
- [l10n_ro_vat_group](../l10n_ro_vat_group/index.md)
- [l10n_ro_vat_on_payment_lock](../l10n_ro_vat_on_payment_lock/index.md)
- [l10n_ro_vat_refund](../l10n_ro_vat_refund/index.md)
- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md)
- [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md)

**Rapoarte Contabile & SAF-T**

- [l10n_ro_account_fisa_cont](../l10n_ro_account_fisa_cont/index.md)
- [l10n_ro_balance_confirmation](../l10n_ro_balance_confirmation/index.md)
- [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md)
- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md)
- [l10n_ro_fiscal_audit](../l10n_ro_fiscal_audit/index.md)
- [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md)
- [l10n_ro_partner_ledger_currency](../l10n_ro_partner_ledger_currency/index.md)
- [l10n_ro_registru_jurnal](../l10n_ro_registru_jurnal/index.md)
- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md)
- [l10n_ro_saft_etva](../l10n_ro_saft_etva/index.md)
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md)

**Stoc & Gestiuni Contabile**

- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md)
- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md)
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md)
- [l10n_ro_invoice_dvi_protect](../l10n_ro_invoice_dvi_protect/index.md)
- [l10n_ro_mrp_labour_account](../l10n_ro_mrp_labour_account/index.md)
- [l10n_ro_sgr](../l10n_ro_sgr/index.md)
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md)
- [l10n_ro_stock_constraints](../l10n_ro_stock_constraints/index.md)
- [l10n_ro_stock_custody](../l10n_ro_stock_custody/index.md)
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)
- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md)
- [l10n_ro_stock_pack_cmp](../l10n_ro_stock_pack_cmp/index.md)
- [l10n_ro_stock_pack_fifo](../l10n_ro_stock_pack_fifo/index.md)
- [l10n_ro_stock_posting_date](../l10n_ro_stock_posting_date/index.md)
- [l10n_ro_stock_provision](../l10n_ro_stock_provision/index.md)
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md)

**Bănci & Trezorerie**

- [l10n_ro_account_bank_statement_import_ing_csv](../l10n_ro_account_bank_statement_import_ing_csv/index.md)
- [l10n_ro_account_bank_statement_import_xlsx](../l10n_ro_account_bank_statement_import_xlsx/index.md)
- [l10n_ro_cash_bank_enhanced](../l10n_ro_cash_bank_enhanced/index.md)
- [l10n_ro_expense_currency](../l10n_ro_expense_currency/index.md)
- [l10n_ro_payment_instruments](../l10n_ro_payment_instruments/index.md)

**Salarizare & HR**

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md)
- [l10n_ro_payroll_import](../l10n_ro_payroll_import/index.md)
- [l10n_ro_payroll_ro](../l10n_ro_payroll_ro/index.md)
- [l10n_ro_reges](../l10n_ro_reges/index.md)

**Fiscalitate Specială & Mediu**

- [l10n_ro_cbam](../l10n_ro_cbam/index.md)
- [l10n_ro_environmental_tax](../l10n_ro_environmental_tax/index.md)
- [l10n_ro_excise](../l10n_ro_excise/index.md)
- [l10n_ro_grants](../l10n_ro_grants/index.md)
- [l10n_ro_oss_threshold](../l10n_ro_oss_threshold/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)

**Conformitate & Audit**

- [l10n_ro_audit_immutable](../l10n_ro_audit_immutable/index.md)
- [l10n_ro_sod_matrix](../l10n_ro_sod_matrix/index.md)

**Puncte de Vânzare (POS)**

- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md)
- [l10n_ro_sale_receipt_type_report](../l10n_ro_sale_receipt_type_report/index.md)
