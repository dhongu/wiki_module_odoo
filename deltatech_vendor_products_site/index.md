# Vendor Products from Website Pages (localizat la `deltatech_vendor_products_site/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_site`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/20.0/deltatech_vendor_products_site
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_site`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul citește prețul de achiziție, stocul, codurile, pozele și descrierea produselor de pe site-ul unui furnizor care nu oferă flux (CSV, XML sau API), inclusiv de pe magazine B2B cu autentificare. Datele merg în catalogul furnizorului, ca la un flux obișnuit; ce ajunge la produse este verificat mai întâi, iar pozele și descrierile sunt alese de o persoană.

#### 2. Funcționalități Cheie

- Tip de conexiune nou, **Vendor Website**, pe fluxul furnizorului: adresa site-ului, autentificarea, pauza dintre pagini, numărul de pagini per rulare.
- Citire prin date schema.org (JSON-LD, Microdata) cu ajutorul modulului Web Scan Base; pentru alte site-uri, selectori XPath, CSS, expresie regulată sau cale JSON-LD, cu tabel de valori (ex. *In stoc*). Butonul *Test on 5 Pages* arată ce se citește, fără a scrie nimic.
- Găsirea paginilor: import CSV/Excel (cod și *Page URL*), citirea `sitemap.xml` cu filtru pe adresă, căutare pe site după codul furnizorului sau codul de bare (pagina se leagă de produs doar dacă arată același cod).
- Autentificare B2B: formular de login (inclusiv câmpurile ascunse, ex. token CSRF), HTTP Basic sau token de acces; sesiunea trăiește doar în memorie, parola nu apare în mesaje sau loguri. Fără ocolirea protecțiilor: CAPTCHA, verificarea în doi pași sau protecția anti-roboți opresc citirea (stare *Blocked*); după două autentificări eșuate la rând fluxul nu mai încearcă.
- Verificări înainte de produse: *Other Product* pentru pagini cu alt cod sau cod de bare; preț suspect (variație peste procentul setat, implicit 30%, sau altă monedă) care așteaptă *Confirm Price*; butoanele *Update Purchase Price* / *Update Price List* și acțiunile programate sar peste rândurile suspecte, blocate sau cu alt produs.
- *Propose Content*: afișează poza și descrierea produsului lângă cele de pe pagina furnizorului; implicit se aplică doar ce lipsește.
- Istoric de prețuri pe intervale: linie nouă doar când se schimbă prețul de achiziție sau disponibilitatea.
- Citire programată, inactivă implicit: în fiecare oră, paginile scadente ale fluxurilor cu termenii confirmați (*Automatic Reading Allowed*); se respectă robots.txt și o pauză de 3 secunde între pagini.
- Configurare: *Achiziții › Produse › Vendor Feed*, apoi tab-ul *Website*; ordinea completă a pașilor este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- `deltatech_web_scan`

#### 4. Componente Cheie

**Modele**

- `vendor.feed` (extins): tipul de conexiune *Vendor Website*, citirea paginilor.
- `vendor.product` (extins, cu `web.scan.source.mixin`): stări ale paginii, preț suspect, confirmare.
- `vendor.feed.column` (extins): mapare de coloane la import.
- `vendor.site.selector`: selectori pentru site-urile fără date schema.org.
- `vendor.product.price.history` (cu `web.scan.history.mixin`): istoric de prețuri pe intervale.
- `vendor.product.content.wizard`: asistentul *Propose Content* pentru poze și descrieri.

**Vizualizări**

- `view_vendor_feed_form_site`: tab-ul *Website* pe fluxul furnizorului.
- `view_vendor_product_form_site`, `view_vendor_product_tree_site`, `view_vendor_product_search_site`: catalogul cu paginile și stările lor.
- `view_vendor_product_price_history_list` / `_graph` / `_search`: istoricul de prețuri.
- `view_vendor_product_content_wizard_form`: asistentul de conținut.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_vendor_site_scan` (*Vendor Website: Read Pages*): orară, inactivă implicit.

#### 5. Conexiuni

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): produsele furnizorilor în magazinul online.
