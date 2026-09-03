# Terrabit Facebook Pixel (localizat la `terrabit_facebook_pixel/index.md`)

- **Nume Tehnic:** `terrabit_facebook_pixel`
- **Versiune:** `19.0.0.1.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_facebook_pixel
- **Cale Locală:** `odoo-addons/bitshop/terrabit_facebook_pixel`
- **Ultima Ingestie:** 2026-09-03

#### 1. Sumar

Integrare Meta (Facebook) Pixel și Conversion API (CAPI) pentru website-ul Odoo 19, pentru urmărirea acțiunilor vizitatorilor și optimizarea campaniilor publicitare cu acuratețe ridicată a datelor. Combină tracking-ul client-side din browser (Pixel) cu evenimente server-side (CAPI), depășind limitările AdBlocker-elor și ale browserelor. Se bazează pe modulul de fundație `terrabit_website_sale_tracking_base` pentru evenimentele de frontend.

#### 2. Funcționalități Cheie

- **Tracking hibrid (Pixel + CAPI):** evenimente client-side combinate cu evenimente server-side pentru acuratețe maximă.
- **Advanced Matching:** trimite date de utilizator hash-uite SHA-256 (email, telefon) pentru a crește rata de potrivire (Event Match Quality).
- **Identificare produs centralizată:** dropdown-ul `Item ID Type` global oferă trei opțiuni pentru potrivirea cu Catalogul Meta — **Product Variant ID** (implicit, ID-ul variantei), **Product Template ID** (ID-ul produsului template) sau **Internal Reference SKU** (`default_code`, cu fallback pe ID dacă produsul nu are SKU).
- **Exclude Delivery:** comutator care, activat, scade costul de livrare din parametrul `value` trimis către Facebook, astfel încât valoarea de conversie raportată să reflecte doar produsele.
- **Evenimente standard:** `PageView`, `ViewContent`, `AddToCart`, `RemoveFromCart`, `Search`, `InitiateCheckout`, `AddPaymentInfo`, `Purchase`, `CompleteRegistration`, `Login`, `AddToWishlist`, plus lead-uri (`Contact`, `Lead`).
- **Lead generation:** urmărește clicurile pe numere de telefon (`tel:`) și trimiterile de formulare (ex. pagina de contact); CAPI pentru lead-uri noi create în CRM.
- **CAPI asincron:** evenimentele server-side se trimit în thread-uri de fundal, fără impact asupra performanței site-ului.
- **Configurare:** din **Website > Configuration > Settings**, secțiunea *Google Analytics* — se bifează „Facebook Pixel" și se completează Pixel ID și tokenul Conversion API; opțiunile `Item ID Type` și `Exclude Delivery` se găsesc în aceleași setări de tracking global, sub secțiunea *SEO*.
- **Verificare:** evenimentele Pixel se verifică cu extensia Chrome „Meta Pixel Helper", iar sosirea evenimentelor CAPI se confirmă în Events Manager din Meta Business Suite.

#### 3. Dependențe

- `website_sale`
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)
- `crm`

#### 4. Componente Cheie

**Modele**

- `website`: extins cu `facebook_pixel_code`, `facebook_capi_token`, helperul `_hash_data` și `_send_facebook_capi_event` (trimitere CAPI asincronă).
- `res.config.settings`: expune codul de pixel și token-ul CAPI în configurarea website-ului.
- `sale.order`: la `action_confirm` trimite evenimentul `Purchase` prin CAPI.
- `crm.lead`: hook pe `create` pentru evenimentul `Lead` via CAPI.

**Vizualizări**

- `views/res_config_settings_views.xml`: setările Facebook Pixel/CAPI (Website > Configuration > Settings).
- `views/website_templates.xml`: injectează scriptul de pixel Meta și extinde pagina de confirmare comandă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul; trimiterea evenimentelor CAPI se face sincron din fluxul de execuție (thread de fundal la `action_confirm` pe `sale.order` și la `create` pe `crm.lead`), nu prin programator.

#### 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează magistrala de evenimente normalizate și îmbogățirea payload-ului de tracking.
- [terrabit_tiktok_pixel](../terrabit_tiktok_pixel/index.md): modul-soră pentru TikTok, cu aceeași arhitectură de tracking.
