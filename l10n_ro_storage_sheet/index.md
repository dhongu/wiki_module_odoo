# Romania - Storage Sheet (Fișă Magazie) (localizat la `l10n_ro_storage_sheet/index.md`)

- **Nume Tehnic:** `l10n_ro_storage_sheet`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_storage_sheet
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_storage_sheet`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul adaugă raportul românesc „Fișă de magazie”: pentru o perioadă și o gestiune, arată pentru fiecare produs soldul inițial, intrările, ieșirile și soldul final, în cantitate și în valoare. Raportul poate fi consultat ca analiză pivot în Odoo sau tipărit în PDF. Funcționează pe valorizarea de stoc nativă din Odoo și nu depinde de motorul de valorizare OCA (`l10n_ro_stock_account`), fiind varianta potrivită pentru bazele de date care nu îl folosesc.

#### 2. Funcționalități Cheie

- Raport de tip fișă de magazie: sold inițial, intrări, ieșiri, sold final pe produs și locație, în cantitate și valoare (inclusiv prețuri unitare de intrare și de ieșire).
- Vizualizare ca analiză pivot în Odoo sau tipărire în PDF (cu opțiunea „un produs pe pagină”).
- Filtre în formularul raportului: gestiune/locație, produse alese, perioadă (dată început / dată sfârșit), doar produse cu mișcări, includere sub-locații, detaliere pe locații și afișarea locației.
- Meniu: Inventar > Raportare > „Romanian Stock Sheet Report” (acces pentru utilizatorii de stoc).
- Înlocuiește copia Terrabit a modulului `l10n_ro_stock_report`, redenumit pentru a evita conflictul cu modulul OCA omonim. Modelele raportului sunt tranzitorii, deci nu se migrează date. Pe bazele unde fișa de magazie era instalată fără `l10n_ro_stock_account`, se instalează `l10n_ro_storage_sheet` și se dezinstalează `l10n_ro_stock_report` înainte de actualizare, altfel actualizarea aduce și motorul OCA de valorizare.
- Pentru tipurile de mișcare valorizate din motorul OCA se folosește în continuare modulul OCA `l10n_ro_stock_report`.

#### 3. Dependențe

- `stock`
- `account`
- `purchase`
- `sale`
- `l10n_ro_config`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.storage.sheet`: model tranzitoriu cu parametrii raportului (locație, produse, perioadă, opțiuni de afișare) și logica de calcul (interogări SQL pentru sold inițial, intrări, ieșiri, sold final), plus acțiunile de afișare și de tipărire PDF.
- `l10n.ro.storage.sheet.line`: linia raportului, pe produs, cu cantități și valori inițiale, de intrare, de ieșire și finale.

**Vizualizări**

- `view_stock_sheet_report_form`: formularul de parametri al raportului (deschis ca fereastră).
- `view_sheet_stock_report_line_tree`, `view_sheet_stock_report_line_form`, `view_sheet_stock_report_line_pivot`, `view_sheet_stock_report_line_search`: listă, formular, pivot și căutare pentru liniile raportului.
- `report_storage_sheet`: șablonul QWeb pentru varianta PDF.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): modulul OCA cu același nume vechi; oferă fișa de magazie pe motorul OCA de valorizare (`l10n_ro_stock_account`), pe când acest modul lucrează pe valorizarea nativă.
