# Marketplace Delivery addon (localizat la `deltatech_marketplace_delivery/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_delivery`
- **Versiune:** `19.0.0.0.20`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_delivery`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_delivery`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul asociază metodele de livrare ale marketplace-urilor cu curierii din Odoo și păstrează punctul de ridicare (locker) ales de cumpărător, astfel încât fiecare comandă importată dintr-un marketplace ajunge pe curierul potrivit, pregătită pentru expediere. Nu necesită suita de curierat Terrabit: vânzătorii care expediază cu propriul curier pot instala un conector fără ea.

#### 2. Funcționalități Cheie

- Curier corect de la început: fiecare metodă de livrare din marketplace este legată (binding) de un `delivery.carrier` din Odoo, deci comenzile importate sunt gata de expediere la sosire.
- Fără nepotriviri tăcute: dacă marketplace-ul trimite un nume de curier care nu se potrivește exact cu niciun curier existent, comanda cade pe curierul implicit (`delivery.free_delivery_carrier`), iar pe backend se programează o activitate „Curier necunoscut”, ca greșeala să nu se repete neobservată la comenzile următoare.
- Puncte de ridicare păstrate pe comandă: codul lockerului ales la checkout se salvează pe comanda de marketplace (`marketplace_locker`) și se trimite pe AWB, inclusiv pentru comenzile reimportate după confirmare.
- Lockerul se oglindește pe `sale.order.locker` doar dacă este instalată suita de curierat; altfel rămâne pe comanda de marketplace, de unde îl citește payload-ul AWB.
- Codul lockerului este trimis pe AWB indiferent de opțiunea `use_locker` a metodei de livrare, fiindcă provine direct de la cumpărător.
- O singură mapare pentru toate canalele: același binding funcționează cu toți conectorii (Shopify, WooCommerce, eMAG, Magento, PrestaShop, OpenCart, Trendyol etc.).
- Ștergerea unei mape de curier se face doar în Odoo; curierul Odoo și curierul din magazin rămân neatinse, iar o nouă importare poate recrea maparea.
- Fișa consultant conține fluxul pas-cu-pas.

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- `delivery`

#### 4. Componente Cheie

**Modele**

- `marketplace.delivery.carrier`: binding între un curier din marketplace și un `delivery.carrier` Odoo (cod extern în `external_code`); caută curierul după nume și companie, iar la lipsa potrivirii folosește curierul implicit și programează o activitate pe backend. Verifică dubla mapare a aceluiași curier Odoo pe un backend.
- `marketplace.sale.order` (extins): adaugă `marketplace_locker`, codul punctului de ridicare primit de la marketplace; îl înregistrează la prima sosire chiar și pe comenzile marcate `marketplace_no_refresh` și îl oglindește în `sale.order.locker` când câmpul există.
- `delivery.carrier` (extins): `get_order_delivery_details` și `get_picking_delivery_details` completează `ship_to.lockerId` cu lockerul din marketplace; sunt apelate doar de fluxul AWB din `deltatech_delivery`.
- `marketplace.backend.item` (extins): în `models/backend.py`; nu adaugă logică activă (codul este comentat).

**Vizualizări**

- `view_marketplace_delivery_carrier_form`, `view_marketplace_delivery_carrier_tree`, `view_marketplace_delivery_carrier_search`: formular, listă și căutare pentru maparea curierilor.
- `action_delivery_carrier`: acțiunea de listare a mapărilor de curieri.
- `view_marketplace_sale_order_form_locker`: afișează câmpul `marketplace_locker` pe comanda de marketplace, după partener.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): modulul de bază al ecosistemului marketplace.
- [deltatech_delivery](../deltatech_delivery/index.md): suita de curierat; dacă este instalată, apelează metodele care pun lockerul pe AWB (dependență opțională, eliminată din manifest).
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): definește `sale.order.locker`, în care este oglindit lockerul (dependență opțională, eliminată din manifest).
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea stării livrărilor, complementară acestui modul.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md), [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md), [deltatech_marketplace_woocommerce](../deltatech_marketplace_woocommerce/index.md), [deltatech_marketplace_magento](../deltatech_marketplace_magento/index.md), [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md), [deltatech_marketplace_opencart](../deltatech_marketplace_opencart/index.md), [deltatech_marketplace_trendyol](../deltatech_marketplace_trendyol/index.md): conectori care folosesc aceeași mapare de curieri și același câmp de locker.
