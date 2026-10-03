# Romania - D112 ANAF: punte salarizare Odoo (localizat la `l10n_ro_anaf_d112_payroll/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d112_payroll`
- **Versiune:** `19.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d112_payroll
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d112_payroll`
- **Ultima Ingestie:** 2026-10-03
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face legătura directă între declarația D112 și salarizarea Odoo Enterprise: în loc să completeze manual evidența nominală, ea se preia automat din statele de plată validate ale lunii, iar previzualizarea obligațiilor de plată afișează o proiecție live calculată din salarizare, nu doar totalurile deja salvate în declarație. Se instalează singur când firma are atât D112, cât și salarizarea în Odoo; pentru clienții care țin salarizarea în afara Odoo (de exemplu, aplicații externe), D112 continuă să funcționeze independent, cu liniile completate prin import sau manual.

#### 2. Funcționalități Cheie

- **Import automat al evidenței nominale** din statele de plată validate (stare **Validat** sau **Plătit**) ale lunii, la apăsarea butonului **Calculează** din declarația D112 — câte o linie per stat de plată.
- **Mapare coduri regulă salarială → câmpuri D112:** `GROSS` (venit brut), `BASIC` (salariu de bază, cu revenire pe `GROSS` dacă lipsește), `CAS`, `CASS`, `INCOMETAX` (impozit).
- **Tichete, sumă neimpozabilă și deduceri**, din 19.0.1.1.0, din regulile modulului `l10n_ro_hr_payroll_enhancement`: `TICHETE` → tichete de masă; `NEIMPOZ` → suma neimpozabilă (declarată ca tip asigurat 51, A_13S); `DPB`, `DPBTIN`, `DPBCOP` → deducerea de bază, pentru tineri și pentru copii (E1_41, E1_421, E1_422). Bazele: CAS = brut − suma neimpozabilă; CASS = brut + tichete − suma neimpozabilă; baza CAM (`A_5`) = brut − suma neimpozabilă (fix în `l10n_ro_anaf_d112` 19.0.2.4.1). Numărul de persoane în întreținere și de copii înscriși în învățământ vine din evidența angajatului (altfel din numărul de pe versiune). Fără aceste reguli valorile rămân 0. **Scutirea de impozit din art. 60** (din 19.0.1.2.0): versiunea angajatului (`l10n_ro_tax_exempt_reason`: handicap → 1, cercetare-dezvoltare → 3) completează *Scutire impozit (art. 60)* pe linie; declarația emite `asigScu`, `E3_23`/`E3_24` (pct. 1) sau `E3_27`/`E3_28` (pct. 3), obligația 602 cu `A_scutit` și `angajatorF1`.
- **Deduceri din baza de impozit** (19.0.1.3.0): regula `DEDBAZA` (sindicat, pensie facultativă) → «alte deduceri» ale liniei, deci `E1_5` / `E3_13` cumulat; baza impozabilă din declarație coincide cu statul de plată.
- **Avertisment la validare** (19.0.1.4.0): salariat cu contract activ în lună fără fluturaș validat în declarație (doar când declarația are linii din state de plată).
- **Avertisment pentru concedii medicale** (19.0.1.4.1): salariații cu concediu medical pe fluturaș (`CM_FS` / `CM_FNUASS`) primesc avertisment la validare, fiindcă certificatele (secțiunea D, GrupB) nu se declară încă automat.
- **Zile din fluturaș (`worked_days_line_ids`)**, din 19.0.1.0.2: zilele lucrate din tipurile de prezență care nu sunt concediu (`WORK100`, `WORK110` munca de acasă, delegația), zilele de concediu de odihnă din `LEAVE120` și cele de concediu medical din `LEAVE110`. Un fluturaș fără linii de zile primește zilele lucrătoare ale lunii (NZL). Până în 19.0.1.0.2 se căuta o regulă salarială `WORK100` care nu există, deci declarația pleca mereu cu 21 de zile lucrate și fără CO/CM.
- **Zile cu contract activ (`zile_contract_activ`)**, din 19.0.1.0.3, pentru pragul minim CAS/CASS (art. 146 alin. 5^6 Cod fiscal; HG 1/2016, Titlul V, pct. 6 alin. 3): lucrate + CO + CM + zilele plătite sau absențele fără decizie de suspendare (evenimente familiale, recuperare, alt concediu plătit, absență nemotivată). Nu se numără concediul fără plată, suspendarea prin decizie, creșterea copilului, șomajul tehnic, maternitatea și sărbătorile (`LEAVE100`, pe care NZL le scade deja).
- **CNP și dată angajare preluate automat**: CNP din angajat (`l10n_ro_cnp`, cu revenire pe `ssnid`), data angajării din contractul/versiunea angajatului.
- **Idempotență la reimport**: un stat de plată deja importat nu se adaugă a doua oară; statele adăugate ulterior în lună intră la următoarea apăsare a butonului **Calculează**.
- **Linii cu valori autoritare**: liniile importate au „Calcul automat deduceri" debifat — valorile din statul de plată nu se recalculează din parametrii fiscali ai D112.
- **Proiecție live în previzualizarea „Obligații D112"**: cât timp luna are state de plată validate, sumele afișate vin din salarizare (impozit, CAS, CASS, CAM 2,25% din brut − suma neimpozabilă); fără state de plată în perioadă, raportul revine la totalurile declarației salvate.
- **Trasabilitate**: fiecare linie nominală păstrează statul de plată sursă (câmp ascuns implicit în listă, vizibil la nevoie pentru verificarea provenienței).

#### 3. Dependențe

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- `hr_payroll`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.d112` (extindere): `_d112_payslip_extras` preia tichetele, suma neimpozabilă și deducerile din regulile fluturașului; implementează punctul de extensie `_d112_collect_employee_lines` din `l10n_ro_anaf_d112` — populează evidența nominală din statele de plată validate/plătite ale perioadei; `_d112_payslip_days` calculează zilele lucrate, CO, CM și zilele cu contract activ din liniile de zile ale fluturașului.
- `l10n.ro.d112.employee.line` (extindere): adaugă câmpul `payslip_id` (statul de plată sursă), folosit pentru a evita importul dublu al aceleiași linii.
- `l10n_ro_anaf_d112.report.handler` (extindere, `models.AbstractModel`): implementează `_d112_live_obligation_amounts` — proiecția live a obligațiilor lunii (impozit, CAS, CASS, CAM) din statele de plată validate; întoarce dicționar gol dacă nu există state de plată în perioadă, pentru ca raportul să cadă pe declarația persistentă.

**Vizualizări**

- `views/l10n_ro_d112_views.xml` (`view_l10n_ro_d112_form_payroll`): extinde formularul declarației D112 din `l10n_ro_anaf_d112` cu coloana `payslip_id` (ascunsă implicit) în lista liniilor nominale.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul se declanșează manual prin butonul „Calculează" al declarației D112.*

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): sursa regulilor `TICHETE`, `NEIMPOZ`, `DPB`, `DPBTIN`, `DPBCOP` transferate pe linia nominală (nu e dependență; fără el valorile rămân 0).
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația de bază pe care acest modul o alimentează automat din salarizare, prin punctele de extensie `_d112_collect_employee_lines` și `_d112_live_obligation_amounts`.
- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): aduce în fluturaș, ca prezențe, zilele corectate în foaia colectivă de prezență; codurile de suspendare `L10N_RO_*` din [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md) sunt recunoscute la zilele cu contract activ (un cod absent din bază nu deranjează). Nu e dependență.
- `hr_payroll` (Odoo Enterprise): sursa statelor de plată (`hr.payslip`), a liniilor de regulă salarială și a liniilor de zile lucrate folosite la import.
