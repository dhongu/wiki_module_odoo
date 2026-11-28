# Romania - Configurare localizare Enterprise (localizat la `l10n_ro_ent_config/index.md`)

- **Nume Tehnic:** `l10n_ro_ent_config`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_ent_config
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_ent_config`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un punct unic de instalare și configurare pentru suita **l10n_ro_ent** (localizarea enterprise Terrabit pentru România). Din **Setări → România Enterprise** se bifează direct modulele necesare (declarații ANAF, e-Factura/e-Transport, contabilitate și închidere de lună, rapoarte contabile și SAF-T, gestiuni de stoc, trezorerie, salarizare, fiscalitate specială, conformitate și audit, POS), grupate pe categorii, fără a căuta fiecare modul în Aplicații.

#### 2. Funcționalități Cheie

- Pagina **România Enterprise** în **Setări**, vizibilă doar când compania curentă este din România și doar utilizatorilor din grupul **Meniuri România Enterprise** (la instalare îl primește administratorul implicit; alți administratori se adaugă din Setări → Utilizatori & Companii → Grupuri, în modul dezvoltator).
- Zece categorii: ANAF - Declarații & SPV, e-Factura & e-Transport, Contabilitate & Închidere de Lună, Rapoarte Contabile & SAF-T, Stoc & Gestiuni Contabile, Bănci & Trezorerie, Salarizare & HR, Fiscalitate Specială & Mediu, Conformitate & Audit, Puncte de Vânzare (POS).
- Bifarea unei setări și **Salvează** instalează modulul cu toate dependențele; debifarea pornește dezinstalarea, după confirmarea din fereastra **Dezinstalați modulele** (se văd modulele și datele afectate).
- Pentru stocuri se alege un singur pachet de valorizare (CMP sau FIFO): cele două se exclud, iar Odoo oprește instalarea cu mesajul de module incompatibile.
- Instalările și dezinstalările nu se combină într-o singură salvare: când există o debifare, Odoo deschide doar fereastra de dezinstalare, iar modulele bifate nou nu se instalează.
- Modulele `auto_install` (punți între alte două module) nu apar în listă; se activează singure când ambele module conexe sunt prezente.
- Fiecare setare are text de ajutor cu rolul modulului asociat.

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extindere, tranzient): câmpuri booleene `module_<nume_modul>`, câte unul pentru fiecare modul instalabil al suitei; bifarea/debifarea declanșează instalarea/dezinstalarea prin mecanismul standard Odoo de setări.

**Vizualizări**

- `wizard/res_config_settings_views.xml`: extinde formularul de setări cu aplicația **România Enterprise**, organizată pe blocuri de categorii, cu câte o setare per modul.

**Securitate**

- `security/ro_ent_menus_group.xml`: grupul **Meniuri România Enterprise**, care controlează vizibilitatea paginii; membru implicit administratorul.


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

- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md)
- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md)
- [l10n_ro_efactura_import_assist](../l10n_ro_efactura_import_assist/index.md)
- [l10n_ro_esigiliu](../l10n_ro_esigiliu/index.md)
- [l10n_ro_etransport_block](../l10n_ro_etransport_block/index.md)

**Contabilitate & Închidere de Lună**

- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md)
- [l10n_ro_account_correspondence](../l10n_ro_account_correspondence/index.md)
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
- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md)
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
- [l10n_ro_excise_duty](../l10n_ro_excise_duty/index.md)
- [l10n_ro_grants](../l10n_ro_grants/index.md)
- [l10n_ro_oss_threshold](../l10n_ro_oss_threshold/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)

**Conformitate & Audit**

- [l10n_ro_audit_immutable](../l10n_ro_audit_immutable/index.md)
- [l10n_ro_sod_matrix](../l10n_ro_sod_matrix/index.md)

**Puncte de Vânzare (POS)**

- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md)
- [l10n_ro_sale_receipt_type_report](../l10n_ro_sale_receipt_type_report/index.md)
