# Extended Marketplace Connector (localizat la `deltatech_marketplace_extended/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_extended`
- **Versiune:** `19.0.0.0.8`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_marketplace_extended`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_extended`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul este un conector specific care leagă platforma de e-commerce externă „Extended" de Odoo, folosind cadrul generic de marketplace al suitei Terrabit. El adaugă providerul „Extended" în lista de conectori de marketplace și permite sincronizarea automată, în ambele sensuri, a datelor comerciale: produse, clienți, comenzi, curieri de livrare, metode de plată, categorii publice de site și etape de vânzare. Astfel, magazinul online Extended și sistemul Odoo rămân aliniate, iar comenzile primite de pe platformă ajung direct în fluxul de vânzări din Odoo, inclusiv printr-un webhook care preia comenzile în timp real.

#### 2. Funcționalități Cheie

- Adaugă providerul „Extended" la configurarea backend-ului de marketplace, cu opțiuni proprii (data de start a importului și numărul de produse importate).
- Import de produse de pe platforma Extended, paginat și procesat asincron prin cozi de joburi.
- Import de clienți pe intervale de timp (segmente de 15 zile), pornind de la o dată configurabilă.
- Import de comenzi de vânzare, cu posibilitatea de preluare în timp real prin webhook (la primirea unui `order_id`).
- Sincronizarea curierilor de livrare și a metodelor de plată între Extended și Odoo (cu mapare către produse de tip serviciu, respectiv către providerul de plată prin transfer bancar).
- Import al categoriilor publice de site (arborescent, cu păstrarea ierarhiei părinte-copil) și al etapelor/statusurilor de vânzare.
- Comunicare cu API-ul Extended pe bază de cheie API, cu documentație publicată (specificație Swagger / webhook API).

#### 3. Dependențe

- `sale`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `deltatech_marketplace_sale`
- `deltatech_marketplace_website`
- `deltatech_marketplace_delivery`
- `deltatech_marketplace_payment`
- `deltatech_marketplace_sale_stage`

#### 4. Componente Cheie

**Modele**

- `marketplace.backend` (extins): adaugă providerul `extended`, câmpurile `extended_start_date` și `extended_products_number`, metoda de apel API `extended_call` (autentificare cu `apikey`) și lista de tipuri de elemente sincronizabile.
- `marketplace.product` (extins): import paginat și export de produse către/din Extended.
- `marketplace.customer` (extins): import de clienți pe intervale de date prin joburi asincrone.
- `marketplace.sale.order` (extins): import comenzi și endpoint de webhook (`extended_webhook`) pentru preluarea comenzilor în timp real.
- `marketplace.delivery.carrier` (extins): mapare a curierilor Extended către curieri/produse serviciu Odoo.
- `marketplace.payment.provider` (extins): mapare a metodelor de plată Extended (implicit către providerul de transfer bancar).
- `marketplace.public.category` (extins): import recursiv al categoriilor publice de site, cu păstrarea ierarhiei.
- `marketplace.sale.phase` (extins): import al statusurilor/etapelor de vânzare.

**Vizualizări**

- `view_marketplace_backend_form`: extinde formularul backend-ului de marketplace pentru a afișa câmpurile specifice Extended (`extended_start_date`, `extended_products_number`), vizibile doar când providerul este `extended`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite înregistrări `ir.cron`, `base.automation` sau `ir.actions.server` proprii în acest modul. Sincronizarea se realizează prin joburi în coadă (`with_delay`) și prin webhook, declanșate din cadrul generic de marketplace.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază al familiei de marketplace; furnizează modelul `marketplace.backend` și mecanica generică de conectare extinsă aici pentru providerul „Extended".
