# Deltatech Hierarchy Many2one Widget (localizat la `deltatech_widget_hierarchy_m2o/index.md`)

- **Nume Tehnic:** `deltatech_widget_hierarchy_m2o`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_widget_hierarchy_m2o
- **Cale Locală:** `odoo-addons/bitshop/deltatech_widget_hierarchy_m2o`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul înlocuiește lista derulantă plată standard a câmpurilor many2one cu un widget de tip arbore părinte/copil, permițând utilizatorului să vadă și să navigheze direct ierarhia unui model (categorii de produse, conturi contabile, conturi analitice, locații de stoc, departamente etc.) atunci când alege o valoare. Este util oriunde structura ierarhică a înregistrărilor contează pentru o selecție corectă și rapidă, evitând confuziile dintr-o listă lungă și fără context de tip părinte-copil.

#### 2. Funcționalități Cheie

- Arbore expandabil părinte/copil direct în câmpul many2one, cu încărcare leneșă (lazy loading) a copiilor — copiii unui nod se aduc din server doar când nodul este deschis, deci scalează bine pe ierarhii mari.
- Casetă de căutare încorporată, care caută pe întreg arborele (nu doar la nivelul curent vizibil) și afișează rezultatele într-o listă plată.
- Funcționează pe **orice** câmp many2one al cărui model țintă are un câmp părinte de tip self-relation, configurabil prin opțiunea `parent_field` (implicit `parent_id`).
- Adâncime maximă a arborelui și număr de înregistrări per nivel reglabile din opțiunile câmpului (`level`, `limit`).
- Widget OWL pur, fără biblioteci JavaScript externe (fără jsTree/zTree) și fără dependențe suplimentare de server dincolo de `web`.

#### 3. Dependențe

- `web`
- `product`

#### 4. Componente Cheie

**Modele**

Modulul nu definește sau extinde modele Python; toată logica este client-side (widget OWL) și citește datele modelului țintă prin ORM (`searchRead`, `formattedReadGroup`).

**Vizualizări**

- `product_category_form_view_hierarchy`: moștenește formularul `product.category` din modulul `product` și adaugă widget-ul `hierarchy_m2o` pe câmpul `parent_id` (selecția categoriei părinte ca arbore) — vizualizare demonstrativă.
- `product_template_form_view_hierarchy`: moștenește formularul `product.template` și adaugă widget-ul `hierarchy_m2o` pe câmpul `categ_id` (Categorie Internă) — vizualizare demonstrativă, nu obligatorie în producție.

**Componente tehnice (widget OWL)**

- `HierarchyM2OField` (`static/src/hierarchy_m2o_field.esm.js`): componentă OWL înregistrată în `registry.category("fields")` sub cheia `hierarchy_m2o`; gestionează popover-ul de selecție, căutarea cu debounce (250ms) și opțiunile de view `parent_field`, `limit`, `level`.
- `HierarchyNode`: componentă recursivă pentru fiecare nod al arborelui, cu expandare/încărcare leneșă a copiilor la primul click.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

Nu au fost identificate în cod alte module din wiki cu legături funcționale directe (widget-ul este generic și nu are dependențe funcționale în afara `web`/`product`).
