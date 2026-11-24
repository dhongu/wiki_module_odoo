# Manager Mărci Produse (Product Brand Manager) (localizat la `deltatech_product_brand/index.md`)

- **Nume Tehnic:** `deltatech_product_brand`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_product_brand
- **Cale Locală:** odoo-addons/bitshop/deltatech_product_brand
- **Ultima Ingestie:** `2026-11-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul oferă o listă centralizată de mărci de produs în Odoo, ajutând companiile să-și organizeze catalogul în funcție de marcă. Fiecare marcă are logo, partener asociat (furnizorul sau producătorul) și descriere, iar fiecare produs poate primi o marcă. Din perspectivă de business, produsele pot fi filtrate și grupate pe marcă, iar vânzările și facturile pot fi analizate pe marcă, ceea ce sprijină marketingul și vânzările țintite.

#### 2. Funcționalități Cheie

- Identitate de marcă unificată: o singură listă de mărci (cu logo, partener și descriere), cu o marcă atribuită fiecărui produs.
- Căutare și descoperire îmbunătățite: filtrare și căutare facilă a produselor după marcă (coloana **Brand** în lista de produse, căutare **Search Brand**, grupare după **Brand**; produsele fără marcă cad în grupul **None**).
- Marketing țintit: campanii de marketing și strategii de vânzări specifice pe marcă.
- Analize pe marcă: comenzile de vânzare și facturile clienților pot fi analizate pe marca produsului, în rapoartele *Sales Analysis* și *Invoice Analysis*; produsele, comenzile și facturile create înainte de completarea mărcii apar în grupul **None**.
- Administrare simplă a mărcilor: din **Sales > Configuration > Products > Product Brands** (vizualizare kanban cu logo și numărul de produse; butonul **Products** din formular arată și deschide produsele mărcii). Câmpul **Brand** apare în formularul produsului, sub nume, fără etichetă (gol afișează „Brand"), din **Sales > Products > Products** sau **Inventory > Products > Products**.
- Nu oferă ierarhie de mărci și nici rapoarte de inventar pe marcă.

#### 3. Dependențe

- `sale`

Analiza facturilor pe marcă necesită și aplicația Invoicing.

#### 4. Componente Cheie

*Notă: Conform fluxului de ingestie, Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` și `readme/USAGE.md`. Componentele de mai jos sunt incluse din cod, ca reper de orientare pentru utilizator.*

**Modele**

- `product.brand`: marca de produs — `name` (obligatoriu), `description` (traductibilă), `partner_id` (`res.partner`, `ondelete="restrict"`), `logo`, `product_ids` și `products_count` (calculat).
- `product.template`: extins cu `product_brand_id` (Many2one către `product.brand`, etichetat „Brand"), disponibil în formularul de produs.
- `sale.report` și `account.invoice.report`: extinse (`reports/`) cu marca produsului, pentru grupare în analiza vânzărilor și a facturilor.

**Vizualizări**

- `views/product_brand_view.xml`: administrarea mărcilor (kanban, listă, formular) din **Sales > Configuration > Products > Product Brands**, plus câmpul de marcă în formularul și lista produselor.
- `reports/sale_report_view.xml`: gruparea/dimensionarea după marcă în vizualizarea pivot din **Sales > Reporting > Sales**.
- `reports/account_invoice_report_view.xml`: gruparea/dimensionarea după marcă în **Invoicing > Reporting > Management > Invoice Analysis**.

**Acțiuni Automate / Acțiuni Server**

- Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_brand_field](../deltatech_brand_field/index.md): modul tehnic care citește marca produsului din câmpul indicat în Setări; `product_brand_id` din acest modul este exemplul uzual de câmp indicat.
- [deltatech_marketplace_brand](../deltatech_marketplace_brand/index.md): depinde de acest modul (manifest) și extinde mărcile de produse în contextul marketplace.
