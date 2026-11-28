# Romania - Reevaluare valutară (OMFP 1802) (localizat la `l10n_ro_currency_revaluation/index.md`)

- **Nume Tehnic:** `l10n_ro_currency_revaluation`
- **Versiune:** `20.0.1.3.3`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_currency_revaluation`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_currency_revaluation`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru reevaluarea lunară obligatorie a soldurilor în valută conform OMFP 1802/2014 (pct. 325 alin. (1)–(2) pentru creanțe, datorii și disponibilități, pct. 322 alin. (2) pentru diferența lunară), cu generarea diferențelor de curs pe conturile 665 (pierdere) și 765 (câștig), fără stornare automată. Este adresat companiilor românești cu tranzacții în valută (exportatori, importatori, conturi bancare sau împrumuturi în EUR/USD), care trebuie să ajusteze lunar valoarea în lei a soldurilor la cursul BNR din ultima zi a lunii. Spre deosebire de comportamentul implicit al modulului Enterprise `account_reports` (model IFRS cu provizion stornat a doua zi), diferențele sunt înregistrate definitiv, iar fiecare reevaluare este urmărită printr-un model de audit cu stări clare (ciornă → postată → anulată).

#### 2. Funcționalități Cheie

- Model de audit dedicat (`l10n.ro.currency.revaluation`) cu mașină de stări ciornă → postată → anulată și jurnal de activitate în chatter; liniile unei reevaluări postate nu se mai pot modifica.
- Calcul SQL al soldurilor reziduale în valută la data reevaluării, ținând cont de reconcilierile parțiale (nu soldul brut).
- Reevaluare pe fiecare partener: creanțele și datoriile se reevaluează separat pe client/furnizor, fără compensare între parteneri; nota contabilă poartă partenerul pe contul valutar și pe 665/765, iar băncile și casa se reevaluează pe cont.
- Notă contabilă fără stornare automată, comportament corect pentru OMFP 1802 (diferențele sunt definitive, nu provizioane IFRS).
- Calcul incremental: diferența se măsoară față de cursul ultimei reevaluări, nu față de cel al documentului; liniile notei sunt marcate `l10n_ro_is_fx_revaluation`, iar la decontarea unui element partea nerealizată rămasă se închide prin diferență de sens opus la reevaluarea următoare.
- Raport de audit PDF per reevaluare: perioadă, companie/CUI, jurnal, partener, cursuri BNR, sold rezidual și contabil, diferențe 665/765 cu totaluri.
- Parametru de companie OMFP 1802 / IFRS (`l10n_ro_fx_revaluation_standard`, în Contabilitate → Configurare → Setări, secțiunea reevaluare valutară): wizard-ul Enterprise „Unrealized Currency Gains/Losses” și meniul propriu rulează același motor pentru compania configurată pe OMFP 1802; pe IFRS meniul propriu refuză calculul și trimite spre wizard-ul standard.
- Buton **RO Currency Revaluation (OMFP 1802)** pe raportul standard Enterprise, care deschide reevaluarea RO a lunii afișate.
- Conturi incluse automat: 5124, 5314, 4111, 401, 451, 461, 462, 267, 508, plus 162, 167, 168, 519 și 4118; excluse capitalurile proprii, stocurile (3xx), veniturile/cheltuielile, avansurile 409/419 (pct. 316 alin. (2)) și excluderile manuale cont/valută partajate cu raportul standard.
- Configurare necesară: conturile de reevaluare 665/765 și jurnalul de operațiuni diverse pe companie; cursurile BNR trebuie importate (în Odoo 20 un curs se aplică din ziua următoare datei lui, iar modulul folosește cursul BNR cu data reevaluării).
- Anulare prin stornare în roșu a notei contabile; o singură reevaluare pe dată și companie.
- Temei legal: OMFP 1802/2014, pct. 315, 322 alin. (2), 325 alin. (1)–(2) și 329 alin. (1) (evidența pe fiecare partener).

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.currency.revaluation`: sesiunea de reevaluare (audit trail), cu `UNIQUE(date, company_id)` și metodele `action_compute`, `action_post`, `action_cancel`, `action_view_move` și `action_print_audit_report`. Moștenește `mail.thread` și `mail.activity.mixin`.
- `l10n.ro.currency.revaluation.line`: linie per cont/partener/valută, cu sold rezidual în valută, sold contabil, curs BNR, sold recalculat, diferență și tip (665/765).
- `account.move.line` (extindere): câmpul `l10n_ro_is_fx_revaluation` marchează liniile de ajustare, pentru reportarea corectă în luna următoare.
- `res.company` / `res.config.settings` (extindere): standardul de reevaluare (`l10n_ro_fx_revaluation_standard`) și conturile/jurnalul de reevaluare.
- `account.multicurrency.revaluation.report.handler` (extindere): adaugă butonul de deschidere a reevaluării RO pe raportul standard (`action_open_l10n_ro_currency_revaluation`).

**Vizualizări**

- `view_l10n_ro_currency_revaluation_tree` / `_form` / `_search`: lista, formularul (butoane Calculează, Postează nota, Anulează, notă contabilă, raport audit) și filtrele sesiunilor.
- `action_l10n_ro_currency_revaluation`: acțiunea meniului „Reevaluare valutară RO” (Contabilitate → Contabilitate).
- `res_config_settings_view_form_fx_revaluation`: secțiunea de setări a standardului și conturilor de reevaluare.
- `view_account_multicurrency_revaluation_wizard_ro`: adaptarea wizard-ului Enterprise.
- `action_report_currency_revaluation` / `report_currency_revaluation`: raportul PDF de audit.

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Reevaluarea este declanșată manual de contabil; `post_init_hook` doar inițializează setările la instalare.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): diferențele de curs aferente soldurilor de furnizori (ex. 408) intră în perimetrul reevaluat.
- [l10n_ro_expense_currency](../l10n_ro_expense_currency/index.md): avansurile în valută (cont 542) se corelează cu reevaluarea soldurilor monetare.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): reevaluarea este un pas din checklist-ul de închidere lunară.
- `account_reports`: modulul extinde wizard-ul Enterprise de reevaluare multi-valută, dezactivând stornarea automată pentru companiile din România.
