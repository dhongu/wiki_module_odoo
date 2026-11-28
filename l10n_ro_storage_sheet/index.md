# Romania - Fișă Magazie (`l10n_ro_storage_sheet`)

- **Nume Tehnic:** `l10n_ro_storage_sheet`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_storage_sheet
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_storage_sheet`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă raportul românesc „Fișa de magazie”: stoc inițial, intrări, ieșiri și stoc final, per produs și locație, disponibil ca PDF sau ca analiză pivot. Funcționează pe evaluarea de stoc nativă din Odoo și nu depinde de motorul de evaluare `l10n_ro_stock_account`.

A fost publicat anterior în acest repository sub numele `l10n_ro_stock_report`, nume care intra în conflict cu modulul OCA omonim. Bazele de date care au nevoie de tipurile de mișcări evaluate din motorul OCA continuă să folosească modulul OCA `l10n_ro_stock_report`.

#### 2. Funcționalități Cheie

- Raport accesibil din **Inventar > Raportare > Romanian Stock Sheet Report**, cu alegerea locației și a intervalului de date (luna curentă implicit), prin butonul **Show Sheet**.
- Analiză pivot per produs, cu cantitate și valoare inițială, de intrare, de ieșire și finală; export XLSX.
- Vizualizare listă cu fiecare mișcare și documentul ei; rândurile INITIAL și FINAL marchează soldul de început și de sfârșit al perioadei.
- Fișa tipărită în PDF (**Show Sheet Pdf**): per produs și cont de stoc, rândul INITIAL, mișcările și rândul FINAL, cu stocul după fiecare operație.
- Fluxul pas cu pas, cu capturi, se află în fișa consultantului.

#### 3. Dependențe

- `stock`
- `account`
- `stock_account`
- `purchase`
- `sale`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.storage.sheet`: model tranzitoriu (wizard) cu locația și intervalul de date; generează liniile fișei.
- `l10n.ro.storage.sheet.line`: model tranzitoriu cu rândurile fișei (produs, mișcare, cantități și valori), baza pentru pivot, listă și PDF.

**Vizualizări**

- `view_stock_sheet_report_form`: formularul wizardului.
- `view_sheet_stock_report_line_tree` / `_form` / `_pivot` / `_search`: listă, formular, pivot și căutare pentru liniile fișei.
- `stock_report_template.xml`: șablonul QWeb al fișei PDF.

**Acțiuni Automate / Acțiuni Server**

- `action_sheet_stock_report` și meniul `menu_sheet_stock_report`: deschid wizardul. Nu există acțiuni automate.

#### 5. Conexiuni

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): numele sub care a fost publicat anterior modulul; bazele cu motorul de evaluare OCA rămân pe modulul OCA cu același nume.
