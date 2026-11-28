# Romania - Casă și bancă extinse (localizat la `l10n_ro_cash_bank_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_cash_bank_enhanced`
- **Versiune:** `20.0.1.2.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_cash_bank_enhanced
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cash_bank_enhanced`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează funcționalitățile native de trezorerie din Odoo Enterprise cu documentele și controalele de casierie specifice României: un tablou „Casă și bancă”, **dispoziția de plată / de încasare către casierie** (cod 14-4-4), plafoanele legale de numerar din Legea 70/2015 și alertarea automată a tranzacțiilor bancare nereconciliate. Scopul este să reducă riscul de amenzi și erori de conformitate legate de operațiunile cash și de reconcilierea bancară, fără să reimplementeze ce acoperă deja Enterprise (sincronizare bancară PSD2, OCR extrase, reconciliere automată).

#### 2. Funcționalități Cheie

- **Tablou „Casă și bancă”**: un card pe fiecare casierie și cont bancar, cu soldul din balanță (nu din extrase), încasările și plățile din perioada aleasă, linia soldului pe 30 de zile, soldul în valută, gradul de ocupare a plafonului de casă de 50.000 RON și extrasele nereconciliate; de pe card se deschid mișcările contului și reconcilierea bancară.
- **Dispoziție de plată / de încasare către casierie (cod 14-4-4)**: documentul de casă care justifică o mișcare de numerar neacoperită de chitanță (restituirea contravalorii unei mărfi returnate, avans de trezorerie, plată către o persoană fizică). Registru propriu, în **Contabilitate → Tranzacții → Cash Orders**, numerotat separat pe casierie și sens, cu resetare anuală; suma se tipărește și în litere, cu acordul limbii române pentru leu (alte monede rămân pe implementarea nucleului). Actul de identitate al beneficiarului se reține pe document, nu în fișa partenerului; un document anulat își păstrează numărul. Se întocmește din registru sau dintr-un bon de retur, când e instalat modulul de retururi POS.
- Pentru plățile înregistrate ca `account.payment`, dispoziția se tipărește direct de pe plată, cu raportul din modulul OCA `l10n_ro_invoice_report`; registrul de aici acoperă mișcările de numerar care nu trec printr-o plată contabilă, în primul rând restituirile de la casa de marcat.
- **Alertă tranzacții bancare nereconciliate**: un cron zilnic identifică liniile de extras rămase nereconciliate după un număr configurabil de zile și creează o activitate pe jurnalul de bancă, asignată responsabilului de trezorerie; alertele existente se actualizează (număr și sumă totală), fără duplicare.
- **Plafoane de numerar conform Legii 70/2015**, verificate la validarea plăților și încasărilor în numerar (jurnale de tip casă): 5.000 RON per partener/zi pentru persoane juridice, 10.000 RON per partener/zi pentru persoane fizice, 10.000 RON/zi total plăți în numerar către persoane juridice.
- **Anti-fragmentare** (art. 3 alin. (2)–(3) și art. 4 alin. (2)): o factură peste plafon poate fi achitată în numerar doar până la plafon (cumulat, indiferent de zile); diferența se plătește prin bancă, iar reconcilierea unei plăți cash care ar depăși plafonul pe factură este blocată.
- **Plafon sold casierie**: un cron zilnic verifică soldul fiecărui jurnal de casă și alertează responsabilul de trezorerie peste 50.000 RON (art. 4² — excedentul se depune la bancă în două zile lucrătoare).
- Plafoanele sunt configurabile (ex. 10.000 RON pentru magazinele cash and carry), iar controlul poate fi dezactivat per companie.

#### 3. Dependențe

- `account_accountant`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cash.payment.order` (`mail.thread`, `sequence.mixin`): registrul dispozițiilor de casă; numerotare filtrată pe casierie, operațiune și an prin `_get_last_sequence_domain`, suma în litere formatată în modul pentru leu.
- `l10n.ro.cash.bank.dashboard`: model abstract de serviciu pentru tabloul „Casă și bancă” (`get_dashboard_data`, solduri, linii spark pe 30 de zile, extrase nereconciliate, acțiuni de deschidere a mișcărilor și a reconcilierii).
- `account.bank.statement.line` (extindere): identificarea liniilor nereconciliate și cron-ul de alertă.
- `account.journal` (extindere): cron-ul de verificare a plafonului de sold pentru jurnalele de casă.
- `account.partial.reconcile` (extindere): controlul anti-fragmentare la reconcilierea plăților cash pe facturi.
- `account.payment` și `account.move` (extinderi): validarea plafoanelor de numerar la confirmarea plăților și încasărilor.
- `res.company` / `res.config.settings` (extinderi): plafoanele, pragul de alertă și responsabilul de trezorerie.

**Vizualizări**

- `l10n_ro_cash_payment_order_view_list` / `_view_form` / `_view_search`: registrul dispozițiilor de
  casă, cu acțiunea și meniul din **Contabilitate → Tranzacții → Cash Orders**.
- `action_l10n_ro_cash_bank_dashboard` (acțiune client) și meniul `menu_l10n_ro_cash_bank_dashboard`: tabloul „Casă și bancă”, componentă OWL din `static/src/dashboard/`.
- `action_report_cash_payment_order` + șablonul `report_cash_payment_order`: formularul tipizat
  14-4-4 / 14-4-1, în engleză în cod și tradus în română prin `i18n/ro.po`.
- `res_config_settings_view_form_cash_bank`: secțiune „Cash and Bank (RO)” în Setări
  Contabilitate, cu pragul de alertă pentru nereconciliate, responsabilul de trezorerie și
  plafoanele de numerar (Legea 70/2015).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_l10n_ro_cash_balance_alert`: rulează zilnic, verifică soldul jurnalelor de casă
  față de plafonul legal și creează activitate pentru responsabilul de trezorerie la depășire.
- `ir_cron_l10n_ro_unreconciled_alert`: rulează zilnic, verifică liniile de extras bancar
  nereconciliate mai vechi decât pragul configurat și creează/actualizează activitatea pe
  jurnalul de bancă afectat.

#### 5. Conexiuni

- `account_accountant`: furnizează motorul de reconciliere automată pe care se bazează
  detectarea liniilor nereconciliate.
- `l10n_ro`: localizarea românească de bază peste care se aplică regulile Legii 70/2015.
- `account_online_synchronization`: sincronizarea bancară PSD2, folosită nativ pentru
  importul extraselor (nu este reimplementată de acest modul).
- `account_bank_statement_extract`: extragerea OCR din PDF a extraselor bancare, folosită
  nativ (nu este reimplementată de acest modul).
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): tipărește dispoziția de plată
  direct de pe `account.payment`; registrul de aici **nu dublează** acel flux, ci acoperă mișcările
  de numerar care nu trec printr-o plată contabilă.
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): alimentează registrul din bonurile de
  retur, unde restituirea stă în linia de extras a sesiunii POS și nu există `account.payment` de
  pe care să tipărești.
