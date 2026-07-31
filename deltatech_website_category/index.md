# eCommerce Product Category (localizat la `deltatech_website_category/index.md`)

- **Nume Tehnic:** `deltatech_website_category`
- **Versiune:** `19.0.1.1.1`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_category](https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_category)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_category`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul îmbunătățește administrarea categoriilor publice de produse din magazinul online (eCommerce): permite arhivarea categoriilor în loc de ștergerea lor definitivă, păstrând astfel o navigare curată pe site fără a pierde datele istorice, și optimizează performanța paginii de magazin prin încărcarea „leneșă" (lazy) a arborelui de categorii din bara laterală — un beneficiu important pentru cataloage cu multe categorii, unde timpul de încărcare al paginii poate scădea semnificativ.

#### 2. Funcționalități Cheie

- Oferă posibilitatea de a arhiva categorii publice de produse, fără a le șterge definitiv.
- Menține o navigare mai curată pe site, eliminând din meniu categoriile depășite sau temporare.
- Permite restaurarea ușoară a categoriilor arhivate, dacă sunt din nou necesare.
- Categoriile arhivate nu mai apar în meniul magazinului și nici ca opțiuni de filtrare pe pagina de listare a produselor.
- Adaugă un câmp `website_url` calculat pe categorie, cu adresa completă către pagina categoriei pe site.
- **Arbore de categorii cu încărcare leneșă (lazy) în bara laterală a magazinului**: ramurile colapsate ale arborelui de categorii nu mai sunt randate integral pe server, ci sunt încărcate abia când vizitatorul le extinde, printr-o rută dedicată (`/shop/category_children/<id>`). Măsurat pe un catalog cu 1222 de categorii publice, timpul de răspuns al paginii de listare a scăzut de la 0,82s la 0,23s, iar volumul de HTML transferat de la 2,22 MB la 1,20 MB, fără nicio schimbare vizuală pentru vizitator. *(Notă: această funcționalitate majoră de performanță nu este menționată în `readme/DESCRIPTION.md` al modulului — descrierea readme acoperă doar arhivarea categoriilor; am completat Sumarul și lista de funcționalități cu ea pe baza codului și a `readme/HISTORY.md`, pentru ca pagina wiki să reflecte realitatea codului din 19.0.)*

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.public.category` (extindere): adaugă câmpul `active` (boolean, implicit `True`) pentru arhivare/dezarhivare fără ștergere, și câmpul calculat `website_url` (dependent de limbă) cu adresa completă către pagina categoriei pe site (`{SHOP_PATH}/category/<slug>`).

**Vizualizări**

- `categorie_link` (`views/shop_template.xml`, extinde `website_sale.categorie_link`): adaugă un handler `onclick` pe link-ul categoriei, pentru navigare compatibilă cu link-urile construite dinamic de arborele lazy.
- `lazy_collapse_categories_recursive` (`views/shop_template.xml`, extinde `website_sale.option_collapse_categories_recursive`): randează complet doar ramura deschisă a arborelui de categorii; ramurile colapsate primesc o listă `<ul>` goală, marcată cu `data-lazy-category`, care este umplută la cerere. Cât timp o căutare e activă, arborele (deja filtrat) rămâne randat integral.
- `lazy_categories_children` (`views/shop_template.xml`): fragment QWeb randat de ruta `/shop/category_children/<id>`, cu categoriile-copil ale ramurii cerute, identic cu ce ar fi randat bara laterală standard.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

**Controller**

- `WebsiteSaleCategory` (`controllers/main.py`): expune ruta `GET /shop/category_children/<int:category_id>`, care întoarce HTML-ul cu categoriile-copil direct ale unei ramuri colapsate din bara laterală, la prima extindere a acesteia de către vizitator. Filtrează categoriile inaccesibile pe website-ul curent și, pentru utilizatori neinterni, pe cele fără produse publicate; păstrează parametrii de filtrare (căutare, sortare, preț, tag-uri, atribute) în link-urile generate, pentru a nu pierde starea de filtrare a paginii.

**Frontend (assets)**

- `DeltatechLazyCategories` (`static/src/interactions/lazy_categories.esm.js`, interacțiune OWL înregistrată în `public.interactions`): ascultă evenimentul Bootstrap `show.bs.collapse` pe containerul listei de categorii și, la prima extindere a unei ramuri colapsate, apelează `/shop/category_children/<id>` și injectează HTML-ul primit, păstrând filtrele curente ale paginii (sortare, preț, categorie activă).

#### 5. Conexiuni

- [deltatech_website_sale_category](../deltatech_website_sale_category/index.md): ambele module acționează asupra navigării pe categorii în paginile `/shop` ale magazinului online — acesta gestionează arborele de categorii din bara laterală (arhivare, `website_url`, încărcare lazy), în timp ce `deltatech_website_sale_category` intercepte click-urile pe categorii pentru a afișa mai întâi o pagină de selecție a subcategoriilor.
- `website_sale`: modulul standard de e-commerce ale cărui șabloane `categorie_link` și `option_collapse_categories_recursive` (bara laterală de categorii) sunt extinse de acest modul.
