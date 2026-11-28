# Stock Close (localizat la `deltatech_stock_close/index.md`)

- **Nume Tehnic:** `deltatech_stock_close`
- **Versiune:** `20.0.1.1.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_close
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_close`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul lasă mișcările de stoc închise în afara fișei de magazie românești (din `l10n_ro_stock_report`): după închiderea unei perioade sau a unui exercițiu financiar, fișa de magazie poate fi rulată doar pe mișcările încă deschise. Se păstrează astfel rapoartele de inventar lizibile și rapide.

#### 2. Funcționalități Cheie

- **Indicatorul Valuation Active:** fiecare mișcare de stoc primește indicatorul **Valuation Active**, activ implicit; o mișcare cu indicatorul dezactivat este considerată închisă (evaluarea se ține pe mișcarea de stoc).
- **Opțiunea Only active** în asistentul fișei de magazie: când e bifată, soldul inițial, intrările, ieșirile și soldul final exclud mișcările închise. Fără opțiune, fișa este cea din localizarea românească, iar mișcările nu sunt ascunse în alte locuri din Odoo.
- **Close Stock Moves** (*Inventar > Operațiuni > Ajustări > Close Stock Moves*): închide toate mișcările de stoc efectuate ale companiei, datate cel târziu la ziua aleasă în **Close until**; nicio înregistrare contabilă nu se modifică. Asistentul este pentru gestionarii de stoc.
- **Coloana Valuation Active** (ascunsă implicit) și filtrul **Closed** în lista mișcărilor de stoc (*Inventar > Raportare > Moves Analysis*), pentru verificarea sau redeschiderea unei singure mișcări (se reactivează comutatorul).
- Nu se trimit date în afara Odoo.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `stock_account`
- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.move` (extins): indicatorul **Valuation Active**.
- `l10n.ro.stock.storage.sheet` (extins): opțiunea **Only active** a fișei de magazie.
- `stock.close.moves` (asistent): închiderea mișcărilor până la o dată.

**Vizualizări**

- `view_move_tree_valuation_active` și `view_move_search_valuation_active`: coloana și filtrul **Closed** în lista mișcărilor de stoc.
- `view_stock_sheet_report_form_active`: opțiunea **Only active** în asistentul fișei de magazie.
- `view_stock_close_moves_form` / `action_stock_close_moves`: asistentul **Close Stock Moves**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server; accesul la asistent este dat grupului gestionar de stoc prin `security/ir.access.csv`.

#### 5. Conexiuni

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): modulul extins direct — fișa de magazie primește opțiunea **Only active**.
