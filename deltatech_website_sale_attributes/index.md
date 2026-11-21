# eCommerce Attribute Values (localizat la `deltatech_website_sale_attributes/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_attributes`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_attributes
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_attributes`
- **Ultima Ingestie:** `2026-11-21`

#### 1. Sumar

Modulul ascunde din magazinul online valorile de atribut alese, păstrându-le pe produse în back office. Fiecare valoare a unui atribut primește un câmp *Vizibilitate* (*Visible* sau *Hidden*), iar valorile ascunse nu mai pot fi alese de client în selectorul de variante de pe pagina produsului. În back office valorile rămân disponibile pe produse, comenzi de vânzare și variante.

#### 2. Funcționalități Cheie

- **Vizibilitate pe fiecare valoare de atribut:** câmpul *Vizibilitate* (*Visible* implicit sau *Hidden*) apare în lista de valori din formularul atributului. Odoo are aceeași alegere pentru un atribut întreg; modulul o aplică pe valori individuale.
- **Ascundere pe pagina produsului:** când magazinul afișează un produs, valorile ascunse sunt excluse din valorile active ale liniilor de atribut, deci clientul nu le poate alege în selectorul de variante.
- **Unde se configurează:** *Website > eCommerce > Products > Attributes* (sau *Sales > Configuration > Products > Attributes*); se deschide atributul și se setează *Vizibilitate* pe valorile de ascuns. Meniul este disponibil când opțiunea *Variante* este activată în setări.
- **Limitări:**
  - filtrele de atribute din bara laterală a magazinului listează în continuare valorile ascunse;
  - suprascrierea paginii de magazin calculează o listă de valori vizibile (`value_ids`) pe care niciun șablon standard nu o citește, deci nu are efect singură asupra paginii de magazin.

*Notă:* descrierea paginii anterioare (filtrarea valorilor după produsele afișate, ajustarea șablonului `website_sale.products_attributes`) nu corespundea codului și a fost corectată după `readme/DESCRIPTION.md` din versiunea 19.0.1.0.6.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.attribute.value` (extins): adaugă câmpul `visibility` (`visible` / `hidden`, implicit `visible`, indexat).
- `product.template.attribute.value` (extins): câmpul stocat `website_visible`, calculat din `visibility` al valorii de atribut; `_only_active` filtrează valorile ascunse când contextul conține `website_id`.

**Vizualizări**

- `product_attribute_view_form`: moștenește `product.product_attribute_view_form` și adaugă câmpul `visibility` după `default_extra_price`.

**Controllere**

- `WebsiteSaleAttribute` (extinde `WebsiteSale`): suprascrie ruta `shop` (parametrii `category` și `search` numiți explicit, restul prin `kwargs`) și adaugă `value_ids` în `qcontext`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- `website_sale`: modulul standard Odoo de comerț electronic, a cărui pagină de produs și a cărui rută de magazin sunt extinse de acest modul.
- [deltatech_website_sale_attribute_filter](../deltatech_website_sale_attribute_filter/index.md): modul complementar, care lucrează asupra filtrelor de atribute din panoul lateral al magazinului (acolo valorile ascunse de acest modul apar încă, conform limitărilor din README).
