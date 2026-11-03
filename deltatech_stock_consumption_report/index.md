# Stock Consumption Report (Raport consumuri stoc)

- **Nume Tehnic:** `deltatech_stock_consumption_report`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_consumption_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_consumption_report`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă contabilului un raport lunar al bonurilor de consum (transferurile de stoc către locații de consum), grupat pe magazin și pe destinația consumului. Gestionarul alege destinația (investiții, consum propriu etc.) pe fiecare bon, dintr-o listă întreținută de companie, iar raportul arată cantitatea și valoarea consumurilor. Rezultatul se vede pe ecran sau se descarcă în Excel, astfel încât contabilitatea să aibă o imagine de ansamblu asupra consumurilor din toate magazinele la închiderea lunii. Modulul nu generează documente și nu înregistrează nimic în contabilitate: citește doar mișcările de stoc deja validate.

#### 2. Funcționalități Cheie

- **Raport lunar al consumurilor**, din *Inventar → Raportare → Raport consumuri*: se alege perioada (implicit luna curentă) și, opțional, tipurile de operațiune (câte unul pe magazin sau depozit), apoi *Vizualizare* (pivot) sau *Export XLSX*. Implicit sunt preselectate tipurile de operațiune a căror destinație implicită este o locație de consum; dacă se golește câmpul, intră toate consumurile din perioadă.
- **Destinația consumului** pe bonul de consum: câmp obligatoriu pe bonurile noi (până la validare, dar poate fi completat și ulterior), copiat pe retururi. Lista se întreține în *Inventar → Configurare → Destinații consum* și e goală după instalare; o destinație nefolosită se arhivează, nu se șterge.
- **Locații de consum**: cu localizarea românească se iau în calcul locațiile de tip *Consum* și *Utilizare*; alte module pot extinde lista prin `stock.location._get_consumption_usages()`.
- **Valoare din contabilitate**: valoarea unui consum este creditul liniilor de produs din nota contabilă a bonului (stocul care iese din contul de stoc); dacă nu există notă contabilă, se folosește valoarea de stoc a mișcării.
- **Pivot pe ecran** pe magazin, destinație și produs, cu cantitate și valoare; rândurile „Nedefinit” sunt bonuri fără destinație.
- **Export XLSX** cu două foi: *centralizat* pe magazin și destinație (produse, cantitate, valoare) și *detaliat* pe magazin, destinație și produs, cu categorie, cost mediu, marcajul „se poate vinde” și cantitatea livrată clienților în ultimele 6 luni, ca să se observe marfa destinată vânzării ieșită pe consum.
- **Marfa folosită intern** trece întâi, la cost, într-o locație de materiale a magazinului (Dr 3028 = Cr 371, prin contul de transfer stoc al companiei), apoi se dă în consum din materiale (Dr 6028 = Cr 3028); marfa dată direct din stocul de vânzare (Dr 607 = Cr 371) e o anomalie, găsită în elementele de jurnal pe 607 cu eticheta `/CNS/` (detalii și corecție în fișa consultant).
- **Acces**: raportul este disponibil rolurilor Inventar / Administrator; destinațiile pot fi citite de orice utilizator de inventar (pentru alegerea pe bon) și modificate doar de administratori. Destinațiile sunt filtrate multi-company.
- Fluxul pas-cu-pas, cu capturi, este în [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock_account`
- Dependență externă Python: `xlsxwriter`

#### 4. Componente Cheie

**Modele**

- `stock.consumption.purpose`: destinația consumului (nume traductibil, secvență, activ, companie).
- `stock.picking` (extins): câmpul `consumption_purpose_id` și câmpul calculat `is_consumption` (transferul merge către o locație de consum).
- `stock.location` (extins): metoda `_get_consumption_usages()` cu tipurile de locație considerate consum.
- `stock.consumption.report.wizard` (tranzitoriu): perioada, tipurile de operațiune, calculul datelor și exportul XLSX.
- `stock.consumption.report.line` (tranzitoriu): liniile raportului (magazin, destinație, produs, cantitate, valoare) afișate în pivot.

**Vizualizări**

- `view_stock_consumption_purpose_list`: lista destinațiilor de consum.
- `view_picking_form` / `view_picking_internal_search`: câmpul și filtrul pe destinația consumului în transferuri.
- `view_stock_consumption_report_wizard_form`: wizardul raportului cu butoanele *Vizualizare* și *Export XLSX*.
- `view_stock_consumption_report_line_pivot` / `view_stock_consumption_report_line_list`: pivotul și lista rezultatelor.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- `l10n_ro_stock_account`: tipurile de locație *Consum* și *Utilizare* folosite ca locații de consum.
- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md): tipărirea bonului de consum.
