# Deltatech OBYC - Account Determination (localizat la `deltatech_obyc/index.md`)

- **Nume Tehnic:** `deltatech_obyc`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_obyc
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_obyc`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Deltatech OBYC - Account Determination aduce în Odoo un mecanism de determinare automată a conturilor contabile pentru tranzacțiile de stoc, inspirat din conceptul SAP OBYC. În loc ca notele contabile de stoc să fie derivate doar din categoria produsului, modulul le determină dintr-o matrice de reguli configurabilă, în funcție de cheia de tranzacție (recepție, livrare, retur, transfer intern, ajustare de inventar, producție, dropship, landed cost etc.), clasa de evaluare a produsului, aria de evaluare, un modificator contabil opțional și companie. Contabilitatea de stoc poate fi astfel segmentată mult mai fin decât permite mecanismul standard Odoo, iar costul mărfii vândute se înregistrează la livrare, conform regulilor contabile românești.

#### 2. Funcționalități Cheie

- Matrice de mapare flexibilă (`product.account.determination`) pentru atribuirea automată a conturilor: cont sursă, cont destinație și cont de evaluare, pe baza cheii de tranzacție, clasei de evaluare, ariei de evaluare, modificatorului contabil și companiei.
- Date de bază configurabile: `product.valuation.class` (clasă de evaluare pe șablonul de produs) și `account.modifier` (modificator contabil opțional, pe tipul de operațiune sau pe jurnal).
- Cheia de tranzacție se calculează automat pe mișcarea de stoc din uzanța locațiilor sursă/destinație (furnizor, client, intern, tranzit, inventar, producție): 16 combinații acoperite; pentru o combinație necunoscută se ridică eroare, iar contextul `price_difference` suprascrie cheia calculată.
- Regula de contare a conturilor la mișcarea de stoc: cu contul sursă completat nota este Dr Evaluare / Cr Sursă (intrări); cu sursa goală, Dr Destinație / Cr Evaluare (ieșiri); cu toate trei goale nu se generează notă.
- Fără notă contabilă pentru: produse nestocabile, categorii fără evaluare în timp real, cantități zero, stoc al unui terț și mișcări ignorate de evaluarea standard.
- **Costul mărfii vândute se înregistrează la livrare**, pe nota mișcării de stoc (cheia `stock_delivery`, ex. Dr 607 / Cr 371), nu la postarea facturii: pentru produsele cu clasă de evaluare, factura de vânzare nu mai conține linii COGS (`account.move._get_cogs_lines_vals`), deci costul nu se dublează. Cazurile neacoperite (livrat și nefacturat la sfârșit de lună, consignație, facturi înainte de livrare) sunt descrise în `readme/bugs.md`.
- Conturile liniilor de factură: documentele de vânzare (factură, notă de credit) folosesc contul destinație al regulii `stock_income`, cele de achiziție contul sursă al regulii `stock_receipt` (contul de evaluare doar dacă acela e gol); linia primește și aria de evaluare. Diferențele de preț și de curs dintre recepție și factura furnizorului nu sunt tratate, rămân pe 408 și se regularizează manual.
- Landed cost: cheie dedicată `landed_cost` (Dr contul de evaluare / Cr contul liniei de cost), prin extinderea `stock.valuation.adjustment.lines`.
- Jurnal pe arie: dacă aria de evaluare are „Stock Journal", nota OBYC se postează pe jurnalul ariei.
- Storno: cu opțiunea „Storno accounting" pe companie, retururile generează o notă „în roșu" (aceleași conturi, sume negative).
- Ajustări de inventar: câștigul la inventar (inventar → intern) folosește `inventory_adjustment_plus`, lipsa (intern → inventar) `inventory_adjustment_minus` (în versiunile înainte de 20.0.1.0.5 cheile erau inversate).
- Dacă regula lipsește, se ridică un `RedirectWarning` cu trimitere directă la configurarea regulilor; produsele fără clasă de evaluare rămân pe comportamentul standard Odoo.
- Notele păstrează `product_id`, cantitate semnată și unitate de măsură, convenție necesară stratului `deltatech_stock_valuation`.
- Neacoperit: stoc evaluat la preț cu amănuntul (371 cu adaos pe 378 și TVA pe 4428); ruta de transfer între arii prin tranzit (`internal_transfer_out`/`in`) nu este validată în Odoo 20 (mișcarea stoc → tranzit nu primește valoare, OBYC-009) și nu trebuie folosită.
- Meniuri: configurare în Inventar, submeniul „Account Determination Config" cu „Evaluation Class", „Account Modifiers" și „Product Account Determination".

**Chei de tranzacție (18).** `stock_valuation`, `price_difference`, `stock_receipt`, `return_to_supplier`, `stock_receipt_price_difference`, `stock_delivery`, `return_from_customer`, `stock_income`, `dropship`, `dropship_return`, `internal_transfer`, `internal_transfer_out`, `internal_transfer_in`, `inventory_adjustment_plus`, `inventory_adjustment_minus`, `production_issue`, `production_receipt`, `landed_cost`.

Exemple de mapări (plan de conturi românesc; MF = mărfuri, RM = materii prime, FG = produse finite): recepție MF Dr 371 / Cr 408; livrare MF Dr 607 / Cr 371; livrare FG Dr 711 / Cr 345; retur de la client Dr 371 / Cr 607; consum producție Dr 601 / Cr 301; predare din producție Dr 345 / Cr 711; transfer intern în aceeași arie: fără notă. Fluxul detaliat pas cu pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

> **Notă de corecție (2026-10-01):** `readme/DESCRIPTION.md` este deja aliniat la Odoo 20 (fără referințe la versiuni vechi); pagina reflectă codul 20.0.1.0.6, inclusiv trecerea COGS la livrare, cheile de inventar corectate și recunoașterea a 16 combinații de uzanțe (față de 13 în ingestia de 19.0).

#### 3. Dependențe

- `stock`
- `account`
- `stock_account`
- `purchase_stock`
- `stock_landed_costs`
- [deltatech_valuation_area](../deltatech_valuation_area/index.md)

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md` și `readme/FISA_CONSULTANT.md`; modelele sunt listate ca reper tehnic.

**Modele**

- `product.account.determination`: regula centrală de mapare (cheie, modificator, clasă, arie, companie, conturi sursă/destinație/evaluare).
- `product.valuation.class`: clasificarea contabilă a produselor, afișată `[COD] Nume`.
- `account.modifier`: modificator contabil opțional, afișat `[COD] Nume`.
- `product.template` (extindere): clasa de evaluare pe produs.
- `stock.move` (extindere): calculul cheii de tranzacție, regula de cont, crearea notei contabile OBYC (jurnal pe arie, storno la retururi) și valorizarea mișcării.
- `stock.move.line` (extindere): actualizează valoarea mișcării la modificarea cantităților.
- `stock.picking.type` și `account.journal` (extinderi): atașează un modificator contabil.
- `account.move` (extindere): elimină liniile COGS de pe factura de vânzare pentru produsele OBYC.
- `account.move.line` (extindere): contul liniilor de factură pe baza cheii și a ariei de evaluare.
- `stock.valuation.adjustment.lines` (extindere): cheia `landed_cost`.

**Vizualizări**

- `view_product_account_determination_tree` / `_form`: lista și formularul regulilor de determinare.
- `view_product_valuation_class_tree` / `_form`: clase de evaluare.
- `view_account_modifier_tree` / `_form`: modificatori contabili.
- `view_product_template_form_valuation_class`, `view_product_template_search_valuation_class`, `view_product_template_tree_valuation_class`: clasa de evaluare pe produs.
- `view_picking_type_form`, `view_account_bank_journal_form`: modificatorul contabil pe tipul de operațiune și pe jurnal.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau cron; modulul oferă doar acțiuni de fereastră pentru regulile de determinare, clasele de evaluare și modificatorii contabili.

#### 5. Conexiuni

- [deltatech_valuation_area](../deltatech_valuation_area/index.md): furnizează aria de evaluare, dimensiune de selecție a regulilor și jurnal de stoc dedicat.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): stratul de evaluare care reconstruiește mișcările cantitativ-valorice din liniile notei generate de acest modul.
