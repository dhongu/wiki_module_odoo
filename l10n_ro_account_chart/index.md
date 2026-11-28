# Romania - Plan de conturi extins (localizat la `l10n_ro_account_chart/index.md`)

- **Nume Tehnic:** `l10n_ro_account_chart`
- **Versiune:** `20.0.1.1.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_account_chart
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_chart`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul completează planul de conturi românesc (OMFP 1802/2014) cu conturile lipsă din nomenclatorul SAF-T și cu trei mecanisme de control: blocarea postărilor directe pe conturile sintetice, impunerea analiticului obligatoriu per cont și blocarea inactivării conturilor cu rulaj. Primele două sunt opt-in per companie, din **Setări → Contabilitate**, secțiunea „Plan de conturi România".

#### 2. Funcționalități Cheie

- **Blocare postare pe conturi sintetice:** conturile marcate ca sintetice nu permit postare directă; excepție fac conturile de tip `asset_receivable` / `liability_payable` (401, 411, 421 etc.). Marcajul se poate schimba manual pe formularul contului.
- **Analitic obligatoriu per cont:** conturile marcate cu „Analitic obligatoriu" impun completarea `analytic_distribution` la postare (de regulă conturile din clasele 6 și 7).
- **Blocaj inactivare cont cu rulaj:** un cont cu înregistrări contabile nu poate fi marcat `deprecated` sau dezactivat; este activ automat, fără comutator, pentru companiile fiscal RO.
- **Conturi lipsă din nomenclatorul SAF-T:** adaugă conturile din nomenclatorul ANAF (PlanConturiBalSocCom) pe care planul `l10n_ro` nu le are (6051–6058, 6121–6123, 616, 617, 618, 6461, 6462, 4901–4904 și altele), inclusiv pe companiile existente, la instalare sau actualizare.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.account`: adaugă câmpurile `l10n_ro_is_synthetic` (cont sintetic, blochează postarea directă) și `l10n_ro_analytic_required` (impune distribuție analitică la postare); suprascrie `write()` pentru a bloca dezactivarea conturilor RO cu rulaj.
- `account.move`: constrângerile `_check_no_post_on_synthetic` și `_check_analytic_required`, active doar dacă setarea companiei e activată și compania e fiscal RO.
- `account.chart.template`: extins pentru adăugarea conturilor SAF-T lipsă în șablonul planului de conturi.
- `res.company`: câmpurile de configurare `l10n_ro_block_synthetic_posting` și `l10n_ro_require_analytic` (opt-in per companie).
- `res.config.settings`: expune cele două setări de companie în ecranul de configurare Contabilitate.

**Vizualizări**

- `view_account_form_l10n_ro_chart`: adaugă câmpurile `l10n_ro_is_synthetic` și `l10n_ro_analytic_required` pe formularul contului contabil.
- `res_config_settings_view_form_l10n_ro_chart`: adaugă comutatoarele de configurare în Setări → Contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (hooks.py): la instalare, marchează automat ca sintetice conturile companiilor fiscal RO al căror cod este prefix al altui cont (ex: 401 devine sintetic dacă există 401.01) și adaugă conturile SAF-T lipsă pe companiile existente.

#### 5. Conexiuni

- [l10n_ro_account_fisa_cont](../l10n_ro_account_fisa_cont/index.md): raportul „Fișă de Cont", care folosește planul de conturi românesc.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): închiderea conturilor 6xx/7xx în 121, bazată pe structura planului de conturi.
