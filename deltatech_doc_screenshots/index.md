# Doc Screenshots

- **Nume Tehnic:** `deltatech_doc_screenshots`
- **Versiune:** `20.0.1.3.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_doc_screenshots
- **Cale Locală:** odoo-addons/deltatech/deltatech_doc_screenshots
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de unelte pentru dezvoltare, fără funcționalitate de business. Oferă un mixin de teste care generează automat capturile de ecran ale fișelor de consultant, pornind de la date create determinist în teste. Este vizibil doar dezvoltatorilor și documentariștilor.

#### 2. Funcționalități Cheie

- `ScreenshotCase` (în `tests/screenshot_case.py`): clasă de bază `HttpCase` + Playwright (Chrome de sistem), reutilizabilă în orice modul; capturile se descriu ca listă de dicționare și se generează cu o singură comandă, direct în `static/description/`.
- `prepare_ro_company` (date românești: țară, RON, CUI, adresă, drepturi de contabilitate, limba română, temă luminoasă) și `prepare_demo_company` (pentru module cu date demo); `account_move_shot`, `force_light_theme`, `_autotrim` (taie marginile uniforme).
- `highlight` pe fiecare captură: conturează elemente cu portocaliu Odoo și insigne numerotate ①②③.
- Capturile se generează doar la cerere (`--test-tags` cu `fise_screenshots` sau orice tag care se termină în `_screenshots`, ori `FISE_SCREENSHOTS=1`); `SKIP_FISE_SCREENSHOTS=1` are prioritate. Fără `playwright`, testele de capturi sunt omise, iar suita trece.
- Două limbi: capturi în română pentru fișa consultantului și în engleză (`static/description/en/`) pentru USAGE.md.
- `capture_gif`: GIF demo animat pentru pagina Apps Store (cursor simulat, text tastat literă cu literă, subtitrări, slide de început și de final din `banner.json`).
- Înlocuiește `l10n_ro_doc_screenshots`, care doar reexportă `ScreenshotCase` de aici.
- Cerințe de instalare pentru generare: `playwright`, `websocket-client`, `pillow` (opțional) și `playwright install chrome`.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- Nu definește modele; clasa `ScreenshotCase` este în `tests/screenshot_case.py`.

**Vizualizări**

- Nu are vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): modul din localizarea României, care reexportă `ScreenshotCase` din acest modul.
