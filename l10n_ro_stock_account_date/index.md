# Romania - Stock Accounting Date

- **Nume Tehnic:** `l10n_ro_stock_account_date`
- **Versiune:** `20.0.0.2.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock_account_date
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_stock_account_date
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite alegerea unei „Date contabile” pentru operațiunile de stoc, astfel încât recepțiile și livrările să poată fi contabilizate la data reală a documentului, nu neapărat la data validării. Pentru companiile românești datele din viitor sunt blocate, iar data se poate restrânge la perioada începând cu prima zi a lunii anterioare.

#### 2. Funcționalități Cheie

- Câmp `Data contabilă` pe picking, folosit la validarea operațiunii și la mișcările de stoc rezultate.
- Blocarea datelor viitoare pentru companiile românești.
- Posibilitatea de restricționare a datei de la prima zi a lunii precedente.
- Câmpul apare în formularul și în lista de picking-uri, precum și în filtrul de căutare.

#### 3. Dependențe

- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking`: câmpul `l10n_ro_accounting_date`; aplicat în `_action_done`.
- `stock.move`: propagă data contabilă pe mișcări.
- `stock.quant`: extins pentru respectarea datei contabile.

**Vizualizări**

- `view_picking_form`, `vpicktree`, `view_picking_internal_search`: câmpul și filtrarea după data contabilă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_stock_account_date_wizard](../l10n_ro_stock_account_date_wizard/index.md): aceeași dată în wizard-urile de confirmare.
