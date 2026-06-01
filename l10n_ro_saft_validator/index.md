# Pre-Validator SAF-T D406 România (FR-05) (localizat la `l10n_ro_saft_validator/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_validator`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_saft_validator
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_validator`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Acest modul oferă verificări de pre-export pentru declarația **SAF-T D406**, identificând din timp problemele de date care ar cauza respingerea fișierului de către ANAF. Validatorul scanează partenerii fără CUI, conturile contabile nemapate și codurile de țară invalide, prezentând rezultatele într-o listă structurată pentru ca utilizatorul să corecteze datele înainte de generarea efectivă a declarației.

## 2. Funcționalități Cheie

- **Verificare date companie (`company_incomplete`):** semnalează adresa, orașul, codul poștal, țara sau județul lipsă.
- **Verificare parteneri fără CUI (`partner_no_vat`):** detectează partenerii cu rulaj fără cod de identificare fiscală (sau persoane fizice fără CNP).
- **Verificare parteneri fără țară (`partner_no_country`) sau cu țară invalidă (`partner_invalid_country`).**
- **Verificare conturi nemapate (`accounts_no_type`):** identifică conturile fără tip configurat pentru SAF-T.
- **Verificare taxe (`taxes_no_saft_type`):** semnalează taxele fără tipul SAF-T configurat.
- **Raport de validare structurat:** prezintă fiecare problemă ca linie distinctă (tip, mesaj, partener/cont), pentru remediere înainte de export. Verificarea partenerilor vizează doar pe cei cu rulaj pe conturi de creanțe/datorii.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `l10n.ro.saft.validator`: Wizardul/transient model care rulează verificările de pre-export SAF-T.
- `l10n.ro.saft.validator.line`: Liniile cu problemele identificate (partener, cont, cod țară etc.).

### Vizualizări / Date

- `wizard/l10n_ro_saft_validator_views.xml`: Interfața wizardului de validare și afișarea rezultatelor.
- `security/ir.model.access.csv`: Drepturile de acces pentru entitățile validatorului.

### Acțiuni Automate / Acțiuni Server

*Nu sunt definite acțiuni automate; validarea se rulează manual din wizard.*

## 5. Conexiuni

- `l10n_ro_saft`: generarea efectivă a fișierului SAF-T D406 (pasul ulterior validării).
- `l10n_ro`: planul de conturi și structura fiscală RO.
