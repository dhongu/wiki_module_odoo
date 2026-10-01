# Product Attribute Extension (localizat la `deltatech_product_attribute/index.md`)

- **Nume Tehnic:** `deltatech_product_attribute`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_product_attribute
- **Cale Locală:** `odoo-addons/bitshop/deltatech_product_attribute`
- **Ultima Ingestie:** `2026-10-01`

#### 1. Sumar

Modulul extinde gestionarea atributelor de produs din Odoo pentru cataloagele cu produse complexe, cu multe atribute și variante. Permite organizarea atributelor în grupuri și introduce atribute de tip Da/Nu, care exprimă simplu prezența unei caracteristici. Rezultatul este un catalog mai bine structurat, mai ușor de filtrat și de raportat, cu informații mai clare pentru site-uri și marketplace-uri.

#### 2. Funcționalități Cheie

- **Grupuri de atribute:** atributele pot fi încadrate într-un grup configurabil, de tip „un singur atribut" sau „mai multe", cu limite minim și maxim. Grupul se alege din formularul atributului, lângă opțiunea de creare a variantelor.
- **Atribute de tip Da/Nu (`boolean`):** tip nou de afișare pentru atribute, fără valori artificiale „Da"/„Nu". Pe fiecare valoare apare o bifă „True Value", vizibilă doar când atributul este de tip Da/Nu.
- **Denumire mai curată a variantelor:** la atributele Da/Nu, numele variantei conține doar caracteristicile active. Rezultă „Cămașă (Mânecă lungă)", nu „Cămașă (Mânecă lungă: Da)".
- **Meniu dedicat:** Vânzări → Configurare → Attribute group, vizibil pentru utilizatorii cu variantele de produs activate.
- Pentru a structura catalogul, a facilita filtrarea și raportarea după atribute, modulul sprijină și integrarea cu site-ul și marketplace-urile prin date de produs mai detaliate.

#### 3. Dependențe

- `product`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.attribute.group`: grup de atribute, cu nume, tip (`single` / `multiple`), limite `min` / `max` și lista atributelor membre.
- `product.attribute` (extins): adaugă `group_id` și tipul de afișare `boolean` (la dezinstalare revine la valoarea implicită).
- `product.attribute.value` (extins): adaugă câmpul `bool_value` („True Value").
- `product.template.attribute.value` (extins): suprascrie `_get_combination_name`. Pentru atributele Da/Nu afișează doar numele atributului, și doar dacă valoarea este adevărată.

**Vizualizări**

- `product_attribute_view_form`: moștenește formularul atributului. Adaugă `group_id` și coloana `bool_value` pe valori.
- `product_attribute_group_view_tree` / `product_attribute_group_view_form`: listă și formular pentru grupurile de atribute.
- `action_attribute_group` și `menu_product_attribute_group`: acțiunea și meniul din Vânzări → Configurare (grup `product.group_product_variant`).

**Acțiuni Automate / Acțiuni Server**

- Nu există. Accesul la `product.attribute.group` este acordat grupului `base.group_user` (citire, scriere, creare, ștergere).

#### 5. Conexiuni

- Nu există conexiuni funcționale verificate cu alte module cu pagină wiki.
