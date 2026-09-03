# Products Alternative (localizat la `deltatech_alternative/index.md`)

- **Nume Tehnic:** `deltatech_alternative`
- **Versiune:** `19.0.2.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_alternative
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Modulul permite gestiunea mai multor coduri alternative pentru același produs, astfel încât acesta să poată fi găsit indiferent de codul cu care este cunoscut — cod de furnizor, cod de producător, cod vechi (legacy) sau identificator specific unui client. Este util companiilor care lucrează cu nomenclatoare provenite din surse multiple, unde același articol circulă sub denumiri sau coduri diferite.

#### 2. Funcționalități Cheie

- Tab dedicat **Alternative** pe fișa produsului, unde se pot adăuga oricâte coduri suplimentare, reordona (prin drag handle) și marca individual ca ascunse din afișarea combinată (`hide`).
- Câmp calculat **Alternative Code** (concatenarea codurilor vizibile, separate prin „; ”), afișat în lista de produse și pe fișa produsului, în secțiunea de informații generale.
- Extinderea căutării de produs (`name_search`) astfel încât introducerea unui cod alternativ să returneze produsul potrivit, atât pentru șabloane de produs cât și pentru variante. Căutarea este opțională (dezactivată implicit) și configurabilă din Setări.
- Coloană opțională **Alternative Code** (needit, ascunsă implicit) pe liniile de Comandă de Vânzare, Comandă de Achiziție și Mișcare de Stoc — se activează din meniul coloanelor opționale al listei de linii.
- Câmp text liber **Used For** pe produs, pentru a nota utilizarea acestuia (ajută la identificare și la vânzarea încrucișată).
- Configurare din **Setări > Inventar** (secțiunea injectată după *Unități de Măsură*):
  - **Alternative Search** (`alternative.search_name`, implicit dezactivat) — activează scanarea codurilor alternative în căutarea de produse.
  - **Alternative Limit** (`alternative.limit`, implicit 10) — numărul maxim de rezultate suplimentare din căutarea după cod alternativ.
  - **Minimum Length** (`alternative.length_min`, implicit 3) — numărul minim de caractere introduse înainte ca această căutare să se declanșeze.
  - Cei trei parametri sunt salvați ca `ir.config_parameter` și pot fi editați și direct din **Setări > Tehnic > Parametri > Parametri de Sistem**.

#### 3. Dependențe

- `product`
- `stock`
- `sale`
- `purchase`

#### 4. Componente Cheie

- Model `product.alternative` (`_name = "product.alternative"`): stochează codurile alternative (`name`, `sequence`, `hide`), legate many2one de `product.template` (`product_tmpl_id`, `ondelete="cascade"`).
- `ProductTemplate`: câmpul calculat/inversat `alternative_code` (compute `_compute_alternative_code`, inverse `_inverse_alternative_code`) sincronizează textul concatenat cu liniile `alternative_ids`; câmpul `used_for`.
- `ProductTemplate.name_search` / `ProductProduct.name_search`: suprascriu căutarea standard pentru a include și potriviri pe `product.alternative.name`, condiționat de parametrul `alternative.search_name`.
- `res.config.settings`: expune cei trei parametri de configurare (`alternative_search`, `alternative_limit`, `alternative_length_min`).
- Câmpuri `related` `alternative_code` (needit, nestocat) pe `sale.order.line`, `purchase.order.line`, `stock.move` și `stock.move.line`, pentru afișare pe documente.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki (dependențele `product`, `stock`, `sale`, `purchase` nu au încă pagină proprie).
