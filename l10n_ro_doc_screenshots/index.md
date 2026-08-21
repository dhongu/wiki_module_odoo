# Romania - Tooling capturi fișe consultant (localizat la `l10n_ro_doc_screenshots/index.md`)

- **Nume Tehnic:** `l10n_ro_doc_screenshots`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_doc_screenshots
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doc_screenshots`
- **Ultima Ingestie:** 2026-08-20

#### 1. Sumar

Modul de **tooling de dezvoltare** — nu adaugă funcționalitate de business, fiind ascuns din Odoo Apps (`hidden: True`). Oferă mixinul `ScreenshotCase` pentru generarea **automată** a capturilor de ecran folosite în fișele consultant (`<modul>/readme/screenshots/`), pornind de la date seedate determinist în teste. Mecanismul combină `HttpCase` (serverul Odoo + tranzacția testului) cu **Playwright** (Chrome de sistem) pentru navigare și capturi cu nume curate, scrise direct în directorul de capturi al modulului consumator. Autentificarea se face prin cookie de sesiune.

#### 2. Funcționalități Cheie

- `ScreenshotCase` — clasă de bază (`HttpCase`) reutilizabilă în orice modul consumator; descrie capturile ca listă de dict-uri și le generează dintr-o singură comandă (`capture_screenshots`).
- `prepare_ro_company` — seedează compania cu date RO (țară, monedă RON, CUI, adresă), acordă drepturi contabile adminului, activează limba română și tema luminoasă.
- `prepare_demo_company` — alternativă pentru module cu date demo pre-populate (ex. facturi din localizarea RO).
- `account_move_shot` — helper pentru captura unui formular `account.move` cu tab-ul „Journal Items"/„Elemente jurnal" deschis (liniile Dr/Cr vizibile).
- `report_shot` — captură pentru un raport tipăribil (PDF), randat ca HTML prin `/report/html/<report_ref>/<res_id>`, fără a depinde de wkhtmltopdf în mediul de test.
- `xlsx_shot` / `xlsx_to_html` — randează prima foaie a unui XLSX generat ca tabel HTML stilizat, pentru capturi din exporturi.
- `xml_excerpt` — formatează (pretty-print) un extras dintr-un XML generat (D300/D390/e-Factura etc.), gata de inserat în fișă între ``` ```xml ``` ```.
- Opțiunea `highlight` per captură evidențiază selectoare CSS/Playwright cu contur portocaliu Odoo și buline numerotate ①②③, pentru a indica exact pașii din fișă.
- Opțiuni suplimentare per captură: `full`, `wait`, `hover`, `click_btn`, `click_tab` (cu traducere automată RO), `unfold_report` (desfășoară toate liniile pliabile dintr-un `account.report`), `hide_fields`, `eval`, `hide_chatter`, `settle`.
- `_autotrim` — decupează automat marginile uniforme ale capturii (elimină spațiul gol, gestionează și fundaluri neuniforme, ex. chatter alb lângă raport gri).
- Degradare elegantă: dacă `playwright` lipsește din mediul Odoo, testele de capturi se sar (`skipTest`) fără a bloca suita; testele sunt sărite explicit pe CI prin variabila `SKIP_FISE_SCREENSHOTS`.

Sursă: `readme/DESCRIPTION.md` + docstring-ul din `screenshot_case.py` (Componentele Cheie de mai jos completează cu detalii tehnice din cod, dat fiind caracterul de tooling al modulului).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

Modul de tooling — nu definește sau extinde modele Odoo de business.

**Vizualizări**

Nu definește vizualizări sau date (`"data": []` în manifest); întreaga logică se află în clasa Python `ScreenshotCase` din `tests/screenshot_case.py`.

**Acțiuni Automate / Acțiuni Server**

- Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`. Generarea capturilor se declanșează manual, per modul consumator, prin `--test-tags=fise_screenshots` (test `HttpCase`, nu o acțiune de sistem).

#### 5. Conexiuni

- [l10n_ro_process_library](../l10n_ro_process_library/index.md): singurul modul care are `l10n_ro_doc_screenshots` ca **dependență formală** în manifest (nu doar import defensiv în teste); extinde `ScreenshotCase` pentru capturile procesele de business documentate acolo.
- Zeci de module din `l10n_ro_ent`, `deltatech`, `deltatech_stock_valuation`, `bitshop`/`bitshop_ent` și din arborele `proiecte/` (ex. `l10n_ro_anaf_d300`, `l10n_ro_fixed_assets`, `deltatech_advanced_planner`, `terrabit_apps_base` etc.) importă defensiv `ScreenshotCase` în propriile `tests/test_screenshots.py`, fără dependență de manifest — dacă modulul de tooling lipsește de pe disc, testul de capturi pur și simplu nu se definește. Nefiind dependențe reale de business, nu sunt listate individual aici.
