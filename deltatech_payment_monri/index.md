# Monri (Payten) Payment Provider (localizat la `deltatech_payment_monri/index.md`)

- **Nume Tehnic:** `deltatech_payment_monri`
- **Versiune:** `20.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_monri
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_monri`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează Odoo la procesatorul de plăți **Monri WebPay** (parte din grupul Payten), permițând clienților să plătească comenzile și facturile printr-un flux de redirecționare către pagina securizată Monri, cu confirmarea automată a statusului plății printr-un callback server-to-server. Fluxul este validat pe mediul de test (staging) Monri: trimitere, revenire în browser și callback, inclusiv verificările de digest. Sunt acceptate rambursări parțiale sau totale prin API-ul XML de tranzacții; capturarea manuală nu poate fi activată în această versiune.

#### 2. Funcționalități Cheie

- Plată prin redirecționare securizată către pagina Monri WebPay (formular auto-submit către `/v2/form`), separat pentru mediul de test și cel de producție; pagina Monri se afișează în engleză, spaniolă, bosniacă sau croată, orice altă limbă a clientului revenind la engleză.
- Confirmare automată a statusului plății prin callback server-to-server (webhook `WP3-callback`), verificat criptografic (digest SHA-512 cu cheia de comerciant). Adresa de callback se trimite la Monri odată cu fiecare comandă, deci nu se înregistrează nimic în contul Monri; site-ul trebuie să fie accesibil din internet prin `https`.
- Verificare suplimentară a digest-ului la revenirea clientului în browser (`/payment/monri/return`); oricare dintre cele două căi poate confirma plata, dar doar webhook-ul poartă ID-ul tranzacției Monri și datele băncii.
- Respingerile: dacă Monri a configurat webhook-urile de tip `transaction:purchase:approved` / `declined`, tranzacția respinsă devine **Anulată**, cu motivul în mesajul de stare; fără ele rămâne în **Ciornă**. O notificare tardivă sau dublată nu anulează niciodată o tranzacție confirmată sau autorizată.
- Rambursare parțială sau totală, din butonul **Refund** de pe plata contabilă, prin API-ul Monri; respingerea cu orice cod diferit de `0000` lasă tranzacția de rambursare în **Eroare**. Comisionul Monri nu este calculat de modul, ci înregistrat la reconcilierea extrasului de cont.
- Confirmarea unei tranzacții creează o plată contabilă pe jurnalul furnizorului (în procesare până la reconcilierea cu extrasul); în chatter-ul comenzii sau facturii se înregistrează ID-ul Monri, codul de aprobare, referința băncii și cardul mascat.
- Configurare în **Contabilitate > Configurare > Plăți online > Furnizori de plată > Monri (Payten)**, fila **Configuration**, secțiunea **Credentials**: **Monri Authenticity Token** și **Monri Merchant Key** (mascată, vizibilă doar grupului Settings), jurnalul de plată și restricția de monedă. Credențialele de test și cele de producție sunt diferite.
- Mesaje personalizabile pentru stările plății, traductibile prin i18n.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `account`
- `payment`

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): adaugă codul `monri`, câmpurile de credențiale (`monri_merchant_key`, `monri_authenticity_token`), calculul digest-urilor (cerere, retur, callback, API) și apelul către API-ul XML de tranzacții Monri pentru `capture`/`void`/`refund`; declară suportul de rambursare parțială.
- `payment.transaction` (extins): construiește valorile formularului de redirecționare (`_get_specific_rendering_values`), extrage referința tranzacției din datele Monri, mapează codurile de răspuns pe stările Odoo și trimite cererile de rambursare către API-ul Monri.
- `account.payment.method` (extins): înregistrează metoda de plată `monri`, restricționată la conturi bancare.

**Vizualizări**

- `payment_provider_form` (extindere a `payment.payment_provider_form`): expune câmpurile de credențiale în formularul furnizorului, vizibile doar când codul e `monri`.
- Șablonul QWeb din `views/payment_monri_templates.xml`: formularul HTML auto-submit pentru redirecționarea către Monri.

**Controllere**

- `/payment/monri/return` (GET/POST, public): revenirea din browser, cu verificarea digest-ului de retur.
- `/payment/monri/webhook` (POST, public): callback-ul server-to-server autoritativ, cu verificarea digest-ului din antetul `Authorization: WP3-callback`.

**Date**

- `data/payment_provider_data.xml` și `data/payment_method_data.xml`: furnizorul „Monri (Payten)" și metoda de plată `monri`.

#### 5. Conexiuni

- [deltatech_payment](../deltatech_payment/index.md): modul din suita de plăți Terrabit, parte din același ecosistem de procesare a plăților.
- [deltatech_payment_revolut](../deltatech_payment_revolut/index.md): conector de plată din aceeași familie `deltatech_payment_*`, cu flux de redirecționare similar.
- [deltatech_payment_mobilpay](../deltatech_payment_mobilpay/index.md): conector de plată din aceeași familie `deltatech_payment_*`, cu flux de redirecționare similar.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularul de livrare și plată pe website, context în care se folosesc furnizorii de plată precum Monri.
