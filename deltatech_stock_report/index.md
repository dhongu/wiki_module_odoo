# Stock Picking Report (localizat la `deltatech_stock_report/index.md`)

- **Nume Tehnic:** `deltatech_stock_report`
- **Versiune:** `19.0.1.0.10`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_report`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Managerii au adesea nevoie să afle cât a intrat de la un furnizor sau ce a ieșit către un client într-o perioadă. Modulul adaugă un raport *Picking Analysis* pe transferurile de stoc finalizate, sub formă de tabel pivot și de listă, cu filtrare și grupare după tipul operațiunii, partener, produs, categorie sau locație. Astfel, logistica sau managementul analizează rapid cantitățile și valorile vehiculate, fără extrageri manuale din documentele individuale.

#### 2. Funcționalități Cheie

- **Doar mișcări finalizate:** fiecare rând reprezintă un transfer, un produs, o locație sursă și o locație destinație, construit din mișcări de stoc în stare „done”. Mișcările din afara unui transfer sunt excluse.
- **Cantitate și valoare cu semn:** *Quantity* este cantitatea procesată, în unitatea de măsură a produsului. *Amount* este valoarea stocată pe mișcarea de stoc sau, în lipsă, cantitatea înmulțită cu prețul unitar al mișcării. Ambele sunt pozitive când destinația este o locație internă (inclusiv la mișcări între două locații interne) și negative în rest.
- **Pivot și listă:** pivotul se deschide grupat după *Picking Type*, apoi *Commercial Entity*; rândurile arată și *Partner* al transferului. Lista însumează cantitatea și valoarea, iar *Date*, *Location*, *Location Destination* și *Category* sunt coloane opționale.
- **Filtre și grupări:** filtrele *Incoming*, *Internal* și *Outgoing* aleg după tipul operațiunii, iar filtrul de dată folosește data la care s-a încheiat transferul. Rândurile se mai pot grupa după produs, categorie, partener, locație, locație destinație, dată sau companie.
- **Acces și companii:** raportul este doar pentru citire, disponibil managerilor de stoc (`stock.group_stock_manager`), din meniul *Picking Analysis* sub rapoartele de depozit; utilizatorii văd doar transferurile companiilor lor active.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.picking.report`: model SQL de tip vizualizare (`_auto = False`), construit printr-un `CREATE VIEW` peste `stock_picking` și `stock_move`. Agregă mișcările `done` și expune partener, entitate comercială, tip operațiune, dată (`date_done`), companie, categorie, produs, locații, cantitate cu semn, preț unitar, valoare și greutate.

**Vizualizări**

- `view_stock_picking_report_pivot`: pivotul principal (rânduri pe tip operațiune și entitate comercială, măsuri pe cantitate și valoare).
- `view_stock_picking_report_tree`: lista cu totaluri pe cantitate și valoare; coloanele de dată, locații și categorie sunt ascunse implicit.
- `view_stock_picking_report_filter`: căutarea, cu filtrele pe tip operațiune și grupările configurabile.
- `action_stock_picking_report`: acțiunea de fereastră „Picking Report” (pivot, listă), din meniul `Picking Analysis` sub rapoartele de depozit.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_stock_account](../deltatech_stock_account/index.md): completează partea de valorizare contabilă a stocurilor pe care acest raport o folosește prin valoarea mișcărilor.
- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): raportare de stoc specifică localizării românești (fișa de magazie, balanțe); raportul de față oferă o analiză complementară a pozițiilor din transferuri.
