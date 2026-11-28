# Romania - Contabilizare salarii (conturi implicite pe reguli)

- **Nume Tehnic:** `l10n_ro_hr_payroll_account_enhancement`
- **Versiune:** `20.0.1.8.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_hr_payroll_account_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_payroll_account_enhancement`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Completează salarizarea românească cu nota contabilă a statului de plată: pune conturile implicite pe regulile salariale, astfel încât la validarea fluturașului să se genereze automat înregistrarea contabilă, fără configurare de mână. Se instalează automat când sunt prezente [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md) și `l10n_ro_hr_payroll_account`.

#### 2. Funcționalități Cheie

- Monografia salarizării, verificată conform OMFP 1802/2014: Dr 641 = Cr 421 (brut); Dr 421 = Cr 43151 / 43161 / 4441 (CAS, CASS, impozit pe salarii); Dr 6461 = Cr 4361 (CAM, 646 dacă planul nu are 6461); Dr 6422 = Cr 5328 (tichete de masă); Dr 6451 = Cr 4311 (CAS angajator pentru condiții deosebite sau speciale).
- Rețineri în favoarea terților (popriri, cesiuni, pensie alimentară, sindicat, pensie facultativă): Dr 421 = Cr 4271.
- Linia contului 421 are ca partener angajatul, deci plata salariilor se reconciliază pe angajat. Cu opțiunea de grupare a liniilor pe companie (`batch_payroll_move_lines`) se obține o singură notă pe stat, iar liniile nu mai au partener.
- Conturile se completează doar la regulile fără conturi, la instalare și la încărcarea planului RO; configurările manuale nu se suprascriu. Contul se caută întâi după cod exact, apoi după prefix; dacă lipsește din plan, regula rămâne nemapată și jurnalul afișează un avertisment. Maparea se verifică în Stat de plată → Configurare → Salariu → Reguli → fila Contabilitate.
- Nota se generează în jurnalul Salarii, datată în ultima zi a lunii, și se verifică în Contabilitate → Note contabile.
- Beneficii suportate de angajator (art. 76 alin. 4^1): pensiile (6456 / 6458 = 4381) și primele de asigurare de sănătate (6457 = 4381) se înregistrează din fluturaș; factura furnizorului se închide pe 4381 = 401, nu din nou pe cheltuială. Beneficiile în natură nu au cont în fluturaș.
- Rulajul debitor al lui 641 diferă de brutul din D112 cu avantajele impozabile neplătite în bani (sunt doar bază de calcul).
- Nemapate: vărsământul Legea 448/2006, avansul chenzinal, plata netului și a obligațiilor către buget, achiziția tichetelor.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- `l10n_ro_hr_payroll_account`

#### 4. Componente Cheie

**Modele**

- `hr.payslip`: extins pentru nota contabilă, cu partener pe linia 421.
- `account.chart.template`: completează conturile implicite pe regulile salariale la încărcarea planului RO.

**Vizualizări**

- Fără vizualizări proprii; maparea se vede pe regulile salariale (fila Contabilitate).

**Acțiuni Automate / Acțiuni Server**

- `data/hr_salary_rule_data.xml`: completează conturile pe reguli (GROSS, CAS, CASS, INCOMETAX, CAM, PENSION, TICHETE, popriri).

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): regulile salariale și fluturașul pe care se ridică nota contabilă.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația D112, cu al cărei brut se reconciliază contul 641.
