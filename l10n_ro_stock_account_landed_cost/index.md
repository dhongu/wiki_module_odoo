# Romania - Stock Accounting Landed Cost

- **Nume Tehnic:** `l10n_ro_stock_account_landed_cost`
- **Versiune:** `20.0.1.7.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock_account_landed_cost
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_stock_account_landed_cost
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Extinde costurile adiționale (landed costs) din Odoo pentru a distribui costurile și pe mișcările de stoc rezervate din stocul real, nu doar pe cele deja intrate. Este util când transportul, vama sau alte cheltuieli se cunosc după recepție și trebuie repartizate corect pe valoarea stocului.

#### 2. Funcționalități Cheie

- Distribuirea costurilor adiționale și pe mișcările de stoc rezervate din stocul actual.
- Tip de cost adițional românesc (`l10n_ro_cost_type`) și opțiunea de a distribui doar pe liniile de evaluare distribuite (de ex. pentru diferențe de preț, unde valoarea e deja contabilizată pe factură).
- Linii de evaluare distribuite, afișate separat în formularul costului adițional.
- Verificarea sumei adaptată pentru costurile care nu se distribuie pe mișcările existente.
- Acces configurat prin `ir.access` pentru liniile de evaluare distribuite.

#### 3. Dependențe

- `stock_landed_costs`
- `l10n_ro_stock_account_tracking`

#### 4. Componente Cheie

**Modele**

- `stock.landed.cost`: câmpurile `l10n_ro_cost_type`, `l10n_ro_only_on_distributed_lines`, `l10n_ro_distributed_valuation_lines`.
- `stock.valuation.adjustment.lines`: extins cu logica românească.
- `l10n.ro.stock.valuation.adjustment.lines`: liniile de evaluare distribuite.
- `account.move`, `stock.move`: legătura cu factura furnizorului și cu mișcările de stoc.

**Vizualizări**

- `view_stock_landed_cost_form`: tipul de cost și liniile distribuite.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_stock_account_landed_cost_account](../l10n_ro_stock_account_landed_cost_account/index.md): determinarea contului și completarea costului din factură.
- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md): contabilitatea de stoc românească.
