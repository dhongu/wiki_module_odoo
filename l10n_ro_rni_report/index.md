# Romania - Raport recepții nefacturate (408) (localizat la `l10n_ro_rni_report/index.md`)

- **Nume Tehnic:** `l10n_ro_rni_report`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_rni_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_rni_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Raportul din spatele soldului contului 408, marfă primită fără factură. Soldul creditor al lui 408 spune cât datorează firma, dar nu și pentru ce; la închiderea lunii se cere tocmai lista recepțiilor care încă își așteaptă factura, cu vechimea lor și furnizorul de la care au venit. Raportul desface soldul pe furnizor și pe document, ca un control intern la închidere; nu generează note contabile și nu intră în nicio declarație.

#### 2. Funcționalități Cheie

- Grupare pe furnizor, cu drill-down până la documentul individual (transferul de stoc, când legătura există, altfel nota contabilă).
- Pentru fiecare rând: valoarea **Recepționat**, cât s-a decontat prin **Facturat**, **Rămas** și **Vechime (zile)**, socotită până la data de sfârșit a perioadei selectate.
- Soldul este cumulat, nu al perioadei; furnizorii cu sold zero nu apar.
- Funcționează cu ambele mecanisme de 408 din suită: [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md) (nota `371 = 408`) și [l10n_ro_stock_account](../l10n_ro_stock_account/index.md) (pivotul 408 din valorizarea mișcării marcate `reception_notice`).
- Conturile 408 se iau din configurare (contul de recepție fără factură de pe gestiune, apoi cel de pe companie); în lipsă, se folosesc conturile cu codul care începe cu 408. Liniile fără partener ajung într-un rând fără nume.
- Meniu: **Contabilitate → Rapoarte → Situații legale → Recepții fără factură (408)**; export **PDF** și **XLSX**.
- Dacă modulul de închidere periodică e instalat, verificarea **Recepții fără factură (408)** din checklist confruntă soldul urmărit acolo cu cel din raport și deschide raportul.
- Pașii de lucru sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.rni.report.handler` (`AbstractModel`, extinde `account.report.custom.handler`): motorul raportului. `_l10n_ro_rni_accounts` stabilește conturile 408, iar `_report_engine_rni` (semnătura din `account_reports` 20, apel pe `formulas_dict`) construiește interogările pe `account_move_line` / `account_move`, filtrate pe conturile 408 și pe starea `posted`, cu agregări pe totaluri, furnizor și linie individuală. Nivelul următor de grupare se deduce din groupby-ul liniei.

**Vizualizări**

- Fără vizualizări XML proprii: raportul se randează prin componenta standard `account_report`, configurată din `data/rni_report.xml`.

**Acțiuni Automate / Acțiuni Server**

- Fără `ir.cron` sau `base.automation`. Definește `action_rni_report` (`ir.actions.client`, tag `account_report`), meniul `menu_rni_report` sub situațiile legale și raportul `rni_report` cu 5 coloane (Document, Recepționat, Facturat, Rămas, Vechime).

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): când e instalat, raportul preferă contul configurat pe gestiune și afișează recepția din spatele notei contabile.
- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md) (OCA): al doilea mecanism suportat, pivotul 408.
