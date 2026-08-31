# Odoo Modules Wiki - Log

This is an append-only log of all operations performed on the wiki.

---

## [2026-08-31] Ingestie `l10n_ro_payment_allocation_report` (modul nou — tichet #9363 Damira)

- **Acțiune:** Pagină nouă pentru modulul `l10n_ro_payment_allocation_report` (`19.0.1.0.0`), creat în aceeași sesiune pornind de la tichetul #9363 (client Damira): contabilitatea cerea un raport din care să reiasă ce facturi reconciliază un ordin de plată, în special când o factură și un storno se sting cu o plată pentru diferență. Modulul adaugă două rapoarte native `account.report` — *Alocarea plăților* și *Stingerea facturilor* — construite pe `account.partial.reconcile`.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar/Funcționalități Cheie (conform schema.md), completat din `models/payment_allocation_report_handler.py` și `data/payment_allocation_report.xml` pentru Componente Cheie (handlerele nu sunt acoperite de DESCRIPTION).
- **Decizie de proiectare confirmată pe date de producție, nu pe teste:** sursa de date este `account.partial.reconcile`, **nu** `account.payment`. Măsurat pe baza Damira (august 2026): o singură `account.payment` de furnizor în trei luni, față de 269 stingeri prin note contabile din jurnalul bancar, 31 prin note de credit și 7 din registrul de casă. Un raport construit pe `account.payment` ar fi întors aproape gol în producție — eroare tăcută, nu excepție.
- **Trei capcane rezolvate în cod, toate ieșite din confruntarea cu date reale sau din audit:** (1) nota de credit este și ea document de stingere, iar un total naiv dădea 1.200 acolo unde din bancă ieșiseră 1.000 — de aici secțiunile cu subtotaluri; (2) reconcilierile POS și de stoc arată identic cu plățile (408 alocări `entry ⟷ entry` în jurnalele POS, 76 pe conturi de stoc într-o lună) — izolate în secțiune proprie, nu tăiate tăcut, iar filtrul pe conturi de terți se aplică **ambelor** laturi ale reconcilierii; (3) auditul `verificator-fisa` a prins că secțiunea „Plăți" adunase plăți către furnizori cu încasări de la clienți (4.500 lei față de 3.800 ieșiri + 700 intrări) — plățile și încasările au acum secțiuni și totaluri distincte, fiecare confruntabil cu rulajul care îi corespunde.
- **Fișă consultant:** copiată din `readme/FISA_CONSULTANT.md`, cu cele 6 capturi din `readme/screenshots/`, generate reproductibil din `tests/test_screenshots.py` (seed determinist relativ la luna curentă, fiindcă raportul se deschide implicit pe `this_month`). Fișa a trecut prin audit și a fost corectată pe 16 puncte, printre care: secțiunile prezentate ca „până la patru, fiecare doar dacă are conținut" (captura arăta două, fișa promitea trei), semantica nivelului 3 din raportul invers (alte facturi stinse de același OP, nu o compensare între facturi) și calea reală de meniu (**Facturare** în lipsa modulului *Accounting*, iar submeniul este „Rapoarte partener", la singular).
- **Traducere:** `i18n/ro.po` acoperă toate cele 21 de stringuri. Pentru `Open Balance` s-a folosit „Sold restant", nu „sold deschis" — „deschis"/„deschidere" sunt rezervate exercițiului financiar (cont 891, OMFP 1802/2014), iar confuzia a produs deja un tichet la un client. Verificat cu `scripts/i18n/po_lint_terms.py`.
- **Fișiere actualizate:** `l10n_ro_payment_allocation_report/index.md` (pagină nouă), `l10n_ro_payment_allocation_report/FISA_CONSULTANT.md`, `l10n_ro_payment_allocation_report/screenshots/*.png` (6 fișiere), `index.md` (1 intrare nouă), `log.md`.

## [2026-08-27] Re-ingestie `bitshop_sale_withdrawal` (PR #2773, #2774 — UX portal + traducere RO)

- **Acțiune:** Regenerare paginii `bitshop_sale_withdrawal` (versiune nouă `19.0.0.2.2`), după două PR-uri fuzionate pe tichetul #9251 (client Damira): PR #2773 a adăugat traducerea completă în română (`i18n/ro.po`, nu exista deloc înainte), a schimbat butonul de retragere din `btn-secondary` gri în `btn-primary` și a adăugat secțiunii un titlu propriu `<h3>Right of withdrawal</h3>`, care primește automat o ancoră proprie în navigarea rapidă (navspy) a portalului; PR #2774 a actualizat `readme/FISA_CONSULTANT.md` și a regenerat cele 7 capturi de ecran, plus a reparat garda `SkipTest` lipsă din `tests/test_screenshots.py` (fără ea, testul pica CI-ul cu `AttributeError` în loc să sară curat, din cauză că `l10n_ro_doc_screenshots` nu e dependență a repo-ului `bitshop`).
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar/Funcționalități Cheie (neschimbat), completat din analiza de cod (`views/portal_templates.xml`) pentru elementele funcționale noi (titlu + ancoră navspy, stil buton, traducere RO).
- **Fișă consultant:** resincronizată din `readme/FISA_CONSULTANT.md`, împreună cu cele 7 capturi din `readme/screenshots/`. Fișa notează explicit că interfața de portal din capturi rămâne în engleză (limitare a mediului de test — paginile `website=True` își aleg limba din website/cookie de limbă frontend, nu din `admin.lang`), deși codul are acum traducere RO funcțională (confirmată direct în `ir_ui_view.arch_db['ro_RO']`).
- **Fișiere actualizate:** `bitshop_sale_withdrawal/index.md` (regenerat), `bitshop_sale_withdrawal/FISA_CONSULTANT.md` (resincronizată), `bitshop_sale_withdrawal/screenshots/*.png` (7 fișiere), `index.md` (1 linie de descriere actualizată), `log.md`.

## [2026-08-26] Re-ingestie 7 conectori marketplace (fișe consultant + corecturi de audit)

- **Acțiune:** Regenerare completă a paginilor pentru toți cei 7 conectori marketplace activi din `odoo-addons/bitshop_marketplace` (branch `19.0`) — `deltatech_marketplace_shopify`, `_woocommerce`, `_prestashop`, `_magento`, `_emag`, `_trendyol`, `_merchantpro` — după fuziunea unei serii de PR-uri (#221, #226, #227, #229, #231, #232, #233) care a adăugat câte o fișă `readme/FISA_CONSULTANT.md` (11 secțiuni) cu capturi reale de ecran pentru fiecare modul. Procesate în paralel, 7 subagenți `documentarist-wiki` izolați.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar/Funcționalități (prioritizat conform schema.md), completat din `readme/FISA_CONSULTANT.md`/`readme/USAGE.md` pentru Componente Cheie și pentru corecturile funcționale de mai jos.
- **Corecturi funcționale importante, ieșite din procesul de audit (`verificator-fisa`) și reflectate acum în wiki, nu doar în fișe:**
  - **WooCommerce:** eliminat exportul de preț (inexistent în cod); exportul de stoc e pe cron dedicat, dezactivat implicit, nu „în timp real"; testul de conexiune validează acum efectiv credențialele (fix de cod separat, `system_status`).
  - **PrestaShop:** direcția webhook-ului e PrestaShop → Odoo (nu invers); wizard-ul real se numește „Marketplace sync" (nu „Update in Marketplace"); tracking-ul și legătura facturii se trimit necondiționat, doar statusul comenzii depinde de „Active On Write".
  - **Magento:** mecanismul real de export stoc e `magento_stock_export()` (bulk pe sursa MSI implicită), nu metoda `update_stock` menționată eronat anterior; eliminate „real-time stock sync" și „multi-warehouse" (nesusținute de cod).
  - **eMAG:** importul de localități RO are buton real „Get city"; „Safe stock" fără efect; nu există „Import All"; Auto Price cu Min/Max=0 trimite efectiv preț 0; comandă CANCELED nu se anulează automat; push factură trimite link, nu PDF; potrivire la import e EAN-câștigă-ultimul.
  - **Trendyol:** tracking-ul automat NU e necondiționat (depinde de transportator real cu integrare rate-and-ship); maparea automată a curierului Trendyol nu funcționează (cade mereu pe „Free delivery" — bug de cod semnalat separat); atributele de categorie nu au buton dedicat de import.
  - **MerchantPro:** nu există „Import All"; importul de produse nu leagă categoria (cod mort, bug semnalat separat); lista de prețuri a backend-ului NU e sursa prețului exportat (`list_price` al produsului e sursa reală); importul de comenzi filtrează pe `shipping_status` și nu recuperează comenzi noi ratate de webhook.
  - **Shopify:** pagina actualizată la versiunea curentă (`19.0.0.29.2`), cu wizard-ul „Check webhooks" documentat.
- **Fișă consultant:** copiată/resincronizată pentru toate cele 7 module (Shopify, PrestaShop, MerchantPro, Trendyol nu o aveau încă în wiki — copiată acum prima dată; WooCommerce, Magento, eMAG resincronizate) — total 34 capturi de ecran noi/actualizate.
- **Notă de proces:** repo-ul `bitshop_marketplace` e un working tree partajat cu sesiuni concurente de lucru pe alte task-uri; checkout-ul local era pe un branch de lucru (`19.0-merchantpro-fisa-consultant`) fără toate commit-urile — subagenții pentru Shopify, eMAG și Trendyol au extras conținutul direct din `origin/19.0` (via `git show`/`git archive`), fără să modifice working tree-ul local.
- **Bug-uri de cod descoperite în timpul auditului (semnalate separat, NEreparate în această re-ingestie):** WooCommerce (XML-ID mort la trigger export stoc, deja reparat separat), Magento (`parent_id` adresă nesalvat, cod mort în `backend_stock.py`), Trendyol (mapare curier eșuează mereu), MerchantPro (categorie nelegată la import, cron export stoc dezactivat implicit — framework comun), plus un typo („Currier Currency") în `deltatech_delivery`.
- **Fișiere actualizate:** 7× `<modul>/index.md`, 7× `<modul>/FISA_CONSULTANT.md` (copii noi/resincronizate), 34× `<modul>/screenshots/*.png`, `index.md` (7 linii de descriere actualizate), `log.md`.

## [2026-08-25] Re-ingestie `l10n_ro_pos_fiscal_compliance` (PR #110 — import arhivă Z)

- **Acțiune:** Regenerare completă a paginii (nu doar bump de versiune) după PR #110, merge-uit în `19.0`, care a dus modulul de la `19.0.1.0.0` la `19.0.2.0.0` cu o funcționalitate majoră nouă: import și reconciliere a arhivelor Z fiscale (`.zip` cu fișiere `.p7b`, export periodic AMEF semnat CMS/PKCS7).
- **Sursă:** `readme/DESCRIPTION.md` pentru sumarul funcționalității de bază (rămâne valid); `readme/DESCRIPTION.md` **nu fusese actualizat** cu noua funcționalitate din PR #110, deci secțiunile „Funcționalități Cheie" și „Componente Cheie" au fost completate manual din analiza codului (`models/l10n_ro_amef_journal.py`, `l10n_ro_amef_journal_bon.py`, `l10n_ro_amef_parser.py`, view-urile și securitatea) și din `readme/USAGE.md`/`FISA_CONSULTANT.md`.
- **Dependențe/Conexiuni:** dependențe manifest neschimbate (`point_of_sale`, `account`, `l10n_ro`, fără pagină wiki proprie) + dependență externă Python nouă `asn1crypto` (CMS/PKCS7, nu shell-out la `openssl`). Conexiuni neschimbate: [deltatech_pos](../deltatech_pos/index.md) (driver fiscal opțional), [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md) (agregare D394).
- **Fișă consultant:** resincronizată — copiate toate cele 6 capturi din `readme/screenshots/` (cele 4 existente + `05_import_arhiva.png`/`06_discrepante.png`, noi din acest PR).
- **Corecție la sursă:** `readme/FISA_CONSULTANT.md` secțiunea 10 conținea încă nota că cele două capturi noi „nu există încă", deși fuseseră deja generate — notă rămasă neactualizată din tura anterioară. Corectată direct la sursă (nu doar în copia wiki) și re-copiată.
- **Fișiere actualizate:** `l10n_ro_pos_fiscal_compliance/index.md`, `l10n_ro_pos_fiscal_compliance/FISA_CONSULTANT.md`, `l10n_ro_pos_fiscal_compliance/screenshots/*.png` (6 fișiere), `index.md` (linia sumarului), `log.md`.

---

## [2026-08-20] Rezolvare conflict de nume duplicat `l10n_ro_account_bank_statement_import_xlsx`

- **Acțiune:** Investigație (agent read-only) a confirmat că modulul `l10n_ro_account_bank_statement_import_xlsx` exista ca **două module distincte** cu același nume tehnic — unul în `odoo-addons/l10n_ro_ent` (Enterprise, OEEL-1, plătit) și unul în `odoo-addons/bitshop_ent` (AGPL-3, moștenit din 2016 "Forest and Biomass Romania"). Cauza: o migrare din mai 2026 (AGPL → Enterprise) rămasă incompletă — ambele au supraviețuit și au fost întreținute în paralel până azi. Confirmat din cod (`odoo/modules/module.py`): Odoo nu semnalează conflictul de nume, ia silențios primul director găsit în `addons_path` — iar `bitshop_ent` apărea înaintea `l10n_ro_ent` în `odoo.conf`, deci varianta AGPL veche câștiga silențios pe toate cele 14 instanțe client care au ambele suite, iar varianta Enterprise plătită nu se instala niciodată.
- **Decizie utilizator:** păstrează `l10n_ro_account_bank_statement_import_xlsx` doar în `l10n_ro_ent`; elimină complet varianta din `bitshop_ent` (nu redenumire).
- **Executat:** `git rm -r l10n_ro_account_bank_statement_import_xlsx` în repo-ul `odoo-addons/bitshop_ent` (branch `19.0`), urmat de regenerarea `README.md` al suitei prin `update_readme.sh` (pre-commit, hook `oca-gen-addons-table`) — linia modulului a dispărut automat din tabelul de module. Diff-ul a fost restrâns strict la această schimbare (au fost revertite 6 fișiere `index.html` neînrudite, regenerate ca efect secundar al rulării hook-ului pe toată suita, dar cu drift preexistent nelegat de acest task).
- **Neschimbat:** pagina wiki a modulului (deja documenta corect versiunea `l10n_ro_ent`, fără nicio referire directă la copia ștearsă). Dependența declarată în `proiecte/flodel/terrabit_flodel/__manifest__.py` rămâne funcțională — se va rezolva acum exclusiv prin `l10n_ro_ent`.
- **Rămas de făcut (nu în sarcina agentului):** commit + push pe repo-ul `bitshop_ent` — lăsate explicit în sarcina utilizatorului, conform cererii.
- **Fișiere atinse:** `odoo-addons/bitshop_ent/README.md` (modificat local, necommis), `odoo-addons/bitshop_ent/l10n_ro_account_bank_statement_import_xlsx/*` (șters, necommis), `wiki_module_odoo/log.md`.

---

## [2026-08-20] Re-ingestie 170 module cu drift de versiune (audit sistematic)

- **Acțiune:** Utilizatorul a întrebat dacă toate modulele din wiki sunt la ultima versiune. Un script de audit a comparat câmpul `Versiune:` din fiecare din cele 463 pagini wiki cu versiunea reală din `__manifest__.py` local, excluzând fals-pozitivele cauzate de repo-ul `l10n-romania` fiind pe branch-ul greșit local (`18.0-fix-...`) și de copii client-pinned din `proiecte/`. Rezultat: 272 module la zi, **170 module cu drift real** (wiki mai vechi decât codul). Toate cele 170 au fost re-ingerate în paralel, în 9 loturi de câte 20 de subagenți `documentarist-wiki` izolați (limita de concurență), cu instrucțiune explicită de regenerare completă a paginii (nu doar bump de versiune).
- **Descoperiri structurale importante ieșite la iveală în timpul re-ingestiei:**
  - **Migrări de suită neînregistrate anterior în wiki:** întreaga familie `deltatech_delivery_*` (cca. 15 module) și `deltatech_marketplace_*` (cca. 19 module) s-au mutat din `odoo-addons/bitshop` în suitele dedicate `odoo-addons/bitshop_delivery` și `odoo-addons/bitshop_marketplace`; `deltatech_vendor_products` s-a mutat în `odoo-addons/bitshop_vendor`; `l10n_ro_balance_confirmation` s-a mutat din `odoo-addons/l10n-romania` (OCA) în `odoo-addons/l10n_ro_ent` (Enterprise), cu rescriere funcțională majoră (trimitere în masă prin email cu tracking per partener). Toate căile locale și URL-urile GitHub din wiki au fost corectate.
  - **Conflict de nume duplicat:** `l10n_ro_account_bank_statement_import_xlsx` există ca **două module distincte** cu același nume tehnic — unul în `odoo-addons/l10n_ro_ent` (Enterprise, licență OEEL-1, depinde de `l10n_ro`) și altul în `odoo-addons/bitshop_ent` (AGPL-3, depinde de `deltatech_account_bank_statement_import`). Dacă ambele devin instalabile simultan pe aceeași bază, Odoo va da eroare de nume duplicat — necesită decizie de retragere/redenumire a unuia dintre ele.
  - **Sintaxă `[[wikilink]]` incorectă corectată sistematic:** un număr mare de pagini din `l10n_ro_ent` (peste 15 module: `l10n_ro_account_chart`, `l10n_ro_anaf_d205`, `l10n_ro_anaf_d207`, `l10n_ro_anaf_d300`, `l10n_ro_anaf_d318`, `l10n_ro_anaf_d390`, `l10n_ro_anaf_d394`, `l10n_ro_anaf_d394_pos`, `l10n_ro_audit_immutable`, `l10n_ro_fixed_assets`, `l10n_ro_grants`, `l10n_ro_inventory_register`, `l10n_ro_partner_ledger_currency`, `l10n_ro_period_close_enhanced`, `l10n_ro_process_library`, `l10n_ro_reges` ș.a.) foloseau sintaxă stil Obsidian `[[modul]]` în loc de link Markdown standard `[modul](../modul/index.md)`, deci link-urile erau nefuncționale — corectate în timpul re-ingestiei.
  - **DESCRIPTION.md desincronizate de cod:** cel puțin `deltatech_mrp` (descrie funcționalități complet dispărute din cod — rotunjire BOM, generare lot automat — în loc de modelul SQL real de cost pe categorii), `deltatech_feed` (platforme diferite față de cele implementate), `l10n_ro_financial_statements` (nu menționa rapoartele noi F30/F40), `l10n_ro_period_close_enhanced`, `l10n_ro_intrastat_enhancement` și altele au descrieri sursă (readme) învechite față de codul curent — paginile wiki au fost corectate pe baza analizei directe de cod, cu semnalarea explicită a decalajului pentru echipa de dezvoltare.
- **Fișă consultant:** re-copiată/resincronizată pentru toate modulele care o au (majoritatea `l10n_ro_ent`); nicio copiere nouă pentru module fără `readme/FISA_CONSULTANT.md`.
- **Verificare finală:** toate cele 170 module confirmate cu versiune identică wiki↔cod (un singur caz, `deltatech_stock_report`, a necesitat corecție manuală directă după re-ingestie). Total pagini wiki neschimbat: 463.
- **Fișiere actualizate:** 170 pagini `<modul>/index.md` (+ fișe consultant/screenshots resincronizate acolo unde există), `log.md`. Nu a fost necesară actualizarea descrierilor de o linie din `index.md` central — toate au rămas reprezentative pentru funcționalitatea modulului.

---

## [2026-08-20] Ingestie 4 module lipsă din `bitshop_delivery`/`bitshop_marketplace`

- **Acțiune:** Utilizatorul a semnalat că auditul anterior de acoperire nu verificase și suitele `bitshop_delivery` (24 module), `bitshop_marketplace` (20 module) și `bitshop_vendor` (4 module). Verificare comparativă a găsit doar 4 module fără pagină wiki (restul de 44 erau deja documentate, probabil ingerate anterior sub altă mapare de cale): `deltatech_delivery_dropshiping`, `deltatech_delivery_ne`, `deltatech_marketplace_trendyol`, `deltatech_marketplace_woocommerce`. Toate patru documentate în paralel de subagenți `documentarist-wiki` izolați.
- **Sursă:** `readme/DESCRIPTION.md` pentru toate cele 4 (Sumar/Funcționalități); `deltatech_delivery_dropshiping` e semnalat explicit ca **deprecated pe 19.0** (`installable: False`), funcționalitate acoperită de `deltatech_delivery`; `deltatech_delivery_ne` deleagă integral logica API către `deltatech_delivery_cm` (Courier Manager), fără implementare proprie.
- **Fișă consultant:** niciunul dintre cele 4 module nu are `readme/FISA_CONSULTANT.md` — nu s-a copiat nimic.
- **Dependențe/Conexiuni:** toate dependențele custom (`deltatech_delivery`, `deltatech_delivery_cm`, `deltatech_marketplace`, `deltatech_marketplace_sale`, `deltatech_marketplace_sale_stage`, `deltatech_marketplace_delivery`, `deltatech_marketplace_payment`, `deltatech_marketplace_website`) au deja pagină wiki și au fost linkuite activ; `sale`, `delivery`, `mail`, `stock_dropshipping` (module core) au rămas text `cod`.
- **Cale GitHub:** suitele `bitshop_delivery` și `bitshop_marketplace` nu erau în tabelul de mapare al agentului — remote-urile reale confirmă `terrabit-solutions/bitshop_delivery` și `terrabit-solutions/bitshop_marketplace`, branch `19.0`.
- **Fișiere actualizate:** 4 directoare noi `<modul>/index.md`, `index.md`, `log.md`.

---

## [2026-08-20] Ingestie lot 23 module lipsă din `deltatech`/`bitshop`/`bitshop_ent`

- **Acțiune:** Audit de acoperire wiki peste toate modulele cu `__manifest__.py` din `odoo-addons/deltatech`, `odoo-addons/bitshop` și `odoo-addons/bitshop_ent` (279 module) a găsit 23 fără pagină wiki; toate au fost documentate în paralel de subagenți `documentarist-wiki` izolați (4 loturi, în limita de 20 subagenți concurenți): `bitshop_sale_withdrawal_stock`, `deltatech_ai_anthropic`, `deltatech_bank_reconcile_ai`, `deltatech_bank_salary_confidential`, `deltatech_delivery_cod`, `deltatech_delivery_iot`, `deltatech_image_optimize`, `deltatech_partner_merge`, `deltatech_payment_ing_webpay`, `deltatech_pos_fix`, `deltatech_pos_online_payment`, `deltatech_pos_price_sync`, `deltatech_pos_stock`, `deltatech_product_chatter`, `deltatech_product_reordering_limit`, `deltatech_quality_lot`, `deltatech_restrict_reports`, `deltatech_sale_analysis_vat`, `deltatech_sale_referrer_dashboard`, `deltatech_sale_referrer_raport`, `deltatech_sale_stage_route`, `deltatech_secondary_uom`, `deltatech_website_searchbar`.
- **Sursă:** `readme/DESCRIPTION.md` acolo unde există (majoritatea modulelor), completat cu analiza codului (`models/`, `views/`, `security/`, `wizard/`, JS static) pentru secțiunea Componente Cheie; câteva module (`deltatech_pos_fix`, `deltatech_pos_stock`, `deltatech_pos_online_payment`, `deltatech_website_searchbar`, `deltatech_partner_merge`, `deltatech_restrict_reports`) nu au `models/`/`views/` proprii sau nu au avut DESCRIPTION detaliat, documentate direct din cod.
- **Fișă consultant:** niciunul dintre cele 23 de module nu are `readme/FISA_CONSULTANT.md` — nu s-a copiat nimic în acest lot.
- **Dependențe/Conexiuni:** majoritatea dependențelor sunt module Odoo core (`sale`, `account`, `stock`, `point_of_sale`, `product`, `mail`, `base`, `payment`) fără pagină wiki, rămase text `cod`; conexiuni linkuite activ unde exista deja pagină: `bitshop_sale_withdrawal` ↔ `bitshop_sale_withdrawal_stock`, `deltatech_website_watermark` ↔ `deltatech_image_optimize`, `deltatech_sale_cost_product` ↔ `deltatech_sale_referrer_dashboard`, `deltatech_sale_referrer_raport` ↔ `deltatech_sale_referrer_dashboard`, `deltatech_sale_stage` ↔ `deltatech_sale_stage_route`, `deltatech_pos_online_payment`/`deltatech_website_delivery_and_payment` ↔ `deltatech_payment_ing_webpay`, `deltatech_delivery` ↔ `deltatech_delivery_cod`.
- **Fișiere actualizate:** 23 directoare noi `<modul>/index.md` (fără fișe consultant/screenshots), `index.md`, `log.md`.

---

## [2026-08-19] Ingestie `bitshop_sale_withdrawal` (v19.0.0.2.0)

- **Acțiune:** Primul modul din suita `bitshop` documentat în wiki. Adaugă pe portalul clienților funcția de retragere din contract la distanță (dreptul de renunțare, Directiva 2011/83/UE modificată prin Directiva (UE) 2023/2673, transpusă în România prin OUG 18/2026, aplicabilă din 19 iunie 2026): buton pe pagina comenzii, recapitulare + confirmare într-un pas separat, confirmare de primire pe suport durabil (e-mail + PDF cu timestamp), excepții art. 16 per produs/categorie și registru de retrageri în Vânzări.
- **Sursă:** `readme/DESCRIPTION.md` + `readme/USAGE.md` + `readme/CONFIGURE.md` pentru Sumar și Funcționalități Cheie; secțiunea Componente Cheie completată suplimentar din analiza `models/`, `views/` și `data/` (readme-ul nu detaliază tehnic modelele/vizualizările).
- **Fișă consultant:** DA — copiată împreună cu cele **7** capturi (`01_portal_buton` … `07_fisa_retragere`), generate din `tests/test_screenshots.py`, integral pe portal (flux de vizitator/consumator, nu back office).
- **Dependențe/Conexiuni:** `sale`, `portal` (fără pagină wiki, rămase text `cod`). Conexiune identificată: `bitshop_sale_withdrawal_stock` (extensie operațională pe stoc, nu are încă pagină wiki).
- **Fișiere actualizate:** `bitshop_sale_withdrawal/index.md`, `bitshop_sale_withdrawal/FISA_CONSULTANT.md`, `bitshop_sale_withdrawal/screenshots/` (7), `index.md`, `log.md`.

---

## [2026-08-15] Re-ingestie `l10n_ro_cash_register` (v19.0.1.1.7 → v19.0.1.2.0)

- **Acțiune:** Regenerată pagina modulului după PR dhongu/l10n-romania#508 (merged pe 19.0). Soldurile registrului (`balance_start` / `balance_end`) se recalculează acum automat la postarea, anularea sau ștergerea notelor care ating contul de casă — pentru ziua respectivă **și pentru toate zilele ulterioare** din același jurnal, pentru că reportul se propagă în lanț. Înainte erau compute stocate cu `depends` care nu urmărea înregistrările contabile, deci rămâneau înghețate la momentul creării registrului; cum registrul zilei se creează automat la prima plată, se năștea pe o zi goală și afișa tăcut cifre false. Recalculul era posibil doar manual, din butonul Refresh, și numai pentru registrele selectate. Bază legală: OMFP 2634/2015, Anexa 1 pct. 58 lit. e) și n) — reluarea **automată** în calcul a soldurilor obținute anterior.
- **Sursă:** `readme/DESCRIPTION.md` este sărac (o singură linie), deci Sumarul și Funcționalitățile Cheie au fost sintetizate din `__manifest__.py`, cod și `readme/FISA_CONSULTANT.md` + `readme/HISTORY.md`; secțiunea Componente Cheie a fost inclusă integral (Modele / Vizualizări / Acțiuni).
- **Alte schimbări reflectate:** model nou `models/account_move.py` (override `_post` / `button_draft` / `unlink`); migrare `migrations/19.0.1.2.0/post-migration.py` care recalculează registrele existente; liniile se listează cronologic și filtrează pe companie; eliminată `action_recompute_from_previous_balance` (putea produce un sold de deschidere diferit de soldul de închidere al zilei precedente); metode noi `action_print`, `_l10n_ro_software_signature`, `_l10n_ro_annex_count`; raport PDF conform formularului **14-4-7A** (Nr. act de casă, Nr. anexe, Explicații, rând de report, totaluri distincte, semnături, mențiunea programului și versiunii — pct. 58 lit. k); teste noi `tests/test_cash_register_balance.py`.
- **Fișă consultant:** DA — recopiată împreună cu cele **5** capturi regenerate azi (`01_jurnal_cash` … `05_raport_pdf`), în RO pe planul de conturi RO. Fișa descrie acum recalculul automat în locul Împrospătării manuale, structura raportului 14-4-7A, faptul că listarea zilnică pe hârtie nu este obligatorie (Anexa 1 pct. 12, 36, 56 — obligatorie e întocmirea zilnică) și limitarea legată de casieriile care partajează același cont de casă.
- **Dependențe/Conexiuni:** `l10n_ro_account_sequence` (dependență); conexiuni către [l10n_ro_cash_register_report](l10n_ro_cash_register_report/index.md) (același registru ca raport nativ `account.report`, pe interval, cu export PDF/XLSX), [l10n_ro_cash_bank_enhanced](l10n_ro_cash_bank_enhanced/index.md) și [l10n_ro_bank_register_report](l10n_ro_bank_register_report/index.md). `l10n_ro_cash_register_report` nu a fost modificat de PR, deci pagina lui rămâne valabilă.
- **Fișiere actualizate:** `l10n_ro_cash_register/index.md`, `l10n_ro_cash_register/FISA_CONSULTANT.md`, `l10n_ro_cash_register/screenshots/` (5), `index.md`, `log.md`.

---

## [2026-08-10] Refresh capturi `l10n_ro_stock_pack_cmp` + `l10n_ro_stock_pack_fifo`

- **Acțiune:** Actualizate capturile din wiki după rafinarea cosmetică din suită (PR #83): documentele se deschid prin acțiunea de jurnal (breadcrumb cu context, nu formular fără ancoră), datele de scadență și de livrare urmează scenariul din iunie 2026 în loc de data rulării, numele demo sunt plauzibile (Alfa Distribuție SRL, Beta Retail SRL, Marfă A (buc)), iar previzualizarea CMP periodic are antetele de coloană lizibile.
- **Sursă:** regenerate din `tests/test_screenshots.py` al fiecărui pachet; fișele nu s-au schimbat, doar imaginile.
- **Fișiere actualizate:** `l10n_ro_stock_pack_cmp/screenshots/` (8), `l10n_ro_stock_pack_fifo/screenshots/` (9), `log.md`.

---

## [2026-08-10] Fișe consultant pentru `l10n_ro_stock_pack_cmp` + `l10n_ro_stock_pack_fifo` (v19.0.1.3.0)

- **Acțiune:** Adăugate fișele consultant la paginile celor două pachete de evaluare stoc, ingerate mai devreme azi. Paginile au fost actualizate la versiunea 19.0.1.3.0, cu linia de metadate **Fișă Consultant**.
- **Fișă consultant:** DA la ambele — copiate `FISA_CONSULTANT.md` și capturile: **8** la CMP (`01_instalare_pachet` … `08_corectie_cmp_periodic`) și **9** la FIFO (`01_instalare_pachet` … `09_balanta_stocuri`), generate reproductibil din `tests/test_screenshots.py`, în RO, pe planul de conturi RO, cu același scenariu ca testul de flux.
- **Corecții consemnate (audit `verificator-fisa`, aplicate înainte de copiere):** formula CMP periodic din fișă era greșită (intrări/intrări în loc de (stoc inițial + intrări)/(cantitate inițială + intrări), OMFP 1802 pct. 96 alin. (2)); calea de activare a RNI e în Setări → **Inventar**, nu Contabilitate; conturile de inventariere nu au valoare implicită; nedeductibilitatea minusului formulată cu excepțiile art. 25 alin. (4) lit. c); consecința convenției „408 fără TVA"; pași noi de flux pentru retur și inventariere.
- **Fix de tooling adiacent:** `l10n_ro_doc_screenshots` v19.0.1.0.1 — `click_tab` încerca doar eticheta engleză, deci pe interfața RO capturile de facturi rămâneau pe tabul greșit.
- **Fișiere actualizate:** `wiki_module_odoo/l10n_ro_stock_pack_cmp/{index.md,FISA_CONSULTANT.md,screenshots/}` (8 poze), `wiki_module_odoo/l10n_ro_stock_pack_fifo/{index.md,FISA_CONSULTANT.md,screenshots/}` (9 poze), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild).

---

## [2026-08-10] Ingestie `l10n_ro_stock_pack_cmp` + `l10n_ro_stock_pack_fifo` — pachetele de evaluare stoc (v19.0.1.2.0)

- **Acțiune:** Documentate în paralel (2 subagenți `documentarist-wiki`) cele două module-pălărie noi din `l10n_ro_ent` (create 09–10.08.2026, PR #81): bundle-uri care instalează pachetul de stoc RO per metodă de evaluare, mutual exclusive prin cheia de manifest `excludes`, cu `post_init_hook` care setează `cost_method` (average/fifo) + valorizare perpetuă pe companiile RO.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar/Funcționalități la ambele; `readme/USAGE.md` (monografia fluxului end-to-end, cifre verificate de testul `tests/test_stock_flow.py` și de agentul contabil) ca sursă suplimentară; module fără `models/`/`views/` — secțiunea 4 documentează doar `hooks.py`.
- **Fișă consultant:** NU — niciunul dintre pachete nu are `readme/FISA_CONSULTANT.md`.
- **Dependențe/Conexiuni:** toate cele 6 dependențe custom RO au pagini wiki → link-uri active (`l10n_ro_stock_cmp_periodic` doar la CMP, `l10n_ro_stock_posting_date`, `l10n_ro_stock_constraints`, `l10n_ro_stock_sheet`, `l10n_ro_stock_gestiune`, `l10n_ro_inventory_closing`); `purchase_stock`/`sale_stock` rămân text `cod`. Cross-link-urile pack_cmp ↔ pack_fifo au fost activate la consolidare (paginile s-au creat simultan).
- **Fișiere actualizate:** `wiki_module_odoo/l10n_ro_stock_pack_cmp/index.md` (nou), `wiki_module_odoo/l10n_ro_stock_pack_fifo/index.md` (nou), `wiki_module_odoo/index.md` (+2 linii), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild).

---

## [2026-07-31] Re-ingestie `deltatech_purchase_add_extra_line` — v19.0.1.0.2 → v19.0.1.2.0, cu fișă consultant

- **Acțiune:** Regenerată pagina modulului `deltatech_purchase_add_extra_line` (ingestia anterioară: 2026-06-03, versiunea 19.0.1.0.2), prin subagent `documentarist-wiki`. Perechea de achiziție a modulului documentat mai sus, adus la același nivel: preț manual păstrat, traducere RO, fișă consultant.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar/Funcționalități, completat din `readme/HISTORY.md` și analiza codului (`models/purchase.py`) pentru Componente Cheie.
- **Fișă consultant:** DA — copiate `FISA_CONSULTANT.md` și 6 capturi (`01_configurare_produs.png` … `06_comanda_confirmata.png`), generate din `tests/test_screenshots.py` pe compania „Demo Achiziții SRL" în RON, cu interfața în RO.
- **Capcană de configurare consemnată în pagină:** cele trei câmpuri (`extra_product_id`, `extra_percent`, `extra_qty`) sunt declarate de **ambele** module surori pe `product.template`, deci configurarea e **comună** — un produs configurat generează linia suplimentară atât la vânzare, cât și la achiziție, iar nu există posibilitatea de a o limita la un singur tip de document. Corolar tehnic: textele de ajutor trebuie ținute IDENTICE în ambele module, altfel tooltipul depinde de ordinea de încărcare (ultimul modul încărcat câștigă). Aliniate în această sesiune, cu formulare neutră față de document („ordered") și menționând atât lista de prețuri, cât și prețul de furnizor.
- **Limitare consemnată:** mecanismul lucrează doar pe comenzi în stările `draft`/`sent` (cerere de ofertă / ofertă trimisă) — pe o comandă confirmată, o modificare de cantitate pe linia principală nu mai actualizează linia suplimentară. Punctele de apel: `create()`, onchange pe `order_line`, `action_rfq_send()`, `print_quotation()`.
- **Dependențe/Conexiuni:** `purchase` rămâne text `cod`; [deltatech_sale_add_extra_line](deltatech_sale_add_extra_line/index.md) → link activ (modul soră, configurare partajată).
- **Fișiere actualizate:** `wiki_module_odoo/deltatech_purchase_add_extra_line/index.md` (regenerat), `FISA_CONSULTANT.md` + `screenshots/` (6 fișiere, nou), `wiki_module_odoo/index.md` (linie actualizată), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

---

## [2026-07-31] Re-ingestie `deltatech_sale_add_extra_line` — v19.0.1.0.9 → v19.0.1.3.0, cu fișă consultant

- **Acțiune:** Regenerată integral pagina modulului `deltatech_sale_add_extra_line` (ingestia anterioară: 2026-06-03, versiunea 19.0.1.0.9), prin subagent `documentarist-wiki`. Modulul a primit între timp trei schimbări funcționale și o fișă consultant nouă.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar/Funcționalități (corect pentru 19.0, fără referințe la versiuni vechi), plus `readme/HISTORY.md` și analiza codului (`models/sale.py`, `models/product_template.py`, `views/*.xml`, `migrations/19.0.1.1.0/post-migration.py`) pentru Componente Cheie. Pagina are și o secțiune „Migrări", în plus față de schema standard.
- **Fișă consultant:** DA — prima fișă din suita `deltatech` intrată în wiki. Copiate `FISA_CONSULTANT.md` și cele 6 capturi din `readme/screenshots/` (`01_configurare_produs.png` … `06_factura_linie_extra.png`), plus linia de metadate din pagină. Capturile sunt generate reproductibil din `tests/test_screenshots.py` (Playwright, interfață RO, plan de conturi RO).
- **Schimbări funcționale documentate:**
  - prețul introdus manual pe linia suplimentară este păstrat, marcat prin câmpul tehnic nou `extra_price_computed` pe `sale.order.line`; revenirea la prețul calculat = ștergerea liniei, care se regenerează;
  - cu procent zero se aplică recalculul standard Odoo (listă de prețuri, valută, unitate de măsură), nu mai `lst_price` brut, care ignora toate trei;
  - coșul din magazinul online generează din nou linia suplimentară — hook-ul `_cart_update` nu mai există în Odoo 19, s-a trecut pe `_verify_cart_after_update`;
  - traducere română completă (`i18n/ro.po`): „Linie suplimentară", „Produs suplimentar", „Procent suplimentar", „Cantitate suplimentară".
- **Constatare din auditul fișei (relevantă pentru `l10n_ro_sgr`, consumatorul acestui modul):** baza legală a garanției SGR era citată greșit în fișă — SGR e stabilit prin **HG 1074/2021**, iar regimul TVA stă în **art. 315^5 alin. (2) Cod fiscal** („nu reprezintă contravaloarea unei livrări… **în sfera TVA**"), nu în art. 286 alin. (4), care enumeră ce se exclude din baza unei operațiuni aflate în sferă. Corectat în fișă; denumirea taxei create de `l10n_ro_sgr` citează încă art. 286 alin. 4 — semnalat separat ca task.
- **Dependențe/Conexiuni:** dependențele (`sale`, `website_sale`, `stock`) sunt module standard fără pagină wiki → rămân text `cod`. Toate cele trei module conexe au pagină wiki → linkuri active: [deltatech_purchase_add_extra_line](deltatech_purchase_add_extra_line/index.md), [deltatech_sale_add_extra_line_pos](deltatech_sale_add_extra_line_pos/index.md), [l10n_ro_sgr](l10n_ro_sgr/index.md).
- **Fișiere actualizate:** `wiki_module_odoo/deltatech_sale_add_extra_line/index.md` (regenerat), `FISA_CONSULTANT.md` + `screenshots/` (6 fișiere, nou), `wiki_module_odoo/index.md` (linie actualizată), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

---

## [2026-07-31] Ingestie suita bitshop_delivery — 3 module, acoperire completă (22/22)

- **Acțiune:** Documentate cele 3 module rămase din `odoo-addons/bitshop_delivery`, în paralel prin subagenți `documentarist-wiki`: `deltatech_delivery_category_price` (v19.0.1.0.1, tarif de livrare pe categorii website), `deltatech_delivery_tnt` (v19.0.0.1.1, curier TNT) și `deltatech_delivery_batch` (v19.0.1.0.5, AWB în lot pe `stock.picking.batch`). Suita e acum acoperită integral (22/22).
- **Sursă:** `readme/DESCRIPTION.md` la toate trei. La `deltatech_delivery_tnt` conținutul a fost corectat față de readme (vezi mai jos), nu preluat ca atare.
- **Fișă consultant:** niciunul dintre cele 3 module nu are `readme/FISA_CONSULTANT.md`.
- **Constatare importantă — `deltatech_delivery_tnt`, readme greșit în AMBELE direcții** (verificată direct în cod, nu doar raportată de subagent):
  - Metoda declarativă `_tnt_api_capabilities()` din `models/delivery.py:45` returnează **doar `{"ship"}`**, cu comentariu explicit în cod: „TNT nu expune deloc anulare — confirmat la conectarea la gardă." Nu există nicio metodă `cancel_shipment`/`tnt_cancel` în `models/`. Testul modulului confirmă textual că anularea și istoricul de status nu sunt acoperite deoarece nu sunt implementate.
  - Dar `readme/DESCRIPTION.md` listează la „Key Features": „AWB cancellation capability for rejected or changed orders" (linia 30), „Comprehensive delivery status tracking" (31), „Comprehensive delivery history tracking" (46), „Extension of delivery tracking capabilities" (70) — **capabilități inexistente**, într-un readme publicat pe Apps Store.
  - Invers, la „Without Features" readme-ul afirmă că generarea AWB în format ZPL **nu** e suportată (linia 120), dar codul o implementează: `tnt_label_type` include `zpl`, `tnt_transform_xml_to_zpl()` există, plus 4 fișiere `static/src/xsl/ZPL*RoutingLabelRenderer.xsl`.
  - Pagina wiki reflectă capabilitățile reale și citează contradicția. **DESCRIPTION.md al modulului rămâne de corectat** — semnalat separat ca task, fiind o problemă comercială (modul plătit pe Apps Store care promite anularea AWB).
  - Confirmă regula suitei: capabilitățile curierilor se citesc din contractul declarat (`_*_api_capabilities()`), nu deduse din prezența numelor de metode.
- **Dependențe/Conexiuni:** `deltatech_delivery` are pagină wiki → linkat activ la TNT și batch; `delivery`, `website_sale`, `mail`, `stock_picking_batch` rămase text `cod`. Dependență externă Python la TNT: `phonenumbers`.
- **Fișiere actualizate:** 3 pagini noi, `wiki_module_odoo/index.md` (3 intrări, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-31] Ingestie suita deltatech — 59 module, acoperire completă (179/179)

- **Acțiune:** Documentate toate cele 59 module din `odoo-addons/deltatech` care nu aveau pagină wiki, în 10 loturi paralele de câte ~6 prin subagenți `documentarist-wiki`. Suita `deltatech` este acum acoperită integral (179/179 module). Zone acoperite: contabilitate/facturare (`deltatech_account_analytic`, `deltatech_account_edi_ubl_advice`, `deltatech_account_edit_currency_rate`, `deltatech_invoice_number`, `deltatech_invoice_report`, `deltatech_invoice_to_draft`, `deltatech_generic_partner_restriction`, `deltatech_payment_forecast`), vânzări (`deltatech_sale_*`, `deltatech_saleorder_search`, `deltatech_discount_policy`, `deltatech_kit_price`, `deltatech_pricelist`), achiziții (`deltatech_purchase_*`), stoc/depozit (`deltatech_lot`, `deltatech_picking_*`, `deltatech_move_negative_stock`, `deltatech_stock_*`, `deltatech_replenishment_explain`, `deltatech_report_packaging`), producție (`deltatech_mrp_*`), produse (`deltatech_product_*`, `deltatech_competitors_price`), website/eCommerce (`deltatech_website_*`), plus infrastructură (`deltatech_tc`, `deltatech_rpc_audit`, `deltatech_cron_monitor_webhook`, `deltatech_markdown_field`, `deltatech_line_counter`, `deltatech_pos_product_filter`).
- **Sursă:** `readme/DESCRIPTION.md` prezent la toate 59; Componente Cheie completate din analiza codului acolo unde readme-ul nu acoperea secțiunea. La modulele fără `models/` (biblioteci JS, controllere pure — `deltatech_markdown_field`, `deltatech_rpc_audit`, `deltatech_website_country`, `deltatech_website_pager_guard`, `deltatech_website_sale_attribute_filter`) secțiunea a fost adaptată la fișierele reale.
- **Fișă consultant:** niciunul dintre cele 59 module nu are `readme/FISA_CONSULTANT.md` — nimic de copiat.
- **Drift readme→cod semnalat de subagenți (de corectat la sursă, în module):**
  - `deltatech_account_analytic` — DESCRIPTION.md STALE GRAV: descrie împărțirea automată a liniilor de factură în valoare de stoc + marjă, condiționată de `deltatech_sale_commission` (modul inexistent), plus câmpuri pe `account.analytic.account` care nu mai există. În cod funcționalitatea e dezactivată (`views/res_config_settings.xml` complet comentat, câmpurile din `models/res_config_settings.py` comentate).
  - `deltatech_website_category` — DESCRIPTION.md acoperă doar arhivarea categoriilor și **omite complet** funcționalitatea majoră de performanță (arbore de categorii lazy-loaded, ruta `/shop/category_children/<id>`, interacțiunea OWL `lazy_categories.esm.js`), care e cea mai mare parte a codului 19.0 — confirmată de HISTORY.md.
  - `deltatech_purchase_phase` — hook-ul `write()` din `models/stock_picking.py` propagă automat faza pe comandă în funcție de `delivery_state` (`pre_advice`, `shipped`, `delivered`, `refused`, confirmate și de datele demo), dar nu e menționat deloc în DESCRIPTION.md.
  - `deltatech_sale_purchase` — DESCRIPTION.md afirmă că modulul gestionează scăderea cantităților comandate; comportamentul e acum nativ în nucleul Odoo 19 (suprascrierea `_log_decrease_ordered_quantity` din 18.0 a fost eliminată), fapt documentat de test.
  - `deltatech_picking_restrict_entry_exit` — DESCRIPTION.md afirmă blocarea la **creare**; restricția din `create()` e comentată în 19.0, controlul real e la `button_validate` și `write`.
  - `deltatech_saleorder_search` — DESCRIPTION.md menționează filtrare după „mobile", dar view-ul implementează doar e-mail și telefon.
  - `deltatech_sale_activity_report` — `name`/`summary` din manifest („Sale Order Last Modified", „Adds a last modified field") descriu un simplu câmp de dată, dar codul implementează un sistem complet de audit al comenzilor de vânzare cu curățare via `data_recycle`.
  - `deltatech_competitors_price` — DESCRIPTION.md conține exemplu de comandă cu `odoo18.conf`.
  - `deltatech_discount_policy` — DESCRIPTION.md spune „...in Odoo 18", modulul e 19.0.1.0.0.
  - `deltatech_sale_report` — DESCRIPTION.md referă versiunea `(17.0.0.0.0)`.
  - `deltatech_website_sale_portal` — `readme/DESCRIPTION.md` e practic gol (placeholder „Features:\n-"); pagina a fost sintetizată din manifest + cod.
  - `deltatech_sale_add_extra_line_pos` — `pos.session` extins conține doar o metodă comentată (`_loader_params_product_product`), fără logică activă.
  - `deltatech_mrp_simple_barcode` — id de view rămas placeholder în XML: `your_module_view_mrp_simple_form_inherit`.
  - `deltatech_cron_monitor_webhook`, `deltatech_pos_product_filter` — `README.rst` auto-generat are link-uri/badge-uri către branch-ul `18.0` (artefact OCA neregenerat).
- **Corecție la consolidare:** link-uri ratate de subagenții paraleli, convertite în link-uri active — `deltatech_purchase_portal` → `deltatech_purchase_phase` (dependență directă, la secțiunile 3 și 5) și `deltatech_ecr_connect` → `deltatech_tc` (documentat anterior ca „agent local, non-Odoo"; `deltatech_tc` este de fapt și modul Odoo, iar agentul local e componenta separată care rulează pe stație — formulare clarificată).
- **Dependențe/Conexiuni:** rămase text `cod` (module core Odoo, fără pagină wiki): `account`, `analytic`, `sale`, `sale_stock`, `sale_margin`, `sale_purchase`, `purchase`, `purchase_stock`, `stock`, `stock_account`, `product`, `mrp`, `mail`, `web`, `base`, `base_setup`, `portal`, `point_of_sale`, `website_sale`, `website_sale_stock`, `website_blog`, `delivery`, `barcodes`, `data_recycle`, `rpc`, `account_edi_ubl_cii`.
- **Fișiere actualizate:** 59 pagini noi, `wiki_module_odoo/index.md` (59 intrări, ordine alfabetică verificată programatic — 429 module în total), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-31] Ingestie suita bitshop — 17 module, acoperire completă a golului

- **Acțiune:** Documentate toate cele 17 module din `odoo-addons/bitshop` care nu aveau pagină wiki, în 3 loturi paralele prin subagenți `documentarist-wiki`: plăți online (`deltatech_payment_bt_ipay`, `deltatech_payment_eu_platesc`, `deltatech_payment_monri`), interfețe contabile/fiscale (`deltatech_keez`, `deltatech_saga_mrp`, `deltatech_ecr_connect`), achiziții (`deltatech_purchase_portal`, `deltatech_purchase_price_compare`), depozit (`deltatech_barcode_picking`, `terrabit_picking_flow`, `deltatech_report_prn_zebra_sdk`), website/eCommerce (`deltatech_website_sale_category`, `deltatech_website_seo`, `terrabit_google_tag`, `terrabit_partner_credit_limit_website`), plus `deltatech_sale_product_reference` și `deltatech_widget_hierarchy_m2o`. Suita `bitshop` este acum acoperită integral (61/61 module).
- **Sursă:** `readme/DESCRIPTION.md` la toate 17 (niciun modul fără); Componente Cheie completate din analiza codului acolo unde readme-ul nu acoperea secțiunea. La `deltatech_ecr_connect` (bibliotecă JS pură, fără `models/`/`views/`) secțiunea a fost adaptată la fișierele `static/src/*.esm.js`.
- **Fișă consultant:** niciunul dintre cele 17 module nu are `readme/FISA_CONSULTANT.md` — nimic de copiat.
- **Corecție de infrastructură (importantă):** doi subagenți au semnalat independent că tabelul de mapare suită→repo din `.claude/agents/documentarist-wiki.md` avea owner-ul GitHub **stale**: `terrabit-ro` în loc de `terrabit-solutions`. Verificat cu `git remote get-url origin` pe fiecare suită și cu `gh repo view` (`terrabit-ro/*` doar redirectează către `terrabit-solutions/*`). Tabelul a fost corectat și completat (15 suite, inclusiv `bitshop_delivery`, `bitshop_marketplace`, `bitshop_vendor`, `queue`, `l10n-moldova`), cu regula nouă: dacă remote-ul contrazice tabelul, remote-ul câștigă. Excepție reală păstrată: `l10n-romania-oca` → `terrabit-ro/l10n-romania`. Owner-ul a fost corectat retroactiv în **196 pagini existente** (`bitshop` 92, `bitshop_ent` 13, `l10n_ro_ent` 100, `terrabit` 2) plus în paginile din loturile 1–2 ale acestei ingestii.
- **Corecție de conținut:** la `deltatech_barcode_picking`, `DESCRIPTION.md` marchează ca „todo" adăugarea produselor în inventar prin scanare, dar `models/stock_inventory.py` implementează deja complet fluxul (`on_barcode_scanned`, `_add_product`) — pagina notează discrepanța.
- **Risc semnalat de subagent:** `deltatech_website_sale_category` și `deltatech_website_sale_attributes` suprascriu ambele metoda `shop()` a controllerului `WebsiteSale` — ordinea MRO contează la instalarea simultană; notat în secțiunea de conexiuni a paginii.
- **Dependențe/Conexiuni:** rămase text `cod` (fără pagină wiki): `stock`, `account`, `payment`, `purchase`, `portal`, `web`, `website_sale`, `website_sale_stock`, `payment_custom`, `phone_validation`, `barcodes`, `mrp`, `sale`, `base_setup`, `l10n_ro`, `stock_account`, `deltatech_purchase_phase`, `deltatech_tc` (agent local, non-Odoo). Linkate activ la consolidare: `terrabit_facebook_pixel` și `deltatech_website_breadcrumb`, ratate de subagenți.
- **Fișiere actualizate:** 17 pagini noi, `wiki_module_odoo/index.md` (17 intrări, ordine alfabetică verificată programatic — 370 module în total), `wiki_module_odoo/log.md`, `.claude/agents/documentarist-wiki.md` (tabel de mapare), `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-31] Ingestie lot module cu fișă consultant fără pagină wiki — evaluare stoc + raport Z

- **Acțiune:** După un audit al golului dintre modulele din `odoo-addons/` (515) și paginile wiki (347), au rezultat 5 module care aveau deja fișă consultant cu capturi, dar nicio pagină wiki. Documentate toate 5 în paralel, prin subagenți `documentarist-wiki`: `deltatech_stock_valuation` (v19.0.0.0.6), `deltatech_obyc` (v19.0.1.0.0), `deltatech_valuation_area` (v19.0.1.0.0), `deltatech_valuation_report` (v19.0.0.0.1) — toată suita `deltatech_stock_valuation`, care nu avea până acum nicio pagină — plus `deltatech_sale_store_report` (v19.0.1.1.0, suita `bitshop`).
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar și Funcționalități Cheie la toate cinci; Componente Cheie completate din analiza codului (modele, view-uri, handler-e de raport, wizard) acolo unde DESCRIPTION.md nu acoperea secțiunea.
- **Fișă consultant:** toate 5 module au `readme/FISA_CONSULTANT.md` — copiate integral împreună cu capturile: `deltatech_stock_valuation` (7), `deltatech_obyc` (7), `deltatech_sale_store_report` (6), `deltatech_valuation_area` (5), `deltatech_valuation_report` (3) — 28 de capturi în total.
- **Corecție aplicată la consolidare:** subagenții rulând în paralel nu au putut linka paginile create simultan — `deltatech_valuation_area` și `deltatech_stock_valuation` rămăseseră text `cod` la dependențe/conexiuni în `deltatech_stock_valuation` și `deltatech_obyc`. Convertite în link-uri active după terminarea lotului, plus conexiuni reciproce adăugate în `deltatech_valuation_area` și `deltatech_stock_valuation` (întreaga familie e acum interlinkată: area → obyc → stock_valuation → valuation_report).
- **Corecție de conținut (rezolvată):** la `deltatech_obyc`, subagentul a semnalat că `readme/DESCRIPTION.md` are referințe la Odoo 17 și o listă de chei de tranzacție „mai largă decât cea activă în cod". Verificat direct în sursă: referințele la Odoo 17 erau reale, dar constatarea despre chei era **inversă** — DESCRIPTION.md avea o listă *incompletă* (15 din cele 18 chei din `TRANSACTION_KEYS`; lipseau `price_difference`, `stock_receipt_price_difference`, `landed_cost`), iar tabelul de determinare implicită acoperea doar 6 din cele 13 combinații de uzanțe tratate de `_compute_transaction_key`. Corectat în modul (`readme/DESCRIPTION.md`, versiune 19.0.1.0.0 → 19.0.1.0.1, `readme/HISTORY.md` nou, `README.rst` regenerat) și în pagina wiki, care listează acum toate cheile reale.
- **Dependențe/Conexiuni:** rămase text `cod` (fără pagină wiki): `stock`, `account`, `stock_account`, `purchase_stock`, `stock_landed_costs`, `account_reports`. `deltatech_sale_store` avea deja pagină → link activ.
- **Fișiere actualizate:** `deltatech_stock_valuation/`, `deltatech_obyc/`, `deltatech_valuation_area/`, `deltatech_valuation_report/`, `deltatech_sale_store_report/` (5 pagini noi, fiecare cu `FISA_CONSULTANT.md` + `screenshots/`), `wiki_module_odoo/index.md` (5 intrări noi, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-31] Ingestie deltatech_payment_advice — aviz de plată către furnizori (cerință Inedit Venture)

- **Acțiune:** Documentat modulul `deltatech_payment_advice` (suita `bitshop_ent`, v19.0.1.0.0), prin subagent `documentarist-wiki`. Modulul fusese dezvoltat la cererea clientului Inedit Venture (Victor Cazacu), dar nu era legat de nicio instalare — exista doar în `addons_path`, deci nu ajungea pe baza clientului. Ingestia în wiki s-a făcut odată cu instalarea lui pe producția Inedit și trecerea în `depends` la `terrabit_inedit`.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar și Funcționalități Cheie (aliniat cu codul 19.0, fără referințe la versiuni vechi); Componente Cheie completate minimal din `models/account_batch_payment.py` și `views/account_batch_payment_views.xml`.
- **Fișă consultant:** `readme/FISA_CONSULTANT.md` + 3 capturi (`01_plata_in_lot.png`, `02_aviz_pdf.png`, `03_email_furnizor.png`) — copiate integral în pagina wiki.
- **Dependențe/Conexiuni:** `account_batch_payment` (Enterprise) rămas text `cod`, fără pagină wiki; în Conexiuni și `terrabit_inedit`, modulul de proiect care îl are ca dependență.
- **Fișiere actualizate:** `deltatech_payment_advice/index.md` (pagină nouă, + FISA_CONSULTANT.md + screenshots/), `wiki_module_odoo/index.md` (1 intrare nouă, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-23] Ingestie lot import extrase bancare — GLS, Euplatesc, ING CSV (task 830, Insignis)

- **Acțiune:** Documentate 3 module noi, procesate în paralel prin subagenți `documentarist-wiki`: `deltatech_account_bank_statement_import_gls` (borderou ramburs GLS, semnătură A1, skip preambul/total), `deltatech_account_bank_statement_import_euplatesc` (detaliere decontare Euplatesc.ro, dedup pe RRN, comision/transfer configurabil), `l10n_ro_account_bank_statement_import_ing_csv` (istoric conturi ING Business CSV, solduri + CUI contrapartidă). Toate trei dezvoltate pentru task Terrabit #830 (client Insignis/ART STORE), F1 al planului (parsere) DONE și merged.
- **Sursă:** `readme/DESCRIPTION.md` pentru Sumar și Funcționalități Cheie la toate trei (prezent și la zi cu codul 19.0); Componente Cheie completate minimal din analiza codului (`models/account_journal.py`, view-urile de jurnal) doar unde DESCRIPTION.md nu acoperea.
- **Fișă consultant:** toate trei module au `readme/FISA_CONSULTANT.md` + 3 capturi de ecran fiecare — copiate integral în paginile wiki respective.
- **Dependențe/Conexiuni:** dependențele (`account_bank_statement_import`, `account_bank_statement_import_csv`, `l10n_ro`) rămase text `cod` (module core, fără pagină wiki). Cele trei module noi sunt conectate funcțional între ele (aceeași familie de import extrase) și cu `deltatech_account_bank_statement_import` — linkate reciproc unde relevant.
- **Corecție aplicată:** la Euplatesc, subagentul a inclus inițial `deltatech_account_bank_statement_import` ca dependență (secțiunea 3), deși nu apare în `depends` din manifest — corectat, mutată doar în Conexiuni (secțiunea 5).
- **Fișiere actualizate:** `deltatech_account_bank_statement_import_gls/index.md`, `deltatech_account_bank_statement_import_euplatesc/index.md`, `l10n_ro_account_bank_statement_import_ing_csv/index.md` (pagini noi, + FISA_CONSULTANT.md + screenshots/ la fiecare), `wiki_module_odoo/index.md` (3 intrări noi, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-21] Completare fișă consultant deltatech_calendar_caldav (port 18.0→19.0)

- **Acțiune:** Fișa consultant a modulului `deltatech_calendar_caldav` a fost portată pe branch-ul `19.0` (bitshop PR #2674, deschis) — copiată fidel, fără modificări de conținut (era deja version-agnostic, menționează „Odoo 18/19" generic). Completat ce rămăsese notat ca TODO în ingestia inițială.
- **Fișiere actualizate:** `deltatech_calendar_caldav/index.md` (adăugată linia de metadate „Fișă Consultant"), `deltatech_calendar_caldav/FISA_CONSULTANT.md` + `deltatech_calendar_caldav/screenshots/` (4 poze, copii noi), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-21] Ingestie deltatech_calendar_caldav (modul nou, bitshop)

- **Acțiune:** Documentat modulul nou `deltatech_calendar_caldav` (repo `bitshop`, branch `19.0`, port dintr-o dezvoltare inițială pe Odoo 18 — PR-uri #2671 merged pe 18.0, #2672 deschis pe 19.0) — sincronizare bidirecțională CalDAV ↔ Odoo (evenimente, recurență RRULE, reminder-e VALARM, participanți ATTENDEE/ORGANIZER, detectare conflicte ETag/schimbări CTag). Prima pagină wiki din repo-ul `bitshop` care documentează un conector generic (nu o localizare fiscală).
- **Sursă:** `readme/DESCRIPTION.md` (Sumar + Funcționalități Cheie); Componente Cheie completate din analiza codului (`models/caldav_account.py`, `models/calendar_event.py`, `views/caldav_account_views.xml`, `data/ir_cron_data.xml`) — DESCRIPTION.md nu acoperă modele/vizualizări/cron-uri.
- **Fișă consultant:** modulul are `readme/FISA_CONSULTANT.md` + 4 capturi pe branch-ul `18.0` (PR #2673, deschis), dar **nu a fost încă portată pe branch-ul `19.0`** — pagina wiki curentă nu are linie de metadate „Fișă Consultant" și directorul nu are `screenshots/`. De completat la o ingestie ulterioară, după portarea fișei pe 19.0.
- **Owner corect folosit:** `https://github.com/terrabit-solutions/bitshop/...` (owner canonic, verificat cu `gh repo view`) — NU `terrabit-ro/bitshop` (alias/redirect stale, folosit din greșeală în pagini mai vechi precum `deltatech_saga`, de corectat separat).
- **Dependențe/Conexiuni:** `calendar` (Odoo core, fără pagină wiki proprie) rămas text `cod` la ambele secțiuni.
- **Fișiere actualizate:** `deltatech_calendar_caldav/index.md` (pagină nouă), `wiki_module_odoo/index.md` (1 intrare nouă, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-19] Ingestie l10n_ro_bank_register_report + l10n_ro_registru_jurnal (2 module, port 18→19)

- **Acțiune:** Documentate 2 module noi din suita `l10n_ro_ent` (branch `19.0`), portate în aceeași sesiune de lucru dintr-o dezvoltare inițială pe Odoo 18: `l10n_ro_bank_register_report` (Jurnal de bancă, extinde direct `l10n_ro_cash_register_report` — suprascrie doar `_journal_type()`/`_day_section_label()`) și `l10n_ro_registru_jurnal` (Registrul-jurnal cod 14-1-1, handler complet autonom pe SQL brut, fără dependență de motorul de interogare standard `account_reports`).
- **Sursă:** `readme/DESCRIPTION.md` (Sumar + Funcționalități Cheie) pentru ambele; niciunul nu are `readme/FISA_CONSULTANT.md` — nimic de copiat. Componente Cheie completate din analiza codului (`models/bank_register_report_handler.py`, `models/registru_jurnal_report_handler.py`, XML-urile de date).
- **Consolidare retroactivă:** actualizată pagina `l10n_ro_sale_receipt_type_report` (ingestată azi mai devreme) — referința `l10n_ro_bank_register_report` din secțiunea Conexiuni era text `cod` (pagina nu exista încă); acum e link Markdown activ.
- **Dependențe/Conexiuni:** `l10n_ro_bank_register_report` → dependență directă `l10n_ro_cash_register_report` (linkată, are pagină). `l10n_ro_registru_jurnal` → `account_reports`/`l10n_ro` rămase text `cod`; conexiuni linkate activ: `l10n_ro_journal_reports`, `l10n_ro_cash_register`, `deltatech_saga` (aceeași convenție „%" pentru note compuse, folosită și la exportul SAGA), `l10n_ro_bank_register_report`.
- **Fișiere actualizate:** `l10n_ro_bank_register_report/index.md` + `l10n_ro_registru_jurnal/index.md` (pagini noi), `l10n_ro_sale_receipt_type_report/index.md` (1 link corectat), `wiki_module_odoo/index.md` (2 intrări noi, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-19] Ingestie l10n_ro_sale_receipt_type_report (modul nou, nu port)

- **Acțiune:** Documentat modulul nou `l10n_ro_sale_receipt_type_report` (suita `l10n_ro_ent`, branch `19.0`) — raport nativ pentru situația "Vânzări pe tipuri de încasări", cerută de contabilitatea clientului Damira. Nu e un port dintr-o versiune mai veche: modulul a fost construit direct pe Odoo 18, apoi portat pe 19.0 (fără niciun echivalent preexistent pe vreun branch).
- **Sursă:** `readme/DESCRIPTION.md` (Sumar + Funcționalități Cheie); secțiunea Componente Cheie completată din analiza codului (`models/sale_receipt_type_report_handler.py`, `data/l10n_ro_sale_receipt_type_report.xml`), inclusiv detaliul tehnic că `pos.payment.method.type` e câmp calculat nestocat (relevant pentru cine modifică raportul).
- **Corecție de conținut semnalată:** maparea suită→repo din `documentarist-wiki` (`.claude/agents/documentarist-wiki.md`) listează `l10n_ro_ent` ca `terrabit-ro/l10n_ro_ent`, dar acel owner e doar un alias/redirect GitHub — repo-ul canonic actual e `terrabit-solutions/l10n_ro_ent` (verificat live: `gh repo view terrabit-ro/l10n_ro_ent` rezolvă la `terrabit-solutions/l10n_ro_ent`). Pagina nouă folosește URL-ul corect; maparea din agent rămâne de actualizat separat (afectează toate paginile viitoare din suită).
- **Fișă consultant:** copiată integral, cu cele 4 capturi din `readme/screenshots/` (generate real, prin `tests/test_screenshots.py` rulat pe o bază 19.0 — nu doar scaffolding).
- **Dependențe/Conexiuni:** `l10n_ro`, `account_reports`, `point_of_sale`, `payment` rămase text `cod` (fără pagină wiki proprie). `l10n_ro_cash_register_report` linkat activ (are pagină); `l10n_ro_bank_register_report` și `l10n_ro_registru_jurnal` — module-soră create în aceeași sesiune de lucru — rămase text `cod`, nu au încă pagină wiki (de documentat separat).
- **Fișiere actualizate:** `l10n_ro_sale_receipt_type_report/index.md` (pagină nouă) + `FISA_CONSULTANT.md` + `screenshots/` (4 poze), `wiki_module_odoo/index.md` (1 intrare nouă, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-02] Ingestie lot l10n_ro_ent (13 module cu fișă consultant, fără pagină wiki)

- **Acțiune:** Documentate 13 module noi din suita `l10n_ro_ent` (repo `terrabit-ro/l10n_ro_ent`, branch `19.0`) care aveau `readme/FISA_CONSULTANT.md` dar nu aveau încă pagină wiki — rămase excluse din backfill-ul precedent. Procesate în paralel prin subagenți `documentarist-wiki`, în 2 loturi (7 + 6). Module: `l10n_ro_account_counterpart`, `l10n_ro_account_vat_journal`, `l10n_ro_anaf_d101`, `l10n_ro_anaf_d103`, `l10n_ro_anaf_fiscal_status`, `l10n_ro_cash_bank_enhanced`, `l10n_ro_cash_register_report`, `l10n_ro_esigiliu`, `l10n_ro_fiscal_audit`, `l10n_ro_payroll_ro`, `l10n_ro_stock_custody`, `l10n_ro_stock_posting_date`, `l10n_ro_vat_on_payment_lock`.
- **Sursă:** `readme/DESCRIPTION.md` (Sumar + Funcționalități Cheie) pentru toate; Componente Cheie completate din analiză de cod unde DESCRIPTION.md nu le acoperea explicit.
- **Fișă consultant:** copiată pentru toate cele 13, cu tot cu capturile din `readme/screenshots/` (total 45 de poze), conform regulii noi din `schema.md`.
- **Avertisment de conținut semnalat de subagent:** `l10n_ro_stock_custody` — `readme/DESCRIPTION.md` declară contabilizarea custodiei date (cont 357) ca fiind în afara scopului modulului, dar codul (`models/stock_picking.py`, `models/res_company.py`) o implementează efectiv (Dr 357 = Cr 371, cu stornare simetrică); pagina wiki documentează comportamentul real din cod și semnalează discrepanța, DESCRIPTION.md rămâne de actualizat separat.
- **Dependențe/Conexiuni:** module fără pagină wiki proprie rămase text `cod` (`account`, `stock`, `account_reports`, `l10n_ro`, `l10n_ro_hr_payroll` etc.); dependențe/conexiuni cu pagină existentă linkate activ (ex. `l10n_ro_profit_tax`, `l10n_ro_anaf_base`, `l10n_ro_anaf_d394`, `l10n_ro_cash_register`, `l10n_ro_anaf_d112`, `l10n_ro_stock_gestiune`, `l10n_ro_anaf_d300`/`l10n_ro_saft_validator`/`l10n_ro_efactura_dedup`).
- **Fișiere actualizate:** 13× `index.md` (pagină nouă) + `FISA_CONSULTANT.md` + `screenshots/`, `wiki_module_odoo/index.md` (13 intrări noi, ordine alfabetică), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-07-02] Copierea fișelor consultant în wiki (backfill 80 module + regulă nouă de ingestie)

- **Acțiune:** Extins fluxul de ingestie: dacă modulul are `readme/FISA_CONSULTANT.md`, fișa se copiază fidel (cu tot cu capturile din `readme/screenshots/`) în directorul wiki al modulului, iar pagina primește linia de metadate `- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)`. La re-ingestie, copia se suprascrie (sursa de adevăr rămâne `readme/` din modul). Backfill executat pe toate modulele deja documentate care au fișă: **80 de fișe copiate, 332 de capturi**, 80 de linii de metadate adăugate. 3 fișe fără capturi (`deltatech_pos`, `deltatech_helpdesk_tag_primary`, `l10n_ro_anaf_base`).
- **Sursă:** `readme/FISA_CONSULTANT.md` + `readme/screenshots/` din fiecare modul.
- **Dependențe/Conexiuni:** neschimbate — doar metadatele paginilor au fost extinse.
- **Fișiere actualizate:** `schema.md` (metadate pagină + pași 5–7 flux de ingestie), 80× `index.md` (linie metadate), 80× `FISA_CONSULTANT.md` + `screenshots/` (copii noi), agentul `documentarist-wiki` (ambele copii: standalone + monorepo), skill-ul `wiki-module` (monorepo), `wiki_module_odoo/.index/` (rebuild lexical), `wiki_module_odoo/log.md`.

## [2026-06-09] Re-ingestie lot l10n_ro_ent (11 module, după corecții de cod + fișe)

- **Acțiune:** Re-ingestate paginile a 11 module din suita `l10n_ro_ent` (repo `terrabit-ro/l10n_ro_ent`, branch `19.0`), procesate în paralel prin subagenți `general-purpose` în 2 loturi (6 + 5). Module: `l10n_ro_deferred_entries`, `l10n_ro_micro_tax`, `l10n_ro_profit_tax`, `l10n_ro_financial_statements`, `l10n_ro_financial_notes`, `l10n_ro_payroll_import`, `l10n_ro_anaf_d100`, `l10n_ro_anaf_d107`, `l10n_ro_anaf_d120`, `l10n_ro_anaf_d390`, `l10n_ro_anaf_d398`. Declanșată de adăugarea capturilor de fișă + corecții de cod în aceste module.
- **Sursă:** `readme/DESCRIPTION.md` (Sumar + Funcționalități) + `USAGE.md`/`FISA_CONSULTANT.md`; secț. 4 reflectată din cod unde diferea de pagina veche.
- **Corecții de conținut notabile:**
  - `l10n_ro_deferred_entries`: pagina veche descria greșit un mecanism `account.asset` + dependență `account_asset` → corectat la mecanismul nativ Enterprise (`deferred_start_date`/`deferred_end_date`, conturi 4711/4721, `post_init_hook`), dependențe `account_accountant`+`l10n_ro`. Actualizată și linia din index.
  - `l10n_ro_anaf_d120`: clarificat că este **Decontul (anual) privind accizele**, nu impozit pe profit; sursă FISA_CONSULTANT corectată.
  - `l10n_ro_profit_tax`: adăugat Registrul de evidență fiscală (`l10n.ro.tax.register`) + corecția credit sponsorizări pe contul 6582.
  - `l10n_ro_financial_statements`: handler unic `l10n.ro.fs.handler`, buton `always_show` pe toate variantele de CPP.
  - `l10n_ro_financial_notes` și `l10n_ro_anaf_d107`: reflectată moștenirea `mail.thread`/`mail.activity.mixin`.
  - Peste tot: corectată sintaxa neconformă `[[...]]` → link-uri Markdown relative active (acolo unde pagina țintă există); versiuni și „Ultima Ingestie" (2026-06-09) actualizate.
- **Fișiere actualizate:** 11 `index.md` (re-scrise), `wiki_module_odoo/index.md` (linia `l10n_ro_deferred_entries` corectată), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-06-09] Mutare suită l10n_ro_intrastat_enhancement (bitshop_ent → l10n_ro_ent)

- **Acțiune:** Modulul `l10n_ro_intrastat_enhancement` a fost mutat fizic din suita `bitshop_ent` în `l10n_ro_ent` (modul de localizare RO, mai potrivit acolo). Verificat înainte: fără conflict de nume, niciun modul nu-l listează în `depends`, dependențele (`l10n_ro_intrastat` Enterprise, `stock_delivery` core) nu se rup. Actualizat în pagina wiki câmpurile **Cale** (`terrabit-ro/l10n_ro_ent`) și **Cale Locală** (`odoo-addons/l10n_ro_ent/l10n_ro_intrastat_enhancement`).
- **Readme:** fragmentele (DESCRIPTION/USAGE/CONFIGURE, scrise în EN cât era în bitshop_ent) au fost retraduse în **RO** + creat CONTEXT.md, conform convenției suitei l10n_ro_ent; `README.rst` regenerat și validat cu generatorul suitei l10n_ro_ent.
- **Fișiere actualizate:** `wiki_module_odoo/l10n_ro_intrastat_enhancement/index.md` (Cale + Cale Locală), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical). Necommitat — git: ștergere în repo `bitshop_ent` + adăugare în repo `l10n_ro_ent` (două commit-uri separate, în sarcina utilizatorului).

## [2026-06-09] Ingestie lot bitshop_ent (11 module)

- **Acțiune:** Documentate cele 11 module reale din suita `bitshop_ent` (repo `terrabit-ro/bitshop_ent`, branch `19.0`), procesate în paralel prin subagenți `general-purpose` în 2 loturi (6 + 5). Module: `deltatech_account_bank_statement_import`, `deltatech_account_enterprise`, `deltatech_account_scenario`, `deltatech_account_scenario_ai`, `deltatech_advanced_planner`, `deltatech_bank_stmt_foreign_currency`, `deltatech_crm_fsm`, `deltatech_helpdesk_tag_primary`, `deltatech_stock_barcode`, `l10n_ro_account_bank_statement_import_xlsx`, `l10n_ro_intrastat_enhancement`. Consolidare centralizată (append + inserare alfabetică în blocul `## Module`).
- **Excluse:** 4 directoare fără `__manifest__.py` (doar `__pycache__`, fără surse) — NU sunt module instalabile: `deltatech_batch_return`, `deltatech_inter_company`, `deltatech_inter_company_vendor_stock`, `deltatech_sale_referrer_raport`.
- **Sursă:** `readme/DESCRIPTION.md` (prezent la 10/11) pentru Sumar și Funcționalități. Componente Cheie (secț. 4) populate doar unde DESCRIPTION/FISA o cereau explicit (`deltatech_account_scenario` tabel Modele, `deltatech_account_scenario_ai` agent AI, `deltatech_helpdesk_tag_primary` din FISA_CONSULTANT). `l10n_ro_intrastat_enhancement` avea DESCRIPTION gol (0 bytes) → sintetizat din manifest + cod (modele/views/wizard/data), secț. 4 completată. Texte EN traduse în RO cu diacritice.
- **Dependențe/Conexiuni (verificate):** linkuri active interne: `deltatech_bank_stmt_foreign_currency` și `l10n_ro_account_bank_statement_import_xlsx` → `deltatech_account_bank_statement_import`; `deltatech_account_scenario_ai` → `deltatech_account_scenario`; `deltatech_stock_barcode` → `deltatech_delivery`, `deltatech_stock_inventory`. Restul (`account`, `account_accountant`, `account_reports`, `account_bank_statement_import(_csv)`, `stock_barcode`, `helpdesk`, `crm`, `project`, `mrp`, `purchase`, `sale_management`, `resource`, `mail`, `ai`, `l10n_ro_intrastat`, `stock_delivery`) rămase text `cod` (fără pagină wiki).
- **Avertismente notabile:** `deltatech_bank_stmt_foreign_currency` marcat `Beta`; `deltatech_account_scenario` are discrepanță deps DESCRIPTION↔manifest (folosit manifestul: `purchase_stock`/`sale_stock`); `l10n_ro_intrastat_enhancement` are `readme/DESCRIPTION.md` gol (de completat la sursă); module Enterprise (helpdesk, stock_barcode, account_reports) nu au încă pagină wiki.
- **Fișiere actualizate:** 11 `index.md` noi, `wiki_module_odoo/index.md` (11 intrări inserate alfabetic), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-06-08] Ingestie lot l10n-romania (22 module RO)

- **Acțiune:** Documentate 22 module rămase nedocumentate din suita `l10n-romania` (repo `dhongu/l10n-romania`, branch `19.0`), procesate în paralel prin subagenți `general-purpose` în 4 loturi (~6). Module: `l10n_ro_account_edi_ubl`, `l10n_ro_account_report`, `l10n_ro_account_sequence`, `l10n_ro_balance_confirmation`, `l10n_ro_cash_register`, `l10n_ro_edi_ubl_sale_store`, `l10n_ro_efactura_enhancement`, `l10n_ro_etransport_enhancement`, `l10n_ro_footer_anpc`, `l10n_ro_invoice_report`, `l10n_ro_lang`, `l10n_ro_message_spv_purchase`, `l10n_ro_partner_create_by_vat_button`, `l10n_ro_partner_create_by_vat_openapi`, `l10n_ro_sale_order_report`, `l10n_ro_stock_account_enhancement`, `l10n_ro_stock_age_report`, `l10n_ro_stock_picking_report`, `l10n_ro_stock_picking_report_product_expiry`, `l10n_ro_stock_report`, `l10n_ro_zip`, `terrabit_dvi`. Consolidare centralizată (append + re-sortare alfabetică, 305 module total).
- **Sursă:** `readme/DESCRIPTION.md` (prezent la 21/22) pentru Sumar și Funcționalități; `l10n_ro_account_edi_ubl` și `l10n_ro_stock_picking_report_product_expiry` aveau DESCRIPTION gol → sintetizat din manifest + cod. Componente Cheie (secț. 4) populate doar unde DESCRIPTION conținea o secțiune tehnică (efactura/etransport/balance_confirmation/message_spv_purchase), altfel omise conform prioritizării Readme. Texte EN traduse în RO cu diacritice; cedila corectată la `terrabit_dvi`.
- **Dependențe/Conexiuni (verificate):** `l10n_ro_stock_picking_report_product_expiry` → link activ la `l10n_ro_stock_picking_report`. Restul dependențelor (`account`, `l10n_ro`, `l10n_ro_edi`, `l10n_ro_config`, `website`, `purchase`, `sale`, `l10n_ro_stock`, `l10n_ro_stock_account`, `base_address_extended`, `l10n_ro_city`) rămase text `cod` (fără pagină wiki).
- **Avertismente notabile:** `l10n_ro_account_edi_ubl` e modul gol bridge/legacy (`auto_install=True`, logica în `l10n_ro_edi`); `l10n_ro_message_spv_purchase` avea „Odoo 17.0" în DESCRIPTION (folosit manifest 19.0); `l10n_ro_invoice_report` cere `num2words`; `l10n_ro_zip`/`l10n_ro_stock_age_report` au `post_init_hook` (import/recalcul la instalare); `terrabit_dvi` și `l10n_ro_stock_picking_report` declară `excludes` (incompatibilități reciproce — notate la Conexiuni); README/INSTALL la `l10n_ro_stock_report` mai menționează branch 15.0 (text moștenit).
- **Fișiere actualizate:** 22 `index.md` noi, `wiki_module_odoo/index.md` (re-sortat, 305 module), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical).

## [2026-06-08] Re-ingestie l10n_ro_anaf_messages (corecție mecanism transport)

- **Acțiune:** Re-ingestat `l10n_ro_anaf_messages` (repo `terrabit-ro/l10n_ro_ent`, branch `19.0`) pentru a rezolva discrepanța readme↔cod semnalată la ingestia anterioară. Verificat codul real (`models/anaf_spv_client.py`, `res_company.py`, `l10n_ro_anaf_message.py`, `l10n_ro_anaf_agent_job.py`): conexiunea la SPVWS2 se face **prin Agentul Terrabit (mTLS)**, nu prin OAuth2 Bearer. Sursa adevărată = manifestul + codul; `readme/DESCRIPTION.md` (care descria OAuth2 via `l10n_ro_edi`) era greșit și a fost rescris la realitate, alături de docstring-ul învechit din `l10n_ro_anaf_message.py`.
- **Sursă:** `readme/DESCRIPTION.md` (rescris) pentru Sumar și Funcționalități; mecanismul confirmat în cod (apel `make_spv_request` către agent local pe `localhost` cu `X-Agent-Token`; model cloud prin push/job `sync_messages`). Componente Cheie omise conform prioritizării Readme.
- **Dependențe/Conexiuni:** dependențe link activ la `l10n_ro_anaf_base` și `l10n_ro_anaf_agent`. Conexiuni: `l10n_ro_anaf_agent` (transport mTLS), `l10n_ro_anaf_submission` (recipise complementare), `l10n_ro_message_spv` (e-Factura, separat — text `cod`). Eliminată conexiunea înșelătoare către `l10n_ro_edi` (nu se refolosește tokenul OAuth pentru transport).
- **Fișiere actualizate:** `wiki_module_odoo/l10n_ro_anaf_messages/index.md` (rescris secț. 1, 2, 5), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical). Sursă corectată în paralel în repo modul: `readme/DESCRIPTION.md` și docstring `l10n_ro_anaf_message.py`.

## [2026-06-08] Ingestie lot l10n_ro_ent (6 module ANAF/fiscal)

- **Acțiune:** Documentate 6 module rămase nedocumentate din suita `l10n_ro_ent` (repo `terrabit-ro/l10n_ro_ent`, branch `19.0`), procesate în paralel prin 6 subagenți `general-purpose`: `l10n_ro_anaf_agent`, `l10n_ro_anaf_messages`, `l10n_ro_anaf_submission`, `l10n_ro_cost_centers`, `l10n_ro_pos_fiscal_compliance`, `l10n_ro_saft_etva`. Consolidare centralizată (append + re-sortare alfabetică a blocului `## Module`, 283 module total).
- **Sursă:** `readme/DESCRIPTION.md` (prezent la toate) pentru Sumar și Funcționalități Cheie; context suplimentar din `FISA_CONSULTANT.md`/`USAGE.md` unde existau (cost_centers, pos_fiscal_compliance, saft_etva). Componente Cheie (secț. 4) omise conform prioritizării Readme. Toate textele în RO cu diacritice (DESCRIPTION-uri EN traduse).
- **Dependențe/Conexiuni (verificate în manifest):** `l10n_ro_anaf_agent` → link activ la `l10n_ro_anaf_base`; `l10n_ro_anaf_submission` → link la `l10n_ro_anaf_base`; `l10n_ro_saft_etva` → link la `l10n_ro_anaf_d300`; `l10n_ro_pos_fiscal_compliance` → link la `deltatech_pos`. Dependențe core (`account`, `l10n_ro`, `point_of_sale`, `analytic`, `mail`, `l10n_ro_reports`) rămase text `cod`.
- **Avertisment notabil:** la `l10n_ro_anaf_messages` există o discrepanță readme↔cod — `DESCRIPTION.md` descrie acces OAuth2 (via `l10n_ro_edi`), dar `__manifest__.py` indică transport mTLS prin Agentul Terrabit și depinde de `l10n_ro_anaf_base` + `l10n_ro_anaf_agent`. Pagina respectă DESCRIPTION la secț. 1–2 și manifestul la secț. 3; `DESCRIPTION.md` pare învechit și ar trebui aliniat la implementarea actuală. Module preponderent Beta, licențe OPL-1; certSIGN Cloud încă stub în `l10n_ro_anaf_submission`.
- **Fișiere actualizate:** 6 `index.md` noi, `wiki_module_odoo/index.md` (re-sortat, 283 module), `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical; vectorii se regenerează cu `--embed`).

## [2026-06-08] Ingestie l10n_ro_account_storno (suita l10n-romania)

- **Acțiune:** Adăugată o pagină nouă pentru `l10n_ro_account_storno` (repo `dhongu/l10n-romania`, branch `19.0`). Motiv: o interogare de test („cum inversez o cheltuială greșită pe clasa 6") nu găsea niciun modul de storno — diagnostic: modulul nu era documentat (gol de acoperire), nu o problemă de retrieval. Modul mic, documentat direct.
- **Sursă:** `readme/DESCRIPTION.md` (prezent, EN → tradus RO) pentru Sumar și Funcționalități. Componente Cheie ancorate ușor în cod (modele `account.move`/`account.move.line`, `account.account`, `res.company`; `post_init_hook`) conform mențiunilor din DESCRIPTION.
- **Dependențe/Conexiuni:** dependențe `account` și `l10n_ro` (fără pagină wiki → text `cod`). Fără conexiuni inventate; notat doar că oferă mecanismul de bază pentru înregistrări negative folosit indirect de alte module.
- **Avertismente notabile:** licență AGPL-3, `development_status: Production/Stable`, autor „Dorin Hongu, Terrabit, OCA". Are `post_init_hook`.
- **Fișiere actualizate:** `wiki_module_odoo/l10n_ro_account_storno/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (rebuild lexical; vectorii se regenerează separat cu `--embed`).

## [2026-06-08] Ingestie terrabit_helpdesk_link (suita terrabit)

- **Acțiune:** Adăugată o pagină nouă pentru modulul `terrabit_helpdesk_link` (repo `terrabit-ro/terrabit`, branch `19.0`). Modul minuscul (un meniu + o acțiune URL), documentat direct (fără subagent). Demonstrație a fluxului ingestie → push → interogare (`wiki-query`).
- **Sursă:** `readme/DESCRIPTION.md` prezent dar gol (doar „Features:") → Sumar și Funcționalități Cheie sintetizate din `__manifest__.py` + cod; Componente Cheie ancorate în `views/menu_link.xml` (nu există modele).
- **Dependențe/Conexiuni:** singura dependență din manifest este `base` (fără pagină wiki → text `cod`). Nicio conexiune funcțională verificată către alte module cu pagină.
- **Avertismente notabile (cod/manifest, nu wiki):** licență LGPL-3, `development_status: Beta`, autor „Terrabit, Dan Stoica". Acțiunea `ir.actions.act_url` deschide `https://www.terrabit.ro/helpdesk` în filă nouă; meniu restrâns la `base.group_user`.
- **Fișiere actualizate:** `wiki_module_odoo/terrabit_helpdesk_link/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`, `wiki_module_odoo/.index/` (reconstruit).

## [2026-06-03] Finalizare documentare suita deltatech (70 module)

- **Acțiune:** Documentate toate cele 70 module deltatech rămase nedocumentate (repo `dhongu/deltatech`, branch `19.0`), încheind suita deltatech (120 module cu manifest, toate au acum pagină și intrare în index). Analiza delegată subagenților `general-purpose` în 10 loturi paralele de ~7. `deltatech_partner_generic`, `deltatech_product_mpn` și `deltatech_restrict_ip` (acesta din bitshop) și-au auto-adăugat intrarea; restul consolidate centralizat prin append + re-sortare alfabetică a blocului `## Module`.
- **Sursă:** `readme/DESCRIPTION.md` (prezent la majoritate) pentru Sumar și Funcționalități Cheie; Componente Cheie ancorate în cod doar unde DESCRIPTION era gol/sumar (frecvent — multe readme-uri deltatech au o singură linie). Texte EN traduse în RO cu diacritice.
- **Confirmări de denumire/scop (verificate în cod):** `deltatech_ral` = pigmenți de culoare RAL în BOM; `deltatech_record_type` = tipuri de înregistrare (folosit de `deltatech_marketplace_sale_type`); `deltatech_sms` = gateway 4Pay/Wapi (înlocuiește IAP); `deltatech_transport_change` = transport de **configurație** între medii prin Git (NU transport marfă); `deltatech_test_system` = marcaj test/producție; `deltatech_watermark` = câmp de bază filigran (consumat de `deltatech_website_watermark` din bitshop); `deltatech_queue_job` = îmbunătățiri queue_job pentru Odoo.sh.
- **Lanțuri/conexiuni reale activate:** `deltatech_sms` ← `deltatech_sms_sale`; `deltatech_purchase_add_extra_line` ↔ `deltatech_sale_add_extra_line`; `deltatech_watermark` → `deltatech_website_watermark`; `deltatech_website_city` → `deltatech_delivery_locker_website`; `deltatech_product_list`/`deltatech_website_short_description` → `deltatech_feed`; `deltatech_record_type` → `deltatech_marketplace_sale_type`; `deltatech_sale_stage` → `deltatech_marketplace_sale_stage`; `deltatech_warehouse_arrangement`/`deltatech_putaway_strategy` → `deltatech_warehouse_map`; `deltatech_stock_delivery` → familia `deltatech_invoice_*`. Dependențe core (`sale`, `stock`, `purchase`, `account`, `website_sale`, `web`, `mail`) rămase text `cod`.
- **Avertismente notabile (cod/readme, nu wiki):** multe readme-uri foarte sumare (o linie) — Sumar/Funcționalități sintetizate din cod; texte de versiune veche în readme (`deltatech_record_type` „17.0", `deltatech_project_price_list` exemple `odoo18.conf`); inconsecvențe cod semnalate doar informativ: `deltatech_ral` `create` fără `@api.model_create_multi`, `deltatech_warehouse_arrangement` precedență `_compute_full_name` + f-string în `_()`, `deltatech_website_price_without_tax` cheie QWeb nepotrivită, `deltatech_product_trade_markup` metode stub `pass`. Multe module Beta/Alpha și OPL-1.
- **Fișiere actualizate:** 70 `index.md` noi, `wiki_module_odoo/index.md` (re-sortat, 275 module total), `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie deltatech_product_mpn (suita deltatech)

- **Acțiune:** Adăugată o pagină nouă pentru modulul `deltatech_product_mpn` (repo `dhongu/deltatech`, branch `19.0`). Modul mic, documentat direct (fără subagent).
- **Sursă:** `readme/DESCRIPTION.md` (prezent) pentru Sumar și Funcționalități Cheie; Componente Cheie omise conform prioritizării Readme (notat doar la nivel general: extindere `product.template` cu câmpul MPN + vizualizare `views/product_template_view.xml`). Text EN tradus în RO cu diacritice. Nu există `readme/USAGE.md` sau `readme/FISA_CONSULTANT.md`.
- **Dependențe/Conexiuni:** singura dependență din manifest este `product` (fără pagină wiki → text `cod`). Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki.
- **Avertismente notabile (cod/manifest, nu wiki):** licență OPL-1 (comercial), `development_status: Mature`, autor „Terrabit, Voicu Stefan". DESCRIPTION.md în engleză (tradus la ingestie). Fără greșeli de versiune în readme.
- **Fișiere actualizate:** `wiki_module_odoo/deltatech_product_mpn/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

---

## [2026-06-03] Ingestie deltatech_partner_generic (suita deltatech)

- **Acțiune:** Adăugată o pagină nouă pentru modulul `deltatech_partner_generic` (repo `dhongu/deltatech`, branch `19.0`). Modul mic, documentat direct (fără subagent).
- **Sursă:** `readme/DESCRIPTION.md` (prezent) pentru Sumar și Funcționalități Cheie; Componente Cheie omise conform prioritizării Readme. Text EN tradus în RO cu diacritice.
- **Dependențe/Conexiuni:** singura dependență din manifest este `sale` (fără pagină wiki → text `cod`). Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki.
- **Avertismente notabile (cod/manifest, nu wiki):** `summary` din manifest conține o greșeală de tipar („Gneric partner"); `development_status: Mature`, licență LGPL-3. Cod sursă neanalizat (există modele/vederi pentru setarea partenerului generic în `res.config.settings`, dar nedetaliate datorită prioritizării Readme).
- **Fișiere actualizate:** `wiki_module_odoo/deltatech_partner_generic/index.md` (nou), `wiki_module_odoo/index.md`, `wiki_module_odoo/log.md`.

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
---

## [2026-08-14] Ingest: `deltatech_mrp_bom_formula`

- **Acțiune:** Ingestat modulul nou `deltatech_mrp_bom_formula` (19.0.1.0.0).
- **Detalii:** Pagina a fost generată din `readme/DESCRIPTION.md` pentru sumar și funcționalități, completată cu analiza modelelor și a vizualizărilor pentru secțiunea de componente cheie. Fișa de consultant și capturile aferente au fost copiate din `readme/`.
- **Fișiere actualizate:**
    - `wiki_module_odoo/deltatech_mrp_bom_formula/index.md`
    - `wiki_module_odoo/deltatech_mrp_bom_formula/FISA_CONSULTANT.md`
    - `wiki_module_odoo/deltatech_mrp_bom_formula/screenshots/`
    - `wiki_module_odoo/index.md`
    - `wiki_module_odoo/log.md`

---

## [2026-08-20] Re-ingest: `deltatech_sale_margin`, `deltatech_sale_commission`

- **Acțiune:** Actualizate paginile existente după introducerea politicii configurabile de reacție la vânzarea sub cost (`res.company.sale_margin_check_mode`): `deltatech_sale_margin` 19.0.1.1.0 → 19.0.1.2.0, `deltatech_sale_commission` 19.0.1.4.3 → 19.0.1.5.0.
- **Detalii:** Sumarul și funcționalitățile reflectă cele trei moduri (blochează / doar avertisment / fără verificare, implicit blochează — comportamentul istoric rămâne neschimbat), marcajul de linie `margin_below_limit`, garda de unitate la comparația preț↔cost și expunerea pragului „Limită de marjă" în Setări. Secțiunea de componente a fost completată la `deltatech_sale_margin` pentru câmpurile și vizualizările referite de alte module. La `deltatech_sale_commission` s-a precizat că constrângerea de pe linia de factură respectă aceeași politică. Niciunul dintre cele două module nu are fișă de consultant, deci nu s-a copiat nimic în wiki.
- **Fișă consultant:** `deltatech_sale_margin` a primit fișă de consultant (nu avea), cu 2 capturi generate din `tests/test_screenshots.py`; fișa și capturile au fost copiate în wiki. `deltatech_sale_commission` nu are fișă.
- **Fișiere actualizate:**
    - `wiki_module_odoo/deltatech_sale_margin/index.md`
    - `wiki_module_odoo/deltatech_sale_margin/FISA_CONSULTANT.md`
    - `wiki_module_odoo/deltatech_sale_margin/screenshots/`
    - `wiki_module_odoo/deltatech_sale_commission/index.md`
    - `wiki_module_odoo/index.md`
    - `wiki_module_odoo/log.md`
