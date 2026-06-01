# Website Sale Tracking Base (localizat la `terrabit_website_sale_tracking_base/index.md`)

- **Nume Tehnic:** `terrabit_website_sale_tracking_base`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/terrabit_website_sale_tracking_base
- **Cale Locală:** `odoo-addons/bitshop/terrabit_website_sale_tracking_base`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Modul de fundație care centralizează și standardizează urmărirea evenimentelor de eCommerce pentru mai multe platforme de marketing (Meta/Facebook, TikTok etc.) într-un magazin Odoo 19. Oferă o configurație globală unică (tipul de identificator de produs și excluderea livrării din valoarea conversiilor) și o magistrală de evenimente normalizate pe care modulele de pixel o consumă, evitând duplicarea logicii în fiecare modul de tracking.

## 2. Funcționalități Cheie

- **Configurare centralizată:** setări globale per website pentru **Item ID Type** (Product Variant ID / Product Template ID / SKU) și **Exclude Delivery** (excluderea costului de transport din valoarea conversiilor).
- **Evenimente normalizate:** capturează acțiunile utilizatorului neacoperite de core (begin checkout, add payment info, search, contact pe `tel:`, form submit) și le re-emite ca `CustomEvent`-uri DOM cu prefix `terrabit_tracking:*` pe rădăcina `.oe_website_sale`.
- **Îmbogățire payload tracking:** extinde datele de tracking ale core-ului (view item, add to cart, purchase) cu `item_tmpl_id` și `item_sku`, astfel încât `Item ID Type` să poată fi respectat client-side de pixeli.
- **Sursă unică de adevăr:** metoda helper `_get_tracking_data` asigură consistența valorilor între Pixel (client) și Conversion API (server) în modulele dependente.

## 3. Dependențe

- `website_sale`

## 4. Componente Cheie

### Modele

- `website`: extins cu `tracking_exclude_delivery`, `tracking_item_id_type` și helperul `_get_tracking_data`.
- `res.config.settings`: expune setările de tracking în pagina de configurare a website-ului.
- `product.template`: override pe `_get_combination_info` (populează `product_tracking_info` indiferent de cheia Google Analytics) și `_get_google_analytics_data` (adaugă `item_tmpl_id`/`item_sku`).

### Controllere

- `WebsiteSaleTracking` (extinde `website_sale.controllers.main.WebsiteSale`): `order_lines_2_google_api` adaugă SKU/template id pe liniile de purchase.
- `CartTracking` (extinde `website_sale.controllers.cart.Cart`): `_get_tracking_information` adaugă SKU/template id pe liniile de add-to-cart.

### Vizualizări / JS

- `views/res_config_settings_views.xml`: setările de tracking (Item ID Type, Exclude Delivery).
- `views/website_templates.xml`: injectează în pagină input-urile ascunse cu opțiunile de tracking.
- `static/src/js/website_sale_tracking_base.esm.js`: interaction `WebsiteSaleTrackingBase` (framework Odoo 19 `@web/public/interaction`, registry `public.interactions`) care emite evenimentele normalizate.

## 5. Conexiuni

- [terrabit_facebook_pixel](../terrabit_facebook_pixel/index.md): consumă evenimentele normalizate și îmbogățirea de payload pentru Meta Pixel/CAPI.
- [terrabit_tiktok_pixel](../terrabit_tiktok_pixel/index.md): consumă evenimentele normalizate și îmbogățirea de payload pentru TikTok Pixel/CAPI.
