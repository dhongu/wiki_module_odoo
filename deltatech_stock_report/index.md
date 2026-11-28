# Stock Picking Report (localizat la `deltatech_stock_report/index.md`)

- **Nume Tehnic:** `deltatech_stock_report`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Managerii au adesea nevoie să știe cât a intrat de la un furnizor sau cât a ieșit către un client într-o perioadă. Modulul adaugă raportul *Picking Analysis* pe transferurile efectuate, sub formă de tabel pivot și listă.

#### 2. Funcționalități Cheie

- Doar mișcări efectuate: fiecare rând este un transfer, produs, locație sursă și locație destinație, construit din mișcările de stoc în starea *done*; mișcările fără transfer sunt excluse.
- Cantitate cu semn și valoare pozitivă: *Cantitatea* este cea din cerere, în unitatea de măsură a produsului; e pozitivă când destinația este internă (inclusiv între două locații interne) și negativă altfel. *Valoarea* este cea stocată pe mișcare, sau cantitatea înmulțită cu prețul unitar când lipsește.
- Pivot și listă: pivotul se deschide grupat după *Tip operațiune*, apoi *Entitate comercială*; lista arată partenerul transferului, cu totaluri, și coloane opționale (dată, locații, categorie).
- Filtre și grupări: filtrele *Incoming*, *Internal* și *Outgoing* după tipul operațiunii; filtrul de dată folosește data efectuării; grupare după produs, categorie, partener, locație, locație destinație sau dată.
- Raport doar în citire, accesibil managerilor de stoc (`stock.group_stock_manager`); utilizatorii văd transferurile companiilor active.
- Meniu: `Inventar > Raportare`; fluxul de citire și export este în fișa consultantului.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.picking.report`: model SQL de tip vizualizare (`_auto = False`), construit peste `stock_picking` și `stock_move`, pentru mișcările în starea `done`.

**Vizualizări**

- `view_stock_picking_report_pivot`: pivotul implicit (tip operațiune, entitate comercială).
- `view_stock_picking_report_tree`: lista cu totaluri pe cantitate și valoare.
- `view_stock_picking_report_filter`: filtre și grupări.
- `action_stock_picking_report`: acțiunea din meniul *Picking Analysis*.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_stock_account](../deltatech_stock_account/index.md): completează valorizarea contabilă a stocurilor, folosită prin valoarea mișcărilor.
- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): raportare de stoc specifică localizării românești; raportul de față oferă o analiză complementară a pozițiilor din transferuri.
