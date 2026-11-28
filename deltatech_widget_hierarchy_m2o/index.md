# Hierarchy Many2one Widget (localizat la `deltatech_widget_hierarchy_m2o/index.md`)

- **Nume Tehnic:** `deltatech_widget_hierarchy_m2o`
- **Versiune:** `20.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_widget_hierarchy_m2o
- **Cale Locală:** `odoo-addons/bitshop/deltatech_widget_hierarchy_m2o`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Widget OWL care permite alegerea unei înregistrări dintr-un **arbore** părinte/copil expandabil, direct în orice câmp many2one, în loc de o listă plată care ascunde ierarhia. Nu folosește biblioteci JavaScript externe și nu conține cod Python.

#### 2. Funcționalități Cheie

- Arbore expandabil cu încărcare leneșă: copiii se aduc doar la deschiderea nodului, deci scalează la ierarhii mari; nodul curent este expandat și evidențiat la deschidere.
- Casetă de căutare care aplatizează rezultatele pe tot arborele, cu calea completă.
- Funcționează pe orice many2one a cărui țintă are un câmp părinte (`parent_field`, implicit `parent_id`); opțiuni `limit` (implicit 80 înregistrări pe nivel) și `level` (adâncime, implicit 8). Cazuri tipice: categorii de produs, planuri analitice, locații de stoc, departamente.
- **Mod multi-nivel** (`levels`): arborele trece prin modele diferite (de ex. marcă → serie → model); doar înregistrările ultimului nivel se pot selecta. Câmpul închis arată calea ca segmente, iar un click pe segment deschide arborele până la nod. Opțiuni pe nivel: `link`, `fallback_link`, `domain`, `detail`.
- **Mod pași** (`steps: True`, doar multi-nivel): panoul arată câte un nivel pe rând, cu calea aleasă deasupra, potrivit cataloagelor mari.
- Domeniul câmpului se aplică înregistrărilor selectabile, în arbore și în căutare; în modul părinte/copil, nodurile din afara domeniului rămân estompate.
- Pe înregistrare doar-citire câmpul apare ca text simplu. Include două vizualizări demonstrative (categoria de produs și produsul).
- Utilizabil și pe Odoo Online (plan Custom), prin **Apps > Import Module**.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `web`
- `product`

#### 4. Componente Cheie

Modulul nu definește sau extinde modele Python; logica este client-side (widget OWL).

**Modele**

Niciun model Python.

**Vizualizări**

- `product_category_form_view_hierarchy`: formularul `product.category` cu widgetul `hierarchy_m2o` pe **Parent Category**.
- `product_template_form_view_hierarchy`: formularul `product.template` cu widgetul pe **Category** (`categ_id`).

**Componente tehnice (widget OWL)**

- `HierarchyM2OField` (`static/src/hierarchy_m2o_field.esm.js`): câmp înregistrat în `registry.category("fields")` sub cheia `hierarchy_m2o`.
- Șablon și stiluri în `hierarchy_m2o_field.xml` / `.scss`; tur și test unitar în `static/tests/`.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

Nu există legături funcționale directe cu alte module cu pagină wiki; widgetul este generic.
