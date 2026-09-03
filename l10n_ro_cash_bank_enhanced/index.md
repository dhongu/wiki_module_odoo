# Romania - Cash and Bank Enhanced (localizat la `l10n_ro_cash_bank_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_cash_bank_enhanced`
- **Versiune:** `19.0.1.1.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_cash_bank_enhanced](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_cash_bank_enhanced)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cash_bank_enhanced`
- **Ultima Ingestie:** `2026-08-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează funcționalitățile native de trezorerie din Odoo 19 Enterprise cu documentele
și controalele de casierie specifice pieței din România (FR-28 — Casierie și bancă): **dispoziția
de plată / de încasare către casierie** (cod 14-4-4, respectiv 14-4-1), alertarea automată a
tranzacțiilor bancare rămase nereconciliate și aplicarea plafoanelor legale de numerar
prevăzute de Legea 70/2015. Scopul este să reducă riscul de amenzi și erori de conformitate
legate de operațiunile cash și de reconcilierea bancară, fără să reimplementeze funcții deja
acoperite nativ de Odoo Enterprise (sincronizare bancară, OCR extrase, reconciliere automată).

#### 2. Funcționalități Cheie

- **Dispoziție de plată / de încasare către casierie (cod 14-4-4)**: documentul de casă care
  justifică o mișcare de numerar neacoperită de chitanță — restituirea contravalorii unei mărfi
  returnate, un avans de trezorerie, o plată către o persoană fizică. Registru propriu, cu
  numerotare separată pe casierie, pe sensul operațiunii și pe an; formular tipizat cu suma în
  cifre și în litere, actul de identitate al beneficiarului și cele trei semnături. Un document
  anulat își păstrează numărul, ca registrul să nu aibă goluri. Se întocmește din registru sau
  dintr-un bon de retur, când e instalat modulul de retururi POS.
- **Alertă tranzacții bancare nereconciliate**: un cron zilnic identifică liniile de extras
  bancar rămase nereconciliate după un număr configurabil de zile și creează o activitate pe
  jurnalul de bancă, asignată responsabilului de trezorerie; alertele existente se actualizează
  (numărul de tranzacții și suma totală), fără duplicare.
- **Plafoane de numerar conform Legii 70/2015**: la validarea plăților și încasărilor în
  numerar (jurnale de tip casă), sistemul blochează depășirea plafoanelor zilnice legale:
  - încasări/plăți cu persoane juridice: 5.000 RON per partener/zi;
  - încasări/plăți cu persoane fizice: 10.000 RON per partener/zi;
  - total plăți în numerar către persoane juridice: 10.000 RON/zi.
- **Anti-fragmentare (art. 1¹)**: o factură peste plafon poate fi achitată în numerar doar
  până la plafon (cumulat, indiferent de zile); diferența trebuie plătită prin bancă —
  reconcilierea unei plăți cash care ar depăși plafonul pe factură este blocată.
- **Plafon sold casierie**: un cron zilnic verifică soldul fiecărui jurnal de casă și
  alertează responsabilul de trezorerie când soldul depășește plafonul legal de 50.000 RON
  (art. 4¹ — excedentul se depune la bancă în două zile lucrătoare).
- **Plafoane configurabile**: valorile pot fi ajustate (de exemplu pentru magazinele cash and
  carry, unde plafonul legal este 10.000 RON), iar controlul poate fi dezactivat per companie.

#### 3. Dependențe

- `account_accountant`
- `l10n_ro`

#### 4. Componente Cheie

*(secțiune neanalizată din cod — DESCRIPTION.md acoperă Sumarul și Funcționalitățile Cheie,
conform fluxului de ingestie; componentele de mai jos sunt orientative, extrase direct din
structura fișierelor modulului)*

**Modele**

- `account_bank_statement_line` (extindere): logica pentru identificarea liniilor
  nereconciliate și cron-ul de alertă aferent.
- `account_journal` (extindere): cron-ul de verificare a plafonului de sold pentru jurnalele
  de casă.
- `account_partial_reconcile` (extindere): controlul anti-fragmentare la reconcilierea
  plăților cash pe facturi.
- `account_payment` (extindere): validarea plafoanelor de numerar la confirmarea plăților și
  încasărilor.
- `res_company` (extindere): câmpurile de configurare a plafoanelor și a responsabilului de
  trezorerie.
- `res_config_settings` (extindere): expune setările companiei în ecranul de configurare.
- `l10n.ro.cash.payment.order`: registrul dispozițiilor de casă. Folosește `sequence.mixin` pentru
  numerotare, cu `_get_last_sequence_domain` care filtrează pe casierie, operațiune și an —
  mixinul cere clauza `WHERE` completă, altfel interogarea de secvență iese fără `WHERE` și crapă
  în SQL. Suma în litere vine din `currency.amount_to_text`; actul de identitate al beneficiarului
  se reține pe document, nu în fișa partenerului.

**Vizualizări**

- `l10n_ro_cash_payment_order_view_list` / `_view_form` / `_view_search`: registrul dispozițiilor de
  casă, cu acțiunea și meniul din **Contabilitate → Tranzacții → Cash Orders**.
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
