# Romania - Sporuri, ore suplimentare și muncă de noapte (localizat la `l10n_ro_payroll_allowances/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_allowances`
- **Versiune:** `20.0.1.1.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_allowances
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_allowances`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Aduce sporurile din salarizare în brutul fluturașului: sporuri permanente pe angajat, spor pentru ore suplimentare, muncă de noapte, muncă în sărbători legale și în repaus săptămânal, toate cu procent și bază configurabile. Procentele nu pot coborî sub minimul legal. Modulul nu se instalează automat, fiindcă schimbă brutul.

#### 2. Funcționalități Cheie

- **Nomenclator de sporuri** (*Stat de plată → Configurare → Sporuri salariale*): cod, tip, procent implicit, baza de calcul (salariul de bază, salariul aferent timpului lucrat sau salariul de bază plus sporurile permanente) și bifa «în baza orelor suplimentare». Sunt precreate sporurile de ore suplimentare (75%), noapte (25%), sărbători legale (100%) și repaus săptămânal (multiplicator 2 față de sporul de ore suplimentare).
- **Sporuri permanente pe angajat** (fila *Stat de plată*, secțiunea *Sporuri permanente (RO)*): procent sau sumă fixă, perioadă de valabilitate; regula `SPORPERM` le adună într-o linie din brut (intră în CAS, CASS, CAM, impozit; contabil 641 = 421) și intră în media indemnizației de concediu de odihnă. În luna cu absențe, sporurile se proratează cu timpul lucrat.
- **Ore suplimentare** (`SPOR_ORE_SUPL`): din prezențele de tip *Ore suplimentare*; orele se plătesc la tariful orar prin salariul de bază, iar sporul se adaugă separat. Orele compensate cu timp liber nu se plătesc în luna lucrată.
- **Sărbători legale** (`SPOR_SARBATOARE`) și **repaus săptămânal** (`SPOR_REPAUS`): aplicate orelor din tipurile de prezență produse de pontaj; la repaus, sporul este multiplicator al sporului de ore suplimentare.
- **Muncă de noapte** (`SPOR_NOAPTE`): orele de noapte (22:00–06:00) se introduc manual pe fluturaș, în intrarea *Ore de noapte*.
- Limitele (ex. fără evidență a soldului de compensare, condițiile de salariat de noapte nevalidate) sunt detaliate în fișă și în DESCRIPTION; fluxul pas-cu-pas e în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.salary.supplement`: nomenclatorul de sporuri.
- `l10n.ro.hr.supplement.line`: sporul permanent al unui angajat.
- `hr.employee`, `hr.payslip`: extinse pentru sporurile permanente și calculul în fluturaș.

**Vizualizări**

- `view_l10n_ro_salary_supplement_form` / `_list`: nomenclatorul de sporuri.
- `view_hr_employee_form_l10n_ro_supplements`: secțiunea de sporuri permanente pe angajat.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate; datele conțin sporurile implicite, intrările și regulile salariale.

#### 5. Conexiuni

- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): produce tipurile de prezență pentru orele suplimentare, de sărbătoare și de repaus.
- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md): foaia de pontaj și codurile de pontaj (`OC`, `RS`).
