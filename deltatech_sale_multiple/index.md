# Sale Qty Multiple (localizat la `deltatech_sale_multiple/index.md`)

- **Nume Tehnic:** `deltatech_sale_multiple`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_multiple`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_multiple`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul permite definirea, la nivel de produs, a unei cantități minime și a unei cantități multiplu pentru vânzare. Atunci când un produs este adăugat pe o comandă de vânzare, cantitatea este verificată și ajustată automat: dacă se introduce mai puțin decât minimul, cantitatea este ridicată la valoarea minimă, iar dacă se folosește un multiplu, vânzarea este permisă doar în pași egali cu acel multiplu. Astfel se respectă regulile comerciale de ambalare și de cantitate minimă de comandă, fără intervenții manuale.

#### 2. Funcționalități Cheie

- Setarea unei cantități minime de vânzare pe produs.
- Setarea unei cantități multiplu pe produs (vânzare permisă doar în multipli ai acestei valori).
- Ajustarea automată a cantității la minim atunci când se încearcă vânzarea sub cantitatea minimă.
- Verificarea respectării multiplului la introducerea cantității pe linia de comandă.
- Dezactivarea verificărilor: dacă valoarea este setată la 0, nici minimul, nici multiplul nu mai sunt verificate.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.template` / `product.product`: extinse cu câmpurile de cantitate minimă și cantitate multiplu folosite la vânzare.
- `sale.order.line`: extins pentru verificarea și ajustarea cantității în funcție de minimul și multiplul definite pe produs.

**Vizualizări**

- `views/product_view.xml`: adaugă pe formularul de produs câmpurile pentru cantitatea minimă și cantitatea multiplu.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate (`ir.cron`), reguli `base.automation` sau acțiuni server (`ir.actions.server`) în acest modul.

#### 5. Conexiuni

- `sale_stock`: modulul standard Odoo de vânzări cu gestiune de stoc, pe care acest modul îl extinde pentru a aplica regulile de cantitate minimă și multiplu.
