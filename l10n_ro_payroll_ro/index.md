# Romania - Payroll Income Tax & Personal Deduction (localizat la `l10n_ro_payroll_ro/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_ro`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_ro
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_ro`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul corectează calculul impozitului pe venitul din salarii și adaugă deducerea personală
de bază (DPB) în statul de plată românesc, peste structura nativă Odoo 19 Enterprise
(`l10n_ro_hr_payroll`). Regula nativă `INCOMETAX` calculează impozitul ca 10% din salariul brut,
ceea ce este greșit fiscal — conform Codului fiscal, impozitul pe salarii trebuie aplicat pe
baza redusă: 10% × (brut − CAS − CASS − deducere personală). Nativul nu are deloc deducerea
personală, astfel încât atât impozitul cât și salariul net rezultau incorecte (cu impact și
asupra declarației D112).

#### 2. Funcționalități Cheie

- Adaugă regula salarială **DEDUCERE (DPB)** — deducerea personală de bază calculată în funcție
  de numărul de persoane în întreținere și de salariul minim aplicabil (S1 general / S2
  construcții), cu descreșterea liniară a deducerii până la plafonul salariu minim + 2.000 lei
  (Cod fiscal, art. 77).
- Corectează regula **INCOMETAX** să folosească baza corectă: brut − CAS − CASS − DPB.
- Păstrează salariul net corect — DPB reduce doar baza impozabilă, nu și netul.
- Ține cotele și plafoanele în parametri versionați pe dată (`hr.rule.parameter`), astfel încât
  actualizarea anuală a valorilor nu necesită modificări de cod.
- Adaugă pe fișa angajatului și pe versiunea de contract câmpurile **Persoane în întreținere**
  (`l10n_ro_dependent_persons`) și **Tip salariu minim** (`l10n_ro_min_wage_tier`: S1/S2).
- Asigură coerența cu declarația D112 (`l10n_ro_anaf_d112`), deoarece ambele module folosesc
  aceeași funcție de calcul al deducerii personale (`compute_dpb`).

> **Notă:** facilitățile fiscale speciale (scutire impozit IT, reduceri CAS/CASS pentru
> construcții și agro-alimentar) au fost abrogate începând cu 01.01.2025 și nu sunt incluse
> în acest modul.

#### 3. Dependențe

- `l10n_ro_hr_payroll`
- `l10n_ro_hr_payroll_account`

#### 4. Componente Cheie

**Modele**

- `hr.version` (extins): adaugă câmpurile `l10n_ro_min_wage_tier` (tip salariu minim S1/S2) și
  `l10n_ro_dependent_persons` (persoane în întreținere), folosite la calculul DPB pe versiunea
  de contract.
- `hr.employee` (extins prin views): aceleași câmpuri disponibile direct pe fișa angajatului.
- `hr.payslip` (extins): expune metoda `_l10n_ro_dpb()` pentru calculul deducerii personale de
  bază, apelată de regula salarială DPB în timpul confirmării fluturașului.
- Parametri salariali (`hr.rule.parameter`): cotele, plafoanele și pragurile DPB, versionate
  pe dată, definite în `data/hr_rule_parameter_data.xml`.

**Vizualizări**

- `view_hr_contract_template_form_l10n_ro_dpb`: adaugă câmpurile Tip salariu minim și Persoane
  în întreținere pe formularul versiunii de contract (`hr.version`), vizibile doar pentru RO.
- `view_hr_employee_form_l10n_ro_dpb`: aceleași câmpuri pe formularul angajatului
  (`hr.employee`), vizibile doar pentru RO.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`;
regulile salariale (`DEDUCERE`/DPB și `INCOMETAX` corectat) rulează în cadrul motorului
standard de calcul al fluturașului, definite în `data/hr_salary_rule_data.xml` și
`data/hr_salary_rule_category_data.xml`.

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația D112 folosește aceeași logică
  de calcul a deducerii personale (`compute_dpb`) ca și acest modul, pentru a asigura coerența
  între statul de plată și declarație.
- `l10n_ro_hr_payroll`: furnizează structura salarială de bază pentru Romania (regulile GROSS,
  CAS, CASS, INCOMETAX native) peste care acest modul aplică corecțiile fiscale.
- `l10n_ro_hr_payroll_account`: integrarea contabilă a statului de plată RO, dependență directă
  a modulului.
