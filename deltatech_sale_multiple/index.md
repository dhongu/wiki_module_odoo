# Sale Qty Multiple (localizat la `deltatech_sale_multiple/index.md`)

- **Nume Tehnic:** `deltatech_sale_multiple`
- **Versiune:** `19.0.1.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_multiple`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_multiple`
- **Ultima Ingestie:** `2026-08-20`

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

- `product.template`: expune câmpurile calculate `qty_multiple` și `qty_minim` (sincronizate cu varianta unică a produsului, dacă există o singură variantă).
- `product.product`: extins cu câmpurile stocate `qty_multiple` și `qty_minim`, constrângeri de non-negativitate (SQL și Python), și metodele de logică `_get_sale_quantity_rules`, `_normalize_sale_quantity` (rotunjire în sus la minim/multiplu) și `_valid_sale_quantity_at_most` (cea mai mare cantitate validă care nu depășește o valoare dată).
- `sale.order.line`: extins pentru a normaliza `product_uom_qty` la `create`, `write` și la onchange-ul `product_uom_qty`/`product_id`/`product_uom_id`, folosind regulile definite pe produs; păstrează metoda de compatibilitate `fix_qty_multiple`.

**Vizualizări**

- `views/product_view.xml`: adaugă câmpurile `qty_multiple` și `qty_minim` pe formularul de produs (`product.template`, grup „Quantity”, ascuns dacă produsul are variante multiple) și pe formularul rapid al variantei (`product.product`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate (`ir.cron`), reguli `base.automation` sau acțiuni server (`ir.actions.server`) în acest modul.

#### 5. Conexiuni

- `sale_stock`: modulul standard Odoo de vânzări cu gestiune de stoc, pe care acest modul îl extinde pentru a aplica regulile de cantitate minimă și multiplu pe linia de comandă.
