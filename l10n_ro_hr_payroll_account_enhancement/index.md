# Romania - Contabilizare salarii, conturi implicite pe reguli (localizat la `l10n_ro_hr_payroll_account_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_hr_payroll_account_enhancement`
- **Versiune:** `19.0.1.5.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_payroll_account_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_payroll_account_enhancement`
- **Ultima Ingestie:** `2026-10-12`

> **Origine:** partea contabilă a fostului `l10n_ro_payroll_ro`, separată în 19.0.2.0.0 al modulului [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md), în linie cu perechea standard `l10n_ro_hr_payroll` / `l10n_ro_hr_payroll_account`.

#### 1. Sumar

Modulul completează salarizarea românească (`l10n_ro_hr_payroll_enhancement`) cu nota contabilă a statului de plată: pune conturile implicite pe regulile salariale, ca la validarea fluturașului să se genereze automat înregistrarea, fără configurare de mână. Nativul `l10n_ro_hr_payroll_account` trimite o mapare goală. Se instalează automat când sunt prezente ambele module dependente.

#### 2. Funcționalități Cheie

- **Conturi implicite pe reguli** (Debit = Credit): `GROSS` 641 = 421; `CAS` 421 = 43151; `CASS` 421 = 43161; `INCOMETAX` 421 = 4441; `CAM` 6461 = 4361 (646 dacă planul nu are 6461); `TICHETE` 6422 = 5328; popriri, cesiuni, pensie alimentară, `DEDUCTION` și `RETINERI` (sindicat, pensie facultativă reținută) 421 = 4271.
- **Completează doar golurile:** regulile care au deja conturi pe companie nu se suprascriu; se aplică la instalare și la încărcarea planului RO. Conturile lipsă din plan sunt sărite, cu avertisment în jurnal.
- **Căutarea contului:** întâi cod exact (fără zerouri de completare), apoi prefix; alternativele se scriu cu «|» (de ex. `6461|646`).
- **Concedii medicale** (19.0.1.1.0, din 19.0.1.2.0 direct pe regulile din [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)): `CM_FNUASS` Dr 4382 = Cr 423; `CAS_CM` / `CASS_CM` / `TAX_CM` Dr 423 = Cr 4315 / 4316 / 444; indemnizația angajatorului (`CM_FS`) rămâne în brut, 641 = 421. Planul RO are analitice pe 423 (4231), deci contul se caută pe familie.
- **CAS angajator pentru condiții deosebite / speciale** (19.0.1.5.0): regula `PENSION` (4% / 8%, art. 138 lit. b și c Cod fiscal) se înregistrează 6451 = 4311 (43111 în planul RO), nu pe 4315 și nici pe CAM. La actualizare se completează și companiile existente, doar dacă regula nu are conturi.
- **Beneficii suportate de angajator** (19.0.1.3.0): pensia facultativă 6456 = 4381 și pensia ocupațională 6458 = 4381, pe toată suma. Excedentul peste plafon e în brut doar ca bază pentru contribuții și impozit; `AVANTAJ_ANG_DED` îl stornează Dr 421 = Cr 641, ca cheltuiala să rămână o singură dată pe 645x. Asigurarea de sănătate suportată de angajator nu are notă pe fluturaș (se înregistrează din factura asigurătorului, 6457 = 4381).
- **Vouchere de vacanță și tichete cadou** (19.0.1.4.0): 6422 = 5328 pe toată valoarea; excedentul tichetelor cadou peste plafon e stornat Dr 421 = Cr 641 (`CADOU_IMP_DED`).
- **Impozit redirecționat** (3,5%, cu [l10n_ro_payroll_tax_redirect](../l10n_ro_payroll_tax_redirect/index.md)): Dr 4441 = Cr 462.
- **Grupare opțională:** cu opțiunea `batch_payroll_move_lines` (pe companie) se generează o singură notă pe stat, datată în ultima zi a lunii; liniile nu mai au partener.
- **Linii cu partener:** liniile contului 421 au ca partener angajatul (`employee_move_line`), ca plata salariilor să se poată reconcilia pe angajat.
- **Cifre de control** dintr-un stat de plată de referință, 09/2026 (testul TC-15; TC-17 pentru `PENSION`): 641 = 421 19.325; 421 Dr 7.333; 43151 4.781; 43161 2.003; 4441 549; 6422 / 5328 900; CAM 432. Monografia verificată de Pacioli (OMFP 1802/2014).

> **Limite cunoscute:** plata netului, avansurile, achiziția tichetelor (Dr 5328 = Cr 401) și `UNEMPDISABLED` (vărsământul L448/2006, dezactivat pe fluturaș) nu sunt mapate contabil; impozitul scutit (art. 60), suma neimpozabilă, deducerile și `COSTANG` nu se înregistrează; CAM rotunjit la leu pe angajat poate diferi cu câțiva lei de CAM-ul pe total din D112.

#### 3. Dependențe

- `l10n_ro_hr_payroll_enhancement`
- `l10n_ro_hr_payroll_account`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): `_configure_payroll_account_ro` completează conturile pe reguli (`PAYROLL_RULES`, `PAYROLL_ACCOUNTS` în `models/account_chart_template.py`); `_l10n_ro_payroll_account` caută contul.

**Reguli salariale**

`data/hr_salary_rule_data.xml` setează `employee_move_line` pe `GROSS`, `CAS`, `CASS`, `INCOMETAX`, `RETINERI`, popriri, cesiuni, pensie alimentară, `DEDUCTION`, regulile de stornare a excedentelor (`AVANTAJ_ANG_DED`, `CADOU_IMP_DED`) și regulile de concediu medical, și apelează `_load_payroll_accounts` pentru companiile RO existente.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): regulile salariale și parametrii pe care le mapează.
- [l10n_ro_payroll_tax_redirect](../l10n_ro_payroll_tax_redirect/index.md): regula de impozit redirecționat (3,5%), mapată Dr 4441 = Cr 462.
- `l10n_ro_hr_payroll_account`: integrarea contabilă standard (jurnal, notă contabilă la validare).
