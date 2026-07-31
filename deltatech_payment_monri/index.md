# Monri (Payten) Payment Provider (localizat la `deltatech_payment_monri/index.md`)

- **Nume Tehnic:** `deltatech_payment_monri`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_monri
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_monri`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul conectează Odoo la procesatorul de plăți **Monri WebPay** (parte din grupul Payten), permițând clienților să plătească comenzile printr-un flux de redirecționare către pagina securizată Monri, cu confirmarea automată a statusului plății printr-un callback server-to-server. Modulul se află în stadiu **Alpha**: fluxul de redirecționare este implementat pe baza documentației Monri și a unui plugin WooCommerce open-source de referință, dar trebuie validat integral pe contul de test Monri înainte de a fi folosit în producție.

#### 2. Funcționalități Cheie

- Plată prin redirecționare securizată către pagina Monri WebPay (formular auto-submit către `/v2/form`), separat pentru mediul de test și cel de producție.
- Confirmare automată a statusului plății prin callback server-to-server (webhook `WP3-callback`), verificat criptografic (digest SHA-512 cu cheia de comerciant).
- Verificare suplimentară a digest-ului la revenirea clientului în browser (`/payment/monri/return`), ca strat secundar față de callback-ul autoritativ.
- Suport pentru capturare manuală a plății (`authorize` + captură ulterioară) și pentru rambursare parțială, prin API-ul XML de tranzacții Monri (`capture`/`void`/`refund`).
- Configurare dedicată în formularul furnizorului de plată pentru credențialele Monri (`monri_authenticity_token`, `monri_merchant_key`).
- Mesaje personalizabile pentru stările plății (în așteptare, autorizat, finalizat, anulat), traductibile prin i18n.

#### 3. Dependențe

- `account`
- `payment`

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): adaugă codul `monri`, câmpurile de credențiale (`monri_merchant_key`, `monri_authenticity_token`), calculul digest-urilor (cerere, retur, callback, API) și apelul către API-ul XML de tranzacții Monri pentru `capture`/`void`/`refund`.
- `payment.transaction` (extins): construiește valorile formularului de redirecționare (`_get_specific_rendering_values`), extrage referința tranzacției din datele Monri, mapează codurile de răspuns Monri pe stările Odoo (`done`/`authorized`/`canceled`) și trimite cererile de capturare/anulare/rambursare către API-ul Monri.
- `account.payment.method` (extins): înregistrează metoda de plată `monri` ca fiind de tip `multi`, restricționată la conturi bancare.

**Vizualizări**

- `payment_provider_form` (extindere a `payment.payment_provider_form`): expune câmpurile `monri_authenticity_token` și `monri_merchant_key` (parolă) în formularul furnizorului, vizibile doar când codul e `monri`.
- Șablonul QWeb din `views/payment_monri_templates.xml`: formularul HTML auto-submit folosit pentru redirecționarea către Monri.

**Controllere**

- `/payment/monri/return` (GET/POST, public): tratează revenirea din browser, verifică digest-ul de retur și declanșează procesarea tranzacției.
- `/payment/monri/webhook` (POST, public): tratează callback-ul server-to-server autoritativ, verifică digest-ul din antetul `Authorization: WP3-callback` și confirmă statusul tranzacției.

**Date**

- `data/payment_provider_data.xml`: înregistrează furnizorul de plată „Monri (Payten)" cu metoda de plată asociată și mesajele personalizate pentru client.
- `data/payment_method_data.xml`: definește metoda de plată `monri`.

#### 5. Conexiuni

- [deltatech_payment](../deltatech_payment/index.md): modul din suita de plăți Terrabit, parte din același ecosistem de procesare a plăților (confirmare comandă la plată parțială).
- [deltatech_payment_revolut](../deltatech_payment_revolut/index.md): conector de plată din aceeași familie `deltatech_payment_*`, cu flux de redirecționare similar.
- [deltatech_payment_mobilpay](../deltatech_payment_mobilpay/index.md): conector de plată din aceeași familie `deltatech_payment_*`, cu flux de redirecționare similar.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularul de livrare și plată pe website, context în care se folosesc furnizorii de plată precum Monri.
