# Revolut Payment Provider (localizat la `deltatech_payment_revolut/index.md`)

- **Nume Tehnic:** `deltatech_payment_revolut`
- **Versiune:** `19.0.0.0.34`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_revolut
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_revolut`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul integrează platforma de plăți Revolut în Odoo, oferind clienților o modalitate sigură și fluidă de a plăti pentru produse sau servicii folosind contul Revolut sau cardurile de credit/debit. Modulul ajută la reducerea numărului de coșuri abandonate în timpul finalizării comenzii, aduce un canal suplimentar de încasare pentru magazinele online și permite returnarea banilor direct din Odoo, fără acces la portalul Revolut. Funcționează în toate țările în care contul Revolut Business poate încasa plăți, indiferent de planul de conturi sau de localizarea fiscală.

#### 2. Funcționalități Cheie

- **Rambursări din Odoo:** rambursări totale sau parțiale, mai multe pe aceeași plată, trimise la Revolut direct din plata clientului. Butonul **Refund** apare cât timp mai există sumă rambursabilă, iar butonul inteligent **Refunds** deschide rambursările făcute. Se creează o tranzacție `R-<referință>` cu sumă negativă, legată de tranzacția sursă: este *Confirmed* când Revolut finalizează rambursarea imediat, altfel rămâne *Pending* până la confirmarea prin webhook; o rambursare respinsă pune tranzacția în *Error*.
- **Flux de plată la alegere:** **Direct (Popup)** sau **Redirect** către pagina securizată de checkout Revolut.
- **Plată expresă Apple Pay și Google Pay** în checkout (nou în 19.0); pentru Apple Pay se încarcă fișierul de domeniu și se apasă **Register domain for Apple Pay**.
- **Integrare prin webhook:** butonul **Generate your webhook** creează webhook-ul pe Revolut (evenimentele `ORDER_COMPLETED` și `ORDER_AUTHORISED`) și salvează secretul de semnare; webhook-urile fără semnătură validă sunt ignorate.
- **Confirmare sigură a plății:** Odoo preia comanda de la Revolut și confirmă plata doar dacă id-ul comenzii, suma și moneda coincid; webhook-ul confirmă plata și dacă clientul închide pagina înainte de întoarcerea în magazin.
- **Captură manuală:** cu opțiunea **Capture Amount Manually**, plata rămâne *Authorized*, iar din tranzacție se alege **Capture Transaction** (doar suma integrală autorizată) sau **Void Transaction**. Dacă Odoo refuză bifarea (metoda de plată nu declară captură manuală), plățile se capturează automat.
- **Contabilitate:** la confirmare se creează plata contabilă pe jurnalul bancar al furnizorului (**Payment Journal**); comisionul Revolut nu este calculat de modul și se înregistrează din raportul Revolut la decontarea încasării.
- **Suport sandbox:** stările **Test Mode** / **Enabled** și chei separate pentru testare.
- **Mesaje personalizabile** pentru stările plății (În așteptare, Autorizat, Finalizat, Anulat).
- **Limbi:** engleză, română, germană, franceză, italiană, spaniolă, olandeză, poloneză, portugheză (traducerile în afară de engleză și română sunt asistate de AI).

Configurare: **Accounting > Configuration > Online Payments > Payment Providers > Revolut**; pe tabul **Credentials** se completează cheia secretă (**Revolut Api Key**) și cheia publică (**Revolut Public Key**), pe tabul **Configuration** se alege **Payment Journal**. Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `account`
- `payment`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de componente sunt omise deoarece `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie. (Din manifest reies: un furnizor și o metodă de plată Revolut definite în `data/`, șabloane și view-uri de plată și două scripturi JS pentru checkout: formularul de plată și checkout-ul expres.)

#### 5. Conexiuni

- [deltatech_payment](../deltatech_payment/index.md): modul din suita de plăți Terrabit, parte din același ecosistem de procesare a plăților.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularul de livrare și plată pe website, context în care se folosesc furnizorii de plată precum Revolut.
