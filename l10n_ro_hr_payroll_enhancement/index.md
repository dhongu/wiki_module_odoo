# Romania - Impozit pe salarii, deduceri personale și tichete de masă (localizat la `l10n_ro_hr_payroll_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_hr_payroll_enhancement`
- **Versiune:** `19.0.2.4.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_payroll_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_payroll_enhancement`
- **Ultima Ingestie:** `2026-10-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

> **Redenumit:** fostul `l10n_ro_payroll_ro` (până la 19.0.1.3.0); migrarea se face automat la instalare (`pre_init_hook`). Din 19.0.2.3.0 include și fostul `l10n_ro_payroll_leave` (migrare prin `migrations/19.0.2.3.0/pre-migration.py`).

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
- **Nota contabilă la validarea fluturașului** (S1) a trecut în modulul separat [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md) (instalat automat): conturile implicite pe regulile salariale, 641 = 421, 421 = 43151 / 43161 / 4441, 6461 = 4361, 6422 = 5328, 421 = 4271.
- **Rețineri deductibile din baza de impozit** (S2): tipuri de intrare `SINDICAT`, `PENSIE_FAC`, `PENSIE_FAC_RET`, `SANATATE_PRIV`, disponibile și în *Ajustări salariale*. Indicatori pe tip: deductibil din baza impozitului (art. 78 alin. 2 lit. a Cod fiscal), reținut din net (sindicat: da; pensie facultativă plătită direct și asigurare de sănătate: doar baza), plafon anual și grup de plafon. Regulile `DEDBAZA` (scade baza impozitului; deducerea personală rămâne din brut; doar la funcția de bază) și `RETINERI` (scade netul; 421 = 4271). Plafonul de 400 EUR/an se aplică pe cumul în euro, fiecare lună la cursul ei, pe grup (pensia plătită direct și cea reținută împart plafonul); fără curs EUR calculul se oprește cu eroare. Cifre de control 09/2026: brut 5.000, sindicat 50 + pensie 100 → bază 2.538, impozit 254, net 2.946. Verificat cu Pacioli.
- **Avertizări pe fluturaș** (S3), în mecanismul nativ: CNP lipsă sau invalid, perioadă de întreținere încheiată luna trecută, copil înscris în învățământ fără CNP valid (deducerea pentru copil nu se acordă). Nu blochează calculul. Nu există avertizarea «salariu minim după 2 ani» (fără temei legal în 2026) și nici «contract fără COR» (fără câmp COR).
- **Simulator brut ↔ net** (S4): *Salarizare → Raportare → Simulator brut / net (RO)*; brut → net și net → brut (cel mai mic brut întreg care atinge netul, cu o fereastră de 60 de lei pentru treptele deducerii), cu sau fără angajat ales, fără urme în bază (savepoint anulat), cu PDF. Rulează structura salarială a fluturașului, deci cifrele coincid cu ale statului de plată.
- **Concedii medicale** (unite din fostul `l10n_ro_payroll_leave` în 19.0.2.3.0; OUG 158/2005 și structura D112):
    - **Certificat unic** (`l10n.ro.medical.certificate`): serie și număr (`D_1`/`D_2`), perioada (`D_6`/`D_7`), data eliberării (`D_5`), codul de indemnizație (`D_9`), locul prescrierii (`D_10`), `D_11`/`D_12`/`D_23`, bifele *Spitalizat* și *Program național*, CNP copil; la confirmare creează concediul medical din *Concedii*, iar zilele ies din salariu.
    - **Nomenclator `D_9`** (`l10n.ro.medical.code`): codurile 01–17 și 51 cu grupa, procentul (55 / 65 / 75% după durata certificatului la codul 01; procente fixe la celelalte), regula zilelor angajatorului, ziua neplătită, CASS și impozit pe cod. Codurile 10 și 11 nu sunt calculate.
    - **Zile:** zilele lucrătoare din perioadă (calendarul angajatului, sărbători excluse); primele 5 ale angajatorului, restul din FNUASS; **prima zi neplătită** pentru certificatele din 01.02.2026–31.12.2027 (OUG 91/2025), cu excepțiile din Legea 64/2026 și fără ea la codul 51.
    - **Baza** (art. 10): media zilnică a veniturilor din cele mai recente 6 luni cu venit din ultimele 12, plafonate lunar la 12 salarii minime, cu indemnizațiile și zilele de concediu medical incluse; automată sau manuală (adeverință de la alt angajator). Indemnizația = media × zilele plătite × procentul, rotunjită la leu.
    - **Continuări:** câmpul *Continuă* leagă certificatele aceluiași episod (`D_3`/`D_4`/`Data_CMI` din primul); procentul pe zilele cumulate ale episodului (cod 01), cele 5 zile ale angajatorului pe episod, ziua neplătită doar la primul certificat; de la 01.07.2026 recalcul retroactiv: suma lunii = cuvenitul cumulat − plătit efectiv în lunile anterioare (din fluturașii validați), cu partea retroactivă identificată (`D_20a`/`D_21a`).
    - **Pe fluturaș:** `CM_FS` (în brut, cu CAS, CASS după cod, impozit și CAM), `CM_FNUASS` (categoria `CMFN`: în afara brutului și a bazei CAM, dar în venitul impozabil și în net), `CAS_CM`, `CASS_CM` (doar codurile 01, 07, 10) și `TAX_CM` (impozitul alocat proporțional părții din FNUASS). Contabil, cu [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md): 4382 = 423 pentru FNUASS, contribuțiile aferente pe 423; indemnizația angajatorului rămâne în brut (641 = 421).
    - **D112:** `hr.payslip._l10n_ro_d112_medical_leaves()` furnizează secțiunile D pentru luna fluturașului (zile angajator / FNUASS, ziua neplătită, baza, procentul, indemnizațiile și diferențele retroactive).
    - **Exemplu verificat** (14–23.09.2026, brut 5.000, media 238,10, 65%): indemnizații 619 (angajator) și 464 (FNUASS), salariu 3.181,82, CAS 950 + 116, CASS 380 + 46, impozit 191 (21 pe FNUASS), 423 net 281.
- **Rotunjire**: CAS, CASS și CAM la leu; baza impozabilă la leu cu 0,50 în jos (HG 1/2016), apoi cota de 10%.
- **Exemplu verificat** (brut 4.325, 1 persoană, 20 tichete × 45 lei): CAS 1.031, CASS 503, DPB 692, impozit 280, net 2.511, cost angajator 5.318.

> **Limite cunoscute:** plata netului, avansurile, achiziția tichetelor, `PENSION` și `UNEMPDISABLED` nu sunt încă mapate contabil; CAM rotunjit la leu pe angajat poate diferi cu câțiva lei de CAM-ul pe total din D112; lipsesc pensiile ocupaționale, PEPP, ETF și abonamentele sportive (OUG 8/2026), deducerile angajatorului anterior și limita cotizației sindicale (Legea 367/2022) e de verificat. Scutirea art. 60 și deducerile se transferă în D112 prin puntea `l10n_ro_anaf_d112_payroll` (declarate). Facilitățile sectoriale (IT, construcții, agro) sunt abrogate din 01.01.2025 și nu sunt incluse.
>
> **Concedii medicale, limite:** D112 declară certificatele pe GrupB prin [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md) (codurile neimpozabile 08, 09, 91, 92, 15, 17 au venitul și impozitul manuale; perioada unui certificat se limitează la luna raportată); lipsesc rapoartele. De confirmat: zilele angajatorului urmează convenția D112 (4 plătite), nu literal OUG 91/2025 (zilele 2–6); partea angajatorului 641 = 421 (funcțiunea OMFP ar fi 6458 = 423); excepția pentru codul 51, Legea 64/2026 și procentul la codurile 02–04; plățile anterioare se iau din toți fluturașii validați din lunile episodului.

#### 3. Dependențe

- `l10n_ro_hr_payroll`

#### 4. Componente Cheie

**Modele**

- `hr.version` (extins): câmpurile `l10n_ro_dependent_persons`, `l10n_ro_min_wage_tier` (informativ), `l10n_ro_basic_function`, `l10n_ro_young_deduction`, `l10n_ro_tax_exempt_reason`, `l10n_ro_meal_tickets` și avertismentul pentru data nașterii.
- `l10n.ro.hr.dependent` (nou): persoanele în întreținere ale angajatului, cu CNP, perioadă și bifa «Școală».
- `hr.employee` (extins): legătura `l10n_ro_dependent_ids` către persoanele în întreținere.
- `l10n.ro.payroll.simulator` (wizard, `wizard/`): simulatorul brut ↔ net, cu liniile de rezultat `l10n.ro.payroll.simulator.line` și raportul PDF «Simulare salariu».
- `l10n.ro.medical.certificate` (nou): certificatul de concediu medical, cu zilele, procentul, baza și sumele (`_episode_schedule`, `_entitlement`, `_episode_window_amounts`, `_auto_base`).
- `l10n.ro.medical.code` (nou): nomenclatorul `D_9`.
- `hr.payslip.input.type` (extins): indicatorii `l10n_ro_tax_deductible`, `l10n_ro_withheld`, `l10n_ro_annual_cap`, `l10n_ro_cap_group`.
- `hr.payslip` (extins): numărul de tichete și metodele de calcul apelate de regulile salariale (`_l10n_ro_dpb_breakdown`, `_l10n_ro_non_taxable_amount`, `_l10n_ro_meal_ticket_value`, rotunjirile).
- Parametri salariali (`hr.rule.parameter`, cod `l10n_ro_salary_params`): cote, salariul minim, procentele grilei, deducerile, valoarea tichetului, suma neimpozabilă — două valori, de la 01.01.2026 și 01.07.2026.

- Maparea conturilor pe reguli (`account.chart.template`) e în [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md).

**Vizualizări**

- `view_hr_employee_form_l10n_ro_dpb`: pe fila *Stat de plată* a angajatului, grupul «Salarizare România» pe două coloane (funcție de bază, persoane în întreținere, sub 26 de ani | tichete, scutire, tip salariu minim) și un grup separat, pe toată lățimea, cu lista persoanelor în întreținere.
- `view_hr_contract_template_form_l10n_ro_dpb`: aceleași câmpuri RO în două grupuri pe formularul versiunii de contract (fără lista de persoane, care aparține angajatului).
- `view_hr_payslip_form_l10n_ro_meal_tickets`: numărul de tichete pe fluturaș.
- `report_payslip_ro_clean`: șablonul fluturașului tipărit, fără rata ±100%.

**Reguli salariale**

Reguli noi: `NEIMPOZ`, `TICHETE`, `DPB`, `DPBTIN`, `DPBCOP`, `COSTANG`; reguli native suprascrise: `CAS`, `CASS`, `CAM`, `INCOMETAX`; concedii medicale: `CM_FS`, `CM_FNUASS`, `CAS_CM`, `CASS_CM`, `TAX_CM`.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; regulile salariale rulează în motorul standard de calcul al fluturașului (`data/hr_salary_rule_data.xml`).

#### 5. Conexiuni

- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): puntea care transferă în D112 tichetele, suma neimpozabilă, deducerile și bazele CAS/CASS din regulile acestui modul.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația D112; are propria formulă liniară de deducere, nealiniată cu grila pe tranșe (pentru liniile cu calcul automat).
- `l10n_ro_hr_payroll`: furnizează structura salarială de bază pentru Romania (regulile GROSS,
  CAS, CASS, INCOMETAX native) peste care acest modul aplică corecțiile fiscale.
- [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md): partea contabilă (conturi implicite pe reguli), separată din acest modul în 19.0.2.0.0; se instalează automat cu `l10n_ro_hr_payroll_account`.
