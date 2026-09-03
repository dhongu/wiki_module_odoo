# Supplier Price Comparison (localizat la `deltatech_purchase_price_compare/index.md`)

- **Nume Tehnic:** `deltatech_purchase_price_compare`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_purchase_price_compare`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_price_compare`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Modulul adaugă pe comanda de achiziție (`purchase.order`) un buton „Compare supplier prices" care deschide un dialog de comparare a prețurilor tuturor furnizorilor definiți pentru produsele din comandă (`product.supplierinfo`). Din punct de vedere al afacerii, ajută echipa de achiziții să cumpere la cel mai bun preț și, mai important, să sesizeze din timp situațiile în care prețul de pe comandă nu mai corespunde tarifului curent al furnizorului — înainte ca o comandă cu preț greșit să fie plasată.

#### 2. Funcționalități Cheie

- Comparație unul-lângă-altul a tuturor furnizorilor unui produs, cu prețul convertit în moneda și UM-ul comenzii (selecția respectă logica standard Odoo: companie, valabilitate, cantitate minimă, discount).
- Evidențierea celui mai mic preț, cu economia calculată pe linie și pe total.
- Detectarea prețurilor „derapate" — pentru furnizorul comenzii se afișează tariful curent, iar liniile la care prețul comenzii diferă de tariful actual al furnizorului sunt marcate.
- Aplicare rapidă — scrie prețul ales înapoi pe liniile comenzii și, dacă toate liniile converg către un singur furnizor, actualizează și furnizorul comenzii.
- Acces din `Purchase → Orders`, prin butonul „Compare supplier prices" din antetul comenzii de achiziție.
- În grid, furnizorii apar ca și coloane; un clic pe o celulă selectează furnizorul respectiv pentru linie, iar furnizorul curent al comenzii este mereu vizibil, marcat cu eticheta „order".
- Liniile ale căror preț de pe comandă diferă de tariful curent al furnizorului sunt evidențiate, cu un banner de avertizare în partea de sus care numără liniile afectate.
- KPI-urile din dialog arată suma curentă a comenzii, suma optimizată (dacă s-ar aplica prețurile alese) și economia estimată.
- Butonul „Apply selected prices to the order" scrie prețurile alese pe liniile comenzii și actualizează furnizorul comenzii dacă toate liniile converg spre același furnizor.
- Conversie automată monedă/UM: prețul din `product.supplierinfo` (exprimat în moneda și UM-ul furnizorului) este convertit în moneda comenzii (la data `date_order`) și în UM-ul liniei înainte de comparație.

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
