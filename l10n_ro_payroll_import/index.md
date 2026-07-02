# Romania - Import Note Salarii (localizat la `l10n_ro_payroll_import/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_import`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_payroll_import`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_import`
- **Ultima Ingestie:** `2026-06-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite importul notelor contabile de salarii generate de aplicații externe de salarizare (SAGA, Nexus, Charisma, WizSalary etc.) direct în Odoo 19, fără reintroducere manuală. Se adresează companiilor care gestionează salarizarea într-o aplicație externă și trebuie să importe lunar nota contabilă de salarii în Odoo, cu distribuție pe centre de cost analitice. Fișierul exportat (JSON sau CSV) este parsat, codurile externe sunt mapate pe conturile Odoo, iar după validare se generează automat nota contabilă (`account.move`) postată, conform monografiei salariale (641 / 421 / 4315 / 4316 / 444 / 646 / 436).

#### 2. Funcționalități Cheie

- **Import fișiere** — suportă format JSON (structură flexibilă exportată de aplicații moderne) și format CSV (delimitatori automați: virgulă sau punct-și-virgulă), cu suport pentru denumiri de coloane în română și engleză.
- **Câmpuri suportate** — cont debit, cont credit, sumă, centru de cost, departament, descriere.
- **Mapare conturi** — tabel de echivalență `cod extern → cont Odoo` configurat per companie, cu fallback automat prin căutare după prefix de cod (ex. `641` → primul cont care începe cu `641`).
- **Mapare analitică** — `cod centru cost extern → cont analitic Odoo`, cu distribuție 100% pe centrul de cost indicat.
- **Distribuție analitică pe linie** — linia de import moștenește `analytic.mixin`, expunând câmpul `analytic_distribution` pentru repartizarea pe centre de cost direct în formular.
- **Validare și contabilizare** — verificare echilibru debit = credit înainte de validare, blocare import duplicat pentru aceeași perioadă și același jurnal, creare automată notă contabilă (`account.move`) în starea `posted`.
- **Anulare** — anularea notei contabile asociate, cu reset la stare schiță pentru repostare.
- **Flux de stări** — `Schiță` → `Validat` → `Contabilizat` → `Anulat`.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `analytic`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.import`: documentul de import notă salarii (header) — perioadă, jurnal, sistem sursă, stare și nota contabilă generată; orchestrează validarea, postarea, anularea și resetarea.
- `l10n.ro.payroll.import.line`: linia de import (cont debit + cont credit + sumă); moștenește `analytic.mixin` pentru distribuția analitică pe centre de cost.
- `l10n.ro.payroll.account.mapping`: configurarea de mapare conturi per companie; expune `get_account` (cu fallback pe prefix de cod) și `get_analytic_distribution`.
- `l10n.ro.payroll.account.mapping.line`: linie de mapare `cod extern → cont Odoo`.
- `l10n.ro.payroll.analytic.mapping.line`: linie de mapare `cod centru cost extern → cont analitic Odoo`.
- `l10n.ro.payroll.import.wizard`: wizard de încărcare fișier (JSON/CSV) care parsează datele și generează importul cu liniile aferente.

**Vizualizări**

- `l10n_ro_payroll_import_views.xml`: formular și listă pentru documentul de import (butoane Validează / Postează / Anulează / Resetează, link la nota contabilă, distribuție analitică pe linie).
- `l10n_ro_payroll_account_mapping_views.xml`: formular și listă pentru configurarea mapării conturilor și a centrelor de cost.
- `l10n_ro_payroll_import_wizard_views.xml`: formularul wizardului de import fișier.
- `menus.xml`: meniurile sub Contabilitate (Note Salarii, Import Note Salarii, Configurare Mapare Conturi).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în modul; importul este declanșat manual prin wizard.

#### 5. Conexiuni

- `l10n_ro`: localizarea contabilă românească (plan de conturi RO) pe care se bazează monografia salarială.
- `analytic`: contabilitatea analitică (centre de cost) folosită pentru distribuția analitică a liniilor.
