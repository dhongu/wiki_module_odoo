# Romania - Localități

- **Nume Tehnic:** `l10n_ro_city`
- **Versiune:** `20.0.1.10.1`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_city
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_city
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul încarcă în baza de date nomenclatorul localităților din România (cod SIRUTA, județ, cod poștal), astfel încât adresele partenerilor să fie completate uniform, cu localitate aleasă dintr-o listă.

#### 2. Funcționalități Cheie

- Nomenclator de peste 13.700 de localități, cu cod SIRUTA, județ, cod poștal și municipiu/comună de care aparțin.
- Județele României actualizate (`res.country.state`).
- Pe partener, localitatea se alege din lista filtrată după județ; județul și localitatea se pot completa pornind de la codul poștal.
- Corecție în 20.0.1.10.1: prefixul codului poștal pentru județul Giurgiu era `87` în loc de `08`; la actualizare bazele existente primesc prefixul corect.

#### 3. Dependențe

- `base_address_extended`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `res.city`: localitățile, extinse cu SIRUTA, municipiu și mixin-ul românesc.
- `res.country.state`: județele.
- `res.partner`: câmpul `city_id` filtrat după județ și onchange-uri pe județ, cod poștal și localitate.

**Vizualizări**

- `view_city_tree`: lista localităților.

**Acțiuni Automate / Acțiuni Server**

- Nu are; datele se încarcă din `data/res.city.csv` și `data/res.country.state.csv`.

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): configurarea de bază a localizării.
