# Romania - Redirecționarea a 3,5% din impozit (localizat la `l10n_ro_payroll_tax_redirect/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_tax_redirect`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_tax_redirect
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_tax_redirect`
- **Ultima Ingestie:** `2026-10-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Evidența redirecționării de până la 3,5% din impozitul pe salarii, cerută de salariat angajatorului, cu calculul lunar, nota contabilă și declararea în D112 (Codul fiscal, art. 78 alin. (6) și art. 123^1). Calea prin angajator exclude declarația D230 pe aceeași perioadă.

#### 2. Funcționalități Cheie

- **Evidență pe angajat** (*Stat de plată → Angajați → Redirecționare 3,5% din impozit*): entitate nonprofit (denumire, CIF) sau bursă privată (CNP, număr și dată de contract), cotă și perioadă; cota totală ≤ 3,5%, cel mult 2 ani fiscali, un singur beneficiar nonprofit și o bursă pe perioadă.
- **Fluturaș:** linia informativă *Impozit redirecționat către beneficiari*, în afara netului; suma = `ROUND(impozit × cotă / 100)`, fără să depășească rotunjirea totalului. Nota: Dr 4441 = Cr 462 (cu `l10n_ro_hr_payroll_account_enhancement`).
- **D112:** suma intră în `A_deductibil` și `angajatorF1` (impozitul de plată scade), iar pe asigurat apar `Tcota_E4`, `Tsuma_E4` și `asiguratE4`.
- **Limite:**
    - schema ANAF permite un singur `asiguratE4` pe asigurat, cu cota entității 1 sau 2 (întreg), deci un angajat are cel mult o entitate și o bursă, iar bursa nu se declară fără entitate;
    - plata către beneficiari (Dr 462 = Cr 5121) și verificarea în registrul entităților sunt manuale;
    - de confirmat dacă atributul `cota` din XSD este procent sau cod;
    - condițiile bursei (contract în 30 de zile, justificative lunare) nu sunt verificate de modul;
    - regulile au fost verificate pe XSD, nu cu DUKIntegrator.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- `l10n_ro_anaf_d112_payroll`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.tax.redirect`: beneficiarul, cota și perioada, cu restricțiile de mai sus și alocarea `_allocate`.
- `l10n.ro.d112.employee.redirect`: redirecționările preluate pe linia de angajat din D112.
- `hr.payslip` extins: `_l10n_ro_tax_redirect_amount` pentru regula salarială.

**Vizualizări**

- `views/l10n_ro_hr_tax_redirect_views.xml`: lista, formularul și meniul.
- `data/hr_salary_rule_data.xml`: categoria `REDIRECT` și regula (secvența 195).

**Acțiuni Automate / Acțiuni Server**

Nu are `ir.cron` sau acțiuni server. Modul `auto_install`.

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): punctele de extensie `_d112_redirect_total`, `_d112_asigurat_redirects`, `_d112_asigurat_redirect_elements`.
- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): fluturașul și categoria de reguli.
- `l10n_ro_hr_payroll_account_enhancement`: contul 462 și nota contabilă.
