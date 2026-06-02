# Invoice Product Filter (localizat la `deltatech_invoice_product_filter/index.md`)

- **Nume Tehnic:** `deltatech_invoice_product_filter`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_product_filter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_product_filter`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul adaugă posibilitatea de a căuta facturi după produsul conținut în liniile acestora. În mod standard, lista de facturi din Odoo permite filtrarea după partener, dată sau alte câmpuri de antet, dar nu și după produsele facturate. Modulul completează această lipsă, oferind utilizatorilor din contabilitate o cale rapidă de a regăsi toate facturile în care apare un anumit produs.

#### 2. Funcționalități Cheie

- Adaugă un filtru de căutare după produs în vizualizarea de listă a facturilor.
- Permite regăsirea facturilor pe baza produselor din liniile documentului, nu doar a câmpurilor de antet.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Vizualizări**

- `view_account_invoice_filter`: extinde vizualizarea de căutare standard a facturilor (`account.view_account_invoice_filter`), adăugând după câmpul partener un câmp de filtrare după produs (`line_ids`) cu domeniul `[('line_ids.product_id', 'ilike', self)]`.

#### 5. Conexiuni

Nu au fost identificate conexiuni cu alte module documentate în wiki.
