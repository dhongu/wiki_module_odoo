# Sale Invoice Currency (localizat la `deltatech_sale_currency/index.md`)

- **Nume Tehnic:** `deltatech_sale_currency`
- **Versiune:** `20.0.0.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_currency`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_currency`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează conversia valutară între comenzile de vânzare și facturile generate din ele. Este util companiilor care ofertează și își țin listele de prețuri într-o valută (de exemplu EUR), dar facturează în altă monedă: moneda jurnalului de vânzări sau, dacă jurnalul nu are monedă, moneda companiei (de exemplu RON). Prețurile se convertesc automat la cursul zilei, iar evidența contabilă reflectă valorile corecte în moneda facturii.

#### 2. Funcționalități Cheie

- **Moneda facturii după jurnal**: factura creată din comandă primește moneda jurnalului de vânzări al comenzii (sau moneda companiei, dacă jurnalul nu are monedă), în loc de moneda comenzii, cum face Odoo standard.
- **Conversia prețurilor la creare**: prețurile unitare din moneda listei de prețuri a comenzii se convertesc în moneda facturii, la cursul de la data creării facturii. Dacă moneda comenzii coincide cu cea a facturii, prețurile rămân neschimbate.
- **Reconversie la schimbarea datei sau a monedei facturii**: liniile provenite din comandă se recalculează pornind mereu de la prețul din comandă, la cursul noii date. Dacă unitatea de măsură a liniei de factură diferă de cea din comandă, prețul se aduce întâi în unitatea facturii.
- **Linii manuale neatinse**: liniile adăugate direct pe factură, fără legătură cu o comandă, nu se reconvertesc. Prețurile modificate manual pe liniile din comandă se pierd la o nouă schimbare a datei.
- **Avansuri**: suma avansului deja facturat (în lei, pe o comandă în valută) se reconvertește în moneda comenzii, la cursul de la data facturii de avans, astfel încât factura finală să deducă corect avansul.
- **Protecție la monede multiple**: dacă o linie de factură provine din linii de comandă în monede diferite, se afișează eroarea „You cannot have multiple currencies in the same invoice line.” Comenzile în monede diferite se facturează separat.
- **Configurare**: moneda facturii se decide din câmpul **Monedă** al jurnalului de vânzări (Contabilitate → Configurare → Jurnale); cursurile se încarcă din Contabilitate → Configurare → Monede. Dacă lipsește cursul pentru data facturii, conversia se face cu cursul 1. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): `_prepare_invoice` setează moneda facturii din jurnalul comenzii (sau din moneda companiei).
- `sale.order.line` (extins): `_prepare_invoice_line` convertește prețul unitar din moneda listei de prețuri în moneda facturii; `_get_downpayment_line_price_unit` reconvertește avansurile deja facturate în moneda comenzii.
- `account.move` (extins): `_onchange_invoice_date` (pe `invoice_date` și `currency_id`) recalculează prețurile liniilor provenite din comandă, la cursul datei facturii.

**Vizualizări**

- Nu sunt definite vizualizări (`data` este gol în manifest).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_purchase_currency](../deltatech_purchase_currency/index.md): modulul pereche pe achiziții. Pune un jurnal de facturare pe comanda de achiziție, iar factura furnizorului ia moneda jurnalului, cu prețurile convertite la cursul de la data facturii.
