# Romania - Localization Config Fix

- **Nume Tehnic:** `l10n_ro_config_fix`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_config_fix
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_config_fix`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul corectează comportamentul din `l10n_ro_config` (OCA), care ascunde în Setări orice câmp `l10n_ro_*` atunci când compania curentă nu folosește planul de conturi „ro”. O companie românească din punct de vedere fiscal, dar care nu a trecut explicit pe planul de conturi „ro”, nu mai pierde tacit setările din alte module (de exemplu tipul de export ANAF sau standardul de reevaluare valutară). Se instalează automat, fără configurare.

#### 2. Funcționalități Cheie

- Lărgește criteriul de „înregistrare românească” folosit de `l10n_ro_config`: pe lângă planul de conturi „ro”, este considerată românească și o companie cu țara fiscală România (`account_fiscal_country_id.code == 'RO'`).
- Setările, listele și căutările `l10n_ro_*` definite de alte module rămân vizibile pentru companiile românești care folosesc un plan de conturi generic sau de test.
- Nu modifică codul OCA, ci doar extinde verificarea printr-o suprascriere minimă.
- Se instalează automat (`auto_install`) odată cu `l10n_ro_config`.

#### 3. Dependențe

- `l10n_ro_config`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): suprascrie `_check_is_l10n_ro_record`; returnează True dacă verificarea originală trece sau dacă țara fiscală a companiei este RO.

**Vizualizări**

- Nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `l10n_ro_config`: modulul OCA a cărui verificare este corectată (mecanismul `l10n.ro.mixin.get_view` care ascunde câmpurile).
