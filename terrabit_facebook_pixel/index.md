# Facebook Pixel (localizat la `terrabit_facebook_pixel/index.md`)

- **Nume Tehnic:** `terrabit_facebook_pixel`
- **Versiune:** `20.0.0.1.10`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/terrabit_facebook_pixel
- **Cale Locală:** `odoo-addons/bitshop/terrabit_facebook_pixel`
- **Ultima Ingestie:** 2026-11-28

#### 1. Sumar

Trimite către **Meta** (reclame Facebook și Instagram) vizitele și pașii de cumpărare de pe website-ul Odoo, prin Meta Pixel din browser și, pentru comenzile confirmate, prin Conversions API de pe server. Astfel campaniile pot fi măsurate și optimizate pe vânzările efectiv realizate, chiar dacă browserul blochează pixelul.

#### 2. Funcționalități Cheie

- **Pixel pe fiecare pagină:** Meta Pixel se încarcă pe paginile website-ului cu Pixel ID-ul tău și înregistrează fiecare vizualizare de pagină (`PageView`).
- **Pașii de cumpărare:** produs vizualizat (`ViewContent`), adăugat în coș (`AddToCart`), căutare (`Search`), început de checkout (`InitiateCheckout`), metodă de plată aleasă (`AddPaymentInfo`) și comanda de pe pagina de confirmare (`Purchase`), cu ID-urile produselor, cantități, valoare și monedă.
- **Purchase de pe server:** cu un token Conversions API, fiecare comandă de website confirmată în Odoo este trimisă și de pe server (`Purchase`), deci este numărată chiar dacă pixelul din browser e blocat.
- **Potrivire mai bună (Advanced Matching):** pentru clientul autentificat, e-mailul și telefonul se trimit hash-uite SHA-256.
- **Contacte și formulare:** clicul pe un număr de telefon (`Contact`) și un formular de website trimis (`Lead`) sunt înregistrate.
- **ID-urile produselor tale:** identificatorul produsului și excluderea transportului din valoare se setează o singură dată, pentru toate modulele de tracking ale website-ului (din `terrabit_website_sale_tracking_base`).
- **Configurare:** din *Website > Configuration > Settings* se activează **Facebook Pixel Tracker** și se completează Pixel ID-ul și, opțional, **Facebook Conversion API Token**. Opțiunile **Item ID Type for Tracking** (ID variantă, ID șablon de produs sau referință internă/SKU, cu ID când SKU e gol) și **Exclude Delivery from Tracking Events** sunt în aceeași pagină de setări.
- **Verificare:** evenimentele din browser se văd în Meta Events Manager (*Test events*) sau cu extensia Meta Pixel Helper; la confirmarea unei comenzi, cu token, apare și un `Purchase` de pe server.
- **Date trimise către Meta:** din browser, evenimentele de mai sus cu ID-uri, nume, prețuri, cantități și valoarea comenzii, plus e-mailul și telefonul hash-uite ale clientului autentificat; de pe server (cu token), comenzile confirmate cu valoare, produse și datele hash-uite ale clientului.

#### 3. Dependențe

- `website_sale`
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)
- `crm`

#### 4. Componente Cheie

**Modele**

- `website`: extins cu codul de pixel, token-ul CAPI și metodele de hash și de trimitere a evenimentelor CAPI.
- `res.config.settings`: expune pixelul și token-ul CAPI în setările website-ului.
- `sale.order`: la confirmare trimite evenimentul `Purchase` prin CAPI.
- `crm.lead`: la creare trimite evenimentul `Lead` prin CAPI.

**Vizualizări**

- `views/res_config_settings_views.xml`: setările Facebook Pixel (Website > Configuration > Settings).
- `views/website_templates.xml`: injectează scriptul Meta Pixel și extinde pagina de confirmare a comenzii.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează evenimentele normalizate și îmbogățirea payload-ului de tracking.
- [terrabit_tiktok_pixel](../terrabit_tiktok_pixel/index.md): modul-soră pentru TikTok, cu aceeași arhitectură de tracking.
