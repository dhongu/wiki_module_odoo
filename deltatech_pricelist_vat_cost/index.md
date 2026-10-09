# Listă de prețuri pe baza costului cu TVA (localizat la `deltatech_pricelist_vat_cost/index.md`)

- **Nume Tehnic:** `deltatech_pricelist_vat_cost`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pricelist_vat_cost
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist_vat_cost`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite calcularea prețurilor de vânzare pornind de la costul produsului la care se adaugă TVA-ul de achiziție. Este util în comerțul cu amănuntul și cu ridicata, unde adaosul se stabilește față de costul total de achiziție, taxe incluse. Costul cu TVA se calculează automat pe produs, iar regulile din listele de prețuri îl pot folosi ca bază de calcul.

#### 2. Funcționalități Cheie

- Câmp calculat „Cost cu TVA" (`standard_price_with_vat`) pe șablonul de produs și pe variantă, afișat în formularul produsului lângă taxele furnizor; pe șablon e ascuns dacă produsul are mai multe variante.
- Calculul aplică taxele de achiziție ale produsului (doar cele ale companiei curente) asupra costului standard; dacă produsul nu are taxe de achiziție sau cost, valoarea rămâne egală cu costul.
- Valoarea se recalculează la schimbarea costului, a monedei, a taxelor de achiziție, a sumei sau tipului taxei și la schimbarea companiei active.
- Opțiune nouă „Cost cu TVA" în câmpul **Bază** al regulilor din listele de prețuri, pentru adaosuri sau reduceri față de costul cu TVA.
- Utilizare: în **Vânzări > Produse > Produse** se completează costul și taxa de achiziție; în **Vânzări > Configurare > Liste de prețuri** se adaugă o regulă cu baza „Cost cu TVA".
- Stare de dezvoltare: Alpha. În `readme/bugs.md` rămâne semnalată problema VATCOST-003 (moneda sursă folosită pentru baza personalizată în multi-companie/multi-monedă).

#### 3. Dependențe

- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.pricelist.item` (extins): adaugă valoarea `standard_price_with_vat` în selecția `base` (`ondelete` = „set default").
- `product.template` (extins): câmpul calculat `standard_price_with_vat`.
- `product.product` (extins): același câmp calculat, la nivel de variantă.

**Vizualizări**

- `view_product_template_form`: moștenește `product.product_template_only_form_view`; adaugă „Cost cu TVA" înaintea taxelor furnizor.
- `view_product_product_form`: moștenește `product.product_normal_form_view`; același câmp pe variantă.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `product`, `sale`: listele de prețuri și produsele standard sunt extinse direct.
