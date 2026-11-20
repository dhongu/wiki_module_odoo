# Purchase Invoice Currency (Facturare achiziții în altă monedă) (localizat la `deltatech_purchase_currency/index.md`)

- **Nume Tehnic:** `deltatech_purchase_currency`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_currency
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_currency`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite facturarea unei comenzi de achiziție într-o altă monedă decât cea a comenzii, aleasă prin **Jurnalul de facturare** setat pe comandă. Cazul tipic: un furnizor român oferă și confirmă comanda în EUR, dar emite factura în RON la cursul din data facturii. Este omologul pentru achiziții al modulului [deltatech_sale_currency](../deltatech_sale_currency/index.md).

#### 2. Funcționalități Cheie

- **Jurnal de facturare pe comandă** (tab-ul *Alte informații*): factura de furnizor se creează în acest jurnal și în moneda lui (moneda companiei, dacă jurnalul nu are monedă). Fără jurnal, factura rămâne în moneda comenzii, ca în Odoo standard, deci furnizorii externi nu sunt afectați.
- **Conversia prețurilor**: prețurile unitare din comandă se convertesc în moneda facturii la cursul zilei la crearea facturii și din nou la cursul din *Data facturii* când aceasta se setează sau se schimbă. Prețul este adus întâi la unitatea de măsură a liniei facturii (ex. duzină în loc de bucată).
- **Curs furnizor** pe factură: se completează cu cursul Odoo (BNR) din data facturii, exprimat în moneda facturii pentru 1 unitate din moneda comenzii (ex. 5,0912 RON pentru 1 EUR). Dacă factura furnizorului indică alt curs, se scrie acolo (după setarea datei facturii) și prețurile se convertesc la el. Schimbarea datei facturii readuce cursul Odoo și afișează un avertisment când înlocuiește un curs scris de mână; golirea câmpului readuce, de asemenea, cursul Odoo. Câmpul apare doar când liniile provin din comenzi într-o singură altă monedă.
- **Completare automată** a unei facturi noi: preia jurnalul și moneda comenzii, cu prețurile convertite.
- **Facturare grupată**: la *Creați facturi* din listă, Odoo grupează după furnizor și monedă, nu după jurnal; comenzile cu jurnale diferite, dar aceeași monedă, ajung pe o singură factură, în jurnalul primei comenzi. Pentru jurnale separate, se facturează pe rând.
- **Atenție la corecții manuale**: schimbarea datei sau a monedei facturii reconvertește prețurile din comandă și pierde modificările făcute de mână pe linii; prețurile se corectează după fixarea datei.
- **Diferență față de 20.0**: pe 19.0 nu există indicatorul de potrivire a prețului pe liniile facturii.
- **Punct de extindere pentru alt curs** (de exemplu BNR + un procent convenit cu furnizorul): `account.move._get_purchase_odoo_rate()`. Nu se suprascrie `purchase.order.line._get_invoice_price_unit()`, care aplică mereu cursul primit, iar *Curs furnizor* este mereu completat și are prioritate (vezi issue [dhongu/deltatech#4257](https://github.com/dhongu/deltatech/issues/4257)).

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order`: câmpul Jurnal de facturare și moneda facturii; completează valorile facturii create din comandă.
- `purchase.order.line`: `_get_invoice_price_unit()` convertește prețul (unitate de măsură și curs) și aplică mereu cursul primit.
- `account.move`: câmpurile Curs furnizor / curs Odoo și moneda sursă a comenzilor; `_get_purchase_odoo_rate()` dă cursul implicit, iar onchange-urile pe data facturii, monedă și curs reconvertesc prețurile.

**Vizualizări**

- `purchase_order_form`: Jurnal de facturare în tab-ul *Alte informații* al comenzii.
- `view_move_form`: câmpul Curs furnizor în antetul facturii de furnizor.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_sale_currency](../deltatech_sale_currency/index.md): perechea pentru vânzări (facturare client în altă monedă decât comanda).
- `terrabit_interheat`: proiectul Interheat depinde de acest modul.
