# Deltatech Website SEO (localizat la `deltatech_website_seo/index.md`)

- **Nume Tehnic:** `deltatech_website_seo`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_seo
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_seo`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul optimizează modul în care Google și celelalte motoare de căutare „citesc" magazinul online Odoo, adăugând date structurate (JSON-LD) în paginile de produs și de categorie. Practic, magazinul devine eligibil pentru afișări îmbunătățite în rezultatele de căutare — casetă de căutare directă pe site (Sitelinks Searchbox), carusel de produse recomandate și fir de navigare (breadcrumb) în lista de categorii — ceea ce crește vizibilitatea și rata de click din Google, fără intervenție manuală din partea echipei de marketing.

#### 2. Funcționalități Cheie

- Adaugă date structurate de tip Website (Sitelinks Searchbox) pe toate paginile magazinului și ale produselor.
- Adaugă un carusel de tip ItemList și un Breadcrumb structurat (date invizibile, pentru motoarele de căutare) în listarea de categorii a magazinului.
- Îmbogățește JSON-LD-ul de produs pe care Odoo îl generează deja pe pagina produsului cu SKU, MPN, marcă, categorie și disponibilitate.
- Validează codul GTIN (îl elimină dacă nu are efectiv 8/12/13/14 cifre), evitând erorile de tip „Invalid GTIN" în Google Search Console pentru coduri interne de referință.
- Nu duplică datele de Organizație (Corporate Contact, Logo companie) și Breadcrumb per-produs, deoarece acestea sunt deja furnizate nativ de Odoo 19 pe această versiune.

*Notă de corecție:* `readme/DESCRIPTION.md` menționează generic funcționalitățile de mai sus fără referiri la versiuni vechi; `readme/HISTORY.md` confirmă că modulul a fost portat/adaptat explicit pentru Odoo 19 (secțiunea `19.0.1.1.0`), înlocuind markup-ul `itemprop`/`itemscope` (specific versiunilor anterioare) cu îmbogățirea directă a JSON-LD-ului nativ `_to_markup_data()`. Nu a fost necesară nicio corecție suplimentară.

#### 3. Dependențe

- `website_sale_stock`
- [deltatech_brand_field](../deltatech_brand_field/index.md)

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost preluată din `readme/DESCRIPTION.md`, prin urmare analiza detaliată a componentelor tehnice de mai jos este una sumară, orientativă (nu înlocuiește o analiză completă), conform fluxului de ingestie din schemă.

**Modele**

- `product.product`: suprascrie `_to_markup_data()` pentru a adăuga `sku`, `mpn`, `brand`, `category` și `availability` în JSON-LD-ul de produs generat nativ de `website_sale`, și pentru a elimina câmpul `gtin` atunci când valoarea din `barcode` nu este un GTIN valid (8/12/13/14 cifre).

**Vizualizări**

- `deltatech_website_seo.snippet_homepage`: injectează pe pagina de start snippet-ul `WebSite`/`SearchAction` (Sitelinks Searchbox).
- `deltatech_website_seo.products`: pe pagina `/shop`, injectează snippet-ul `WebSite`, caruselul `ItemList` și, pentru paginile de categorie, breadcrumb-ul structurat `BreadcrumbList`.
- `deltatech_website_seo.snippet_website`, `snippet_carousels`, `snippet_breadcrumb`: șabloanele QWeb care generează efectiv blocurile `<script type="application/ld+json">` cu date serializate prin `json.dumps` (JSON sigur, fără interpolare brută de șiruri).

#### 5. Conexiuni

- [deltatech_brand_field](../deltatech_brand_field/index.md): furnizează metoda `get_brand_name()` folosită de acest modul pentru a popula câmpul `brand` din JSON-LD-ul de produs.
- [deltatech_website_breadcrumb](../deltatech_website_breadcrumb/index.md): adaugă un breadcrumb *vizual* (navigare pentru client) pe pagina de produs, distinct de breadcrumb-ul *structurat* (date invizibile pentru motoarele de căutare, pe pagina de categorie) generat de acest modul — funcționalități complementare, fără suprapunere de cod.
- `website_sale`: modul core Odoo pe care acest modul îl completează — `website_sale` generează deja nativ JSON-LD-ul de Organizație (sitewide) și Breadcrumb per-produs, motiv pentru care acest modul nu le mai duplică.
