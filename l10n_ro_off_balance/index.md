# Romania - Evidență extrabilanțieră (clasa 8)

- **Nume Tehnic:** `l10n_ro_off_balance`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_off_balance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_off_balance`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conturile din grupa 80 (în afara bilanțului) se țin în partidă simplă (OMFP 1802/2014, clasa 8), dar Odoo cere ca orice notă contabilă să fie echilibrată. Modulul stabilește o convenție unică pentru toate modulele Terrabit care scriu note extrabilanțiere: un cont tehnic de contrapartidă și un jurnal comun.

#### 2. Funcționalități Cheie

- **Cont tehnic 803999** (Contrapartidă tehnică evidență extrabilanțieră), analitic al contului 8039: echilibrează nota (ex. Dr 8033 = Cr 803999), iar conturile de evidență (8031, 8033, 8035) își păstrează soldul real. Se încadrează în nomenclatorul SAF-T (D406).
- **Jurnal EXTR** (Evidență extrabilanțieră), comun tuturor notelor din grupa 80.
- Contul și jurnalul se creează la instalare pe companiile cu planul RO și automat pe companiile noi, la încărcarea planului.
- Ierarhie: în Odoo 20 grupele de conturi sunt conturi părinte; planul RO nu are ierarhie, iar pe bazele migrate din 19.0 contul 803999 se creează sub același părinte ca celelalte conturi 803x.
- Contul 803999 rămâne numai pentru contrapartidă; valorile reale din 8039 (ex. consignație) se țin pe un analitic propriu (ex. 803901).
- Setări în **Facturare → Configurare → Setări**, secțiunea Off-Balance Accounts: contul de contrapartidă și jurnalul (completate singure la instalare).
- Control: soldul creditor al 803999 egalează suma soldurilor debitoare ale conturilor de evidență înregistrate cu această contrapartidă; opțiunea **Hide off-balance accounts** din balanța de verificare (`l10n_ro_reports_fix`) scoate clasa 8 din totaluri.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): configurarea contului tehnic și a jurnalului EXTR (`_l10n_ro_setup_off_balance`).
- `res.config.settings` (extins): câmpurile de setări pentru contrapartidă și jurnal.
- `account.chart.template` (extins): creează contul și jurnalul pe companiile care încarcă planul RO după instalare.

**Vizualizări**

- `res_config_settings_view_form_off_balance`: secțiunea de setări pentru contrapartidă și jurnal.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: configurează companiile cu planul RO deja încărcat. Nu are cron-uri.

#### 5. Conexiuni

- [l10n_ro_move_template](../l10n_ro_move_template/index.md): șabloanele de comodat folosesc contrapartida tehnică și jurnalul EXTR.
- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): obiectele de inventar (8035) folosesc convenția.
- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md): consignația (8033) folosește convenția.
- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md): opțiunea Hide off-balance accounts din balanța de verificare.
