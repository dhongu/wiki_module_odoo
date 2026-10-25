# Free Disassembly - Bill of Materials (localizat la `deltatech_stock_disassembly_mrp/index.md`)

- **Nume Tehnic:** `deltatech_stock_disassembly_mrp`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_disassembly_mrp
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_disassembly_mrp`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Punte între dezmembrarea liberă (`deltatech_stock_disassembly`) și modulul de producție, instalată automat când ambele sunt prezente. Produsele rezultate dintr-un proces-verbal de dezmembrare pot fi completate dintr-o listă de materiale (rețetă), în loc să fie introduse pe rând. Procesul-verbal rămâne liber și nu necesită ordin de producție.

#### 2. Funcționalități Cheie

- Câmpul **Listă de materiale** pe procesul-verbal de dezmembrare, propus automat din produsul dezmembrat (liste de tip normal, pe produs sau pe șablonul acestuia) și modificabil; vizibil doar pentru utilizatorii cu drept de producție (`mrp.group_mrp_user`) și editabil doar în ciornă.
- Butonul **Load from BoM** (doar în ciornă, când există listă de materiale; cere confirmare): înlocuiește liniile de produs cu componentele listei, pentru cantitatea dezmembrată convertită în unitatea de măsură a listei.
- Kiturile sunt desfăcute până la componente, serviciile și cantitățile nule sunt omise, iar liniile de pierdere se păstrează.
- Liniile încărcate pot fi apoi modificate, șterse sau completate liber (cantități, loturi, pierderi); alocarea costurilor și contabilitatea rămân cele ale procesului-verbal de dezmembrare.
- Flux: creezi procesul-verbal și alegi produsul, stabilești cantitatea, apeși **Load from BoM**, ajustezi liniile, alegi metoda de alocare și **Validezi**.

#### 3. Dependențe

- `deltatech_stock_disassembly`
- `mrp`

#### 4. Componente Cheie

**Modele**

- `stock.disassembly` (extins): adaugă `bom_id` (calculat, stocat, editabil, precalculat prin `_bom_find` pe produs și companie), metoda `_compute_bom_id` și `action_load_bom`.

**Vizualizări**

- `view_stock_disassembly_form_bom`: moștenește formularul `deltatech_stock_disassembly.view_stock_disassembly_form`; adaugă butonul de încărcare după **Validate** și câmpul `bom_id` după locație.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `deltatech_stock_disassembly`: modulul de bază (dezmembrare liberă), a cărui formă și model sunt extinse.
- `mrp`: sursa listelor de materiale și a metodelor `_bom_find` / `explode`.
