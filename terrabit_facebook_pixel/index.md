# Terrabit Facebook Pixel (localizat la `terrabit_facebook_pixel/index.md`)

- **Nume Tehnic:** `terrabit_facebook_pixel`
- **Versiune:** `19.0.0.1.5`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/terrabit_facebook_pixel
- **Cale Locală:** `odoo-addons/bitshop/terrabit_facebook_pixel`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Integrare Meta (Facebook) Pixel și Conversion API (CAPI) pentru website-ul Odoo 19, pentru urmărirea acțiunilor vizitatorilor și optimizarea campaniilor publicitare cu acuratețe ridicată a datelor. Combină tracking-ul client-side din browser (Pixel) cu evenimente server-side (CAPI), depășind limitările AdBlocker-elor și ale browserelor. Se bazează pe modulul de fundație `terrabit_website_sale_tracking_base` pentru evenimentele de frontend.

## 2. Funcționalități Cheie

- **Tracking hibrid (Pixel + CAPI):** evenimente client-side combinate cu evenimente server-side pentru acuratețe maximă.
- **Advanced Matching:** trimite date de utilizator hash-uite SHA-256 (email, telefon) pentru a crește rata de potrivire (Event Match Quality).
- **Identificare produs centralizată:** folosește `Item ID Type` global (Product Variant ID / Template ID / SKU) pentru potrivirea cu Catalogul Meta.
- **Evenimente standard:** `PageView`, `ViewContent`, `AddToCart`, `Search`, `InitiateCheckout`, `AddPaymentInfo`, `Purchase`, plus lead-uri (`Contact`, `Lead`).
- **Lead generation:** urmărește clicurile pe numere de telefon (`tel:`) și trimiterile de formulare; CAPI pentru lead-uri noi din CRM.
- **CAPI asincron:** evenimentele server-side se trimit în thread-uri de fundal, fără impact asupra performanței site-ului.

## 3. Dependențe

- `website_sale`
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)
- `crm`

## 4. Componente Cheie

### Modele

- `website`: extins cu `facebook_pixel_code`, `facebook_capi_token`, helperul `_hash_data` și `_send_facebook_capi_event` (trimitere CAPI asincronă).
- `res.config.settings`: expune codul de pixel și token-ul CAPI în configurarea website-ului.
- `sale.order`: la `action_confirm` trimite evenimentul `Purchase` prin CAPI.
- `crm.lead`: hook pe `create` pentru evenimentul `Lead` via CAPI.

### Vizualizări / JS

- `views/res_config_settings_views.xml`: setările Facebook Pixel/CAPI.
- `views/website_templates.xml`: injectează scriptul de pixel Meta și extinde pagina de confirmare comandă.
- `static/src/js/facebook_pixel.esm.js`: interaction `FacebookPixel` (framework Odoo 19 Interactions) care ascultă evenimentele core (`view_item_event`, `add_to_cart_event`) și cele normalizate `terrabit_tracking:*`, transmițându-le către `fbq`.

### Teste

- `tests/test_facebook_pixel_tracking.py`: tur HttpCase post_install care verifică ViewContent / AddToCart / InitiateCheckout / AddPaymentInfo / Purchase cu `content_ids` bazate pe SKU.

## 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează magistrala de evenimente normalizate și îmbogățirea payload-ului de tracking.
- [terrabit_tiktok_pixel](../terrabit_tiktok_pixel/index.md): modul-soră pentru TikTok, cu aceeași arhitectură de tracking.
