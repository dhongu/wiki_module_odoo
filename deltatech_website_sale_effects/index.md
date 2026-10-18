# Website Sale Effects

- **Nume Tehnic:** `deltatech_website_sale_effects`
- **Versiune:** `19.0.1.4.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_sale_effects
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_effects`
- **Ultima Ingestie:** `2026-10-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Aduce efectele din *Website Effects* în paginile de eCommerce: magazinul, pagina de produs și checkout-ul. Fiecare efect este o opțiune în editorul de website, lângă opțiunile pe care Odoo le are deja pentru aceste pagini. Nimic nu se schimbă până nu activați o opțiune, iar mișcarea se oprește pentru vizitatorii care au cerut sistemului lor mișcare redusă. Opțiunile se rețin per website.

#### 2. Funcționalități Cheie

**Magazin (`/shop`)**

- **Categories Card**: lista de categorii din bara laterală într-un card alb, cu titlu, rândul *All Products* pentru revenire, categoria curentă ca „pastilă” în culoarea primară a temei, rânduri care se luminează la hover și chevroane pentru lista pliabilă. **Subcategory Count** (dezactivat implicit) afișează numărul de subcategorii. Cu `deltatech_website_category_icon` instalat, iconițele categoriilor apar pe pătrate discrete.
- **Filters Card**: filtrele de atribute și de preț într-un card cu același stil, ca listă luminoasă, fără chenar în jurul fiecărui filtru.
- **Sidebar Corners**: o singură setare pentru colțurile ambelor carduri: Large (implicit), Medium, Small sau Square.
- **Animated Product Cards**: dalele de produs devin carduri cu bordură și umbră fină, cu raza din *Products Design > Roundness*; butonul de adăugare în coș apare animat la hover.
- **Hover Effect** în *Products Design*: **3D Tilt** (cardul se înclină spre cursor, cu o lumină care urmărește mouse-ul), **Lift**, **Glow** și **Holo**; funcționează cu orice design de produse.
- **Small Decimals**: zecimalele prețului sunt mai mici, pe linia de bază, iar unitatea de măsură apare lângă preț (ex. *0.82 lei/buc*). Disponibil și pe pagina de produs.

**Pagina de produs**

- **Small Decimals**: ca în magazin; prețul urmărește varianta și cantitatea aleasă.
- **Box Corners**: o singură rază pentru casetele coloanei de achiziție (Theme, Small, Medium, Large); caseta de preț preia lățimea coloanei când e însoțită de termeni sau de traseu în casetă.
- **Terms and Conditions > Style: Boxed**: în locul celor trei rânduri mici de text (termeni, garanție de returnare, timp de livrare), blocul *Info List* cu titlu, rânduri cu pictograme și linkuri către politici; se editează o singură dată, pentru toate produsele.
- **Delivery Route**: traseul animat din *Website Effects* sub termeni, editat o singură dată pentru toate produsele (texte, vehicul, viteză, culoare).
- **Bottom Tabs**: descrierea, specificațiile (*Specification: Bottom of Page*) și recenziile devin taburi într-un card; primesc tab doar secțiunile prezente. Link-ul de rating al produsului duce la tabul de recenzii. În modul de editare secțiunile rămân neschimbate.
- **Description under Image**: descrierea lungă se mută în coloana de imagini, iar coloana de achiziție rămâne în vedere; pe telefon vine după blocul de achiziție.

**Checkout**

- **Animated Steps**: bara de progres devine un drum punctat între pași numerotați; pe fiecare pagină un vehicul conduce de la pasul anterior la cel curent, iar drumul se umple cu culoarea temei. Pașii parcurși rămân clicabili. **Vehicle**: camion (implicit), coș de cumpărături, mașină, motocicletă, bicicletă, avion, vapor sau rachetă.
- **Box Corners** (Theme, Small, Medium, Large) rotunjește sumarul comenzii, adresele și metodele de livrare și plată. **Box Hover** (None, Lift, Glow, Frame) face adresele și metodele să reacționeze la mouse; cu una activă, metodele devin casete separate, nu listă unită.

Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `website_sale`
- [deltatech_website_effects](../deltatech_website_effects/index.md)

#### 4. Componente Cheie

**Modele**

- Modulul nu definește modele Python; lucrează prin șabloane QWeb, opțiuni de website builder, interacțiuni JS și SCSS.

**Vizualizări**

- `views/templates.xml`: carduri de categorii/filtre și carduri de produs animate în magazin.
- `views/checkout_steps.xml`: bara de pași animați din checkout.
- `views/product_page.xml`: casete, taburi inferioare și mutarea descrierii pe pagina de produs.
- `views/price_split.xml`: afișarea zecimalelor mici și a unității de măsură.
- `static/src/website_builder/`: panourile de opțiuni din editor (`products_design_panel.xml`, `product_page_option.xml`, `checkout_page_option.xml`).
- `static/src/interactions/`: `shop_card_tilt.esm.js`, `product_tabs.esm.js`, `price_split.esm.js`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_website_effects](../deltatech_website_effects/index.md): oferă efectele de bază (inclusiv traseul animat de livrare) reutilizate aici.
- [deltatech_website_category_icon](../deltatech_website_category_icon/index.md): iconițele categoriilor sunt afișate pe pătrate discrete în cardul de categorii.
