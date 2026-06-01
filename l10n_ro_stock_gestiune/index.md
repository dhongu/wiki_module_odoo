# Gestiuni Contabile de Stoc România (FR-54) (localizat la `l10n_ro_stock_gestiune/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_gestiune`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_gestiune
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_gestiune`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Acest modul extinde `deltatech_valuation_area` pentru evidența gestiunilor contabile de stoc conform Legii 82/1991 și OMFP 2861/2009. Adaugă pe fiecare gestiune informații specifice românești (gestionar responsabil, cont de stoc principal, cont de transfer între gestiuni, politică de inventariere) și validează transferurile valorice între gestiuni cu conturi de stoc diferite, blocându-le când lipsește contul de transfer configurat.

## 2. Funcționalități Cheie

- **Câmpuri gestiune RO** pe `valuation.area`: gestionar responsabil, cont stoc principal (clasa 3), cont transfer între gestiuni, politică de inventariere (la cerere / periodică / anuală) și flag activ/inactiv.
- **Validare transfer inter-gestiune:** blochează transferul direct între gestiuni cu conturi diferite dacă nu există cont de transfer configurat (mod strict, activabil din Setări → Contabilitate).
- **Metode utile pe `stock.move`:** `l10n_ro_is_inter_gestiune()`, `l10n_ro_needs_transfer_account()`, `l10n_ro_get_transfer_account()`.

## 3. Dependențe

- `account`
- `stock_account`
- `deltatech_valuation_area`
- `l10n_ro`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `valuation.area`: Extins cu câmpurile RO de gestiune (gestionar, conturi, politică inventariere).
- `stock.move`: Extins cu metodele de detectare a transferurilor inter-gestiune și de obținere a contului de transfer.

### Vizualizări / Date

- `views/valuation_area_views.xml`: Câmpurile RO pe formularul de gestiune.
- `views/res_config_settings_views.xml`: Setarea „Blocare transfer fără cont de transfer".

### Acțiuni Automate / Acțiuni Server

*Nu sunt definite acțiuni automate; validarea se aplică la momentul transferului de stoc.*

## 5. Conexiuni

- `l10n_ro_stock_constraints`
- `l10n_ro_stock_cmp_periodic`
