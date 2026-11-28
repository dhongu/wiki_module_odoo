# Romania - Diurna în fluturaș

- **Nume Tehnic:** `l10n_ro_expense_allowance_payroll`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_expense_allowance_payroll
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_expense_allowance_payroll`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul duce diurna din decontul de cheltuieli în salarizare: partea de peste plafon devine venit din salarii în fluturașul lunii, iar partea neimpozabilă se declară în D112. Se instalează singur când sunt prezente cele trei module de care depinde.

#### 2. Funcționalități Cheie

- **Plafonul neimpozabil** (Cod fiscal, art. 76 alin. (2) lit. k)) este cel mai mic dintre 2,5 × nivelul legal × zile (23 lei/zi la deplasările interne, deci 57,50 lei/zi) și 3 salarii de bază pe lună, calculate pe zilele de deplasare; surplusul este venit asimilat salariilor.
- **Decontul conține doar partea din plafon**: «Total diurnă», totalul și diferența de plată către angajat; la finalizare (Avans → Validează) cele două părți se memorează; un decont invalidat își șterge memorarea.
- **Fluturașul** preia diurna impozabilă în brut (linia *Diurnă (surplus impozabil)*, cu CAS, CASS, CAM, impozit, recalcularea deducerii personale; contabil 641 = 421) și arată diurna neimpozabilă ca linie informativă, în afara brutului și a netului.
- Opțiunea de companie **Diurnă impozabilă ca sumă netă**: surplusul ajunge net la salariat, brutul fiind calculat prin mecanismul primelor în net.
- **D112**: diurna neimpozabilă merge la rândul 8.4.3 (`E3_62`) și în totalul veniturilor neimpozabile (`E3_69`), fără a intra în bazele de contribuții.
- Limite: plafonul de 3 salarii nu se aplică deplasărilor externe; sărbătorile legale se scad doar dacă sunt în calendarul de lucru; deconturile finalizate înainte de instalare nu se preiau; avansurile de trezorerie deja date se regularizează manual. Meniu decont: **Contabilitate → Furnizori → Decont Cheltuieli**; fluxul complet este în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md)
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md)
- `l10n_ro_hr_payroll_enhancement`

#### 4. Componente Cheie

**Modele**

- `deltatech.expenses.deduction`: extins cu împărțirea diurnei în parte neimpozabilă și impozabilă.
- `hr.payslip`: preia diurna în fluturaș.
- `l10n.ro.d112`: raportează diurna neimpozabilă în D112.
- `res.company`, `res.config.settings`: opțiunea „Diurnă impozabilă ca sumă netă”.

**Vizualizări**

- `view_deltatech_expenses_deduction_diem_payroll_form`: informațiile despre diurnă pe decont.
- `res_config_settings_view_form_diem_payroll`: setările modulului.

**Acțiuni Automate / Acțiuni Server**

- Nu are; regulile salariale se încarcă din `data/hr_salary_rule_data.xml`.

#### 5. Conexiuni

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md): decontul de cheltuieli al cărui rezultat este dus în salarizare.
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): declarația D112 în care se raportează diurna neimpozabilă.
