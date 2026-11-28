# Website Sale Category Selection (localizat la `deltatech_website_sale_category/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_category`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_sale_category
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_category`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un pas intermediar de navigare în magazinul online: atunci când un client dă click pe o categorie de produse care are subcategorii, în loc să vadă direct toate produsele, i se afișează mai întâi o pagină de selecție cu subcategoriile disponibile (sub formă de carduri, cu imagine și nume). Astfel, clienții găsesc mai ușor produsul căutat în cataloage cu structură ierarhică bogată, iar magazinul păstrează opțiunea de a vedea toate produsele dintr-o categorie dintr-un singur click ("Vezi toate produsele").

#### 2. Funcționalități Cheie

- Permite utilizatorilor să navigheze prin subcategorii înainte de a vedea produsele în magazinul online (e-commerce).
- Interceptează click-urile pe categorii în pagina de shop.
- Afișează o pagină de selecție a subcategoriilor dacă respectiva categorie are categorii-copil (`child_id`).
- Sortarea, filtrele și paginile rămân pe lista „Vezi toate produsele” (nu readuc pagina de selecție); pe baze cu mai multe site-uri se afișează doar subcategoriile site-ului curent.
- Include o opțiune „Vezi toate produsele" (`all_products=True`) pentru a ocoli pasul de selecție a subcategoriei și a ajunge direct la listarea produselor.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.public.category` (extins): metoda `tb_category_visual_soft()` returnează pictograma sau imaginea afișată pe cardul categoriei; folosește `tb_category_visual` din [deltatech_website_category_icon](../deltatech_website_category_icon/index.md) dacă acel modul e instalat (nu e dependență), altfel imaginea categoriei sau nimic.

Restul logicii stă în controllerul HTTP.

**Vizualizări**

- `category_selection` (`views/templates.xml`): șablon QWeb pentru pagina de selecție a subcategoriilor — afișează titlul categoriei curente, butoane de navigare (înapoi, acasă, „Vezi toate produsele din <categorie>") și un grid de carduri cu imaginea și numele fiecărei subcategorii, fiecare link-uind către `/shop/category/<subcategorie>`.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

**Controller**

- `WebsiteSaleCategory` (`controllers/main.py`): extinde controllerul `WebsiteSale` din `website_sale` și suprascrie metoda `shop()` pe rutele `/shop`, `/shop/page/<page>`, `/shop/category/<category>` și `/shop/category/<category>/page/<page>`. Dacă se accesează pagina simplă a unei categorii (fără căutare, `all_products`, sortare, filtre de atribute/preț/etichete/promoții/stoc sau pagină de listă) care are subcategorii ale site-ului curent și URL-ul canonic, randează șablonul `category_selection` în loc să continue către listarea standard de produse; altfel deleagă către implementarea standard din `website_sale` prin `super().shop()`.

#### 5. Conexiuni

- [deltatech_website_sale_attributes](../deltatech_website_sale_attributes/index.md): ambele module suprascriu metoda `shop()` a controllerului `WebsiteSale` din `website_sale`; ordinea de moștenire (MRO) a celor două extensii afectează comportamentul combinat al paginii de shop (una poate intercepta cererea înainte ca cealaltă să-și aplice filtrele pe atribute).
- [deltatech_website_category_icon](../deltatech_website_category_icon/index.md): dacă e instalat, furnizează pictograma SVG a categoriei pe carduri (dependență opțională, neimpusă).
- `website_sale`: modulul standard de e-commerce ale cărui rută `/shop` și pagini de categorie sunt interceptate și extinse de acest modul.
