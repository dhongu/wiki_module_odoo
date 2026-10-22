# Products Feed (localizat la `deltatech_feed/index.md`)

- **Nume Tehnic:** `deltatech_feed`
- **Versiune:** `19.0.3.7.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_feed
- **Cale Locală:** `odoo-addons/bitshop/deltatech_feed`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul publică produsele din magazinul Odoo sub formă de feed-uri pentru site-uri de comparare de prețuri, marketplace-uri și platforme de publicitate. Fiecare listă de produse primește o adresă publică pe care platforma o citește singură, la intervalul ei, cu prețurile unei liste de prețuri alese și cu stocul disponibil pe website. Astfel, datele de produs se administrează într-un singur loc și se distribuie pe mai multe canale. Odoo nu trimite nimic activ: fiecare platformă descarcă feed-ul.

#### 2. Funcționalități Cheie

- **Feed-uri pentru principalele platforme**: Google Merchant Center (citit și de catalogul Facebook și Instagram), OpenAI (căutare ChatGPT și Ads), eMAG, CEL.ro, Compari, Bizoo, 2Performant, VidaXL și e-licitatie, plus feed-uri generice: stoc și preț în XML sau CSV, stoc în JSON și export de bază de produse în CSV.
- **O listă, un feed**: produsele unui feed sunt o listă de produse cu filtru (implicit, produsele publicate); fiecare listă alege tipul feed-ului, formatul, website-ul și lista de prețuri. Câmpul **Limit** plafonează numărul de produse; 0 (implicit la listele noi) înseamnă fără limită.
- **Prețuri și stoc ca în magazin**: prețurile vin din lista de prețuri aleasă, cu extra-urile atributelor fiecărei variante; stocul este cantitatea disponibilă pentru website.
- **Datele cerute de platforme**: SKU și cod de bare pe variantă, brand, categorie Google, categorie publică, descriere scurtă sau HTML (sau denumirea ca descriere) și imagini redimensionate la dimensiunea cerută de platformă; câmpul de identificare a produsului este configurabil.
- **Rapid și protejat**: feed-urile se generează în fundal și se servesc din cache (implicit 12 ore), cu reîmprospătare programată opțională (**Auto Refresh**); cataloagele Google mari pot fi împărțite în sub-feed-uri (**Use subfeeds**); un token de acces (**Restrict Access**) limitează cine citește feed-ul.
- **Cache separat pe fiecare rută de feed**: o cerere pe altă rută nu mai înlocuiește feed-ul citit de marketplace-uri; generarea este serializată cu lock-uri, iar cererea care pierde lock-ul primește copia expirată din cache.
- **Cifre de generare**: fiecare listă afișează când a fost generat feed-ul, cât a durat și dimensiunea fișierului; butonul **Refresh Feeds** forțează regenerarea după modificări mari de produse sau prețuri.
- **Flux operațional**: listele se creează din *Website > eCommerce > Products > Product List*; linkul din câmpul **Feed** se dă platformei. La produse se completează **Google category** pentru publicarea în Google.
- **OpenAI / ChatGPT (csv)**: OpenAI nu citește feed-ul de la adresă; fișierul CSV se încarcă pe locația SFTP primită în contul de reclame OpenAI, de fiecare dată când se schimbă catalogul. Se completează brandul (altfel se trimite numele website-ului) și codurile de bare, iar **Limit** se ridică la întreg catalogul. Se trimite un rând pe variantă; variantele fără imagine sau fără preț pozitiv sunt excluse, iar GTIN apare doar dacă codul de bare are cifra de control validă.

#### 3. Dependențe

- `product`
- `website_sale_stock`
- [deltatech_brand_field](../deltatech_brand_field/index.md)
- [deltatech_product_list](../deltatech_product_list/index.md)
- [deltatech_website_short_description](../deltatech_website_short_description/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template` (`models/product.py`): extins cu câmpul `google_product_category` și metode utilitare pentru informații de preț/stoc folosite la generarea feed-urilor.
- `product.list` (`models/product_list.py`, `models/product_list_openai.py`): moștenește `product.list` și `portal.mixin`; adaugă tipul și formatul feed-ului (`feed_type`, `format_type`), `feed_link`, `id_field`, `brand_field` (calculat), `pricelist_id`, `website_id`, opțiunile de descriere (`use_html`, `use_short_description`, `use_name_as_description`), `products_domain`, `limit`, `restrict_access`, dimensiunile imaginii, `cache_hours`, `auto_refresh`, `use_subfeeds`/`limit_subfeeds` și cifrele de generare; găzduiește `_cron_refresh_feed`. Extensia OpenAI adaugă tipul `openai` (CSV).
- `website` (`models/website.py`): extinde `sale_product_domain` pentru a include potrivirea căutării pe brand.

**Vizualizări**

- `views/feed_google.xml`, `views/feed_google_index.xml`: șabloane Google Merchant Center și indexul de sub-feed-uri.
- `views/feed_emag.xml`, `views/feed_compari.xml`, `views/feed_e_licitatie.xml`: șabloane pentru eMAG, Compari și e-licitatie.
- `views/feed_ptc.xml`: șablonul „Generic stock and price (XML)" (cheia tehnică `ptc` păstrată pentru compatibilitate).
- `views/website_product_templates.xml`: șabloane web pentru livrarea feed-urilor.
- `views/product_view.xml`, `views/product_list_view.xml`: câmpul Google category pe produs și formularul listei de produse cu setările feed-ului.

**Controllere**

- `controllers/main.py` (`WebsiteProducts`): rute publice `/feed/products_<tip>_feed_<id>.<ext>` (Google, eMAG, CEL, Compari, Bizoo, VidaXL, e-licitatie, stoc JSON, OpenAI CSV etc.) și sub-feed-uri paginate; verifică token-ul de acces, folosește lock-uri consultative PostgreSQL și cache pe fiecare rută.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_regenerate_feed` („Feed: refresh"): `ir.cron` zilnic care apelează `model._cron_refresh_feed()` pe `product.list`, pentru listele cu **Auto Refresh** bifat.

#### 5. Conexiuni

- [deltatech_product_list](../deltatech_product_list/index.md): furnizează listele de produse pe care se bazează feed-urile.
- [deltatech_brand_field](../deltatech_brand_field/index.md): câmpul de brand exportat către platforme.
- [deltatech_website_short_description](../deltatech_website_short_description/index.md): descrierea scurtă folosită în feed-uri.
- `website_sale_stock`: stocul disponibil pe website, publicat în feed.
