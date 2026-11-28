# Prestashop Marketplace Connector (localizat la `deltatech_marketplace_prestashop/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_prestashop`
- **Versiune:** `20.0.0.7.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_prestashop
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_prestashop`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectorul PrestaShop sincronizează un magazin PrestaShop cu Odoo, peste cadrul Marketplace al suitei, prin API-ul de servicii web al PrestaShop. Produsele, clienții și comenzile se gestionează din Odoo, fără dublă introducere: catalogul, comenzile și starea lor circulă între cele două sisteme, iar stocul vine din PrestaShop în Odoo.

#### 2. Funcționalități Cheie

- Conectare cu cheia de webservice (**Location** = URL-ul care se termină în `/api`, tip de acces *Client_id and client_secret*, cheia în **Client Secret / API key**). **Test connection** nu contactă magazinul: o eroare reală apare abia la primul import sau export.
- Import produse (șabloane, variante/combinații, caracteristici, atribute, accesorii, imagini), categorii publice, clienți, țări, județe, limbi, valute, depozite, transportatori, procesatori de plată și etape de comandă; fiecare tip are un card în fila **Objects**, cu **Import** în meniul ⋮ (nu există **Import All**; **Only Missing** limitează importul la ce lipsește).
- Setări de limbă și taxe: **Prestashop Lang** (gol pentru magazin multilingv; importul de limbi îl rescrie) și **Prestashop Tax Included** (afectează și prețurile produselor importate); **Disable Import Sale Order** scoate backend-ul din cron-ul comun de comenzi.
- Import comenzi cu client, adrese, linii, livrare, reduceri și plată, marcate cu starea PrestaShop; filtrare opțională pe statusuri prin **Import Orders With Status (PrestaShop)**, în limita ferestrei **Order Days**.
- Import automat prin **Marketplace: Get Orders** (orară, inactivă implicit) sau prin webhook (apelat de PrestaShop spre Odoo), cu import imediat al comenzii indicate.
- Export produse (preț din lista backend-ului sau `list_price`, nume, EAN, greutate, categorii, imagini): manual din cardul **Product Template** (setați întâi un **Domain**), automat cu **Active On Write** sau prin wizardul *Marketplace sync* în modul *All*. Exportul de stoc și de preț separat nu este implementat (acțiunile programate comune sunt fără efect).
- Din Odoo spre PrestaShop: starea comenzii (doar cu **Active On Write** pe **Sale Order**), numărul de urmărire și linkul facturii (necondiționat).
- Rută pentru factura unei comenzi importate: `/marketplace/sale_order/get_invoice`, autentificată cu **Security Token** al backend-ului.
- Indicator de sănătate pe kanban-ul backend-urilor (ultima sincronizare, contoare, joburi eșuate) și acțiunea *Map Products* pentru legarea produselor existente după referință sau cod de bare.
- Mapare câmpuri produs: vezi tabelul din secțiunea 4.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, componentele nu au fost extrase din cod (readme-ul acoperă funcționalitatea); lista de modele este din prezentarea modulului.

**Modele**

- `marketplace.backend` (extins): provider-ul `prestashop` și opțiunile lui.
- Legături extinse: `marketplace.product.template`, `marketplace.product`, `marketplace.product.attribute`, `marketplace.product.attribute.value`, `marketplace.product.image`, `marketplace.public.category`, `marketplace.customer`, `marketplace.sale.order`, `marketplace.sale.phase`, `marketplace.sale.tag`, `marketplace.delivery.carrier`, `marketplace.payment.provider`, `marketplace.country`, `marketplace.county`, `marketplace.currency`, `marketplace.lang`, `marketplace.warehouse`, `marketplace.stock`.

**Vizualizări**

- `views/backend_views.xml`, `views/menu.xml`: setările backend-ului și meniul conectorului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_prestashop_late_customer_messages`: „PrestaShop: Customer Messages After Confirmation", orar, inactiv implicit.
- Importul comenzilor folosește cron-ul comun **Marketplace: Get Orders** (orar, inactiv implicit).

**Mapare câmpuri produs**

"Ambele" înseamnă că starea circulă în ambele sensuri, pe acțiunea proprie. Câmpurile traductibile circulă pe fiecare limbă din `marketplace.lang`.

| Câmp | Câmp Odoo | Câmp PrestaShop | Direcție |
|------|-----------|-----------------|----------|
| ID produs | `external_id` (legătură) | `id` | ambele |
| Denumire produs | `name` | `name` (traductibil) | ambele |
| Referință internă | `default_code`, `external_code` (legătură) | `reference` | ambele |
| Preț de vânzare | `list_price` | `price` (fără TVA) | ambele (importul adaugă TVA cu **Tax included**; exportul ia prețul din lista backend-ului) |
| Cod de bare | `barcode` | `ean13` | ambele |
| Greutate | `weight` | `weight` | ambele |
| Publicat | `active` | `active` | Odoo → PrestaShop |
| Descriere site | `website_description` | `description` (traductibil) | ambele |
| Descriere scurtă | `description_sale` | `description_short` (traductibil) | Odoo → PrestaShop |
| Meta titlu | `website_meta_title` | `meta_title` (traductibil) | ambele |
| Meta descriere | `website_meta_description` | `meta_description` (traductibil) | ambele |
| Meta cuvinte-cheie | `website_meta_keywords` | `meta_keywords` (traductibil) | ambele |
| Categorii eCommerce | `public_categ_ids` | `associations.categories` | ambele (cu **Use public category**) |
| Caracteristici | `product.attribute.value` | `associations.product_features` | PrestaShop → Odoo |
| Atribute de variantă | `attribute_line_ids` | `associations.product_option_values` | PrestaShop → Odoo |
| Variante | legături `marketplace.product` | `associations.combinations`, `/combinations` | PrestaShop → Odoo |
| Referință variantă | `default_code`, `external_code` | `/combinations` `reference` | PrestaShop → Odoo |
| Preț variantă | `list_price` | `/combinations` `price` | PrestaShop → Odoo |
| Accesorii | `accessory_product_ids` | `associations.accessories` | PrestaShop → Odoo |
| Imagine principală | `image_1920` | `id_default_image`, `/images/products/{id}` | ambele |
| Imagini suplimentare | `product.image` | `associations.images` | ambele |
| Stoc | `odoo_stock` (legătură), `external_quantity` | `/stock_availables` `quantity` | PrestaShop → Odoo |

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): comenzile de vânzare din marketplace (dependență tranzitivă prin `deltatech_marketplace_delivery`).
