# Sale Margin Report by Manufacturer

- **Nume Tehnic:** `deltatech_sale_commission_manufacturer`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_commission_manufacturer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_commission_manufacturer`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Adaugă producătorul produsului în raportul de marjă la vânzare (analiza profitului) din modulul Comenzi de vânzare cu comision. Utilizatorii pot căuta după producător și pot grupa datele după el, astfel încât vânzările, costul și profitul să poată fi citite pe fiecare producător.

#### 2. Funcționalități Cheie

- Filtru de căutare după producător în raportul de marjă la vânzare.
- Grupare nouă **Group By > Manufacturer** în același raport, pentru vânzări, cost și profit pe producător.
- Producătorul este cel setat pe produs (modulul Products Extension).
- Se instalează automat (`auto_install`) când ambele module dependente sunt prezente într-o bază nouă; într-o bază existentă se instalează din Apps.

#### 3. Dependențe

- [deltatech_sale_commission](../deltatech_sale_commission/index.md)
- [deltatech_product_extension](../deltatech_product_extension/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.margin.report` (extins): adaugă câmpul `manufacturer_id` (Many2one către `res.partner`, readonly) și îl include în interogările `_select`, `_sub_select` și `_group_by` ale vizualizării SQL.

**Vizualizări**

- `view_sale_margin_report_filter_manufacturer`: extinde vizualizarea de căutare a raportului cu câmpul Manufacturer și filtrul de grupare `group_manufacturer`.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_sale_commission](../deltatech_sale_commission/index.md): oferă raportul de marjă extins aici.
- [deltatech_product_extension](../deltatech_product_extension/index.md): oferă câmpul producător de pe produs.
