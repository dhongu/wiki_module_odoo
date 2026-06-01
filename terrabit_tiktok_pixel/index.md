# Terrabit TikTok Pixel (localizat la `terrabit_tiktok_pixel/index.md`)

- **Nume Tehnic:** `terrabit_tiktok_pixel`
- **Versiune:** `19.0.0.1.1`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/terrabit_tiktok_pixel
- **Cale Locală:** `odoo-addons/bitshop/terrabit_tiktok_pixel`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Integrare TikTok Pixel și Conversion API (CAPI) pentru website-ul Odoo 19, pentru urmărirea acțiunilor vizitatorilor și optimizarea campaniilor TikTok (inclusiv Video Shopping Ads) cu acuratețe ridicată a datelor. Combină tracking-ul client-side din browser (Pixel) cu evenimente server-side (CAPI). Se bazează pe modulul de fundație `terrabit_website_sale_tracking_base` pentru evenimentele de frontend.

## 2. Funcționalități Cheie

- **Tracking hibrid (Pixel + CAPI):** evenimente client-side combinate cu evenimente server-side pentru acuratețe maximă.
- **Advanced Matching:** trimite date de utilizator hash-uite SHA-256 (email, telefon, external id) pentru creșterea ratei de potrivire în TikTok Ads Manager.
- **Identificare produs centralizată:** folosește `Item ID Type` global (Product Variant ID / Template ID / SKU) pentru potrivirea cu Catalogul TikTok — esențial pentru Video Shopping Ads.
- **Evenimente standard:** `Pixel page`, `ViewContent`, `AddToCart`, `Search`, `InitiateCheckout`, `AddPaymentInfo`, `CompletePayment`, plus lead-uri (`Contact`, `SubmitForm`, `CompleteRegistration`).
- **Lead generation:** urmărește clicurile pe numere de telefon (`tel:`) și trimiterile de formulare; CAPI pentru lead-uri/înregistrări noi.
- **CAPI asincron:** evenimentele server-side se trimit în thread-uri de fundal, fără impact asupra performanței site-ului.

## 3. Dependențe

- `website_sale`
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)

## 4. Componente Cheie

### Modele

- `website`: extins cu `tiktok_pixel_id`, `tiktok_capi_token`, helperele `_get_tiktok_user_data`, `_hash_data` și `_send_tiktok_capi_event` (trimitere CAPI asincronă).
- `res.config.settings`: expune ID-ul de pixel și token-ul CAPI în configurarea website-ului.
- `sale.order`: trimite evenimentul `CompletePayment` prin CAPI la confirmarea comenzii.
- `crm.lead`: hook pentru evenimentul `Lead` via CAPI.
- `res.users`: hook pe `create` pentru evenimentul `CompleteRegistration` via CAPI.

### Vizualizări / JS

- `views/res_config_settings_views.xml`: setările TikTok Pixel/CAPI.
- `views/website_templates.xml`: injectează scriptul de pixel TikTok (`ttq`) și extinde pagina de confirmare comandă.
- `static/src/js/tiktok_pixel.esm.js`: interaction `TiktokPixel` (framework Odoo 19 Interactions) care ascultă evenimentele core (`view_item_event`, `add_to_cart_event`) și cele normalizate `terrabit_tracking:*`, transmițându-le către `ttq`.

### Teste

- `tests/test_tiktok_pixel_tracking.py`: tur HttpCase post_install care verifică ViewContent / AddToCart / InitiateCheckout / AddPaymentInfo / CompletePayment cu `content_id` bazat pe SKU.

## 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează magistrala de evenimente normalizate și îmbogățirea payload-ului de tracking.
- [terrabit_facebook_pixel](../terrabit_facebook_pixel/index.md): modul-soră pentru Meta, cu aceeași arhitectură de tracking.
