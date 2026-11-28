# Marketplace website addon (localizat la `deltatech_marketplace_website/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_website`
- **Versiune:** `20.0.0.2.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_website
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_website`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce conținutul de produs din marketplace pe website-ul Odoo, astfel încât magazinul online să arate aceleași informații ca ofertele din marketplace. Descrierile, categoriile și imaginile importate dintr-un canal extern ajung în categoriile publice și în fișa de produs de pe site, fără a fi reintroduse manual. Este un modul „Hidden”, care se instalează ca dependență a conectorului de marketplace ales.

#### 2. Funcționalități Cheie

- Descrierea de produs din marketplace se salvează ca descriere de website; descrierea scurtă se completează doar dacă este instalat `deltatech_website_short_description`.
- Categoriile din marketplace se mapează pe categoriile publice de eCommerce, inclusiv imaginea categoriei.
- Produsele exportate în marketplace folosesc maparea categoriei lor de eCommerce.
- Imaginile suplimentare ale produsului se păstrează într-o galerie dedicată (`marketplace.product.image`), fără a goli galeria existentă la fiecare reimport.
- Caracteristicile din marketplace se importă în catalogul marketplace, dar nu se afișează pe website, iar modulul nu adaugă informații despre marcă în magazin.
- Fluxul de configurare și verificare, în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `marketplace.public.category` (nou): categoria publică din marketplace, legată de `product.public.category`.
- `marketplace.product.image` (nou): imaginile suplimentare ale produsului din marketplace.
- `marketplace.product`, `marketplace.product.template`, `marketplace.product.category`, `marketplace.backend`, `marketplace.backend.item`, `marketplace.binding` (extinse): descrierea de website, maparea categoriilor și importul imaginilor.
- `product.public.category` (extins): legătura cu categoria din marketplace.

**Vizualizări**

- `view_marketplace_public_category_form` / `_tree` / `_search` și `action_marketplace_public_category`: categoriile publice din marketplace.
- `view_marketplace_product_image_form` / `_tree` / `_search` și `action_marketplace_product_image`: galeria de imagini.
- `view_marketplace_product_category_form` / `_tree` (extinse) și `view_marketplace_backend_form` (extinsă): maparea categoriilor și setările backend-ului.

**Acțiuni Automate / Acțiuni Server**

Nu are.

#### 5. Conexiuni

- [deltatech_marketplace_woocommerce](../deltatech_marketplace_woocommerce/index.md): conector care depinde de acest modul.
- [deltatech_website_short_description](../deltatech_website_short_description/index.md): opțional, adaugă descrierea scurtă de pe website, completată din marketplace.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): zona de vânzări a aceluiași cadru marketplace.
