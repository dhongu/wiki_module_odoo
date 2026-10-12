# Pay Transparency - Payroll (localizat la `deltatech_hr_pay_transparency_payroll/index.md`)

- **Nume Tehnic:** `deltatech_hr_pay_transparency_payroll`
- **Versiune:** `19.0.0.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_hr_pay_transparency_payroll
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_hr_pay_transparency_payroll`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul preia remunerația pentru raportul de transparență salarială (Directiva UE 2023/970) din fluturașii de salariu validați din Odoo Payroll, în locul salariului din contract. Raportul de diferențe salariale și răspunsurile la cererile de informare folosesc astfel ce a primit efectiv fiecare angajat: salariul de bază și toate componentele complementare sau variabile, în bani sau în natură. Modulul se instalează automat când sunt prezente ambele module de care depinde.

#### 2. Funcționalități Cheie

- Fiecare categorie de reguli salariale indică natura sumelor: **salariu de bază**, **complementar sau variabil**, **în natură** sau **nu este remunerație** (totaluri, rețineri, contribuții ale angajatorului).
- O regulă salarială poate suprascrie categoria sa; o categorie fără valoare urmează categoria părinte, iar în lipsa oricărei valori se consideră „nu este remunerație”.
- La instalare sunt mapate categoriile generice: *Basic* ca salariu de bază, *Allowance* ca variabil, iar *Gross* (Taxable Salary), *Deduction*, *Net* și *Company Contribution* ca nu este remunerație. Categoriile din localizare (prime, ore suplimentare, indemnizații, tichete de masă, beneficii în natură) se mapează manual.
- Orele plătite provin din zilele lucrate plătite din fluturași, deci salariul orar corespunde orelor efectiv plătite.
- Se iau în calcul doar fluturașii validați sau plătiți din perioadă, inclusiv ștornările (valori negative). Angajații fără fluturași în perioadă, ca și lunile neacoperite de fluturași, păstrează liniile de remunerație sau salariul din contract.
- Fluxul modulului de bază nu se schimbă: raportul sau răspunsul la cerere se calculează ca de obicei. În fila *Angajați* a raportului, coloana *Sursă* afișează *Fluturași* pentru angajații ale căror cifre provin din payroll.
- Configurare: **Payroll → Configurare → Categorii de reguli**, coloana *Pay Transparency*; opțional, câmpul și pe regula salarială.

#### 3. Dependențe

- [deltatech_hr_pay_transparency](../deltatech_hr_pay_transparency/index.md)
- `hr_payroll`

#### 4. Componente Cheie

**Modele**

- `hr.salary.rule.category` (extins): câmpul `pay_transparency_component` (base / variable / in_kind / excluded) și metoda `_get_pay_transparency_component`, cu moștenire pe lanțul de categorii părinte.
- `hr.salary.rule` (extins): același câmp, care are prioritate față de categorie.
- `hr.employee` (extins): `_pay_transparency_collect` completează datele modulului de bază cu sumele și orele din fluturașii validați/plătiți (`_pay_transparency_payroll_pay`), marcând sursa „payroll”.

**Vizualizări**

- `hr_salary_rule_form`: câmpul *Pay Transparency* pe regula salarială, după categorie.
- `hr_salary_rule_category_form`: câmpul pe formularul categoriei, după părinte.
- `hr_salary_rule_category_list`: coloană opțională în lista de categorii.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Datele `hr_salary_rule_category_data.xml` (noupdate) mapează categoriile generice `hr_payroll`.

#### 5. Conexiuni

- [deltatech_hr_pay_transparency](../deltatech_hr_pay_transparency/index.md): modulul de bază, al cărui raport și ale cărui răspunsuri folosesc datele din fluturași.
