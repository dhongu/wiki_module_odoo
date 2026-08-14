# MRP BoM Formula (localizat la `deltatech_mrp_bom_formula/index.md`)

- **Nume Tehnic:** `deltatech_mrp_bom_formula`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_bom_formula
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_bom_formula`
- **Ultima Ingestie:** `2026-08-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite ca **cantitatea unei componente din lista de materiale să fie calculată printr-o formulă**, evaluată în raport cu atributele variantei fabricate. Standardul Odoo poate doar să includă sau să excludă o linie în funcție de valorile unui atribut („Se aplică pe variante"), cantitatea rămânând constantă; de îndată ce consumul depinde de configurație, singura soluție standard este multiplicarea liniei pentru fiecare combinație de atribute. Cu acest modul, o singură linie acoperă toate variantele.

Este echivalentul funcțional al părții de calcul al consumului din mecanismul *variant configuration* al SAP.

#### 2. Funcționalități Cheie

- Cod de formulă (`code`) pe atribut și pe valoarea atributului, generat automat din denumire, cu diacriticele curățate și sufix numeric la coliziune
- Valoare numerică (`numeric_value`) pe valoarea atributului, pentru caracteristici măsurabile (lățime, lungime, grosime)
- Formulă de cantitate (`qty_formula`) pe linia de componentă, evaluată cu `safe_eval` peste dicționarele `attr` (cod atribut → cod valoare) și `num` (cod atribut → valoare numerică)
- Cantitatea de bază a liniei este disponibilă în formulă ca `qty`; sunt disponibile `ceil`, `floor` și funcțiile matematice uzuale
- Formulele sunt validate la salvare, nu la lansarea producției, iar un cod inexistent este raportat cu numele lui
- Un atribut pe care produsul nu îl poartă are valoare neutră (`False` / `0.0`), astfel încât o LDM de semifabricat poate citi o caracteristică a produsului finit
- Pe LDM-uri imbricate, configurația produsului rădăcină rămâne disponibilă; doar valorile purtate efectiv de produsul intermediar o suprascriu
- Linia fără formulă își păstrează cantitatea, iar o LDM fără nicio formulă folosește integral codul standard

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

**Modele**

- `product.attribute` (extins): câmpul `code` (identificatorul din formule, generat din denumire prin `slugify_code` și menținut unic prin `_get_unique_code`) și metoda `_get_formula_defaults()`, care returnează dicționarele neutre cu toate codurile de atribut din baza de date.
- `product.attribute.value` (extins): câmpurile `code` și `numeric_value`, valorile returnate de dicționarele `attr`, respectiv `num`.
- `product.template.attribute.value` (extins): câmpuri `related` către cele de mai sus, pentru acces din interfață.
- `product.product` (extins): `_get_own_formula_values()` returnează strict valorile purtate de variantă, iar `_get_formula_values()` le suprapune peste dicționarele neutre. Separarea este necesară pentru ca, la LDM-uri imbricate, valorile neutre ale semifabricatului să nu suprascrie configurația produsului rădăcină.
- `mrp.bom` (extins): metoda `explode()` este rescrisă pentru a folosi rezultatul formulei în locul câmpului stocat `product_qty`. Corpul este copiat din standard, cu o singură diferență funcțională, și trebuie recomparat la fiecare trecere de versiune. O LDM fără nicio formulă apelează `super()`.
- `mrp.bom.line` (extins): câmpul `qty_formula`, metodele `_get_formula_eval_context()` și `_get_formula_quantity()` (evaluare, cu respingerea rezultatelor non-numerice sau negative) și constrângerea `_check_qty_formula`, care testează formula la salvare pe o configurație plauzibilă.

**Vizualizări**

- `product_attribute_view_form` (moștenește `product.product_attribute_view_form`): câmpul `code` pe atribut și coloanele `code` / `numeric_value` pe valorile atributului, vizibile pentru grupul *Manufacturing / Administrator*.
- `mrp_bom_form_view` (moștenește `mrp.mrp_bom_form_view`): coloana opțională `qty_formula` pe componentele listei de materiale, ascunsă implicit și afișată doar când LDM-ul este definit pe șablon.
- `mrp_bom_line_view_form` (moștenește `mrp.mrp_bom_line_view_form`): câmpul `qty_formula` pe formularul liniei de LDM.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`. Calculul se face sincron, la explodarea listei de materiale.

#### 5. Conexiuni

- `mrp`: furnizează `mrp.bom`, `mrp.bom.line` și mecanismul de explodare extins de modul.
- `product`: furnizează atributele și valorile de atribut pe care se sprijină formulele.
- [deltatech_mrp_bom](../deltatech_mrp_bom/index.md): abordare complementară asupra aceleiași probleme — LDM-uri de tip Bază/Derivat generate pe variante. Reduce munca manuală de întreținere, dar păstrează câte o linie per combinație; modulul de față elimină liniile duplicate.
- [deltatech_mrp_concentration](../deltatech_mrp_concentration/index.md): ajustează tot cantitățile de pe liniile de LDM, însă pe baza concentrației ingredientului activ, nu a atributelor variantei.

#### 6. Limitări cunoscute

- Valorile numerice introduse de utilizator la comandă (`product.attribute.custom.value`) nu sunt propagate de standardul Odoo către ordinul de fabricație, deci formulele pot folosi doar valori definite în nomenclator.
- Formula se aplică doar componentelor, nu și operațiilor sau subproduselor.
- Raportul de structură al listei de materiale își calculează cantitățile separat de mecanismul de explodare, deci nu reflectă formulele.
