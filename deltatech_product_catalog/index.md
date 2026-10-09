# Product Catalog (Catalog de produse)

- **Nume Tehnic:** `deltatech_product_catalog`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_catalog
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_catalog`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite tipărirea unui catalog PDF cu mai multe produse deodată. Catalogul se poate genera fie dintr-o selecție de produse, fie pentru o categorie de produse din website (inclusiv subcategoriile ei), fiind util pentru a pune rapid la dispoziția clienților o ofertă ilustrată, cu datele companiei în antet și subsol.

#### 2. Funcționalități Cheie

- Opțiune de tipărire a catalogului pentru unul sau mai multe produse, din meniul Tipărire al listei de produse (șabloane de produs).
- Catalog pe categorie de website: din categoriile de produse publice se tipărește catalogul tuturor produselor din categoria selectată și din subcategoriile acesteia.
- Fiecare produs apare ca o fișă (card) cu imagine, cod intern și denumire; dacă produsul are produse alternative, acestea sunt afișate sub fișă.
- Antetul și subsolul catalogului preiau datele companiei (nume, adresă, telefon, e-mail, website, cod fiscal, antet/subsol de raport).

#### 3. Dependențe

- `product`
- [deltatech_alternative](../deltatech_alternative/index.md)
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `report.deltatech_product_catalog.report_product_catalog`: model abstract de raport; primește ID-urile produselor (`product.template`) selectate.
- `report.deltatech_product_catalog.report_category_catalog`: model abstract de raport; primește categoriile publice și caută produsele cu `public_categ_ids child_of`.

**Vizualizări**

- `report_product_catalog`: șablon QWeb al catalogului de produse (carduri cu imagine, cod, denumire, alternative).
- `report_category_catalog`: șablon QWeb al catalogului pe categorie.
- `catalog_layout`: layout comun, cu antet și subsol din datele companiei.

**Acțiuni Automate / Acțiuni Server**

- `action_report_product_catalog`: raport PDF „Product Catalog” legat de `product.template`.
- `action_report_product_category_catalog`: raport PDF „Product Catalog” legat de `product.public.category`.

#### 5. Conexiuni

- [deltatech_alternative](../deltatech_alternative/index.md): sursa produselor alternative afișate în catalog (dependență).
