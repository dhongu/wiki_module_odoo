# Confirmare Comandă la Checkout eCommerce (localizat la `deltatech_website_checkout_confirm/index.md`)

- **Nume Tehnic:** `deltatech_website_checkout_confirm`
- **Versiune:** `20.0.1.0.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_checkout_confirm`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_checkout_confirm`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

În eCommerce-ul standard Odoo, o ofertă plătită prin transfer bancar sau ramburs rămâne ofertă după checkout, pentru că tranzacția este doar `pending`, iar comanda se confirmă mai târziu, manual sau la încasarea plății. Modulul confirmă comanda imediat ce clientul ajunge pe pagina de confirmare (`/shop/confirmation`) de la finalul checkout-ului, astfel că livrarea și restul fluxului de vânzare pornesc fără întârziere.

#### 2. Funcționalități Cheie

- **Confirmare automată la finalul checkout-ului:** când clientul ajunge pe pagina de confirmare, ultima comandă din sesiune trece în starea *Sales Order*. Nu există pagină sau buton suplimentar; modulul lucrează pe ruta standard din `website_sale`.
- **Metode de plată offline incluse:** o tranzacție `pending` la un furnizor fără procesare online (transfer bancar, ramburs) este suficientă pentru confirmare; furnizorii online cer în continuare o tranzacție *Confirmed* sau *Authorized*.
- **Aceleași verificări ca fluxul standard de plată:** comanda se confirmă doar dacă este încă ofertă, nu așteaptă semnătură online, iar tranzacțiile eligibile, legate numai de această comandă, acoperă suma cerută (totalul sau procentul de avans de pe ofertă). Reîncărcarea paginii pe o comandă deja confirmată nu face nimic.
- **Limitare:** o tranzacție care plătește mai multe comenzi deodată nu este luată în calcul, la fel ca în post-procesarea standard.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul nu adaugă modele, vizualizări sau acțiuni automate; suprascrie ruta standard prin controllerul `controllers/website_sale.py`.

**Rute (Controllere)**

- `shop_payment_confirmation` (`/shop/confirmation`, extinsă): confirmă comanda când verificările `_checkout_confirm_can_confirm` sunt îndeplinite.

#### 5. Conexiuni

- `website_sale`: modulul de comerț electronic Odoo a cărui rută de confirmare este extinsă.
