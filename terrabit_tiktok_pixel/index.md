# Terrabit TikTok Pixel (localizat la `terrabit_tiktok_pixel/index.md`)

- **Nume Tehnic:** `terrabit_tiktok_pixel`
- **Versiune:** `19.0.0.1.10`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_tiktok_pixel
- **Cale Locală:** `odoo-addons/bitshop/terrabit_tiktok_pixel`
- **Ultima Ingestie:** `2026-11-23`

#### 1. Sumar

Trimite vizitele și pașii de cumpărare de pe website-ul Odoo către reclamele **TikTok**, prin TikTok Pixel în browser și, pentru comenzile confirmate, conturile noi și lead-urile din website, prin TikTok Events API (Conversion API) de pe server, astfel încât campaniile să poată fi măsurate și optimizate pe vânzările efectiv realizate. Combină tracking-ul client-side (Pixel) cu evenimente server-side (CAPI). Evenimentele de magazin vin din modulul de fundație `terrabit_website_sale_tracking_base`, de care depinde.

#### 2. Funcționalități Cheie

- **Pixel pe fiecare pagină:** TikTok Pixel se încarcă pe paginile website-ului cu Pixel ID-ul configurat și înregistrează fiecare vizualizare de pagină (`PageView`).
- **Pașii de cumpărare** (din browser, pe paginile magazinului): produs vizualizat (`ViewContent`), produs adăugat în coș (`AddToCart`), căutare de produse (`Search`), început de checkout (`InitiateCheckout`), metodă de plată aleasă (`AddPaymentInfo`) și comanda de pe pagina de confirmare (`CompletePayment`), cu ID-uri de produs, cantități, valoare și monedă.
- **Evenimente de pe server:** cu un token de acces, fiecare comandă de website confirmată în Odoo (`CompletePayment`), fiecare cont nou de client (`CompleteRegistration`) și fiecare lead creat dintr-un formular de website (`SubmitForm`) se trimit și de pe server, deci se numără chiar dacă browserul blochează pixelul. Trimiterea se face asincron, în thread de fundal, fără impact asupra performanței site-ului; datele lipsă (e-mail, telefon) sunt omise, iar liniile de livrare nu se trimit ca produse cumpărate.
- **Potrivire mai bună (Advanced Matching):** pentru un client autentificat, e-mailul și telefonul se trimit hash-uite SHA-256 (`identify`); pe server se adaugă și `external_id` la crearea contului.
- **Contacte și formulare:** pe paginile magazinului se înregistrează clicurile pe numere de telefon (`Contact`) și formularele de website trimise (`SubmitForm`).
- **Identificatori de produs și valoare:** setările comune ale website-ului, din modulul de bază, stabilesc tipul identificatorului de produs (**Item ID Type for Tracking**: ID variantă, ID șablon sau referință internă/SKU, pentru potrivirea cu catalogul TikTok) și dacă transportul se exclude din valoarea achiziției (**Exclude Delivery from Tracking Events**).
- **Configurare:** în **Website → Configurare → Setări** se activează TikTok Pixel și se completează **TikTok Pixel ID** și, opțional, **TikTok Conversion API Token** (Pixel ID din TikTok Ads Manager, *Assets > Events*, iar token-ul se generează pentru Events API). Verificarea: **Test events** din TikTok Events Manager sau extensia TikTok Pixel Helper.
- **Date trimise către TikTok:** din browser, evenimentele de mai sus cu ID-uri, nume, prețuri, cantități și valoarea comenzii, plus e-mailul și telefonul hash-uite ale clientului autentificat; de pe server (cu token), comenzile confirmate, conturile noi și lead-urile din website, cu e-mail și telefon hash-uite.

#### 3. Dependențe

- `crm`
- `website_sale`
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)

#### 4. Componente Cheie

**Modele**

- `website`: extins cu `tiktok_pixel_id`, `tiktok_capi_token`, `tiktok_pixel_exclude_delivery` (legat de `tracking_exclude_delivery`) și helperele `_get_tiktok_user_data`, `_hash_data`, `_tiktok_user_data` și `_send_tiktok_capi_event` (trimitere CAPI asincronă către `business-api.tiktok.com`).
- `res.config.settings`: expune ID-ul de pixel și token-ul CAPI (câmpuri `related` pe website) în configurarea website-ului.
- `sale.order`: la `action_confirm` trimite evenimentul `CompletePayment` prin CAPI, cu `content_id` calculat conform `Item ID Type` (variant/template/SKU).
- `crm.lead`: la `create`, dacă website-ul are `tiktok_capi_token`, trimite evenimentul `SubmitForm` via CAPI cu email/telefon hash-uite, doar pentru lead-urile create din website (website-ul cererii curente).
- `res.users`: la `create`, trimite evenimentul `CompleteRegistration` via CAPI cu email/telefon/external_id hash-uite.

**Vizualizări**

- `res_config_settings_views.xml`: setările TikTok Pixel/CAPI (activare, Pixel ID, token CAPI) în Website > Configurare > Setări, alături de setările comune din modulul de bază.
- `website_templates.xml`: injectează scriptul de pixel TikTok (`ttq`) și apelul inițial `page()`.

**Alte componente**

- `static/src/js/tiktok_pixel.esm.js`: interaction `TiktokPixel` (framework Odoo 19 Interactions, selector `.oe_website_sale`) care ascultă evenimentele core `view_item_event`/`add_to_cart_event` și cele normalizate `terrabit_tracking:*` (begin_checkout, add_payment_info, search, contact, form_submit), transmițându-le către `ttq`; apelează `identify` pentru clientul autentificat.
- `tests/test_tiktok_pixel_tracking.py`: tur `HttpCase` (`post_install`) care verifică `ViewContent`/`AddToCart`/`InitiateCheckout`/`AddPaymentInfo`/`CompletePayment` cu `content_id` bazat pe SKU.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, reguli `base.automation` sau acțiuni server; evenimentele CAPI pornesc din confirmarea comenzii, crearea contului și crearea lead-ului.

#### 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează magistrala de evenimente normalizate (`terrabit_tracking:*`) și îmbogățirea payload-ului de tracking (valoare, monedă, excludere livrare) consumată de acest modul.
- [terrabit_facebook_pixel](../terrabit_facebook_pixel/index.md): modul-soră pentru Meta Pixel/CAPI, cu aceeași arhitectură de tracking hibrid bazată pe `terrabit_website_sale_tracking_base`.
