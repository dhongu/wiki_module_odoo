# Products Category (Categorii de produse pe companie)

- **Nume Tehnic:** `deltatech_product_category`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_category
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_category`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul permite ca fiecare categorie de produse să aparțină unei companii, util în bazele de date multi-companie în care firmele au structuri de categorii separate. Categoriile standard Odoo rămân comune tuturor companiilor, iar partajarea categoriilor între firme se poate activa sau dezactiva dintr-o setare.

#### 2. Funcționalități Cheie

- Categorie de produse per companie: câmpul „Company” pe formularul categoriei (vizibil doar în mod multi-companie), cu valoarea implicită compania curentă.
- Setarea „Share product category to all companies” (Setări > Companii, vizibilă în mod debug): bifată, categoriile sunt vizibile în toate companiile; debifată, se activează regula de acces multi-companie, iar fiecare companie vede doar categoriile proprii și pe cele fără companie.
- Categoriile standard („All”, „Goods”, „Expenses”, „Services”) rămân fără companie, deci comune; la salvarea setărilor li se șterge compania, dacă au primit una (inclusiv la bazele migrate din 18.0).
- Câmpul companie are valoare implicită compania curentă și pe șabloanele de produs.

#### 3. Dependențe

- `product`
- `base_setup`

#### 4. Componente Cheie

**Modele**

- `product.category` (extins): adaugă `company_id`.
- `product.template` (extins): `company_id` cu valoare implicită compania curentă.
- `res.config.settings` (extins): setarea `company_share_product_category`, care activează/dezactivează regula de acces și readuce categoriile standard fără companie.

**Vizualizări**

- `product_category_form_view`: adaugă câmpul „Company” după categoria părinte (grup multi-companie).
- `res_config_settings_view_form`: setarea de partajare în blocul Companii (grup `base.group_no_one`, mod debug).

**Acțiuni Automate / Acțiuni Server**

- `product_category_comp_rule` (`ir.rule`, globală, dezactivată implicit): domeniu `company_id` fals sau în `company_ids`; se activează când partajarea este debifată.

#### 5. Conexiuni

- [deltatech_product_category_color](../deltatech_product_category_color/index.md): extinde categoriile de produse cu culoare (legătură funcțională după temă, fără dependență în manifest).
- [deltatech_product_category_group](../deltatech_product_category_group/index.md): grupări de categorii de produse (legătură după temă, fără dependență în manifest).
