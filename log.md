# Odoo Modules Wiki - Log

This is an append-only log of all operations performed on the wiki.

---

## [2026-06-01] Ingestie module tracking eCommerce (bitshop)

- **Acțiune:** Adăugate 3 pagini noi pentru suita de tracking eCommerce migrată la 19.0: `terrabit_website_sale_tracking_base`, `terrabit_facebook_pixel`, `terrabit_tiktok_pixel`.
- **Sursă:** `readme/DESCRIPTION.md` + `readme/USAGE.md` pentru Sumar și Funcționalități; analiza codului (models/controllers/JS) pentru Componente Cheie. Textul a fost corectat la realitatea 19.0 (framework Interactions, evenimente normalizate `terrabit_tracking:*`), nu copiat din referințele „Odoo 18" rămase în DESCRIPTION.
- **Dependențe/Conexiuni:** link-uri Markdown active între cele 3 module; `website_sale`/`crm` rămân text `cod` (fără pagină wiki).
- **Fișiere actualizate:** cele 3 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-01] Convenție link-uri active + actualizare schema

- **Acțiune:** Convertit link-urile de Dependențe/Conexiuni din format wikilink `[[module]]` în **link-uri Markdown active** relative (`[module](../module/index.md)`) pentru cele 4 pagini verificate (`l10n_ro_oss_threshold`, `l10n_ro_receivables_enhanced`, `l10n_ro_saft_validator`, `l10n_ro_vat_refund`).
- **Schema:** Actualizat `schema.md` (secțiunile 3. Dependențe și 5. Conexiuni) — de acum încolo link-urile către module cu pagină wiki se scriu ca link Markdown activ relativ; modulele fără pagină rămân ca text `cod`.
- **Fișiere actualizate:** `wiki_module_odoo/schema.md`, paginile celor 4 module, `wiki_module_odoo/log.md`.

---

## [2026-06-01] Adăugare DESCRIPTION.md + verificare 4 pagini

- **Acțiune:** Pentru cele 4 module care nu aveau `readme/DESCRIPTION.md` la ingestia în masă (`l10n_ro_oss_threshold`, `l10n_ro_receivables_enhanced`, `l10n_ro_saft_validator`, `l10n_ro_vat_refund`) am creat câte un `readme/DESCRIPTION.md` (proză + funcționalități cheie), derivat din `readme/FISA_CONSULTANT.md` și din cod/manifest.
- **Verificare pagini wiki:** Paginile generate anterior erau corecte în mare parte; am corectat secțiunea **Conexiuni** (ghicită greșit de agenți) și am completat lista de verificări la `l10n_ro_saft_validator` (6 tipuri în loc de 3), aliniind conținutul la noile `DESCRIPTION.md`.
- **Fișiere create:**
    - `odoo-addons/l10n_ro_ent/l10n_ro_oss_threshold/readme/DESCRIPTION.md`
    - `odoo-addons/l10n_ro_ent/l10n_ro_receivables_enhanced/readme/DESCRIPTION.md`
    - `odoo-addons/l10n_ro_ent/l10n_ro_saft_validator/readme/DESCRIPTION.md`
    - `odoo-addons/l10n_ro_ent/l10n_ro_vat_refund/readme/DESCRIPTION.md`
- **Fișiere actualizate:** paginile wiki ale celor 4 module și `wiki_module_odoo/log.md`.

---

## [2026-06-01] Ingestie în masă: 65 module `l10n_ro_ent`

- **Acțiune:** Corectat duplicatul `l10n_ro_advance_invoice` din `index.md` și ingestate toate cele 65 de module rămase din `odoo-addons/l10n_ro_ent`, conform `schema.md` și în română.
- **Detalii:** Procesare în paralel (4 grupuri). Pentru fiecare modul, pagina wiki a fost generată prioritizând `readme/DESCRIPTION.md` pentru Sumar și Funcționalități Cheie, iar `__manifest__.py` pentru metadate (nume prietenesc, versiune, dependențe). Pentru modulele fără DESCRIPTION.md (`l10n_ro_oss_threshold`, `l10n_ro_receivables_enhanced`, `l10n_ro_saft_validator`, `l10n_ro_vat_refund`) componentele au fost sintetizate din scanarea `models/`, `views/`, `wizard/`, `data/`. Tot textul este în română.
- **Module ingestate (65):** d100, d107, d112, d120, d205, d207, d300, d318, d390, d394, d394_pos, d398, anaf_partner, audit_immutable, cbam, currency_revaluation, deferred_entries, dividends, doc_screenshots, efactura_b2c, efactura_dedup, environmental_tax, etransport_block, excise, expense_allowance, expense_currency, financial_notes, financial_statements, fixed_assets, force_reconcile, grants, inventory_closing, inventory_items, inventory_register, invoice_dvi_protect, journal_reports, journal_tva, leasing, micro_tax, mrp_labour_account, oss_threshold, partner_ledger_currency, partner_screening, payment_instruments, payroll_import, period_close_enhanced, process_library, profit_tax, provisions, receivables_enhanced, reges, reports_fix, saft_validator, sgr, sod_matrix, stock_cmp_periodic, stock_constraints, stock_gestiune, stock_k_coefficient, stock_provision, vat_deductibility, vat_group, vat_refund, vat_regularization, wip_closing (toate cu prefix `l10n_ro_`).
- **Fișiere create:** 65 × `wiki_module_odoo/<module_name>/index.md`.
- **Fișiere actualizate:**
    - `wiki_module_odoo/index.md` (catalog reordonat alfabetic, duplicat eliminat)
    - `wiki_module_odoo/log.md`
- **Total module documentate în wiki:** 70.

---

## [2026-05-31] Re-ingest: `l10n_ro_anaf_base`

- **Acțiune:** Re-ingestat modulul `l10n_ro_anaf_base` conform noii scheme (cu cale locală și versiune) și în română.
- **Detalii:** Pagina wiki a fost generată/actualizată folosind `readme/DESCRIPTION.md` pentru sumar/funcționalități și componente cheie, și `__manifest__.py` pentru metadate. Tot textul este în română.
- **Fișiere actualizate:**
    - `wiki_module_odoo/l10n_ro_anaf_base/index.md`
    - `wiki_module_odoo/index.md`
    - `wiki_module_odoo/log.md`

---

## [2026-05-31] Ingest: `l10n_ro_advance_invoice`

- **Acțiune:** Ingestat modulul `l10n_ro_advance_invoice` conform noii scheme și în română.
- **Detalii:** Pagina wiki a fost generată folosind `readme/DESCRIPTION.md` pentru sumar/funcționalități și `__manifest__.py` și analiza minimă a structurii de fișiere pentru componente cheie. Tot textul este în română.
- **Fișiere create:**
    - `wiki_module_odoo/l10n_ro_advance_invoice/index.md`
- **Fișiere actualizate:**
    - `wiki_module_odoo/index.md`
    - `wiki_module_odoo/log.md`

---

## [2026-05-31] Ingest: `l10n_ro_account_return_pl_closing`

- **Acțiune:** Ingestat modulul `l10n_ro_account_return_pl_closing` conform noii scheme și în română.
- **Detalii:** Pagina wiki a fost generată folosind `readme/DESCRIPTION.md` pentru sumar/funcționalități și componente cheie, și `__manifest__.py` pentru metadate. Tot textul este în română.
- **Fișiere create:**
    - `wiki_module_odoo/l10n_ro_account_return_pl_closing/index.md`
- **Fișiere actualizate:**
    - `wiki_module_odoo/index.md`
    - `wiki_module_odoo/log.md`

---

## [2026-05-31] Re-ingest: `l10n_ro_account_fisa_cont`

- **Acțiune:** Re-ingestat modulul `l10n_ro_account_fisa_cont` conform noii scheme și în română.
- **Detalii:** Pagina wiki a fost generată folosind `readme/DESCRIPTION.md` pentru sumar/funcționalități și `__manifest__.py` și analiza minimă a structurii de fișiere pentru componente cheie, cu toate textele traduse în română.
- **Fișiere actualizate:**
    - `wiki_module_odoo/l10n_ro_account_fisa_cont/index.md`
    - `wiki_module_odoo/index.md`
    - `wiki_module_odoo/log.md`

---

## [2026-05-31] Re-ingest: `l10n_ro_account_chart`

- **Acțiune:** Re-ingestat modulul `l10n_ro_account_chart` conform noii scheme și în română.
- **Detalii:** Pagina wiki a fost generată folosind `readme/DESCRIPTION.md` pentru sumar/funcționalități și `__manifest__.py` și analiza minimă a structurii de fișiere pentru componente cheie, cu toate textele traduse în română.
- **Fișiere actualizate:**
    - `wiki_module_odoo/l10n_ro_account_chart/index.md`
    - `wiki_module_odoo/index.md`
    - `wiki_module_odoo/log.md`