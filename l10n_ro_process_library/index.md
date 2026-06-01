# Bibliotecă de Procese (Business Process) (localizat la `l10n_ro_process_library/index.md`)

- **Nume Tehnic:** `l10n_ro_process_library`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_process_library
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_process_library`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul oferă o bibliotecă versionată de procese de implementare (în special contabile) pentru `deltatech_business_process`. Nu adaugă funcționalitate de business, ci un catalog de procese RO pe care consultantul îl importă selectiv într-un proiect de implementare. Fiecare proces are pașii lui, modulele de localizare legate, un test UAT și fișa atașată ca PDF, generată automat la import.

#### 2. Funcționalități Cheie

- Catalog de procese organizat ca foldere `processes/<COD>_<slug>/` cu `process.json` (definiția), `fisa.html` (fișa) și `screenshots/` (capturi opționale).
- Import selectiv din wizardul `business.process.import` extins cu sursa "Bibliotecă de procese" (varianta "Fișier exportat JSON" rămâne neschimbată).
- La import: creare `business.process` legat de proiect, legarea modulelor după numele tehnic, crearea pașilor și a unui test UAT cu step-tests; reimport idempotent după code + proiect.
- Atașarea automată a fișelor ca PDF în "Documents" pe proces: fișa procesului (`Fisa_<COD>.pdf`) și fișa fiecărui modul legat (`Fisa_modul_<modul>.pdf`) din `readme/FISA_CONSULTANT.md`.
- Conversie Markdown → HTML (imagini base64) și HTML → PDF (wkhtmltopdf), cu fallback la HTML dacă wkhtmltopdf lipsește.
- Capturi pentru fișe: fișa modulului folosește capturile din `readme/screenshots/` (generate de `l10n_ro_doc_screenshots`), iar capturile proprii proceselor se generează cu `ProcessScreenshotCase`.

#### 3. Dependențe

- `[[deltatech_business_process]]`
- `[[l10n_ro_doc_screenshots]]`

#### 4. Componente Cheie

**Modele**

- `business.process.library`: Logica de catalog și import; metoda `_attach_documents` creează atașamentele PDF pe proces.
- `business.process.import` (extins): Adaugă sursa "Bibliotecă" la wizardul de import.

**Vizualizări / Date**

- `wizard/business_process_library_wizard_views.xml`: Interfața de selecție și import a proceselor din bibliotecă.
- `security/ir.model.access.csv`: Drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; biblioteca nu se încarcă automat la instalare, importul fiind explicit prin wizard.*

#### 5. Conexiuni

- `[[deltatech_business_process]]`
- `[[l10n_ro_doc_screenshots]]`
