# Deltatech Auto Reorder Rule (localizat la `deltatech_auto_reorder_rule/index.md`)

- **Nume Tehnic:** `deltatech_auto_reorder_rule`
- **Versiune:** `19.0.0.1.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_auto_reorder_rule`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_auto_reorder_rule`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul automatizează crearea regulilor de reaprovizionare (reordering rules) pentru produse. La adăugarea unui produs nou, modulul generează automat o regulă de reaprovizionare cu valori implicite, eliminând astfel un pas manual repetitiv. Pentru produsele deja existente, oferă o metodă dedicată prin care regulile pot fi create în masă. Astfel, echipa de achiziții și logistică se asigură că fiecare produs gestionat are definite pragurile de stoc necesare pentru reaprovizionarea automată.

#### 2. Funcționalități Cheie

- Creează automat o regulă de reaprovizionare cu valori implicite atunci când este creat un produs nou.
- Oferă metoda `create_rule()` pe modelul `product.product` pentru a crea reguli pentru produsele deja existente.
- Regulile sunt create doar pentru produsele de tip stocabil (`type='product'`).

#### 3. Dependențe

- `stock`
- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

DESCRIPTION.md acoperă scopul și funcționalitățile principale ale modulului. Întrucât descrierea face referire explicită la mecanismul de creare a regulilor (metoda `create_rule()`), se notează componentele de declanșare puse la dispoziția utilizatorului.

**Acțiuni Automate / Acțiuni Server**

- `product_action_create_rule`: Acțiune server legată de `product.template`, disponibilă din meniul de acțiuni pe produse; apelează `create_rule()` pe variantele produselor selectate pentru a genera regulile de reaprovizionare.
- `product_action_create_variant_rule`: Acțiune server legată de formularul `product.template`; deschide asistentul `order.rules.details.wizard` pentru detalierea regulilor de comandă.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki. Modulul se integrează cu funcționalitatea nativă Odoo de reaprovizionare din `stock`, `purchase_stock` și `sale_stock`.
