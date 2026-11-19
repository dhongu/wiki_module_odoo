# Purchase Invoice Currency (Moneda facturii de achiziție)

- **Nume Tehnic:** `deltatech_purchase_currency`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_currency
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_currency`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite facturarea unei comenzi de achiziție într-o altă monedă decât cea a comenzii, aleasă printr-un **Jurnal de facturare** setat pe comandă. Este perechea pe achiziții a modulului [deltatech_sale_currency](../deltatech_sale_currency/index.md). Cazul tipic: un furnizor român confirmă comanda în EUR, dar emite factura în RON la cursul din data facturii.

#### 2. Funcționalități Cheie

- **Jurnal de facturare pe comanda de achiziție** (fila *Other Info*): factura de furnizor se creează în acest jurnal și în moneda lui (moneda companiei, dacă jurnalul nu are monedă). Fără jurnal, factura rămâne în moneda comenzii, ca în Odoo standard, deci furnizorii externi nu sunt afectați.
- **Conversia prețurilor**: prețurile unitare din comandă se convertesc în moneda facturii la cursul de azi la crearea facturii și din nou la cursul *Bill Date* când data este setată sau modificată. Prețul este adus întâi la unitatea de măsură a liniei de factură.
- Schimbarea monedei facturii reconvertește prețurile; modificările manuale de preț se pierd, deci prețurile se corectează după fixarea datei.
- **Curs furnizor** (*Vendor Rate*) pe factura de furnizor: arată cursul din Odoo (BNR) la data facturii, exprimat ca moneda facturii pentru 1 unitate din moneda comenzii (ex. 5,0912 RON pentru 1 EUR); nu mai este 0. Când factura furnizorului indică alt curs, se scrie pe factură **după setarea datei facturii** și prețurile din comandă se convertesc la acel curs. Schimbarea datei facturii readuce cursul BNR al noii date, cu un avertisment care numește cursul înlocuit când acesta fusese scris de mână; golirea câmpului readuce tot cursul Odoo. Câmpul apare doar când liniile provin din comenzi într-o singură altă monedă, iar coloana de comparație cu comanda folosește același curs.
- **Completare automată** (*Auto-Complete*) a unei facturi noi preia jurnalul și moneda din comandă.
- **Indicator de potrivire a prețului** pe liniile facturii: compară prețul facturii cu prețul comenzii convertit în moneda facturii, astfel încât liniile convertite nu apar ca diferențe de preț.
- La facturarea în lot din listă, Odoo grupează după furnizor și monedă, nu după jurnal: comenzile cu jurnale diferite, dar aceeași monedă, ajung pe o factură, în jurnalul primei comenzi.
- **Punct de extensie** pentru alt curs (de exemplu BNR plus un procent convenit cu furnizorul): `account.move._get_purchase_odoo_rate()`, adică cursul pus automat în câmpul Curs furnizor. Nu se folosește `purchase.order.line._get_invoice_price_unit()` pentru asta: Curs furnizor este mereu completat și câștigă asupra lui (issue dhongu/deltatech#4257).
- **Disponibilitate:** modulul există și pe 19.0, în PR-ul dhongu/deltatech#4256, încă neunit.

Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): câmpul `journal_id` (Jurnal de facturare), moneda facturii și pregătirea facturii (`_get_invoice_currency`, `_prepare_invoice`).
- `purchase.order.line` (extins): `_get_invoice_price_unit()` pentru conversia prețului (nu este punctul de extensie pentru alt curs); `_prepare_account_move_line` aplică prețul convertit.
- `account.move` (extins): reconversia prețurilor la schimbarea datei facturii sau a monedei; câmpul `purchase_vendor_rate` (Curs furnizor, nenegativ, completat cu cursul Odoo la data facturii), câmpul ascuns `purchase_odoo_rate` (ultimul curs completat automat, folosit pentru a recunoaște un curs scris de mână), `_get_purchase_odoo_rate()` (punctul de extensie pentru alt curs) și `_get_purchase_vendor_rate()`.
- `account.move.line` (extins): calculul mesajului de potrivire a prețului față de comandă.

**Vizualizări**

- `purchase_order_form`: adaugă Jurnalul de facturare în fila *Other Info* a comenzii.
- Vizualizarea facturii de furnizor (`account_move_views.xml`): câmpul Curs furnizor în antet, sub date.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_sale_currency](../deltatech_sale_currency/index.md): perechea pe vânzări (factura de client în altă monedă decât comanda).
