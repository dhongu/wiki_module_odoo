# eCommerce Product Price Without Tax (localizat la `deltatech_website_price_without_tax/index.md`)

- **Nume Tehnic:** `deltatech_website_price_without_tax`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_price_without_tax`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_price_without_tax`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul extinde magazinul online Odoo (eCommerce) pentru a pune la dispoziție prețul produselor fără taxe (fără TVA) în paginile site-ului. Este util în special pentru magazinele orientate către clienți de tip business (B2B), unde prețurile relevante sunt cele fără TVA. Modulul calculează automat prețul fără taxe pentru fiecare variantă afișată și permite expunerea acestuia în interfața magazinului.

#### 2. Funcționalități Cheie

- Afișarea prețului produsului fără taxe (fără TVA) în paginile magazinului online.
- Calcul automat al prețului fără taxe pe baza taxelor configurate pe produs, integrat în informațiile de combinație ale variantei.
- Afișarea opțională a prețului unitar de bază fără taxe lângă prețul unitar standard.

#### 3. Dependențe

- `website`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.template`: extins prin suprascrierea metodei `_get_combination_info` pentru a adăuga prețul fără taxe (`list_price_without_tax`) în informațiile de combinație ale produsului afișat în magazin.

**Vizualizări**

- `base_unit_price_without_tax`: șablon QWeb care moștenește `website_sale.base_unit_price` pentru a afișa „Base Unit Price without tax" în pagina produsului (afișare opțională, `customize_show`).

#### 5. Conexiuni

- `website_sale`: modulul standard de eCommerce al cărui flux de afișare a prețurilor este extins pentru a include valoarea fără taxe.
