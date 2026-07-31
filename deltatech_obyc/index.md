# Deltatech OBYC - Account Determination (localizat la `deltatech_obyc/index.md`)

- **Nume Tehnic:** `deltatech_obyc`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_obyc
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_obyc`
- **Ultima Ingestie:** `2026-07-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Deltatech OBYC - Account Determination aduce în Odoo un mecanism de determinare automată a conturilor contabile pentru tranzacțiile de stoc, inspirat din conceptul SAP OBYC (Object-based valuation and account determination for inventorY and Cost management). În loc ca notele contabile de stoc să fie derivate doar din categoria de produs, modulul le determină dintr-o matrice de reguli configurabilă, bazată pe combinația dintre cheia de tranzacție (recepție, livrare, retur, transfer intern, ajustare de inventar, producție, dropship, landed cost etc.), clasa de evaluare a produsului, aria de evaluare, un modificator contabil opțional și companie. Astfel, contabilitatea de stoc poate fi mult mai fin segmentată decât permite mecanismul standard Odoo cu două conturi, oferind un al treilea cont dedicat diferențelor de valorizare.

#### 2. Funcționalități Cheie

- Definește o matrice de mapare flexibilă (`product.account.determination`) pentru atribuirea automată a conturilor contabile (sursă, destinație, evaluare) pe baza cheii de tranzacție, clasei de evaluare, ariei de evaluare, modificatorului contabil și companiei.
- Introduce date de bază configurabile: `product.valuation.class` (clasă de evaluare atașată pe șablonul de produs) și `account.modifier` (modificator contabil opțional, folosit de exemplu pe tipul de operațiune de stoc sau pe jurnal).
- Calculează automat cheia de tranzacție pe mișcările de stoc, pe baza combinației uzanță sursă/destinație (furnizor, client, intern, tranzit), pentru operațiuni precum recepție, livrare, retur de la client, retur la furnizor, transfer intern, dropship.
- Suprascrie determinarea contului pe liniile de factură (`account.move.line`): documentele de vânzare folosesc cheia `stock_income`, cele de achiziție folosesc `stock_receipt`, iar linia primește și aria de evaluare corespunzătoare.
- Dacă nu există regulă de determinare pentru o combinație dată, ridică un `RedirectWarning` care trimite direct spre ecranul de configurare a regulilor, cu contextul precompletat (în loc de o eroare simplă, greu de acționat).
- Notele contabile generate păstrează `product_id` și o cantitate semnată (pozitivă pe debit, negativă pe credit) plus unitatea de măsură — convenție necesară stratului de evaluare (`deltatech_stock_valuation`) care reconstruiește mișcările cantitativ-valorice direct din liniile notei contabile.
- Dacă aria de evaluare a mișcării are completat câmpul „Stock Journal", nota OBYC se postează pe jurnalul ariei, nu pe jurnalul de stoc al companiei — permite separarea notelor de stoc pe gestiune/arie.
- Cu opțiunea „Storno accounting" activă pe companie, retururile (mișcări care au la origine o mișcare returnată) generează o notă „în roșu" (aceleași conturi ca tranzacția originală, cu sume negative), în loc de o notă inversată clasică.
- Suportă și `landed_cost` ca o cheie de tranzacție dedicată, prin extinderea liniilor de ajustare a costului de aterizare (`stock.valuation.adjustment.lines`).
- Dacă produsul nu are `valuation_class_id` completat, fluxul revine automat la comportamentul standard de valorizare Odoo, fără a bloca sau altera notele contabile existente.

**Chei de tranzacție.** Modulul definește 18 chei în `TRANSACTION_KEYS`
(`models/product_account_determination.py`): `stock_valuation`, `price_difference`,
`stock_receipt`, `return_to_supplier`, `stock_receipt_price_difference`, `stock_delivery`,
`return_from_customer`, `stock_income`, `dropship`, `dropship_return`, `internal_transfer`,
`internal_transfer_out`, `internal_transfer_in`, `inventory_adjustment_plus`,
`inventory_adjustment_minus`, `production_issue`, `production_receipt`, `landed_cost`.
Pe mișcările de stoc, cheia se deduce din uzanța locațiilor sursă/destinație
(`stock.move._compute_transaction_key`, 13 combinații acoperite, inclusiv tranzit); dacă nicio
combinație nu se potrivește, mișcarea ridică `UserError`, iar contextul `price_difference`
suprascrie cheia calculată. Cheile `stock_income`/`stock_receipt` se determină și pe
`account.move.line`, iar `landed_cost` pe `stock.landed.cost`.

> **Notă de corecție (2026-07-31):** `readme/DESCRIPTION.md` conținea referințe la Odoo 17
> (mențiunea „compatible with Odoo 17 Enterprise & Community" și link-urile către documentația
> oficială 17.0) și o listă **incompletă** de chei de tranzacție — lipseau `price_difference`,
> `stock_receipt_price_difference` și `landed_cost`, iar tabelul de determinare implicită acoperea
> doar 6 din cele 13 combinații de uzanțe. Corectat direct în modul (v19.0.1.0.1, vezi
> `readme/HISTORY.md`); pagina reflectă acum codul 19.0.

#### 3. Dependențe

- `stock`
- `account`
- `stock_account`
- `purchase_stock`
- `stock_landed_costs`
- [deltatech_valuation_area](../deltatech_valuation_area/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de mai sus (Sumar și Funcționalități Cheie) sunt preluate din `readme/DESCRIPTION.md` și `readme/FISA_CONSULTANT.md`; acestea nu solicită explicit detalierea Componentelor Cheie (Vizualizări, Acțiuni Automate). Totuși, modelele introduse sau extinse sunt explicit menționate în readme, motiv pentru care sunt listate mai jos ca reper tehnic.

**Modele**

- `product.account.determination`: regula centrală de mapare — combină cheia de tranzacție, modificatorul contabil, clasa de evaluare, aria de evaluare și compania pentru a stabili contul sursă, contul destinație și contul de evaluare.
- `product.valuation.class`: date de bază pentru clasificarea contabilă a produselor (ex. materii prime, produse finite), afișată în format `[COD] Nume`.
- `account.modifier`: modificator contabil opțional pentru rafinarea suplimentară a selecției regulii, afișat în format `[COD] Nume`.
- `product.template` (extindere): adaugă câmpul de clasă de evaluare pe șablonul de produs.
- `stock.move` (extindere): calculează cheia de tranzacție și generează notele contabile OBYC pe mișcările de stoc.
- `stock.picking.type` (extindere): permite atașarea unui modificator contabil pe tipul de operațiune.
- `account.journal` (extindere): permite atașarea unui modificator contabil pe jurnal.
- `account.move.line` (extindere): recalculează contul pe liniile de produs din facturi, pe baza cheii de tranzacție și a ariei de evaluare.
- `stock.valuation.adjustment.lines` (extindere): integrează cheia de tranzacție `landed_cost` în determinarea contului pentru costurile de aterizare.

#### 5. Conexiuni

- [deltatech_valuation_area](../deltatech_valuation_area/index.md): furnizează conceptul de arie de evaluare (`valuation.area`), folosit ca dimensiune de selecție a regulilor OBYC și pentru jurnalul de stoc dedicat pe arie.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): stratul de evaluare care reconstruiește mișcările cantitativ-valorice direct din liniile notei contabile generate de acest modul (cantitate semnată + unitate de măsură pe linii).
