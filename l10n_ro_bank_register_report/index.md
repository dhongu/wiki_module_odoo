# Jurnal de Bancă (RO) - Raport (localizat la `l10n_ro_bank_register_report/index.md`)

- **Nume Tehnic:** `l10n_ro_bank_register_report`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_bank_register_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_bank_register_report`
- **Ultima Ingestie:** `2026-07-19`

#### 1. Sumar

Modulul aduce Jurnalul de bancă românesc ca raport nativ Odoo (`account.report`), cu aceeași structură zilnică ca Registrul de casă (modulul `l10n_ro_cash_register_report`, pe care îl extinde direct — moștenește handler-ul acestuia). Soldurile se calculează pe contul jurnalului de bancă (`default_account_id`, ex. 5121.x), din mișcările contabile postate, cu report automat al soldului între zile, astfel încât soldul contabil 512x se confruntă direct cu extrasul bancar. Spre deosebire de Registrul de casă (formular tipizat 14-4-7A), jurnalul de bancă nu are un formular impus prin lege — raportul urmează forma uzuală din practica contabilă românească.

#### 2. Funcționalități Cheie

- Secțiune per (jurnal, zi), cu antet care afișează **contul și jurnalul** (ex. „5121.2 BANCA TRANSILVANIA — 26.01.2026") și totalurile zilei: încasări, plăți, sold final.
- Rând de report al soldului din ziua precedentă.
- Linii de mișcare ale contului bancar, cu încasările pe debit, plățile pe credit și sold cumulat.
- Rând de sold final, folosit drept report pentru ziua următoare.
- Filtrul de jurnale limitat automat la jurnalele de tip **bancă** (câte unul per cont bancar/monedă).
- Drill-down din liniile de mișcare direct către înregistrarea contabilă (`account.move.line`).
- Filtru de interval de dată, selector de jurnale și selector multi-companie, moștenite din framework-ul `account_reports`.
- Export PDF/XLSX și tipărire, disponibile nativ din bara de instrumente a raportului.

#### 3. Dependențe

- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.bank.register.report.handler` (`AbstractModel`, moștenește `l10n.ro.cash.register.report.handler` din `l10n_ro_cash_register_report`): suprascrie doar două puncte de extensie ale handler-ului părinte — `_journal_type()` returnează `'bank'` în loc de `'cash'` (limitează filtrul de jurnale și interogarea la jurnalele bancare) și `_day_section_label()` construiește antetul de secțiune cu codul contului jurnalului urmat de numele acestuia (ex. „5121.2 BANCA TRANSILVANIA"), esențial când există mai multe conturi bancare. Toată logica de calcul a soldurilor, generare de linii și coloane rămâne moștenită neschimbată din handler-ul de bază.

**Vizualizări**

Nu există vizualizări (`views/`) proprii; interfața este generată integral de framework-ul `account_reports` pe baza definiției raportului.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul definește în schimb configurația raportului prin date (`data/bank_register_report.xml`):

- `l10n_ro_bank_register_report` (`account.report`): definește raportul „Bank Journal (RO)", cu filtre de interval de dată, jurnale (bancă) și multi-companie (selector), și coloanele Receipts/Payments/Balance.
- `action_l10n_ro_bank_register_report` (`ir.actions.client`, tag `account_report`): acțiunea client care deschide raportul.
- `menu_l10n_ro_bank_register_report`: meniul „Bank Journal", sub „Legal Statements" din meniul Contabilitate.

#### 5. Conexiuni

- [l10n_ro_registru_jurnal](../l10n_ro_registru_jurnal/index.md): registrul-jurnal cronologic pe toate jurnalele (inclusiv bancă); acest raport oferă în schimb o vedere per cont bancar, pe zile, cu sold reportat — utilă direct pentru reconcilierea cu extrasul.
- [l10n_ro_sale_receipt_type_report](../l10n_ro_sale_receipt_type_report/index.md): unifică încasările bancare (OP/online) cu cele de la casa de marcat într-o singură reconciliere pe canal; acest raport rămâne, în schimb, un registru clasic pe un singur cont, pe zile.
- `account_reports`: framework-ul Enterprise de raportare contabilă folosit ca bază tehnică (filtre, coloane, export PDF/XLSX).
