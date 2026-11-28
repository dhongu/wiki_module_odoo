# Base pricelist on cost with vat (localizat la `deltatech_pricelist_vat_cost/index.md`)

- **Nume Tehnic:** `deltatech_pricelist_vat_cost`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_pricelist_vat_cost
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist_vat_cost`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă o strategie de preț care pornește de la costul produsului inclusiv TVA. Este util în comerțul cu amănuntul și cu ridicata, unde prețul de vânzare se stabilește față de costul total de achiziție, cu taxe incluse.

#### 2. Funcționalități Cheie

- Câmp nou pe produs, **Cost with VAT**, calculat automat din costul standard și taxa de achiziție implicită a produsului.
- **Cost with VAT** devine bază posibilă pentru regulile de tip **Surcharge** (adaos) din listele de prețuri; eticheta regulii afișează „product cost with VAT".
- Regulile de tip **Discount** nu au selector de bază, deci trecerea unei reguli la Discount readuce baza la prețul de vânzare.
- Utilizare: produsul are Cost și Purchase Tax; în *Sales > Products > Pricelists* (cu setarea Pricelists activă) se adaugă o regulă de tip Surcharge cu baza **Cost with VAT**.

#### 3. Dependențe

- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.pricelist.item`: extins cu baza `standard_price_with_vat` și eticheta aferentă.
- `product.template`, `product.product`: câmpul calculat `standard_price_with_vat`.

**Vizualizări**

- `view_product_template_form`, `view_product_product_form`: afișează Cost with VAT lângă taxele de achiziție.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu există conexiuni verificate cu alte pagini wiki.
