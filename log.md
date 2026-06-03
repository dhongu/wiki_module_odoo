# Odoo Modules Wiki - Log

This is an append-only log of all operations performed on the wiki.

---

## [2026-06-03] Ingestie module diverse + finalizare suita bitshop (19 module)

- **Acțiune:** Adăugate 19 pagini noi pentru suita `bitshop` (repo `terrabit-ro/bitshop`, branch `19.0`) — ultimele module nedocumentate (singletoni + perechi mici), încheind documentarea celor 79 module bitshop. `deltatech_restrict_ip` documentat separat (intrare proprie de log de mai jos). Analiza delegată subagenților `general-purpose` în 3 loturi paralele de 7: (A) `deltatech_access`, `deltatech_barcode_sale`, `deltatech_brand_field`, `deltatech_chart_of_accounts`, `deltatech_chatter`, `deltatech_cmr_document`, `deltatech_document_template`; (B) `deltatech_event`, `deltatech_mentor`, `deltatech_nap`, `deltatech_nap_website`, `deltatech_partner_gifts`, `deltatech_product_brand` (+ restrict_ip); (C) `deltatech_sale_cancel_order`, `deltatech_sale_contracts`, `deltatech_sale_store`, `deltatech_website_watermark`, `deltatech_work_days_report`, `terrabit_partner_credit_limit`, `terrabit_partner_payable_receivable`.
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie; Componente Cheie ancorate ușor în cod doar unde DESCRIPTION o cerea explicit (`deltatech_chart_of_accounts` — `sync.chart.of.accounts`/`import.chart.of.accounts`, postare diferențe cu storno; `deltatech_chatter` — assets frontend split.js; `deltatech_document_template`). Texte EN traduse în RO cu diacritice.
- **Confirmări de denumire (verificate în cod/manifest):** `deltatech_mentor` = export către **WinMentor** (complementar lui `deltatech_saga`/`deltatech_contwin`); `deltatech_nap` = „Need and Availability Planning" (planificare necesar achiziții), NU listă de prețuri; `deltatech_chart_of_accounts` confirmat ca modul de migrare/corecție solduri inițiale (vezi nota de migrare existentă). `deltatech_sale_store` = vânzare cu bon fiscal din magazin (ECR).
- **Dependențe/Conexiuni:** Lanțuri reale: `deltatech_nap` ← `deltatech_nap_website`; `terrabit_partner_payable_receivable` ← `terrabit_partner_credit_limit` (link intern activat la consolidare). Conexiuni cu pagină existentă: `deltatech_product_brand` ↔ `deltatech_marketplace_brand` (dependență reală) și ↔ `deltatech_brand_field`; `deltatech_brand_field` → `deltatech_feed` (folosește câmpul de marcă); `deltatech_mentor`/`deltatech_chart_of_accounts` → `deltatech_contact`. Dependențe rămase text `cod`: `deltatech_watermark` (bază pentru website_watermark, nedocumentat), `deltatech_record_type`, `account_payment`, `sale_management`, `portal`, `hr`/`hr_holidays`, `event`, `contacts`, core diverse.
- **Avertismente notabile (cod/readme, nu wiki):** `deltatech_access` DESCRIPTION menționează „Odoo 17.0" (versiune veche în readme, cod e 19.0); `deltatech_product_brand` are nume „- Temp" în manifest + inconsecvență licență (OPL-1 manifest vs AGPL-3 antet, origine OCA); `deltatech_work_days_report` DESCRIPTION zice 18.0 (manifest 19.0); multe module Beta/OPL-1 comerciale (`access`, `barcode_sale`, `sale_cancel_order` 100 EUR, `restrict_ip`, `event` Alpha). `deltatech_website_watermark` depinde de `deltatech_watermark` (nedocumentat — candidat viitor).
- **Fișiere actualizate:** cele 19 `index.md` noi, link intern activat în `terrabit_partner_credit_limit`, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie deltatech_restrict_ip (suita bitshop)

- **Acțiune:** Adăugată o pagină nouă pentru modulul `deltatech_restrict_ip` (repo `terrabit-ro/bitshop`, branch `19.0`). Modul mic, documentat direct (fără subagent).
- **Sursă:** `readme/DESCRIPTION.md` (prezent) pentru Sumar și Funcționalități Cheie; Componente Cheie omise conform prioritizării Readme. Text EN tradus în RO cu diacritice.
- **Dependențe/Conexiuni:** singura dependență din manifest este `base` (fără pagină wiki → text `cod`). Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki.
- **Avertismente notabile (cod/manifest, nu wiki):** modul comercial OPL-1 (15 EUR), `development_status: Beta`. Cod sursă neanalizat (modele `res.users`, `res.users.log`, `res.user.ip`, `ir.http` prezente, dar nedetaliate datorită prioritizării Readme).
- **Fișiere actualizate:** `wiki_module_odoo/deltatech_restrict_ip/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

## [2026-06-03] Ingestie partner_rating + POS + export contabil suita bitshop (7 module)

- **Acțiune:** Adăugate 7 pagini noi pentru suita `bitshop` (repo `terrabit-ro/bitshop`, branch `19.0`) — al cincilea lot, trei grupuri mici. Analiza delegată la 7 subagenți `general-purpose` într-un singur lot paralel: rating parteneri (`deltatech_partner_rating` bază, `deltatech_partner_rating_sale`, `deltatech_partner_rating_service`), POS-ECR (`deltatech_pos_base` bază, `deltatech_pos`), export contabil RO (`deltatech_saga`, `deltatech_contwin`).
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate; la `deltatech_saga` și `readme/USAGE.md`) pentru Sumar și Funcționalități Cheie; Componente Cheie omise conform prioritizării Readme. Texte EN traduse în RO cu diacritice.
- **Confirmări:** `deltatech_contwin` exportă către **ContWin** (Omnidata/Petrescu), formate `.fis` + SAF-T — NU WinMentor (acela e alt modul al suitei). `deltatech_pos`/`deltatech_pos_base` sunt integrare POS↔casă de marcat fiscală (ECR), nu POS generic.
- **Dependențe/Conexiuni:** Lanțuri reale: `deltatech_partner_rating` (bază) ← `_sale`, `_service` (link-uri active). `deltatech_pos_base` ← `deltatech_pos`. `deltatech_saga` ↔ `deltatech_contwin` (module de export contabil înrudite, link activ bidirecțional). `deltatech_contact` (pagină existentă) e dependență la saga/contwin → link activ. Dependențe core/service rămase text `cod`: `point_of_sale`, `account`, `stock`, `purchase_stock`, `sale_stock`, `l10n_ro`, `mail`, `contacts`, `deltatech_service_*`. Dep. externe Python notate: `xlwt`/`dicttoxml`/`unidecode` (SAGA).
- **Avertismente notabile (cod/readme, nu wiki):** `deltatech_partner_rating` are funcție „Todo" (evaluare automată pe sumă facturată) neimplementată; `deltatech_partner_rating_service` e Beta/OPL-1 (10 EUR); la `deltatech_pos` mai multe fișiere `data` sunt comentate în manifest (config/dashboard/wizard pos_box dezactivate); `nexterp_base_module` comentat în pos_base.
- **Fișiere actualizate:** cele 7 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie familii „EDI" + „vendor_products" suita bitshop (7 module)

- **Acțiune:** Adăugate 7 pagini noi pentru suita `bitshop` (repo `terrabit-ro/bitshop`, branch `19.0`), două familii mici — al patrulea lot. Analiza delegată la 7 subagenți `general-purpose` într-un singur lot paralel: EDI (`deltatech_edi` bază, `deltatech_ediconnect`, `deltatech_edinet`) și cataloage furnizori (`deltatech_vendor_products` bază, `deltatech_vendor_products_granit`, `deltatech_vendor_products_kramp`, `deltatech_vendor_products_website`).
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie; Componente Cheie ancorate ușor în manifest/cod unde DESCRIPTION era sumar (`deltatech_edi` — hooks `account.move` + QWeb invoice, conform CLAUDE.md; `deltatech_ediconnect`/`deltatech_edinet` — cron + view config). Texte EN traduse în RO cu diacritice.
- **Lanțuri de dependențe (verificate în manifest):** EDI: `deltatech_edi` (bază) ← `deltatech_ediconnect` (platforma EDIConnect, dep. externe `zeep`+`xmltodict`) și ← `deltatech_edinet` (platforma Infinite EDINET). Vendor: `deltatech_vendor_products` (bază) ← `deltatech_vendor_products_website` ← `deltatech_vendor_products_granit` și `deltatech_vendor_products_kramp` (conectorii pe furnizor specific depind de `_website`, NU direct de bază — corectat la consolidare: link-urile `_website` din granit/kramp activate după ce pagina `_website` a fost creată).
- **Dependențe/Conexiuni rămase text `cod`:** core `product`, `purchase`, `stock`, `purchase_stock`, `sale_stock`, `account`, `website_sale`. `deltatech_gln` (pagină existentă) linkat la `deltatech_edi`. Dep. externe Python notate: `zeep`/`xmltodict` (ediconnect), `psutil` (vendor_products_website).
- **Avertismente notabile (cod/readme, nu wiki):** `deltatech_edi`, `deltatech_ediconnect` (250 EUR) sunt comerciale OPL-1; `deltatech_edi` README.rst auto-generat ignorat ca sursă; componentele tehnice EDI (hooks exacte pe `account.move`, QWeb) nedetaliate — candidat de re-ingestie cu analiză de cod dacă se dorește.
- **Fișiere actualizate:** cele 7 `index.md` noi, link-uri interne activate în `deltatech_vendor_products_granit`/`_kramp`, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie familia „plăți" suita bitshop (6 module)

- **Acțiune:** Adăugate 6 pagini noi pentru suita `bitshop` (repo `terrabit-ro/bitshop`, branch `19.0`), familia de plăți — al treilea lot din modulele bitshop nedocumentate. Analiza delegată la 6 subagenți `general-purpose` rulați într-un singur lot paralel: `deltatech_payment`, `deltatech_payment_card_dummy`, `deltatech_payment_libra_pay`, `deltatech_payment_mobilpay`, `deltatech_payment_on_delivery`, `deltatech_payment_revolut`.
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie; Componente Cheie omise conform prioritizării Readme. Texte EN traduse în RO cu diacritice.
- **Corecție de premisă (importantă):** `deltatech_payment` NU este modulul de bază al familiei (cum presupunea prompt-ul) — e o personalizare mică ce extinde `payment.transaction` pentru a confirma comanda de vânzare la plată parțială (parametru `payment.do_not_set_transaction_done`). Gateway-urile (`libra_pay`, `mobilpay`, `revolut`, `card_dummy`, `on_delivery`) NU depind de el — depind direct de `payment`/`website_sale`/`payment_custom` core. Subagenții au evitat corect să-l adauge ca dependență falsă; apare doar la Conexiuni („familie de module") unde are pagină.
- **Dependențe/Conexiuni:** Dependențe core rămase text `cod`: `payment`, `website_sale`, `sale`, `account`, `delivery`, `payment_custom`. Conexiune reală cu pagină: `deltatech_delivery` (la `deltatech_payment_on_delivery`, COD), `deltatech_website_delivery_and_payment` (la `deltatech_payment`). Dependențe externe Python notate: `pyjwt`+`netopia-sdk` (mobilPay), `phpserialize` (LibraPay).
- **Avertismente notabile (cod/readme, nu wiki):** `deltatech_payment` are typo în `summary` din manifest („Deltatech Paymentr"); `deltatech_payment_revolut` și unele gateway-uri sunt `Beta`/OPL-1 (comerciale, preț listat); USAGE.md la `revolut` are capturi pe terminologia veche „Payment Acquirer" (v15). `libra_pay` are `post_init_hook`/`uninstall_hook` și controller IPN.
- **Fișiere actualizate:** cele 6 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie familia „marketplace/integrări" suita bitshop (18 module)

- **Acțiune:** Adăugate 18 pagini noi pentru suita `bitshop` (repo `terrabit-ro/bitshop`, branch `19.0`), familia marketplace — al doilea lot din cele 79 module bitshop nedocumentate (`deltatech_feed` documentat separat de propriul subagent). Analiza delegată subagenților `general-purpose`, rulați în 3 sub-loturi paralele (6 + 6 + 6): nucleu (`deltatech_marketplace` bază, `deltatech_marketplace_extended`, `_sale`, `_purchase`, `_payment`, `_delivery`); conectori platforme (`deltatech_marketplace_emag`, `_magento`, `_prestashop`, `_shopify`, `_opencart`, `_merchantpro`); restul (`deltatech_marketplace_website`, `_odoo`, `_doraly`, `_brand`, `_sale_stage`, `_sale_type`).
- **Sursă:** `readme/DESCRIPTION.md` (prezent la majoritatea) pentru Sumar și Funcționalități Cheie; Componente Cheie ancorate în cod doar unde DESCRIPTION era gol/sumar (`deltatech_marketplace_extended` — DESCRIPTION aproape gol, doar link Swagger; `_purchase`, `_payment`) sau menționa explicit cron-uri. Texte EN/RST traduse în RO cu diacritice.
- **Dependențe/Conexiuni:** `deltatech_marketplace` (bază) e referit ca link activ de toți conectorii. Lanț: conectorii de platformă depind de `deltatech_marketplace_sale`/`_payment`/`_delivery` (toate au pagini → link-uri active). `deltatech_delivery` și `deltatech_delivery_status` (familia delivery, deja documentate) apar la `deltatech_marketplace_delivery`. Dependențe core (`sale`, `sale_stock`, `stock_delivery`, `purchase_stock`, `payment`, `website_sale`, `queue_job`, `base_address_extended`) rămase text `cod`. Module bitshop încă nedocumentate rămase text `cod`: `deltatech_marketplace_website` (la momentul scrierii unor conectori — acum are pagină), `deltatech_product_brand`, `deltatech_sale_stage`, `deltatech_record_type`. Dependențe externe Python notate: `dicttoxml` (PrestaShop).
- **Avertismente notabile (cod/readme, nu wiki):** `deltatech_marketplace_extended` are DESCRIPTION.md aproape gol (doar referințe Swagger) — de completat de echipă; `deltatech_marketplace_magento` are neconcordanță status (DESCRIPTION „Alpha" vs manifest „Production/Stable"); `deltatech_marketplace_doraly` e `Alpha` cu `data: []` (niciun XML încărcat) și export produse/comenzi parțial sau neimplementat; cron-urile de import (`ir_cron_marketplace_get_order`, `_get_purchase_order`) sunt livrate `active=False` și trebuie activate manual; `cron_import_purchase_orders` are corp gol (placeholder).
- **Corecții post-subagent:** Subagenții au evitat corect includerea `deltatech_marketplace_purchase` ca dependență acolo unde nu figura în manifest (eMAG, Magento, Shopify, OpenCart, MerchantPro) — pus la Conexiuni unde era cazul, nu inventat ca dependență.
- **Fișiere actualizate:** cele 18 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie `deltatech_feed` (suita bitshop)

- **Acțiune:** Adăugată o pagină nouă pentru modulul `deltatech_feed` (repo `terrabit-ro/bitshop`, branch `19.0`), generator de feed-uri de produse pentru platforme de e-commerce și marketing.
- **Sursă:** `readme/DESCRIPTION.md` (prezent) pentru Sumar și Funcționalități Cheie; text EN tradus în RO cu diacritice. Componente Cheie completate ușor pe baza secțiunii „Technical Implementation" din DESCRIPTION, coroborată cu structura `models/`, `views/`, `controllers/` și cron-ul din `data/ir_cron_data.xml`.
- **Dependențe/Conexiuni:** Toate cele 5 dependențe rămase text `cod` — niciuna nu are pagină wiki (`product`, `website_sale_stock`, `deltatech_brand_field`, `deltatech_product_list`, `deltatech_website_short_description`). Conexiuni funcționale reale notate către `deltatech_product_list` (model liste produse), `deltatech_brand_field` (câmp brand în feed), `deltatech_website_short_description` (descriere scurtă) și `website_sale_stock` (stoc eCommerce) — toate fără pagină wiki încă.
- **Observații:** DESCRIPTION.md menționează ca dezvoltare viitoare platforme suplimentare (Shopmania.ro, Price.ro, Compara-pret.ro, Cauti.ro) — nereflectate ca funcționalități curente. Cron `ir_cron_regenerate_feed` rulează zilnic `product.list._cron_refresh_feed()`.
- **Fișiere actualizate:** `wiki_module_odoo/deltatech_feed/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie familia „livrare/curierat" suita bitshop (20 module)

- **Acțiune:** Adăugate 20 pagini noi pentru suita `bitshop` (repo `terrabit-ro/bitshop`, branch `19.0`), întreaga familie de livrare/curierat — primul lot din cele 79 module bitshop nedocumentate. Analiza delegată subagenților `general-purpose`, rulați în 3 sub-loturi paralele (6 + 6 + 8): bază/generice (`deltatech_delivery`, `deltatech_delivery_relay`, `deltatech_delivery_locker`, `deltatech_delivery_locker_website`, `deltatech_delivery_send_mail`, `deltatech_delivery_send_sms`); integrări curieri 1 (`deltatech_delivery_dpd`, `deltatech_delivery_gls`, `deltatech_delivery_dsc`, `deltatech_delivery_packeta`, `deltatech_delivery_sd`, `deltatech_delivery_sd_easybox`); integrări curieri 2 + transport/staff (`deltatech_delivery_cm`, `deltatech_delivery_fc`, `deltatech_delivery_memex`, `deltatech_delivery_pr`, `deltatech_delivery_uc`, `deltatech_delivery_transport`, `deltatech_delivery_dummy`, `terrabit_delivery_staff`).
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie; Componente Cheie omise conform prioritizării Readme, cu excepția câtorva unde DESCRIPTION era sumar (`deltatech_delivery_locker`, `deltatech_delivery_gls`, `deltatech_delivery_dummy`). Texte EN traduse în RO cu diacritice.
- **Confirmări coduri curieri (verificate în cod/manifest, nu ghicite):** CM = **Courier Manager** (NU Cargus, cum sugera prompt-ul), FC = Fan Courier, SD = Sameday, UC = Urgent Cargus, PR = **Poșta Română**, DSC = Dragon Star Curier, Memex = PTT Express, Packeta = Zásilkovna.
- **Dependențe/Conexiuni:** `deltatech_delivery` (modul de bază al familiei) primește pagină și e referit ca link activ de aproape toate integrările. `deltatech_delivery_status` (pagină preexistentă) apare la Conexiuni pe majoritatea curierilor. Lanț locker: `deltatech_delivery_locker` ← `deltatech_delivery_locker_website` ← `deltatech_delivery_sd_easybox`. Dependențe core (`delivery`, `sale`, `stock`, `mail`, `sms`, `website_sale`, `purchase`, `base_address_extended`) rămase text `cod`. Dependențe externe Python notate în pagini: `zeep` (GLS/Packeta/Memex), `googlemaps` (transport), `phonenumbers` (DSC).
- **Avertismente notabile (cod/readme, nu wiki):** `deltatech_delivery_sd_easybox` are `installable: False` în manifest — frontend JS încă pe API Odoo 18 (`WebsiteSale.include`), dezactivat până la migrarea la Interactions; multe module de curier sunt `development_status: Beta` cu licență OPL-1 (`extra_buy`); `terrabit_delivery_staff` are notă „de verificat după migrare".
- **Fișiere actualizate:** cele 20 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-02] Re-ingestie 2 module l10n_ro_ent (gestiuni stoc + reevaluare valutară)

- **Acțiune:** Actualizate (re-ingestie) 2 pagini existente din suita `l10n_ro_ent` (repo `terrabit-ro/l10n_ro_ent`, branch `19.0`), regenerate complet după extinderi majore de cod: `l10n_ro_stock_gestiune` (adăugată recepția fără factură 371=408) și `l10n_ro_currency_revaluation`. Analiza delegată la 2 subagenți `general-purpose` rulați în paralel.
- **Sursă:** `readme/DESCRIPTION.md` (actualizat la ambele) pentru Sumar și Funcționalități Cheie; Componente Cheie ancorate în cod (`models/`, `wizard/`, `views/`) fiindcă DESCRIPTION nu acoperea exhaustiv partea tehnică. La `l10n_ro_currency_revaluation` titlurile au fost convertite din `##` în `####` și wikilink-urile `[[...]]` invalide rescrise ca link-uri Markdown active.
- **Dependențe/Conexiuni:** Dependențele ambelor (`account`, `stock_account`, `deltatech_valuation_area`, `l10n_ro`, `account_reports`) rămân text `cod` — niciuna nu are pagină wiki (notabil: `deltatech_valuation_area`, coloana vertebrală a `l10n_ro_stock_gestiune`). Conexiune funcțională reală activată bidirecțional: `l10n_ro_stock_gestiune` ↔ `l10n_ro_currency_revaluation` (diferențele de curs pe contul 408 din recepția fără factură se reevaluează ca element monetar). Pentru reevaluare, conexiuni active și către `l10n_ro_expense_currency` și `l10n_ro_period_close_enhanced`.
- **Corecții post-subagent:** La `l10n_ro_currency_revaluation` eliminată conexiunea anterioară speculativă către `l10n_ro_deferred_entries` (nu e legătură funcțională reală pentru reevaluare).
- **Observații:** `deltatech_valuation_area` rămâne nedocumentat în wiki, deși e dependență-cheie pentru gestiuni — candidat de ingestie viitoare.
- **Fișiere actualizate:** `wiki_module_odoo/l10n_ro_stock_gestiune/index.md`, `wiki_module_odoo/l10n_ro_currency_revaluation/index.md`, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-02] Ingestie lot 5 suita deltatech (10 module)

- **Acțiune:** Adăugate 10 pagini noi pentru suita `deltatech` (repo `dhongu/deltatech`, branch `19.0`), al cincilea lot din documentarea celor 119 module (rămân 69 nedocumentate). Analiza delegată subagenților `general-purpose`, rulați în 2 sub-loturi paralele de câte 5: `deltatech_gln`, `deltatech_invoice_picking_automatically`, `deltatech_invoice_product_filter`, `deltatech_invoice_receipt`, `deltatech_invoice_weight`, `deltatech_ledger`, `deltatech_list_view`, `deltatech_logistic_docs`, `deltatech_mrp_concentration`, `deltatech_mrp_cost`.
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie; Componente Cheie ancorate în cod doar unde DESCRIPTION.md era prea sumar (`deltatech_invoice_product_filter`, `deltatech_invoice_receipt`, `deltatech_mrp_cost`) sau menționa explicit elemente (`deltatech_invoice_picking_automatically` — cron). Texte EN/scurte traduse/extinse în RO cu diacritice. Nicio referință de versiune veche de corectat în paginile produse.
- **Dependențe/Conexiuni:** Link-uri active de conexiune (nu dependențe stricte) către module deltatech existente: `deltatech_invoice_picking_automatically`, `deltatech_invoice_receipt`, `deltatech_logistic_docs` → [deltatech_invoice_picking](deltatech_invoice_picking/index.md); `deltatech_mrp_concentration` și `deltatech_mrp_cost` → [deltatech_mrp](deltatech_mrp/index.md). Restul dependențelor sunt module core (`account`, `stock`, `sale`, `purchase_stock`, `mrp_account`, `web`, `base`, `mail`), rămase text `cod`. Atenție diferențiere: dependența `mrp` (core) ≠ `deltatech_mrp`.
- **Corecții post-subagent:** La `deltatech_mrp_cost` subagentul adăugase 2 conexiuni speculative („deduse pe baza modelelor comune": `l10n_ro_mrp_labour_account`, `deltatech_stock_account`) — eliminate la consolidare; păstrat doar `deltatech_mrp` (legătură reală, ambele extind `mrp.production`).
- **Observații (candidate de corecție în readme-uri/cod, nu în wiki):** `deltatech_gln` marcat „Obsolet" în DESCRIPTION dar `development_status=Mature` în manifest (inconsecvent); `deltatech_ledger` are comentariu de antet învechit („version 16.0", typo „Dealtatech") și `development_status=Alpha`.
- **Fișiere actualizate:** cele 10 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-02] Ingestie lot 4 suita deltatech (10 module)

- **Acțiune:** Adăugate 10 pagini noi pentru suita `deltatech` (repo `dhongu/deltatech`, branch `19.0`), al patrulea lot din documentarea celor 119 module (rămân 79 nedocumentate). Analiza delegată subagenților `general-purpose`, rulați în 2 sub-loturi paralele de câte 5: `deltatech_category_group`, `deltatech_contact`, `deltatech_credentials`, `deltatech_data_sheet`, `deltatech_data_sheet_website`, `deltatech_dc`, `deltatech_delivery_status`, `deltatech_download`, `deltatech_fast_purchase`, `deltatech_followup`.
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie; secțiunea Componente Cheie omisă conform fluxului, cu mențiuni minime de cod doar unde DESCRIPTION.md era prea sumar (`deltatech_credentials` — DESCRIPTION de o linie, completat din `models/access_credentials.py`). Texte EN traduse în RO cu diacritice. Nicio referință de versiune veche de corectat.
- **Dependențe/Conexiuni:** Link-uri active între module deltatech: `deltatech_data_sheet_website` → [deltatech_data_sheet](deltatech_data_sheet/index.md) (dependență + conexiune, activat post-lot fiindcă ambele s-au documentat în paralel); `deltatech_category_group` → [deltatech_sale_commission](deltatech_sale_commission/index.md) (dependență) și [deltatech_sale_margin](deltatech_sale_margin/index.md) (conexiune raport marjă); `deltatech_fast_purchase` → [deltatech_fast_sale](deltatech_fast_sale/index.md) (conexiune, modul analog). Restul dependențelor sunt module core, rămase text `cod`. Nicio conexiune inventată.
- **Observații (candidate de corecție în readme-uri, nu în wiki):** `deltatech_data_sheet` are notă „TODO: de utilizat funcționalitatea standard" (autor marchează modulul ca posibil înlocuibil cu standard Odoo); `deltatech_followup` are `development_status = Alpha`; `deltatech_fast_purchase` typo „repetition" pentru „reception" (recepție) în DESCRIPTION; `deltatech_dc` are dependența `stock_picking_invoice_link` comentată (nu activă).
- **Fișiere actualizate:** cele 10 `index.md` noi, `wiki_module_odoo/deltatech_data_sheet_website/index.md` (link activat), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-02] Ingestie lot 3 suita deltatech (10 module)

- **Acțiune:** Adăugate 10 pagini noi pentru suita `deltatech` (repo `dhongu/deltatech`, branch `19.0`), al treilea lot din documentarea celor 119 module (rămân 89 nedocumentate). Analiza delegată subagenților `general-purpose`, rulați în 2 sub-loturi paralele de câte 5: `deltatech_actions`, `deltatech_alternative`, `deltatech_alternative_website`, `deltatech_analytic_distribution`, `deltatech_auto_reorder_rule`, `deltatech_average_payment_period`, `deltatech_backup_attachment`, `deltatech_batch_transfer`, `deltatech_business_process_handover_document`, `deltatech_cash_statement`.
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie. Componente Cheie ancorate minimal în cod doar unde DESCRIPTION.md o cere explicit: `deltatech_actions` (cron-uri + `force_cancel_order_and_moves`), `deltatech_auto_reorder_rule` (acțiuni server `create_rule()`), `deltatech_business_process_handover_document` (acțiune raport PDF); restul au omis secțiunea conform fluxului. Texte EN traduse în RO cu diacritice. Nicio referință de versiune veche de corectat.
- **Dependențe/Conexiuni:** Singurul link activ între module deltatech: `deltatech_business_process_handover_document` → [deltatech_business_process](deltatech_business_process/index.md) (dependență + conexiune reală). `deltatech_alternative_website` → `deltatech_alternative` (conexiune reală, dar fără pagină wiki încă → text `cod`). Restul dependențelor sunt module core (`account`, `stock`, `sale`, `purchase`, `web`, `base`, `stock_picking_batch` etc.), rămase text `cod`. Nicio conexiune inventată.
- **Observații:** `deltatech_business_process_handover_document` are readme numit `Description.md` (D mare), tratat ca echivalent `DESCRIPTION.md`. Avertismente de readme nepropagate în cod (candidate de corecție în readme-uri, nu în wiki): `deltatech_alternative` typo `product_catelog`; `deltatech_auto_reorder_rule` menționează `type='product'` (în O19: `consu`+`is_storable`).
- **Fișiere actualizate:** cele 10 `index.md` noi, `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-02] Ingestie `l10n_ro_stock_sheet`

- **Acțiune:** Adăugată pagină nouă pentru modulul `l10n_ro_stock_sheet` (suita `l10n_ro_ent`, repo `terrabit-ro/l10n_ro_ent`, branch `19.0`). Analiza a fost delegată unui subagent `general-purpose` izolat.
- **Sursă:** `readme/DESCRIPTION.md` (prezent și complet) pentru Sumar și Funcționalități Cheie. DESCRIPTION.md menționează explicit modele/vizualizări/meniu, deci secțiunea Componente Cheie a fost completată și verificată în cod (`models/`, `data/stock_sheet_report.xml`, `views/`): handler `l10n.ro.stock.sheet.report.handler` (moștenește `account.report.custom.handler`), raport `account.report` `l10n_ro_stock_sheet_report`, acțiune client `action_l10n_ro_stock_sheet`, `menu_l10n_ro_stock_sheet`. Versiunea `19.0.1.0.0` corectă, fără text de versiune veche de corectat.
- **Dependențe/Conexiuni:** Dependențele din manifest (`account_reports`, `stock_account`, `l10n_ro`) nu au pagină wiki — rămase text `cod`. La Conexiuni, linkuri active reale verificate către [l10n_ro_stock_cmp_periodic](l10n_ro_stock_cmp_periodic/index.md) și [l10n_ro_stock_k_coefficient](l10n_ro_stock_k_coefficient/index.md); `l10n_ro_stock_account` (fără pagină wiki) rămas text `cod`. Nicio conexiune inventată.
- **Fișiere actualizate:** `wiki_module_odoo/l10n_ro_stock_sheet/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-01] Re-ingestie `deltatech_expenses` (clarificare vs. `hr_expense`)

- **Acțiune:** Actualizată pagina existentă `deltatech_expenses`. Adăugată o notă de clarificare în secțiunea Sumar privind diferența și coexistența cu modulul standard `hr_expense` (avans de trezorerie / cont 542 / diurnă vs. flux generic HR de rambursare). Restul paginii (Funcționalități, Dependențe, Componente, Conexiuni) rămâne neschimbat.
- **Sursă:** `readme/DESCRIPTION.md`, în care a fost adăugat în prealabil un tabel comparativ `deltatech_expenses` vs. `hr_expense`.
- **Dependențe/Conexiuni:** Nicio schimbare; `hr_expense` menționat doar ca text `cod` în notă (nu e dependență, nu are pagină wiki).
- **Fișiere actualizate:** `wiki_module_odoo/deltatech_expenses/index.md`, `wiki_module_odoo/log.md`. Sursă editată anterior: `odoo-addons/deltatech/deltatech_expenses/readme/DESCRIPTION.md`.

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