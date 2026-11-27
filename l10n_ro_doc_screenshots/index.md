# Romania - Tooling capturi fișe consultant (localizat la `l10n_ro_doc_screenshots/index.md`)

- **Nume Tehnic:** `l10n_ro_doc_screenshots`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_doc_screenshots
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doc_screenshots`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Ultima Ingestie:** 2026-11-27

#### 1. Sumar

Modul **punte** de tooling de dezvoltare, păstrat pentru compatibilitate — nu adaugă funcționalitate de business și este ascuns din Odoo Apps (`hidden: True`, categoria `Hidden`). Mixinul `ScreenshotCase`, care generează automat capturile de ecran folosite în fișele consultant, s-a mutat în modulul `deltatech_doc_screenshots` din suita deltatech (repo public), ca orice suită și CI-ul ei să-l poată folosi fără acces la un repo privat. Acest modul îl reexportă, așa că testele de capturi existente, care importă din `l10n_ro_doc_screenshots`, merg mai departe fără modificări. Pentru module noi se recomandă importul direct din `deltatech_doc_screenshots`. Modulul este gratuit pe Odoo Apps și are propria fișă consultant.

#### 2. Funcționalități Cheie

- **Reexport al `ScreenshotCase`** — `tests/screenshot_case.py` importă din `odoo.addons.deltatech_doc_screenshots.tests.screenshot_case`, deci importurile `odoo.addons.l10n_ro_doc_screenshots.tests.screenshot_case` rămân valide.
- **Înlocuitor de rezervă** — dacă suita deltatech nu e în calea de addon-uri (CI-ul obișnuit al suitei), puntea exportă un `ScreenshotCase` (`HttpCase`) care sare testul în `setUpClass` cu mesajul „deltatech_doc_screenshots nu e în calea de addon-uri.". Astfel consumatorii sunt săriți, nu cad pe metodele mixinului (`prepare_ro_company`), iar registrul se încarcă.
- **Fără dependență formală** de `deltatech_doc_screenshots`: nu e în `depends`, ca bazele instalate să nu fie afectate.
- **Test propriu de capturi** (`tests/test_screenshots.py`, tag `fise_screenshots`): capturează formularul companiei demo, cu câmpuri evidențiate, în română (fișa) și în engleză (`static/description/en/`), trecând prin punte, exact ca modulele documentate.
- **Generare doar la cerere**: capturile se produc numai cu `--test-tags=fise_screenshots` (sau `FISE_SCREENSHOTS=1`); altfel testul e sărit. Comandă: `-i <modul>,l10n_ro_doc_screenshots,deltatech_doc_screenshots --test-tags=fise_screenshots --stop-after-init`.
- **Cerințe de mediu** pentru generare (descrise în `deltatech_doc_screenshots`): `playwright` + `playwright install chrome`, `websocket-client`, `openpyxl`, opțional `pillow`.
- Opțiunile capturilor (`highlight`, `click_tab`, `unfold_report`, `xlsx_shot`, `report_shot`, `prepare_ro_company` etc.) sunt documentate acum în `deltatech_doc_screenshots`, nu aici.

Sursă: `readme/DESCRIPTION.md` + `readme/USAGE.md` + `readme/HISTORY.md` (20.0.1.2.0) + `tests/screenshot_case.py`, `tests/test_screenshots.py`.

#### 3. Dependențe

- `web`

(Fără dependență formală de `deltatech_doc_screenshots`, care furnizează mixinul propriu-zis.)

#### 4. Componente Cheie

**Modele**

Modul de tooling — nu definește sau extinde modele Odoo.

**Vizualizări**

Nu definește vizualizări sau date (`"data": []`); logica se reduce la reexportul din `tests/screenshot_case.py` și testul `tests/test_screenshots.py`.

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`. Capturile se declanșează manual prin `--test-tags=fise_screenshots`.

#### 5. Conexiuni

- `deltatech_doc_screenshots` (suita deltatech, fără pagină wiki): sursa reală a mixinului `ScreenshotCase`, reexportat de această punte.
- [l10n_ro_process_library](../l10n_ro_process_library/index.md): are `l10n_ro_doc_screenshots` ca dependență formală în manifest (preluat din pagina anterioară; neverificat în această ingestie) și extinde `ScreenshotCase` pentru capturile proceselor documentate acolo.
- Zeci de module din `l10n_ro_ent`, deltatech, bitshop și `proiecte/` importă defensiv `ScreenshotCase` prin această punte în `tests/test_screenshots.py`, fără dependență de manifest; nu sunt listate individual.
