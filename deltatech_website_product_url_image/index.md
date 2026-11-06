# Product Image from URL (localizat la `deltatech_website_product_url_image/index.md`)

- **Nume Tehnic:** `deltatech_website_product_url_image`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_product_url_image
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_product_url_image`
- **Ultima Ingestie:** `2026-11-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul simplifică gestionarea imaginilor de produs în magazinul online, permițând încărcarea unei poze direct dintr-o adresă web (URL), fără a descărca manual fișierul și a-l urca apoi în Odoo. Este util mai ales la importul în masă al cataloagelor de produse, când imaginile sunt deja găzduite pe site-ul unui furnizor sau pe un server propriu, scurtând timpul de pregătire a produselor pentru publicare.

#### 2. Funcționalități Cheie

- **Imaginea principală**: adresa lipită în **Image File Name** (formularul produsului, fila **Sales**, grupul **Ecommerce Shop**) descarcă imaginea și o setează ca imagine a produsului; câmpul păstrează apoi doar numele fișierului. Dacă adresa rămâne în câmp, imaginea nu a putut fi încărcată.
- **Imagini suplimentare**: adresa lipită în **Image Name** al unei imagini din **Ecommerce Media** încarcă acea imagine; se apasă **Save** în fereastra imaginii, apoi se salvează produsul.
- **Import**: actualizarea produselor existente prin import (cu coloana ID) și coloana **Image File Name** cu adrese web încarcă imaginile; produsele create prin import păstrează adresa ca text, fără imagine.
- **Descărcare sigură**: se accesează doar adrese publice `http`/`https` (protecție SSRF, cu verificarea fiecărei redirecționări, maximum 5), răspunsul trebuie să fie o imagine de cel mult 10 MB, cu timp limitat (15 s), iar descărcarea o pot declanșa doar utilizatorii care au drept de modificare a produselor.
- Verificare: pagina produsului din magazin (**Go to Website**) afișează imaginea principală și cea suplimentară provenite din adrese.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Componentele sunt descrise după cod, fiindcă README-ul nu le detaliază.

**Modele**

- `product.template` (extins): adaugă câmpul `image_file_name`; `_fetch_public_image` descarcă imaginea (verificări de adresă publică, redirecționări, tip și mărime), `_load_image_from_url` returnează imaginea în base64, iar `onchange_image_file_name` și `write` setează `image_1920` și reduc câmpul la numele fișierului.
- `product.image` (extins): `onchange_name` și `write` încarcă imaginea suplimentară din adresa introdusă în `name`.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs din `website_sale` cu câmpul `image_file_name` în grupul `extra_info`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module documentate în wiki.
