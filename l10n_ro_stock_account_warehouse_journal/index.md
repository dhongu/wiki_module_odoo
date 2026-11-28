# Romania - Stock Journal per Warehouse

- **Nume Tehnic:** `l10n_ro_stock_account_warehouse_journal`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_account_warehouse_journal
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_stock_account_warehouse_journal
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Notele contabile de stoc ale fiecărui depozit se postează în jurnalul propriu al depozitului. Odoo postează implicit toate notele de stoc ale unei companii în jurnalul de stoc al companiei; firmele cu mai multe depozite pot astfel numerota și verifica separat notele fiecărui depozit.

#### 2. Funcționalități Cheie

- Câmpul **Stock Journal** pe depozit (dependent de companie, vizibil utilizatorilor cu drepturi de Contabilitate / Administrator): notele mișcărilor care intră sau ies dintr-o locație a depozitului se postează în el; dacă e gol, se folosește jurnalul de stoc al companiei.
- Acoperă nota de stoc standard a evaluării native Odoo; notele suplimentare românești din `l10n_ro_stock_account` sunt acoperite de modulul-punte [l10n_ro_stock_account_warehouse_journal_extra](../l10n_ro_stock_account_warehouse_journal_extra/index.md).
- O mișcare care generează notă între două depozite cu jurnale de stoc diferite este refuzată, fiindcă nota nu poate aparține ambelor.
- Configurare: se creează câte un jurnal de tip *Miscellaneous* pe depozit, apoi se setează în *Inventar > Configurare > Warehouses*.
- Până la 18.0 câmpul (`l10n_ro_property_stock_journal_id`) făcea parte din `l10n_ro_stock_account`; la migrare din 18.0 modulul se instalează în aceeași rulare cu migrarea acestuia (sau înainte), altfel jurnalele setate se pierd.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse`: câmpul `l10n_ro_property_stock_journal_id`.
- `stock.move`: alegerea jurnalului depozitului la generarea notei și verificarea între depozite.
- `account.move`: postarea notei în jurnalul stabilit.

**Vizualizări**

- `view_warehouse`: câmpul Stock Journal pe formularul depozitului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_stock_account_warehouse_journal_extra](../l10n_ro_stock_account_warehouse_journal_extra/index.md): extinde regula la notele suplimentare ale `l10n_ro_stock_account`.
