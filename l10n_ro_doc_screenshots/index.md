# Romania - Tooling capturi fișe consultant (localizat la `l10n_ro_doc_screenshots/index.md`)

- **Nume Tehnic:** `l10n_ro_doc_screenshots`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_doc_screenshots
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doc_screenshots`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Modul de tooling de dezvoltare care nu adaugă funcționalitate de business. Oferă un mixin reutilizabil (`ScreenshotCase`) pentru generarea automată a capturilor de ecran folosite în fișele consultant (`<modul>/readme/screenshots/`), pornind de la date seedate determinist în teste. Mecanismul combină `HttpCase` (serverul Odoo și tranzacția testului) cu Playwright (Chrome de sistem) pentru navigare și capturi cu nume curate.

## 2. Funcționalități Cheie

- **Mixin `ScreenshotCase`** (în `tests/screenshot_case.py`) pentru generarea automată a capturilor folosite în fișele consultant.
- **Bazat pe `HttpCase` + Playwright** cu autentificare prin cookie de sesiune și navigare programatică.
- **Rulare prin tag de test** `--test-tags=fise_screenshots`.
- **Degradare elegantă:** dacă `playwright` lipsește din mediul Odoo, testele de capturi se sar fără eroare. Necesită `playwright` și `websocket-client`.

## 3. Dependențe

- `web`

## 4. Componente Cheie

### Modele

*Modul de tooling — nu definește modele de business.*

### Vizualizări / Date

*Nu definește vizualizări sau date; întreaga logică se află în `tests/screenshot_case.py`.*

### Acțiuni Automate / Acțiuni Server

- Mixinul de test `ScreenshotCase` (tag `fise_screenshots`), executat la cerere pentru regenerarea capturilor.

## 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
