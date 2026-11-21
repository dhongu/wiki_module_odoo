# eCommerce Sale Short Description (localizat la `deltatech_website_short_description/index.md`)

- **Nume Tehnic:** `deltatech_website_short_description`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_short_description
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_short_description`
- **Ultima Ingestie:** `2026-11-21`

#### 1. Sumar

Feed-urile de produse și alte canale de vânzare au nevoie de un text scurt despre produs, pe lângă descrierea completă din website. Modulul adaugă pe produs o descriere scurtă traductibilă și două moduri de a publica produse pe website: un buton pe formularul produsului și o acțiune în masă din lista de produse.

#### 2. Funcționalități Cheie

- **Descriere scurtă:** fiecare produs primește câmpul *Website short description*, un editor HTML în pagina *Sales* a formularului de produs; textul este traductibil pe limbi.
- **Ambele texte împreună:** *Website description* a produsului este afișată alături, în același loc, deci cele două texte se editează împreună.
- **Buton de publicare:** butonul *Publish* din `button_box` al formularului de produs publică produsul pe website.
- **Publicare în masă:** acțiunea *Publish on Website* din lista de produse publică produsele selectate care nu sunt încă publicate și le lasă neschimbate pe celelalte.
- Modulul doar stochează descrierea scurtă și nu are grupuri de securitate proprii; alte module Terrabit, precum *Products Feed* (`deltatech_feed`), o citesc.

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpul `website_short_description` (HTML, traductibil) pentru descrierea scurtă folosită în feed-uri și metoda `action_website_publish`, care publică pe website produsele încă nepublicate.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs (`product.product_template_form_view`), adaugă butonul statistic „Publish" în `button_box` și, în pagina „Sales", grupurile „Website description" și „Website short description".

**Acțiuni Automate / Acțiuni Server**

- `action_website_publish_product_template`: acțiune server (`ir.actions.server`) legată de `product.template`, disponibilă ca acțiune contextuală în lista de produse, care apelează `action_website_publish()` pentru a publica pe website produsele selectate.

#### 5. Conexiuni

- [deltatech_feed](../deltatech_feed/index.md): citește câmpul `website_short_description` pentru descrierea scurtă din feed-urile de produse generate.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): folosește descrierea scurtă a produselor în contextul marketplace-ului.
