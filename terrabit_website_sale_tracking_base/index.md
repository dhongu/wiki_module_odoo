# Website Sale Tracking Base (localizat la `terrabit_website_sale_tracking_base/index.md`)

- **Nume Tehnic:** `terrabit_website_sale_tracking_base`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/terrabit_website_sale_tracking_base
- **Cale Locală:** `odoo-addons/bitshop/terrabit_website_sale_tracking_base`
- **Ultima Ingestie:** 2026-11-28

#### 1. Sumar

Modul de fundație care centralizează urmărirea evenimentelor de magazin online pentru mai multe platforme de marketing (Meta/Facebook, TikTok etc.). Oferă o configurație globală unică și evenimente normalizate pe care modulele de pixel le consumă, ca logica să nu fie duplicată în fiecare modul de tracking.

#### 2. Funcționalități Cheie

- **Configurare centralizată:** în *Website > Configuration > Settings* se aleg **Tracking Item ID Type** (variantă de produs, șablon de produs sau SKU) și **Tracking Exclude Delivery** (costul de transport nu intră în valoarea conversiilor).
- **Evenimente normalizate:** captează interacțiunile „Add to Cart", „Begin Checkout", „Add Payment Info", „Search", „Contact" și „Form Submit" și le re-emite ca `CustomEvent` DOM cu prefix `terrabit_tracking:*`, consumate de pixelii din aval.
- **Payload îmbogățit:** extinde datele de tracking de bază (view item, add to cart, purchase) cu `item_tmpl_id` și `item_sku`, ca **Item ID Type** să fie respectat în browser.
- **Sursă unică de adevăr:** metoda `_get_tracking_data` asigură aceleași valori în Pixel (browser) și în Conversions API (server).
- **Cadru JS:** interacțiune Odoo înregistrată în registrul `public.interactions`, care emite evenimentele pe rădăcina `.oe_website_sale`.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `website`: extins cu `tracking_exclude_delivery`, `tracking_item_id_type` și helperul `_get_tracking_data`.
- `res.config.settings`: expune setările de tracking.
- `product.template`: extinde datele de tracking ale produsului cu `item_tmpl_id` și `item_sku`.

**Vizualizări**

- `views/res_config_settings_views.xml`: setările de tracking (Item ID Type, Exclude Delivery).
- `views/website_templates.xml`: injectează în pagină opțiunile de tracking.
- `static/src/js/website_sale_tracking_base.esm.js`: interacțiunea care emite evenimentele normalizate.

**Controllere:** `WebsiteSaleTracking` (extinde `WebsiteSale`) adaugă SKU și ID de șablon pe liniile de purchase.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [terrabit_facebook_pixel](../terrabit_facebook_pixel/index.md): consumă evenimentele normalizate pentru Meta Pixel/CAPI.
- [terrabit_tiktok_pixel](../terrabit_tiktok_pixel/index.md): consumă evenimentele normalizate pentru TikTok Pixel/CAPI.
