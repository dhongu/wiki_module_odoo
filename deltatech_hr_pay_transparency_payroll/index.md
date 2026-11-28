# Transparență Salarială - Salarizare (localizat la `deltatech_hr_pay_transparency_payroll/index.md`)

- **Nume Tehnic:** `deltatech_hr_pay_transparency_payroll`
- **Versiune:** `20.0.0.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_hr_pay_transparency_payroll
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_hr_pay_transparency_payroll`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul preia salariul pentru raportul de transparență salarială (Directiva UE 2023/970) din fluturașii validați din Odoo Payroll, în loc de salariul din contract. Directiva consideră remunerație salariul de bază și orice component complementar sau variabil, în numerar sau în natură; raportul de diferență salarială și răspunsurile la cererile de informare folosesc astfel ce a primit efectiv fiecare angajat. Primele rapoarte privind diferența salarială între femei și bărbați sunt scadente la 7 iunie 2027.

#### 2. Funcționalități Cheie

- Fiecare categorie de reguli salariale indică natura sumelor: *Basic pay*, *Complementary or variable*, *In kind* sau *Not pay* (totaluri, rețineri, contribuții angajator); coloana *Pay Transparency* apare în **Payroll → Configuration → Salary → Rule Categories**.
- O regulă salarială poate suprascrie categoria (setată sub *Categories*); o categorie fără valoare urmează categoria părinte.
- Categoriile generice sunt mapate la instalare: *Basic* ca salariu de bază, *Allowance* ca variabil, iar *Taxable Salary*, *Deduction*, *Net* și *Company Contribution* ca „not pay”; categoriile din localizare (prime, ore suplimentare, tichete de masă, beneficii în natură) se mapează manual.
- Orele plătite provin din zilele lucrate plătite din fluturași, deci salariul orar corespunde orelor efectiv plătite.
- Se iau în calcul doar fluturașii validați și plătiți din perioadă, inclusiv rambursările; angajații fără fluturași păstrează liniile de remunerație sau salariul din contract.
- Fluxul modulului de bază rămâne neschimbat: în **Employees → Pay Transparency → Pay Gap Reports** se apasă *Compute*, iar coloana *Source* din fila *Workers* arată *Payslips*, *Pay lines* sau *Contract wage*. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- [deltatech_hr_pay_transparency](../deltatech_hr_pay_transparency/index.md)
- `hr_payroll`

Se instalează automat (`auto_install`) când ambele dependențe sunt prezente.

#### 4. Componente Cheie

**Modele**

- `hr.salary.rule.category`: câmpul *Pay Transparency* (componenta de remunerație), cu moștenire de la părinte.
- `hr.salary.rule`: același câmp, care are prioritate față de categorie.
- `hr.employee`: extins pentru a calcula remunerația din fluturașii validați.

**Vizualizări**

- `views/hr_salary_rule_views.xml`: câmpul *Pay Transparency* pe regula salarială și coloana în lista categoriilor.

**Acțiuni Automate / Acțiuni Server**

- `data/hr_salary_rule_category_data.xml`: maparea inițială a categoriilor generice (date, nu cron).

#### 5. Conexiuni

- [deltatech_hr_pay_transparency](../deltatech_hr_pay_transparency/index.md): modulul de bază al cărui raport este alimentat din fluturași.
