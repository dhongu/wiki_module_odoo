# Romania - D112 ANAF: punte salarizare Odoo (localizat la `l10n_ro_anaf_d112_payroll/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d112_payroll`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d112_payroll
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d112_payroll`
- **Ultima Ingestie:** 2026-09-12

#### 1. Sumar

Modulul face legătura directă între declarația D112 și salarizarea Odoo Enterprise: în loc să completeze manual evidența nominală, ea se preia automat din statele de plată validate ale lunii, iar previzualizarea obligațiilor de plată afișează o proiecție live calculată din salarizare, nu doar totalurile deja salvate în declarație. Se instalează singur când firma are atât D112, cât și salarizarea în Odoo; pentru clienții care țin salarizarea în afara Odoo (de exemplu SAGA), D112 continuă să funcționeze independent, cu liniile completate prin import sau manual.

#### 2. Funcționalități Cheie

- **Import automat al evidenței nominale** din statele de plată validate (stare **Validat** sau **Plătit**) ale lunii, la apăsarea butonului **Calculează** din declarația D112 — câte o linie per stat de plată.
- **Mapare coduri regulă salarială → câmpuri D112:** `GROSS` (venit brut, bază CAS, bază CASS), `BASIC` (salariu de bază, cu revenire pe `GROSS` dacă lipsește), `CAS`, `CASS`, `INCOMETAX` (impozit), `WORK100` (zile lucrate, implicit 21 dacă lipsește).
- **CNP și dată angajare preluate automat**: CNP din angajat (`l10n_ro_cnp`, cu revenire pe `ssnid`), data angajării din contractul/versiunea angajatului.
- **Idempotență la reimport**: un stat de plată deja importat nu se adaugă a doua oară; statele adăugate ulterior în lună intră la următoarea apăsare a butonului **Calculează**.
- **Linii cu valori autoritare**: liniile importate au „Calcul automat deduceri" debifat — valorile din statul de plată nu se recalculează din parametrii fiscali ai D112.
- **Proiecție live în previzualizarea „Obligații D112"**: cât timp luna are state de plată validate, sumele afișate vin din salarizare (impozit, CAS, CASS, CAM 2,25% din brut); fără state de plată în perioadă, raportul revine la totalurile declarației salvate.
- **Trasabilitate**: fiecare linie nominală păstrează statul de plată sursă (câmp ascuns implicit în listă, vizibil la nevoie pentru verificarea provenienței).

#### 3. Dependențe

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- `hr_payroll`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.d112` (extindere): implementează punctul de extensie `_d112_collect_employee_lines` din `l10n_ro_anaf_d112` — populează evidența nominală din statele de plată validate/plătite ale perioadei.
- `l10n.ro.d112.employee.line` (extindere): adaugă câmpul `payslip_id` (statul de plată sursă), folosit pentru a evita importul dublu al aceleiași linii.
- `l10n_ro_anaf_d112.report.handler` (extindere, `models.AbstractModel`): implementează `_d112_live_obligation_amounts` — proiecția live a obligațiilor lunii (impozit, CAS, CASS, CAM) din statele de plată validate; întoarce dicționar gol dacă nu există state de plată în perioadă, pentru ca raportul să cadă pe declarația persistentă.

**Vizualizări**

- `views/l10n_ro_d112_views.xml` (`view_l10n_ro_d112_form_payroll`): extinde formularul declarației D112 din `l10n_ro_anaf_d112` cu coloana `payslip_id` (ascunsă implicit) în lista liniilor nominale.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul se declanșează manual prin butonul „Calculează" al declarației D112.*

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația de bază pe care acest modul o alimentează automat din salarizare, prin punctele de extensie `_d112_collect_employee_lines` și `_d112_live_obligation_amounts`.
- `hr_payroll` (Odoo Enterprise): sursa statelor de plată (`hr.payslip`) și a liniilor de regulă salarială folosite la import.
