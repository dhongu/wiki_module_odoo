# Supplier Price Comparison (localizat la `deltatech_purchase_price_compare/index.md`)

- **Nume Tehnic:** `deltatech_purchase_price_compare`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_purchase_price_compare
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_price_compare`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe comanda de achiziție (`purchase.order`) un buton „Compare supplier prices" care deschide un dialog de comparare a prețurilor tuturor furnizorilor definiți pentru produsele din comandă (`product.supplierinfo`). Ajută echipa de achiziții să cumpere la cel mai bun preț și să sesizeze din timp situațiile în care prețul de pe comandă nu mai corespunde tarifului curent al furnizorului, înainte ca o comandă cu preț greșit să fie plasată.

#### 2. Funcționalități Cheie

- Comparație unul lângă altul a tuturor furnizorilor unui produs, cu prețul convertit în moneda (la `date_order`) și UM-ul comenzii; selecția respectă logica standard Odoo (companie, valabilitate, cantitate minimă, discount).
- Evidențierea celui mai mic preț, cu economia calculată pe linie și pe total.
- Detectarea prețurilor „derapate": liniile la care prețul comenzii diferă de tariful curent al furnizorului sunt marcate, iar un banner din partea de sus le numără.
- Furnizorii apar ca coloane; un clic pe o celulă îl alege pe furnizorul respectiv pentru linie. Furnizorul comenzii este marcat cu eticheta „order".
- Indicatori (KPI): suma curentă, suma optimizată, economia estimată și procentul de economie.
- Aplicare rapidă prin **Apply selected prices to the order**: scrie prețurile alese pe liniile comenzii și, dacă toate liniile converg spre un singur furnizor, actualizează și furnizorul comenzii.
- Acces din **Purchase > Orders**, butonul din antetul comenzii; fluxul cu capturi este în fișa consultantului.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.price.compare.wizard` (`TransientModel`): asistentul, legat de comandă; populează liniile, calculează totalurile și economia și scrie prețurile alese prin `action_apply`.
- `purchase.price.compare.line` (`TransientModel`): o linie de comparație per linie de comandă; calculează furnizorii disponibili, cel mai bun preț și tariful curent al furnizorului comenzii.
- `purchase.order`: extins cu `action_compare_supplier_prices()`, care deschide asistentul ca dialog modal.

**Vizualizări**

- `view_purchase_order_form_compare`: butonul din antetul formularului comenzii de achiziție.
- `view_price_compare_wizard_form`: formularul asistentului, cu bannerul de avertizare și grila OWL pivotată (`supplier_price_grid`).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki. Modulul se integrează cu funcționalitatea nativă `purchase` (comenzi de achiziție și `product.supplierinfo`).
