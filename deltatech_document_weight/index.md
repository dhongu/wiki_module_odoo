# Document Weight (localizat la `deltatech_document_weight/index.md`)

- **Nume Tehnic:** `deltatech_document_weight`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_document_weight
- **Cale Locală:** `odoo-addons/deltatech/deltatech_document_weight`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Tipărește greutatea netă, greutatea brută și volumul mărfii pe oferta de preț și pe factura către client: sub numele fiecărui produs și, în total, sub sume. Valorile sunt estimări, utile de exemplu pentru calculul transportului înainte de tipărire.

#### 2. Funcționalități Cheie

- Valorile se calculează din cantitatea liniei, convertită în unitatea de măsură a produsului, înmulțită cu greutatea și volumul produsului.
- Coloană opțională **Greutate brută** pe liniile ofertei, comenzii de vânzare și facturii client.
- Opțiuni per companie în **Vânzări ‣ Configurare ‣ Setări**, secțiunea *Weights on documents*: greutăți pe oferte (implicit activ), greutăți pe facturi (implicit inactiv), doar greutatea brută (fără net și volum) și copierea greutăților pe toate variantele produsului (inclusiv variantele create la cerere).
- Liniile al căror produs nu are greutate și volum nu tipăresc nimic; blocul de totaluri este omis când toate totalurile sunt 0.
- Greutatea netă este câmpul `l10n_ro_net_weight` al produsului, declarat identic cu `l10n_ro_stock` și `l10n_ro_stock_base`: modulul funcționează cu sau fără ele, iar câmpul apare o singură dată pe formular.
- Nu modifică `deltatech_invoice_weight`, care stochează totalurile pe document.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `deltatech.document.weight.mixin`: mixin abstract care calculează greutățile și volumul totale.
- `sale.order`, `account.move`: extinse cu mixinul; `sale.order.line`, `account.move.line`: greutatea brută estimată pe linie.
- `product.template`, `product.product`: greutatea netă și copierea pe variante.
- `res.company`, `res.config.settings`: opțiunile de tipărire.

**Vizualizări**

- `view_order_form_document_weight`, `view_move_form_document_weight`: coloana opțională pe linii.
- `product_template_form_view_document_weight`: greutatea netă pe produs.
- `res_config_settings_view_form_document_weight`: opțiunile din setări.
- `report_saleorder_document`, `report_invoice_document`: moștenesc rapoartele de ofertă și de factură.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_invoice_weight](../deltatech_invoice_weight/index.md): stochează totalurile pe document; acest modul doar le tipărește.
- [deltatech_product_dimension](../deltatech_product_dimension/index.md): dimensiunile produsului.
