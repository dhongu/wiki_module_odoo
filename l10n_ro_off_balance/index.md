# Romania - Evidență extrabilanțieră (clasa 8)

- **Nume Tehnic:** `l10n_ro_off_balance`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_off_balance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_off_balance`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Conturile din grupa 80 (în afara bilanțului) se țin în partidă simplă, dar Odoo cere ca orice notă contabilă să fie echilibrată. Modulul stabilește o convenție unică pentru toate modulele Terrabit care scriu note extrabilanțiere: un cont tehnic de contrapartidă, un jurnal dedicat și grupele clasei 8 în planul de conturi. Astfel, conturile de evidență își păstrează soldul real, iar notele rămân echilibrate.

#### 2. Funcționalități Cheie

- **Cont tehnic 803999** (Contrapartidă tehnică evidență extrabilanțieră), analitic al sinteticului 8039. Echilibrează nota (ex. Dr 8033 = Cr 803999); se încadrează în nomenclatorul de conturi SAF-T (D406). Rămâne numai pentru contrapartidă; valorile reale din 8039 (ex. mărfuri primite în consignație) se țin pe un analitic propriu, ex. 803901. Pe bazele existente ele pot rămâne pe 803900 sau se reclasifică prin Dr 803901 = Cr 803900.
- **Jurnal EXTR** (Evidență extrabilanțieră), comun pentru toate notele din grupa 80.
- **Grupele clasei 8** (8, 80, 801–809, 89) create în planul de conturi, ca balanța de verificare să nu mai afișeze conturile sub „No Group”.
- Crearea automată a contului, jurnalului și grupelor la instalare pe companiile cu plan de conturi RO și pe companiile noi, la încărcarea planului.
- Configurare în **Facturare → Configurare → Setări**, secțiunea „Romania - Off-Balance Accounts”: **Counterpart Account** (implicit 803999) și **Journal** (implicit EXTR); se schimbă doar dacă firma folosește alt analitic tehnic sau alt jurnal.
- Modulul nu are meniuri proprii; notele generate de modulele care îl folosesc ajung în jurnalul EXTR, cu contrapartida 803999.
- Control: soldul creditor al contului 803999 este egal cu suma soldurilor debitoare ale conturilor de evidență înregistrate cu această contrapartidă. În balanța de verificare, opțiunea „Hide off-balance accounts” scoate toată clasa 8 din totaluri.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): câmpurile `l10n_ro_off_balance_account_id` și `l10n_ro_off_balance_journal_id` (contul și jurnalul extrabilanțier ale companiei) și logica de creare a contului, jurnalului și grupelor.
- `res.config.settings` (extins): expune cele două câmpuri în setări.
- `account.chart.template` (extins): creează elementele pe companiile noi la încărcarea planului de conturi.

**Vizualizări**

- `res_config_settings_view_form_off_balance`: blocul „Romania - Off-Balance Accounts” în setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare creează contul, jurnalul și grupele pe companiile cu plan RO existente.

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): obiecte de inventar (cont 8035), folosește convenția.
- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md): custodie/consignație (cont 8033), folosește convenția.
- [l10n_ro_move_template](../l10n_ro_move_template/index.md): șabloane de note contabile (cont 8031), folosește convenția.
- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md): opțiunea „Hide off-balance accounts” din balanța de verificare.
