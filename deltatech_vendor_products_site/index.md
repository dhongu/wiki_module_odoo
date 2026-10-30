# Vendor Products from Website Pages (localizat la `deltatech_vendor_products_site/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_site`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_vendor/tree/19.0/deltatech_vendor_products_site`
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_site`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Citește **prețul de achiziție, stocul, codurile, pozele și descrierea** produselor direct de pe site-ul unui furnizor care nu trimite feed (CSV, XML sau API), inclusiv de pe magazinele B2B care cer autentificare. Ce se citește ajunge în catalogul furnizorului, ca în cazul unui feed; ce ajunge la produsele proprii este verificat înainte, iar pozele și descrierile sunt alese de o persoană. Citirea paginilor este ultima soluție: se cere întâi un feed sau un API de la furnizor.

#### 2. Funcționalități Cheie

**Citirea paginilor**
- Tip nou de conexiune pe feedul furnizorului, *Vendor Website*: adresa site-ului, autentificarea, pauza dintre pagini și numărul de pagini pe rulare.
- Datele schema.org (JSON-LD, Microdata) sunt citite primele: nume, cod, cod de bare, brand, poze, descriere, preț, monedă, disponibilitate (prin modulul `deltatech_web_scan`).
- Pentru celelalte site-uri: selectori XPath, CSS, expresie regulată sau cale JSON-LD, cu tabel de valori (ex. *În stoc* devine disponibil). Butonul *Test on 5 Pages* arată ce se citește, fără să scrie nimic.

**Găsirea paginilor**
- Import dintr-un fișier CSV sau Excel cu codul și adresa paginii (coloana *Page URL*).
- Sitemap: paginile de produs din `sitemap.xml` (și din indexul lui) intră în catalog, filtrate după un șablon de adresă; codul lor e provizoriu până la prima citire.
- Căutare pe site: produsele proprii care au furnizorul pe o linie de furnizor sunt căutate după codul furnizorului (sau codul de bare). Pagina se leagă de produs doar dacă arată același cod sau cod de bare.

**Autentificare pe magazine B2B**
- Formular de login (câmpurile ascunse, ex. tokenul CSRF, se retrimit), HTTP Basic sau token de acces; utilizatorul și parola sunt cele ale feedului, vizibile doar administratorilor.
- Sesiunea trăiește doar în memorie; parola nu apare în mesaje sau loguri.
- Fără ocolirea protecțiilor: CAPTCHA, verificarea în doi pași sau protecția anti-roboți opresc citirea (stare *Blocked*). După două autentificări eșuate la rând feedul nu se mai autentifică, ca să nu fie blocat contul.

**Verificări înainte de produse**
- *Other Product*: pagina arată alt cod de bare sau alt cod decât rândul din catalog.
- Preț suspect: o variație peste procentul setat (implicit 30%) sau o monedă diferită de a feedului așteaptă confirmare (*Confirm Price*).
- Butoanele *Update Purchase Price* / *Update Price List* și acțiunile programate sar peste rândurile suspecte, produsele greșite și paginile blocate.
- *Propose Content* afișează poza și descrierea produsului lângă cele de pe pagina furnizorului; implicit se aplică doar ce lipsește.

**Istoric și programare**
- Istoricul prețurilor pe intervale: o linie nouă doar când se schimbă prețul de achiziție sau disponibilitatea; altfel ultima linie se prelungește.
- Citire programată, inactivă implicit: din oră în oră, paginile scadente ale feedurilor cu termenii confirmați (*Automatic Reading Allowed*), site cu site, reluând de unde a rămas.
- Politețe: se respectă robots.txt (dezactivabil doar după confirmarea termenilor furnizorului) și o pauză de 3 secunde între două pagini ale aceluiași site.

**Configurare (pe scurt)**: în *Purchase › Products › Vendor Feed* se creează un feed de tip *Vendor Website*, se confirmă termenii, se adaugă paginile, se rulează *Test on 5 Pages*, apoi se activează acțiunea programată. Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- [deltatech_web_scan](../deltatech_web_scan/index.md)

#### 4. Componente Cheie

**Modele**

- `vendor.feed` (extins): tipul de conexiune *Vendor Website*, autentificarea, acțiunile de test, citire sitemap, căutare pe site și citire pagini.
- `vendor.product` (extins, cu `web.scan.source.mixin`): rândul din catalog primește starea paginii, sursa și verificările de cod/preț.
- `vendor.product.price.history` (cu `web.scan.history.mixin`): istoricul prețurilor și al disponibilității pe intervale.
- `vendor.site.selector`: selectorii (XPath, CSS, regex, cale JSON-LD) pentru valorile citite de pe site, per feed.
- `vendor.feed.column` (extins): mapare de coloane pentru importul paginilor.
- `vendor.product.content.wizard` (tranzitoriu): propunerea de poze și descrieri.

**Vizualizări**

- `view_vendor_feed_form_site`: fila *Website* pe feed, cu butoanele de test, sitemap, căutare și citire.
- `view_vendor_product_tree_site`, `view_vendor_product_form_site`, `view_vendor_product_search_site`: catalogul cu starea paginii, prețul suspect și filtrele aferente.
- `view_vendor_product_price_history_list` / `_graph` / `_search`: istoricul prețurilor (listă, grafic, căutare).
- `view_vendor_product_content_wizard_form`: dialogul *Propose Content*.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_vendor_site_scan` (*Vendor Website: Read Pages*): rulează `model._cron_site_scan()` pe `vendor.feed`, din oră în oră; inactiv implicit.

#### 5. Conexiuni

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): același catalog de furnizori (`vendor.product`) este folosit și pentru căutarea online în magazin; nu este dependență.
- [deltatech_vendor_products_storage](../deltatech_vendor_products_storage/index.md): alt modul din suita `bitshop_vendor`, documentat în paralel.
