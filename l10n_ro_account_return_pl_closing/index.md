# România - Închidere P&L Cont Return (121) (localizat la `l10n_ro_account_return_pl_closing/index.md`)

- **Nume Tehnic:** `l10n_ro_account_return_pl_closing`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_return_pl_closing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_return_pl_closing`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru închiderea lunară a conturilor de venituri (clasa 7) și cheltuieli (clasa 6) prin transferul soldului în contul 121 – Profit și pierdere, conform OMFP 1802/2014. Folosește framework-ul standard Enterprise `account.return` din `account_reports` (Odoo 19), oferind un flux structurat cu audit trail, similar cu cel de închidere TVA.

#### 2. Funcționalități Cheie

- Generare automată a notei contabile de închidere 6xx/7xx → 121 la apăsarea butonului Review.
- Flux cu stări Review → Submit, cu audit trail complet prin chatter.
- Suport pentru conturi cu sold pe ambele părți: 609, 709, 711 etc. (`pl_bypass_account_ids`).
- Calcul profit/pierdere estimat înainte de generarea notei (fără a crea înregistrări).
- Badge profit/pierdere vizibil direct în vizualizarea Kanban pe fiecare return lunar.
- Buton „View Entry” pentru deschiderea directă a notei generate.
- Reset automat al notei la reluarea fluxului (nota veche este ștearsă și se regenerează).
- Fallback multi-companie: dacă jurnalul sau contul 121 aparțin altei companii, echivalentele sunt găsite automat.
- Include tipurile `income_other` (ex. 758) alături de `income` și `expense`.
- Periodicitate lunară cu termen de 25 de zile, configurabilă pe tipul de return.

#### 3. Dependențe

- `account_reports`
- `account`
- `l10n_ro`
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `account.return.type` (extins): adaugă configurația implicită pentru închiderea P&L pe tipul de return — `pl_journal_id` (jurnalul de închidere), `pl_account_id` (contul 121), `pl_bypass_account_ids` (conturi închise pe sold net, indiferent de parte) și câmpul calculat `is_pl_closing_return_type` (identifică dacă tipul de return se bazează pe un raport P&L românesc). Include și `_demo_setup()` pentru configurarea datelor demo.
- `account.return` (extins): adaugă `pl_profit_amount`/`pl_profit_currency_id`/`pl_show_profit` (rezultatul calculat din nota de închidere postată) și `is_pl_closing_return` (related pe tipul de return). Suprascrie `_run_checks()` pentru a injecta verificarea „Estimated Profit/Loss”, `action_validate()` și `_proceed_with_locking()` pentru a genera nota de închidere la validare, și `_on_post_submission_event()` pentru a afișa rezultatul (profit/pierdere) și nota generată după Submit. Metoda centrală `_generate_pl_closing_entries()` calculează soldurile conturilor 6xx/7xx/7581 pe perioada return-ului și creează + postează nota contabilă de închidere, legată de return prin `closing_return_id`.
- `account.move` (extins prin câmpul standard `closing_return_id` din `account_reports`): leagă nota contabilă generată de instanța de return.

**Vizualizări**

- `data/account_return_pl_closing.xml`: definește tipul de return „RO – Închidere venituri/cheltuieli (P&L)” și verificările (checks) asociate.
- `views/account_return_type_views.xml`: extinde vizualizarea formularului tipului de return pentru a expune câmpurile `pl_journal_id`, `pl_account_id`, `pl_bypass_account_ids`.
- `data/menu.xml`: adaugă opțiunea de meniu pentru rularea/accesul la închiderea P&L.

**Acțiuni Automate / Acțiuni Server**

- Verificare „Estimated Profit / Loss” (`_check_template_pl_estimated_profit`): injectată în `_run_checks()`, calculează și afișează ca notificare profitul/pierderea estimat(ă) înainte de generarea notei finale, prin `action_compute_estimated_profit()`.

#### 5. Conexiuni

- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md): modulul de plan de conturi românesc extins, fundamental pentru structura contabilă (contul 121 și conturile de clasă 6/7).
- [l10n_ro_account_fisa_cont](../l10n_ro_account_fisa_cont/index.md): raportul „Fișă de Cont”, complementar pentru verificarea soldurilor conturilor 6xx/7xx/121 înainte și după închidere.
- `account_reports`: framework-ul standard Odoo Enterprise pentru rapoarte financiare și return-uri (`account.return`), pe care se bazează întregul flux al modulului.
- `l10n_ro_reports`: furnizează rapoartele financiare P&L românești (micro/SMLE/internațional) folosite pentru a identifica tipurile de return relevante prin `is_pl_closing_return_type`.
- `l10n_ro_account_period_close` (OCA): modul alternativ cu funcționalitate similară de închidere a exercițiului/perioadei, dar cu arhitectură diferită (fără framework-ul `account.return`); menționat în documentație ca punct de comparație.
