# Romania - Stock Report (Fișă Magazie) (localizat la `l10n_ro_stock_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_report`
- **Versiune:** `19.0.2.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_report`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Acest modul adaugă un raport de stocuri conform cerințelor legislației din România. El generează fișa de magazie (soldul inițial, intrările, ieșirile și soldul final) pe gestiuni și perioadă, document specific gestiunii românești pe care companiile trebuie să îl poată produce pentru evidența mișcărilor și a soldurilor de produse. În această variantă (suita `l10n-romania`) raportul se bazează direct pe valorizarea standard a mișcărilor de stoc din Odoo 19, fără dependența de `l10n_ro_stock_account`.

#### 2. Funcționalități Cheie

- Generarea fișei de magazie (situație stocuri) pentru un interval de date, cu sold inițial, intrări, ieșiri și sold final pe produs; valorile se citesc din câmpurile standard `stock.move.value` și `stock.move.quantity`, doar pentru mișcările în starea `done`.
- Filtrare pe o singură gestiune (locație) sau pe mai multe, cu opțiunea de a include sub-gestiunile (`sublocation`, implicit activă).
- Afișare detaliată pe locații (`detailed_locations`) și opțiune de a arăta explicit locația pe fiecare linie (`show_locations`).
- Filtrare pe produse specifice sau doar pe produsele cu mișcări în perioada selectată (`products_with_move`).
- Opțiune „un produs pe pagină" (`one_product`) pentru raportul PDF; există două rapoarte PDF: „Stock Sheet" (pe locație) și „Stock Sheet All" (pentru toate locațiile), cu soldul final preluat din valorile rândului FINAL.
- Detaliere pe număr de serie / lot, unde este cazul (`serial_number`).
- Vizualizare a rezultatului ca listă/pivot interactiv în Odoo sau ca raport PDF.
- Vizualizare pivot și căutare cu grupare pe cont contabil, produs, locație sau tip valorizat. În această variantă `valued_type` are doar valoarea locală „indefinite" iar `account_id` rămâne necompletat în liniile calculate (nu există mapare pe conturi contabile românești fără `l10n_ro_stock_account`).
- Meniul „Romanian Stock Sheet Report" apare sub Inventar > Raportare, pentru utilizatorii din grupul de stoc, și este marcat ca înregistrare specifică localizării române.

#### 3. Dependențe

- `stock`
- `account`
- `purchase`
- `sale`
- `l10n_ro_config`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.storage.sheet` (`TransientModel`): wizard-ul de configurare a raportului — filtre pe gestiune, produse, interval de date, opțiuni de detaliere; calculează liniile raportului prin interogări SQL directe pe `stock.move` (sold inițial, sold final, intrări, ieșiri) și declanșează afișarea în ecran sau ca PDF.
- `l10n.ro.stock.storage.sheet.line` (`TransientModel`): liniile rezultate ale raportului (cantități și valori inițiale, intrări, ieșiri, finale, prețuri unitare), cu referințe la produs, partener, categorie, locație, factură, lot/serie, cont contabil și tipul valorizat (`valued_type`).

**Vizualizări**

- `view_stock_sheet_report_form`: formularul wizard de lansare a raportului (filtre gestiune/produse/perioadă, butoane „Show Sheet" și „Show Sheet Pdf").
- `view_sheet_stock_report_line_tree` / `_form` / `_pivot` / `_search`: listă, formular, pivot și căutare pentru liniile fișei de magazie generate.
- `menu_sheet_stock_report`: meniul „Romanian Stock Sheet Report" sub `stock.menu_warehouse_report`.
- Rapoarte QWeb: `report_storage_sheet` și `report_storage_sheet_all` (acțiunile `action_report_storage_sheet`, `action_report_storage_sheet_all`).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; raportul se calculează sincron, la cererea utilizatorului, prin butoanele wizard-ului.

#### 5. Conexiuni

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): modul înrudit din aceeași suită, care furnizează documentele de mișcare a stocurilor (NIR, bon de consum, aviz de însoțire), complementar rapoartelor de sold oferite aici.
- `l10n_ro_stock_account`: în varianta din suita `l10n-romania-oca` (19.0.2.10.0) este dependența care aduce tipul valorizat și conturile contabile; aici NU este dependență.
