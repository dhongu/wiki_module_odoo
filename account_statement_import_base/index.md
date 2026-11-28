# Modul de bază pentru importul extraselor bancare

- **Nume Tehnic:** `account_statement_import_base`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/others_addons/tree/20.0/account_statement_import_base
- **Cale Locală:** `odoo-addons/others_addons/account_statement_import_base`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul tehnic care pune la dispoziție cod comun pentru modulele de import al extraselor bancare: importul din fișiere (`account_statement_import_file`) și importul online prin servicii web/API (`account_statement_import_online`). Nu are o interfață proprie de sine stătătoare, ci este baza pe care se construiesc celelalte.

#### 2. Funcționalități Cheie

- Cod partajat între importul din fișiere și importul online de extrase.
- Extinde jurnalul contabil (`account.journal`) și linia de extras bancar (`account.bank.statement.line`) cu elementele comune importului.
- Adaugă informațiile suplimentare ale importului în formularul liniei de extras.

#### 3. Dependențe

- [account_statement_base](../account_statement_base/index.md)

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): câmpuri și metode comune importului.
- `account.bank.statement.line` (extins): câmpuri de import pe linia de extras.

**Vizualizări**

- `account_bank_statement_line_form`: formularul liniei de extras, completat cu datele importului.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `account_statement_import_file`: import de extrase din fișiere, construit peste acest modul.
- `account_statement_import_online`: import prin servicii web/API (modul separat, fără pagină wiki).
