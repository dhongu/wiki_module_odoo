# Romania - Pontaj în salarizare (localizat la `l10n_ro_hr_pontaj_payroll/index.md`)

- **Nume Tehnic:** `l10n_ro_hr_pontaj_payroll`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_pontaj_payroll
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_pontaj_payroll`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul duce corecțiile din foaia colectivă de prezență (pontaj) în salarizarea Odoo, pe drumul standard al prezențelor (work entries). Astfel, zilele de concediu, absențele și orele lucrate diferit de program, corectate în pontaj, ajung în fluturaș și în declarația D112 fără evidențe paralele. Nu se instalează automat, deoarece schimbă prezențele din care se calculează fluturașii.

#### 2. Funcționalități Cheie

- O zi corectată în pontaj cu un cod de concediu sau absență (absență nemotivată, concediu trecut de mână etc.) devine o prezență de tipul codului, pentru orele zilei din program; prezențele generate de program, sărbători și concedii pentru acea zi sunt înlocuite.
- Zi lucrată (`8`, `D`) cu alte ore decât programul:
  - mai puține ore: orele lucrate, iar diferența până la program ca absență nemotivată (`N`), ca salariul lunar să nu se plătească întreg pentru o zi scurtă;
  - mai multe ore: orele programului, iar surplusul pe tipul *ore suplimentare* (OVERTIME);
  - în zi de repaus sau sărbătoare legală: toate orele ca ore suplimentare, sărbătoarea rămânând plătită (Codul muncii, art. 120–123, 137, 142); sporul se calculează în structura salarială.
- La adăugarea, schimbarea sau ștergerea unei corecții se regenerează doar ziua respectivă, dacă prezențele lunii sunt deja generate; prezențele validate nu se ating.
- Ștergerea corecției (sau „Înapoi la codul generat” în pontaj) readuce ziua la program și concedii și în salarizare.
- Fluturașul citește zilele din prezențe ca de obicei: fiecare cod apare ca linie de zile lucrate (ex. `L10N_RO_N` pentru absență nemotivată, `L10N_RO_D` pentru delegație, `LEAVE120` pentru concediu de odihnă). D112 ia de acolo zilele lucrate, de concediu de odihnă și de concediu medical.
- Configurare: fiecare cod de pontaj folosit trebuie să aibă un **tip de prezență** (*Concediu* → *Configurare* → *Pontaj (RO)* → *Coduri pontaj*); un cod fără tip rămâne doar pe foaie și nu schimbă salarizarea. Regulile din structura salarială citesc liniile de zile lucrate după codul tipului (`worked_days.L10N_RO_N`, `worked_days.LEAVE120` etc.).
- Flux: corecția se face în *Concediu* → *Management* → *Pontaj*; se generează fluturașul; după validarea fluturașilor se închide luna în pontaj.

#### 3. Dependențe

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md)
- `hr_payroll`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.pontaj.override` (extins): la creare, modificare și ștergere a unei corecții regenerează prezențele zilelor afectate (`_l10n_ro_regenerate_work_entries`).
- `hr.version` (extins): în generarea prezențelor (`_generate_work_entries`, `_generate_work_entries_postprocess`) înlocuiește prezențele zilelor corectate cu cele derivate din pontaj (`_l10n_ro_pontaj_vals`), inclusiv tratarea sărbătorilor legale.

**Vizualizări**

- Modulul nu definește vizualizări proprii (fără fișiere de date).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): declarația D112 preia zilele lucrate, de concediu de odihnă și medical din prezențele generate.
