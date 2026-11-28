# Romania - Registru de casă (localizat la `l10n_ro_cash_register_report/index.md`)

- **Nume Tehnic:** `l10n_ro_cash_register_report`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_cash_register_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cash_register_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce Registrul de casă românesc (cod 14-4-7A, conform OMFP 2634/2015) ca raport nativ Odoo (`account.report`), nu ca wizard separat. Contabilii beneficiază integral de framework-ul de raportare Enterprise: filtru de interval de date, selector de jurnale (limitat la jurnalele de casă), selector multi-companie, derulare pe niveluri și export PDF/XLSX/print direct din bara de instrumente a raportului. Raportul **nu numerotează** nimic; evidența oficială, numerotată, o ține documentul din `l10n_ro_cash_register`.

#### 2. Funcționalități Cheie

- Structură pe interval și jurnal de casă: secțiune per (jurnal, zi) cu totalurile zilei (încasări, plăți, sold final), rând de report (soldul zilei precedente), liniile de mișcare cu încasări pe debit, plăți pe credit și sold cumulat, apoi rândul de sold final, folosit drept report pentru ziua următoare.
- Soldurile se calculează pe contul de casă al jurnalului (`default_account_id`, ex. 5311), din mișcările contabile postate, cu report automat între zile; liniile de mișcare au drill-down către înregistrarea contabilă.
- **Cont corespondent** citit din aceeași notă contabilă: la o încasare contul creditat (ex. 4111), la o plată contul debitat (ex. 401). La o notă compusă apar toate conturile, în ordinea sumelor (ex. „628, 4426”); peste trei conturi, restul se trec ca „…”. La bancă, plata prin contul intermediar arată contul plății reconciliate, iar un rând de extras rămas pe contul de așteptare apare marcat „nereconciliat”.
- **Explicația operațiunii** pe fiecare rând: referința documentului, apoi eticheta liniei contabile, apoi partenerul, deci încasările, viramentele și restituirile de retur se disting fără drill-down.
- Filtru de interval de dată, selector de jurnale (doar tip casă) și multi-companie, moștenite din `account_reports`; export PDF/XLSX și tipărire din bara raportului.
- **Care variantă alegeți:** acest modul dă *raportul* (mai multe zile, analiză și verificare, necesită Odoo Enterprise); `l10n_ro_cash_register` (suita `l10n-romania`, Community) dă *documentul* numerotat, o filă per casierie și zi, pentru evidența prezentată la control. Cifrele sunt aceleași, iar cele două se pot instala împreună.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cash.register.report.handler` (`AbstractModel`, moștenește `account.report.custom.handler`): construiește liniile dinamice ale raportului — inițializează filtrul de jurnale (doar tip `cash`), calculează soldul de deschidere per cont/companie/dată, grupează mișcările pe zi și generează liniile ierarhice (secțiune zi → report → mișcări → sold final), plus contul corespondent și explicația rândului. Tipul de jurnal (`_journal_type`) și eticheta secțiunii de zi (`_day_section_label`) sunt metode-hook, suprascrise de modulul soră [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md) pentru jurnalele de bancă. Pe 20.0 liniile sunt obiecte `AccountReportLineData`, iar coloanele se construiesc conform `account_reports` 20.

**Vizualizări**

Nu există vizualizări (`views/`) proprii; interfața este generată de framework-ul `account_reports` pe baza definiției raportului.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Configurația raportului e în `data/cash_register_report.xml`:

- `l10n_ro_cash_register_report` (`account.report`): raportul „Cash Register (RO)”, cu filtre de interval, jurnale și multi-companie, și coloanele Receipts/Payments/Balance.
- `action_l10n_ro_cash_register_report` (`ir.actions.client`, tag `account_report`): deschide raportul.
- `menu_l10n_ro_cash_register_report`: meniul „Cash Register”, sub „Legal Statements” din Contabilitate.

#### 5. Conexiuni

- [l10n_ro_cash_register](../l10n_ro_cash_register/index.md): registrul de casă zilnic ca document numerotat; acest raport oferă o vizualizare alternativă, pe interval de date, peste aceleași mișcări de casă.
- [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md): modul soră, care reutilizează handler-ul (prin hook-urile `_journal_type` / `_day_section_label`) pentru jurnalele de bancă.
- `account_reports`: framework-ul Enterprise de raportare contabilă folosit ca bază tehnică.
