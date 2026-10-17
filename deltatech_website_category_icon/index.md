# eCommerce Category Icons

- **Nume Tehnic:** `deltatech_website_category_icon`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_category_icon
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_category_icon`
- **Ultima Ingestie:** `2026-10-17`

#### 1. Sumar

Modulul oferă fiecărei categorii de magazin online o iconiță proprie în format SVG și o afișează în magazin. Iconița este o alegere făcută intenționat pentru categorie, spre deosebire de imaginea categoriei, care este adesea doar fotografia primului produs. Astfel, navigarea prin categorii devine mai clară și mai unitară vizual. Iconița este verificată la salvare, deci este sigur să fie afișată pe paginile publice.

#### 2. Funcționalități Cheie

- Câmp nou **Icon (SVG)** pe categoria de eCommerce, cu previzualizare directă pe formularul categoriei. Se completează din **Website > eCommerce > Categories**, lipind codul SVG în câmp.
- Categoriile afișate în partea de sus a magazinului (filmstrip) arată iconița în locul imaginii categoriei; categoriile fără iconiță rămân cu imaginea. Filmstrip-ul se activează din editorul de website, în pagina magazinului.
- Lista de categorii din stânga afișează o iconiță mică înaintea numelui, doar pentru categoriile care o au (view-ul **Category Icons in List**, care poate fi arhivat dacă nu e dorit).
- Validare la salvare, cu listă de elemente permise: doar forme simple (`path`, `rect`, `circle`, `ellipse`, `line`, `polyline`, `polygon`, `g`, plus `title`), cu culori, numere și `transform`. Scripturile, stilurile, linkurile, imaginile externe și handlerele de evenimente sunt refuzate, iar mesajul de eroare spune ce trebuie corectat.
- Desenul trebuie să aibă `viewBox`; dimensiunea provine din pagină (CSS), iar atributele `width`/`height` sunt eliminate. Dimensiunea maximă este de 20.000 de caractere.
- Iconițele pot fi desenate manual, generate în masă de Terrabit în stilul magazinului (skill-ul Claude `iconita-categorie`, din pluginul terrabit-odoo, care nu este un modul Odoo) sau scrise de orice instrument prin câmpul `icon_svg` (import, XML-RPC); validarea se aplică la fel în toate cazurile.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.public.category` (extins): adaugă `icon_svg` (marcajul SVG, curățat la `create`/`write` prin `_sanitize_icon_svg`) și câmpurile calculate `icon_html` și `icon_preview`, folosite la afișare și la previzualizare.

**Vizualizări**

- `product_public_category_form_view` (moștenește `website_sale.product_public_category_form_view`): adaugă previzualizarea și editorul de cod XML pentru `icon_svg`, după imaginea de copertă.
- `filmstrip_categories` (moștenește `website_sale.filmstrip_categories`): afișează iconița în locul imaginii, când există.
- `categorie_link_icon` (moștenește `website_sale.categorie_link`): iconiță mică în lista de categorii din stânga.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_website_category](../deltatech_website_category/index.md): moștenește același template `website_sale.categorie_link`, deci cele două module afectează aceeași listă de categorii din magazin.
