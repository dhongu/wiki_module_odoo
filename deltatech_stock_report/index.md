# Stock Reports (localizat la `deltatech_stock_report/index.md`)

- **Nume Tehnic:** `deltatech_stock_report`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_report`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul adaugă un raport analitic dedicat mișcărilor de stoc finalizate, construit pe baza pozițiilor (liniilor) din transferurile de stoc (picking-uri). Practic, agregă toate liniile de mișcare în stare „done" și le pune la dispoziția utilizatorului sub formă de tabel pivot și listă, cu posibilități bogate de filtrare și grupare. Astfel, departamentul de logistică sau management poate analiza rapid cantitățile și valorile vehiculate pe tipuri de operațiuni (recepții, livrări, transferuri interne), pe parteneri, produse, categorii sau locații, fără a fi nevoie de extrageri manuale din documentele individuale.

#### 2. Funcționalități Cheie

- Raport de analiză a transferurilor de stoc bazat pe pozițiile (liniile) din picking-uri finalizate.
- Vizualizare pivot și listă, cu măsuri pe cantitate și valoare (amount).
- Filtre predefinite pe tip de operațiune: Recepții (incoming), Interne (internal) și Livrări (outgoing).
- Grupare configurabilă după tip operațiune, partener, entitate comercială, categorie de produs, produs, locație, locație destinație, dată sau companie.
- Calculul cantității cu semn în funcție de utilizarea locației destinație (intrările în locații interne sunt pozitive, restul negative).
- Calculul valorii și al prețului unitar pe baza valorii mișcării de stoc (`sm.value`), cu revenire la prețul unitar atunci când valoarea lipsește.
- Acces dedicat din meniul de rapoarte al depozitului („Picking Analysis"), restricționat la grupul de management al stocului.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.picking.report`: Model SQL de tip vizualizare (`_auto = False`), care nu stochează date proprii, ci este construit dintr-un `CREATE VIEW` peste `stock_picking` și `stock_move`. Agregă mișcările finalizate (`state = 'done'`) și expune câmpuri precum partener, entitate comercială, tip operațiune, dată, companie, categorie, produs, locații, cantitate, preț unitar, valoare și greutate.

**Vizualizări**

- `view_stock_picking_report_pivot`: Tabelul pivot principal (rânduri pe tip operațiune și entitate comercială, măsuri pe cantitate și valoare).
- `view_stock_picking_report_tree`: Lista cu liniile de raport și totaluri pe cantitate și valoare; coloanele de dată, locații și categorie sunt opționale/ascunse implicit.
- `view_stock_picking_report_filter`: Vizualizarea de căutare cu filtrele pe tip operațiune și grupările configurabile.
- `action_stock_picking_report`: Acțiunea de fereastră „Picking Report" (mod pivot, list), accesibilă din meniul `Picking Analysis` sub rapoartele de depozit.

#### 5. Conexiuni

- [deltatech_stock_account](../deltatech_stock_account/index.md): completează partea de valorizare contabilă a stocurilor pe care acest raport o folosește prin valoarea mișcărilor.
- `l10n_ro_stock_report`: raportare de stoc specifică localizării românești (fișa de magazie, balanțe); raportul de față oferă o analiză complementară a pozițiilor din picking-uri.
