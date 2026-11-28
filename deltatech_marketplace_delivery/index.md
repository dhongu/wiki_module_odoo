# Marketplace Delivery addon (localizat la `deltatech_marketplace_delivery/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_delivery`
- **Versiune:** `20.0.0.0.20`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_delivery
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_delivery`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul leagă metodele de livrare ale marketplace-urilor de transportatorii Odoo (`delivery.carrier`) și păstrează punctul de ridicare (locker) ales de cumpărător, astfel încât fiecare comandă importată dintr-un marketplace ajunge pe transportatorul corect, gata de onorat. Funcționează identic pentru toți conectorii (Shopify, WooCommerce, eMAG, Magento, PrestaShop, OpenCart, Trendyol etc.) și nu cere suita de curierat Terrabit.

#### 2. Funcționalități Cheie

- Transportator corect din start: fiecare metodă de livrare din marketplace este legată de un `delivery.carrier`, deci comenzile importate sunt gata de expediere.
- Fără nepotriviri tăcute: când marketplace-ul trimite un curier care nu corespunde niciunui transportator, comanda cade pe transportatorul implicit și se programează o activitate pe backend, în loc ca greșeala să se repete neobservată.
- Punctul de ridicare rămâne cu comanda: codul locker-ului ales la checkout se păstrează pe comanda de marketplace și ajunge pe AWB, inclusiv la comenzile reimportate după confirmare.
- O singură mapare pentru toate canalele: aceeași legătură funcționează pe toți conectorii.
- Amprentă redusă: modulul nu depinde de suita de curierat Terrabit; vânzătorii care expediază cu propriul curier instalează un conector fără ea. Unde suita este instalată, locker-ul se reflectă pe comanda de vânzare și pe AWB.
- Detaliile pas-cu-pas (mapare curieri, activitatea pentru curier necunoscut, câmpul locker) sunt în [Fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- `delivery`

#### 4. Componente Cheie

Documentația de business este preluată din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru componente este omisă, întrucât Readme-ul nu o solicită explicit. La nivel de structură, modulul cuprinde modele în `models/`, vizualizări în `views/` (`delivery_carrier_view.xml`, `sale_order_view.xml`), reguli de acces în `security/ir.access.csv`, migrări și teste.

#### 5. Conexiuni

- [deltatech_marketplace_doraly](../deltatech_marketplace_doraly/index.md): conector care folosește maparea transportatorilor din acest modul.
- [deltatech_delivery](../deltatech_delivery/index.md) și [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): suita de curierat Terrabit; nu sunt dependențe, dar, când sunt instalate, locker-ul comenzii se oglindește pe `sale.order` și ajunge pe AWB.
