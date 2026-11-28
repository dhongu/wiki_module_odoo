# Auto Reorder Rules (localizat la `deltatech_auto_reorder_rule/index.md`)

- **Nume Tehnic:** `deltatech_auto_reorder_rule`
- **Versiune:** `20.0.0.1.11`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_auto_reorder_rule
- **Cale Locală:** `odoo-addons/deltatech/deltatech_auto_reorder_rule`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează crearea regulilor de reaprovizionare pentru produse. La adăugarea unui produs stocabil nou, generează automat o regulă de reaprovizionare pentru fiecare depozit marcat în acest scop. Pentru produsele existente oferă acțiuni de creare în masă sau cu cantități personalizate. Astfel, echipa de achiziții și logistică are definite pragurile de stoc pentru fiecare produs gestionat, fără pași manuali repetitivi.

#### 2. Funcționalități Cheie

- Creare automată a unei înregistrări `stock.warehouse.orderpoint` pentru fiecare produs stocabil nou, în fiecare depozit cu opțiunea **Generate Reorder Rules** activă (implicit activă la depozitele noi), folosind ruta marcată **Use This for Auto Rules**. Dacă nicio rută nu e marcată, regulile se creează fără rută.
- Acțiunea server **Create rule** (în meniul Acțiune al listei de produse) creează reguli în masă pentru produsele selectate care nu au încă una.
- Acțiunea server **Open Rules Wizard** (pe formularul produsului) deschide un asistent pentru reguli pe locații alese, cu **Minimum Quantity**, **Maximum Quantity** și **Trigger** (automat sau manual). Se creează câte o regulă pentru fiecare variantă de produs și fiecare locație.
- Dezactivarea creării automate fără dezinstalare: parametrul de sistem `deltatech_auto_reorder_rule.dont_auto_create_rule` cu valoarea `True`; regulile se pot genera în continuare manual.
- Regulile create se verifică în **Inventar > Operațiuni > Reaprovizionare**.
- Configurare: opțiunea de depozit în **Inventar > Configurare > Depozite**, opțiunea de rută în **Inventar > Configurare > Rute** (detaliile pas cu pas sunt în fișa consultantului).

#### 3. Dependențe

- `stock`
- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.product`: creează regulile (metoda `create_rule()`) la crearea produsului sau la cerere.
- `stock.warehouse`: opțiunea **Generate Reorder Rules**.
- `stock.route`: marcajul **Use This for Auto Rules**.
- `order.rules.details.wizard`: asistentul pentru reguli cu cantități și locații personalizate.

**Vizualizări**

- Vizualizări moștenite pe depozit și rută, plus formularul asistentului de reguli (`wizard/order_rules_details_view.xml`).

**Acțiuni Automate / Acțiuni Server**

- `product_action_create_rule`: acțiune server pe produs; apelează `create_rule()` pentru produsele selectate.
- `product_action_create_variant_rule`: acțiune server pe formularul produsului; deschide `order.rules.details.wizard`.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte module documentate în wiki. Modulul se integrează cu reaprovizionarea nativă din `stock`, `purchase_stock` și `sale_stock`.
