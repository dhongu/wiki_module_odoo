# eCommerce Sale Short Description (localizat la `deltatech_website_short_description/index.md`)

- **Nume Tehnic:** `deltatech_website_short_description`
- **Versiune:** `19.0.1.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_short_description`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_short_description`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul adaugă pe produsele din magazinul online un câmp dedicat de descriere scurtă, separat de descrierea completă afișată pe pagina produsului. Această descriere scurtă este folosită în special în feed-urile de produse (de exemplu cele trimise către platforme externe sau marketplace-uri), unde este nevoie de un text concis. În plus, modulul oferă o cale rapidă de a publica produse pe website direct din lista de produse, fără a deschide fiecare produs în parte.

#### 2. Funcționalități Cheie

- Câmp nou `website_short_description` pe produse, destinat unei descrieri scurte utilizate în feed-uri.
- Buton / acțiune de publicare a produselor pe website, disponibil direct din lista de produse pentru mai multe produse simultan.

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.template`: este extins cu câmpul `website_short_description` (HTML, traductibil) pentru descrierea scurtă folosită în feed-uri și cu metoda `action_website_publish`, care publică pe website produsele încă nepublicate.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs (`product.product_template_form_view`) și adaugă, în pagina „Sales", grupurile „Website description" și „Website short description".

**Acțiuni Automate / Acțiuni Server**

- `action_website_publish_product_template`: acțiune server (`ir.actions.server`) legată de `product.template`, disponibilă ca acțiune contextuală în vizualizarea de tip listă, care apelează `action_website_publish()` pentru a publica pe website produsele selectate.

#### 5. Conexiuni

- [deltatech_feed](../deltatech_feed/index.md): consumă câmpul `website_short_description` pentru a popula descrierea scurtă în feed-urile de produse generate.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): dependență funcțională care folosește descrierea scurtă a produselor în contextul marketplace-ului.
