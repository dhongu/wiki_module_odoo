# ING WebPay Payment Acquirer (localizat la `deltatech_payment_ing_webpay/index.md`)

- **Nume Tehnic:** `deltatech_payment_ing_webpay`
- **Versiune:** `20.0.0.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_ing_webpay
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_ing_webpay`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează Odoo cu ING WebPay, platforma de plăți online cu cardul a ING Bank România, pentru comenzile din magazinul online, facturile din portal și plățile din Point of Sale. Este destinat comercianților din România care vor să centralizeze încasările în Odoo oferind clienților o experiență de plată locală, de încredere. Datele cardului sunt introduse pe pagina ING (cu 3-D Secure 2), iar Odoo nu le stochează.

#### 2. Funcționalități Cheie

- Opțiunea „Plată cu cardul (ING WebPay)” la checkout-ul eCommerce.
- Buton opțional **Google Pay** direct în coș (necesită parametrii gateway Google Pay de la ING): adresa de facturare/livrare vine din portofel, iar metodele de livrare și totalurile se recalculează live.
- Plata facturilor deschise din portalul clientului, prin linkurile standard de plată.
- Plăți cu cardul în **Point of Sale**: clientul scanează codul QR de la casier și plătește pe pagina ING de pe telefon; folosește fluxul standard `pos_online_payment`, fără configurare în acest modul. Se recomandă `deltatech_pos_online_payment`, care împiedică marcarea plății ca efectuată înainte de confirmarea ING.
- Verificare server-la-server a rezultatului (`getOrderStatusExtended.do`); statusul raportat de browser nu este niciodată considerat de încredere. Un job programat sincronizează tranzacțiile nerezolvate (la 5 minute; prima interogare la cel puțin 10 minute de la înregistrare, maximum două încercări automate per comandă).
- Garanții: URL-ul de checkout este validat înainte de redirecționare, o comandă ING deja înregistrată este reutilizată, suma și moneda sunt verificate înainte de confirmare, iar o plată confirmată nu este retrogradată automat de o stare ulterioară de stornare.
- Monede RON și EUR: câte un furnizor per monedă, fiecare cu propriile credențiale ING; **Live** debifat = mediul UAT, bifat = producție. Opțiunea **Send orderNumber** se activează doar dacă ING o cere.
- Pe tranzacție, butonul **Refresh ING Status** interoghează imediat ING. Comisionul ING nu este calculat de modul (se înregistrează la reconcilierea extrasului), iar rambursările se fac din back office-ul ING.
- Fluxul pas-cu-pas, cu capturi, este în [Fișa Consultant](FISA_CONSULTANT.md).

Cerințe: cont de comerciant ING WebPay (UAT sau producție) și credențiale pe monedă; pentru POS, `pos_online_payment` și o metodă de plată POS cu **Online Payment**.

#### 3. Dependențe

- `payment`

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): credențiale ING WebPay, parametrii Google Pay, opțiunea **Send orderNumber**.
- `payment.transaction` (extins): înregistrarea comenzii la ING, verificarea statusului, contorul de încercări automate și butonul **Refresh ING Status**.

**Vizualizări**

- `payment_provider_form_ing_webpay`: formularul furnizorului, cu credențialele și secțiunea Google Pay.
- `payment_transaction_form_ing_webpay`: formularul tranzacției, cu statusul ING și butonul de reîmprospătare.

**Acțiuni Automate / Acțiuni Server**

- `cron_ing_webpay_sync_status`: sincronizează tranzacțiile nerezolvate cu ING, la fiecare 5 minute.

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de furnizori de plăți, extins cu ING WebPay.
- `pos_online_payment`: modulul standard pe care se bazează plata din Point of Sale prin cod QR.
- `deltatech_pos_online_payment`: recomandat pentru POS; blochează marcarea manuală a plății ca efectuată înainte de confirmarea ING.
