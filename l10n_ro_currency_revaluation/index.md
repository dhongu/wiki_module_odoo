# Romania - Reevaluare Valutară (OMFP 1802) (localizat la `l10n_ro_currency_revaluation/index.md`)

- **Nume Tehnic:** `l10n_ro_currency_revaluation`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_currency_revaluation`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_currency_revaluation`
- **Ultima Ingestie:** `2026-06-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul automatizează reevaluarea lunară a soldurilor monetare exprimate în valută (creanțe, datorii, disponibilități, avansuri etc.), conform cerințelor contabile românești din OMFP 1802/2014, pct. 340–345. La sfârșitul fiecărei luni, modulul calculează soldurile reziduale în valută la cursul de închidere și generează automat o notă contabilă cu diferențele de curs înregistrate definitiv pe conturile de venituri (765) și cheltuieli (665) din diferențe de curs valutar. Spre deosebire de abordarea IFRS folosită implicit în Odoo Enterprise, aceste diferențe sunt considerate definitive și NU sunt stornate automat în luna următoare — comportament corect din punct de vedere fiscal pentru companiile din România. Întregul proces este urmărit printr-un model de tip audit trail, cu stări clare (ciornă → postată → anulată), oferind contabilului trasabilitate completă și control asupra închiderii lunare.

#### 2. Funcționalități Cheie

- Reevaluare lunară a soldurilor în valută cu generarea automată a diferențelor de curs valutar pe conturile 665 (cheltuieli) și 765 (venituri).
- Diferențe de curs înregistrate definitiv, FĂRĂ stornare automată în luna următoare — corect conform OMFP 1802/2014 (vs. comportamentul IFRS din Enterprise).
- Model de audit trail `l10n.ro.currency.revaluation` cu state machine: ciornă → postată → anulată.
- Calcul automat al soldurilor reziduale valutare la data balanței, prin interogare SQL care ține cont de reconcilierile parțiale.
- Excluderea automată a conturilor nemonetare (clase 1xx/3xx, venituri și cheltuieli) — se reevaluează doar conturile monetare relevante (ex.: 5124, 5314, 4111, 401, 451, 461, 462, 267, 508).
- Override al wizard-ului Enterprise `account.multicurrency.revaluation.wizard`, cu opțiunea „Fără stornare automată" activă pentru companiile din România.
- Temei legal: OMFP 1802/2014, pct. 340–345.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.currency.revaluation`: Sesiunea de reevaluare valutară (audit trail). Implementează state machine-ul (ciornă/postată/anulată) și metodele `action_compute` (calculează soldurile reziduale și liniile), `action_post` (generează nota contabilă fără stornare), `action_cancel` (anulează sesiunea) și `action_view_move` (deschide nota contabilă generată). Moștenește `mail.thread` și `mail.activity.mixin` pentru istoric și activități.
- `l10n.ro.currency.revaluation.line`: Linie de reevaluare per cont/valută, cu sold rezidual valutar (`balance_currency`), sold contabil (`balance_book`), cursul nou (`rate_new`), soldul recalculat (`balance_new`), diferența (`adjustment`) și tipul diferenței (`diff_type` — pierdere/câștig).
- `account.multicurrency.revaluation.wizard` (extindere): Adaugă câmpul `l10n_ro_no_reversal` și suprascrie `create_entries` pentru a genera înregistrări fără stornare automată (`_l10n_ro_create_entries_no_reversal`) când compania este din România.

**Vizualizări**

- `view_l10n_ro_currency_revaluation_tree`: Lista sesiunilor de reevaluare valutară.
- `view_l10n_ro_currency_revaluation_form`: Formularul sesiunii, cu butoanele de calcul/postare/anulare și liniile de reevaluare.
- `view_l10n_ro_currency_revaluation_search`: Filtre și grupări pentru sesiuni.
- `action_l10n_ro_currency_revaluation`: Acțiunea de fereastră care deschide sesiunile, accesibilă din meniul „Reevaluare valutară RO".

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Procesul de reevaluare este declanșat manual de contabil (nu există cron-uri definite).

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): diferențele de curs aferente soldurilor de furnizori (ex. contul 408 din recepția fără factură) intră în perimetrul reevaluat de acest modul.
- [l10n_ro_expense_currency](../l10n_ro_expense_currency/index.md): avansurile în valută (cont 542) sunt tratate separat, dar se corelează cu reevaluarea soldurilor monetare în valută.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): reevaluarea valutară este un pas din checklist-ul de închidere lunară.
