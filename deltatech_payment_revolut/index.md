# Revolut Payment Provider (localizat la `deltatech_payment_revolut/index.md`)

- **Nume Tehnic:** `deltatech_payment_revolut`
- **Versiune:** `20.0.0.0.34`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_revolut
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_revolut`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul integrează platforma de plăți Revolut în Odoo, oferind clienților o modalitate sigură și fluidă de a plăti cu contul Revolut sau cu cardul de credit/debit. Poate reduce numărul coșurilor abandonate la finalizarea comenzii și aduce un canal suplimentar de încasare pentru magazinele online. Fiind bazat pe Revolut Business, folosit de companii din toată UE, același modul servește magazine din orice țară în care contul Revolut Business încasează plăți.

#### 2. Funcționalități Cheie

- **Două fluxuri de plată**, alese în **Revolut Flow**: **Direct (Popup)**, cu fereastră Revolut deschisă în magazin, sau **Redirect**, către pagina securizată Revolut.
- **Confirmare verificată**: la revenire, Odoo preia comanda de la Revolut și confirmă plata doar dacă ID-ul comenzii, suma și moneda se potrivesc; altfel tranzacția trece în **Eroare**. Webhook-ul confirmă plata și dacă clientul închide pagina înainte de revenire.
- **Webhook generat din Odoo**: butonul **Generate your webhook** creează webhook-ul pe Revolut (`ORDER_COMPLETED`, `ORDER_AUTHORISED`) și stochează secretul de semnare; webhook-urile fără semnătură validă sunt ignorate.
- **Capturare manuală**: cu **Capture Amount Manually** bifat, plata rămâne **Autorizată** și se încasează din **Capture Transaction** (doar suma integrală autorizată) sau se anulează din **Void Transaction**.
- **Apple Pay (express checkout)**: încărcarea fișierului de domeniu Apple Pay și înregistrarea domeniului din formularul furnizorului.
- **Mediu sandbox** (**Live** debifat) pentru teste, apoi producție.
- **Contabilitate**: la confirmare se creează plata contabilă pe jurnalul furnizorului; comisionul Revolut nu este calculat de modul, ci înregistrat la decontarea virămentului, din raportul Revolut.
- **Mesaje personalizabile** pentru stările plății (În așteptare, Autorizat, Finalizat, Anulat).
- Configurare: **Contabilitate > Configurare > Plăți online > Furnizori de plată > Revolut**, fila **Configuration** (**Revolut Api Key** = cheia secretă, **Revolut Public Key**, jurnalul de plată). Fluxul pas-cu-pas e în fișa consultant.

#### 3. Dependențe

- `account`
- `payment`

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): codul `revolut`, cheile API și publică, fluxul (`revolut_flow`), secretul de semnare a webhook-ului și fișierul de domeniu Apple Pay.
- `payment.transaction` (extins): creează comanda la Revolut, verifică ID-ul, suma și moneda la procesare și gestionează capturarea/anularea.
- `account.payment.method` (extins): metoda de plată contabilă Revolut.

**Vizualizări**

- `provider_form_revolut`: câmpurile de credențiale, fluxul, butonul de generare a webhook-ului și secțiunea Apple Pay în formularul furnizorului.
- Șabloane QWeb în `views/payment_templates.xml` și interacțiuni JS (`payment_form.esm.js`, `express_checkout.esm.js`) pentru checkout.

**Controllere**

- `/payment/revolut/return`, `/payment/revolut/return_json`, `/payment/revolut/callback`: revenirea clientului.
- `/payment/revolut/webhook`: webhook-ul semnat; plus ruta fișierului de asociere a domeniului Apple Pay.

**Date**

- `data/payment_provider_data.xml`, `data/payment_method_data.xml`: furnizorul și metodele de plată Revolut.

#### 5. Conexiuni

- [deltatech_payment](../deltatech_payment/index.md): modul din suita de plăți Terrabit, parte din același ecosistem de procesare a plăților.
- [deltatech_payment_monri](../deltatech_payment_monri/index.md): conector din aceeași familie `deltatech_payment_*`.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularul de livrare și plată pe website, context în care se folosesc furnizorii de plată precum Revolut.
