# Bibliotecă de Procese (Business Process) (localizat la `l10n_ro_process_library/index.md`)

- **Nume Tehnic:** `l10n_ro_process_library`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_process_library
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_process_library`
- **Ultima Ingestie:** 2026-08-20

#### 1. Sumar

Modulul livrează o bibliotecă versionată de procese de implementare (peste 50 de procese contabile și operaționale românești), organizată ca un catalog de foldere pe care consultantul le importă selectiv într-un proiect din `deltatech_business_process`. Nu adaugă funcționalitate de business proprie: furnizează conținutul (definiții JSON, fișe HTML, capturi) pe care motorul de import și cadrul de procese îl consumă.

#### 2. Funcționalități Cheie

- Catalog de procese organizat ca foldere `processes/<COD>_<slug>/` cu `process.json` (definiția: cod, arie, pași, teste UAT, module legate), `fisa.html` (fișa generată) și `screenshots/` (capturi opționale).
- Peste 50 de procese acoperind ariile: CB (Cash & Banking — e-Factură, mesaje SPV, reconcilieri, registru de casă), DEC (declarații fiscale D300/D390/D394/D398/D112/D107/D100/D120/D205/D207/D318/D406), TVA (regularizare, rambursare, grup fiscal, pro-rată, prag OSS, TVA la încasare), IMO (mijloace fixe, obiecte de inventar), INC (închidere perioadă/an, situații financiare, impozit profit/micro), OPS (dividende, leasing, provizioane, subvenții, CBAM, SGR, accize, diurne), TRZ (trezorerie, reevaluări valutare, plată obligații buget), ST (inventariere fizică).
- Import selectiv din wizardul `business.process.import` (parte din `deltatech_business_process`), cu sursa „Bibliotecă de procese" alături de varianta „Fișier exportat JSON".
- Contribuție automată de procese: orice modul instalat care respectă convenția `processes/<COD>_nume/process.json` (fără declarație suplimentară în manifest) e descoperit automat de motorul din `deltatech_business_process`, grupat pe modulul-sursă.
- La import se creează `business.process` legat de proiect, se leagă modulele după numele tehnic, se creează pașii și un test UAT cu step-tests; reimportul e idempotent per proiect + cod proces.
- Atașarea automată a fișelor ca PDF pe proces (smart button „Documents"): fișa procesului (`Fisa_<COD>.pdf`, din `fisa.html`) și fișa fiecărui modul legat (`Fisa_modul_<modul>.pdf`, din `readme/FISA_CONSULTANT.md`), cu fallback la HTML dacă wkhtmltopdf lipsește.
- Capturi pentru fișele modulelor legate provin din `<modul>/readme/screenshots/`, generate de mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`; capturile proprii proceselor se generează cu `ProcessScreenshotCase` din `tests/common.py`.
- Instrument `tools/fisa_generator.py` pentru generarea fișei HTML a unui proces nou dintr-un `process.json`.

#### 3. Dependențe

- [deltatech_business_process](../deltatech_business_process/index.md)
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md)

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni proprii — este un modul de conținut pur (date + tooling). Logica de import, descoperire automată și modelul `business.process.library` sunt implementate în `deltatech_business_process` (vezi pagina sa de wiki pentru detalii tehnice); acest modul contribuie exclusiv:

- Directorul `processes/` — peste 50 de subdirectoare `<COD>_<slug>/` cu `process.json` + `fisa.html` (+ `screenshots/` opțional), consumate de motorul de descoperire/import.
- `tools/fisa_generator.py` — script utilitar pentru generarea `fisa.html` dintr-un `process.json`.
- `tests/common.py` — clasa `ProcessScreenshotCase`, folosită pentru generarea capturilor proprii ale proceselor.

#### 5. Conexiuni

- [deltatech_business_process](../deltatech_business_process/index.md): motorul care descoperă, importă și expune procesele acestei biblioteci într-un proiect de implementare.
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): furnizează capturile de ecran ale modulelor legate, folosite la generarea fișelor PDF atașate proceselor.
