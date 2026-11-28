# Romania - Stock Journal per Warehouse (OCA stock)

- **Nume Tehnic:** `l10n_ro_stock_account_warehouse_journal_extra`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_account_warehouse_journal_extra
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_stock_account_warehouse_journal_extra
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Punte între `l10n_ro_stock_account_warehouse_journal` și `l10n_ro_stock_account`. Se instalează automat când ambele sunt instalate și postează în jurnalul de stoc al depozitului și notele suplimentare românești, nu doar nota de stoc standard.

#### 2. Funcționalități Cheie

- Postează în jurnalul de stoc al depozitului notele suplimentare ale `l10n_ro_stock_account`.
- Postează în același jurnal compensarea stocului negativ FIFO.
- `auto_install`: nu cere nicio configurare proprie; jurnalul se setează pe depozit în modulul de bază.

#### 3. Dependențe

- [l10n_ro_stock_account_warehouse_journal](../l10n_ro_stock_account_warehouse_journal/index.md)
- `l10n_ro_stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.move`: extinde alegerea jurnalului depozitului la notele suplimentare.

**Vizualizări**

- Nu are.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_stock_account_warehouse_journal](../l10n_ro_stock_account_warehouse_journal/index.md): modulul de bază care definește jurnalul pe depozit.
