# Netopia MobilPay Payment Acquirer (localizat la `deltatech_payment_mobilpay/index.md`)

- **Nume Tehnic:** `deltatech_payment_mobilpay`
- **Versiune:** `19.0.1.3.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_mobilpay
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_mobilpay`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Acest modul conectează Odoo cu Netopia MobilPay (NETOPIA Payments API v2), permițând plăți securizate cu cardul pentru comenzile online și facturile clienților. Este conceput pentru comercianții din România care vând online cu Odoo și vor o pagină de plată locală, familiară clienților. Cardul este autorizat și suma debitată imediat, într-un singur pas, iar rezultatul este confirmat automat de Netopia către Odoo, fără reconciliere manuală.

#### 2. Funcționalități Cheie

- Plată cu cardul prin Netopia MobilPay la finalizarea comenzii în eCommerce: clientul este redirecționat către pagina securizată Netopia.
- Plata facturilor deschise din portalul clientului, cu butonul **Pay Now**.
- Captură imediată: autorizare și debitare într-un singur pas.
- Confirmare automată: comanda sau factura este marcată ca plătită după notificarea (IPN) primită de la Netopia.
- Notificări verificate: IPN-ul (`/payment/mobilpay/notify/<id>`) este acceptat doar cu antet `Verification-token` valid (JWT semnat RS512 cu cheia publică NETOPIA, emitent „NETOPIA Payments”, audiență = semnătura POS, `sub` = SHA-512 în base64 al corpului). Dacă tokenul nu poate fi verificat, corpul primit nu este considerat de încredere, iar Odoo interoghează direct Netopia (GetStatus, cu cheia API, folosind `ntpID` și referința proprii); dacă Netopia nu răspunde, IPN-ul primește o eroare temporară și este retrimis.
- Tranzacția este identificată după `order.orderID` din corpul verificat, care trebuie să corespundă cu id-ul din URL; `ntpID` trebuie să coincidă cu cel de la inițiere. Verificarea sumei și a monedei nu este omisă când IPN-ul nu le conține.
- Statusurile non-finale (nou, deschis, în așteptare, autentificare 3D, verificare fraudă) lasă tranzacția neschimbată până la un status final; fallback-ul GetStatus acoperă și tranzacțiile în eroare, ca o plată făcută după o încercare eșuată să fie recuperată. Un răspuns GetStatus fără status de plată nu mai pune tranzacția în eroare. Codul de eroare „00” („Approved”) nu este tratat ca eșec.
- Metoda `payment.transaction.mobilpay_sync_status()` reprocesează tranzacțiile draft/pending/eroare ale căror IPN s-au pierdut.
- Confirmarea IPN are forma folosită de SDK-ul NETOPIA (`errorType`, `errorCode`, `errorMessage`).
- Moduri Test (sandbox) și Live (producție), cu punctele terminale corespunzătoare (`https://sandboxsecure.mobilpay.ro/payment/card/index`, respectiv `https://secure.mobilpay.ro/payment/card/index`).
- Configurare în *Facturare > Configurare > Procesatori de plată* (MobilPay): **Semnătură** (semnătura POS), **Cheie API** (cheia REST) și **Cheie publică NETOPIA** (cheie publică PEM care semnează notificările, nu certificatul `.cer` al vechiului API v1; formularul avertizează când fișierul încărcat nu este o cheie publică PEM). Stare **Test** pentru sandbox sau **Activat** pentru plăți reale, plus publicarea procesatorului pe site.
- Tranzacțiile, cu referința Netopia, se văd în *Facturare > Configurare > Tranzacții de plată* (mod dezvoltator).
- Integrare cu `website_sale` și cu pagina standard de stare a plății (`/payment/status`).

Cerințe: pachetele Python `netopia-sdk` (instalat cu `pip install --no-deps netopia-sdk`, ca să nu aducă dependențe incompatibile), `PyJWT` și `cryptography`.

#### 3. Dependențe

- `payment`
- `website_sale`

Dependențe Python externe: `pyjwt` și `cryptography` (declarate în manifest); verificarea stării folosește și `netopia-sdk` (vezi `odoo-addons/bitshop/requirements.txt`).

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): adaugă codul „mobilpay” și câmpurile `mobilpay_signature`, `mobilpay_api_key`, `mobilpay_public_cert_id` (cheia publică NETOPIA, atașament); alege endpoint-ul în funcție de stare, verifică tokenul IPN (`_mobilpay_verify_ipn`) și avertizează asupra cheii greșite.
- `payment.transaction` (extins): valorile de redirecționare către Netopia, extragerea referinței și a sumei din IPN, aplicarea statusului (`_apply_updates`), interogarea GetStatus (`_mobilpay_fetch_status`) și `mobilpay_sync_status()`.
- `account.payment.method` (extins): înregistrează metoda de plată MobilPay.

**Vizualizări**

- `acquirer_form_mobilpay`: câmpurile de credențiale în formularul procesatorului de plată.
- `mobilpay_form`: formularul de redirecționare către Netopia.
- `payment_confirmation_status` (moștenește `website_sale.payment_confirmation_status`) și `payment_process_page`: afișarea stării plății după revenire.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau acțiuni server. Controllere web (`controllers/main.py`): `/payment/mobilpay/notify/<transaction_id>` (IPN) și `/payment/mobilpay/return/<provider_id>` (retur client). Înregistrarea procesatorului `payment_acquirer_mobilpay` din `data/payment_acquirer_data.xml` este creată la instalare, cu `post_init_hook` și `uninstall_hook`.

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de procesatori de plăți, extins cu procesorul MobilPay.
- `website_sale`: eCommerce-ul Odoo, prin care metoda MobilPay este disponibilă la checkout și în portal.
