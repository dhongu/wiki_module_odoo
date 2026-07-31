# Netopia MobilPay Payment Acquirer (localizat la `deltatech_payment_mobilpay/index.md`)

- **Nume Tehnic:** `deltatech_payment_mobilpay`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_mobilpay
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_mobilpay`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul conectează Odoo cu Netopia MobilPay, permițând plăți securizate cu cardul pentru comenzile online și facturile clienților. Este conceput pentru comercianții din România care doresc să centralizeze procesul de vânzare în Odoo, oferind în același timp o experiență de plată locală familiară. Integrarea folosește un flux într-un singur pas: cardul clientului este autorizat și suma este debitată imediat la finalizarea comenzii sau la plata unei facturi, fiind ideală pentru vânzările online unde se dorește colectarea imediată a fondurilor.

#### 2. Funcționalități Cheie

- Oferă opțiunea „Plată cu cardul (Netopia MobilPay)” în timpul finalizării comenzii în Odoo eCommerce.
- Permite clienților să plătească facturile restante direct din portalul de client Odoo.
- Plată cu cardul securizată via Netopia MobilPay printr-un flux prin redirecționare către pagina de plată securizată Netopia.
- Moduri Test și Live cu punctele lor terminale (endpoints) respective (sandbox: `https://sandboxsecure.mobilpay.ro/payment/card/index`, producție: `https://secure.mobilpay.ro/payment/card/index`).
- Puncte terminale de confirmare (IPN) și retur generate automat.
- Integrare cu site-ul web (`website_sale`) și pagina standard de stare a plății (`/payment/status`).
- Câmpuri de configurare pentru Semnătură POS, Cheie API și chei RSA (certificat public / cheie privată), citite în mod securizat de pe înregistrarea procesatorului.
- Verificare opțională a stării la revenire (GetStatus) folosind clientul REST / SDK-ul Netopia, ca alternativă în cazul în care IPN-ul nu a fost încă procesat.
- Urmărirea încercărilor de plată și a stării finale de autorizare pentru comenzi/facturi, cu corelarea automată a tranzacțiilor reușite cu documentele corecte pentru a reduce reconcilierea manuală.

#### 3. Dependențe

- `payment`
- `website_sale`

Dependențe Python externe: `pyjwt` (declarată în manifest); fluxul de verificare a stării utilizează și `netopia-sdk` (vezi `odoo-addons/bitshop/requirements.txt`).

#### 4. Componente Cheie

Documentația de business pentru acest modul provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Componentele tehnice detaliate (modele, vizualizări, acțiuni) nu sunt enumerate aici, deoarece Readme-ul acoperă scopul și funcționalitățile fără a impune analiza codului. Pe scurt, modulul extinde framework-ul standard de plăți Odoo (`payment`) cu un procesator („provider”) dedicat MobilPay și controllere web pentru punctele terminale de confirmare (IPN) și retur.

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de procesatori de plăți, pe care acest modul îl extinde cu procesorul MobilPay.
- `website_sale`: modulul de eCommerce Odoo, prin care metoda de plată MobilPay este disponibilă la checkout.
