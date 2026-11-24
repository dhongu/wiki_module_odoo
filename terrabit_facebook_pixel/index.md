# Terrabit Facebook Pixel (localizat la `terrabit_facebook_pixel/index.md`)

- **Nume Tehnic:** `terrabit_facebook_pixel`
- **Versiune:** `19.0.0.1.11`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_facebook_pixel
- **Cale Locală:** odoo-addons/bitshop/terrabit_facebook_pixel
- **Ultima Ingestie:** `2026-11-24`

#### 1. Sumar

Trimite vizitele și pașii de cumpărare de pe website-ul Odoo către **Meta** (reclame Facebook și Instagram), prin Meta Pixel din browser și, pentru comenzile confirmate, prin Conversions API (CAPI) de pe server, astfel încât campaniile să poată fi măsurate și optimizate pe vânzările reale. Combină tracking-ul client-side cu evenimentul server-side `Purchase`, care se contorizează chiar dacă browserul blochează pixelul. Evenimentele din magazin vin din modulul de fundație `terrabit_website_sale_tracking_base`.

#### 2. Funcționalități Cheie

- **Pixel pe fiecare pagină:** Meta Pixel se încarcă pe paginile website-ului cu Pixel ID-ul configurat și înregistrează fiecare vizualizare de pagină (`PageView`).
- **Pașii de cumpărare** (pe paginile magazinului): produs vizualizat (`ViewContent`), produs adăugat în coș (`AddToCart`), căutare de produse (`Search`), început de checkout (`InitiateCheckout`), metodă de plată aleasă (`AddPaymentInfo`) și comanda de pe pagina de confirmare (`Purchase`), cu ID-uri de produs, cantități, valoare și monedă.
- **Purchase de pe server:** cu un token Conversions API, fiecare comandă de website confirmată în Odoo (`action_confirm`) este trimisă și către Meta de pe server (`Purchase`), în thread de fundal, fără impact asupra performanței site-ului. Valoarea este aceeași în browser și în CAPI: totalul comenzii sau, când livrarea este exclusă, subtotalul mărfii cu discount, fără taxe; liniile de livrare nu intră în `content_ids` / `contents`.
- **Advanced Matching:** pentru un client autentificat, e-mailul și telefonul se trimit hash-uite SHA-256; o valoare lipsă se omite din `user_data`.
- **Contacte și formulare** (pe paginile magazinului): clic pe un număr de telefon (`Contact`) și trimiterea unui formular de website (`Lead`), doar din browser.
- **Identificare produs centralizată:** setările comune ale modulelor de tracking — **Item ID Type for Tracking** (ID variantă — implicit, ID template sau referință internă SKU, cu ID-ul ca rezervă dacă SKU e gol), pentru potrivirea cu Catalogul Meta, și **Exclude Delivery from Tracking Events** (costul de livrare nu intră în valoarea de achiziție).
- **Configurare:** în Meta Events Manager se copiază **Pixel ID** al dataset-ului și, pentru evenimentele server-side, se generează un token **Conversions API**; în Odoo, la **Website > Configuration > Settings** se activează **Facebook Pixel Tracker**, se completează Pixel ID și, opțional, **Facebook Conversion API Token**. Setările comune se află pe aceeași pagină.
- **Verificare:** evenimentele se văd în *Test events* din Events Manager sau cu extensia de browser Meta Pixel Helper; după confirmarea unei comenzi de website, cu token, `Purchase` din server apare lângă cel din browser.
- **Nu trimite** `RemoveFromCart`, `CompleteRegistration`, `Login` sau `AddToWishlist`; lead-urile CRM nu se trimit prin CAPI (hook-ul de pe `crm.lead` este dezactivat în cod).
- **Date trimise către Meta:** din browser, evenimentele de mai sus cu ID-uri de produs, nume, prețuri, cantități și valoarea comenzii, plus e-mailul și telefonul hash-uite ale clientului autentificat; de pe server (cu token), comenzile de website confirmate, cu valoare, produse și e-mailul/telefonul hash-uite ale clientului.

#### 3. Dependențe

- `website_sale`
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)
- `crm`

#### 4. Componente Cheie

**Modele**

- `website`: extins cu `facebook_pixel_code`, `facebook_capi_token`, `facebook_pixel_exclude_delivery` (legat de `tracking_exclude_delivery`), helperii `_hash_data`, `_facebook_purchase_value`, `_facebook_user_data` și `_send_facebook_capi_event` (trimitere CAPI asincronă, în thread, la `graph.facebook.com`).
- `res.config.settings`: expune codul de pixel și token-ul CAPI în configurarea website-ului.
- `sale.order`: la `action_confirm` trimite evenimentul `Purchase` prin CAPI, pentru comenzile de website, când există token.
- `crm.lead`: suprascrie `create`, dar trimiterea evenimentului `Lead` prin CAPI este comentată în cod (marcată „de rezolvat"), deci nu are efect.

**Vizualizări**

- `views/res_config_settings_views.xml`: setările Facebook Pixel/CAPI (Website > Configuration > Settings).
- `views/website_templates.xml`: injectează scriptul de pixel Meta și extinde pagina de confirmare a comenzii.
- `static/src/js/facebook_pixel.esm.js`: interacțiunea publică de frontend care ascultă evenimentele `website_sale` și pe cele normalizate `terrabit_tracking:*` și le trimite către `fbq`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul; evenimentul CAPI se trimite dintr-un thread de fundal pornit la `action_confirm` pe `sale.order`, nu prin programator.

#### 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează magistrala de evenimente normalizate și îmbogățirea payload-ului de tracking.
- [terrabit_tiktok_pixel](../terrabit_tiktok_pixel/index.md): modul-soră pentru TikTok, cu aceeași arhitectură de tracking.
