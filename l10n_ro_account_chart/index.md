# Romania - Plan de conturi extins (localizat la `l10n_ro_account_chart/index.md`)

- **Nume Tehnic:** `l10n_ro_account_chart`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_chart
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_chart`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul completează planul de conturi românesc (OMFP 1802/2014) cu conturile din nomenclatorul ANAF SAF-T care lipsesc din `l10n_ro` și adaugă trei mecanisme de control contabil: blocarea postărilor directe pe conturile sintetice, impunerea analiticului obligatoriu per cont și blocarea inactivării conturilor cu rulaj. Cele trei mecanisme de control sunt opt-in per companie din **Setări → Contabilitate** (blocajul la inactivare este activ automat pe companiile fiscal RO).

#### 2. Funcționalități Cheie

- **Blocare postare pe conturi sintetice:** conturile marcate ca sintetice nu permit postare directă; excepție fac conturile de tip `asset_receivable` / `liability_payable` (401, 411, 421 etc.). Activare prin setarea „Blochează postare pe conturi sintetice".
- **Analitic obligatoriu per cont:** conturile marcate cu „Analitic obligatoriu" impun completarea `analytic_distribution` la postare. Activare prin setarea „Analitic obligatoriu pe conturi marcate".
- **Blocaj inactivare cont cu rulaj:** un cont cu înregistrări contabile nu poate fi marcat `deprecated` sau dezactivat; este activ automat (fără comutator) pe companiile cu țara fiscală România.
- **Conturi lipsă din nomenclatorul SAF-T:** adaugă conturile din PlanConturiBalSocCom absente din `l10n_ro` (ex: 1496, 4417, 467, 4901–4904, 6051–6058, 6121–6123, 616, 617, 618, 6461, 6462, 6818, 697, 7818); contul 605 este redenumit conform OMFP 4291/2022 doar dacă păstrează denumirea veche. Conturile se adaugă și pe companiile existente, la instalare sau actualizare; un cont creat manual cu același cod primește doar identificatorul, fără duplicat.
- **Marcare sintetic / analitic obligatoriu:** la instalare, conturile cu sub-conturi sunt marcate automat sintetice; marcajul și bifa „Analitic obligatoriu" se pot modifica manual din **Contabilitate → Configurare → Planul de conturi** (analiticul obligatoriu se folosește de regulă pe clasele 6 și 7).

Pașii detaliați și capturile de ecran sunt în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.account`: adaugă câmpurile `l10n_ro_is_synthetic` (cont sintetic, blochează postarea directă) și `l10n_ro_analytic_required` (impune distribuție analitică la postare); suprascrie `write()` pentru a bloca dezactivarea conturilor RO cu rulaj (`account.move.line` existente).
- `account.move`: adaugă constrângerile `_check_no_post_on_synthetic` (blochează postarea pe conturi sintetice, cu excepția `asset_receivable`/`liability_payable`) și `_check_analytic_required` (impune analitic pe liniile cu `l10n_ro_analytic_required`), ambele active doar dacă setarea companiei e activată și compania e fiscal RO.
- `account.chart.template`: metoda `_get_ro_account_chart_account_account` (`@template("ro", "account.account")`) încarcă conturile suplimentare din `data/template/account.account-ro.csv` (26 de linii) când planul RO se încarcă după instalarea modulului.
- `res.company`: câmpurile de configurare `l10n_ro_block_synthetic_posting` și `l10n_ro_require_analytic` (opt-in per companie).
- `res.config.settings`: expune cele două setări de companie în ecranul de configurare Contabilitate.

**Vizualizări**

- `view_account_form_l10n_ro_chart`: adaugă câmpurile `l10n_ro_is_synthetic` și `l10n_ro_analytic_required` pe formularul contului contabil.
- `res_config_settings_view_form_l10n_ro_chart`: adaugă cele două comutatoare de configurare în Setări → Contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (hooks.py): la instalare adaugă conturile lipsă (`add_missing_accounts`) pe companiile cu planul RO încărcat, apoi marchează ca sintetice conturile companiilor fiscal RO care au cel puțin un cont-copil cu cod mai lung și același prefix (ex: 401 devine sintetic dacă există 401.01).
- Migrare `19.0.1.1.0` (post-migrate): rulează `add_missing_accounts` pe bazele unde modulul era deja instalat, deoarece `post_init_hook` nu rulează la actualizare.

#### 5. Conexiuni

- [l10n_ro_account_fisa_cont](../l10n_ro_account_fisa_cont/index.md): modulul „Fișă de Cont" din localizarea românească, care poate beneficia de conturile marcate sintetic/analitic obligatoriu introduse de acest modul.
