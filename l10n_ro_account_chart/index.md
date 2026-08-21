# Romania - Plan de Conturi Extins (FR-01) (localizat la `l10n_ro_account_chart/index.md`)

- **Nume Tehnic:** `l10n_ro_account_chart`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_chart
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_chart`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul completează planul de conturi românesc (OMFP 1802/2014) cu trei funcționalități esențiale: blocarea postărilor directe pe conturile sintetice, impunerea analiticului obligatoriu per cont și blocarea inactivării conturilor cu rulaj. Toate cele trei mecanisme sunt opt-in per companie din **Setări → Contabilitate**.

#### 2. Funcționalități Cheie

- **Blocare postare pe conturi sintetice:** conturile marcate ca sintetice nu permit postare directă; excepție fac conturile de tip `asset_receivable` / `liability_payable` (401, 411, 421 etc.).
- **Analitic obligatoriu per cont:** conturile marcate cu „Analitic obligatoriu" impun completarea `analytic_distribution` la postare.
- **Blocaj inactivare cont cu rulaj:** un cont cu înregistrări contabile nu poate fi marcat `deprecated` sau dezactivat.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.account`: adaugă câmpurile `l10n_ro_is_synthetic` (cont sintetic, blochează postarea directă) și `l10n_ro_analytic_required` (impune distribuție analitică la postare); suprascrie `write()` pentru a bloca dezactivarea conturilor RO cu rulaj (`account.move.line` existente).
- `account.move`: adaugă constrângerile `_check_no_post_on_synthetic` (blochează postarea pe conturi sintetice, cu excepția `asset_receivable`/`liability_payable`) și `_check_analytic_required` (impune analitic pe liniile cu `l10n_ro_analytic_required`), ambele active doar dacă setarea companiei e activată și compania e fiscal RO.
- `res.company`: câmpurile de configurare `l10n_ro_block_synthetic_posting` și `l10n_ro_require_analytic` (opt-in per companie).
- `res.config.settings`: expune cele două setări de companie în ecranul de configurare Contabilitate.

**Vizualizări**

- `view_account_form_l10n_ro_chart`: adaugă câmpurile `l10n_ro_is_synthetic` și `l10n_ro_analytic_required` pe formularul contului contabil.
- `res_config_settings_view_form_l10n_ro_chart`: adaugă cele două comutatoare de configurare în Setări → Contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (hooks.py): la instalare, marchează automat ca sintetice conturile companiilor fiscal RO care au cel puțin un cont-copil cu cod mai lung și același prefix (ex: 401 devine sintetic dacă există 401.01).

#### 5. Conexiuni

- `l10n_ro_account_fisa_cont`: modulul „Fișă de Cont” din localizarea românească, care poate beneficia de conturile marcate sintetic/analitic obligatoriu introduse de acest modul.
