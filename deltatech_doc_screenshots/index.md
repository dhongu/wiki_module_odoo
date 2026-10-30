# Doc Screenshots

- **Nume Tehnic:** `deltatech_doc_screenshots`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_doc_screenshots
- **Cale Locală:** `odoo-addons/deltatech/deltatech_doc_screenshots`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Unealtă de dezvoltare, fără funcție de business și fără ecrane proprii. Generează automat capturile de ecran ale fișelor consultant (`static/description/`) din date create determinist în testele modulului documentat, astfel încât imaginile să fie actuale și identice la fiecare regenerare. Se rulează doar la dezvoltare și nu se instalează la clienți. Înlocuiește `l10n_ro_doc_screenshots`, care acum doar reexportă clasa de aici.

#### 2. Funcționalități Cheie

- `ScreenshotCase`: clasă de bază `HttpCase` reutilizabilă; capturile se descriu ca o listă de dicționare și se generează cu o singură comandă. Folosește Playwright (Chrome de sistem), cu autentificare prin cookie de sesiune.
- Pregătirea datelor: `prepare_ro_company` (companie cu date românești: țară, RON, CUI, adresă, drepturi contabile pentru admin, limba română, tema luminoasă) și `prepare_demo_company` (pentru module cu date demo deja existente); `force_light_theme` forțează tema luminoasă.
- Ajutoare de captură: `account_move_shot` (formular `account.move` cu fila *Journal Items* deschisă), capturi de raport și de fișiere xlsx, decuparea automată a marginilor uniforme (`_autotrim`).
- `highlight` per captură: conturează selectorii în portocaliu Odoo, cu insigne numerotate ①②③, pentru a indica pașii din fișă. Se preferă selectorii după `name`; când e nevoie de text din interfață, se dă pe limbă (`ro_RO` / `en_US`).
- Două limbi dintr-o singură listă (`_shots`): `test_capture_fise` produce capturile în română pentru fișă, iar `test_capture_usage` (`lang="en_US"`) le produce în engleză în `static/description/en/`, pentru `readme/USAGE.md` de pe Apps Store.
- Opțiuni per captură: `full`, `wait`, `click_btn`, `click_tab`, `unfold_report`, `eval` (JS propriu), `settle` (pauză în ms); cadrare implicită 1920x950.
- Generare doar la cerere: capturile rescriu fișierele `.png`, deci o rulare obișnuită le sare. Se cer prin `--test-tags=fise_screenshots` (sau orice tag terminat în `_screenshots`), prin numele clasei sau prin `FISE_SCREENSHOTS=1`; `SKIP_FISE_SCREENSHOTS=1` are prioritate peste orice cerere.
- Degradare elegantă: fără `playwright`, testele de capturi sunt sărite, iar suita rămâne verde.
- Cerințe de mediu: `pip install playwright websocket-client pillow` și `playwright install chrome` (`pillow` e opțional, fără el captura nu e decupată).
- Importul în modulul consumator e defensiv (`try/except ImportError`), iar modulul de capturi nu se pune în `depends`; se instalează doar la rulare.

Fluxul detaliat este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

Modulul nu definește modele Odoo; conține doar cod de test.

- `ScreenshotCase` (`tests/screenshot_case.py`): clasa de bază a testelor de capturi.

**Vizualizări**

Nu are vizualizări.

**Acțiuni Automate / Acțiuni Server**

Nu are cron-uri, automatizări sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): vechiul loc al uneltei (suita l10n_ro_ent); acum doar reexportă `ScreenshotCase` de aici.
- Modulele cu `tests/test_screenshots.py` sunt consumatorii: fiecare își descrie propriile capturi.
