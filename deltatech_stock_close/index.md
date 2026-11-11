# Stock Close (localizat la `deltatech_stock_close/index.md`)

- **Nume Tehnic:** `deltatech_stock_close`
- **Versiune:** `19.0.1.1.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_close
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_close`
- **Ultima Ingestie:** `2026-11-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul lasă mișcările de stoc închise în afara fișei de magazie (raportul românesc de stocuri). După închiderea unei perioade sau a exercițiului financiar, fișa de magazie poate fi rulată doar pe mișcările încă deschise, ceea ce menține rapoartele de inventar clare și rapide.

#### 2. Funcționalități Cheie

- Fiecare mișcare de stoc primește marcajul **Valorizare Activă** (*Valuation Active*), activ implicit; o mișcare cu marcajul debifat este considerată închisă. În Odoo 19 valorizarea e ținută pe `stock.move`, deci marcajul se setează acolo.
- Asistentul **Close Stock Moves** (*Inventar > Operațiuni > Ajustări > Close Stock Moves*, destinat responsabililor de stoc): în **Close until** se alege ultima zi a perioadei închise, iar toate mișcările de stoc finalizate ale companiei datate până la acea zi inclusiv se închid. Nicio notă contabilă nu se modifică.
- Pe lista mișcărilor de stoc (*Inventar > Raportare > Moves Analysis*), coloana opțională **Valuation Active** (ascunsă implicit) și filtrul **Closed** permit verificarea sau redeschiderea unei singure mișcări (se reactivează comutatorul **Valuation Active**).
- Fișa de magazie din localizarea românească (*Inventar > Raportare > Romanian Stock Sheet Report*) primește opțiunea **Only Active**: bifată, soldul inițial, intrările, ieșirile și soldul final exclud mișcările închise (deci dispare și soldul inițial format din mișcări închise).
- Cu opțiunea debifată, fișa este exact cea din localizarea românească, cu stocul complet și cifrele care corespund contului de stoc; mișcările nu sunt ascunse nicăieri altundeva în Odoo.
- Nu trimite date în afara Odoo. Flux pas cu pas în fișa consultant.

#### 3. Dependențe

- `stock_account`
- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.move` (extins): câmpul boolean `l10n_ro_valuation_active` (Valorizare Activă), activ implicit.
- `l10n.ro.stock.storage.sheet` (extins): câmpul `only_active` și filtrarea SQL a soldului inițial, intrărilor, ieșirilor și soldului final după mișcările active.
- `stock.close.moves` (tranzitoriu): asistentul care închide mișcările finalizate ale companiei până la o dată (`action_close`).

**Vizualizări**

- `view_move_tree_valuation_active`: coloana opțională Valuation Active pe lista mișcărilor de stoc.
- `view_move_search_valuation_active`: filtrul Closed pe căutarea mișcărilor de stoc.
- `view_stock_sheet_report_form_active`: opțiunea Only Active în formularul fișei de magazie.
- `view_stock_close_moves_form`: formularul asistentului Close Stock Moves (acțiunea `action_stock_close_moves`, cu meniu în Inventar).

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): modulul extins direct — acest modul adaugă opțiunea „Only Active” în fișa de magazie, pentru a exclude mișcările închise din rapoartele de gestiune.
