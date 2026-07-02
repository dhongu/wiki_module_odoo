# Romania - Declarația D112 ANAF (FR-44) (localizat la `l10n_ro_anaf_d112/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d112`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d112
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d112`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul generează fișierul XML al Declarației D112 — declarația privind obligațiile de plată a contribuțiilor sociale, a impozitului pe venit și evidența nominală a persoanelor asigurate. Modulul permite atât importul automat al datelor din statele de plată (când modulul de salarizare Enterprise este instalat), cât și completarea manuală pentru firmele care importă salariile din sisteme externe (SAGA, Nexus).

#### 2. Funcționalități Cheie

- **Model declarație** `l10n.ro.d112` cu state machine: ciornă → calculat → validat → exportat.
- **Linii nominale** `l10n.ro.d112.employee.line` cu CNP, venit brut, CAS/CASS/impozit per angajat, zile lucrate/CO/CM.
- **Import automat** din `hr.payslip` (Enterprise) folosind codurile de reguli `GROSS`, `CAS`, `CASS`, `INCOMETAX`.
- **Completare manuală** pentru salarii importate din sisteme externe.
- **Generator XML D112** (namespace `mfp:anaf:dgti:d112:declaratie:v5`) cu secțiunile A2 (CAM angajator 2,25%), A3 (date nominale per angajat), C1 (obligații de plată).
- **Totaluri** CAS/CASS/impozit/CAM calculate automat din linii.
- **Declarație rectificativă** legată de declarația inițială exportată.
- **Validare** înainte de export: CNP obligatoriu, venit pozitiv.

#### 3. Dependențe

- `account`
- `hr`
- `l10n_ro`
- `[[l10n_ro_anaf_base]]`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.d112`: declarația D112 cu state machine și generatorul de XML.
- `l10n.ro.d112.employee.line`: liniile nominale per angajat (CNP, venituri, contribuții, zile).

**Vizualizări / Securitate**

- `views/l10n_ro_d112_views.xml`: formularele și listele declarației și ale liniilor nominale.
- `views/menus.xml`: intrările de meniu pentru D112.
- `security/ir.model.access.csv`: drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); calculul, validarea și exportul se declanșează manual.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d100]]`
