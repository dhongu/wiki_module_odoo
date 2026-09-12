# Romania - Bibliotecă de procese (Business Process) (localizat la `l10n_ro_process_library/index.md`)

- **Nume Tehnic:** `l10n_ro_process_library`
- **Versiune:** `19.0.2.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_process_library
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_process_library`
- **Ultima Ingestie:** 2026-09-12

#### 1. Sumar

Modulul livrează o bibliotecă versionată de procese de implementare (peste 50 de procese contabile și operaționale românești), organizată ca un catalog de foldere pe care consultantul le importă selectiv într-un proiect din `deltatech_business_process`. Nu adaugă funcționalitate de business proprie: furnizează conținutul (definiții JSON, fișe HTML, capturi) pe care motorul de import și cadrul de procese îl consumă.

#### 2. Funcționalități Cheie

- Catalog de procese organizat ca foldere `processes/<COD>_<slug>/` cu `process.json` (definiția: cod, arie, pași, teste UAT, module legate), `fisa.html` (fișa generată) și `screenshots/` (capturi opționale).
- Peste 50 de procese acoperind ariile: CB (Cash & Banking — e-Factură, mesaje SPV, reconcilieri, registru de casă), DEC (declarații fiscale D300/D390/D394/D398/D112/D107/D100/D120/D205/D207/D318/D406), TVA (regularizare, rambursare, grup fiscal, pro-rată, prag OSS, TVA la încasare), IMO (mijloace fixe, obiecte de inventar), INC (închidere perioadă/an, situații financiare, impozit profit/micro), OPS (dividende, leasing, provizioane, subvenții, CBAM, SGR, accize, diurne), TRZ (trezorerie, reevaluări valutare, plată obligații buget), ST (inventariere fizică).
- Import selectiv din wizardul `business.process.import` (parte din `deltatech_business_process`), cu sursa „Bibliotecă de procese" alături de varianta „Fișier exportat JSON": lista afișează Cod, Denumire, Arie, Module și o bifă „Capturi" (dacă procesul are capturi generate); consultantul bifează „Importă" doar pe procesele relevante pentru proiect.
- Contribuție automată de procese: orice modul instalat care depinde de `deltatech_business_process` și respectă convenția `processes/<COD>_nume/process.json` (fără declarație suplimentară în manifest) e descoperit automat, grupat pe modulul-sursă. Descoperirea globală și restrângerea la o listă explicită de module se controlează din Setări → Business process → Configurare → Bibliotecă de procese.
- La import se creează `business.process` legat de proiect, se leagă modulele după numele tehnic, se creează pașii și un test UAT cu step-tests; reimportul e idempotent per proiect + cod proces. Coduri duplicate între surse: câștigă prima importată, a doua e sărită (vizibil în log).
- Atașarea automată a fișelor ca PDF pe proces (smart button „Documents"): fișa procesului (`Fisa_<COD>.pdf`, din `fisa.html`) și fișa fiecărui modul legat (`Fisa_modul_<modul>.pdf`, din `readme/FISA_CONSULTANT.md`), cu fallback la HTML dacă wkhtmltopdf lipsește.
- Capturi pentru fișele modulelor legate provin din `<modul>/readme/screenshots/`, generate de mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`; capturile proprii proceselor se generează cu `ProcessScreenshotCase` din `tests/common.py`.
- Instrument `tools/fisa_generator.py` pentru generarea fișei HTML a unui proces nou dintr-un `process.json` — atenție: generatorul folosește doar câmpul `description` al fiecărui pas pentru fișa PDF; conținutul mai bogat din `details` (capcane, referințe de meniu, note tehnice) ajunge doar în Odoo la import (pas + `details`), nu și în PDF-ul fișei.
- Proces-exemplu cu capturi proprii — **INC002 „Închidere de lună — cele 7 faze"**: primul proces din bibliotecă cu screenshot-uri generate special pentru el (`screenshots/step_10.png` … `step_70.png`, câte unul per fază), produse de `tests/test_screenshots_inc002.py` (clasa `ProcessScreenshotCase`) pe convenția `step_<sequence>.png`, pe care `fisa_generator.py` o agață automat pe pasul cu secvența corespunzătoare. Procesul acoperă cele șapte faze ale închiderii lunare RO (checklist, documente și bancă, stocuri, producție în curs, regularizări periodice, TVA și declarații, verificare finală/blocare perioadă) și listează 13 module legate din suita `l10n_ro_ent`.

#### 3. Dependențe

- [deltatech_business_process](../deltatech_business_process/index.md)
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md)

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni proprii — este un modul de conținut pur (date + tooling). Logica de import, descoperire automată și modelul `business.process.library` sunt implementate în `deltatech_business_process` (vezi pagina sa de wiki pentru detalii tehnice); acest modul contribuie exclusiv:

- Directorul `processes/` — 50 de subdirectoare `<COD>_<slug>/` cu `process.json` + `fisa.html` (+ `screenshots/` opțional), consumate de motorul de descoperire/import.
- `tools/fisa_generator.py` — script utilitar pentru generarea `fisa.html` dintr-un `process.json`; randează pas cu pas doar câmpul `description` și, dacă există, agață captura `screenshots/step_<sequence>.png` pe pasul cu secvența respectivă.
- `tests/common.py` — clasa `ProcessScreenshotCase`, folosită pentru generarea capturilor proprii ale proceselor.
- `tests/test_screenshots_inc002.py` — testul de capturi al procesului INC002 (`ProcessScreenshotCase` + `ScreenshotCase` din `l10n_ro_doc_screenshots`); seed-urile per fază sunt condiționate de modulul opțional instalat, deci o fază fără modulul ei își sare captura fără să rupă restul testului.

#### 5. Conexiuni

- [deltatech_business_process](../deltatech_business_process/index.md): motorul care descoperă, importă și expune procesele acestei biblioteci într-un proiect de implementare.
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): furnizează capturile de ecran ale modulelor legate, folosite la generarea fișelor PDF atașate proceselor.
Cele 13 module legate de procesul INC002 „Închidere de lună — cele 7 faze". Niciunul nu e dependență a acestui modul: sunt referite doar în conținutul procesului, iar importul le leagă prin `module_ids` dacă sunt instalate.

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklistul lunar care conduce procesul (faza 01 și 07).
- [l10n_ro_registru_jurnal](../l10n_ro_registru_jurnal/index.md) și [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md): registrele tipărite la verificarea finală.
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md), [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md), [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md), [l10n_ro_stock_provision](../l10n_ro_stock_provision/index.md): faza 03, în această ordine strictă.
- [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md): faza 04, producția în curs.
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md), [l10n_ro_deferred_entries](../l10n_ro_deferred_entries/index.md), [l10n_ro_provisions](../l10n_ro_provisions/index.md), [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): faza 05, regularizările periodice.
- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md): faza 06, ultima notă contabilă a lunii.
