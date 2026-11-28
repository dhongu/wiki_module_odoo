# EuPlatesc.ro Payment (localizat la `deltatech_payment_eu_platesc/index.md`)

- **Nume Tehnic:** `deltatech_payment_eu_platesc`
- **Versiune:** `20.0.0.1.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_eu_platesc
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_eu_platesc`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite încasarea plăților cu cardul (Visa și Mastercard) în Odoo prin EuPlatesc.ro, platforma românească de plăți operată de EuroPayment Services S.R.L., la checkout-ul magazinului online și pentru facturile plătite din portalul clientului. Este gândit pentru comercianții din România care vând online cu Odoo. Clientul plătește pe pagina securizată EuPlatesc.ro, iar Odoo nu primește datele cardului.

#### 2. Funcționalități Cheie

- **Plată cu cardul la checkout**: clientul alege EuPlatesc.ro la confirmarea comenzii și plătește pe pagina securizată a platformei.
- **Facturi plătite din portal**: o factură deschisă se poate achita online cu **Pay Now**.
- **Încasare imediată**: cardul este debitat într-un singur pas, iar comanda sau factura este marcată ca plătită.
- **Confirmare în fundal**: EuPlatesc.ro confirmă plata și server-la-server, deci statusul se actualizează chiar dacă clientul închide browserul.
- **Mesaje semnate**: cererile și răspunsurile sunt semnate cu cheia comerciantului (HMAC-MD5); un răspuns nesemnat sau semnat greșit este respins, iar suma și moneda sunt verificate față de tranzacție.
- Configurare: **Invoicing → Configuration → Online Payments → Payment Providers → EuPlatesc.ro**, fila **Configuration**: **Merchant ID**, cheia EuPlatesc.ro și **Payment Journal**; **Live** debifat înseamnă mod test, iar ambele moduri trimit plata la aceeași adresă (decide contul de comerciant).
- Contabilitate: nota plății debitează contul de decontare și creditează creanța clientului; se recomandă un cont dedicat sumelor aflate la EuPlatesc.ro (în România, analitic de 5125) la **Outstanding Receipts accounts**; comisionul se contabilizează din factura furnizorului.
- La card refuzat, tranzacția trece în **Error** cu mesajul băncii, iar comanda rămâne ofertă. Rambursările se fac din contul EuPlatesc.ro, nu din Odoo.
- Fluxul pas-cu-pas, cu capturi, este în [Fișa Consultant](FISA_CONSULTANT.md).

Cerințe: cont activ de comerciant EuPlatesc.ro, cu Merchant ID și cheie.

#### 3. Dependențe

- `account`
- `payment`

#### 4. Componente Cheie

Documentația provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Pe scurt, modulul extinde framework-ul standard de plăți cu un furnizor EuPlatesc.ro (`models/payment_provider.py`, `models/payment_transaction.py`, `models/account_payment_method.py`), controllere pentru returul clientului și notificarea server-la-server (`controllers/`) și date inițiale (`payment_provider_euplatesc`, `payment_method_eu_platesc`).

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de furnizori de plăți, extins cu EuPlatesc.ro.
- `account`: plățile confirmate creează plăți contabile în jurnalul furnizorului.
