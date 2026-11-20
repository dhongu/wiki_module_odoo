# Sale XLS (localizat la `deltatech_sale_xls/index.md`)

- **Nume Tehnic:** `deltatech_sale_xls`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_xls
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_xls`
- **Ultima Ingestie:** `2026-11-20`

#### 1. Sumar

Clienții își trimit adesea comanda, sau modificările ei, sub formă de tabel. Modulul permite vânzătorului să exporte liniile unei comenzi de vânzare în Excel și să le importe înapoi în aceeași comandă, cu instrumentele standard de export și import ale Odoo. Este util mai ales la comenzile cu multe articole, unde introducerea manuală a liniilor ar consuma mult timp.

#### 2. Funcționalități Cheie

- **Butonul „Order lines”:** butonul inteligent de pe comanda de vânzare deschide lista liniilor ei (**Sale Order Lines**: comandă, produs, cantitate, preț unitar). Din această listă liniile se exportă cu **Export** standard, iar un fișier se încarcă cu **Import records**; liniile importate intră în această comandă.
- **Import într-o comandă goală:** fiecare rând din fișier devine o linie nouă a comenzii.
- **Import într-o comandă cu linii:** fiecare rând actualizează linia existentă cu același produs (cantitate, preț și celelalte coloane importate). Produsul se recunoaște după referința internă dintre paranteze drepte (`[COD] Nume`, ca în export) sau, în lipsă, după numele exact. Rândurile cu un produs negăsit sau care nu e pe comandă sunt sărite.
- **Punct de extensie pentru formule de preț:** metoda `use_specific_price_formula` se apelează pe prețurile unitare importate ale unei comenzi noi, deci un modul specific unui client își poate aplica propria regulă de preț.
- **Limitări:**
    - când comanda are deja linii, un rând pentru un produs nou este sărit fără mesaj și nu poate adăuga o linie;
    - dacă pe comandă există două linii cu același produs, importul acelui produs eșuează;
    - fără butonul „Order lines”, comanda se citește din coloana **Order Reference** doar când aceasta conține id-ul din baza de date al comenzii, nu numărul ei.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

Conform prioritizării Readme (`readme/DESCRIPTION.md` prezent), analiza detaliată a codului a fost limitată la verificarea funcționalităților descrise.

**Modele**

- `sale.order` (extins): `show_order_lines()` deschide lista liniilor comenzii, cu `default_order_id` în context.
- `sale.order.line` (extins): `load()` leagă importul de comandă (din context sau din coloana `order_id`), recunoaște produsul și actualizează linia existentă sau adaugă linii noi; `use_specific_price_formula()` este punctul de extensie pentru prețuri.

**Vizualizări**

- `sale_order_form`: butonul inteligent „Order lines” pe formularul comenzii.
- `sale_order_line_tree`: lista liniilor comenzii (comandă, produs, cantitate, preț unitar), folosită la export și import.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_purchase_xls](../deltatech_purchase_xls/index.md): modulul echivalent pentru comenzile de achiziție, cu aceeași logică de import/export a liniilor prin Excel.
