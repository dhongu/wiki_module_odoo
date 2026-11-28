# eCommerce Afișare Preț Fix ca Reducere (localizat la `deltatech_website_fixed_price/index.md`)

- **Nume Tehnic:** `deltatech_website_fixed_price`
- **Versiune:** `20.0.0.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_fixed_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_fixed_price`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul ajustează modul în care magazinul online afișează prețurile atunci când se folosesc reguli de listă de prețuri cu preț fix. În mod implicit, Odoo nu arată prețul tăiat (de comparație) pentru o regulă de preț fix. Modulul îl afișează și în acest caz, dar doar când prețul fix este mai mic decât prețul de referință, astfel încât clientul vede economia reală, fără o „reducere” falsă.

#### 2. Funcționalități Cheie

- Afișează prețul de comparație (barat) și pentru regulile de preț fix din lista de prețuri.
- Baza regulii trebuie să fie un preț pe care clientul îl putea vedea (prețul de vânzare sau altă listă de prețuri), niciodată costul.
- Se aplică doar în magazin (`/shop`), pe pagina produsului și în configuratoare, nu în coș sau checkout.
- Nu necesită configurare: după instalare, regulile de preț fix existente se comportă astfel.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.pricelist.item`: suprascrie `_show_discount_on_shop()`, care returnează adevărat și pentru regulile cu calcul `fixed` și baza `list_price` sau `pricelist`.

**Vizualizări**

Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- `website_sale`: modulul standard de magazin online, ale cărui mecanisme de afișare a reducerilor sunt ajustate de acest modul.
