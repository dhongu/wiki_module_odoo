# Registru de Casă (RO) - Raport (localizat la `l10n_ro_cash_register_report/index.md`)

- **Nume Tehnic:** `l10n_ro_cash_register_report`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_cash_register_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cash_register_report`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce Registrul de casă românesc (cod 14-4-7A, conform OMFP 2634/2015) ca raport nativ Odoo (`account.report`), în locul unui wizard separat. Astfel, contabilii beneficiază integral de framework-ul de raportare Enterprise: filtru de interval de date, selector de jurnale (limitat la jurnalele de casă), selector multi-companie, derulare pe niveluri (fold/unfold) și export PDF/XLSX/print direct din bara de instrumente a raportului, fără a mai fi nevoie de un ecran dedicat.

#### 2. Funcționalități Cheie

- Structurare pe secțiuni per (jurnal, zi), cu totalurile zilei: încasări, plăți și sold final.
- Rând de report al soldului din ziua precedentă (sold inițial al zilei).
- Linii de mișcare ale casei, cu încasările pe debit, plățile pe credit și sold cumulat.
- Rând de sold final, folosit drept report pentru ziua următoare.
- Calculul soldurilor pe contul de casă al jurnalului (`default_account_id`, ex. 5311), din mișcările contabile postate, cu report automat al soldului între zile.
- Drill-down din liniile de mișcare direct către înregistrarea contabilă (`account.move.line`).
- Filtru de interval de dată, selector de jurnale (doar jurnale de tip casă) și selector multi-companie, moștenite din framework-ul `account_reports`.
- Export PDF/XLSX și tipărire, disponibile nativ din bara de instrumente a raportului.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cash.register.report.handler` (`AbstractModel`, moștenește `account.report.custom.handler`): construiește liniile dinamice ale raportului — inițializează filtrul de jurnale (doar tip `cash`), calculează soldul de deschidere per cont/companie/dată printr-o interogare SQL brută pe `account_move_line`, grupează mișcările pe zi și generează liniile ierarhice (secțiune zi → report → mișcări → sold final), fiecare cu coloane de debit/credit/sold construite prin `_build_column_dict`. De la versiunea `19.0.1.0.1`, tipul de jurnal listat (`_journal_type`) și eticheta secțiunii de zi (`_day_section_label`) au fost extrase în metode-hook, astfel încât modulul soră [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md) le poate suprascrie pentru jurnalele de bancă, fără duplicare de logică — refactor fără schimbare funcțională pentru acest modul.

**Vizualizări**

Nu există vizualizări (`views/`) proprii; interfața este generată integral de framework-ul `account_reports` pe baza definiției raportului.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul definește în schimb configurația raportului prin date (`data/cash_register_report.xml`):

- `l10n_ro_cash_register_report` (`account.report`): definește raportul „Cash Register (RO)”, cu filtre de interval de dată, jurnale și multi-companie (selector), și coloanele Receipts/Payments/Balance.
- `action_l10n_ro_cash_register_report` (`ir.actions.client`, tag `account_report`): acțiunea client care deschide raportul.
- `menu_l10n_ro_cash_register_report`: meniul „Cash Register”, plasat sub „Legal Statements” din meniul Contabilitate.

#### 5. Conexiuni

- [l10n_ro_cash_register](../l10n_ro_cash_register/index.md): modulul operațional de registru de casă zilnic (document, casierie, tipărire clasică); acest raport oferă o vizualizare alternativă, nativă `account.report`, pe interval de date, peste aceleași mișcări de casă postate în contabilitate.
- [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md): modul soră, publicat separat pe Odoo Apps, care reutilizează handler-ul acestui modul (prin hook-urile `_journal_type`/`_day_section_label`) pentru a genera aceeași structură zilnică de raport, dar pe jurnalele de bancă.
- `account_reports`: framework-ul Enterprise de raportare contabilă folosit ca bază tehnică (filtre, coloane, export PDF/XLSX).
