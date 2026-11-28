# Viva.com Payment Provider

- **Nume Tehnic:** `deltatech_payment_viva`
- **Versiune:** `20.0.0.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_viva
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_viva`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite încasarea plăților online din magazinul Odoo prin Viva.com Smart Checkout, pagina de plată găzduită de Viva.com. Comunică direct cu API-ul Viva.com, cu contul propriu al firmei, fără server intermediar și fără comision per tranzacție peste cel al Viva.com. Plata nu este considerată reușită pe baza browserului sau a webhook-ului singur: tranzacția este citită din API-ul Viva.com și i se verifică comanda, suma și moneda înainte de confirmare.

#### 2. Funcționalități Cheie

- **Redirecționare Smart Checkout**: clientul plătește pe pagina Viva.com, cu card, Apple Pay, Google Pay și alte metode active în contul Viva.com.
- **Plăți verificate**: confirmarea se face doar după verificarea în API a comenzii, sumei și monedei.
- **Webhook-uri**: notificările *Transaction Payment Created* și *Transaction Failed* confirmă plățile neterminate în browser (tab închis, metode asincrone).
- **Rambursări**: totale sau parțiale, din plata contabilă (butonul **Refund**), trimise la Viva.com prin API; rambursarea apare ca tranzacție copil cu sumă negativă.
- **Date client**: țara și limba clientului sunt trimise către Viva.com.
- **Mediu de test**: cont demo Viva.com cu **Live** debifat.
- **Monede**: CZK, DKK, EUR, GBP, HUF, PLN, RON și SEK.
- **Configurare în Viva.com**: sursă de plată cu URL de succes și de eșec `https://<site>/payment/viva/return`, credențiale Smart Checkout (Client ID, Client Secret), Merchant ID și API Key, două webhook-uri cu URL-ul afișat pe furnizor.
- **Configurare în Odoo**: **Accounting > Configuration > Payment Providers > Viva.com**, tab **Credentials** (Client ID, Client Secret, Merchant ID, API Key, Source Code); furnizorul se publică pentru a apărea la checkout.
- **Contabilitate**: tranzacția confirmată creează plata în jurnalul furnizorului (**In Process** până la reconcilierea cu extrasul); comisionul Viva.com se înregistrează la reconciliere.
- Nu sunt incluse preautorizările, plățile recurente și tokenizarea cardurilor.

Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `account_payment`
- `payment`

#### 4. Componente Cheie

**Modele**

- `payment.provider`: extins cu codul Viva.com, credențialele și URL-ul de webhook.
- `payment.transaction`: inițiază plata, verifică tranzacția în API și procesează rambursările.
- `account.payment.method`: metoda de plată a furnizorului.

**Vizualizări**

- `views/payment_views.xml`: formularul furnizorului (tab Credentials).
- `views/payment_viva_templates.xml`: șabloanele de redirecționare.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni programate; `data/payment_provider_data.xml` și `data/payment_method_data.xml` creează furnizorul și metoda de plată, iar `post_init_hook` / `uninstall_hook` le pregătesc la instalare/dezinstalare.

#### 5. Conexiuni

- `website_sale`: checkout-ul magazinului online în care apare Viva.com.
