# Extensie Produse (localizat la `deltatech_product_extension/index.md`)

- **Nume Tehnic:** `deltatech_product_extension`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_extension
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_extension`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde produsul standard cu câmpuri tehnice și logistice: producătorul, termenul de valabilitate și dimensiunile. Este util companiilor care urmăresc în detaliu atributele produselor, gestionează stoc perisabil sau vor să organizeze partenerii după calitatea de producător.

#### 2. Funcționalități Cheie

- **Termen de valabilitate**: câmpurile *Termen de valabilitate* și *Unitate de măsură pentru termenul de valabilitate* pe șablonul de produs, în fila *Informații generale*, lângă cost.
- **Producător**: legătură către partener direct pe fișa produsului, sub categoria produsului; se pot alege doar partenerii marcați ca producători.
- **Dimensiuni**: câmp text liber (de exemplu „120 x 60 x 75 cm”), util pentru documente și cataloage. Nu calculează volumul; pentru lungime, lățime și înălțime numerice se folosește [deltatech_product_dimension](../deltatech_product_dimension/index.md).
- **Partener**: bifa *Producător* pe partener, pentru filtrare mai bună în Contacte.
- **Analiza facturilor**: producătorul produsului este disponibil în raportul de analiză a facturilor, ca filtru și criteriu de grupare.

#### 3. Dependențe

- `product`
- `account`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): `manufacturer_id`, `dimensions`, `shelf_life`, `uom_shelf_life`.
- `res.partner` (extins): `is_manufacturer`.
- `account.invoice.report` (extins): `manufacturer_id`, pentru analiză.

**Vizualizări**

- `views/product_view.xml`, `views/res_partner_view.xml`, `views/account_invoice_report_view.xml`: câmpurile noi pe produs, partener și în analiza facturilor.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_product_dimension](../deltatech_product_dimension/index.md): dimensiuni numerice și volum calculat, complementar câmpului text *Dimensiuni*.
