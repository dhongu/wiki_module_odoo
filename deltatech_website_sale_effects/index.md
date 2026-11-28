# Efecte pentru eCommerce (Website Sale Effects)

- **Nume Tehnic:** `deltatech_website_sale_effects`
- **Versiune:** `20.0.1.4.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_sale_effects
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_effects`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul aduce efectele din [deltatech_website_effects](../deltatech_website_effects/index.md) în paginile magazinului online: lista de produse, pagina de produs și checkout-ul. Fiecare efect este o opțiune în editorul de site, lângă opțiunile existente ale Odoo pentru aceste pagini. Nimic nu se schimbă până nu este activată o opțiune, iar mișcarea se oprește pentru vizitatorii care au cerut mișcare redusă.

#### 2. Funcționalități Cheie

- **Magazin**: *Categories Card* (lista de categorii din bară într-un card, cu *Subcategory Count* opțional), *Filters Card* pentru filtrele din bară, *Sidebar Corners* (Large, Medium, Small, Square), *Animated Product Cards* (carduri cu bordură și umbră, buton de coș care sare la hover) și *Hover Effect* în *Products Design* (3D Tilt, Lift, Glow, Holo).
- **Small Decimals**: zecimalele prețului mai mici, pe linia de bază, cu unitatea de măsură lângă preț (*0,82 lei/buc*); disponibil și pe pagina de produs, urmărind varianta și cantitatea.
- **Pagina de produs**: *Box Corners* pentru casetele coloanei de cumpărare, *Terms Box* (blocul *Info List* cu termenii de livrare, plată și retur, editat o dată pentru toate produsele), *Delivery Route* (ruta animată sub secțiunea de cumpărare), *Bottom Tabs* (descriere, specificații și recenzii în file într-un card) și *Description under Image* (descrierea lungă sub imagini).
- **Checkout**: *Animated Steps* (bara de progres devine un drum punctat cu pași numerotați, pe care un vehicul — camion, coș, mașină, motocicletă, bicicletă, avion, vapor sau rachetă — merge la pasul curent), *Box Corners* și *Box Hover* (None, Lift, Glow, Frame) pentru sumarul comenzii, adrese și metodele de livrare și plată.
- Opțiunile se activează din editorul de site, în modul de editare al paginilor `/shop`, produs și `/shop/cart`.

#### 3. Dependențe

- `website_sale`
- [deltatech_website_effects](../deltatech_website_effects/index.md)

#### 4. Componente Cheie

**Modele**

- Nu definește modele Python; lucrează prin interacțiuni JS (`price_split`, `product_tabs`, `shop_card_tilt`) și stiluri SCSS.

**Vizualizări**

- `checkout_steps.xml`, `price_split.xml`, `product_page.xml`, `templates.xml`: șabloanele QWeb pentru pași, prețuri, pagina de produs și carduri.
- Opțiunile de editor `products_list_page_option`, `products_design_panel`, `product_page_option`, `checkout_page_option`.

**Acțiuni Automate / Acțiuni Server**

- Nu are sarcini cron sau acțiuni server.

#### 5. Conexiuni

- [deltatech_website_effects](../deltatech_website_effects/index.md): sursa efectelor și a blocurilor *Info List* și *Delivery Route* folosite aici.
- `deltatech_website_category_icon`: dacă este instalat, iconițele categoriilor stau pe pavele discrete în *Categories Card*.
