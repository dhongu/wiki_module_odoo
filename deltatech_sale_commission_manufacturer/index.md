# Sale Margin Report by Manufacturer (localizat la `deltatech_sale_commission_manufacturer/index.md`)

- **Nume Tehnic:** `deltatech_sale_commission_manufacturer`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_commission_manufacturer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_commission_manufacturer`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaugă producătorul produsului în raportul de marjă (analiză profit) din Sale Commission. Vânzările, costul și profitul pot fi citite astfel pe fiecare producător.

#### 2. Funcționalități Cheie

- Căutare după producător în raportul de marjă.
- Grupare după **Producător** (**Group By > Manufacturer**).
- Producătorul este cel setat pe produs (modulul Products Extension).
- Se instalează automat când Sale Commission și Products Extension sunt instalate pe o bază nouă; pe o bază existentă se instalează din Aplicații.

#### 3. Dependențe

- [deltatech_sale_commission](../deltatech_sale_commission/index.md)
- [deltatech_product_extension](../deltatech_product_extension/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.margin.report`: extins cu câmpul producător, preluat de pe produs.

**Vizualizări**

- `view_sale_margin_report_filter_manufacturer`: filtrul de căutare și gruparea după producător în raport.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): raportul de marjă este extins prin Sale Commission.
