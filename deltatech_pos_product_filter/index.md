# POS Order Product Filter (localizat la `deltatech_pos_product_filter/index.md`)

- **Nume Tehnic:** `deltatech_pos_product_filter`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_product_filter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_product_filter`
- **Ultima Ingestie:** `2026-11-17`

#### 1. Sumar

Personalul din magazin are adesea nevoie să găsească comenzile din Punctul de Vânzare care conțin un anumit articol. Modulul adaugă o opțiune *Product* în căutarea comenzilor POS, astfel încât o comandă poate fi regăsită după ceea ce s-a vândut, fără a parcurge manual liniile fiecărei comenzi.

#### 2. Funcționalități Cheie

- **Opțiunea de căutare *Product*:** la scrierea în caseta de căutare a comenzilor POS apare o opțiune nouă *Product*, plasată imediat după cea pentru partener.
- **Căutare pe liniile comenzii:** opțiunea listează comenzile care au cel puțin o linie al cărei produs se potrivește cu textul introdus; potrivirea este parțială și nu ține cont de majuscule.
- **Doar vizualizarea de căutare:** modulul nu schimbă nimic în afară de această vizualizare — nu are cod Python, câmpuri noi, meniuri sau grupuri de acces. Nu adaugă coloană de produs în listă sau în rapoarte și nu are setări. Din 19.0.1.0.3, bannerul din Apps Store marchează modulul ca fiind compatibil cu Odoo Online (fără cod Python).

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele Python; adaugă doar un filtru de căutare pe modelul existent `pos.order`.

**Vizualizări**

- `view_pos_order_filter`: extinde vizualizarea de căutare standard a comenzilor POS (`point_of_sale.view_pos_order_filter`) cu câmpul *Product* (`lines`), după `partner_id`, cu domeniul `[('lines.product_id', 'ilike', self)]`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `point_of_sale`: singura legătură funcțională reală; modulul extinde vizualizarea de căutare standard a comenzilor POS (`point_of_sale.view_pos_order_filter`). Nu există alte legături verificate în cod sau manifest.
