# Romania - Reevaluare valutară (OMFP 1802) (localizat la `l10n_ro_currency_revaluation/index.md`)

- **Nume Tehnic:** `l10n_ro_currency_revaluation`
- **Versiune:** `19.0.1.3.2`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_currency_revaluation`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_currency_revaluation`
- **Ultima Ingestie:** `2026-10-13`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul pentru reevaluarea lunară obligatorie a soldurilor în valută conform OMFP 1802/2014 (pct. 325 alin. (1)-(2), pct. 322 alin. (2) și pct. 329 alin. (1)), cu generare automată a diferențelor de curs valutar la conturile 665 (cheltuieli) și 765 (venituri), FĂRĂ stornare automată. Este adresat companiilor românești cu tranzacții în valută (exportatori, importatori, entități cu conturi bancare sau împrumuturi intra-grup în EUR/USD/altă valută), obligate să ajusteze lunar valoarea RON a soldurilor valutare la cursul BNR din ultima zi a lunii. Spre deosebire de comportamentul implicit al modulului Enterprise (`account_reports`), care aplică modelul IFRS „provizion + stornare a doua zi", acest modul înregistrează diferențele definitiv, așa cum cere legislația română, astfel încât bilanțul și contul de profit și pierdere reflectă corect diferențele de curs ale perioadei. Creanțele și datoriile se reevaluează pe fiecare partener, deci fișa clientului/furnizorului în lei este la zi, iar câștigul unui partener nu se mai compensează cu pierderea altuia. Reevaluarea lunii următoare este incrementală față de cursul ultimei reevaluări, iar procesul este urmărit printr-un model de audit trail (ciornă → postată → anulată).

#### 2. Funcționalități Cheie

- Reevaluare lunară a soldurilor în valută cu diferențe de curs pe 665 (pierdere) și 765 (câștig), definitive, FĂRĂ stornare automată (OMFP 1802/2014, nu IFRS).
- **Reevaluare pe fiecare partener:** soldurile se grupează pe cont + partener + valută, fără compensare între parteneri; nota contabilă poartă partenerul pe contul valutar și pe 665/765. Băncile și casa se reevaluează pe cont, fără partener.
- Model de audit trail `l10n.ro.currency.revaluation` cu state machine ciornă → postată → anulată, urmărit cu `mail.thread`/`mail.activity.mixin`. Liniile reevaluării nu mai pot fi adăugate, modificate sau șterse după postare, deci totalurile rămân egale cu nota contabilă.
- Calcul al soldurilor reziduale valutare la data reevaluării printr-o interogare SQL (CTE) care ține cont de reconcilierile parțiale.
- Calcul incremental: diferența se măsoară față de cursul ultimei reevaluări; liniile de ajustare sunt marcate `l10n_ro_is_fx_revaluation`, iar după decontarea unui element partea nerealizată rămasă se închide la reevaluarea următoare printr-o diferență de sens opus (net corect în P&L, dar rulaje 665/765 mai mari — limitare acceptată, explicată în fișă).
- **Tranziție automată de la versiunea fără partener:** ajustările lunilor anterioare, înregistrate fără partener, se stornează automat la prima reevaluare, iar fiecare partener primește diferența față de cursul istoric; totalul pe cont rămâne același. Liniile stornării au eticheta „Stornare reevaluare fără partener (tranziție)", ca rulajele mai mari din luna respectivă să fie explicabile. Nu e nevoie de migrare manuală.
- Raport de audit PDF per reevaluare (`action_print_audit_report`): perioadă, companie/CUI, jurnal, cursuri BNR (cu separatorii limbii), sold rezidual valutar/contabil, diferențe 665/765 cu totaluri, pe fiecare partener.
- Conturi incluse automat: 5124, 5314, 4111, 401, 451, 461, 462, 267, 508 și creditele/datoriile asimilate în valută (162, 167, 168, 519). Excluse: restul capitalurilor (clasa 1), stocurile (3xx), veniturile/cheltuielile, avansurile din 409/419 (pct. 316 alin. (2)) și combinațiile cont/valută excluse manual din raportul standard.
- Parametru de companie `l10n_ro_fx_revaluation_standard` (Contabilitate → Configurare → Setări → „Foreign Currency Revaluation"): OMFP 1802/2014 (implicit pe companiile RO) sau IFRS - IAS 21. Pe IFRS, meniul propriu refuză calculul și trimite spre wizard-ul standard. Tot acolo: conturile 665/765 și jurnalul de reevaluare (distincte de conturile diferențelor realizate).
- Wizard-ul Enterprise `account.multicurrency.revaluation.wizard` are opțiunea „Fără stornare automată (OMFP 1802)", activă implicit pe companiile RO; wizard-ul și meniul propriu rulează același motor de calcul.
- Buton „RO Currency Revaluation (OMFP 1802)" pe raportul Enterprise „Câștiguri/pierderi valutare nerealizate"; meniul propriu: Contabilitate → Contabilitate → Reevaluare valutară RO.
- Corecția se face doar prin Anulare (stornare în roșu a notei); o a doua reevaluare pentru aceeași dată și companie nu este permisă.
- Temei legal (corectat față de versiunile anterioare, care citau pct. 304 despre încasări/plăți): OMFP 1802/2014, pct. 322 alin. (2) și pct. 325 alin. (1)-(2) (evaluare la cursul BNR de la finele lunii), pct. 329 alin. (1) și pct. 56 (evidența pe fiecare partener), pct. 316 alin. (2) (avansuri).

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.currency.revaluation`: Sesiunea de reevaluare valutară (audit trail). Implementează state machine-ul (ciornă/postată/anulată) cu constrângere de unicitate `UNIQUE(date, company_id)` și metodele `action_compute` (calculează soldurile reziduale eligibile și populează liniile), `action_post` (generează nota contabilă fără stornare, cu partenerul pe liniile aferente, cu cerința prealabilă a conturilor 665/765 configurate pe companie), `action_cancel` (stornează nota contabilă în roșu prin `_reverse_moves`), `action_view_move` (deschide nota contabilă generată) și `action_print_audit_report` (deschide raportul PDF de audit). Moștenește `mail.thread` și `mail.activity.mixin` pentru istoric și activități.
- `l10n.ro.currency.revaluation.line`: Linie de reevaluare per cont/partener/valută (`partner_id`; fără partener pe bancă/casă), cu sold rezidual valutar (`balance_currency`), sold contabil (`balance_book`), cursul BNR nou (`rate_new`), soldul recalculat (`balance_new`), diferența (`adjustment`) și tipul diferenței (`diff_type` — pierdere 665/câștig 765).
- `account.move.line` (extindere): adaugă câmpul `l10n_ro_is_fx_revaluation`, care marchează liniile de ajustare generate de reevaluarea RO, pentru a reporta corect ajustările în soldul contabil al lunii următoare.
- `res.company` / `res.config.settings` (extindere): câmpul `l10n_ro_fx_revaluation_standard` (OMFP 1802 / IFRS), expus în Setări.
- `account.multicurrency.revaluation.report.handler` (extindere): adaugă butonul de deschidere a reevaluării RO pe raportul standard.
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
