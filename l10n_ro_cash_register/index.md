# Registru de casă RO (localizat la `l10n_ro_cash_register/index.md`)

- **Nume Tehnic:** `l10n_ro_cash_register`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_cash_register
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_cash_register`
- **Ultima Ingestie:** `2026-08-15`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un registru de casă zilnic pentru jurnalele de tip numerar și leagă operațiunile de încasare, plată și transfer direct de soldul casei. Pentru fiecare combinație de jurnal de casă și dată există un singur registru, cu sold inițial și sold final calculate automat din mișcările contabile postate pe contul de casă. Începând cu versiunea 19.0.1.2.0, soldurile nu mai rămân înghețate la momentul creării registrului: se recalculează automat la fiecare postare, anulare sau ștergere a unei note contabile care atinge casieria, pentru ziua respectivă și pentru toate zilele ulterioare din același jurnal — conform cerinței OMFP 2634/2015 de reluare automată a soldurilor. Raportul PDF tipărit urmează acum formularul oficial „Registru de casă, cod 14-4-7A". Modulul este soluția operațională pentru partea de registru de casă din localizarea românească, oferind casierilor și contabililor un instrument controlat pentru operarea numerarului și tipărirea registrului. Modulul nu acoperă importul extraselor bancare MT940 și nici reconcilierea bancară automată; acestea rămân module complementare separate.

#### 2. Funcționalități Cheie

- Model de registru de casă, organizat pe zi și pe jurnal de casă (un registru unic per combinație), cu numerotare pe secvență derivată din codul jurnalului.
- Calcul automat de sold inițial și sold final din mișcările contabile postate pe contul de casă, **recalculat automat** la postarea, anularea sau ștergerea oricărei note contabile care atinge contul de casă — pentru ziua respectivă și pentru toate zilele ulterioare din același jurnal (înainte se calcula o singură dată, la creare, și rămânea înghețat până la un Refresh manual).
- Liniile registrului se listează în ordine cronologică (nu în ordinea descrescătoare implicită a înregistrărilor contabile) și filtrează explicit pe companie, evitând contaminarea între companii care ar partaja același cont de casă.
- Acces rapid la încasare, plată și operațiune de casă direct din formularul registrului.
- Wizard de operațiune casă (Cash In / Cash Out) care generează și postează automat nota contabilă cu contul de casă și contul corespondent.
- Generare automată a registrului de casă la postarea plăților pe jurnalul de tip numerar.
- Acțiune „Generate Missing Cash Register" pentru crearea registrelor lipsă pentru toate zilele cu mișcări.
- Buton **Tipărire** (`action_print`) în formularul și în lista registrelor, alături de raportul PDF existent.
- Raport PDF conform formularului oficial **Registru de casă, cod 14-4-7A**: coloane Nr. act de casă, Nr. anexe (numărul de atașamente ale notei contabile, prin `_l10n_ro_annex_count`) și Explicații, rând „Sold reportat din ziua precedentă", totaluri pe rânduri distincte (Total încasări, Total plăți, Sold la sfârșitul zilei), rubrici de semnătură pentru casier și compartimentul financiar-contabil, plus mențiunea programului informatic și a versiunii (`_l10n_ro_software_signature`), cerută de OMFP 2634/2015, Anexa 1 pct. 58 lit. k).
- Deschiderea directă a registrului de casă din jurnalul cash pentru companiile din România.
- Cron pregătit pentru generarea registrelor lipsă, livrat inactiv.
- Script de migrare (`migrations/19.0.1.2.0/post-migration.py`) care recalculează soldurile registrelor existente la actualizarea modulului.

#### 3. Dependențe

- `account`
- [l10n_ro_account_sequence](../l10n_ro_account_sequence/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cash.register`: modelul principal al registrului de casă, pe zi și jurnal; calculează `balance_start`/`balance_end` din mișcările postate pe contul de casă, expune acțiunile de încasare/plată/operațiune, `action_refresh`, `action_print` și `_l10n_ro_software_signature` (menținerea programului informatic pe raport).
- `account.move` (extindere, `models/account_move.py`): suprascrie `_post`, `button_draft` și `unlink` pentru a recalcula (`action_refresh`) registrele de casă afectate — determinate prin `_l10n_ro_cash_registers_to_refresh`, care caută jurnalele de tip cash atinse de liniile pe cont `asset_cash` și registrele lor cu dată egală sau ulterioară.
- `account.move.line` (extindere, `models/account_move_line.py`): adaugă `_l10n_ro_annex_count` (numărul de atașamente ale notei contabile, pentru coloana „Nr. anexe" din raport); `print_cash_operation` rămâne un stub gol, apelat de un buton ascuns din listă.
- `account.payment` (extindere, `models/account_payment.py`): la `action_post`, dacă jurnalul este de tip cash, creează automat registrul zilei dacă lipsește; `_compute_journal_id` este sărită când contextul `keep_journal` e prezent (folosit de acțiunile de încasare/plată deschise din registru).
- `account.journal` (extindere, `models/account_journal_dashboard.py`): `open_action`/`open_action_with_context` redirecționează jurnalele cash ale companiilor RO către registrul de casă; `generate_missing_cash_register` creează registrele lipsă pentru toate zilele cu mișcări postate pe cont, plus ziua curentă.

**Vizualizări**

- `view_cash_register_tree` / `view_cash_register_form`: listă și formular pentru registru, cu butoanele Tipărire, Împrospătare, Încasare, Plată, Operație; formularul afișează sold inițial/final și liniile registrului în ordine cronologică.
- `view_cash_register_search`: căutare/filtrare după jurnal, partener și dată, cu grupare pe jurnal.
- `report_cash_register` (`views/report_cash_register.xml`): șablonul QWeb al raportului PDF „Registru de casă, cod 14-4-7A".
- `cash_register_operation_view.xml`: formularul wizardului de operațiune casă (Cash In / Cash Out).

**Acțiuni Automate / Acțiuni Server**

- `action_generate_missing_cash_register`: acțiune server pe `account.journal`, legată la meniul jurnalului, apelează `generate_missing_cash_register()`.
- `action_remove_outstanding_accounts`: acțiune server pe `account.journal` (nativ Odoo, expusă și pe jurnalul cash).
- `ir_cron_data.xml`: cron pentru generarea automată a registrelor lipsă, livrat **inactiv** (dezactivare explicită, nu ștergere).

#### 5. Conexiuni

- [l10n_ro_account_sequence](../l10n_ro_account_sequence/index.md): furnizează secvențele localizate folosite la numerotarea registrului de casă.
- `account`: jurnale, plăți și note contabile pe care se bazează registrul.
- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md): același registru de casă, dar ca raport nativ `account.report` pe interval de date, cu export PDF/XLSX — complementar acestui modul, care ține evidența operațională zi de zi.
- [l10n_ro_cash_bank_enhanced](../l10n_ro_cash_bank_enhanced/index.md): completări pe fluxul de casă/bancă, funcțional adiacent registrului de casă.
- [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md): echivalentul de partea de bancă al registrului de casă, pentru extrasele bancare.
- `l10n_ro_account_bank_statement_import_mt940_base`: bază pentru importul extraselor bancare MT940, complementar pe partea de bancă a aceluiași domeniu funcțional (FR-28).
- `l10n_ro_account_bank_statement_import_mt940_bcr` / `..._ing` și alte adaptoare de bancă: importul extraselor pentru diverse bănci, în afara acestui modul.
