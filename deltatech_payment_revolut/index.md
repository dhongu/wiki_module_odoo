# Revolut Payment Provider (localizat la `deltatech_payment_revolut/index.md`)

- **Nume Tehnic:** `deltatech_payment_revolut`
- **Versiune:** `19.0.0.0.19`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_revolut`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_revolut`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul integrează platforma de plăți Revolut în Odoo, oferind clienților o modalitate sigură și fluidă de a plăti pentru produse sau servicii folosind contul lor Revolut sau cardurile de credit/debit. Prin redirecționarea clienților către pagina securizată de checkout Revolut, modulul ajută la reducerea numărului de coșuri abandonate în timpul procesului de finalizare a comenzii și aduce un canal suplimentar de încasare pentru magazinele online.

#### 2. Funcționalități Cheie

- **Plăți prin redirecționare securizată**: redirecționează clienții către pagina de checkout securizată Revolut pentru efectuarea plății.
- **Capturare manuală**: opțiune de capturare manuală a plăților direct din comanda de vânzare.
- **Integrare prin webhook**: sincronizare automată a stării plății prin intermediul webhook-urilor Revolut.
- **Suport sandbox**: testare facilă folosind mediul sandbox al Revolut.
- **Plăți securizate**: complet conform cu procesarea securizată a plăților Revolut.
- **Mesaje personalizabile**: configurarea de mesaje proprii pentru diferitele stări ale plății (În așteptare, Autorizat, Finalizat, Anulat).

#### 3. Dependențe

- `account`
- `payment`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie au fost preluate din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru componente nu a fost efectuată, întrucât Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_payment](../deltatech_payment/index.md): modul din suita de plăți Terrabit, parte din același ecosistem de procesare a plăților.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularul de livrare și plată pe website, context în care se folosesc furnizorii de plată precum Revolut.
