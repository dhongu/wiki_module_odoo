# Romania - Stock Accounting

- **Nume Tehnic:** `l10n_ro_stock_account`
- **Versiune:** `20.0.1.15.2`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock_account
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_stock_account
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaptează contabilitatea de stoc din Odoo la cerințele contabilității românești: conturi de stoc, venituri și cheltuieli configurabile pe locație, categorie de produs și depozit, evaluare FIFO separată pe fiecare locație și înregistrări contabile corecte pentru livrările dropship. Beneficiul este un stoc evaluat și contabilizat conform planului de conturi românesc, cu costul mărfurilor recunoscut la momentul potrivit.

#### 2. Funcționalități Cheie

- Configurări contabile specifice pe locație de stoc (cont de evaluare, cont de venituri, cont de cheltuieli), cu acțiune pentru propagarea contului către locațiile copil.
- Conturi speciale pentru operațiuni de stoc: cont de consum și cont pentru recepții în curs, definite pe contul contabil.
- Personalizarea conturilor de stoc pe categoria de produs și poziție fiscală asociată depozitului.
- FIFO pe locație (în loc de FIFO pe toată compania): fiecare ieșire se împarte automat în câte o mișcare pe fiecare strat FIFO; transferurile interne consumă din stiva locației sursă și intră în stiva destinației. Se controlează prin opțiunea de companie `fifo_per_location` (implicit activă pentru companiile românești).
- Compensarea automată a stocului negativ pentru produsele FIFO: ieșirea făcută înaintea intrării se evaluează provizoriu la prețul standard, iar la recepția următoare valoarea se realocă și se generează o notă de corecție legată de mișcarea de intrare (idempotent). Opțiunea de companie `fifo_location_negative_compensation`.
- Evaluare și contabilizare pentru livrările dropship, simetric cu o livrare obișnuită: cheltuială (607) în debit și cont de stoc (371) în credit la plecarea mărfii către client; returul se înregistrează în storno (sumă negativă), nu prin inversare debit/credit. Dropship-ul nu influențează valoarea stocului real al aceluiași produs (FIFO sau cost mediu). Mișcările dropship istorice nu se corectează retroactiv.
- Contul 408 nu se folosește niciodată pe dropship; dacă factura furnizorului lipsește la vânzare, contrapartida corectă este un cont de stoc în tranzit (327).
- Performanță: indecși parțiali pe `stock_move` pentru stiva FIFO și pentru mișcările cu cantitate negativă în așteptare, plus cache pe durata cererii pentru rapoartele mari de evaluare.

#### 3. Dependențe

- `stock_dropshipping`
- [l10n_ro_stock](../l10n_ro_stock/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.move` (extins): split pe straturi FIFO, evaluare pe locație, câmpuri `fifo_neg_pending_qty` / `fifo_neg_origin_value`, evaluare dropship.
- `stock.move.line`, `stock.picking` (câmpurile `l10n_ro_notice`, `l10n_ro_reception_in_progress`), `stock.location`, `stock.warehouse` (`l10n_ro_fiscal_position_id`): extinse cu date contabile românești.
- `account.account` (conturi de consum și recepție în curs), `account.move` / `account.move.line` (legătura corecției de stoc negativ cu mișcarea de intrare), `product.category`, `product.template`, `product.value`.
- `res.company`: opțiunile `fifo_per_location` și `fifo_location_negative_compensation`.

**Vizualizări**

- `view_company_form_fifo_location`: opțiunile FIFO pe compania.
- `view_location_form_inherit`: conturile locației.
- `view_account_form`, `view_product_category_add_romania_form`, `product_template_form_view`, `view_warehouse`: câmpuri contabile românești.
- `view_move_form`, `view_stock_move_operations`, `view_stock_move_form_fifo_neg`, `view_picking_form`: informații de evaluare pe mișcări și picking.

**Acțiuni Automate / Acțiuni Server**

- `action_location_account_propagate`: acțiune server pe locație, propagă conturile către locațiile copil.

#### 5. Conexiuni

- [l10n_ro_stock_account_base](../l10n_ro_stock_account_base/index.md): bază comună a modulelor de contabilitate de stoc.
- [l10n_ro_stock_account_landed_cost_account](../l10n_ro_stock_account_landed_cost_account/index.md): contabilizarea costurilor adiționale.
- [l10n_ro_stock_account_date](../l10n_ro_stock_account_date/index.md): data contabilă pentru operațiunile de stoc.
- [l10n_ro_stock_account_landed_cost](../l10n_ro_stock_account_landed_cost/index.md): costuri adiționale distribuite pe mișcări.
- [l10n_ro_stock_account_reception_in_progress](../l10n_ro_stock_account_reception_in_progress/index.md): recepții în curs.
