# Romania - Pontaj în salarizare

- **Nume Tehnic:** `l10n_ro_hr_pontaj_payroll`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_hr_pontaj_payroll
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_pontaj_payroll`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Duce corecțiile din foaia colectivă de prezență în salarizarea Odoo, pe drumul standard al prezențelor (work entries). Fluturașul și declarația D112 primesc astfel zilele lucrate, de concediu și de absență exact așa cum au fost pontate. Se instalează explicit, nu automat, pentru că schimbă prezențele fluturașelor.

#### 2. Funcționalități Cheie

- O zi corectată în pontaj cu un cod de concediu sau absență devine o prezență de tipul codului; prezențele generate de program, sărbători și concedii pentru acea zi sunt înlocuite.
- Zi lucrată cu alte ore decât programul: mai puține ore înseamnă ore lucrate plus diferența ca absență nemotivată (`N`); mai multe ore înseamnă orele programului plus surplusul pe tipul de ore suplimentare (`040.00`).
- Zi de repaus sau sărbătoare legală: orele merg ca ore suplimentare, sărbătoarea rămâne plătită; în sărbătoare legală se folosește tipul `L10N_RO_OT_HOL`.
- Coduri noi de tip lucrat: `RS` (repaus săptămânal suspendat sau cumulat, tip `L10N_RO_OT_REST`, dublul sporului) și `OC` (ore compensate cu timp liber, tip `L10N_RO_OT_COMP`, neplătite în luna lucrată; ziua liberă se pontează cu `REC`). Câmpul Tip ore suplimentare al codului stabilește tipul orelor peste program.
- În Odoo 20 prezențele se calculează la crearea zilelor lucrate de pe fluturaș: o corecție se vede pe fluturașul creat după ea sau, pe unul în ciornă, după Reset; fluturașul validat nu se mai schimbă. Ștergerea corecției readuce ziua la program.
- Tipurile plătite (delegație, evenimente familiale, șomaj tehnic) intră în salariul de bază; absențele nemotivate, maternitatea și creșterea copilului au tariful 0. D112 preia zilele lucrate, de concediu de odihnă și medical.
- Tichetele de masă au o singură valoare, din salarizare: exportul pentru bancă din pontaj ia valoarea din contractul valabil în ultima zi a lunii, altfel din companie.
- Spor pentru orele suplimentare aduce `l10n_ro_payroll_allowances`; pentru zilele cu ore suplimentare în repaus, verificați plata cu contabilul (Decizia ÎCCJ HP 415/2025).
- Fluxul pas cu pas stă în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md)
- `hr_payroll`
- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.pontaj.code`: extins cu tipul orelor suplimentare și cu codurile `RS` și `OC`.
- `hr.version`: extins pentru valoarea tichetului de masă pe contract.
- `l10n.ro.hr.meal.voucher.export`: extins pentru valoarea tichetului din salarizare.

**Vizualizări**

- Vizualizările codurilor de pontaj (câmpul Tip ore suplimentare) și formularul angajatului (`hr_employee_views`).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: configurează la instalare tipurile de prezență și clasificarea codurilor; nu există cron.

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md) și [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): D112 preia zilele din prezențe.
- `l10n_ro_payroll_allowances`: sporul pentru orele suplimentare.
