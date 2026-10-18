# Website Sale Effects (localizat la `deltatech_website_sale_effects/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_effects`
- **Versiune:** `19.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_sale_effects
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_effects`
- **Ultima Ingestie:** `2026-10-18`

#### 1. Sumar

Aduce efectele din *Website Effects* pe paginile de eCommerce: magazinul, pagina de produs și finalizarea comenzii. Fiecare efect este o opțiune în editorul de website, lângă opțiunile pe care Odoo le are deja pentru aceste pagini. Nimic nu se schimbă până când o opțiune nu este activată, iar mișcarea se oprește pentru vizitatorii care au cerut sistemului lor animații reduse. Opțiunile se salvează per website.

#### 2. Funcționalități Cheie

**Magazin (Shop)**

- **Categories Card:** lista de categorii din bara laterală într-un card alb, cu titlu, rând „All Products” pentru revenire, categoria curentă ca pastilă în culoarea primară a temei, rânduri care se aprind la hover și chevroane pentru lista pliabilă. **Subcategory Count** (dezactivat implicit) afișează numărul de subcategorii. Cu `deltatech_website_category_icon` instalat, iconițele categoriilor apar pe tile-uri discrete.
- **Filters Card:** filtrele de atribute și de preț din bara laterală, într-un card în același stil.
- **Sidebar Corners:** un singur setting pentru colțurile ambelor carduri: Large (implicit), Medium, Small sau Square.
- **Animated Product Cards:** produsele devin carduri cu bordură și umbră, cu raza din *Products Design > Roundness*; butonul de adăugare în coș apare animat la hover.
- **Hover Effect** (în *Products Design*): 3D Tilt (cardul se înclină spre cursor, cu o lumină care urmărește mouse-ul), Lift, Glow și Holo; funcționează cu orice design de produse.
- **Small Decimals:** zecimalele prețului sunt mai mici și pe linia de bază, iar unitatea de măsură apare lângă preț (ex. *0.82 lei/buc*). Disponibil și pe pagina de produs.

**Pagina de produs**

- **Small Decimals:** ca în magazin; prețul urmează varianta și cantitatea alese.
- **Box Corners:** o singură rază pentru casetele coloanei de achiziție (caseta de preț din stilul *Boxed*, termenii și ruta de livrare): Theme, Small, Medium sau Large.
- **Terms and Conditions > Style: Boxed:** în loc de trei linii de text mărunt, blocul *Info List* cu titlu, rânduri cu iconițe și linkuri către politici; se editează o singură dată pentru toate produsele.
- **Delivery Route:** ruta animată din *Website Effects* sub termeni, editată o singură dată pentru toate produsele (texte, vehicul, viteză, culoare).
- **Bottom Tabs:** descrierea, specificațiile (*Specification: Bottom of Page*) și recenziile devin taburi într-un card; apar doar secțiunile prezente. Linkul de rating al produsului duce la tabul de recenzii. În modul de editare secțiunile rămân neschimbate.
- **Description under Image:** descrierea lungă se mută în coloana imaginilor, sub poze, în timp ce coloana de achiziție rămâne vizibilă; pe telefon vine după blocul de achiziție.

**Finalizare comandă (Checkout)**

- **Animated Steps:** bara de progres devine un drum punctat între pași numerotați; pe fiecare pagină un vehicul se deplasează de la pasul anterior la cel curent, iar drumul se umple cu culoarea temei. Pașii parcurși rămân clicabili. **Vehicle:** camion (implicit), coș de cumpărături, mașină, motocicletă, bicicletă, avion, vapor sau rachetă.
- **Box Corners** (Theme, Small, Medium, Large) rotunjește sumarul comenzii, adresele și metodele de livrare/plată. **Box Hover** (None, Lift, Glow, Frame) face adresele și metodele să reacționeze la mouse; cu una activă, metodele devin casete separate.

**Configurare:** opțiunile se activează din editorul de website (mod editare) pe `/shop`, pe o pagină de produs sau pe `/shop/cart`, din opțiunile paginii respective.

#### 3. Dependențe

- `website_sale`
- [deltatech_website_effects](../deltatech_website_effects/index.md)

#### 4. Componente Cheie

Modulul nu definește modele Python; este un modul de front-end (șabloane QWeb, SCSS, interacțiuni OWL/JS și opțiuni pentru website builder).

**Modele**

- Niciunul.

**Vizualizări**

- `products_filters_card`, `products_card_fx`, `sidebar_corners_md`, `sidebar_corners_sm` (`views/templates.xml`): cardurile din magazin, efectele cardurilor de produs și colțurile barei laterale.
- `products_price_split`, `product_price_split` (`views/price_split.xml`): Small Decimals în magazin și pe pagina de produs.
- `product_bottom_tabs` (`views/product_page.xml`): taburile de jos ale paginii de produs.
- `checkout_steps` (`views/checkout_steps.xml`): bara de pași animată.
- Interacțiuni JS: `price_split.esm.js`, `product_tabs.esm.js`, `shop_card_tilt.esm.js`; opțiuni de editor în `static/src/website_builder/`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_website_effects](../deltatech_website_effects/index.md): furnizează efectele (inclusiv ruta de livrare și blocul Info List) refolosite aici.
- [deltatech_website_category_icon](../deltatech_website_category_icon/index.md): legătură opțională; cu el instalat, iconițele categoriilor apar pe tile-uri în Categories Card.
