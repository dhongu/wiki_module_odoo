# Deltatech Payment (localizat la `deltatech_payment/index.md`)

- **Nume Tehnic:** `deltatech_payment`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul ajustează comportamentul tranzacțiilor de plată din Odoo astfel încât o comandă de vânzare să poată fi confirmată automat atunci când clientul efectuează o plată parțială, nu doar la plata integrală. Pe lângă aceasta, modulul introduce un parametru de configurare care permite confirmarea comenzii de vânzare fără a marca tranzacția de plată ca finalizată. Este o personalizare de gateway de plată (nu un modul de bază pentru gateway-uri propriu-zise), utilă în scenarii de e-commerce unde se acceptă avansuri sau plăți parțiale.

#### 2. Funcționalități Cheie

- Confirmă comanda de vânzare dacă este efectuată o plată parțială (chiar dacă suma plătită nu acoperă întreaga valoare a comenzii).
- Permite, prin parametrul `payment.do_not_set_transaction_done`, confirmarea comenzii de vânzare fără ca tranzacția de plată să mai fie trecută în starea „done".

#### 3. Dependențe

- `payment`

#### 4. Componente Cheie

Notă: secțiunea include doar componenta menționată explicit în Readme (parametrul de configurare și logica asociată).

**Modele**

- `payment.transaction` (extins): suprascrie `_check_amount_and_confirm_order` pentru a confirma comenzile de vânzare aflate în starea `draft`/`sent` când suma plătită este pozitivă; suprascrie `_set_transaction_done` pentru a respecta parametrul de sistem `payment.do_not_set_transaction_done`.

**Parametri de configurare**

- `payment.do_not_set_transaction_done`: dacă este `True`, tranzacțiile de plată nu mai sunt trecute în starea „done", dar comenzile de vânzare asociate sunt confirmate.

#### 5. Conexiuni

- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularele de livrare și plată din magazinul online, context tipic în care se aplică confirmarea comenzii la plată parțială.
