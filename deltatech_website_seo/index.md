# Website SEO (localizat la `deltatech_website_seo/index.md`)

- **Nume Tehnic:** `deltatech_website_seo`
- **Versiune:** `19.0.1.1.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_seo
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_seo`
- **Ultima Ingestie:** `2026-11-11`

#### 1. Sumar

Acest modul optimizează modul în care Google și celelalte motoare de căutare „citesc" magazinul online Odoo, adăugând date structurate (JSON-LD) în paginile de produs și de categorie. Practic, magazinul devine eligibil pentru afișări îmbunătățite în rezultatele de căutare — casetă de căutare directă pe site (Sitelinks Searchbox), carusel de produse recomandate și fir de navigare (breadcrumb) în lista de categorii — ceea ce crește vizibilitatea și rata de click din Google, fără intervenție manuală din partea echipei de marketing.

#### 2. Funcționalități Cheie

- Căsuță de căutare în rezultate: pagina de start și paginile magazinului declară căutarea pe site (`WebSite` + `SearchAction` către `/shop?search=`), markup-ul folosit de Google pentru Sitelinks Searchbox.
- Lista de produse a unei categorii: pagina de magazin își listează produsele ca `ItemList`, cu adresa fiecărui produs, iar o pagină de categorie adaugă și `BreadcrumbList` (Products › categorie), date invizibile, pentru motoarele de căutare.
- Date de produs mai bogate: JSON-LD-ul pe care Odoo îl generează deja pe pagina produsului primește SKU și MPN (referința internă), marca, categoria publică și disponibilitatea (în stoc / stoc epuizat, după stocul disponibil pe website).
- Validează codul GTIN: codul de bare se publică drept GTIN doar dacă are 8, 12, 13 sau 14 cifre, evitând erorile „Invalid GTIN" în Google Search Console pentru coduri interne.
- Nu duplică datele de Organizație și Breadcrumb-ul per-produs, furnizate deja nativ de Odoo 19.
- Configurare: nu e nevoie de setări; se completează *Internal Reference*, *Barcode*, *Brand* și categoriile website ale produselor. Pentru produsele vândute și fără stoc se bifează *Continue Selling*, ca să fie publicate ca în stoc.
- Verificare: paginile se testează cu Rich Results Test de la Google și se urmăresc în Search Console; după modificări, se cere Google să reindexeze paginile.
- Nu trimite date în afara Odoo: markup-ul face parte din pagină.

#### 3. Dependențe

- `website_sale_stock`
- [deltatech_brand_field](../deltatech_brand_field/index.md)

#### 4. Componente Cheie

**Modele**

- `product.product`: suprascrie `_to_markup_data()` pentru a adăuga `sku`, `mpn`, `brand` (din `get_brand_name()`), `category` (prima categorie publică) și `availability` în JSON-LD-ul de produs generat nativ de `website_sale`, și pentru a elimina câmpul `gtin` atunci când valoarea din `barcode` nu este un GTIN valid (8/12/13/14 cifre).

**Vizualizări**

- `deltatech_website_seo.snippet_homepage`: injectează pe pagina de start snippet-ul `WebSite`/`SearchAction` (Sitelinks Searchbox).
- `deltatech_website_seo.products`: pe pagina `/shop`, injectează snippet-ul `WebSite`, caruselul `ItemList` și, pentru paginile de categorie, breadcrumb-ul structurat `BreadcrumbList`.
- `deltatech_website_seo.snippet_website`, `snippet_carousels`, `snippet_breadcrumb`: șabloanele QWeb care generează efectiv blocurile `<script type="application/ld+json">` cu date serializate prin `json.dumps` (JSON sigur, fără interpolare brută de șiruri).

#### 5. Conexiuni

- [deltatech_brand_field](../deltatech_brand_field/index.md): furnizează metoda `get_brand_name()` folosită de acest modul pentru a popula câmpul `brand` din JSON-LD-ul de produs.
- [deltatech_website_breadcrumb](../deltatech_website_breadcrumb/index.md): adaugă un breadcrumb *vizual* (navigare pentru client) pe pagina de produs, distinct de breadcrumb-ul *structurat* (date invizibile pentru motoarele de căutare, pe pagina de categorie) generat de acest modul — funcționalități complementare, fără suprapunere de cod.
- `website_sale`: modul core Odoo pe care acest modul îl completează — `website_sale` generează deja nativ JSON-LD-ul de Organizație (sitewide) și Breadcrumb per-produs, motiv pentru care acest modul nu le mai duplică.
