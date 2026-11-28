# Delivery Price by Category (localizat la `deltatech_delivery_category_price/index.md`)

- **Nume Tehnic:** `deltatech_delivery_category_price`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_category_price
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_category_price`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează tarifele de livrare din magazinul online pe baza categoriilor de produse de website ale articolelor din coș, nu pe baza categoriilor contabile (adesea generice) sau a potrivirii fragile după nume. Fiecare metodă de livrare poate avea o listă de tarife pe categorii, iar echipa de vânzări vede clar pe comandă dacă s-a cerut manevrare.

#### 2. Funcționalități Cheie

- **Tarife pe categorii**: preț fix pentru una sau mai multe categorii de website (subcategoriile sunt incluse) sau tarif în funcție de greutate, cu praguri configurabile (*Up to (kg)* și *Price*); se folosește prima treaptă care acoperă greutatea totală a produselor din categoriile tarifului.
- **Cel mai mare tarif, nu suma**: dacă mai multe tarife se potrivesc coșului, se percepe cel mai mare (ex. saltea 300 + pat 350 = 350).
- **Preț implicit**: dacă niciun tarif nu se potrivește (sau greutatea depășește toate treptele și nimic mai mare nu se aplică), se percepe prețul implicit, iar în checkout apare „Communicated before delivery" în loc de „Free"; echipa poate comunica sau împărți manual expedierea.
- **Manevrare opțională**: bifă „Add handling" în checkout, cu taxă configurabilă, adăugată doar peste tarifele fixe pe categorie (nu peste tarifele pe greutate sau prețul implicit); cererea și suma apar pe comanda de vânzare (banner, câmpurile *Delivery handling* și *Handling cost* în tab-ul *Other Info*), suma fiind stocată la momentul comenzii.
- **Configurare**: *Website > Configuration > eCommerce > Delivery Methods* (sau *Sales > Configuration > Sales Orders > Delivery Methods*), **Provider** *Category price (website)*, tab-ul **Category tariffs**; tarifele sunt în moneda companiei și se convertesc pentru liste de prețuri în altă monedă.
- **Limitare**: la tarifele pe greutate coloana *Price* din listă rămâne 0.00, prețurile fiind în treptele de greutate.

#### 3. Dependențe

- `delivery`
- `website_sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar componentele tehnice nu sunt cerute explicit în Readme.

#### 5. Conexiuni

Nu au fost identificate conexiuni cu pagini wiki existente ale altor module.
