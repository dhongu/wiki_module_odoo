# Pre-Validator SAF-T D406 România (FR-05) (localizat la `l10n_ro_saft_validator/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_validator`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_saft_validator
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_validator`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Acest modul oferă verificări de pre-export pentru declarația **SAF-T D406**, identificând din timp problemele de date care ar cauza respingerea fișierului de către ANAF. Validatorul scanează partenerii fără CUI, conturile contabile nemapate și codurile de țară invalide, prezentând rezultatele într-o listă structurată pentru ca utilizatorul să corecteze datele înainte de generarea efectivă a declarației.

## 2. Funcționalități Cheie

- **Verificare parteneri fără CUI:** Detectează partenerii la care lipsește codul de identificare fiscală.
- **Verificare conturi nemapate:** Identifică conturile contabile care nu au corespondent în structura SAF-T.
- **Verificare coduri de țară invalide:** Semnalează valorile de țară care nu respectă formatul cerut de D406.
- **Raport de validare structurat:** Prezintă fiecare problemă detectată ca o linie distinctă, pentru remediere rapidă înainte de export.

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

- `[[l10n_ro_anaf_base]]`
