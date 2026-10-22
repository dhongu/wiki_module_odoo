# eCommerce Category Icons

- **Nume Tehnic:** `deltatech_website_category_icon`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_category_icon
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_category_icon`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul oferă fiecărei categorii de magazin online o iconiță proprie în format SVG și o afișează în magazin: în partea de sus a paginii magazinului, în lista de categorii din stânga și într-un bloc care poate fi plasat pe orice pagină a site-ului. Iconița este aleasă intenționat pentru categorie, spre deosebire de imaginea categoriei, care este adesea doar fotografia primului produs, iar navigarea devine astfel mai clară și mai unitară vizual. Iconița este verificată la salvare, deci este sigur să fie afișată pe paginile publice.

#### 2. Funcționalități Cheie

- Câmp nou **Icon (SVG)** pe categoria de eCommerce, cu previzualizare directă pe formularul categoriei (**Website > eCommerce > Categories**).
- Categoriile din partea de sus a magazinului (filmstrip) afișează iconița în locul imaginii categoriei; filmstrip-ul se activează din editorul de website, în pagina magazinului.
- Lista de categorii din stânga afișează o iconiță mică înaintea numelui.
- Opțiunea **Category Icons in List** (Website > Configuration > Settings, secțiunea Shop - Products) stabilește ce categorii din listă arată iconiță:
  - **Main categories only** (implicit): subcategoriile unei ramuri deschise apar ca text simplu;
  - **All categories**: orice categorie cu iconiță proprie o afișează;
  - **All categories, inherit from parent**: o subcategorie fără iconiță preia iconița celui mai apropiat părinte care are una.
- Opțiunea **Category Icon Order** (aceeași pagină de setări) stabilește ce se afișează pentru o categorie, prima variantă găsită: **SVG, imagine, nimic** (implicit), **Imagine, SVG, nimic**, **SVG, imagine, imaginea primului produs** sau **Imagine, SVG, imaginea primului produs**. „SVG” este iconița categoriei sau, în lipsă, a celui mai apropiat părinte; „imaginea primului produs” este poza primului produs publicat din categorie sau din subcategorii. Ordinea se aplică în filmstrip, în lista din stânga, în blocul Category Icon Grid și, când este instalat, în meniul și lista de subcategorii din Website Shop Blocks.
- Bloc de website **Category Icon Grid** (grupul Catalog din editor), pentru orice pagină (home, landing): categoriile principale sau categorii alese manual, cu iconiță și nume, fiecare cu link către pagina sa din magazin. Se randează la fiecare vizită, deci arată mereu iconițele curente; numărul maxim și dimensiunea iconițelor sunt opțiuni ale blocului; 6 coloane pe desktop, 2 pe telefon.
- Iconițele desenate cu `currentColor` preiau culoarea link-ului categoriei, deci urmează tema, culoarea la hover și categoria activă.
- Validare la salvare, cu listă de elemente permise: doar forme simple (`path`, `rect`, `circle`, `ellipse`, `line`, `polyline`, `polygon`, `g`), cu culori, numere și `transform`. Scripturile, stilurile, linkurile, imaginile externe și handlerele de evenimente sunt refuzate, cu mesaj care spune ce trebuie corectat. Desenul trebuie să aibă `viewBox`; dimensiunea provine din pagină.
- Iconițele pot fi desenate manual, generate în masă de Terrabit în stilul magazinului sau scrise de orice instrument prin câmpul `icon_svg` (import, XML-RPC); validarea se aplică la fel.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.public.category` (extins): adaugă `icon_svg` (curățat la `create`/`write` prin `_sanitize_icon_svg`), câmpurile calculate `icon_html`, `icon_preview` și `icon_inherited_html` (iconița părintelui), metoda `tb_category_visual` (alege ce se afișează conform ordinii setate) și `_get_icon_grid_categories` (categoriile blocului Category Icon Grid).
- `website` (extins): opțiunile `category_icon_levels` și `category_icon_order`.
- `res.config.settings` (extins): expune cele două opțiuni în setările Website.

**Vizualizări**

- `product_public_category_form_view`: previzualizare și editor de cod pentru `icon_svg` pe formularul categoriei.
- `filmstrip_categories` (moștenește `website_sale.filmstrip_categories`): iconița în filmstrip.
- `categorie_link_icon` (moștenește `website_sale.categorie_link`): iconiță în lista de categorii din stânga.
- `res_config_settings_view_form`: opțiunile Category Icons in List și Category Icon Order.
- `s_category_icon_grid`, `s_category_icon_grid_items`, `snippets`: blocul Category Icon Grid și înregistrarea lui în editor (cu opțiuni în `website_builder`, JS/OWL).

**Acțiuni Automate / Acțiuni Server**

- Nu are. Migrarea `19.0.1.2.0` (post-migration) există pentru actualizarea datelor existente.

#### 5. Conexiuni

- [deltatech_website_category](../deltatech_website_category/index.md): moștenește același template `website_sale.categorie_link`, deci cele două module afectează aceeași listă de categorii din magazin.
- [deltatech_website_shop_snippets](../deltatech_website_shop_snippets/index.md) (Website Shop Blocks): când este instalat, ordinea iconițelor se aplică și în meniul de categorii și în lista de subcategorii din Website Shop Blocks (legătură opțională, nedeclarată în manifest).
