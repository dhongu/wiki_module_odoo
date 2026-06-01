# Import Note Salarii (localizat la `l10n_ro_payroll_import/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_import`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_payroll_import
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_import`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul permite importul notelor contabile de salarii generate de aplicații externe de salarizare (SAGA, Nexus, Charisma, WizSalary etc.) direct în Odoo 19, eliminând reintroducerea manuală. Acceptă fișiere JSON și CSV, mapează codurile externe la conturile Odoo (cu fallback automat după prefix) și distribuie analitic sumele pe centre de cost, creând automat notă contabilă echilibrată în starea postată.

#### 2. Funcționalități Cheie

- Import în format JSON (structură flexibilă) și CSV (delimitatori automați, denumiri de coloane în română și engleză).
- Câmpuri suportate: cont debit, cont credit, sumă, centru de cost, departament, descriere; cu aliasuri multiple pentru numele coloanelor.
- Tabel de mapare cont extern → cont Odoo configurat per companie, cu fallback automat după prefix de cod.
- Mapare analitică cod centru cost extern → cont analitic Odoo, cu distribuție analitică 100% pe centrul indicat.
- Verificare echilibru debit = credit și blocarea importului duplicat pentru aceeași perioadă și jurnal.
- Creare automată a notei contabile (`account.move`) în starea posted, cu anulare prin reversare.
- Flux de stări: draft → validated → posted → cancelled.

#### 3. Dependențe

- `account`
- `[[l10n_ro]]`
- `analytic`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.import`: Documentul de import cu fluxul de stări și generarea notei contabile.
- `l10n.ro.payroll.account.mapping`: Tabelul de echivalență cod extern → cont Odoo / cont analitic.
- Wizard de import: încarcă și parsează fișierul JSON/CSV.

**Vizualizări / Date**

- `views/l10n_ro_payroll_import_views.xml`, `views/l10n_ro_payroll_account_mapping_views.xml`, `views/menus.xml`: Interfețele de import și configurare a mapării.
- `wizard/l10n_ro_payroll_import_wizard_views.xml`: Wizardul de încărcare fișier.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; importul este declanșat manual prin wizard.*

#### 5. Conexiuni

- `[[l10n_ro]]`
