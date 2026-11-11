# Romania - Jurnal de stoc per depozit (localizat la `l10n_ro_stock_account_warehouse_journal/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_account_warehouse_journal`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_account_warehouse_journal
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_warehouse_journal`
- **Ultima Ingestie:** `2026-11-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Odoo 19 înregistrează toate notele contabile de stoc ale unei companii într-un singur jurnal de stoc. Modulul permite firmelor care țin evidența pe depozite să folosească un jurnal propriu pentru fiecare depozit, astfel încât notele de stoc ale fiecărui depozit să fie numerotate și verificate separat.

#### 2. Funcționalități Cheie

- Câmpul **Jurnal de stoc** pe depozit (dependent de companie, vizibil doar utilizatorilor cu drepturi de Contabilitate), configurat din *Inventar > Configurare > Depozite*; se folosesc jurnale de tip *Diverse*.
- Notele contabile ale mișcărilor care intră sau ies dintr-o locație internă a depozitului se postează în jurnalul acestuia; dacă e gol, se folosește jurnalul de stoc al companiei.
- Acoperă nota de stoc standard a evaluării native Odoo 19. Notele suplimentare românești din `l10n_ro_stock_account` și compensarea stocului negativ FIFO sunt acoperite de modulul-punte `l10n_ro_stock_account_warehouse_journal_extra`, nu de acest modul.
- Transferul între două depozite cu jurnale de stoc diferite este refuzat, deoarece nota contabilă nu poate aparține ambelor jurnale.
- Migrare din 18.0: câmpul făcea parte din `l10n_ro_stock_account` și a fost eliminat la migrarea la 19.0; păstrează același nume tehnic (`l10n_ro_property_stock_journal_id`). Modulul se instalează în aceeași rulare cu migrarea `l10n_ro_stock_account` (sau înaintea ei), altfel jurnalele setate în 18.0 trebuie reintroduse.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse` (extins): câmpul `l10n_ro_property_stock_journal_id` (Many2one către `account.journal`, tip general, dependent de companie).
- `stock.move` (extins): determină jurnalul depozitului și împarte mișcările pe jurnale la `_create_account_move`; refuză transferurile între depozite cu jurnale diferite.
- `account.move` (extins): la creare, înlocuiește jurnalul de stoc al companiei cu cel al depozitului (indicat prin contextul `l10n_ro_stock_journal_id`).

**Vizualizări**

- `view_warehouse`: extinde formularul depozitului (`stock.view_warehouse`) cu câmpul Jurnal de stoc, după partener (vizibil grupului Contabilitate / Manager).

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `l10n_ro_stock_account_warehouse_journal_extra`: modulul-punte care extinde acoperirea la notele suplimentare românești din `l10n_ro_stock_account` și la compensarea stocului negativ FIFO.
- `l10n_ro_stock_account`: modulul din care provenea câmpul în 18.0 (fără dependență directă în 19.0).
