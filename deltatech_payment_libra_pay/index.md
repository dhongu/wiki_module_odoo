# LibraPay Payment (localizat la `deltatech_payment_libra_pay/index.md`)

- **Nume Tehnic:** `deltatech_payment_libra_pay`
- **Versiune:** `20.0.1.0.15`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_libra_pay
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_libra_pay`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite încasarea plăților cu cardul (Visa și Mastercard) în Odoo prin LibraPay, serviciul de plăți online al Libra Internet Bank, la checkout-ul magazinului online și pentru facturile plătite din portalul clientului. Este gândit pentru comercianții din România care vând online cu Odoo. Clientul plătește pe pagina securizată a băncii, iar datele cardului nu ajung în Odoo.

#### 2. Funcționalități Cheie

- **Plată cu cardul la checkout**: clientul alege LibraPay la confirmarea comenzii și plătește pe pagina securizată a băncii.
- **Facturi plătite din portal**: o factură deschisă se poate achita online cu **Pay Now**.
- **Încasare imediată**: cardul este debitat într-un singur pas, iar comanda sau factura este marcată ca plătită.
- **Confirmare în fundal**: LibraPay trimite și o notificare instantanee de plată (IPN), deci statusul se actualizează chiar dacă clientul închide browserul. Adresa de notificare din portalul LibraPay este `https://<domeniul-tău>/payment/libra_pay/ipn`.
- **Mesaje semnate**: cererile și răspunsurile sunt semnate cu cheia comerciantului; un răspuns cu semnătură greșită este respins, iar suma și moneda sunt verificate. Codul de răspuns `00` confirmă plata, orice alt cod trece tranzacția în **Error** cu mesajul băncii.
- **Moduri test și live**: adrese separate pentru mediul de test și cel de producție.
- Configurare (**Accounting → Configuration → Online Payments → Payment Providers**, fila **Configuration**, secțiunea **Credentials**): **Terminal**, cheia Libra Pay (șir hexazecimal), **Merchant name**, **Merchant URL**, **Merchant**, **Merchant Email** și jurnalul. Cheia este stocată în clar pe furnizor, deci formularul trebuie deschis doar de utilizatori de încredere.
- Date trimise la LibraPay: liniile comenzii sau facturii (produs, cantitate, preț, TVA) și datele de contact de facturare și livrare ale clientului.
- Comisionul băncii nu este calculat de modul (se înregistrează la reconcilierea extrasului), iar rambursările se fac din portalul LibraPay.
- Fluxul pas-cu-pas, cu capturi, este în [Fișa Consultant](FISA_CONSULTANT.md).

Cerințe: contract de comerciant LibraPay cu Libra Internet Bank și pachetul Python `phpserialize`.

#### 3. Dependențe

- `payment`
- `website_sale`

Dependență Python externă: `phpserialize`.

#### 4. Componente Cheie

Documentația provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Pe scurt, modulul extinde framework-ul standard de plăți cu un furnizor LibraPay (`models/payment_provider.py`, `models/payment_transaction.py`, `models/account_payment_method.py`), controllere pentru retur și IPN (`controllers/`) și date inițiale (`payment_acquirer_libra_pay`, `payment_method_libra_pay`). Modulul include și scripturi de migrare (`migrations/`).

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de furnizori de plăți, extins cu LibraPay.
- `website_sale`: modulul de eCommerce prin care metoda de plată LibraPay este disponibilă la checkout.
