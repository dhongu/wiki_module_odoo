# Stock Consumption Report (localizat la `deltatech_stock_consumption_report/index.md`)

- **Nume Tehnic:** `deltatech_stock_consumption_report`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_consumption_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_consumption_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Raport lunar al bonurilor de consum (transferuri către locații de consum), destinat contabilului. Se deschide din *Inventar → Raportare → Consumption report*; permite alegerea perioadei și a tipurilor de operațiuni (câte unul pe magazin sau depozit), apoi vizualizarea în pivot sau exportul XLSX.

#### 2. Funcționalități Cheie

- **Destinația consumului** pe bonul de consum (investiții, uz propriu etc.), aleasă dintr-o listă gestionată în *Inventar → Configurare → Consumption purposes*; obligatorie pe bonurile noi, completabilă și pe cele validate, copiată la retururi. Lista este goală după instalare; o destinație nefolosită se arhivează, nu se șterge.
- **Locații de consum**: cu localizarea română (`l10n_ro_stock_account`) sunt cele de tip *Consumption* și *Usage giving*; alte module pot extinde lista prin `stock.location._get_consumption_usages()`.
- **Valoarea din contabilitate**: valoarea consumului este creditul liniilor de produs din nota contabilă a bonului; fără notă, se folosește valoarea de stoc a mișcării.
- **Wizard de raport**: perioada implicită este luna curentă, iar tipurile de operațiuni cu destinație implicită de consum sunt preselectate; golind câmpul se includ toate consumurile perioadei. *View* afișează pivot pe magazin, destinație și produs (rândurile *Undefined* sunt bonuri fără destinație).
- **Export XLSX** cu două foi: centralizator pe magazin și destinație (produse, cantitate, valoare) și detaliu pe magazin, destinație și produs, cu categorie, cost mediu, indicatorul *Can be sold* și cantitatea livrată clienților în ultimele 6 luni, pentru a depista marfa de vânzare consumată direct din stocul de vânzare.
- Marfa folosită intern se mută întâi printr-un transfer intern către o locație de materiale a magazinului, apoi se emite bonul de consum din acea locație.
- Acces: raportul este disponibil pentru *Inventory / Administrator*; destinațiile pot fi citite de orice utilizator de inventar și modificate de administratori.
- Fluxul pas cu pas (cu capturi) este în fișa consultantului.

#### 3. Dependențe

- `stock_account`
- Dependență Python externă: `xlsxwriter`

#### 4. Componente Cheie

**Modele**

- `stock.consumption.purpose`: destinația consumului (nume, companie).
- `stock.consumption.report.wizard`: wizard-ul cu perioada și tipurile de operațiuni; `action_view` și `action_export_xlsx`.
- `stock.consumption.report.line`: linii tranzitorii folosite de pivot și listă.
- `stock.picking`: câmpul destinația consumului pe bon.
- `stock.location`: `_get_consumption_usages()` (extensibilă) pentru tipurile de locații de consum.

**Vizualizări**

- `view_stock_consumption_purpose_list`: lista destinațiilor de consum.
- `view_picking_form` / `view_picking_internal_search`: câmpul destinației pe transfer și filtrare.
- `view_stock_consumption_report_wizard_form`: wizard-ul raportului.
- `view_stock_consumption_report_line_pivot` / `_list`: vizualizările rezultatelor.

**Acțiuni Automate / Acțiuni Server**

- Nu există (acțiunile de meniu *Consumption report* și *Consumption purposes* sunt ferestre standard).

#### 5. Conexiuni

- `l10n_ro_stock_account`: definește locațiile de tip *Consumption* și *Usage giving* folosite de raport (legătură opțională, nu dependență).
