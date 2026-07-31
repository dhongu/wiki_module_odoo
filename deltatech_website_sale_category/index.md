# Terrabit Website Sale Category Selection (localizat la `deltatech_website_sale_category/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_category`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_sale_category](https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_sale_category)
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_category`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă un pas intermediar de navigare în magazinul online: atunci când un client dă click pe o categorie de produse care are subcategorii, în loc să vadă direct toate produsele, i se afișează mai întâi o pagină de selecție cu subcategoriile disponibile (sub formă de carduri, cu imagine și nume). Astfel, clienții găsesc mai ușor produsul căutat în cataloage cu structură ierarhică bogată, iar magazinul păstrează opțiunea de a vedea toate produsele dintr-o categorie dintr-un singur click ("Vezi toate produsele").

#### 2. Funcționalități Cheie

- Permite utilizatorilor să navigheze prin subcategorii înainte de a vedea produsele în magazinul online (e-commerce).
- Interceptează click-urile pe categorii în pagina de shop.
- Afișează o pagină de selecție a subcategoriilor dacă respectiva categorie are categorii-copil (`child_id`).
- Include o opțiune „Vezi toate produsele" (`all_products=True`) pentru a ocoli pasul de selecție a subcategoriei și a ajunge direct la listarea produselor.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

Modulul nu definește sau extinde modele Odoo; toată logica este implementată la nivel de controller HTTP.

**Vizualizări**

- `category_selection` (`views/templates.xml`): șablon QWeb pentru pagina de selecție a subcategoriilor — afișează titlul categoriei curente, butoane de navigare (înapoi, acasă, „Vezi toate produsele din <categorie>") și un grid de carduri cu imaginea și numele fiecărei subcategorii, fiecare link-uind către `/shop/category/<subcategorie>`.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

**Controller**

- `WebsiteSaleCategory` (`controllers/main.py`): extinde controllerul `WebsiteSale` din `website_sale` și suprascrie metoda `shop()` pe rutele `/shop`, `/shop/page/<page>`, `/shop/category/<category>` și `/shop/category/<category>/page/<page>`. Dacă se accesează o categorie (fără căutare activă și fără parametrul `all_products`) care are categorii-copil, randează șablonul `category_selection` în loc să continue către listarea standard de produse; altfel deleagă către implementarea standard din `website_sale` prin `super().shop()`.

#### 5. Conexiuni

- [deltatech_website_sale_attributes](../deltatech_website_sale_attributes/index.md): ambele module suprascriu metoda `shop()` a controllerului `WebsiteSale` din `website_sale`; ordinea de moștenire (MRO) a celor două extensii afectează comportamentul combinat al paginii de shop (una poate intercepta cererea înainte ca cealaltă să-și aplice filtrele pe atribute).
- `website_sale`: modulul standard de e-commerce ale cărui rută `/shop` și pagini de categorie sunt interceptate și extinse de acest modul.
