# Website Sale Category Selection (localizat la `deltatech_website_sale_category/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_category`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_sale_category
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_category`
- **Ultima Ingestie:** `2026-11-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un pas intermediar de navigare în magazinul online: atunci când un client dă click pe o categorie de produse care are subcategorii, în loc să vadă direct toate produsele, i se afișează mai întâi o pagină de selecție cu subcategoriile disponibile (sub formă de carduri, cu imagine și nume). Astfel, clienții găsesc mai ușor produsul căutat în cataloage cu structură ierarhică bogată, iar magazinul păstrează opțiunea de a vedea toate produsele dintr-o categorie dintr-un singur click ("Vezi toate produsele").

#### 2. Funcționalități Cheie

- Permite utilizatorilor să navigheze prin subcategorii înainte de a vedea produsele în magazinul online (e-commerce).
- Interceptează click-urile pe categorii în pagina de shop și afișează o pagină de selecție dacă respectiva categorie are categorii-copil (`child_id`); o subcategorie care are la rândul ei subcategorii deschide propria pagină de selecție, iar o categorie fără copii deschide direct lista standard de produse.
- Pagina de selecție are carduri cu imaginea și numele fiecărei subcategorii, butonul „View all products in <categorie>", săgeata înapoi către categoria părinte sau `/shop` și butonul de acasă către `/shop`.
- Butonul „Vezi toate produsele" (`all_products=True`) ocolește selecția și arată toate produsele categoriei și ale subcategoriilor sale.
- Pagina `/shop` fără categorie și căutarea din magazin nu sunt modificate.
- Configurare: în *Website > eCommerce > Products > eCommerce Categories* se organizează categoriile prin câmpul *Parent Category*; ordinea rândurilor (drag and drop) dă ordinea cardurilor, iar fiecare subcategorie are nevoie de o imagine. Meniul cere drepturile *Website › Editor and Designer* și *Sales › User*.
- Imaginea cardului vine din `tb_category_visual_soft`: cu `deltatech_website_category_icon` instalat (nu e dependență), se aplică opțiunea lui de ordine a pictogramelor (pictogramă SVG, imaginea categoriei, imaginea primului produs); altfel, imaginea categoriei sau nimic.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.public.category` (extins): metoda privată `tb_category_visual_soft`, care întoarce pictograma sau imaginea afișată pe cardul categoriei; folosește `tb_category_visual` din `deltatech_website_category_icon` dacă acesta e instalat, altfel imaginea `image_128` a categoriei. Aceeași metodă există și în `deltatech_website_shop_snippets`, deci fiecare modul funcționează și singur.

**Vizualizări**

- `category_selection` (`views/templates.xml`): șablon QWeb pentru pagina de selecție a subcategoriilor — afișează titlul categoriei curente, butoane de navigare (înapoi, acasă, „Vezi toate produsele din <categorie>") și un grid de carduri cu pictograma sau imaginea și numele fiecărei subcategorii, fiecare link-uind către `/shop/category/<subcategorie>`.

**Acțiuni Automate / Acțiuni Server**

- Nu are `ir.cron`, `base.automation` sau `ir.actions.server`.

**Controller**

- `WebsiteSaleCategory` (`controllers/main.py`): extinde controllerul `WebsiteSale` din `website_sale` și suprascrie metoda `shop()` pe rutele `/shop`, `/shop/page/<page>`, `/shop/category/<category>` și `/shop/category/<category>/page/<page>`. Dacă se accesează o categorie (fără căutare activă și fără parametrul `all_products`) care are categorii-copil, randează șablonul `category_selection` în loc să continue către listarea standard de produse; altfel deleagă către `website_sale` prin `super().shop()`.

#### 5. Conexiuni

- [deltatech_website_sale_attributes](../deltatech_website_sale_attributes/index.md): ambele module suprascriu metoda `shop()` a controllerului `WebsiteSale` din `website_sale`; ordinea de moștenire (MRO) a celor două extensii afectează comportamentul combinat al paginii de shop.
- [deltatech_website_category_icon](../deltatech_website_category_icon/index.md): dependență opțională — furnizează pictograma sau imaginea cardurilor de categorie prin `tb_category_visual`.
- [deltatech_website_shop_snippets](../deltatech_website_shop_snippets/index.md): definește aceeași metodă `tb_category_visual_soft`, astfel încât oricare dintre module poate funcționa singur.
- `website_sale`: modulul standard de e-commerce ale cărui rută `/shop` și pagini de categorie sunt interceptate și extinse de acest modul.
