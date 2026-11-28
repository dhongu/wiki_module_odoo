# Free Disassembly - Bill of Materials (localizat la `deltatech_stock_disassembly_mrp/index.md`)

- **Nume Tehnic:** `deltatech_stock_disassembly_mrp`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_disassembly_mrp
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_disassembly_mrp`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Punte între [Free Disassembly](../deltatech_stock_disassembly/index.md) și Producție, instalată automat când ambele sunt prezente. Produsele rezultate dintr-un proces-verbal de dezmembrare pot fi completate dintr-o listă de materiale, în loc să fie introduse pe rând; documentul rămâne liber și nu cere ordin de producție.

#### 2. Funcționalități Cheie

- Câmpul **Bill of Materials** pe procesul-verbal, propus din produsul dezmembrat (liste de materiale normale, potrivite după produs sau șablon) și modificabil.
- Butonul **Load from BoM** (doar în ciornă): înlocuiește liniile de produs cu componentele listei, pentru cantitatea dezmembrată convertită în unitatea listei. Kiturile sunt explodate până la componente, serviciile sunt omise, iar liniile de pierdere se păstrează.
- Liniile încărcate pot fi modificate, șterse sau completate liber; repartizarea costului și contabilitatea sunt cele ale dezmembrării.
- Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- [deltatech_stock_disassembly](../deltatech_stock_disassembly/index.md)
- `mrp`

#### 4. Componente Cheie

**Modele**

- `stock.disassembly`: extins cu lista de materiale și metoda `action_load_bom`.

**Vizualizări**

- `view_stock_disassembly_form_bom`: câmpul și butonul pe formularul dezmembrării.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Modulul este `auto_install`.

#### 5. Conexiuni

- [deltatech_stock_disassembly](../deltatech_stock_disassembly/index.md): modulul de bază extins.
