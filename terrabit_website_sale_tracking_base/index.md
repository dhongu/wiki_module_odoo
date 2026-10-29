# Website Sale Tracking Base (localizat la `terrabit_website_sale_tracking_base/index.md`)

- **Nume Tehnic:** `terrabit_website_sale_tracking_base`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_website_sale_tracking_base
- **Cale Locală:** odoo-addons/bitshop/terrabit_website_sale_tracking_base
- **Ultima Ingestie:** `2026-10-29`

#### 1. Sumar

Modul de fundație care centralizează și standardizează urmărirea evenimentelor de eCommerce pentru mai multe platforme de marketing (Meta/Facebook, TikTok, Google etc.) într-un magazin Odoo 19. Oferă o configurație globală unică, pe website (tipul de identificator de produs și excluderea livrării din valoarea conversiilor), și evenimente normalizate pe care modulele de pixel le consumă, ca logica să nu fie duplicată în fiecare modul de tracking.

#### 2. Funcționalități Cheie

- **Configurare centralizată:** în **Website → Configurare → Setări**, per website, **Item ID Type** (Product Variant ID / Product Template ID / Internal Reference (SKU); implicit variantă) și **Exclude Delivery** (excluderea costului de livrare din valoarea evenimentelor de tracking: Purchase, AddToCart etc.).
- **Evenimente normalizate:** capturează acțiunile utilizatorului neacoperite de core (begin checkout, add payment info, search, contact pe linkuri `tel:`, form submit) și le re-emite ca `CustomEvent`-uri DOM cu prefix `terrabit_tracking:*` pe rădăcina `.oe_website_sale`; fiecare eveniment poartă în `detail.options` setările de tracking (`excludeDelivery`, `itemIdType`).
- **View item și add to cart:** nu sunt re-emise; modulele de pixel folosesc direct evenimentele core `view_item_event` și `add_to_cart_event`, pentru a evita duplicarea.
- **Îmbogățire payload tracking:** extinde datele de tracking ale core-ului (view item, add to cart, purchase) cu `item_tmpl_id` și `item_sku`, astfel încât `Item ID Type` să poată fi respectat de pixeli în browser. Datele pentru view item se populează și fără o cheie Google Analytics configurată.
- **Sursă unică de adevăr:** helperul `_get_tracking_data` returnează valoarea comenzii (fără livrare, dacă opțiunea e activă) și moneda, ca valorile să fie identice între Pixel (client) și Conversion API (server) în modulele dependente.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `website` (extins): `tracking_exclude_delivery`, `tracking_item_id_type` și helperul `_get_tracking_data`.
- `res.config.settings` (extins): expune cele două setări de tracking în configurarea website-ului.
- `product.template` (extins): `_get_combination_info` populează `product_tracking_info` indiferent de cheia Google Analytics, iar `_get_google_analytics_data` adaugă `item_tmpl_id` și `item_sku`.

**Controllere**

- `WebsiteSaleTracking` (extinde `WebsiteSale`): `order_lines_2_google_api` adaugă SKU-ul și id-ul de template pe liniile de purchase.
- `CartTracking` (extinde `Cart`): `_get_tracking_information` adaugă SKU-ul și id-ul de template pe liniile de add-to-cart.

**Vizualizări**

- `res_config_settings_view_form`: setările „Exclude Delivery" și „Item ID Type" din configurarea website-ului.
- `tracking_base_info`: injectează în pagină input-uri ascunse cu opțiunile de tracking, citite de JS.
- `static/src/js/website_sale_tracking_base.esm.js`: interaction `WebsiteSaleTrackingBase` (framework-ul Odoo 19 `@web/public/interaction`, registry `public.interactions`) care emite evenimentele normalizate.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește cron-uri sau acțiuni server.

#### 5. Conexiuni

- [terrabit_facebook_pixel](../terrabit_facebook_pixel/index.md): depinde de acest modul și consumă evenimentele normalizate și îmbogățirea de payload pentru Meta Pixel/CAPI.
- [terrabit_tiktok_pixel](../terrabit_tiktok_pixel/index.md): depinde de acest modul și consumă evenimentele normalizate și îmbogățirea de payload pentru TikTok Pixel/CAPI.
- [terrabit_google_tag](../terrabit_google_tag/index.md): depinde de acest modul pentru setările și datele de tracking comune.
