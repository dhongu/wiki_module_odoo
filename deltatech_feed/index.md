# Products Feed (localizat la `deltatech_feed/index.md`)

- **Nume Tehnic:** `deltatech_feed`
- **Versiune:** `20.0.3.8.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_feed
- **Cale Locală:** `odoo-addons/bitshop/deltatech_feed`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul publică produsele magazinului Odoo sub formă de feed-uri pentru site-uri de comparare a prețurilor, marketplace-uri și platforme de reclame: fiecare listă de produse primește o adresă publică de feed pe care platforma o citește singură, după propriul program, cu prețurile unei liste de prețuri alese și cu stocul disponibil pe website. Nimic nu este trimis de Odoo însuși; fiecare platformă descarcă feed-ul.

#### 2. Funcționalități Cheie

- **Feed-uri pentru platformele principale:** Google Merchant Center (citit și de catalogul Facebook și Instagram), OpenAI (ChatGPT search și Ads), eMAG, CEL.ro, Compari, Bizoo, 2Performant, VidaXL și e-licitatie, plus feed-uri generice: stoc și preț în XML sau CSV, stoc în JSON și export de bază de produse în CSV.
- **O listă, un feed:** produsele unui feed sunt o listă de produse cu filtru (implicit produsele publicate); fiecare listă alege tipul de feed, formatul, website-ul și lista de prețuri (*Website > eCommerce > Produse > Listă de produse*).
- **Prețuri și stoc ca în magazin:** prețurile vin din lista de prețuri aleasă, cu extra-urile de atribute ale fiecărei variante; stocul este cantitatea disponibilă pentru website.
- **Datele cerute de platforme:** SKU și cod de bare al variantei, brand, categoria Google (tab *Vânzări*, blocul *ECOMMERCE SHOP*), categoria publică, descriere scurtă sau HTML (sau numele ca descriere) și imagini redimensionate la mărimea cerută.
- **Setări per listă:** filtrul **Produse**, **Limita** de produse (0 = fără limită), **Câmp de identificare**, **Restricționează accesul** cu **Access Token**, **Ore cache** și **Auto Refresh**, iar pentru cataloage Google mari, **Use subfeeds**.
- **Rapid și protejat:** feed-urile se generează în fundal și se servesc din cache (implicit 12 ore), cu reîmprospătare programată; butonul **Refresh Feeds** regenerează după modificări mari, iar platforma primește fișierul anterior până la finalizare.
- **Cifre de generare:** fiecare listă arată când a fost generat feed-ul, cât a durat și dimensiunea fișierului.
- **Feed OpenAI / ChatGPT (csv):** OpenAI nu citește feed-ul de la adresă; fișierul CSV se încarcă pe SFTP-ul indicat de OpenAI, de fiecare dată când se schimbă catalogul. Se completează brandul produselor (altfel se trimite numele website-ului) și codurile de bare, iar limita se ridică la tot catalogul.
- Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).
- **Date publicate:** adresele de feed sunt publice (în afara cazului în care se cere token de acces) și expun datele de produs de mai sus, prețurile listei alese și stocul disponibil.

#### 3. Dependențe

- `product`
- `website_sale_stock`
- [deltatech_brand_field](../deltatech_brand_field/index.md)
- [deltatech_product_list](../deltatech_product_list/index.md)
- [deltatech_website_short_description](../deltatech_website_short_description/index.md)

#### 4. Componente Cheie

Readme-ul nu detaliază componentele tehnice; lista de mai jos provine din analiza codului curent (feed-uri active în cod, lock-uri de generare).

**Modele**

- `product.template` (`models/product.py`): extins cu câmpul `google_product_category` și metode utilitare (`get_product_ID`, `_get_simple_info`) pentru informații ușoare de preț/stoc folosite la generarea feed-urilor.
- `product.list` (`models/product_list_openai.py`): extinde lista de produse cu generarea feed-ului OpenAI / ChatGPT (CSV).
- `product.list` (`models/product_list.py`): moștenește `product.list` și `portal.mixin`; adaugă `id_field`, `brand_field` (calculat), `pricelist_id`, `website_id`, opțiuni de descriere (`use_html`, `use_short_description`, `use_name_as_description`) și domeniul de produse (`products_domain`); găzduiește metoda de reîmprospătare programată (`_cron_refresh_feed`).
- `website` (`models/website.py`): extinde `sale_product_domain` pentru a include potrivirea căutării pe brand de produs.

**Vizualizări**

- `views/feed_google.xml`, `views/feed_google_index.xml`: șabloane de feed pentru Google Merchant Center.
- `views/feed_emag.xml`: șablon de feed pentru eMAG Marketplace.
- `views/feed_compari.xml`: șablon de feed pentru Compari.
- `views/feed_e_licitatie.xml`: șablon de feed pentru e-licitatie.ro.
- `views/feed_ptc.xml`: șablon de feed pentru clientul PTC.
- `views/website_product_templates.xml`: șabloane web pentru livrarea feed-ului.
- `views/product_view.xml`, `views/product_list_view.xml`: interfețe pentru gestionarea produselor și a listelor de produse.

**Controllere**

- `controllers/main.py` (`WebsiteProducts`): controller web pentru generarea și livrarea feed-urilor (link-uri către produse, escapare CDATA pentru conținut HTML); folosește lock-uri consultative PostgreSQL (namespace `FEED_LOCK_CLASS_ID`) pentru a serializa generarea feed-urilor și a evita suprapunerea rulărilor concurente.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_regenerate_feed` („Feed: refresh"): sarcină `ir.cron` care rulează zilnic (interval 1 zi) și apelează `model._cron_refresh_feed()` pe modelul `product.list` pentru a reîmprospăta feed-urile.

#### 5. Conexiuni

- [deltatech_product_list](../deltatech_product_list/index.md): furnizează modelul de liste de produse pe care se bazează gruparea produselor pentru feed-uri.
- [deltatech_brand_field](../deltatech_brand_field/index.md): oferă câmpul de brand/producător folosit în datele exportate către platforme.
- [deltatech_website_short_description](../deltatech_website_short_description/index.md): pune la dispoziție descrierea scurtă utilizată în feed-uri.
- `website_sale_stock`: aduce datele de stoc din e-commerce, valorificate la generarea feed-urilor.
