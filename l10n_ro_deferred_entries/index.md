# Romania - Venituri și cheltuieli înregistrate în avans (471/472) (localizat la `l10n_ro_deferred_entries/index.md`)

- **Nume Tehnic:** `l10n_ro_deferred_entries`
- **Versiune:** `19.0.2.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_deferred_entries
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_deferred_entries`
- **Ultima Ingestie:** 2026-09-23
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul configurează automat mecanismul nativ Odoo Enterprise de recunoaștere a cheltuielilor și veniturilor înregistrate în avans, conform **OMFP 1802/2014 pct. 351 alin. (1)–(2)** și funcțiunii conturilor **471**/**472**, folosind conturile **4711** (Cheltuieli înregistrate în avans) și **4721** (Venituri înregistrate în avans) din planul de conturi românesc. Se bazează pe motorul nativ `account_accountant` (Enterprise) — coloana opțională „Dată amânată" de pe liniile de factură și rapoartele „Cheltuieli reportate" / „Venituri reportate" sunt disponibile fără cod custom adițional; modulul le livrează cu planul RO și traducerile care lipsesc din standard. Pe lângă cheltuielile/veniturile facturate, modulul acoperă și un caz major care nu are echivalent nativ: plăți în avans fără factură (asigurări RCA, CASCO), eșalonate direct dintr-un model de reconciliere aplicat pe extrasul bancar sau pe casă.

#### 2. Funcționalități Cheie

- Planul de conturi românesc (`account.chart.template`) livrează direct conturile `4711`/`4721` ca „Cheltuială amânată" / „Venit amânat" pe companie — corectează comportamentul standard al `account_accountant`, care altfel alege primul cont de activ/datorie curentă din plan (301/1614 pe planul RO) și amânările ar ajunge acolo tăcut.
- `post_init_hook` reconfirmă/corectează aceste conturi la instalare pe orice companie RO și setează jurnalul de Operațiuni diverse ca jurnal de amânare; păstrează neatins un cont ales manual de utilizator din grupa 471/472 (ex. 4712, termen lung).
- Corectează retroactiv și ciornele lunare de amânare deja generate pe contul greșit (301/1614), mutându-le pe 4711/4721 — notele deja postate nu se modifică, reclasificarea lor rămâne manuală (fișă §9).
- Metoda de calcul implicită: **Luni** (recunoaștere liniară pe luni calendaristice); poate fi schimbată în setări pe „Zile" sau „Luni complete".
- Pe linia de factură (cont 6xx sau 7xx) se completează coloana opțională „Dată amânată" (început → sfârșit); la postare Odoo generează automat nota de transfer și planifică notele lunare de recunoaștere, fără cod custom.
- **Amânare configurabilă pe modelul de reconciliere bancară/casă**, pentru plăți fără obligație de facturare (asigurări): pe linia modelului se setează **Amânare (luni)** și **Amânarea începe** (`Luna plății` / `Luna următoare`), doar pe conturi de cheltuieli (6xx) — o încasare în avans pentru o operațiune taxabilă ar cere factură de avans și TVA la încasare, deci veniturile nu se pot eșalona din extras.
- Modelul aplicat din reconcilierea bancară pune perioada pe contrapartidă și generează imediat notele de amânare (transfer + note lunare), fără să aștepte postarea unei facturi.
- Ștergerea contrapartidei, anularea reconcilierii, ștergerea sau resetarea la ciornă a tranzacției anulează automat amânarea: ciornele se șterg, notele deja postate se stornează la data lor (sau la prima zi deschisă, dacă luna e blocată) — nu se șterg niciodată note postate.
- Livrează traducerile RO lipsă din `account_accountant`: „Înregistrări de amânare" (buton pe factură) și „Amânare diversă" (tip de intrare amânată), netraduse în Odoo 19.0 standard.

#### 3. Dependențe

- `account_accountant`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extindere, `@template("ro", "res.company")`): livrează `deferred_expense_account_id` = `4711` și `deferred_revenue_account_id` = `4721` odată cu încărcarea planului de conturi românesc, ca `account_accountant` să nu mai completeze singur 301/1614.
- `account.reconcile.model.line` (extindere): adaugă `l10n_ro_deferred_months` (Integer) și `l10n_ro_deferred_start` (Selecție: `payment_month` / `next_month`) pe linia unui model de reconciliere; validează prin `_check_l10n_ro_deferred` că amânarea se poate seta doar pe conturi de cheltuieli (`internal_group = expense`); la aplicarea modelului în widget-ul bancar (`_apply_in_bank_widget`) calculează `deferred_start_date`/`deferred_end_date` pe baza datei tranzacției.
- `account.reconcile.model` (extindere): după `_trigger_reconciliation_model` (buton din ecranul de reconciliere sau reconciliere automată), sincronizează notele de amânare ale liniei de extras, după ce taxele sunt deja recalculate.
- `account.bank.statement.line` (extindere): nucleul funcționalității noi — `_l10n_ro_sync_deferred_entries` (compară o „amprentă" a liniilor amânate curente cu cea reținută pe notă și regenerează amânarea la orice schimbare), `_l10n_ro_cancel_deferred_entries` (șterge ciornele, stornează notele postate la data lor sau la prima zi deschisă dacă luna e blocată), plus supraveghere pe `unlink`, `delete_reconciled_line`, `edit_reconcile_line` și `action_undo_reconciliation`, ca orice modificare din ecranul de reconciliere să regenereze sau să anuleze corect amânarea.
- `account.move` (extindere): câmpul `l10n_ro_deferred_signature` reține amprenta liniilor amânate pentru care s-au generat deja note, ca sincronizarea să nu le storneze/regenereze inutil; suprascrie `button_draft` (stornează manual amânarea unei note de tranzacție bancară înainte ca ștergerea nativă `_unlink_or_reverse` să atingă și stornările proprii) și `_post` (reține amprenta după (re)postarea unei note de tranzacție).

**Vizualizări**

- `view_account_reconcile_model_form`: adaugă coloanele „Amânare (luni)" și „Amânarea începe" pe lista liniilor unui model de reconciliere (`account.view_account_reconcile_model_form`).

Pentru fluxul standard pe factură (fără reconciliere bancară), modulul nu adaugă vizualizări proprii — folosește coloana „Dată amânată" și rapoartele native Enterprise (Contabilitate → Raportare → **Cheltuieli reportate** / **Venituri reportate**).

**Traduceri**

- `i18n/ro.po`: completează traducerile RO lipsă din `account_accountant` pentru termeni de model (rezolvați prin xmlid): `Deferral Entries` → „Înregistrări de amânare" și `Deferred Miscellaneous` → „Amânare diversă". Mesajele de eroare din codul Python al `account_accountant` nu pot fi acoperite astfel — traducerile de cod se caută doar în .po-ul modulului care le definește.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare, corectează pe fiecare companie RO conturile de amânare (înlocuiește orice cont din afara grupei 471/472, nu doar câmpurile goale) și jurnalul de amânare, apoi mută ciornele lunare deja generate pe contul greșit.
- Migrări `19.0.2.0.1` și `19.0.2.0.2` (post-migrate): rulează din nou `_set_ro_deferred_accounts` pe instalările existente — prima corectează conturile pe companie (până atunci hook-ul scria doar în câmpuri goale, dar planul le umpluse deja cu 301/1614), a doua adaugă și mutarea ciornelor lunare rămase pe contul greșit. Notele deja postate nu se modifică în niciun caz — reclasificarea lor rămâne manuală (fișă §9).
- Recunoașterea lunară pe fluxul de factură este realizată de mecanismul standard de amânare din `account_accountant`, care generează și postează notele la scadență.

#### 5. Conexiuni

- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): mecanism nativ Enterprise similar (amortizare mijloace fixe) configurat pentru planul de conturi RO.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele explicative la situațiile financiare, unde se reflectă soldurile de venituri și cheltuieli în avans.
