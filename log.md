# Odoo Modules Wiki - Log

This is an append-only log of all operations performed on the wiki.

---

## [2026-06-01] Ingestie lot 2 suita deltatech (10 module)

- **Acțiune:** Adăugate încă 10 pagini noi pentru suita `deltatech` (repo `dhongu/deltatech`, branch `19.0`), al doilea lot din documentarea celor 119 module. Analiza delegată subagenților `general-purpose`, rulați în 2 sub-loturi paralele de câte 5: `deltatech_agreement_management`, `deltatech_dropshipping`, `deltatech_expenses`, `deltatech_invoice_picking`, `deltatech_mail`, `deltatech_product_labels`, `deltatech_purchase_price`, `deltatech_sale_commission`, `deltatech_stock_inventory`, `deltatech_website_sale_attributes`.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar și Funcționalități Cheie la toate; pentru `deltatech_agreement_management` (DESCRIPTION.md minimal) Componente Cheie ancorate în cod. Texte EN traduse în RO cu diacritice (`deltatech_invoice_picking`, `deltatech_business_process` etc.). Nicio referință de versiune veche de corectat în acest lot.
- **Dependențe/Conexiuni:** Prima dată apar **link-uri active între module deltatech**: `deltatech_sale_commission` → [deltatech_sale_margin](deltatech_sale_margin/index.md); `deltatech_stock_inventory` → [deltatech_stock_account](deltatech_stock_account/index.md). Restul dependențelor sunt module core sau module deltatech încă nedocumentate (ex: `deltatech_product_trade_markup`, `deltatech_partner_generic`), rămase text `cod`. Atenție diferențiere: dependența `stock_account` (core) ≠ `deltatech_stock_account` (deltatech) — nu s-a pus link greșit. Nicio conexiune inventată.
- **Fișiere actualizate:** cele 10 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-01] Ingestie lot pilot suita deltatech (10 module)

- **Acțiune:** Adăugate 10 pagini noi pentru suita `deltatech` (repo `dhongu/deltatech`, branch `19.0`), ca lot pilot al documentării celor 119 module deltatech. Analiza fiecărui modul a fost delegată unui subagent `general-purpose`, rulați în 2 loturi paralele de câte 5: `deltatech`, `deltatech_account`, `deltatech_business_process`, `deltatech_fast_sale`, `deltatech_mrp`, `deltatech_product_extension`, `deltatech_sale_margin`, `deltatech_stock_account`, `deltatech_warehouse_map`, `deltatech_website_delivery_and_payment`.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar și Funcționalități Cheie la toate modulele. Pentru `deltatech`, `deltatech_mrp`, `deltatech_business_process` și `deltatech_warehouse_map` secțiunea Componente Cheie a fost ancorată minimal în cod/manifest (DESCRIPTION.md aspirațional sau cu „data model at a glance"); restul au omis-o conform fluxului de ingestie. Texte reziduale de versiune veche corectate la 19.0: nota „In V18 is working in progress" din `deltatech_website_delivery_and_payment`; descrierea aspirațională a `deltatech` aliniată la realitatea codului.
- **Dependențe/Conexiuni:** Niciun modul `deltatech_*` nu avea încă pagină wiki, deci toate dependențele/conexiunile au rămas text `cod` (inclusiv module core: `account`, `stock`, `sale_margin`, `mrp`, `website_sale_stock` etc.). Nicio conexiune inventată; legăturile listate sunt verificate în cod/manifest.
- **Fișiere actualizate:** cele 10 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-01] Ingestie `terrabit_iap_server_sale` (test skill wiki-module)

- **Acțiune:** Adăugată pagina nouă `terrabit_iap_server_sale` (suita terrabit), prima ingestie rulată prin skill-ul `.claude/skills/wiki-module`, cu analiza modulului delegată unui subagent `general-purpose`.
- **Sursă:** `readme/DESCRIPTION.md` (complet) pentru Sumar și Funcționalități Cheie; conform fluxului de ingestie, secțiunea Componente Cheie a fost omisă (DESCRIPTION.md nu o solicită). Metadate din `__manifest__.py` (`19.0.1.0.0`).
- **Dependențe/Conexiuni:** `terrabit_iap_server` și `website_sale` rămân text `cod` (fără pagină wiki); nicio conexiune inventată.
- **Cale GitHub:** confirmată prin `git remote` — suita terrabit = `terrabit-ro/terrabit`, branch `19.0`; URL-ul `terrabit-ro/terrabit/tree/19.0/terrabit_iap_server_sale` este corect. Heading-urile de secțiune corectate post-subagent de la `##` la `####` pentru consistență cu schema.
- **Fișiere actualizate:** `wiki_module_odoo/terrabit_iap_server_sale/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

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