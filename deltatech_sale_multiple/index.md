# Sale Qty Multiple (localizat la `deltatech_sale_multiple/index.md`)

- **Nume Tehnic:** `deltatech_sale_multiple`
- **Versiune:** `20.0.1.1.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_multiple
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_multiple`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Acest modul permite definirea, la nivel de produs, a unei cantități minime și a unei cantități multiplu pentru vânzare. Atunci când un produs este adăugat pe o comandă de vânzare, cantitatea este verificată și ajustată automat: dacă se introduce mai puțin decât minimul, cantitatea este ridicată la primul multiplu valid egal sau peste minim, iar dacă se folosește un multiplu, vânzarea este permisă doar în pași egali cu acel multiplu. Astfel se respectă regulile comerciale de ambalare și de cantitate minimă de comandă, fără intervenții manuale.

#### 2. Funcționalități Cheie

- Setarea unei cantități minime de vânzare pe produs.
- Setarea unei cantități multiplu pe produs (vânzare permisă doar în multipli ai acestei valori).
- Regulile se configurează în unitatea de măsură implicită a produsului și sunt convertite automat în unitatea liniei de vânzare.
- Ajustarea automată a cantității: la o valoare sub minim, cantitatea este ridicată la primul multiplu valid egal sau peste minim.
- Un multiplu de 0 sau 1 dezactivează restricția de multiplu; un minim de 0 dezactivează restricția de minim.
- Regulile sunt aplicate consecvent: la onchange-urile din formular, la importuri, la creări/scrieri ORM (unice sau în lot).

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.template`: câmpurile `qty_multiple` și `qty_minim` (sincronizate cu varianta unică a produsului, dacă există o singură variantă).
- `product.product`: câmpurile pe variantă și logica de normalizare a cantității (`_normalize_sale_quantity`, `_get_sale_quantity_rules`).
- `sale.order.line`: `fix_qty_multiple`, aplicat la onchange, `create` și `write`.

**Vizualizări**

- `views/product_view.xml`: câmpurile minim și multiplu pe formularul produsului.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_sale_multiple_website](../deltatech_sale_multiple_website/index.md): aplică aceleași reguli pe comenzile din website (depinde de acest modul).
