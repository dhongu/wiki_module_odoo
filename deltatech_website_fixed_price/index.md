# eCommerce Afișare Preț Fix ca Reducere (localizat la `deltatech_website_fixed_price/index.md`)

- **Nume Tehnic:** `deltatech_website_fixed_price`
- **Versiune:** `19.0.0.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_fixed_price`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_fixed_price`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul ajustează modul în care magazinul online afișează prețurile atunci când se folosesc reguli de listă de prețuri cu preț fix. În mod implicit, Odoo nu arată prețul tăiat (prețul de referință barat) atunci când o regulă de preț fix se aplică unui produs. Modulul face ca prețul de comparație (prețul de listă barat) să fie afișat și în cazul prețurilor fixe, dar numai atunci când prețul fix este efectiv mai mic decât prețul de referință. Astfel, clienții văd clar economia reală, iar comerciantul evită afișarea unei „reduceri” false atunci când prețul fix este de fapt mai mare decât prețul de listă.

#### 2. Funcționalități Cheie

- Afișează prețul de comparație (barat) și atunci când se folosesc reguli de preț fix în lista de prețuri.
- Previne afișarea prețului tăiat atunci când prețul fix este mai mare decât prețul de comparație (comportamentul implicit Odoo nu îl afișa deloc).

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.pricelist.item`: extins pentru a recalcula/expune prețul de comparație astfel încât prețul barat să fie afișat și pentru regulile de preț fix, condiționat de faptul că prețul fix este mai mic decât prețul de referință.

**Vizualizări**

- Modulul nu definește vizualizări proprii (lista `data` din manifest este goală); comportamentul afectează afișarea prețurilor în paginile de eCommerce existente.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `website_sale`: modulul standard Odoo de magazin online, ale cărui mecanisme de afișare a prețurilor și reducerilor sunt ajustate de acest modul.
