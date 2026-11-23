# Romania - Import note de salarii (localizat la `l10n_ro_payroll_import/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_import`
- **Versiune:** `19.0.1.1.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_import
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_import`
- **Ultima Ingestie:** `2026-11-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite importul notelor contabile de salarii generate de aplicații externe de salarizare (SAGA, Nexus, Charisma, WizSalary etc.) direct în Odoo 19, fără reintroducere manuală. Se adresează companiilor care țin salarizarea într-o aplicație externă și preiau lunar nota contabilă de salarii în Odoo, cu distribuție pe centre de cost analitice. Nu generează D112 și nu reconciliază plățile salariale din bancă.

#### 2. Funcționalități Cheie

- **Import fișiere** (**Contabilitate → Contabilitate → Note Salarii → Încarcă fișier salarii**): suportă JSON (cu `source_system`, `period` și lista `lines`), CSV (antet `account_debit,account_credit,amount,description,cost_center`, separator virgulă sau punct și virgulă) și Excel (XLSX), cu denumiri de coloane în română și engleză. În wizard se aleg fișierul, formatul, perioada (ultima zi a lunii de salarii), jurnalul și, opțional, configurarea de mapare. Documentele importate apar în **Import Note Salarii**; o notă se poate crea și manual, cu **Nou**.
- **Câmpuri suportate** — cont debit, cont credit, sumă, centru de cost, departament, descriere. Sumele negative (stornări) se importă ca valori negative, echivalent stornării în roșu; defalcările pe mai multe centre de cost se trimit ca linii separate, cu sumă proporțională.
- **Mapare conturi** (**Note Salarii → Configurare Mapare Conturi**, doar pentru grupul `Contabil șef / Administrator`) — tabel de echivalență `cod extern → cont Odoo` per companie (denumire, sistem sursă, companie), cu fallback automat prin căutare după prefix de cod (ex. `641` → primul cont care începe cu `641`); maparea este opțională.
- **Mapare analitică** (fila „Mapare centre de cost”) — `cod centru cost extern → cont analitic Odoo`, cu distribuție 100% pe centrul indicat; poate rămâne goală dacă nu se folosește contabilitate analitică.
- **Jurnal de salarii** — se folosește un jurnal de tip Diverse, dedicat salariilor.
- **Validare și contabilizare** — butonul **Validează** blochează importul fără linii sau cu un import deja contabilizat pentru aceeași perioadă și același jurnal (anti-duplicat); bannerul **Notă echilibrată** confirmă debit = credit; **Contabilizează** creează și postează nota contabilă (`account.move`) în jurnalul ales, iar câmpul **Notă contabilă** devine link către ea.
- **Anulare și corectare** — **Anulează** anulează nota contabilă asociată, iar **Resetează la Schiță** permite corectarea liniilor sau reimportul; dacă există un import contabilizat pentru perioadă, acesta se anulează întâi.
- **Flux de stări** — `Schiță` → `Validat` → `Contabilizat` → `Anulat`. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `analytic`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.import`: documentul de import notă salarii (header) — perioadă, jurnal, sistem sursă, stare și nota contabilă generată; orchestrează validarea, postarea, anularea și resetarea; moștenește `mail.thread` și `mail.activity.mixin`.
- `l10n.ro.payroll.import.line`: linia de import (cont debit + cont credit + sumă); moștenește `analytic.mixin` pentru distribuția analitică pe centre de cost.
- `l10n.ro.payroll.account.mapping`: configurarea de mapare conturi per companie; expune `get_account` (cu fallback pe prefix de cod) și `get_analytic_distribution`.
- `l10n.ro.payroll.account.mapping.line`: linie de mapare `cod extern → cont Odoo`.
- `l10n.ro.payroll.analytic.mapping.line`: linie de mapare `cod centru cost extern → cont analitic Odoo`.
- `l10n.ro.payroll.import.wizard`: wizard de încărcare fișier (JSON/CSV/XLSX) care detectează formatul după extensie, parsează datele și generează importul cu liniile aferente (parsarea XLSX necesită biblioteca opțională `openpyxl`).

**Vizualizări**

- `l10n_ro_payroll_import_views.xml`: formular și listă pentru documentul de import (butoane Validate / Post / Cancel / Reset to Draft / View Accounting Note, distribuție analitică pe linie).
- `l10n_ro_payroll_account_mapping_views.xml`: formular și listă pentru configurarea mapării conturilor și a centrelor de cost.
- `l10n_ro_payroll_import_wizard_views.xml`: formularul wizardului de import fișier.
- `menus.xml`: meniurile sub Contabilitate (Note Salarii, Import Note Salarii, Configurare Mapare Conturi).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în modul; importul este declanșat manual prin wizard.

#### 5. Conexiuni

- `l10n_ro`: localizarea contabilă românească (plan de conturi RO) pe care se bazează monografia salarială.
- `analytic`: contabilitatea analitică (centre de cost) folosită pentru distribuția analitică a liniilor.
