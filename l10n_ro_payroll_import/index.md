# Romania - Import note de salarii (localizat la `l10n_ro_payroll_import/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_import`
- **Versiune:** `20.0.1.1.5`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_import](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_import)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_import`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite importul notelor contabile de salarii generate de aplicații externe de salarizare direct în Odoo, fără reintroducere manuală. Se adresează companiilor care țin salarizarea în aplicații externe și trebuie să preia lunar nota contabilă de salarii în Odoo, cu distribuție pe centre de cost analitice. Nu generează D112 și nu reconciliază plățile salariale din bancă.

#### 2. Funcționalități Cheie

- **Import fișiere** în format JSON (structură flexibilă), CSV (separator virgulă sau punct și virgulă) și Excel (XLSX), cu denumiri de coloane în română sau engleză; wizardul se deschide din **Contabilitate → Contabilitate → Note Salarii → Încarcă fișier salarii**, cu perioada (ultima zi a lunii), jurnalul și, opțional, configurarea de mapare.
- **Câmpuri suportate:** cont debit, cont credit, sumă, centru de cost, departament, descriere. Sumele negative (stornări) se importă ca valori negative.
- **Mapare conturi** `cod extern → cont Odoo`, per companie, cu fallback automat pe prefix de cod (ex. `641` → primul cont care începe cu `641`); configurarea e în **Note Salarii → Configurare Mapare Conturi**, vizibilă pentru grupul Contabil șef / Administrator.
- **Mapare analitică** `cod centru de cost extern → cont analitic Odoo`, cu distribuție 100% pe centrul indicat.
- **Validare și contabilizare:** verificare debit = credit, blocarea importului duplicat pentru aceeași perioadă și același jurnal, creare automată a notei contabile postate într-un jurnal de tip Diverse.
- **Anulare și corectare:** anularea importului anulează nota contabilă asociată, iar „Resetează la Schiță" permite corectarea sau reimportul.
- **Flux de stări:** Schiță → Validat → Contabilizat → Anulat. Fluxul pas-cu-pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `analytic`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.import`: documentul de import (perioadă, jurnal, sistem sursă, stare, nota contabilă generată); orchestrează validarea, postarea, anularea și resetarea.
- `l10n.ro.payroll.import.line`: linia de import (cont debit, cont credit, sumă); moștenește `analytic.mixin` pentru distribuția analitică.
- `l10n.ro.payroll.account.mapping`: configurarea de mapare pe companie; rezolvă contul (cu fallback pe prefix) și distribuția analitică.
- `l10n.ro.payroll.account.mapping.line`: linie de mapare `cod extern → cont Odoo`.
- `l10n.ro.payroll.analytic.mapping.line`: linie de mapare `cod centru de cost extern → cont analitic`.
- `l10n.ro.payroll.import.wizard`: wizardul de încărcare a fișierului; detectează formatul, parsează datele și creează importul cu linii (XLSX cere biblioteca opțională `openpyxl`).

**Vizualizări**

- `l10n_ro_payroll_import_views.xml`: formular și listă pentru documentul de import (butoane Validează / Contabilizează / Anulează / Resetează, link la nota contabilă).
- `l10n_ro_payroll_account_mapping_views.xml`: formular și listă pentru maparea conturilor și a centrelor de cost.
- `l10n_ro_payroll_import_wizard_views.xml`: formularul wizardului de import.
- `menus.xml`: meniurile din Contabilitate (Note Salarii, Import Note Salarii, Configurare Mapare Conturi).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau acțiuni server; importul se declanșează manual prin wizard.

#### 5. Conexiuni

- `l10n_ro`: localizarea contabilă românească (planul de conturi RO) pe care se bazează monografia salarială.
- `analytic`: contabilitatea analitică (centre de cost) folosită pentru distribuția liniilor.
