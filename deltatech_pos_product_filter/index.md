# POS Order Product Filter (localizat la `deltatech_pos_product_filter/index.md`)

- **Nume Tehnic:** `deltatech_pos_product_filter`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_product_filter](https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_product_filter)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_product_filter`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul adaugă posibilitatea de a căuta comenzile din Punctul de Vânzare (POS) direct după produsul vândut, nu doar după client sau alte criterii standard. Este util operatorilor de vânzări și celor din contabilitate care trebuie să regăsească rapid toate bonurile/comenzile POS în care apare un anumit articol, fără a parcurge manual liniile fiecărei comenzi.

#### 2. Funcționalități Cheie

- Căutarea comenzilor POS (`pos.order`) după produsul din liniile comenzii.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

Modulul nu definește sau extinde niciun model Python; adaugă doar un filtru de căutare pe modelul existent `pos.order` (din `point_of_sale`), prin intermediul unui câmp `lines` cu `filter_domain` pe `lines.product_id`.

**Vizualizări**

- `view_pos_order_filter`: extinde vizualizarea de căutare standard a comenzilor POS (`point_of_sale.view_pos_order_filter`), adăugând un câmp de filtrare "Product" imediat după `partner_id`, cu domeniul `[('lines.product_id', 'ilike', self)]`, care permite căutarea comenzilor după numele produsului vândut.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `point_of_sale`: modulul extinde exclusiv vizualizarea de căutare a comenzilor POS oferite de acest modul standard.
