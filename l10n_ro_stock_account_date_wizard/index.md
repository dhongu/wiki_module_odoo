# Romania - Stock Accounting Date Wizard

- **Nume Tehnic:** `l10n_ro_stock_account_date_wizard`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock_account_date_wizard
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_stock_account_date_wizard
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Aduce selecția „Datei contabile” în wizard-urile de confirmare a operațiunilor de stoc, astfel încât utilizatorul să o poată seta direct la validarea unei livrări sau recepții cu backorder.

#### 2. Funcționalități Cheie

- Câmpul `Data contabilă` în wizard-ul de confirmare backorder; ascuns când picking-urile aparțin unei companii non-românești (compania se ia din picking-uri, nu din compania curentă).
- Data nu se propune implicit la data curentă: se scrie pe picking doar dacă utilizatorul o setează, iar ștergerea ei nu șterge o dată deja existentă pe picking.
- Data propusă este data contabilă comună tuturor picking-urilor; dacă diferă, câmpul rămâne gol.
- Butoanele *Validate* și *No Backorder* scriu data pe aceleași picking-uri, cele validate de nucleul stoc, inclusiv cele fără backorder.

#### 3. Dependențe

- [l10n_ro_stock_account_date](../l10n_ro_stock_account_date/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.backorder.confirmation` (wizard): câmp pentru data contabilă și scrierea ei pe picking-uri.

**Vizualizări**

- `view_backorder_confirmation`: câmpul în wizard-ul de confirmare backorder.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md): contabilitatea de stoc pe care o completează indirect.
