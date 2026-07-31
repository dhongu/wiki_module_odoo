# Supplier Price Comparison (localizat la `deltatech_purchase_price_compare/index.md`)

- **Nume Tehnic:** `deltatech_purchase_price_compare`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_purchase_price_compare`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_price_compare`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă pe comanda de achiziție (`purchase.order`) un buton „Compare supplier prices" care deschide un dialog de comparare a prețurilor tuturor furnizorilor definiți pentru produsele din comandă (`product.supplierinfo`). Din punct de vedere al afacerii, ajută echipa de achiziții să cumpere la cel mai bun preț și, mai important, să sesizeze din timp situațiile în care prețul de pe comandă nu mai corespunde tarifului curent al furnizorului — înainte ca o comandă cu preț greșit să fie plasată.

#### 2. Funcționalități Cheie

- Comparație unul-lângă-altul a tuturor furnizorilor unui produs, cu prețul convertit în moneda și UM-ul comenzii (selecția respectă logica standard Odoo: companie, valabilitate, cantitate minimă, discount).
- Evidențierea celui mai mic preț, cu economia calculată pe linie și pe total.
- Detectarea prețurilor „derapate" — pentru furnizorul comenzii se afișează tariful curent, iar liniile la care prețul comenzii diferă de tariful actual al furnizorului sunt marcate.
- Aplicare rapidă — scrie prețul ales înapoi pe liniile comenzii și, dacă toate liniile converg către un singur furnizor, actualizează și furnizorul comenzii.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

DESCRIPTION.md acoperă scopul și funcționalitățile principale ale modulului. Se notează componentele care implementează mecanismul de comparare/aplicare a prețurilor, menționat explicit în descriere.

**Modele**

- `purchase.price.compare.wizard` (`TransientModel`): asistentul principal, legat de o comandă de achiziție (`order_id`); populează câte o linie de comparație per linie de comandă (`_populate_lines`), calculează totalurile curente/optimizate și economia estimată, și scrie prețurile alese înapoi pe comandă prin `action_apply`.
- `purchase.price.compare.line` (`TransientModel`): o linie de comparație per linie de comandă; calculează furnizorii disponibili și cel mai bun preț (`_compute_sellers`), prețul/tariful curent al furnizorului comenzii pentru detectarea derapajului de preț (`_compute_order_supplier`), prețul selectat și economia per linie, cu conversie de monedă și UM.
- Extensie pe `purchase.order`: metoda `action_compare_supplier_prices()` deschide asistentul de comparare ca dialog modal.

**Vizualizări**

- `view_purchase_order_form_compare`: adaugă butonul „Compare supplier prices" în antetul formularului de comandă de achiziție (`purchase.purchase_order_form`).
- `view_price_compare_wizard_form`: formularul asistentului, cu un banner de avertizare pentru liniile cu preț schimbat și un grid OWL pivotat (`supplier_price_grid`, furnizorii ca și coloane) pentru selecția rapidă a prețului pe linie.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki. Modulul se integrează cu funcționalitatea nativă Odoo din `purchase` (comenzi de achiziție și `product.supplierinfo`).
