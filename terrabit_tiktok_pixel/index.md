# Terrabit TikTok Pixel (localizat la `terrabit_tiktok_pixel/index.md`)

- **Nume Tehnic:** `terrabit_tiktok_pixel`
- **Versiune:** `19.0.0.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_tiktok_pixel
- **Cale Locală:** `odoo-addons/bitshop/terrabit_tiktok_pixel`
- **Ultima Ingestie:** 2026-08-20

#### 1. Sumar

Integrare TikTok Pixel și Conversion API (CAPI) pentru website-ul Odoo 19, pentru urmărirea acțiunilor vizitatorilor și optimizarea campaniilor TikTok (inclusiv Video Shopping Ads) cu acuratețe ridicată a datelor. Combină tracking-ul client-side din browser (Pixel) cu evenimente server-side (CAPI). Se bazează pe modulul de fundație `terrabit_website_sale_tracking_base` pentru evenimentele de frontend.

#### 2. Funcționalități Cheie

- **Tracking hibrid (Pixel + CAPI):** evenimente client-side combinate cu evenimente server-side pentru acuratețe maximă, ocolind AdBlockere și limitările de tracking din browser.
- **Advanced Matching:** hash-uiește (SHA-256) și trimite date de utilizator (email, telefon, external id) pentru creșterea ratei de potrivire în TikTok Ads Manager.
- **Identificare produs centralizată:** folosește setările globale `Item ID Type` (Product Variant ID / Product Template ID / SKU) pentru potrivirea cu Catalogul TikTok — esențial pentru Video Shopping Ads.
- **Acoperire completă de evenimente standard:** `PageView`, `ViewContent`, `AddToCart`, `RemoveFromCart`, `Search`, `InitiateCheckout`, `AddPaymentInfo`, `CompletePayment` (Pixel + CAPI), `CompleteRegistration`, `Login`, `AddToWishlist`.
- **Lead generation:** urmărește pe frontend clicurile pe numere de telefon (`tel:`) și trimiterile de formulare; pe backend trimite evenimente CAPI în timp real la crearea de lead-uri CRM/Contact.
- **Exclude Delivery:** opțiune pentru a scădea costul de livrare din valoarea de conversie raportată către TikTok.
- **CAPI asincron:** evenimentele server-side se trimit în thread-uri de fundal, fără impact asupra performanței site-ului.

#### 3. Dependențe

- `crm`
- [website_sale](../website_sale/index.md)
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)

#### 4. Componente Cheie

**Modele**

- `website`: extins cu `tiktok_pixel_id`, `tiktok_capi_token`, `tiktok_pixel_exclude_delivery` și helperele `_get_tiktok_user_data`, `_hash_data` și `_send_tiktok_capi_event` (trimitere CAPI asincronă către `business-api.tiktok.com`).
- `res.config.settings`: expune ID-ul de pixel și token-ul CAPI (câmpuri `related` pe website) în configurarea website-ului.
- `sale.order`: la `action_confirm` trimite evenimentul `CompletePayment` prin CAPI, cu `content_id` calculat conform `Item ID Type` (variant/template/SKU).
- `crm.lead`: la `create`, dacă website-ul are `tiktok_capi_token`, trimite evenimentul `SubmitForm` via CAPI cu email/telefon hash-uite.
- `res.users`: la `create`, trimite evenimentul `CompleteRegistration` via CAPI cu email/telefon/external_id hash-uite.

**Vizualizări**

- `res_config_settings_views.xml`: setările TikTok Pixel/CAPI (activare, Pixel ID, token CAPI, Item ID Type, Exclude Delivery) în Website > Configurare > Setări.
- `website_templates.xml`: injectează scriptul de pixel TikTok (`ttq`) și apelul inițial `page()`, extinzând pagina de confirmare a comenzii.

**Alte componente**

- `static/src/js/tiktok_pixel.esm.js`: interaction `TiktokPixel` (framework Odoo 19 Interactions, selector `.oe_website_sale`) care ascultă evenimentele core `view_item_event`/`add_to_cart_event` și cele normalizate `terrabit_tracking:*` (begin_checkout, add_payment_info, search, contact, form_submit), transmițându-le către `ttq`.
- `tests/test_tiktok_pixel_tracking.py`: tur `HttpCase` (`post_install`) care verifică `ViewContent`/`AddToCart`/`InitiateCheckout`/`AddPaymentInfo`/`CompletePayment` cu `content_id` bazat pe SKU.

#### 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează magistrala de evenimente normalizate (`terrabit_tracking:*`) și îmbogățirea payload-ului de tracking (valoare, monedă, excludere livrare) consumată de acest modul.
- [terrabit_facebook_pixel](../terrabit_facebook_pixel/index.md): modul-soră pentru Meta Pixel/CAPI, cu aceeași arhitectură de tracking hibrid bazată pe `terrabit_website_sale_tracking_base`.
