# eCommerce Qty Multiple (localizat la `deltatech_sale_multiple_website/index.md`)

- **Nume Tehnic:** `deltatech_sale_multiple_website`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_multiple_website`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_multiple_website`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul extinde regulile de cantitate minimă și cantitate multiplu de vânzare (definite de modulul `deltatech_sale_multiple`) și pe canalul eCommerce. Restricțiile pot fi aplicate doar în coșul de pe website sau global, iar valorile active (minim și multiplu) sunt afișate direct pe pagina produsului și în coșul de cumpărături, astfel încât clientul își dă seama imediat ce cantități poate comanda. Cantitatea din coș este normalizată înainte ca Odoo să verifice stocul disponibil; dacă stocul limitează cantitatea cerută, coșul revine automat la cea mai mare cantitate posibilă care respectă în continuare regulile de minim și multiplu.

#### 2. Funcționalități Cheie

- Aplicarea regulilor de cantitate minimă/multiplu doar pentru comenzile de pe website (opțiune `check_min_website` per produs) sau global.
- Afișarea pe pagina produsului a restricțiilor active (cantitate minimă, multiplu de vânzare) cu explicații tip popover.
- Afișarea acelorași restricții pe linia produsului din coșul de cumpărături.
- Actualizarea dinamică a restricțiilor afișate la schimbarea variantei de produs (fără reîncărcarea paginii).
- Normalizarea cantității din coș conform regulilor înainte de verificarea stocului disponibil.
- Recalcularea cantității la cea mai mare valoare validă (respectând minimul/multiplul) atunci când stocul limitează cantitatea cerută.

#### 3. Dependențe

- [deltatech_sale_multiple](../deltatech_sale_multiple/index.md)
- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.template`: adaugă câmpul `check_min_website` (aplică regulile de cantitate doar pe website) și extinde `_get_additionnal_combination_info` pentru a transmite în frontend minimul, multiplul și precizia de cantitate ale variantei curente.
- `product.product`: extinde `_should_enforce_sale_quantity_rules` pentru a dezactiva verificarea regulilor în afara contextului website atunci când `check_min_website` este activ.
- `sale.order`: extinde `_verify_updated_quantity` pentru a normaliza cantitatea conform regulilor înainte de verificările standard (ex. stoc) și pentru a o recapa la cea mai mare valoare validă dacă a fost limitată ulterior.
- `sale.order.line`: extinde `_prepare_quantity_rule_values` pentru a injecta contextul `website_id` al comenzii atunci când regulile de cantitate sunt evaluate pentru o comandă provenită din website.

**Vizualizări**

- `views/templates.xml` — `product_qty_restrictions`: extinde `website_sale.cta_wrapper` pentru a afișa pe pagina produsului cantitatea minimă și multiplul de vânzare, cu popover informativ.
- `views/templates.xml` — `cart_line_description_following_lines`: extinde `website_sale.cart_line_description_following_lines` pentru a afișa restricțiile de cantitate pe linia produsului din coș.
- `views/product_view.xml` — `product_template_form_view` / `product_variant_easy_edit_view`: adaugă câmpul `check_min_website` pe formularul de produs (șablon și variantă), lângă câmpul `qty_minim`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate (`ir.cron`), reguli `base.automation` sau acțiuni server (`ir.actions.server`) în acest modul.

#### 5. Conexiuni

- [deltatech_sale_multiple](../deltatech_sale_multiple/index.md): modulul de bază care definește cantitatea minimă și cantitatea multiplu de vânzare la nivel de produs; acest modul extinde regulile respective pe eCommerce.
- `website_sale_stock`: modulul standard Odoo care leagă disponibilitatea stocului de vânzarea pe website; acest modul se integrează cu el pentru a recapa cantitatea din coș atunci când stocul limitează cererea.
