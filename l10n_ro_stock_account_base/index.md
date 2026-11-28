# Romania - Stock Accounting Fields

- **Nume Tehnic:** `l10n_ro_stock_account_base`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_account_base
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_base`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Păstrează câmpurile modulului OCA `l10n_ro_stock_account`, fără logica lui, pentru ca o bază de date care a avut modulul OCA să-și păstreze coloanele și datele, iar modulul OCA să poată fi eliminat și datele migrate la versiunea următoare. Nu adaugă comportament, ecrane sau logică contabilă.

#### 2. Funcționalități Cheie

- Include conturile de firmă folosite de contabilitatea stocurilor din `l10n_ro_config` (aviz de plătit și de încasat, dare în folosință, transfer de stoc, taxă neeligibilă), pentru ca `l10n_ro_config` să poată fi eliminat.
- Câmpurile calculate din modulul OCA (`l10n_ro_move_type`, `l10n_ro_account_id`, `l10n_ro_transfer_account_id`, `fifo_per_location`, `fifo_location_negative_compensation`) sunt aici câmpuri stocate simple: nu se completează pentru înregistrările noi.
- Fără vizualizări și fără dependență de `l10n.ro.mixin`; notele contabile de stoc sunt făcute de modulul de valorizare instalat în bază.
- Procedură: se lucrează pe o copie a bazei, cu backup; se instalează `l10n_ro_stock_base` și acest modul înainte de dezinstalarea modulului OCA `l10n_ro_stock_account` (și `l10n_ro_stock`, dacă nu mai e necesar); `l10n_ro_config` se dezinstalează abia după preluarea celorlalte câmpuri ale lui. Câmpurile se verifică în **Setări > Tehnic > Structura bazei de date > Câmpuri** (mod dezvoltator), iar valorile se citesc prin **Acțiuni > Export**. Detalii în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock_account`
- `l10n_ro_stock_base`

#### 4. Componente Cheie

Descrierea din Readme nu detaliază componentele tehnice; lista provine din analiza codului.

**Modele**

- `res.company`: conturile de stoc din `l10n_ro_config` și opțiunile FIFO pe locație.
- `stock.move`: tipul mișcării și conturile de valorizare/transfer.
- `stock.picking`: `l10n_ro_notice`, `l10n_ro_reception_in_progress`.
- `stock.location`, `stock.warehouse`: conturi pe locație, poziție fiscală pe depozit.
- `account.move`, `account.account`, `product.category`, `product.template`: câmpuri de stocare păstrate din modulul OCA.

**Vizualizări**

- Nu are.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_stock](../l10n_ro_stock/index.md): omologul OCA `l10n_ro_stock` din care provin datele; modulul de bază `l10n_ro_stock_base` îl înlocuiește.
- `l10n_ro_config` (OCA): cinci conturi de firmă preluate aici.
