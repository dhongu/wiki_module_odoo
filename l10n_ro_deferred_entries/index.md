# Romania - Venituri și cheltuieli înregistrate în avans (471/472) (localizat la `l10n_ro_deferred_entries/index.md`)

- **Nume Tehnic:** `l10n_ro_deferred_entries`
- **Versiune:** `20.0.2.2.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_deferred_entries
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_deferred_entries`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Configurează automat mecanismul nativ Odoo Enterprise de recunoaștere a cheltuielilor și veniturilor înregistrate în avans, conform OMFP 1802/2014 pct. 351 și funcțiunii conturilor 471/472, cu conturile 4711 (cheltuieli în avans) și 4721 (venituri în avans) din planul de conturi românesc. Se bazează pe motorul `account_accountant`: coloana opțională „Dată amânată” de pe liniile de factură și rapoartele „Cheltuieli reportate” / „Venituri reportate” funcționează fără cod custom. Modulul acoperă și plățile în avans fără factură (asigurări RCA, CASCO), eșalonate dintr-un model de reconciliere aplicat pe extras sau casă.

#### 2. Funcționalități Cheie

- **Configurare la instalare:** planul de conturi RO livrează conturile de amânare (`471100` Cheltuială amânată, `472100` Venit amânat), iar `post_init_hook` le corectează pe companiile RO existente, setează jurnalul de operațiuni diverse ca jurnal de amânare și păstrează un cont ales manual din grupa 471/472 (ex. 4712). Fără aceasta, Enterprise ar alege 301/1614 și amânările ar ajunge acolo tăcut; ciornele lunare deja generate pe contul greșit se mută, notele postate rămân neatinse.
- **Metoda de calcul:** implicit „Luni” (cotă egală pe lună calendaristică); în setări (Contabilitate → Configurare → Setări) se poate alege „Zile” sau „Luni complete”, iar generarea poate fi „La validarea facturii” sau „Manual și grupat” (butonul „Generează înregistrare” apare în rapoartele de amânări).
- **Flux pe factură:** pe linia cu cont real de cheltuieli/venituri (612, 613, 704) se bifează coloana opțională „Dată amânată” și se completează intervalul; la confirmare Odoo generează nota de transfer (`Dr 4711 = Cr 6xx`) și notele lunare de recunoaștere. Data facturii stabilește luna transferului.
- **Plăți fără factură din extras/casă:** pe linia unui model de reconciliere se setează **Amânare (luni)** și **Amânarea începe** (`Luna plății` / `Luna următoare`), doar pe conturi 6xx; modelul aplicat generează imediat notele de amânare. Veniturile nu se pot eșalona din extras (o încasare în avans cere factură de avans și TVA la încasare).
- Ștergerea contrapartidei, anularea reconcilierii, ștergerea sau resetarea tranzacției anulează amânarea: ciornele se șterg, notele postate se stornează la data lor (sau la prima zi deschisă, dacă luna e blocată), niciodată nu se șterg.
- **Perioade începute în trecut** (regularizări de energie, servicii facturate pentru luni anterioare, perioadă din e-Factura): lunile trecute din exercițiul curent rămân pe 6xx/7xx în luna facturii, iar prin 471/472 trec doar lunile următoare; la cheltuieli, lunile exercițiului anterior (dacă nu e blocat) se înregistrează pe 31.12 prin 4081 Furnizori - facturi nesosite (OMFP 1802/2014 pct. 65, 67, 70, 72–73). Factura în ciornă afișează o alertă, iar chatterul arată sumele după postare; setarea se poate opri pe companie.
- Traduceri RO care lipsesc din standard: butonul „Înregistrări de amânare” de pe factură și tipul „Amânare diversă”.

#### 3. Dependențe

- `account_accountant`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extindere, `@template("ro", "res.company")`): livrează conturile de amânare odată cu planul de conturi românesc.
- `account.reconcile.model.line` (extindere): `l10n_ro_deferred_months` și `l10n_ro_deferred_start` (`payment_month` / `next_month`), validate pe conturi de cheltuieli; la aplicarea în widget-ul bancar calculează datele de început/sfârșit ale amânării.
- `account.reconcile.model` (extindere): sincronizează notele de amânare ale liniei de extras după `_trigger_reconciliation_model`.
- `account.bank.statement.line` (extindere): `_l10n_ro_sync_deferred_entries` (regenerează amânarea la orice schimbare, pe baza unei amprente) și `_l10n_ro_cancel_deferred_entries`, plus supravegherea ștergerii și anulării reconcilierii.
- `account.move` (extindere): `l10n_ro_deferred_signature` (amprenta liniilor amânate), `button_draft` și `_post` adaptate pentru tranzacții bancare.
- `account.move.line` (extindere): `_get_deferred_periods`, pentru tratarea lunilor trecute în luna facturii.
- `res.company` / `res.config.settings` (extindere): `l10n_ro_deferred_past_in_current` și `l10n_ro_deferred_accrual_account_id` (cont facturi nesosite 4081).

**Vizualizări**

- `view_account_reconcile_model_form`: coloanele „Amânare (luni)” și „Amânarea începe” pe liniile modelului de reconciliere.
- `res_config_settings_view_form`: setările lunilor trecute și contul de facturi nesosite.
- Fluxul pe factură folosește coloana „Dată amânată” și rapoartele native Enterprise (Contabilitate → Raportare → Cheltuieli reportate / Venituri reportate).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): corectează conturile și jurnalul de amânare pe fiecare companie RO și mută ciornele lunare rămase pe contul greșit.
- Directorul `migrations/`: scripturi de migrare care reaplică conturile de amânare pe instalările existente.
- Recunoașterea lunară pe flux de factură este realizată de mecanismul standard din `account_accountant`.

#### 5. Conexiuni

- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): mecanism nativ Enterprise similar (amortizare mijloace fixe) configurat pentru planul RO.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele explicative la situațiile financiare, unde se reflectă soldurile în avans.
