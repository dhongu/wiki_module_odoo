# Romania - Redirecționarea a 3,5% din impozit (`l10n_ro_payroll_tax_redirect`)

- **Nume Tehnic:** `l10n_ro_payroll_tax_redirect`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_tax_redirect
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_tax_redirect`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Evidența redirecționării de până la 3,5% din impozitul pe salarii, cerută de salariat angajatorului, cu calculul lunar, nota contabilă și declararea în D112. Baza legală: Codul fiscal, art. 78 alin. (6) și art. 123^1 alin. (6)–(7); beneficiari pot fi entități nonprofit, unități de cult sau burse private, pe cel mult 2 ani fiscali consecutivi.

#### 2. Funcționalități Cheie

- Evidența cererilor pe angajat (*Stat de plată → Angajați → Redirecționare 3,5% din impozit*): beneficiar (entitate nonprofit cu CIF sau bursă privată cu CNP, număr și dată de contract), cotă și perioadă.
- Validări: cota totală cel mult 3,5%; o entitate nonprofit și o bursă privată per angajat în aceeași perioadă; cota entității 1 sau 2; bursa se declară numai împreună cu o entitate.
- Linia informativă *Impozit redirecționat către beneficiari* pe fluturaș, în afara netului: `ROUND(impozit × cotă / 100)`.
- Nota contabilă Dr 4441 = Cr 462 (cu `l10n_ro_hr_payroll_account_enhancement`).
- În D112, suma intră în `A_deductibil` și `angajatorF1`; pe asigurat apar `Tcota_E4`, `Tsuma_E4` și `asiguratE4`.
- Rămân manuale: plata către beneficiari (Dr 462 = Cr 5121), verificarea în registrul entităților nonprofit și păstrarea cererii. Flux detaliat în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.tax.redirect`: cererea de redirecționare (beneficiar, cotă, perioadă).
- `l10n.ro.d112.employee.redirect`: linia D112 `asiguratE4`.
- `hr.payslip`, `l10n.ro.d112`, `l10n.ro.d112.employee.line` (extinse): calculul pe fluturaș și transferul în declarație.

**Vizualizări**

- `view_l10n_ro_hr_tax_redirect_form` și `view_l10n_ro_hr_tax_redirect_list`: formularul și lista redirecționărilor.
- `action_l10n_ro_hr_tax_redirect`: acțiunea din meniu.

**Acțiuni Automate / Acțiuni Server**

- Fără cron. Datele definesc categoria `l10n_ro_tax_redirect_category` și regula salarială `l10n_ro_employee_salary_tax_redirect`.

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația D112 în care se raportează.
- `l10n_ro_hr_payroll_account_enhancement`: maparea contabilă 4441 / 462.
