# Marketplace website addon (localizat la `deltatech_marketplace_website/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_website`
- **Versiune:** `19.0.0.2.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_website`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_website`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Acest modul îmbogățește website-ul Odoo orientat către client, integrând date specifice marketplace-ului și oferind informații descriptive suplimentare potențialilor cumpărători. Din punct de vedere business, extensia ajută la construirea încrederii și a clarității cu cumpărătorii online, afișând detaliile relevante de marketplace direct în magazinul online. Astfel, conținutul de pe website-ul Odoo și cel din magazinele de tip marketplace rămân aliniate, oferind o experiență de brand unitară și consecventă, gestionată dintr-un singur backend Odoo centralizat.

Modulul este marcat „Hidden" (categorie) și are preț simbolic: se instalează ca dependență a conectorului de marketplace ales, nu se cumpără de sine stătător.

#### 2. Funcționalități Cheie

- Informații bogate despre produs: valorifică descrierile scurte de marketplace pentru a oferi conținut concis și informativ pe paginile de produs.
- Vizibilitate îmbunătățită: scoate în evidență atributele și branding-ul specifice marketplace-ului pe website, îmbunătățind experiența de căutare și descoperire.
- Experiență consecventă pentru client: aliniază informațiile între website-ul Odoo și magazinele de tip marketplace pentru un parcurs de brand fără întreruperi.
- Optimizarea conversiei: conținut descriptiv mai bun și branding clar pot duce la o implicare mai mare și la rate de conversie a vânzărilor îmbunătățite.
- Platformă unificată: gestionează conținutul website-ului și informațiile legate de marketplace dintr-un backend Odoo unic, centralizat.
- Galerii de imagini sincronizate după link: metoda unică `marketplace.product.image.sync_gallery` tratează imaginile suplimentare ale șabloanelor și variantelor, pentru toate conectoarele. O imagine se recunoaște după id-ul din marketplace sau după link; se descarcă doar imaginile noi sau cele cu link schimbat. Imaginea care nu mai vine din marketplace este ștearsă de pe produs, imaginile adăugate manual în Odoo rămân neatinse, iar o galerie goală nu schimbă nimic.
- Categorii publice din marketplace: importul mapează categoriile externe pe `product.public.category` (opțiunea „Use public category" pe backend, activă implicit); mapările duplicate apar în roșu în listă, cu filtrul „Duplicate mappings", iar la citirea id-ului extern se folosește cea mai recentă mapare.
- Mapare categorii eCommerce pe categorii marketplace (nou în 0.2.0): pe o categorie marketplace (Marketplace > Categories) câmpul „eCommerce Categories” listează categoriile eCommerce ale căror produse se publică acolo. O subcategorie nemapată urmează cea mai apropiată categorie părinte mapată, deci e suficient să mapezi ramurile principale. Dacă un produs e în mai multe categorii eCommerce, câștigă potrivirea cea mai specifică (cea mai adâncă în arbore), apoi ordinea eCommerce; la egalitate, mapările mai noi au prioritate. Produsele fără mapare eCommerce urmează în continuare categoria internă. Se folosește la exportul produselor noi și apare ca „Proposed Marketplace Category” pe binding-ul produsului.
- Descrierea scurtă de site se preia doar dacă este instalat separat `deltatech_website_short_description`; fără el valoarea primită este ignorată.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `website_sale`

#### 4. Componente Cheie

> Documentat pe baza fișierelor `readme/DESCRIPTION.md`, `HISTORY.md`, `FISA_CONSULTANT.md` și a structurii modelelor din cod.

- **Modele extinse:** `marketplace.backend` (câmpul `use_public_category`, importul categoriilor publice), `marketplace.backend.item` (tip de element pentru categorii publice), `marketplace.product` și `marketplace.product.template` (`prepare_values` / `save_from_marketplace`; pe `marketplace.product` și `_marketplace_category_for_export`, care alege întâi categoria din maparea eCommerce, apoi pe cea internă), `marketplace.product.category` (câmpul `public_categ_ids` „eCommerce Categories” și căutarea `_find_by_public_categories`), `product.public.category` (câmp calculat `external_id`).
- **Modele noi (binding-uri):** `marketplace.public.category` (legătură cu `product.public.category`) și `marketplace.product.image` (legătură cu `product.image`, câmp `image_url`).
- **Vizualizări:** categorii publice, imagini de produs și backend; `views/category_view.xml` adaugă câmpul „eCommerce Categories” în formularul și lista categoriilor marketplace (`views/`).
- **Securitate:** `security/ir.model.access.csv`.
- **Teste:** `tests/test_sync_gallery.py`, `tests/test_category_mapping.py`.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): modulul de bază pentru funcționalitatea de marketplace, pe care această extensie îl aduce către website.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): extinde marketplace-ul pe zona de vânzări, complementar integrării din storefront.
