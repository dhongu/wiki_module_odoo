# Registrul-Jurnal (RO) - Raport (localizat la `l10n_ro_registru_jurnal/index.md`)

- **Nume Tehnic:** `l10n_ro_registru_jurnal`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_registru_jurnal
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_registru_jurnal`
- **Ultima Ingestie:** `2026-07-19`

#### 1. Sumar

Modulul aduce Registrul-jurnal (cod 14-1-1) ca raport nativ Odoo (`account.report`), conform Legii contabilității nr. 82/1991 art. 20 și OMFP 2634/2015: listarea cronologică a tuturor notelor contabile postate, din toate jurnalele, cu perechea cont debitor/cont creditor pe fiecare rând și totaluri zilnice. Rapoartele standard Enterprise nu acoperă acest gol — *Journal Report* grupează pe jurnal, iar *General Ledger* grupează pe cont — niciunul nu produce registrul cronologic unic cerut de lege. Modulul e vizibil automat doar pentru companiile cu Țara = România.

#### 2. Funcționalități Cheie

- Secțiune per zi, pliabilă, cu totalul zilei (Debit = Credit).
- Rând numerotat per notă contabilă: Nr. crt. continuu pe toată perioada, Data, Explicație, Document, **Cont debitor**, **Cont creditor**, Debit, Credit, Jurnal.
- Note compuse (1:N sau M:N): partea multiplă se afișează cu convenția **„%"** pe rândul numerotat (aceeași convenție folosită și de exportul SAGA), iar conturile componente apar dedesubt ca rânduri nenumerotate, cu sumele lor.
- Rând de total perioadă — egalitatea Debit = Credit se verifică la fiecare nivel; totalurile însumează doar rândurile numerotate, fără dublarea sumelor componentelor.
- Filtru de interval de dată, selector de jurnale, selector multi-companie și unfold all, moștenite din framework-ul `account_reports`.
- Drill-down la nota contabilă (rând numerotat, către `account.move`) sau la linia contabilă componentă (rând nenumerotat, către `account.move.line`).
- Export PDF/XLSX direct din bara de instrumente a raportului.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.registru.jurnal.report.handler` (`AbstractModel`, moștenește `account.report.custom.handler`): handler complet autonom, fără dependență de motorul de interogare standard al `account_reports` — construiește totul prin SQL brut pe `account_move_line`/`account_move`, filtrat pe stare postată și interval/jurnale selectate. Grupează liniile pe zi și, în cadrul zilei, pe notă contabilă; pentru fiecare notă determină perechea cont debitor/cont creditor (folosind convenția „%" pentru notele compuse) și generează liniile ierarhice (zi → notă numerotată → componente → total perioadă).

**Vizualizări**

Nu există vizualizări (`views/`) proprii; interfața este generată integral de framework-ul `account_reports` pe baza definiției raportului.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul definește în schimb configurația raportului prin date (`data/registru_jurnal_report.xml`):

- `l10n_ro_registru_jurnal_report` (`account.report`): definește raportul „Journal Register (RO)", cu filtre de interval de dată, jurnale și multi-companie, și coloanele No./Date/Document/Debit Account/Credit Account/Debit/Credit/Journal.
- `action_l10n_ro_registru_jurnal_report` (`ir.actions.client`, tag `account_report`): acțiunea client care deschide raportul.
- `menu_l10n_ro_registru_jurnal_report`: meniul „Journal Register", sub „Legal Statements" din meniul Contabilitate.

#### 5. Conexiuni

- [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md): acoperă coloana „Cont Corespondent" în Cartea Mare standard — complementar acestui registru, care produce lista cronologică pe toate jurnalele, nu detalierea per cont.
- [l10n_ro_cash_register](../l10n_ro_cash_register/index.md): modulul operațional de registru de casă zilnic; ambele documentează operațiuni contabile, dar acesta din urmă e limitat la casă, în timp ce registrul-jurnal acoperă toate jurnalele.
- [deltatech_saga](../deltatech_saga/index.md): folosește aceeași convenție „%" pentru notele compuse la exportul către SAGA — semnalul de compatibilitate menționat explicit în cod.
- [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md): oferă o vedere alternativă, per cont bancar și pe zile, cu sold reportat; acest registru rămâne cronologic, pe toate jurnalele, fără solduri cumulate.
- `account_reports`: framework-ul Enterprise de raportare contabilă folosit ca bază tehnică (filtre, coloane, export PDF/XLSX).
