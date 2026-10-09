# Sale Catalog Website Categories & Image Zoom (Categorii website și mărire imagine în catalogul de vânzări)

- **Nume Tehnic:** `deltatech_sale_catalog_website`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_catalog_website
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_catalog_website`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul îmbunătățește catalogul de produse care se deschide din comanda de vânzare (butonul „Catalog" de pe o ofertă sau comandă). Panoul din stânga afișează categoriile din website în locul categoriilor interne, iar imaginea produsului se poate deschide la dimensiune completă printr-un simplu clic. Astfel, vânzătorul găsește mai ușor produsele, după structura din magazinul online, și le poate inspecta vizual în timp ce completează comanda. Modificările se aplică doar catalogului de vânzări; catalogul din achiziții rămâne cel standard.

#### 2. Funcționalități Cheie

- Categoriile de website (`public_categ_ids`) apar ca arbore ierarhic în panoul de căutare din stânga, în locul categoriilor interne de produs.
- Selectarea unei categorii părinte listează și produsele din subcategoriile ei (filtrare în cascadă).
- Clic pe imaginea unui produs din catalog o deschide la rezoluție completă într-o fereastră de dialog.
- Aplicabil exclusiv catalogului deschis din comanda de vânzare; catalogul din comenzile de achiziție nu este afectat.
- Starea de dezvoltare a modulului: Beta.

#### 3. Dependențe

- `sale`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.product` (extins): suprascrie `search_panel_select_range` pentru câmpul many2many `public_categ_ids`, reproducând algoritmul ierarhic standard (cu contoare); afișează numele scurt al categoriei, nu calea completă.
- `sale.order` (extins): `action_add_from_catalog` înlocuiește vizualizările kanban și de căutare ale catalogului cu cele proprii, doar pentru vânzări.

**Vizualizări**

- `product_view_kanban_catalog_website`: kanban de catalog derivat din `product.product_view_kanban_catalog`, cu `js_class` propriu și widget-ul `image_catalog_zoom` pe imagine.
- `product_view_search_catalog_website`: căutare de catalog derivată din `product.product_view_search_catalog`; ascunde categoria internă și adaugă arborele „Website Category".
- Front-end (JS/OWL): `ProductCatalogWebsiteSearchModel` (folosește operatorul `child_of` și pe many2many), `ImageCatalogZoomField` și `ImageZoomDialog` (dialog cu imaginea la dimensiune completă).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_product_catalog](../deltatech_product_catalog/index.md): tipărește un catalog PDF pe categorii de website; legătură funcțională prin categoriile de website, dar nu este dependență.
