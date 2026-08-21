# Import Extras ING Business - Format CSV (localizat la `l10n_ro_account_bank_statement_import_ing_csv/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_ing_csv`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_bank_statement_import_ing_csv
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_bank_statement_import_ing_csv`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul importă fișierele „Istoric conturi" (CSV) exportate din ING Business direct ca extrase de cont, fără nicio prelucrare manuală a fișierului.

#### 2. Funcționalități Cheie

- **Import fișier original**: se încarcă CSV-ul exact cum e exportat din ING Business — antetul, separatorul `;`, sumele în format românesc (`1.234,56`) și codificarea sunt gestionate automat.
- **Detecție după semnătură**: fișierul e recunoscut după antetul ING, deci poate fi importat de pe orice jurnal de tip bancă, alături de alte formate de extras.
- **Validare cont**: numărul de cont din fișier e verificat față de contul bancar al jurnalului (mecanismul standard Odoo).
- **Solduri**: soldul inițial și cel final al extrasului sunt calculate din coloana „sold intermediar".
- **Date bogate pentru reconciliere**: numele contrapartidei, contul IBAN și CUI-ul contrapartidei sunt preluate pe linia de extras, pentru identificarea automată a partenerului.
- **Protecție la duplicate**: fiecare tranzacție e importată o singură dată (id unic de import din referința internă/instant ING); reimportul aceluiași fișier e detectat.

#### 3. Dependențe

- `l10n_ro`
- `account_bank_statement_import`
- `account_bank_statement_import_csv`

#### 4. Componente Cheie

Documentația este derivată din `readme/DESCRIPTION.md`, care descrie funcționalitatea la nivel de utilizator. Aceasta nu solicită o analiză detaliată a componentelor tehnice, deci secțiunea nu a fost populată prin analiza codului.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): oferă suport de import XLSX și detectare automată a partenerului pentru extrase bancare, complementar pe alte formate/canale.
- `l10n_ro_account_bank_statement_import_mt940_ing` (OCA): alternativă de import pentru același cont ING, prin formatul MT940 în loc de CSV.
