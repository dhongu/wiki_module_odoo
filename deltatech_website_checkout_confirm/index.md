# eCommerce Checkout Confirm Order (localizat la `deltatech_website_checkout_confirm/index.md`)

- **Nume Tehnic:** `deltatech_website_checkout_confirm`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_checkout_confirm
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_checkout_confirm`
- **Ultima Ingestie:** `2026-11-06`

#### 1. Sumar

În magazinul online standard Odoo, o comandă plătită prin transfer bancar sau ramburs rămâne cotație după checkout, fiindcă tranzacția este doar în așteptare, iar confirmarea se face mai târziu, manual sau la încasare. Acest modul confirmă comanda imediat ce clientul ajunge pe pagina de confirmare a comenzii, la finalul checkout-ului, astfel încât livrarea și restul fluxului de vânzare pornesc de îndată. Nu adaugă nicio pagină sau buton suplimentar.

#### 2. Funcționalități Cheie

- **Confirmare automată la finalul checkout-ului**: când clientul ajunge pe pagina de confirmare (`/shop/confirmation`), ultima comandă din sesiune este confirmată (starea „Comandă de vânzare”).
- **Metode de plată offline incluse**: o tranzacție în așteptare (`pending`) la un furnizor fără procesare online (transfer bancar, ramburs) este suficientă pentru confirmare. Furnizorii online cer o tranzacție confirmată sau autorizată.
- **Aceleași verificări ca la fluxul standard de plată**: comanda se confirmă doar dacă este încă cotație, nu așteaptă o semnătură online, iar tranzacțiile eligibile, legate doar de această comandă, acoperă suma necesară confirmării (suma integrală sau procentul de preplată setat pe cotație).
- Reîncărcarea paginii pe o comandă deja confirmată nu face nimic.
- Limitare: o tranzacție care plătește mai multe comenzi deodată nu este luată în calcul, ca la post-procesarea standard.
- Descrierea din 19.0.1.0.5 corectează o formulare veche (pas suplimentar de confirmare cu buton): modulul lucrează pe ruta standard, fără pagină suplimentară.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni automate (`data` este gol în manifest). Singura componentă este un controller web, descris după cod, fiindcă DESCRIPTION.md nu îl detaliază la nivel de cod.

**Modele**

- Nu sunt definite modele noi.

**Vizualizări**

- Nu sunt definite vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau acțiuni server. Logica stă în controllerul `WebsiteSaleCheckout` (`controllers/website_sale.py`), care extinde `WebsiteSale`: `shop_payment_confirmation` (ruta `/shop/confirmation`) confirmă comanda din `sale_last_order_id` dacă `_checkout_confirm_can_confirm` o permite (cotație, fără semnătură în așteptare, tranzacții `done`/`authorized` sau `pending` la furnizorii offline `custom` / `on_delivery`, care acoperă suma de prepată necesară).

#### 5. Conexiuni

- `website_sale`: modulul de comerț electronic Odoo al cărui flux de checkout este extins.
