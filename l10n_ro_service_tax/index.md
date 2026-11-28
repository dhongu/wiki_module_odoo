# Romania - Service Taxes

- **Nume Tehnic:** `l10n_ro_service_tax`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_service_tax
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_service_tax`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Taxele implicite de vânzare și de achiziție pentru produsele de tip **serviciu**, pentru firmele românești. Planul de conturi românesc are TVA separat pentru servicii (21% S) față de bunuri (21% G), iar Odoo permite o singură pereche de taxe implicite pe firmă; fără modul, un produs nou de tip serviciu ar primi taxele pentru bunuri și serviciile intracomunitare ar ajunge pe rândurile greșite din D300 și D390.

#### 2. Funcționalități Cheie

- Secțiunea *Taxe implicite pentru servicii* în **Contabilitate > Configurare > Setări > Taxe**, lângă taxele implicite standard (vizibilă pentru firmele cu România ca țară fiscală).
- Valorile `tvac_21_s` / `tvad_21_s` se completează la încărcarea planului de conturi românesc și la instalare pentru firmele care îl au deja.
- Pe produs, când tipul devine *Serviciu*, taxele de serviciu înlocuiesc taxele produsului (inclusiv cele puse manual); la revenirea la *Bunuri*, taxele de serviciu sunt înlocuite cu taxele implicite ale firmei (cele puse manual se păstrează).
- Numele câmpurilor coincid cu cele din modulul OCA `l10n_ro_config`, deci bazele care renunță la stack-ul OCA își păstrează configurarea fără migrare de date; ambele module pot fi instalate împreună.
- Pașii cu capturi sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

Descrierea din Readme nu detaliază componentele tehnice; lista provine din analiza codului.

**Modele**

- `res.company`: taxele implicite de vânzare și achiziție pentru servicii.
- `res.config.settings`: câmpurile `l10n_ro_serv_sale_tax_id` / `l10n_ro_serv_purchase_tax_id`.
- `account.chart.template`: completează taxele de servicii la încărcarea planului de conturi.
- `product.template`: schimbarea taxelor la modificarea tipului produsului.

**Vizualizări**

- `views/res_config_settings_views.xml`: blocul *Default Service Taxes* în setările de taxe.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: completează taxele pentru firmele cu planul de conturi românesc deja încărcat.

#### 5. Conexiuni

- `l10n_ro_config` (OCA): folosește aceleași nume de câmpuri; modulele pot coexista.
