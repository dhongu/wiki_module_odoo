# Auto Reorder Rules (localizat la `deltatech_auto_reorder_rule/index.md`)

- **Nume Tehnic:** `deltatech_auto_reorder_rule`
- **Versiune:** `19.0.0.1.11`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_auto_reorder_rule
- **Cale Locală:** odoo-addons/deltatech/deltatech_auto_reorder_rule
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează crearea regulilor de reaprovizionare pentru produse, ca echipa de achiziții și logistică să nu mai definească manual pragurile de stoc pe cataloagele mari. La crearea unui produs nou se generează automat o regulă în fiecare depozit care are opțiunea activată; pentru produsele deja existente, regulile lipsă se pot crea în masă sau cu un asistent care permite cantități proprii. Regulile automate pornesc cu minim și maxim 0 și declanșare manuală, deci fac produsul vizibil în ecranul de reaprovizionare fără să genereze singure cereri de ofertă.

#### 2. Funcționalități Cheie

- Creează automat o regulă de reaprovizionare (`stock.warehouse.orderpoint`) la crearea unui produs, pentru fiecare depozit cu opțiunea **Generate Reorder Rules** activă (implicit activă pe depozitele noi), cu minim 0, maxim 0 și declanșare manuală, pe ruta marcată pentru reguli automate.
- Regulile se creează pentru **orice produs nou**, nu doar pentru cele stocabile (corectat față de pagina veche: în 19.0 nu există filtrare pe tipul produsului). Un produs cu regulă nu mai poate avea listă de materiale de tip kit, deci pentru produsele kit sau nestocate regula trebuie ștearsă.
- Acțiunea **Create rule** (lista de produse): completează în masă regulile lipsă pentru produsele selectate. Fiecare depozit se verifică separat: se creează doar regulile lipsă, cele existente rămân și nu se dublează.
- Acțiunea **Open Rules Wizard** (formularul produsului): creează reguli pentru locații alese, cu **Minimum Quantity**, **Maximum Quantity**, **Trigger** (*Automatic* sau *Manual*) și **Stock Locations**; se creează câte o regulă pentru fiecare variantă și fiecare locație, în compania locației.
- Parametrul de sistem `deltatech_auto_reorder_rule.dont_auto_create_rule` dezactivează crearea automată la salvarea produsului, fără dezinstalarea modulului; doar `True`/`1`/`yes` o dezactivează, `False` o lasă activă.
- Opțiunea **Use This for Auto Rules** pe rută (**Inventar → Configurare → Rute**) stabilește ruta atribuită regulilor automate; dacă nu e setată, regulile se creează fără rută. Opțiunea depozitului se setează în **Inventar → Configurare → Depozite**.
- Regulile create se văd și se completează în **Inventar → Operațiuni → Reaprovizionare**.
- Regulile se creează în compania produsului sau, pentru produsele comune, în compania activă.
- Fișa consultant detaliază configurarea, utilizarea și cazurile frecvente; nu sunt refăcute aici.

#### 3. Dependențe

- `stock`
- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.product` (extins): `create_rule()` creează regulile lipsă pe locația de stoc a fiecărui depozit cu opțiunea activă; `create()` o apelează pentru produsele noi, dacă parametrul de sistem nu o dezactivează.
- `stock.warehouse` (extins): câmpul `generate_reorder_rules`.
- `stock.route` (extins): câmpul `use_this_for_auto_rules`.
- `order.rules.details.wizard` (wizard tranzitoriu): `min_quantity`, `max_quantity`, `stock_location_ids`, `trigger`; `do_create()` creează regulile pe variante și locații.

**Vizualizări**

- `views/stock_warehouse_view.xml`: opțiunea **Generate Reorder Rules** pe formularul depozitului.
- `views/stock_route_view.xml`: opțiunea **Use This for Auto Rules** pe formularul rutei.
- `wizard/order_rules_details_view.xml`: formularul asistentului de reguli.

**Acțiuni Automate / Acțiuni Server**

- `product_action_create_rule` („Create rule”): acțiune server pe `product.template` (meniul Acțiune din listă); apelează `create_rule()` pe variantele produselor selectate.
- `product_action_create_variant_rule` („Open Rules Wizard”): acțiune server pe `product.template`, doar în formular; deschide `order.rules.details.wizard`.
- Nu există cron-uri.

#### 5. Conexiuni

- `stock`, `purchase_stock`, `sale_stock`: modulul se sprijină pe reaprovizionarea nativă Odoo (`stock.warehouse.orderpoint`), cu rute și depozite.
