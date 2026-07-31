# Deltatech Delivery Category Price (localizat la `deltatech_delivery_category_price/index.md`)

- **Nume Tehnic:** `deltatech_delivery_category_price`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_category_price
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_category_price`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul calculează tariful de livrare pentru comenzile din magazinul online pe baza categoriilor de website ale produselor din coș, nu pe baza categoriilor contabile interne (adesea prea generice, de ex. o singură categorie „Bunuri" pentru tot catalogul) sau a unei potriviri fragile după numele produsului. Astfel, echipa de vânzări poate configura prețuri de transport realiste pentru categorii distincte de produse (de exemplu saltele, paturi), inclusiv tarife pe tranșe de greutate, fără să depindă de structura contabilă a catalogului.

#### 2. Funcționalități Cheie

- Fiecare metodă de livrare poate avea propria listă de tarife pe categorii de website: preț fix pentru una sau mai multe categorii (ex. „Saltele", „Paturi") sau tarif pe tranșe de greutate pentru alte categorii (ex. lenjerie, accesorii).
- Când o comandă se potrivește cu mai multe tarife, se aplică prețul cel mai mare, nu suma lor — evitând dubla taxare atunci când clientul cumpără, de exemplu, atât o saltea cât și un pat în aceeași comandă.
- Dacă nicio configurare de tarif nu se potrivește comenzii (sau greutatea depășește toate tranșele configurate), curierul revine la un preț implicit configurabil, iar pagina de finalizare a comenzii afișează clar „Se comunică înainte de livrare" în loc de mesajul „Gratuit", care ar induce în eroare clientul.
- O bifă opțională „handling" (manipulare) poate fi oferită la finalizarea comenzii, adăugând un supliment configurabil doar peste tarifele fixe pe categorie (nu și peste tarifele pe greutate sau prețul implicit).
- Solicitarea de handling și suma aferentă sunt afișate direct pe comanda de vânzare, pentru vizibilitate completă a echipei de vânzări.

#### 3. Dependențe

- `delivery`
- `website_sale`

#### 4. Componente Cheie

Detaliile componentelor tehnice nu sunt documentate aici, deoarece fișierul `readme/DESCRIPTION.md` acoperă scopul și funcționalitățile modulului și nu solicită explicit analiza codului pentru această secțiune.

#### 5. Conexiuni

Nu au fost identificate conexiuni cu pagini wiki existente ale altor module.
