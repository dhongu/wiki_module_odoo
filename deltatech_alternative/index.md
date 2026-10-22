# Products Alternative (localizat la `deltatech_alternative/index.md`)

- **Nume Tehnic:** `deltatech_alternative`
- **Versiune:** `19.0.2.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_alternative
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul permite gestiunea mai multor coduri alternative pentru același produs, astfel încât acesta să poată fi găsit indiferent de codul cu care este cunoscut — cod de furnizor, cod de producător, cod vechi (legacy) sau identificator specific unui client. Este util companiilor care lucrează cu nomenclatoare provenite din surse multiple, unde același articol circulă sub denumiri sau coduri diferite.

#### 2. Funcționalități Cheie

- Tab dedicat **Alternative** pe fișa produsului (**Inventar > Produse > Produse** sau **Vânzări > Produse > Produse**), unde se pot adăuga oricâte coduri suplimentare, reordona (prin drag handle) și marca individual ca ascunse (**Hide**) din afișarea combinată.
- Câmp calculat **Alternative Code** (concatenarea codurilor vizibile), afișat în lista de produse, pe fișa produsului și pe documente.
- Extinderea căutării de produs, pe șabloane și variante: introducerea unui cod alternativ returnează produsul potrivit. Căutarea este opțională (dezactivată implicit) și respectă domeniul câmpului de selecție.
- Coloană opțională **Alternative Code** (needit, ascunsă implicit) pe liniile de comandă de vânzare, comandă de achiziție și mișcări de stoc — se activează din meniul coloanelor opționale.
- Câmp text liber **Used For** pe produs, pentru a nota utilizarea acestuia (identificare, vânzare încrucișată).
- Acțiune programată zilnică (inactivă implicit) care desparte codurile introduse pe o singură linie și separate prin `;` sau `,` în câte o înregistrare per cod, fără a crea coduri deja existente pe produs. Spațiile rămân parte din cod (ex. numere OEM de tipul `366 200 05 01`). Se activează din **Setări > Tehnic > Acțiuni programate**.
- Configurare din **Setări > Inventar** (după secțiunea *Unități de măsură*), salvată ca `ir.config_parameter` (editabilă și din Parametri de sistem):
  - **Alternative Search** (`alternative.search_name`, implicit dezactivat) — căutarea de produse scanează și codurile alternative.
  - **Alternative Limit** (`alternative.limit`, implicit 10) — numărul maxim de rezultate suplimentare.
  - **Minimum Length** (`alternative.length_min`, implicit 3) — numărul minim de caractere pentru declanșarea căutării.
  - **Code Before Name** (`alternative.dropdown_code_first`, implicit dezactivat) — lista de selecție a produselor afișează `[cod] denumire`, în loc de denumirea cu codul estompat în dreapta.
  - **Show Stock in Dropdown** (`alternative.dropdown_show_qty`, implicit dezactivat) — lista de selecție afișează, estompat în dreapta, stocul disponibil al produselor stocabile (doar în selector, nu în documente sau rapoarte).
- Baze mari de date: codurile alternative au index trigram (GIN) pe `name`; este necesară extensia PostgreSQL `pg_trgm`, iar `unaccent` este inclus în index doar dacă funcția `public.unaccent(text)` este `IMMUTABLE` (pe odoo.sh este asigurat de platformă). Pașii detaliați (configurare self-hosted, creare index `CONCURRENTLY`, redenumirea indexului din 18.0) sunt în `readme/CONFIGURE.md` al modulului.

#### 3. Dependențe

- `product`
- `stock`
- `sale`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `product.alternative`: coduri alternative (`name` cu index trigram, `sequence`, `hide`), legate many2one de `product.template` (`product_tmpl_id`, `ondelete="cascade"`); metoda `split_multi_codes` rulată de acțiunea programată.
- `product.template` (extins): `alternative_ids`, câmpul calculat/inversat `alternative_code` și `used_for`; `name_search` include și potriviri pe codurile alternative, condiționat de `alternative.search_name`.
- `product.product` (extins): `name_search` cu căutare în coduri alternative și `_compute_display_name` pentru afișarea din liste de selecție (cod înainte de nume, stoc).
- `res.config.settings` (extins): `alternative_search`, `alternative_limit`, `alternative_length_min`, `alternative_dropdown_code_first`, `alternative_dropdown_show_qty`.
- `sale.order.line`, `purchase.order.line`, `stock.move`, `stock.move.line` (extinse): câmp `related` `alternative_code` (nestocat).

**Vizualizări**

- `views/product_template_view.xml`, `views/product_product_view.xml`: tab-ul **Alternative**, câmpurile `alternative_code` și `used_for` pe produs.
- `views/product_alternative_view.xml`: vizualizări pentru modelul `product.alternative`.
- `views/sale_order_view.xml`, `views/purchase_order_view.xml`, `views/stock_move_view.xml`, `views/stock_picking_view.xml`: coloana opțională de cod alternativ pe linii.
- `views/res_config_settings_views.xml`: secțiunea de configurare din Setări > Inventar.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_split_alternative_codes` (`data/cron.xml`): „Alternative: Split multi-code records”, zilnică, inactivă implicit; apelează `model.split_multi_codes()`.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki (dependențele `product`, `stock`, `sale`, `purchase` nu au încă pagină proprie).
