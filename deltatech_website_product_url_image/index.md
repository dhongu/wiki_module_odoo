# Product Image from URL (localizat la `deltatech_website_product_url_image/index.md`)

- **Nume Tehnic:** `deltatech_website_product_url_image`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_product_url_image
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_product_url_image`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul simplifică gestionarea imaginilor de produs în magazinul online, permițând încărcarea unei poze direct dintr-o adresă web (URL), fără a fi nevoie să descarci manual fișierul și apoi să-l urci în Odoo. Este util mai ales la importul în masă al cataloagelor de produse, când imaginile sunt deja găzduite pe site-ul unui furnizor sau pe un server propriu. Descărcarea este protejată: se preiau doar adrese publice, iar răspunsul trebuie să fie o imagine.

#### 2. Funcționalități Cheie

- **Imaginea principală**: adresa lipită în **Image File Name** (formularul produsului, fila de eCommerce, grupul *Shop*) descarcă imaginea și o setează ca imagine a produsului; câmpul păstrează apoi doar numele fișierului. Dacă adresa rămâne în câmp, imaginea nu a putut fi încărcată.
- **Imagini suplimentare**: adresa lipită în **Image Name** al unei imagini din *Ecommerce Media* încarcă acea imagine (se apasă apoi *Save* în fereastra imaginii și se salvează produsul).
- **Import**: la actualizarea produselor existente prin import (cu coloana ID), coloana **Image File Name** cu adrese web încarcă imaginile; produsele create prin import păstrează adresa ca text, fără imagine.
- **Descărcare sigură**: se preiau doar adrese publice `http`/`https`, fiecare redirecționare este verificată, răspunsul trebuie să fie o imagine de maximum 10 MB, iar descărcarea poate fi declanșată doar de utilizatorii care pot edita produse.
- Fluxul pas cu pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpul pentru introducerea URL-ului imaginii și logica de descărcare a imaginii principale din link.
- `product.image` (extins): permite încărcarea imaginilor suplimentare din galeria produsului pornind de la un URL.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs din `website_sale` adăugând câmpul pentru numele/URL-ul fișierului imagine în secțiunea de informații suplimentare.

**Acțiuni Automate / Acțiuni Server**

- Nu este cazul. Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- Nu au fost identificate conexiuni cu alte module documentate în wiki.
