# Filtrare produse pe marcă în website

- **Nume Tehnic:** `website_sale_product_brand`
- **Versiune:** `20.0.2.4.0`
- **Cale:** https://github.com/dhongu/others_addons/tree/20.0/website_sale_product_brand
- **Cale Locală:** `odoo-addons/others_addons/website_sale_product_brand`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Extinde filtrarea produselor din magazinul online cu filtrare după marcă și adaugă pagini de destinație pentru fiecare marcă, la `/shop/brand/<slug>`, cu conținut propriu în antet și subsol. Reduce efortul clientului în căutarea produselor unei anumite mărci.

#### 2. Funcționalități Cheie

- Filtru pe marcă în magazin și meniul „shop by brand" lângă Shop; selectarea unei mărci publicate din `/shop/brands` duce la pagina ei.
- Formularul mărcii (**Website > Setări > Produse > Product brands**): logo, descriere, imagine de copertă, blocuri de descriere în antet și subsol, aliniere antet, afișare nume/descriere.
- Logo-ul mărcii apare pe pagina produsului și trimite la pagina mărcii; descrierea mărcii se poate afișa sub descrierea produsului (opțiunea *Show description on product page*, dezactivată implicit).
- Ascunderea unei mărci din magazin prin butonul *Website published*.
- Multi-website: marca poate fi legată de un website (câmp vizibil în grupul `website.group_multi_website`); paginile, listările, indexul de căutare și sitemap-ul expun doar mărcile website-ului curent sau globale.
- Setarea *Brand Filter Display* (Website > Configurare > Setări, secțiunea Shop - Products): *Full list*, *Limited list* (primele 5 și „Show more") sau *Alphabetical accordion* (grupare pe litere, peste 50 de mărci).

#### 3. Dependențe

- [product_brand](../product_brand/index.md)
- `website`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.brand` (extins): câmpuri de website, publicare și conținut pentru pagina mărcii.
- `product.template` (extins).
- `website` (extins) și `res.config.settings` (extins): setarea de afișare a filtrului.

**Vizualizări**

- `view_product_brand_form`, `view_product_brand_tree`: formularul și lista mărcilor, cu câmpurile de website.
- `res_config_settings_view_form`: setarea *Brand Filter Display*.
- Șabloane QWeb în `views/templates.xml` și interacțiunea `website_sale_brand_filter`; opțiune în website builder pentru filtru.

**Acțiuni Automate / Acțiuni Server**

- Nu există; meniul „Brands" este creat din `data/website_menu.xml`.

#### 5. Conexiuni

- [product_brand](../product_brand/index.md): modelul de bază al mărcilor.
