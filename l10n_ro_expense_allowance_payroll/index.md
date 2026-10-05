# Romania - Diurna în fluturaș (localizat la `l10n_ro_expense_allowance_payroll/index.md`)

- **Nume Tehnic:** `l10n_ro_expense_allowance_payroll`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_expense_allowance_payroll
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_expense_allowance_payroll`
- **Ultima Ingestie:** `2026-10-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Duce diurna din decontul de cheltuieli în salarizare: partea de peste plafon devine venit din salarii în fluturașul lunii, iar partea neimpozabilă se declară în D112. Plafonul (Codul fiscal, art. 76 alin. (2) lit. k)) este cel mai mic dintre 2,5 × nivelul legal × zile (23 lei/zi la deplasările interne, deci 57,50 lei/zi) și 3 salarii de bază pe lună.

#### 2. Funcționalități Cheie

- **Decontul exclude partea impozabilă:** «Total diurnă», totalul decontului și diferența de plată conțin doar diurna în plafon (625 = 542); la finalizare (Avans → Validează) cele două părți se memorează, iar un decont invalidat își șterge memorarea.
- **Fluturașul lunii decontului** preia diurna impozabilă în brut (linia *Diurnă (surplus impozabil)*: intră în CAS, CASS, CAM și impozit; contabil 641 = 421) și arată diurna neimpozabilă ca linie informativă, în afara brutului și a netului.
- **Diurnă impozabilă ca sumă netă** (opțiune pe companie): surplusul ajunge net la salariat, cu mecanismul primelor în net din [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md).
- **D112:** diurna neimpozabilă merge la rândul 8.4.3 (`E3_62`) și în totalul veniturilor neimpozabile (`E3_69`), fără să intre în bazele de contribuții.
- **Limite:**
    - nivelul de 23 lei/zi și numărarea zilelor rămân de verificat pe legislatie.just.ro;
    - plafonul de 3 salarii nu se aplică deplasărilor externe (alte monede);
    - sărbătorile legale se scad din zilele lucrătoare doar dacă sunt în calendarul de lucru al companiei;
    - partea impozabilă nu se detaliază în D112 la `E3_52` / `E3_59` (coduri neconfirmate);
    - deconturile finalizate înainte de instalare nu se preiau, iar regularizarea unui avans de trezorerie se face manual.

#### 3. Dependențe

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md)
- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- `l10n_ro_anaf_d112_payroll`

#### 4. Componente Cheie

**Modele**

- Modelul de decont (`deltatech_expenses`) extins cu snapshot-ul diurnei neimpozabile / impozabile (`l10n_ro_diem_exempt`, `l10n_ro_diem_taxable`), memorat la `validate_expenses`; `_compute_amount` exclude partea impozabilă.
- `hr.payslip` și `l10n_ro_anaf_d112_payroll` extinse pentru preluarea diurnei în fluturaș și în D112 (`E3_62`, `E3_69`).

**Vizualizări**

- `views/deltatech_expenses_deduction_views.xml`: partea impozabilă / neimpozabilă pe decont.
- `views/res_config_settings_views.xml`: opțiunea *Diurnă impozabilă ca sumă netă*.

**Acțiuni Automate / Acțiuni Server**

Nu are `ir.cron` sau acțiuni server; regulile salariale `DIURNA_IMP` și `DIURNA_NEIMP` sunt în `data/hr_salary_rule_data.xml`.

#### 5. Conexiuni

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md): cuantumurile și calculul plafonului.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declararea diurnei neimpozabile.
- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): mecanismul primelor în net.
