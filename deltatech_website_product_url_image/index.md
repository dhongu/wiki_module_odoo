# eCommerce Product Image URL Link (localizat la `deltatech_website_product_url_image/index.md`)

- **Nume Tehnic:** `deltatech_website_product_url_image`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_product_url_image`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_product_url_image`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul simplifică gestionarea imaginilor de produs în magazinul online, permițând încărcarea unei poze direct dintr-un link (URL) extern, fără a fi nevoie să descarci manual fișierul și apoi să-l urci în Odoo. Este util mai ales la importul în masă al cataloagelor de produse, când imaginile sunt deja găzduite pe site-ul unui furnizor sau pe un server propriu, scurtând astfel timpul de pregătire a produselor pentru publicare în eCommerce.

#### 2. Funcționalități Cheie

- Încărcarea imaginii principale a produsului dintr-un URL extern (introducerea adresei descarcă automat poza).
- Încărcarea imaginilor suplimentare din galeria produsului tot pe baza unui URL.
- Curățarea automată a numelui fișierului (din URL se păstrează doar numele imaginii).

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
