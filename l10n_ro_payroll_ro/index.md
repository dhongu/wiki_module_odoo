# Romania - Impozit pe salarii, deduceri personale și tichete de masă (localizat la `l10n_ro_payroll_ro/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_ro`
- **Versiune:** `19.0.1.1.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_ro
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_ro`
- **Ultima Ingestie:** `2026-10-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează statul de plată românesc, peste structura nativă Odoo 19 Enterprise (`l10n_ro_hr_payroll`), cu regulile fiscale care lipsesc în nativ. Regula nativă `INCOMETAX` calculează impozitul ca 10% din salariul brut, ceea ce este greșit fiscal: impozitul se aplică pe baza redusă (brut + tichete − suma neimpozabilă − CAS − CASS − deduceri personale). Modulul adaugă deducerea personală de bază pe grila oficială, deducerile suplimentare (copii, tineri), suma neimpozabilă la salariul minim, tichetele de masă și scutirile de impozit, toate cu parametri versionați pe dată. Rezultatul este un net și un impozit corecte pe fluturaș, transferate în D112 prin puntea `l10n_ro_anaf_d112_payroll`.

#### 2. Funcționalități Cheie

- **Deducerea personală de bază (DPB)** pe grila art. 77 Cod fiscal: procentul la salariul minim după numărul de persoane în întreținere (20/25/30/35/45%), scăzut cu 0,5 puncte procentuale pentru fiecare tranșă începută de 50 lei peste salariul minim; peste salariul minim + 2.000 lei nu se acordă. Grila se raportează mereu la salariul minim general (S1) și se citește la venitul rotunjit la leu, inclusiv tichetele.
- **Salariul minim cu istoric** în parametri versionați (4.050 lei până la 30.06.2026, 4.325 lei din 01.07.2026); actualizarea cere o valoare nouă cu dată de început, nu modificări de cod.
- **Persoane în întreținere** (model `l10n.ro.hr.dependent`): relație, nume, CNP, perioadă de întreținere, bifa «Școală»; **100 lei/lună** pentru fiecare copil sub 18 ani înscris în învățământ, fără condiție de venit.
- **Deducere pentru tineri**: 15% din salariul minim, doar sub 26 de ani la sfârșitul lunii fluturașului (vârsta din «Data nașterii», altfel din CNP, cu avertisment dacă diferă) și doar în plafonul de venit.
- **Funcție de bază**: fără bifă nu se acordă nicio deducere personală și nici suma neimpozabilă.
- **Suma neimpozabilă la salariul minim**: 300 lei (ian.–iun. 2026), 200 lei din 01.07.2026, plafonată la 33% din salariul de bază; doar când salariul de bază din contract nu depășește salariul minim, cu normă întreagă, proratată cu zilele lucrate și cu partea din lună în care contractul e activ. Scade din baza CAS, CASS, CAM și impozit. *De confirmat cu contabilul:* textul OUG 89/2025 și OUG 8/2026, pragul de venit (parametru opțional `suma_neimpozabila_prag_venit`, nesetat).
- **Tichete de masă**: număr pe fluturaș (implicit zilele lucrate fără concedii, modificabil) × valoare nominală cu dată de început; intră în CASS și în venitul pentru deducere, nu în CAS, CAM sau netul în bani; rând «Cost angajator» (brut + CAM + tichete).
- **Scutire de impozit pe venit** (art. 60): handicap grav sau accentuat și cercetare-dezvoltare (aceasta din urmă doar pentru fluturașul separat al proiectului); se transferă în D112 (`asigScu` 1/3, `E3_23`/`E3_24` sau `E3_27`/`E3_28`, obligația 602, `angajatorF1`); contribuțiile se calculează normal.
- **Fluturașul tipărit (PDF)**: raportul «România» al structurii arată linia «Tichete de masă» cu numărul de tichete și valoarea nominală; rata tehnică ±100% a contribuțiilor rotunjite nu se mai afișează (`report_payslip_ro_clean`).
- **Rotunjire**: CAS, CASS și CAM la leu; baza impozabilă la leu cu 0,50 în jos (HG 1/2016), apoi cota de 10%.
- **Exemplu verificat** (brut 4.325, 1 persoană, 20 tichete × 45 lei): CAS 1.031, CASS 503, DPB 692, impozit 280, net 2.511, cost angajator 5.318.

> **Limite cunoscute:** conturile contabile nu sunt mapate pe regulile salariale (validarea fluturașului nu generează nota); cotizația sindicală și pensiile facultative nu scad din baza impozabilă. Scutirea art. 60 și deducerile se transferă în D112 prin puntea `l10n_ro_anaf_d112_payroll` (declarate ca în SAGA). Facilitățile sectoriale (IT, construcții, agro) sunt abrogate din 01.01.2025 și nu sunt incluse.

#### 3. Dependențe

- `l10n_ro_hr_payroll`
- `l10n_ro_hr_payroll_account`

#### 4. Componente Cheie

**Modele**

- `hr.version` (extins): câmpurile `l10n_ro_dependent_persons`, `l10n_ro_min_wage_tier` (informativ), `l10n_ro_basic_function`, `l10n_ro_young_deduction`, `l10n_ro_tax_exempt_reason`, `l10n_ro_meal_tickets` și avertismentul pentru data nașterii.
- `l10n.ro.hr.dependent` (nou): persoanele în întreținere ale angajatului, cu CNP, perioadă și bifa «Școală».
- `hr.employee` (extins): legătura `l10n_ro_dependent_ids` către persoanele în întreținere.
- `hr.payslip` (extins): numărul de tichete și metodele de calcul apelate de regulile salariale (`_l10n_ro_dpb_breakdown`, `_l10n_ro_non_taxable_amount`, `_l10n_ro_meal_ticket_value`, rotunjirile).
- Parametri salariali (`hr.rule.parameter`, cod `l10n_ro_salary_params`): cote, salariul minim, procentele grilei, deducerile, valoarea tichetului, suma neimpozabilă — două valori, de la 01.01.2026 și 01.07.2026.

**Vizualizări**

- `view_hr_employee_form_l10n_ro_dpb`: pe fila *Stat de plată* a angajatului, grupul «Salarizare România» pe două coloane (funcție de bază, persoane în întreținere, sub 26 de ani | tichete, scutire, tip salariu minim) și un grup separat, pe toată lățimea, cu lista persoanelor în întreținere.
- `view_hr_contract_template_form_l10n_ro_dpb`: aceleași câmpuri RO în două grupuri pe formularul versiunii de contract (fără lista de persoane, care aparține angajatului).
- `view_hr_payslip_form_l10n_ro_meal_tickets`: numărul de tichete pe fluturaș.
- `report_payslip_ro_clean`: șablonul fluturașului tipărit, fără rata ±100%.

**Reguli salariale**

Reguli noi: `NEIMPOZ`, `TICHETE`, `DPB`, `DPBTIN`, `DPBCOP`, `COSTANG`; reguli native suprascrise: `CAS`, `CASS`, `CAM`, `INCOMETAX`.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; regulile salariale rulează în motorul standard de calcul al fluturașului (`data/hr_salary_rule_data.xml`).

#### 5. Conexiuni

- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): puntea care transferă în D112 tichetele, suma neimpozabilă, deducerile și bazele CAS/CASS din regulile acestui modul.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația D112; are propria formulă liniară de deducere, nealiniată cu grila pe tranșe (pentru liniile cu calcul automat).
- `l10n_ro_hr_payroll`: furnizează structura salarială de bază pentru Romania (regulile GROSS,
  CAS, CASS, INCOMETAX native) peste care acest modul aplică corecțiile fiscale.
- `l10n_ro_hr_payroll_account`: integrarea contabilă a statului de plată RO, dependență directă
  a modulului.
