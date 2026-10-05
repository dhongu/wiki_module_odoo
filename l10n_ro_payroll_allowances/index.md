# Romania - Sporuri, ore suplimentare și muncă de noapte (localizat la `l10n_ro_payroll_allowances/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_allowances`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_allowances
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_allowances`
- **Ultima Ingestie:** `2026-10-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Aduce în brutul fluturașului sporurile plătite lunar: sporuri permanente pe angajat, spor pentru orele suplimentare și spor pentru munca de noapte, cu procent și bază configurabile. Contabilul nu mai calculează sporurile de mână: ele intră în CAS, CASS, CAM și impozit, iar cele permanente intră în media indemnizației de concediu de odihnă.

#### 2. Funcționalități Cheie

- **Nomenclator de sporuri** (*Stat de plată → Configurare → Sporuri salariale*): cod, tip (permanent, ore suplimentare, muncă de noapte), procent și bază (salariu de bază, salariu aferent timpului lucrat sau salariu de bază plus celelalte sporuri), plus bifa «în baza orelor suplimentare». Procentele orelor suplimentare (75%) și ale muncii de noapte (25%) sunt minimul legal și nu pot fi coborâte; cele două sporuri nu se arhivează.
- **Sporuri permanente pe angajat** (fișa angajatului, fila *Stat de plată*): procent sau sumă fixă, cu perioadă de valabilitate. Regula `SPORPERM` (secvența 48, sub indemnizația de CO) le adună într-o linie în brut. În luna cu timp nelucrat, sporurile pe salariul de bază și sumele fixe se proratează cu timpul lucrat.
- **Ore suplimentare:** orele din prezențe de tip *Ore suplimentare* (OVERTIME, inclusiv din `l10n_ro_hr_pontaj_payroll`) se plătesc la 100% prin salariul de bază, iar regula `SPOR_ORE_SUPL` adaugă sporul de 75% × tarif orar (salariu lunar / orele normale ale lunii, plus sporurile marcate «în baza orelor suplimentare»).
- **Muncă de noapte:** ore introduse pe fluturaș (intrarea *Ore de noapte*, `NIGHT_HOURS`); regula `SPOR_NOAPTE` plătește 25% × tarif orar × ore.
- **Limite:**
    - munca în sărbători legale (cel puțin 100%) și în repausul săptămânal suspendat sau cumulat (cel puțin 150%) nu se distinge;
    - orele compensate cu timp liber se pontează pe alt tip de prezență, neplătit; tipul *Ore suplimentare* trebuie să aibă rata 100%;
    - orele de noapte nu vin din prezențe, iar condiția de 3 ore nu se verifică;
    - clauza de mobilitate (art. 76 alin. (4^1), neimpozabilă, în D112) nu este implementată.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.salary.supplement`: nomenclatorul de sporuri, cu minimul legal impus pe procente.
- `l10n.ro.hr.supplement.line`: sporul permanent al unui angajat (procent sau sumă fixă, valabilitate).
- `hr.payslip` extins: calculul sporurilor permanente, al sporului de ore suplimentare și de noapte, tariful orar.

**Vizualizări**

- `views/l10n_ro_salary_supplement_views.xml`: lista, formularul și meniul nomenclatorului.
- `views/hr_employee_views.xml`: secțiunea *Sporuri permanente (RO)* pe fișa angajatului.
- `data/hr_salary_rule_data.xml`: regulile `SPORPERM`, `SPOR_ORE_SUPL`, `SPOR_NOAPTE` (categoria ALW).

**Acțiuni Automate / Acțiuni Server**

Nu are `ir.cron` sau acțiuni server. Nomenclatorul și intrarea `NIGHT_HOURS` vin din date (`noupdate` la nomenclator).

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): fluturașul, regulile și media indemnizației de concediu (art. 150).
- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): produce orele de tip OVERTIME din pontaj.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): sporurile intră în venitul brut și în bazele asiguratului.
- `l10n_ro_hr_payroll_account_enhancement`: nota contabilă a fluturașului (641 = 421).
