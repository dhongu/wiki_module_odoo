# Website SEO (localizat la `deltatech_website_seo/index.md`)

- **Nume Tehnic:** `deltatech_website_seo`
- **Versiune:** `20.0.1.1.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_seo
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_seo`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă datele structurate (Schema.org JSON-LD) pe care Odoo nu le publică singur în paginile magazinului și completează datele de produs deja publicate, astfel încât motoarele de căutare să afișeze caseta de căutare a magazinului și detaliile produselor (preț, disponibilitate, marcă) direct în rezultate. Vizibilitatea în Google crește fără intervenție manuală din partea echipei de marketing.

#### 2. Funcționalități Cheie

- **Casetă de căutare în rezultate:** pagina de start și paginile magazinului declară căutarea pe site (`WebSite` + `SearchAction` către `/shop?search=`), markup-ul folosit de Google pentru sitelinks search box.
- **Date de produs mai bogate:** pe pagina produsului, JSON-LD-ul generat de Odoo primește SKU și MPN (referința internă), marca, categoria publică și disponibilitatea ofertei (în stoc / fără stoc, din stocul disponibil pe site; serviciile și produsele vândute fără stoc sunt în stoc).
- **Doar coduri de bare valide:** codul de bare se publică drept GTIN doar dacă are 8, 12, 13 sau 14 cifre, deci un cod intern stocat ca cod de bare nu mai produce erori „invalid GTIN" în Search Console.
- **Fără duplicate:** datele organizației, lista de produse a paginilor de magazin și categorie (`CollectionPage` / `ItemList`) și breadcrumb-urile, pe care Odoo 20 le publică deja, nu se adaugă a doua oară.
- **Configurare:** se instalează pe o bază cu aplicația eCommerce; se completează pe produs **Referința internă**, **Codul de bare**, **Marca** și categoriile de site; pentru produsele vândute fără stoc se bifează **Sell when Out-of-Stock**, ca să fie publicate ca „în stoc".
- **Verificare:** paginile se pot testa cu Rich Results Test de la Google și se urmăresc în Search Console. Marca provine din modulul *Brand Field*. Nu se trimit date în afara Odoo; markup-ul face parte din pagină.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `website_sale_stock`
- [deltatech_brand_field](../deltatech_brand_field/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` (completat cu `USAGE.md` / `CONFIGURE.md`), deci analiza componentelor de mai jos este sumară.

**Modele**

- `product.product`: completează markup-ul JSON-LD al produsului (`sku`, `mpn`, `brand`, `category`, `availability`) și elimină `gtin` când codul de bare nu este valid (8/12/13/14 cifre).

**Vizualizări**

- `snippet_homepage`: adaugă pe pagina de start datele `WebSite` / `SearchAction` (moștenește `website.homepage`).
- `products`: adaugă același markup pe paginile magazinului (moștenește `website_sale.products`).
- `snippet_website`: șablonul QWeb care generează blocul `application/ld+json` al căutării pe site.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_brand_field](../deltatech_brand_field/index.md): furnizează marca (`get_brand_name()`) publicată în JSON-LD.
- [deltatech_website_breadcrumb](../deltatech_website_breadcrumb/index.md): breadcrumb vizual pentru client, complementar datelor structurate.
- `website_sale`: generează nativ organizația și breadcrumb-urile pe care modulul nu le mai duplică.
