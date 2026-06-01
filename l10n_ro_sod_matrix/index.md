# Matrice Segregare Atribuții (SoD) România (localizat la `l10n_ro_sod_matrix/index.md`)

- **Nume Tehnic:** `l10n_ro_sod_matrix`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_sod_matrix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sod_matrix`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Acest modul este un instrument de audit și conformitate internă care detectează și gestionează conflictele de roluri (Segregation of Duties) conform cerințelor de control intern și audit financiar. Definește o matrice configurabilă de perechi de grupuri Odoo incompatibile, scanează utilizatorii pentru a identifica violările și oferă un flux de aprobare pentru recunoașterea, exceptarea sau rezolvarea acestora.

## 2. Funcționalități Cheie

- **Matrice de reguli SoD configurabilă:** perechi de grupuri incompatibile, cu severitate pe 4 niveluri (Critică / Ridicată / Medie / Redusă) și reguli implicite preconfigurate.
- **Detecție automată și manuală:** buton „Scanează" pe fiecare regulă pentru verificare imediată și cron săptămânal pentru scanare automată.
- **Auto-rezolvare violări:** când conflictul dispare (userul pierde un grup), violarea se închide automat.
- **Gestionare violări cu flux de aprobare:** `Deschisă → Recunoscută → Exceptată / Rezolvată`, cu notă de justificare a excepțiilor.
- **Raportare audit:** filtre și grupări pentru analiza conflictelor.

## 3. Dependențe

- `base`
- `account`
- `purchase`
- `stock`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `l10n.ro.sod.rule`: Regula SoD cu perechea de grupuri incompatibile și severitatea.
- `l10n.ro.sod.violation`: Violarea detectată, cu fluxul de aprobare și nota de justificare.

### Vizualizări / Date

- `data/l10n_ro_sod_rules.xml`: Regulile implicite preconfigurate.
- `data/ir_cron.xml`: Cron-ul de scanare automată.
- `views/l10n_ro_sod_rule_view.xml`, `views/l10n_ro_sod_violation_view.xml`: Interfețele pentru reguli și violări.

### Acțiuni Automate / Acțiuni Server

- **Scanare automată SoD:** cron săptămânal care verifică utilizatorii și actualizează violările.

## 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
