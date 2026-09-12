# Romania - Tooling capturi fișe consultant (localizat la `l10n_ro_doc_screenshots/index.md`)

- **Nume Tehnic:** `l10n_ro_doc_screenshots`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_doc_screenshots
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doc_screenshots`
- **Ultima Ingestie:** 2026-09-12

#### 1. Sumar

Modul de **tooling de dezvoltare** — nu adaugă funcționalitate de business, fiind ascuns din Odoo Apps (`hidden: True`). Oferă mixinul `ScreenshotCase` pentru generarea **automată** a capturilor de ecran folosite în fișele consultant (`<modul>/readme/screenshots/`), pornind de la date seedate determinist în teste. Mecanismul combină `HttpCase` (serverul Odoo + tranzacția testului) cu **Playwright** (Chrome de sistem) pentru navigare și capturi cu nume curate, scrise direct în directorul de capturi al modulului consumator. Autentificarea se face prin cookie de sesiune. Din versiunea 19.0.1.1.0, capturile se generează **doar la cerere explicită** — orice altă rulare de teste le sare, ca să nu apară diff-uri binare (`.png`) în mijlocul altei modificări.

#### 2. Funcționalități Cheie

- `ScreenshotCase` — clasă de bază (`HttpCase`) reutilizabilă în orice modul consumator; descrie capturile ca listă de dict-uri și le generează dintr-o singură comandă (`capture_screenshots`).
- **Generare doar la cerere** (`_screenshots_requested`) — capturile se produc numai dacă rularea le cere explicit, prin una din:
  - `--test-tags` conține tagul propriu al clasei, terminat în `_screenshots` (ex. `fise_screenshots`, `shopify_screenshots`);
  - `--test-tags` numește clasa direct, ex. `--test-tags=/<modul>:TestXScreenshots`;
  - variabila de mediu `FISE_SCREENSHOTS=1`, pentru scripturi care declanșează generarea altfel.
  O rulare obișnuită (`-u <modul> --test-tags=/<modul>`) NU cere capturi — testul e sărit (`skipTest`), cu motivul afișat în raport. `SKIP_FISE_SCREENSHOTS=1` rămâne un veto peste orice cerere (îl folosește CI-ul).
- `prepare_ro_company` — seedează compania cu date RO (țară, monedă RON, CUI, adresă), acordă drepturi contabile adminului, activează limba română și tema luminoasă; maschează complet identitatea companiei (nume, NRC, IBAN, telefon, județ, footer de raport) — util când capturile se generează pe o copie de bază de client, singurul loc cu un plan de conturi RO real.
- `prepare_demo_company` — alternativă pentru module cu date demo pre-populate (ex. facturi din localizarea RO).
- `force_light_theme` — forțează tema luminoasă pe admin (câmpul Enterprise `res.users.settings.color_scheme`), indiferent de preferința din baza de date; apelat automat din `prepare_ro_company` / `prepare_demo_company`.
- `account_move_shot` — helper pentru captura unui formular `account.move`, deschis prin acțiunea jurnalului (breadcrumb cu context, nu formular gol), cu tab-ul „Journal Items"/„Elemente jurnal" deschis (liniile Dr/Cr vizibile).
- `report_shot` — captură pentru un raport tipăribil (PDF), randat ca HTML prin `/report/html/<report_ref>/<res_id>`, fără a depinde de wkhtmltopdf în mediul de test.
- `xlsx_shot` / `xlsx_to_html` — randează prima foaie a unui XLSX generat ca tabel HTML stilizat, pentru capturi din exporturi.
- `xml_excerpt` — formatează (pretty-print) un extras dintr-un XML generat (D300/D390/e-Factura etc.), gata de inserat în fișă între ``` ```xml ``` ```.
- Opțiunea `highlight` per captură evidențiază selectoare CSS/Playwright cu contur portocaliu Odoo și buline numerotate ①②③, pentru a indica exact pașii din fișă.
- Opțiuni suplimentare per captură: `full`, `wait`, `hover`, `click_btn`, `click_tab` (încearcă și eticheta română a tab-ului, interfața fiind capturată în română), `unfold_report` (desfășoară toate liniile pliabile dintr-un `account.report`), `hide_fields`, `eval`, `hide_chatter`, `settle`.
- `capture_screenshots(..., hide_systray=True)` — ascunde bara de sistray (AI, notificări, Studio, meniu debug) și tooltip-uri rămase, injectat ca `<style>` ca să supraviețuiască re-randărilor OWL.
- `_autotrim` — decupează automat marginile uniforme ale capturii (elimină spațiul gol, gestionează și fundaluri neuniforme, ex. chatter alb lângă raport gri).
- Lățime de viewport implicită `(1920, 950)` — încape tabelele `account.report` cu multe coloane (la 1600px se tăiau coloanele din dreapta).
- Comandă de rulare (cere explicit capturile): `./odoo/odoo-bin -c odoo.conf -d <db> -u <modul>,l10n_ro_doc_screenshots --test-tags=fise_screenshots --stop-after-init --http-port=<liber> --gevent-port=<liber>`; capturile se scriu în `<modul>/readme/screenshots/`.
- Degradare elegantă: dacă `playwright` lipsește din mediul Odoo, testele de capturi se sar (`skipTest`) fără a bloca suita; testele sunt sărite explicit pe CI prin variabila `SKIP_FISE_SCREENSHOTS`. Necesită și `websocket-client` (comunicare CDP) și, opțional, `pillow` (pentru `_autotrim`; fără el, captura rămâne netăiată) + `playwright install chrome`.
- Parcurgere manuală/diagnoză alternativă printr-un browser controlat (Preview MCP) atașat la o instanță deja rulantă — util pentru diagnoză de mediu (cod vechi în memoria unui server dev), dar capturile „de producție" rămân cele generate determinist de test.

Sursă: `readme/DESCRIPTION.md` + `readme/USAGE.md` + `readme/HISTORY.md` (schimbarea „doar la cerere" din 19.0.1.1.0) + docstring-ul din `screenshot_case.py` (Componentele Cheie de mai jos completează cu detalii tehnice din cod, dat fiind caracterul de tooling al modulului).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

Modul de tooling — nu definește sau extinde modele Odoo de business.

**Vizualizări**

Nu definește vizualizări sau date (`"data": []` în manifest); întreaga logică se află în clasa Python `ScreenshotCase` din `tests/screenshot_case.py`.

**Acțiuni Automate / Acțiuni Server**

- Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`. Generarea capturilor se declanșează manual, per modul consumator, prin `--test-tags=fise_screenshots` (sau tagul echivalent al clasei, sau `FISE_SCREENSHOTS=1`), nu printr-o acțiune de sistem.

#### 5. Conexiuni

- [l10n_ro_process_library](../l10n_ro_process_library/index.md): singurul modul care are `l10n_ro_doc_screenshots` ca **dependență formală** în manifest (nu doar import defensiv în teste); extinde `ScreenshotCase` pentru capturile proceselor de business documentate acolo.
- Zeci de module din `l10n_ro_ent`, `deltatech`, `deltatech_stock_valuation`, `bitshop`/`bitshop_ent` și din arborele `proiecte/` (ex. `l10n_ro_anaf_d300`, `l10n_ro_fixed_assets`, `deltatech_advanced_planner`, `terrabit_apps_base` etc.) importă defensiv `ScreenshotCase` în propriile `tests/test_screenshots.py`, fără dependență de manifest — dacă modulul de tooling lipsește de pe disc, testul de capturi pur și simplu nu se definește. Nefiind dependențe reale de business, nu sunt listate individual aici.
