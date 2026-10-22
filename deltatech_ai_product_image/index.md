# AI - Product Photos and Data Finder (localizat la `deltatech_ai_product_image/index.md`)

- **Nume Tehnic:** `deltatech_ai_product_image`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_product_image
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_product_image`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul găsește pozele, descrierea, codul de bare și greutatea unui produs în catalogul Icecat și pe web, le face verificate sau redactate de modelul de limbaj al unui agent AI din Odoo 19 Enterprise și lasă o persoană să le aleagă și să le aplice înainte ca ceva să fie salvat pe produs. Reduce munca de completare a fișelor de produs din magazinul online, păstrând controlul uman asupra datelor.

#### 2. Funcționalități Cheie

- **Poze, Icecat întâi:** codul de bare al produsului (sau al unei variante) este căutat în Icecat, ale cărui poze sunt publicate de branduri pentru magazine.
- **Căutare web cu AI:** când Icecat oferă mai puțin de 3 poze, modelul caută paginile produsului, site-ul producătorului și distribuitorii oficiali; marketplace-urile, băncile de imagini și rețelele sociale sunt excluse (lista se poate modifica). Pozele sunt citite din ce declară pagina pentru produs (schema.org `Product`, Open Graph, `image_src`), nu logo-uri sau bannere.
- **Descărcare sigură:** doar adrese publice, cu limite de dimensiune și redirecturi; pozele sub dimensiunea minimă și duplicatele sunt eliminate.
- **Verificare AI a pozelor:** fiecare poză primește verdict (*This Product*, *Uncertain*, *Other Product*), scor și semnalare de watermark, logo de magazin sau text promoțional.
- **Alegere de către om:** pozele apar ordonate de la cea mai bună, cu site-ul sursă și pagina; *Main Image* și *Add to Gallery* le scriu pe produs. Opțional, pe un produs fără imagine, cea mai bună poză se setează automat peste un prag de scor, dacă nu are watermark.
- **Descriere:** redactată de modelul de limbaj din textele Icecat și ale paginilor produsului, în limba utilizatorului, fără caracteristici inventate: paragraf, 3–5 beneficii și tabel de specificații pentru magazin, plus 1–2 propoziții pentru descrierea de vânzare. Propunerea se compară cu cea curentă, se poate edita, apoi *Apply* sau *Reject*. Produsele cu descriere primesc propunere doar dacă setarea o permite.
- **Cod de bare cu verificări stricte:** propus doar dintr-o sursă structurată (GTIN Icecat găsit după brand și cod producător, sau `gtin` schema.org de pe o pagină cu același cod producător), cu cifră de control GS1 corectă (EAN-8, UPC-A, EAN-13, GTIN-14), nefolosit de alt produs sau ambalaj, identic în toate sursele (altfel ambele sunt afișate, blocate) și doar pentru produse cu o singură variantă și fără cod de bare. Nu se aplică niciodată fără o persoană; verificările se refac la aplicare.
- **Greutate:** pe un produs fără greutate, se propune cea de pe o pagină (schema.org) sau din specificațiile Icecat, convertită în unitatea bazei de date, când unitatea e clară.
- **Procesare în masă:** până la 3 produse se caută pe loc; restul intră în coadă, procesată de acțiunea programată *AI: search the queued product photos*.
- **Trasabilitate:** fiecare căutare păstrează pozele găsite, adresa și pagina sursă (utilă pentru verificarea drepturilor de utilizare). *Search Again* reia căutarea după corectarea codului de bare, a referinței sau a brandului.
- **Utilizare:** în **Website › eCommerce › Products**, *Actions › Find Photos and Data with AI* (și pe formularul produsului); rezultatele se văd în **Website › eCommerce › AI Product Photos and Data**, în filele *Photos*, *Description*, *Barcode and Data*. Căutarea devine *Done* când nu mai e nimic de ales sau aplicat.
- **Configurare:** în **Website › Configuration › Settings**, blocul *AI Product Photos and Data*: ce se caută, *Also For Products With a Description*, *Icecat User Name* (cont gratuit Open Icecat; token doar pentru Full Icecat), *Icecat Only*, dimensiune minimă, site-uri excluse, scor pentru imaginea principală automată (0 = mereu manual) și modelul de limbaj al agentului *Product Image Finder* (trebuie să citească imagini și să caute pe web). Utilizatorii au nevoie de dreptul *Product › Create*; pentru codul de bare, produsele au nevoie de referință internă (cod producător) și, cu `deltatech_brand_field`, de brand.
- **Drepturi asupra pozelor:** o poză publică pe web nu e liberă de folosit; se preferă pozele Icecat și ale producătorilor.

#### 3. Dependențe

- `website_sale`
- `ai_app`
- [deltatech_website_product_url_image](../deltatech_website_product_url_image/index.md)

#### 4. Componente Cheie

**Modele**

- `product.image.search`: o căutare pentru un produs, cu starea (*To Review*, *Done*) și rezultatele.
- `product.image.candidate`: o poză candidată, cu verdict AI, scor, sursă, dimensiune și pagină de origine.
- `product.image.search.data`: datele propuse (descriere, cod de bare, greutate) cu surse și verificări.
- `product.template` (extins): acțiunea de căutare din formular.
- `res.config.settings` (extins): setările căutării.

**Vizualizări**

- `product_image_search_view_form` / `_list` / `_search`: căutările și filtrele (inclusiv *Data to Apply*).
- `product_image_candidate_view_kanban`: pozele candidate cu butoanele *Main Image* / *Add to Gallery*.
- `product_image_search_data_view_form` / `_list`: propunerile de descriere, cod de bare și greutate.
- `res_config_settings_view_form_ai_product_image`: setările modulului.

**Acțiuni Automate / Acțiuni Server**

- `action_server_ai_find_images`: *Find Photos and Data with AI*, pe produsele selectate.
- `ir_cron_ai_product_image`: *AI: search the queued product photos*, procesează căutările din coadă.
- `ai_agent_product_image`: agentul AI *Product Image Finder*.

#### 5. Conexiuni

- [deltatech_brand_field](../deltatech_brand_field/index.md): brandul produsului, folosit la căutarea codului de bare în Icecat (dacă e instalat).
- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): permite folosirea modelelor Anthropic Claude pentru agent.
