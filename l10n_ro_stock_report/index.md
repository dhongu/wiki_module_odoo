# Romania - Stock Report (Fișă Magazie) (localizat la `l10n_ro_stock_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_report`
- **Versiune:** `19.0.2.7.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/19.0/l10n_ro_stock_report
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_stock_report`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul adaugă un raport de stocuri conform cerințelor legislației din România. El generează fișa de magazie (soldul inițial, intrările, ieșirile și soldul final) pe gestiuni și perioadă, document specific gestiunii românești pe care companiile trebuie să îl poată produce pentru evidența mișcărilor și a soldurilor de produse.

#### 2. Funcționalități Cheie

- Generarea fișei de magazie (situație stocuri) pentru un interval de date, cu sold inițial, intrări, ieșiri și sold final pe produs.
- Filtrare pe o singură gestiune (locație) sau pe mai multe, cu opțiunea de a include sub-gestiunile.
- Afișare detaliată pe locații (`detailed_locations`) și opțiune de a arăta explicit locația pe fiecare linie (`show_locations`).
- Filtrare pe produse specifice sau doar pe produsele cu mișcări în perioada selectată (`products_with_move`).
- Grupare a liniilor pe tipul de mișcare valorizată (`valued_type`: intrare, ieșire, sold inițial, sold final etc.), citit din câmpul `stock.move.l10n_ro_move_type`.
- Vizualizare a rezultatului atât ca listă/pivot interactiv în Odoo, cât și ca raport PDF (o pagină per produs, opțional).
- Vizualizare pivot pentru analiza cantităților și valorilor pe cont contabil, produs, locație sau tip valorizat.

#### 3. Dependențe

- `l10n_ro_stock_account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.storage.sheet` (`TransientModel`): wizard-ul de configurare a raportului — filtre pe gestiune, produse, interval de date, opțiuni de detaliere; calculează liniile raportului prin interogări SQL directe pe `stock.move` (sold inițial, sold final, intrări, ieșiri) și declanșează afișarea în ecran sau ca PDF.
- `l10n.ro.stock.storage.sheet.line` (`TransientModel`): liniile rezultate ale raportului (cantități și valori inițiale, intrări, ieșiri, finale), cu referințe la produs, cont contabil, partener, categorie și tipul valorizat (`valued_type`).

**Vizualizări**

- `view_stock_sheet_report_form`: formularul wizard de lansare a raportului (filtre gestiune/produse/perioadă, butoane „Show Sheet" și „Show Sheet Pdf").
- `view_sheet_stock_report_line_tree` / `_form` / `_pivot` / `_search`: listă, formular, pivot și căutare pentru liniile fișei de magazie generate, cu grupare pe produs, locație, cont contabil sau tip valorizat.
- `menu_sheet_stock_report`: meniul „Romanian Stock Sheet Report" sub raportarea de gestiune stoc, vizibil pentru utilizatorii de stoc din grupul de meniuri specifice României.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; raportul se calculează sincron, la cererea utilizatorului, prin butoanele wizard-ului.

#### 5. Conexiuni

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): modul înrudit din aceeași suită, care furnizează documentele de mișcare a stocurilor (NIR, bon de consum, aviz de însoțire), complementar rapoartelor de sold oferite aici.
- `l10n_ro_stock_account`: furnizează valorizarea stocului pe `stock.move` (câmpurile `l10n_ro_account_id`, `l10n_ro_transfer_account_id`, `l10n_ro_move_type`) pe care se bazează integral interogările SQL ale acestui raport.
