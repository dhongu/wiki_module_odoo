# Sale Invoice Currency (localizat la `deltatech_sale_currency/index.md`)

- **Nume Tehnic:** `deltatech_sale_currency`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_currency
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_currency`
- **Ultima Ingestie:** `2026-11-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite ca o comandă de vânzare să fie în altă monedă decât factura generată din ea. Este util companiilor care ofertează în valută (de exemplu EUR), dar facturează în lei: factura primește moneda jurnalului de vânzări, iar prețurile se convertesc automat din moneda comenzii în moneda facturii, la cursul valabil la data facturii.

#### 2. Funcționalități Cheie

- **Moneda facturii bazată pe jurnal**: factura creată din comandă primește moneda jurnalului de vânzări al comenzii sau, dacă jurnalul nu are monedă, moneda companiei; comportamentul standard Odoo (moneda comenzii) este înlocuit.
- **Conversie automată a prețurilor**: la crearea facturii, prețul unitar din moneda listei de prețuri a comenzii se convertește în moneda facturii, la cursul zilei. Liniile fără legătură cu o comandă nu sunt convertite.
- **Reconversie la schimbarea datei sau a monedei**: la modificarea **Datei facturii** sau a **Monedei**, prețul liniilor provenite din comandă se recalculează pornind de la prețul din comandă, la cursul noii date. Dacă unitatea de măsură a liniei de factură diferă de cea din comandă, prețul se convertește întâi în unitatea facturii (ex. 10 per Unitate devine 120 per Duzină), apoi în moneda facturii.
- **Avansuri**: suma deja facturată prin facturi de avans se reconvertește în moneda comenzii, la cursul de la data facturii de avans, ca la factura finală avansul să se deducă corect.
- **Protecție**: o linie de factură legată de linii de comandă în monede diferite generează o eroare („You cannot have multiple currencies in the same invoice line.”).
- Configurare: moneda se stabilește din câmpul **Monedă** al jurnalului de vânzări (**Contabilitate → Configurare → Jurnale**); cursurile se țin în **Contabilitate → Configurare → Monede**. Modulul nu adaugă grupuri de securitate.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

Modulul nu are `readme/USAGE.md`, iar DESCRIPTION.md nu detaliază componentele; ele sunt descrise după codul din `models/`. Nu definește modele noi, vizualizări sau acțiuni automate (`data` este gol în manifest).

**Modele**

- `sale.order` (extins): `_prepare_invoice` setează moneda facturii din jurnalul de vânzări (sau moneda companiei).
- `sale.order.line` (extins): `_prepare_invoice_line` convertește prețul unitar din moneda listei de prețuri în moneda jurnalului/companiei; `_get_downpayment_line_price_unit` reconvertește avansurile deja facturate în moneda comenzii.
- `account.move` (extins): `_onchange_invoice_date` reconvertește prețurile liniilor provenite din comandă la modificarea datei facturii sau a monedei, cu conversie prealabilă a unității de măsură.

**Vizualizări**

- Nu sunt definite vizualizări noi.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module documentate în wiki.
