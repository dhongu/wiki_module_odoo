# Purchase Invoice Currency (Moneda facturii de achiziție)

- **Nume Tehnic:** `deltatech_purchase_currency`
- **Versiune:** `20.0.1.0.0`
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
- **Completare automată** (*Auto-Complete*) a unei facturi noi preia jurnalul și moneda din comandă.
- **Indicator de potrivire a prețului** pe liniile facturii: compară prețul facturii cu prețul comenzii convertit în moneda facturii, astfel încât liniile convertite nu apar ca diferențe de preț.
- La facturarea în lot din listă, Odoo grupează după furnizor și monedă, nu după jurnal: comenzile cu jurnale diferite, dar aceeași monedă, ajung pe o factură, în jurnalul primei comenzi.
- **Punct de extensie** `purchase.order.line._get_invoice_price_unit()` pentru alt curs (de exemplu cursul BNR plus un procent convenit cu furnizorul).

Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): câmpul `journal_id` (Jurnal de facturare), moneda facturii și pregătirea facturii (`_get_invoice_currency`, `_prepare_invoice`).
- `purchase.order.line` (extins): `_get_invoice_price_unit()` pentru conversia prețului; `_prepare_account_move_line` aplică prețul convertit.
- `account.move` (extins): reconversia prețurilor la schimbarea datei facturii sau a monedei.
- `account.move.line` (extins): calculul mesajului de potrivire a prețului față de comandă.

**Vizualizări**

- `purchase_order_form`: adaugă Jurnalul de facturare în fila *Other Info* a comenzii.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_sale_currency](../deltatech_sale_currency/index.md): perechea pe vânzări (factura de client în altă monedă decât comanda).
