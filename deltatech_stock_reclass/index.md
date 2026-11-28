# Stock Reclassification

- **Nume Tehnic:** `deltatech_stock_reclass`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_stock_reclass
- **Cale Locală:** odoo-addons/deltatech_stock_valuation/deltatech_stock_reclass
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Mută stocul dintr-un cont în altul printr-un document propriu: o regulă stabilește perechile de conturi permise, documentul înregistrează locațiile sursă și destinație și produsele, iar validarea creează transferul de stoc și postează nota contabilă între cele două conturi, la costul mărfii. Documentul păstrează istoricul (cine, când, ce, din ce cont în ce cont), leagă transferul și nota contabilă și poate fi stornat. Accesul este limitat la un grup dedicat.

#### 2. Funcționalități Cheie

- **Reguli de reclasificare** (*Inventar → Operațiuni → Reclassification Rules*): perechea cont sursă / cont destinație, unică per companie, cu conturi diferite; opțional **Management Decision Required** și **Reason Required**. Modulul nu livrează reguli, fiecare companie le definește pe ale sale (ex. 3028 → 371).
- **Documentul de reclasificare** (*Inventar → Operațiuni → Reclassifications*): regulă, locație sursă și destinație (pot fi aceeași locație, când se schimbă doar contul), jurnal, dată, decizie/motiv și linii de produse cu lot/serie (obligatoriu pentru produse urmărite), cantitate și, opțional, linia facturii de furnizor (cantitatea reclasificată nu poate depăși cantitatea liniei).
- Destinația poate fi o locație din afara stocului doar dacă contul destinație nu este de stoc (ex. stoc → mijloc fix).
- **Validare**: verifică regula, decizia, motivul, loturile și stocul disponibil; face un transfer intern (fără nota automată de valorizare), stabilește costul unitar și valoarea liniilor și postează nota contabilă (Dr cont destinație / Cr cont sursă).
- **Stornare**: transfer invers și notă de stornare cu conturile inversate; refuzată dacă stocul din destinație nu mai ajunge. Un document ciornă se șterge, unul validat se poate doar storna, din document, nu cu *Reverse Entry* de pe nota contabilă.
- Cu `l10n_ro_stock_sheet` instalat, mișcarea apare în Balanța analitică stocuri ca ieșire din contul sursă și intrare în contul destinație.
- Două grupuri: **Reclassifications** (creează și validează documente) și **Reclassification Configuration** (administrează regulile).
- Fluxul detaliat, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.reclassification`: documentul de reclasificare (cu `mail.thread`), cu acțiunile de validare, anulare/stornare și deschidere a transferului și a notei contabile.
- `stock.reclassification.line`: linia documentului (produs, lot, cantitate, cost unitar, valoare, linia facturii).
- `stock.reclassification.rule`: perechea de conturi permisă și condițiile (decizie, motiv).
- `stock.move` (extins): legătura mișcărilor cu documentul de reclasificare.

**Vizualizări**

- `view_stock_reclassification_form` / `_list` / `_search`: documentul de reclasificare.
- `view_stock_reclassification_rule_form` / `_list`: regulile de reclasificare.
- `menu_stock_reclassification`, `menu_stock_reclassification_rule`: meniurile din *Inventar → Operațiuni*.

**Acțiuni Automate / Acțiuni Server**

- `ir_sequence_data.xml`: secvența de numerotare a documentelor.

#### 5. Conexiuni

- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): suita de valorizare a stocului.
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md): raportul Balanță analitică stocuri arată mișcarea de reclasificare (nu este dependență).
