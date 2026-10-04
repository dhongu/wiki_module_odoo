# Romania - Contabilizare salarii, conturi implicite pe reguli (localizat la `l10n_ro_hr_payroll_account_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_hr_payroll_account_enhancement`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_payroll_account_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_payroll_account_enhancement`
- **Ultima Ingestie:** `2026-10-03`

> **Origine:** partea contabilă a fostului `l10n_ro_payroll_ro`, separată în 19.0.2.0.0 al modulului [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md), în linie cu perechea standard `l10n_ro_hr_payroll` / `l10n_ro_hr_payroll_account`.

#### 1. Sumar

Modulul completează salarizarea românească (`l10n_ro_hr_payroll_enhancement`) cu nota contabilă a statului de plată: pune conturile implicite pe regulile salariale, ca la validarea fluturașului să se genereze automat înregistrarea, fără configurare de mână. Nativul `l10n_ro_hr_payroll_account` trimite o mapare goală. Se instalează automat când sunt prezente ambele module dependente.

#### 2. Funcționalități Cheie

- **Conturi implicite pe reguli** (Debit = Credit): `GROSS` 641 = 421; `CAS` 421 = 43151; `CASS` 421 = 43161; `INCOMETAX` 421 = 4441; `CAM` 6461 = 4361 (646 dacă planul nu are 6461); `TICHETE` 6422 = 5328; popriri, cesiuni, pensie alimentară, `DEDUCTION` și `RETINERI` (sindicat, pensie facultativă reținută) 421 = 4271.
- **Completează doar golurile:** regulile care au deja conturi pe companie nu se suprascriu; se aplică la instalare și la încărcarea planului RO. Conturile lipsă din plan sunt sărite, cu avertisment în jurnal.
- **Căutarea contului:** întâi cod exact (fără zerouri de completare), apoi prefix; alternativele se scriu cu «|» (de ex. `6461|646`).
- **Concedii medicale** (19.0.1.1.0, din 19.0.1.2.0 direct pe regulile din [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)): `CM_FNUASS` Dr 4382 = Cr 423; `CAS_CM` / `CASS_CM` / `TAX_CM` Dr 423 = Cr 4315 / 4316 / 444; indemnizația angajatorului (`CM_FS`) rămâne în brut, 641 = 421. Planul RO are analitice pe 423 (4231), deci contul se caută pe familie.
- **Linii cu partener:** liniile contului 421 au ca partener angajatul (`employee_move_line`), ca plata salariilor să se poată reconcilia pe angajat.
- **Cifre de control** dintr-un stat de plată de referință, 09/2026 (testul TC-15): 641 = 421 19.325; 421 Dr 7.333; 43151 4.781; 43161 2.003; 4441 549; 6422 / 5328 900; CAM 432. Monografia verificată de Pacioli (OMFP 1802/2014).

> **Limite cunoscute:** plata netului, avansurile, achiziția tichetelor (Dr 5328 = Cr 401), `PENSION` și `UNEMPDISABLED` nu sunt mapate contabil; CAM rotunjit la leu pe angajat poate diferi cu câțiva lei de CAM-ul pe total din D112.

#### 3. Dependențe

- `l10n_ro_hr_payroll_enhancement`
- `l10n_ro_hr_payroll_account`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): `_configure_payroll_account_ro` completează conturile pe reguli (`PAYROLL_RULES`, `PAYROLL_ACCOUNTS` în `models/account_chart_template.py`); `_l10n_ro_payroll_account` caută contul.

**Reguli salariale**

`data/hr_salary_rule_data.xml` setează `employee_move_line` pe `GROSS`, `CAS`, `CASS`, `INCOMETAX`, `RETINERI`, popriri, cesiuni, pensie alimentară și `DEDUCTION`, și apelează `_load_payroll_accounts` pentru companiile RO existente.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): regulile salariale și parametrii pe care le mapează.
- `l10n_ro_hr_payroll_account`: integrarea contabilă standard (jurnal, notă contabilă la validare).
