# Romania - Registru de bancă (localizat la `l10n_ro_bank_register_report/index.md`)

- **Nume Tehnic:** `l10n_ro_bank_register_report`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_bank_register_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_bank_register_report`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul aduce Jurnalul de bancă românesc ca raport nativ Odoo (`account.report`), cu aceeași structură zilnică ca Registrul de casă (modulul `l10n_ro_cash_register_report`, pe care îl extinde). Soldurile se calculează pe contul jurnalului de bancă (`default_account_id`, ex. 5121.x), din mișcările contabile postate, cu report automat al soldului între zile, astfel încât soldul contabil 512x se confruntă direct cu extrasul bancar. Spre deosebire de Registrul de casă (formular tipizat 14-4-7A), jurnalul de bancă nu are un formular impus prin lege — raportul urmează forma uzuală din practica contabilă românească.

#### 2. Funcționalități Cheie

- Secțiune per (jurnal, zi), cu antet care afișează **contul și jurnalul** (ex. „5121.2 BANCA TRANSILVANIA — 26.01.2026") și totalurile zilei: încasări, plăți, sold final.
- Rând de report al soldului din ziua precedentă.
- Linii de mișcare ale contului bancar, cu încasările pe debit, plățile pe credit, **cont corespondent** (la o notă compusă, toate conturile în ordinea sumelor; la o plată trecută prin contul intermediar, contul plății reconciliate; pe contul de așteptare, marcat „nereconciliat") și sold cumulat.
- Rând de sold final, folosit drept report pentru ziua următoare.
- Filtrul de jurnale limitat automat la jurnalele de tip **bancă** (câte unul per cont bancar / monedă).
- Interval de dată, selector de jurnale și companii, fold/unfold, drill-down la nota contabilă și export PDF/XLSX/tipărire, moștenite din framework-ul de raportare Enterprise.

#### 3. Dependențe

- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md)

#### 4. Componente Cheie

Analiza codului pentru această secțiune a fost omisă, conform fluxului de ingestie din schema wiki: fișierul `readme/DESCRIPTION.md` este prezent și nu solicită explicit detalierea componentelor tehnice. Configurația raportului este definită prin date în `data/bank_register_report.xml`; modulul nu are vizualizări proprii, iar interfața este generată de framework-ul `account_reports`.

#### 5. Conexiuni

- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md): Registrul de casă, a cărui structură zilnică și al cărui handler sunt extinse de acest modul.
