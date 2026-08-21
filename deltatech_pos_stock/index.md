# Deltatech POS Stock (localizat la `deltatech_pos_stock/index.md`)

- **Nume Tehnic:** `deltatech_pos_stock`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_stock`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde interfața de Punct de Vânzare (POS) afișând direct pe fișa produsului cantitatea de stoc disponibilă, ajutând astfel casierii să vadă rapid ce produse mai sunt pe stoc chiar în timpul vânzării. Din perspectivă de business, funcționalitatea reduce riscul de a vinde produse epuizate, oferă o imagine clară asupra disponibilității mărfii direct la casă și poate fi activată sau dezactivată în funcție de preferințele fiecărui magazin.

#### 2. Funcționalități Cheie

- **Afișare stoc în timp real:** arată cantitatea disponibilă pentru fiecare produs direct în interfața POS.
- **Afișare preț pe același indicator:** prețul produsului este afișat împreună cu stocul, pe aceeași etichetă (badge).
- **Etichetă (badge) pe imaginea produsului:** informațiile de stoc și preț apar vizual suprapuse pe imaginea produsului din grila POS.
- **Control din setările POS:** vizibilitatea stocului și a prețului poate fi activată/dezactivată din configurarea punctului de vânzare.
- **Compatibilitate cu arhitectura OWL din Odoo 19.**
- **Limitat la produse stocabile:** stocul este afișat doar pentru produsele de tip stocabil, nu pentru servicii sau consumabile.

#### 3. Dependențe

- `point_of_sale`
- `stock`

#### 4. Componente Cheie

Informațiile pentru Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md`, conform fluxului de ingestie; analiza detaliată a codului nu a fost necesară. Pe scurt, modulul extinde modelele `pos.config` și `res.config.settings` (opțiunile de afișare stoc/preț), `product.template` și `stock.quant` (pentru calculul cantității disponibile), iar pe partea de interfață adaugă vizualizarea `views/res_config_settings_views.xml` și componentele OWL din `static/src/js/product_card.esm.js` și `static/src/xml/product_card.xml`, care desenează eticheta de stoc/preț pe cardul produsului în POS.

#### 5. Conexiuni

- `point_of_sale`: modulul de bază al Punctului de Vânzare, a cărui interfață de produse este extinsă.
- `stock`: sursa cantităților de stoc afișate pe cardul produsului.
