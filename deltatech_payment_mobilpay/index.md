# NETOPIA Payments (MobilPay) Payment Provider (localizat la `deltatech_payment_mobilpay/index.md`)

- **Nume Tehnic:** `deltatech_payment_mobilpay`
- **Versiune:** `20.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_mobilpay
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_mobilpay`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite plățile cu cardul, Google Pay și Apple Pay în Odoo prin NETOPIA Payments (fost MobilPay), procesatorul românesc de plăți: la checkout-ul magazinului online, pentru facturile și comenzile plătite din portal și prin linkuri de plată trimise pe e-mail. Este gândit pentru comercianții din România care vor o pagină de plată locală, familiară clienților. Cardul este autorizat și debitat dintr-un singur pas, iar datele cardului nu ajung în Odoo.

#### 2. Funcționalități Cheie

- **Card, Google Pay și Apple Pay**: clientul alege NETOPIA Payments la checkout și plătește pe pagina securizată NETOPIA; Google Pay și Apple Pay apar după ce NETOPIA le activează pe contul de comerciant. Logourile lor din dreptul opțiunii sunt mărci ale metodei de plată și pot fi dezactivate (fila **Payment Methods** a furnizorului, apoi fila **Brands**).
- **Facturi și comenzi plătite din portal**: se pot achita online cu **Pay Now**.
- **Linkuri de plată**: pentru o comandă sau o factură se poate trimite clientului un link (**Generate a Payment Link**) care deschide aceeași plată NETOPIA.
- **Încasare imediată** și **confirmare automată**: NETOPIA notifică Odoo, iar comanda este confirmată sau factura marcată ca plătită, fără reconciliere manuală.
- **Notificări verificate**: fiecare notificare este verificată cu cheia publică NETOPIA; dacă nu poate fi verificată, Odoo cere direct statusul plății de la NETOPIA.
- **Moduri test și live**: sandbox NETOPIA, apoi producție (**Live**).
- Configurare (**Invoicing → Configuration → Online Payments → MobilPay**, fila **Configuration**, secțiunea **Credentials**): **Signature** (semnătura POS), **API Key** și **NETOPIA Public Key** (cheia publică PEM, nu certificatul `.cer` din vechiul API MobilPay; Odoo avertizează dacă fișierul nu este o cheie publică utilizabilă), plus **Payment Journal**.
- Contabilitate: nota plății debitează contul de decontare și creditează creanța clientului; se recomandă un cont dedicat sumelor aflate la NETOPIA (în România, analitic de 5125) la **Outstanding Receipts accounts**, iar comisionul se contabilizează din factura NETOPIA.
- La card refuzat, tranzacția trece în **Error** cu motivul băncii, iar comanda rămâne ofertă.
- Limite: cardurile nu sunt salvate în Odoo, deci reînnoirile de abonament nu se încasează automat; rambursările se fac din contul de comerciant NETOPIA; plata prin SMS nu este acoperită.
- Fluxul pas-cu-pas, cu capturi, este în [Fișa Consultant](FISA_CONSULTANT.md).

Cerințe: pachetele Python `netopia-sdk` (instalat cu `pip install --no-deps netopia-sdk`), `PyJWT` și `cryptography`.

#### 3. Dependențe

- `payment`
- `website_sale`

Dependențe Python externe declarate în manifest: `pyjwt`, `cryptography`; `netopia-sdk` se instalează manual, fără dependențe.

#### 4. Componente Cheie

Documentația provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Pe scurt, modulul extinde framework-ul standard de plăți cu un furnizor NETOPIA (`models/payment_provider.py`, `models/payment_transaction.py`, `models/account_payment_method.py`), controllere pentru confirmare și retur (`controllers/`) și date inițiale pentru furnizor și metodele de plată (`payment_acquirer_mobilpay`, `payment_method_mobilpay`, `payment_method_mobilpay_card`, `payment_method_mobilpay_google_pay`, `payment_method_mobilpay_apple_pay`).

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de furnizori de plăți, extins cu NETOPIA.
- `website_sale`: modulul de eCommerce prin care metoda de plată este disponibilă la checkout.
