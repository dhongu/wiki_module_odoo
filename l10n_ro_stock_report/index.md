# Romania - Stock Report (Fișă Magazie) (localizat la `l10n_ro_stock_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_report`
- **Versiune:** `19.0.2.10.2`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/19.0/l10n_ro_stock_report
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_stock_report`
- **Ultima Ingestie:** `2026-11-20`

#### 1. Sumar

Modulul adaugă raportul de stocuri cerut de legislația din România, cunoscut ca fișă de magazie. Pentru o perioadă și una sau mai multe gestiuni, raportul arată soldul inițial, intrările, ieșirile și soldul final pentru fiecare produs, în cantitate și în valoare, și poate fi consultat în Odoo sau tipărit în PDF. Este documentul de bază pentru evidența mișcărilor și a soldurilor de stoc și se bazează pe valorizarea și pe conturile contabile din localizarea română a stocurilor. Modulul nu este necesar dacă baza de date folosește [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md) sau determină conturile de stoc prin OBYC ([deltatech_obyc](../deltatech_obyc/index.md)).

#### 2. Funcționalități Cheie

- Generarea fișei de magazie pe interval de date, cu sold inițial, intrări, ieșiri și sold final pe produs, în cantitate și valoare.
- Filtrare pe una sau mai multe gestiuni (locații), cu opțiunea de a include sub-locațiile (`sublocation`, activă implicit).
- Afișare detaliată pe locații (`detailed_locations`) și opțiune de a arăta locația pe fiecare linie (`show_locations`).
- Filtrare pe produse alese sau doar pe produsele cu mișcări în perioadă (`products_with_move`).
- Detaliere pe lot / număr de serie, unde produsul este urmărit.
- Fiecare linie are tipul valorizat al mișcării (`valued_type`, citit din tipul de mișcare românesc al lui `stock.move`; „indefinite" pentru mișcările fără tip determinat) și contul contabil. Rândurile de sold au tipuri proprii, `initial` și `final`, ca să nu se amestece cu mișcările fără tip.
- Un transfer intern apare pe contul de stoc al fiecărei locații: sursa pe contul sursei, destinația pe contul destinației (corecție din 19.0.2.10.2; anterior cele două conturi erau citite invers).
- Rezultat vizualizabil ca listă, formular sau pivot (grupare pe cont, produs, locație, tip valorizat) ori ca raport PDF.
- Două rapoarte PDF: „Stock Sheet" (pe locație) și „Stock Sheet All" (toate locațiile); opțiunea „un produs pe pagină" (`one_product`). Soldul final tipărit se preia din rândul FINAL calculat (corecție din 19.0.2.9.0).
- Meniul „Romanian Stock Sheet Report" se află în Inventar > Raportare, pentru grupul de utilizatori de stoc și grupul de meniuri specifice României.
- Raportul se bazează pe câmpurile adăugate de `l10n_ro_stock_account` (`l10n_ro_move_type`, `l10n_ro_account_id`, `l10n_ro_transfer_account_id`), deci funcționează doar împreună cu acesta.
- Când se înlocuiește cu `l10n_ro_stock_sheet`: acesta nu împarte raportul pe tip de mișcare (recepție, livrare, plus/minus inventar, consum, transfer etc.), ci grupează pe cont de stoc, produs și document; nu are filtru pe zonă de valorizare (doar pe locație); iar pentru mișcările fără notă contabilă (de exemplu cele migrate dintr-o versiune anterioară) contul este cel al categoriei de produs.

#### 3. Dependențe

- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.storage.sheet` (`TransientModel`): wizard-ul de configurare (gestiune, produse, perioadă, opțiuni de detaliere); calculează liniile prin interogări SQL pe `stock.move` (sold inițial, intrări, ieșiri, sold final) și deschide rezultatul în ecran sau ca PDF.
- `l10n.ro.stock.storage.sheet.line` (`TransientModel`): liniile raportului (cantități și valori pentru sold inițial, intrări, ieșiri, sold final, prețuri unitare), cu produs, partener, categorie, locație, factură, lot/serie, cont contabil, document și `valued_type`.

**Vizualizări**

- `view_stock_sheet_report_form`: formularul wizard de lansare (butoane „Show Sheet" și „Show Sheet Pdf").
- `view_sheet_stock_report_line_tree` / `_form` / `_pivot` / `_search`: listă, formular, pivot și căutare pentru liniile generate.
- `menu_sheet_stock_report`: meniul „Romanian Stock Sheet Report" sub `stock.menu_warehouse_report`.
- Rapoarte QWeb: `report_storage_sheet` și `report_storage_sheet_all` (acțiunile `action_report_storage_sheet`, `action_report_storage_sheet_all`).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește `ir.cron`, `base.automation` sau `ir.actions.server`; raportul se calculează la cerere, din wizard.

#### 5. Conexiuni

- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md): aduce tipurile de mișcare și conturile contabile folosite de raport (dependență).
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md): alternativă fără dependență OCA (fișa de magazie 14-3-8 și balanța analitică de stoc); înlocuiește acest modul.
- [deltatech_obyc](../deltatech_obyc/index.md): determinarea conturilor de stoc prin OBYC, caz în care acest modul nu se instalează.
- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md): documentele de mișcare a stocurilor (NIR, bon de consum, aviz), complementare fișei de magazie.
- [l10n_ro_stock_report_dropship](../l10n_ro_stock_report_dropship/index.md): extinde acest raport pentru fluxurile dropship.
- [l10n_ro_stock_aged_report](../l10n_ro_stock_aged_report/index.md): raport de vechime a stocurilor, din același domeniu de raportare.
