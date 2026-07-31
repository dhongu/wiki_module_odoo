# Products Feed (localizat la `deltatech_feed/index.md`)

- **Nume Tehnic:** `deltatech_feed`
- **Versiune:** `19.0.3.3.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_feed
- **Cale Locală:** `odoo-addons/bitshop/deltatech_feed`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul Products Feed este o extensie Odoo dezvoltată de Terrabit/Deltatech care permite generarea și administrarea de feed-uri de produse pentru diverse platforme de e-commerce și canale de marketing. Modulul simplifică procesul de creare a exporturilor standardizate de date despre produse, în conformitate cu cerințele mai multor marketplace-uri online și platforme de publicitate. Servește ca punte între catalogul de produse din Odoo și platformele externe de vânzare și promovare, permițând companiilor să gestioneze datele de produs într-un singur loc și să le distribuie eficient pe mai multe canale.

#### 2. Funcționalități Cheie

- **Generarea de feed-uri multi-platformă**: creează feed-uri standardizate de produse pentru mai multe platforme, printre care Google Merchant Center, Facebook Catalog, Bizoo, Compari, 2performant și VidaXL.
- **Formate de feed personalizabile**: suportă diferite formate și specificații cerute de fiecare platformă în parte.
- **Optimizarea datelor de produs**: asigură formatarea și optimizarea corectă a datelor de produs pentru fiecare platformă țintă.
- **Generare automată a feed-urilor**: simplifică crearea și actualizarea periodică a feed-urilor.
- **Administrarea listelor de produse**: instrumente pentru organizarea și gruparea produselor pe liste destinate diferitelor exporturi de feed.
- **Integrare cu website-ul**: integrare cu funcționalitatea de website și e-commerce din Odoo.

#### 3. Dependențe

- `product`
- `website_sale_stock`
- `deltatech_brand_field`
- `deltatech_product_list`
- `deltatech_website_short_description`

#### 4. Componente Cheie

Conform secțiunii „Technical Implementation" din readme, modulul este structurat în jurul următoarelor componente.

**Modele**

- `product.template` / `product.product`: extinse cu atribute și metode specifice feed-urilor.
- `product.list`: administrarea listelor de produse folosite la generarea feed-urilor; modelul găzduiește și metoda de reîmprospătare programată (`_cron_refresh_feed`).
- `website`: componente pentru configurarea și integrarea cu website-ul.

**Vizualizări**

- `views/feed_google.xml`, `views/feed_google_index.xml`: șabloane de feed pentru Google Merchant Center.
- `views/feed_emag.xml`, `views/feed_compari.xml`, `views/feed_e_licitatie.xml`: șabloane de feed pentru alte platforme și marketplace-uri.
- `views/website_product_templates.xml`: șabloane web pentru livrarea feed-ului.
- `views/product_view.xml`, `views/product_list_view.xml`: interfețe pentru gestionarea produselor și a listelor de produse.

**Controllere**

- `controllers/main.py`: controllere web pentru generarea și livrarea feed-urilor.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_regenerate_feed` („Feed: refresh"): sarcină `ir.cron` care rulează zilnic (interval 1 zi) și apelează `model._cron_refresh_feed()` pe modelul `product.list` pentru a reîmprospăta feed-urile.

#### 5. Conexiuni

- `deltatech_product_list`: furnizează modelul de liste de produse pe care se bazează gruparea produselor pentru feed-uri.
- `deltatech_brand_field`: oferă câmpul de brand/producător folosit în datele exportate către platforme.
- `deltatech_website_short_description`: pune la dispoziție descrierea scurtă utilizată în feed-uri.
- `website_sale_stock`: aduce datele de stoc din e-commerce, valorificate la generarea feed-urilor.
