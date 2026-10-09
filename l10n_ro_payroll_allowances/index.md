# Romania - Sporuri, ore suplimentare și muncă de noapte (localizat la `l10n_ro_payroll_allowances/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_allowances`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_allowances
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_allowances`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Aduce în brutul fluturașului sporurile plătite lunar: sporuri permanente pe angajat, spor pentru orele suplimentare, pentru munca de noapte, pentru munca în sărbători legale și în repaus săptămânal, cu procent și bază configurabile. Contabilul nu mai calculează sporurile de mână: ele intră în CAS, CASS, CAM și impozit, iar cele permanente intră în media indemnizației de concediu de odihnă.

#### 2. Funcționalități Cheie

- **Nomenclator de sporuri** (*Stat de plată → Configurare → Sporuri salariale*): cod, tip (permanent, ore suplimentare, muncă de noapte, sărbătoare legală, repaus săptămânal), procent sau multiplicator și bază (salariu de bază, salariu aferent timpului lucrat sau salariu de bază plus celelalte sporuri), plus bifa «în baza orelor suplimentare». Procentele orelor suplimentare (75%), ale muncii de noapte (25%) și ale sărbătorii legale (100%) sunt minimul legal și nu pot fi coborâte; sporurile legale nu se arhivează.
- **Sporuri permanente pe angajat** (fișa angajatului, fila *Stat de plată*): procent sau sumă fixă, cu perioadă de valabilitate. Regula `SPORPERM` (secvența 48, sub indemnizația de CO) le adună într-o linie în brut. În luna cu timp nelucrat, sporurile pe salariul de bază și sumele fixe se proratează cu timpul lucrat.
- **Ore suplimentare:** orele din prezențe de tip *Ore suplimentare* (OVERTIME, inclusiv din [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md)) se plătesc la 100% prin salariul de bază, iar regula `SPOR_ORE_SUPL` adaugă sporul de 75% × tarif orar (salariu lunar / orele normale ale lunii, plus sporurile marcate «în baza orelor suplimentare»).
- **Muncă în sărbătoare legală:** orele din prezențe de tip *Ore suplimentare în sărbătoare legală* primesc, prin regula `SPOR_SARBATOARE`, un spor de cel puțin 100% (art. 142 alin. (2)) peste plata de bază, pe aceeași bază orară ca orele suplimentare. Modulul `l10n_ro_hr_pontaj_payroll` pune automat pe acest tip orele pontate cu codul obișnuit într-o zi de sărbătoare legală.
- **Muncă în repaus săptămânal** (suspendat sau cumulat, art. 137–138): orele din prezențe de tip *Ore suplimentare în repaus săptămânal*, pontate cu codul `RS` (prioritar față de sărbătoare), primesc prin regula `SPOR_REPAUS` **dublul sporului de ore suplimentare**: 2 × 75% = 150%, iar dacă sporul de ore suplimentare e 100%, repausul se plătește cu 200%. Parametrul este un multiplicator, minim 2, nu o valoare fixă. Sporul dublu se aplică doar orelor peste programul zilei.
- **Ore compensate cu timp liber** (art. 122): orele pontate pe tipul *Ore suplimentare compensate cu timp liber* (cod `OC`) apar pe fluturaș, dar nu se plătesc și nu primesc spor în luna lucrată; orele libere luate ulterior (cod `REC`) se plătesc normal, deci nu se plătesc de două ori. Tipul *Ore suplimentare* se folosește numai pentru orele plătite.
- **Muncă de noapte:** ore introduse pe fluturaș (intrarea *Ore de noapte*, `NIGHT_HOURS`); regula `SPOR_NOAPTE` plătește 25% × tarif orar × ore.
- **Limite:**
    - munca în sărbători legale: legea (art. 142 alin. (1)) dă ca regulă timp liber în 30 de zile, iar sporul de cel puțin 100% (alin. (2)) se acordă doar dacă nu se dau zilele libere; aplicarea la angajatorii din afara art. 140–141 și plata separată a orelor sunt de confirmat juridic (și cu contractul colectiv); timpul liber se pontează cu `OC`, termenul de 30 de zile se ține manual;
    - repausul prestat în alte zile decât sâmbătă–duminică (art. 137 alin. (2)–(3)) nu are minim legal și se acoperă cu un spor permanent; clasificarea ca repaus se face explicit, prin codul `RS`; pentru zile de repaus planificate sau cumulate într-un calendar de ture, orele din program nu primesc sporul dublu (de confirmat juridic, decizia ÎCCJ HP nr. 415/2025);
    - compensarea orelor nu are evidență de sold: termenul de 90 de zile (art. 122) nu se urmărește, iar orele necompensate la expirare se pontează manual ca ore suplimentare plătite;
    - orele de noapte nu vin din prezențe, iar condiția de 3 ore nu se verifică;
    - clauza de mobilitate (art. 76 alin. (4^1), neimpozabilă, în D112) nu face parte din acest modul.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.salary.supplement`: nomenclatorul de sporuri, cu minimul legal impus pe procente. Câmpul `kind` are, pe lângă permanent, ore suplimentare și noapte, valorile `holiday` (sărbătoare legală, minim 100%) și `weekly_rest` (repaus săptămânal). Câmpul `multiplier` este folosit la `weekly_rest` (minim 2) și se aplică sporului de ore suplimentare.
- `l10n.ro.hr.supplement.line`: sporul permanent al unui angajat (procent sau sumă fixă, valabilitate).
- `hr.payslip` extins: calculul sporurilor permanente, de ore suplimentare, de noapte, de sărbătoare legală și de repaus săptămânal (pe baza tipurilor de prezență `L10N_RO_OT_HOL` și `L10N_RO_OT_REST`), tariful orar.

**Vizualizări**

- `views/l10n_ro_salary_supplement_views.xml`: lista, formularul și meniul nomenclatorului; în listă, repausul săptămânal afișează coloana *Multiplicator* în locul procentului (care e 0 pentru acest tip).
- `views/hr_employee_views.xml`: secțiunea *Sporuri permanente (RO)* pe fișa angajatului.
- `data/hr_salary_rule_data.xml`: regulile `SPORPERM`, `SPOR_ORE_SUPL`, `SPOR_NOAPTE`, `SPOR_SARBATOARE`, `SPOR_REPAUS` (categoria ALW).

**Acțiuni Automate / Acțiuni Server**

Nu are `ir.cron` sau acțiuni server. Nomenclatorul și intrarea `NIGHT_HOURS` vin din date (`noupdate` la nomenclator).

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): fluturașul, regulile și media indemnizației de concediu (art. 150).
- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): produce din pontaj tipurile de prezență (ore suplimentare, în sărbătoare legală, în repaus săptămânal, compensate cu timp liber) și codurile de pontaj `RS` și `OC`.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): sporurile intră în venitul brut și în bazele asiguratului.
- `l10n_ro_hr_payroll_account_enhancement`: nota contabilă a fluturașului (641 = 421).
