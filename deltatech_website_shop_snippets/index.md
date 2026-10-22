# Website Shop Blocks (localizat la `deltatech_website_shop_snippets/index.md`)

- **Nume Tehnic:** `deltatech_website_shop_snippets`
- **Versiune:** `19.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_shop_snippets
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_shop_snippets`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Adaugă blocuri pentru editorul de website și variante de pagini pentru magazinele online cu catalog mare, navigat pe categorii: meniu de categorii (mega menu) generat automat, blocuri de prezentare a produselor și categoriilor, card uniform de produs, filtre de produse, bannere de categorie, precum și elemente pentru pagina de produs (coduri, livrare estimată, beneficii). Variantele paginii de magazin nu sunt active după instalare; se aleg din editor.

#### 2. Funcționalități Cheie

- **Meniu de categorii (mega menu):** un element de meniu cu *Mega Menu Source* = *Shop categories (automatic)* (*Website > Configuration > Menus*) afișează categoriile eCommerce: categorii principale în stânga, panou cu subcategorii (imagine, număr de produse), accordion pe telefon. Se construiește o dată din arbore și se ține în cache pe website și limbă; cache-ul se golește la modificarea unei categorii sau a publicării unui produs. Doar categoriile cu produse publicate; opțiunea *Hide in Category Menu* exclude o categorie.
- **Blocuri în editor:**
  - *Category Browser* (Catalog): secțiune pe trei coloane (meniu de categorii, banner, casetă de autentificare / *My account*).
  - *Product Tabs* (Catalog): blocul standard *Products* cu taburi (*New arrivals*, *Best sellers*, *Big discounts*), cu opțiuni per tab (filtru, insigne de rang, pagină *See All*).
  - *Categories Showcase Cards* (Catalog): carduri colorate de categorii cu număr de produse, subcategorii și imagini de produse; opțiuni *Card Colors*, *Corners*, *Shadow*, *Hover Animation*.
  - *Benefits Strip* (Columns): livrare, verificare colet, retur, plată.
  - *Recently Viewed* (Catalog): produsele văzute recent, cu carduri compacte.
  - *Deal of the Day*: produs cu preț vechi/nou, reducere și numărătoare inversă până la miezul nopții (implicit produsul cu cea mai mare reducere).
- **Card uniform de produs:** insigne (reducere, *New*, rang), buton wishlist, imagine pătrată, referință internă, stoc, preț vechi tăiat, buton *Add to Cart*; disponibil și pentru caruselele standard.
- **Filtre de produse:** *Best Sellers (last 90 days)* (după cantitate, comenzi confirmate) și *On Sale (comparison price)* (cea mai mare reducere prima).
- **Pagina de magazin:** *Category Banner* (titlu ca banner cu număr de produse/subcategorii), *Categories on top, Cards*, listă laterală cu subcategorii și casetă de filtrare fără diacritice la peste cinci subcategorii.
- **Pagina de produs:** *Product Code Chips* (cod intern, cod echivalent copiabil, brand, rating), *Estimated Delivery* (interval de zile lucrătoare, oră limită și pagină de condiții setate în *Website > Configuration > Settings*), *Product Benefits*.
- **Picture Pedestal** (setare, implicit dezactivată): postament discret pentru imaginile de produs decupate pe fundal transparent, util pe teme închise.

#### 3. Dependențe

- `website_sale`
- `website_sale_wishlist`
- [deltatech_website_effects](../deltatech_website_effects/index.md)

#### 4. Componente Cheie

**Modele**

- `product.public.category`: opțiunea de ascundere din meniul de categorii și numărătoarea produselor.
- `product.template`: câmpuri/metode pentru card și pagina de produs (reducere, noutate, livrare estimată).
- `website`: extinderi pentru construirea și cache-ul meniului de categorii.
- `website.menu`: sursa *Shop categories (automatic)* pentru mega menu.
- `website.snippet.filter`: filtrele de produse *Best Sellers* și *On Sale*.
- `res.config.settings`: setările de livrare estimată, *Picture Pedestal*.

**Vizualizări**

- `views/snippets/*.xml`: șabloanele blocurilor (product tabs, category showcase, deal of the day, benefit strip, card de produs) și înregistrarea lor în `snippets.xml`.
- `views/category_browser.xml`: blocul *Category Browser* și meniul de categorii.
- `views/shop.xml`, `views/product.xml`: variantele paginii de magazin și elementele paginii de produs.
- `views/res_config_settings_views.xml`: setările din *Website > Configuration > Settings*.

**Acțiuni Automate / Acțiuni Server**

- `dynamic_snippet_best_sellers_action` și `dynamic_snippet_on_sale_action` (`ir.actions.server`, în `data/snippet_filters.xml`): alimentează filtrele dinamice *Best Sellers* și *On Sale*.

#### 5. Conexiuni

- [deltatech_alternative](../deltatech_alternative/index.md): *Alternative Code* este afișat ca cod echivalent pe pagina de produs, dacă e instalat.
- [deltatech_image_optimize](../deltatech_image_optimize/index.md): decupează imaginile pe fundal transparent, pentru *Picture Pedestal*.
- [deltatech_website_shop_header](../deltatech_website_shop_header/index.md): antetul *Shop* afișează meniul de categorii ca buton.
