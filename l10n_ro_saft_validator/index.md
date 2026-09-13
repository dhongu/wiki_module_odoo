# Romania - Pre-validator SAF-T D406 (FR-05) (localizat la `l10n_ro_saft_validator/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_validator`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_validator
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_validator`
- **Ultima Ingestie:** 2026-09-12
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md) — overview, cu fișe dedicate pe speță: [L/T](FISA_CONSULTANT_LT.md), [A](FISA_CONSULTANT_A.md), [C](FISA_CONSULTANT_C.md)

## 1. Sumar

Acest modul rulează verificări **înainte** de generarea declarației **SAF-T D406**, identificând din timp datele care ar duce la respingerea fișierului. Wizardul acoperă cele trei spețe de depunere (lunar/trimestrial, anual pentru active, la cerere pentru stocuri) și prezintă problemele ca listă structurată, fiecare cu legătură directă la înregistrarea de corectat — partener, cont, notă contabilă sau articol. Verificările nu se uită doar la configurație, ci și la documentele perioadei alese, iar o parte însemnată dintre ele sunt derivate din confruntarea unui fișier generat de Odoo cu validatorul oficial `D406Validator` din DUK Integrator: fiecare a fost mai întâi un fișier respins de ANAF, apoi o regulă.

## 2. Funcționalități Cheie

- **Trei seturi de verificări, după tipul declarației:** câmpul *Tip declarație* comută între **LT** (lunar/trimestrial), **A** (anual — active) și **C** (la cerere — stocuri); verificarea datelor de companie rulează pentru toate.
- **Date de companie complete (`company_incomplete`):** CUI, adresă, județ, plus prerechizitele fără de care exportul refuză să pornească — telefon, cont bancar, baza de impozitare SAF-T — și existența unui contact cu nume din două cuvinte și telefon, fără de care declarația iese fără elementul obligatoriu `Contact`.
- **Identificarea partenerilor:** parteneri cu rulaj fără CUI/CNP (`partner_no_vat`), fără țară sau cu cod non-ISO2 (`partner_no_country`, `partner_invalid_country`), fără localitate (`partner_no_city`), fără județ sau cu județ în afara nomenclatorului ISO 3166-2:RO (`partner_no_state`, `partner_invalid_state`).
- **Tip fiscal incoerent (`partner_fiscal_type_mismatch`):** persoane juridice la care țara și prefixul codului de TVA se contrazic — combinația decide `RegistrationType` în declarație (operator român, UE, non-UE).
- **Note contabile fără partener (`move_line_no_partner`):** linii pe conturi de creanțe/datorii (după `account_type`, dar și după prefixul de cod 40/41) fără partener completat; `CustomerID`/`SupplierID` ar lipsi din `GeneralLedgerEntries`.
- **Secțiuni care ar ieși goale (`export_section_empty`):** exportul scrie necondiționat `SalesInvoices`, `PurchaseInvoices` și `Payments`, iar validatorul oficial cere minimum un element în fiecare secțiune prezentă — o lună fără achiziții produce un fișier respins integral.
- **Plăți absente din export (`payments_not_exported`):** declarația preia **doar** plățile venite dintr-o linie de extras bancar; o plată înregistrată prin „Înregistrează plata", fără extras, nu ajunge în fișier.
- **Articole (`product_no_default_code`, `product_no_category`, `product_no_account`):** referință internă lipsă (exportul refuză să ruleze), categorie lipsă (`ProductGroup` ar ieși vid și e respins) și lipsa conturilor de venit/cheltuială pe articol și pe categorie.
- **Conturi și taxe (`account_no_type`, `tax_no_saft_type`):** conturi cu rulaj fără `account_type` și taxe fără tipul SAF-T configurat.
- **Speța A — active (`asset_no_saft_category`):** imobilizări fără categorie SAF-T mapată.
- **Speța C — stocuri (`picking_type_no_movement_type`, `uom_no_unece_code`):** tipuri de operație fără cod de mișcare SAF-T și unități de măsură fără corespondent UNECE, care ar fi exportate ca `C62`.
- **Severități și buclă de corecție:** erori (blochează exportul), avertismente (recomandate) și informații (module opționale neinstalate); după corectare se reapasă *Validează*, iar wizardul confirmă explicit „Nicio problemă detectată".
- **Totul rulează local:** verificările interoghează baza proprie, fără niciun apel către ANAF sau alt serviciu extern.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `l10n.ro.saft.validator`: wizardul (transient) care rulează verificările; câmpurile `declaration_type`, `date_from`/`date_to` și contoarele de erori/avertismente/informații. Metoda `action_validate` orchestrează verificările pe speță.
- `l10n.ro.saft.validator.line`: linia de rezultat — severitate, tip de verificare, mesaj și legături către partener, cont, notă contabilă (`move_id`) sau articol (`product_id`).

### Vizualizări / Date

- `wizard/l10n_ro_saft_validator_views.xml`: formularul wizardului (bannere pe severitate, sumar, lista problemelor cu coloane opționale pentru notă și articol), acțiunea și meniul din **Contabilitate → Raportare**.
- `demo/account_asset_demo.xml`: active demo cu categorie SAF-T mapată, pentru speța A (Odoo nu aduce active demo pentru localizarea RO).
- `security/ir.model.access.csv`: drepturile pe cele două modele tranzitorii.

### Teste

- `tests/test_saft_validator.py`: acoperă fiecare verificare pe perechea detectare / non-detectare, plus filtrarea pe tipul declarației. `test_saft_export_dump_for_duk` construiește un scenariu complet valid, confirmă că pre-validarea e curată, generează declarația prin `l10n_ro_saft` și — cu variabila de mediu `SAFT_DUMP_DIR` setată — scrie XML-ul pe disc pentru revalidare cu DUK Integrator. Testul se oprește singur dacă modulele Enterprise nu sunt instalate.
- `tests/test_screenshots.py`: generează capturile fișelor consultant (tag `fise_screenshots`).

### Acțiuni Automate / Acțiuni Server

*Nu sunt definite acțiuni automate; validarea se rulează manual din wizard.*

## 5. Conexiuni

- `l10n_ro_saft` (Enterprise): generează efectiv fișierul D406 — butoanele lunar și „Active" de pe raportul Cartea Mare. Sursa mai multor reguli de verificare: `_l10n_ro_saft_fill_payment_values` (plățile doar din extras bancar) și `_l10n_ro_saft_get_registration_number` (tipul fiscal al partenerului).
- `l10n_ro_saft_stock` (Enterprise): exportul pentru speța C și câmpul `l10n_ro_stock_movement_type` pe tipul de operație.
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): rulează DUK Integrator pe stația contabilului, prin agentul local — validarea oficială de după acest pas de pre-verificare.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): verificare încrucișată — soldurile din SAF-T trebuie să corespundă cu D300 al perioadei.
- `l10n_ro`: planul de conturi și structura fiscală RO.
