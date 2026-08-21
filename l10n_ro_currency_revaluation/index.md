# Romania - Reevaluare Valutară (OMFP 1802) (localizat la `l10n_ro_currency_revaluation/index.md`)

- **Nume Tehnic:** `l10n_ro_currency_revaluation`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_currency_revaluation`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_currency_revaluation`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul pentru reevaluarea lunară obligatorie a soldurilor în valută conform OMFP 1802/2014, pct. 340–345, cu generare automată a diferențelor de curs valutar la conturile 665 (cheltuieli) și 765 (venituri), FĂRĂ stornare automată. Este adresat companiilor românești cu tranzacții în valută (exportatori, importatori, entități cu conturi bancare sau împrumuturi intra-grup în EUR/USD/altă valută), obligate să ajusteze lunar valoarea RON a soldurilor valutare la cursul BNR din ultima zi a lunii. Spre deosebire de comportamentul implicit al modulului Enterprise (`account_reports`), care aplică modelul IFRS „provizion + stornare a doua zi" — lăsând soldurile 665/765 la zero la finele lunii —, acest modul înregistrează diferențele definitiv, așa cum cere legislația română, astfel încât bilanțul și contul de profit și pierdere reflectă corect diferențele de curs ale perioadei. Reevaluarea lunii următoare este calculată incremental față de cursul ultimei reevaluări (nu față de cursul istoric al documentului), iar întregul proces este urmărit printr-un model de audit trail cu stări clare (ciornă → postată → anulată), oferind contabilului trasabilitate completă și control asupra închiderii lunare.

#### 2. Funcționalități Cheie

- Reevaluare lunară a soldurilor în valută cu generarea automată a diferențelor de curs valutar pe conturile 665 (cheltuieli) și 765 (venituri).
- Diferențe de curs înregistrate definitiv, FĂRĂ stornare automată în luna următoare — corect conform OMFP 1802/2014 (vs. comportamentul IFRS din Enterprise).
- Model de audit trail `l10n.ro.currency.revaluation` cu state machine: ciornă → postată → anulată, urmărit cu `mail.thread`/`mail.activity.mixin`.
- Calcul automat al soldurilor reziduale valutare la data reevaluării, printr-o interogare SQL (cu CTE) care ține cont de reconcilierile parțiale efectuate până la acea dată.
- Diferența la decontare calculată incremental față de ultima reevaluare (nu față de cursul istoric): liniile de ajustare sunt marcate `l10n_ro_is_fx_revaluation` și poartă valuta elementului cu `amount_currency=0`, astfel încât soldul contabil rezidual reportat în luna următoare include ajustările deja postate; la decontarea unui element, partea nerealizată rămasă se „realizează" (stornare) la reevaluarea următoare.
- Raport de audit PDF per reevaluare (`action_print_audit_report`): perioadă, companie/CUI, jurnal, cursuri BNR per linie, sold rezidual valutar/contabil, diferențe 665/765 cu totaluri.
- Excluderea automată a conturilor nemonetare (clase 1xx capitaluri, 3xx stocuri, venituri și cheltuieli) — se reevaluează doar conturile monetare relevante (ex.: 5124, 5314, 4111, 401, 451, 461, 462, 267, 508).
- Override al wizard-ului Enterprise `account.multicurrency.revaluation.wizard`, cu opțiunea „Fără stornare automată (OMFP 1802)" activă implicit pentru companiile din România.
- Temei legal: OMFP 1802/2014, pct. 340–345 (elemente monetare în valută, evaluare la cursul BNR de la data bilanțului).

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.currency.revaluation`: Sesiunea de reevaluare valutară (audit trail). Implementează state machine-ul (ciornă/postată/anulată) cu constrângere de unicitate `UNIQUE(date, company_id)` și metodele `action_compute` (calculează soldurile reziduale eligibile și populează liniile), `action_post` (generează nota contabilă fără stornare, cu cerința prealabilă a conturilor 665/765 configurate pe companie), `action_cancel` (stornează nota contabilă în roșu prin `_reverse_moves`), `action_view_move` (deschide nota contabilă generată) și `action_print_audit_report` (deschide raportul PDF de audit). Moștenește `mail.thread` și `mail.activity.mixin` pentru istoric și activități.
- `l10n.ro.currency.revaluation.line`: Linie de reevaluare per cont/valută, cu sold rezidual valutar (`balance_currency`), sold contabil (`balance_book`), cursul BNR nou (`rate_new`), soldul recalculat (`balance_new`), diferența (`adjustment`) și tipul diferenței (`diff_type` — pierdere 665/câștig 765).
- `account.move.line` (extindere): adaugă câmpul `l10n_ro_is_fx_revaluation`, care marchează liniile de ajustare generate de reevaluarea RO, pentru a reporta corect ajustările în soldul contabil al lunii următoare.
- `account.multicurrency.revaluation.wizard` (extindere): Adaugă câmpul `l10n_ro_no_reversal` (bifat implicit pentru companiile din România) și suprascrie `create_entries` pentru a genera înregistrări fără stornare automată (`_l10n_ro_create_entries_no_reversal`) când compania este din România.

**Vizualizări**

- `view_l10n_ro_currency_revaluation_tree`: Lista sesiunilor de reevaluare valutară, cu totaluri de pierderi/câștiguri și badge de stare.
- `view_l10n_ro_currency_revaluation_form`: Formularul sesiunii, cu butoanele Compute/Post Entry/Cancel/View Accounting Entry/Audit Report și liniile de reevaluare.
- `view_l10n_ro_currency_revaluation_search`: Filtre (ciornă/postată/anulată) și grupări (companie, stare) pentru sesiuni.
- `action_l10n_ro_currency_revaluation`: Acțiunea de fereastră care deschide sesiunile, accesibilă din meniul „RO Currency Revaluation" (sub Contabilitate → Intrări contabile).

**Rapoarte**

- `action_report_currency_revaluation` / template `report_currency_revaluation`: raport PDF de audit al reevaluării, cu perioadă, companie/CUI, jurnal, cursuri BNR, solduri și totaluri 665/765, disponibil ca acțiune de raportare legată de model.

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Procesul de reevaluare este declanșat manual de contabil (nu există cron-uri sau reguli de automatizare definite).

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): diferențele de curs aferente soldurilor de furnizori (ex. contul 408 din recepția fără factură) intră în perimetrul reevaluat de acest modul.
- [l10n_ro_expense_currency](../l10n_ro_expense_currency/index.md): avansurile în valută (cont 542) sunt tratate separat, dar se corelează cu reevaluarea soldurilor monetare în valută.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): reevaluarea valutară este un pas din checklist-ul de închidere lunară.
- `account_reports`: modulul extinde wizard-ul Enterprise de reevaluare multi-valută (`account.multicurrency.revaluation.wizard`), dezactivând stornarea automată pentru companiile din România.
