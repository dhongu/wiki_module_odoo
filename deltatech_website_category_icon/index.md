# eCommerce Category Icons (localizat la `deltatech_website_category_icon/index.md`)

- **Nume Tehnic:** `deltatech_website_category_icon`
- **Versiune:** `20.0.1.0.1`
- **Cale:** [https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_category_icon](https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_category_icon)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_category_icon`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă fiecărei categorii din magazinul online o pictogramă proprie în format SVG, afișată direct în magazin. Categoriile devin mai ușor de recunoscut vizual, iar pictogramele rămân clare la orice dimensiune, fără imagini grele de încărcat.

#### 2. Funcționalități Cheie

- Câmp nou **Icon (SVG)** pe categoria eCommerce, cu previzualizare în formularul categoriei.
- Categoriile din partea de sus a magazinului (filmstrip) afișează pictograma în locul imaginii categoriei.
- Lista de categorii din stânga afișează o pictogramă mică înaintea denumirii fiecărei categorii care are una (vizualizarea *Category Icons in List*, care poate fi arhivată).
- SVG-ul este validat la salvare, deci este sigur pentru paginile publice: sunt acceptate doar forme simple (`path`, `rect`, `circle`, `ellipse`, `line`, `polyline`, `polygon`, `g`), cu culori, numere și `transform`. Scripturile, stilurile, linkurile, imaginile externe și handlerele de evenimente sunt refuzate, cu un mesaj care spune ce trebuie corectat. Desenul are nevoie de `viewBox`, iar dimensiunea provine din pagină.
- Pictogramele pot fi desenate manual, generate în masă de Terrabit în stilul magazinului sau scrise prin câmpul `icon_svg` (import, XML-RPC).
- Utilizare: **Website > eCommerce > Categories**, se deschide categoria, se lipește codul SVG în **Icon (SVG)** și se salvează. Pentru filmstrip, se activează în editorul website-ului banda de categorii din partea de sus a magazinului.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.public.category` (extins): câmpul `icon_svg`, previzualizarea HTML calculată și curățarea/validarea SVG-ului la creare și scriere.

**Vizualizări**

- `views/product_public_category_views.xml`: câmpul și previzualizarea pe formularul categoriei.
- `views/shop_template.xml`: pictogramele în filmstrip și în lista de categorii din magazin.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `website_sale`: magazinul online în care sunt afișate pictogramele.
