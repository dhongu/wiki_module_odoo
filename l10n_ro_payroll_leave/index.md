# Romania - Concedii medicale (indemnizații, FNUASS) (localizat la `l10n_ro_payroll_leave/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_leave`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_leave
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_leave`
- **Ultima Ingestie:** `2026-10-03`

#### 1. Sumar

Modulul calculează concediile medicale pe statul de plată românesc, după OUG 158/2005 (forma consolidată) și structura D112. Operatorul introduce un singur certificat de concediu medical; modulul calculează zilele lucrătoare, partea angajatorului și partea din FNUASS, procentul, baza pe 6 luni și rândurile din fluturaș, cu contribuțiile aferente. Concediul medical din *Concedii* se creează automat, ca zilele să nu se mai plătească ca salariu.

#### 2. Funcționalități Cheie

- **Certificat unic** (`l10n.ro.medical.certificate`): serie și număr (`D_1`/`D_2`), certificat inițial (`D_3`/`D_4`, `Data_CMI`, pentru continuări), data eliberării (`D_5`), perioada (`D_6`/`D_7`), codul de indemnizație (`D_9`), locul prescrierii (`D_10`), coduri `D_11`/`D_12`/`D_23`, bifele *Spitalizat* și *Program național*, CNP copil.
- **Nomenclator `D_9`** (`l10n.ro.medical.code`): codurile 01–17 și 51 din nomenclatorul ANAF, cu grupa, procentul (55 / 65 / 75% după durata certificatului la codul 01; procente fixe la celelalte), regula zilelor angajatorului, ziua neplătită, CASS și impozit pe cod. Codurile 10 și 11 au formule speciale și nu sunt calculate.
- **Zile:** zilele lucrătoare din perioadă (calendarul angajatului, sărbători excluse); primele 5 zile lucrătoare la angajator, restul din FNUASS; la codurile cu FNUASS integral toate sunt din FNUASS.
- **Prima zi neplătită** pentru certificatele eliberate între 01.02.2026 și 31.12.2027 (OUG 91/2025 art. II), cu excepțiile din Legea 64/2026 de la 01.06.2026 (maternitate, risc maternal, oncologie, spitalizare, programe naționale) și fără ea la codul 51.
- **Baza de calcul** (art. 10): media zilnică a veniturilor din cele mai recente 6 luni cu venit din ultimele 12, fiecare plafonată la 12 salarii minime din luna respectivă, cu indemnizațiile și zilele de concediu medical incluse; automată din fluturașii validați sau manuală (adeverință de la alt angajator).
- **Indemnizația** = media zilnică × zilele plătite × procentul, rotunjită la leu, separat pentru angajator și FNUASS.
- **Pe fluturaș:** `CM_FS` (în brut, cu CAS, CASS după cod, impozit și CAM), `CM_FNUASS` (categoria `CMFN`: în afara brutului și a bazei CAM, dar în venitul impozabil și în net), `CAS_CM`, `CASS_CM` (doar codurile 01, 07, 10) și `TAX_CM` (impozitul alocat proporțional părții din FNUASS). Zilele de concediu medical sunt neplătite ca salariu pentru structura RO.
- **Conturi** (cu [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md)): 4382 = 423 pentru FNUASS, contribuțiile și impozitul aferente pe 423; indemnizația angajatorului rămâne în brut (641 = 421).
- **Exemplu verificat** (14–23.09.2026, brut 5.000, media 238,10, 65%): indemnizații 619 (angajator) și 464 (FNUASS), salariu 3.181,82, CAS 950 + 116, CASS 380 + 46, impozit 191 (21 pe FNUASS), 423 net 281.

> **Limite cunoscute:** nu sunt implementate continuările (0 zile la angajator, procent pe episod, recalcul în luna curentă), carantina cod 05, D112 (GrupB, secțiunea D: la validare apare avertisment) și rapoartele. De confirmat: zilele angajatorului urmează convenția D112 (4 plătite), nu literal OUG 91/2025 (zilele 2–6); partea angajatorului se contabilizează 641 = 421 (funcțiunea OMFP ar fi 6458 = 423); excepția pentru codul 51, Legea 64/2026 și procentul la codurile 02–04.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- `hr_payroll_holidays`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.medical.certificate` (nou): certificatul, cu calculul zilelor, procentului, bazei și sumelor (`_compute_period`, `_day_schedule`, `_auto_base`).
- `l10n.ro.medical.code` (nou): nomenclatorul `D_9`.
- `hr.payslip` (extins): `_l10n_ro_cm_amounts` (sumele lunii, apelate de reguli).

**Reguli salariale**

`CM_FS`, `CM_FNUASS`, `CAS_CM`, `CASS_CM`, `TAX_CM` (`data/hr_salary_rule_data.xml`); tipul de prezență `LEAVE110` devine neplătit pentru structura RO.

**Vizualizări**

Formularul, lista și căutarea certificatelor, meniul *Salarizare → Angajați → Certificate medicale (RO)*.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; la instalare, `post_init_hook` completează conturile regulilor când contabilitatea salarizării e prezentă.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): categoria `CMFN` și cârligele de calcul (CASS, impozit, net, deduceri) pe care modulul le folosește.
- [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md): conturile regulilor de concediu medical.
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): puntea D112; avertisment pentru salariații cu concediu medical până la implementarea secțiunii D.
