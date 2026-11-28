# Alternative Product Codes (localizat la `deltatech_alternative/index.md`)

- **Nume Tehnic:** `deltatech_alternative`
- **Versiune:** `20.0.2.2.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_alternative
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite gestiunea mai multor coduri alternative pentru același produs, astfel încât acesta să poată fi găsit indiferent de codul cu care este cunoscut: cod de furnizor, cod de producător, cod vechi (legacy) sau identificator specific unui client. Este util companiilor care lucrează cu nomenclatoare provenite din surse multiple, unde același articol circulă sub denumiri sau coduri diferite.

#### 2. Funcționalități Cheie

- Tab dedicat **Alternative** pe fișa produsului (**Inventar > Produse > Produse** sau **Vânzări > Produse > Produse**), unde se pot adăuga oricâte coduri suplimentare, reordona prin drag handle și marca individual ca ascunse (`Hide`) din afișarea combinată.
- Câmp calculat **Alternative Code**, care concatenează codurile vizibile; apare în lista de produse și în secțiunea de informații generale a fișei.
- Căutarea de produs (șabloane și variante) returnează produsul și după un cod alternativ. Căutarea este opțională (dezactivată implicit) și se configurează din **Setări > Inventar**.
- Coloană opțională **Alternative Code** (doar citire, ascunsă implicit) pe liniile de comandă de vânzare, comandă de achiziție și mișcări de stoc, activată din butonul coloanelor opționale.
- Câmp text liber **Used For** pe produs, pentru a nota utilizarea articolului (ajută la identificare și vânzare încrucișată).
- Acțiune programată zilnică (inactivă implicit) care separă codurile introduse pe aceeași linie cu `;` sau `,` în câte o înregistrare alternativă per cod, fără a crea coduri deja existente. Spațiile rămân parte din cod (de ex. numere OEM de tipul `366 200 05 01`). Se activează din **Setări > Tehnic > Acțiuni programate**.
- Parametri din **Setări > Inventar** (după secțiunea *Unități de Măsură*), salvați ca parametri de sistem și editabili și din **Setări > Tehnic > Parametri de sistem**:
  - **Alternative Search** (`alternative.search_name`, implicit dezactivat): scanarea codurilor alternative în căutarea de produse.
  - **Alternative Limit** (`alternative.limit`, implicit 10): numărul maxim de rezultate suplimentare.
  - **Minimum Length** (`alternative.length_min`, implicit 3): numărul minim de caractere înainte de declanșarea căutării.
  - **Code Before Name** (`alternative.dropdown_code_first`, implicit dezactivat): lista de selecție a produsului afișează `[cod] nume`.
  - **Show Stock in Dropdown** (`alternative.dropdown_show_qty`, implicit dezactivat): lista de selecție afișează cantitatea în stoc a produselor stocabile.
- Pentru baze de date mari, codurile alternative folosesc un index trigram (GIN). Necesită extensia PostgreSQL `pg_trgm`, iar indexul include `unaccent` doar dacă funcția `public.unaccent(text)` este `IMMUTABLE` (pe odoo.sh este deja asigurat; pe instalări proprii se configurează după procedura din `readme/CONFIGURE.md`).

#### 3. Dependențe

- `product`
- `stock`
- `sale`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `product.alternative`: stochează codurile alternative (`name`, `sequence`, `hide`), legate many2one de `product.template` (`product_tmpl_id`, ștergere în cascadă).
- `product.template`: câmpul `alternative_code` (calculat și inversabil, sincronizat cu liniile `alternative_ids`) și câmpul `used_for`; suprascrie căutarea după nume.
- `product.product`: extinde căutarea după nume cu potriviri pe codurile alternative.
- `res.config.settings`: expune parametrii de configurare ai căutării.
- `sale.order.line`, `purchase.order.line`, `stock.move`, `stock.move.line`: câmp `alternative_code` (related, nestocat) pentru afișare pe documente.

**Vizualizări**

- Vizualizări moștenite pe produs (șablon și variantă), `product.alternative`, linii de comandă de vânzare/achiziție, mișcări de stoc, transferuri și setările de Inventar.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_split_alternative_codes`: acțiune programată zilnică, inactivă implicit, care împarte codurile multiple de pe o linie în înregistrări separate.

#### 5. Conexiuni

- [deltatech_alternative_website](../deltatech_alternative_website/index.md): afișează codurile alternative și câmpul `used_for` în magazinul online și le include în căutarea site-ului.
