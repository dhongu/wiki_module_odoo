# Work Days Report (localizat la `deltatech_work_days_report/index.md`)

- **Nume Tehnic:** `deltatech_work_days_report`
- **Versiune:** `19.0.0.0.15`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_work_days_report
- **Cale Locală:** `odoo-addons/bitshop/deltatech_work_days_report`
- **Ultima Ingestie:** `2026-11-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

> **Modul în curs de retragere:** este înlocuit de [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md) (*Romania - Timesheet*), care face același lucru pornind de la programul real de lucru și de la contract, cu corecții, luni închise și export de tichete de masă. Modulul primește doar corecturi, fără funcționalități noi.

#### 1. Sumar

Modulul generează rapoarte Excel pentru prezența angajaților și pentru gestionarea tichetelor de masă. Este util departamentelor de resurse umane și salarizării: oferă fișiere Excel cu orele lucrate zilnic, totalurile pe angajat, codurile de concediu și tichetele de masă cuvenite, plus un fișier pentru bancă cu tichetele de masă pe card. Raportările rămân consecvente chiar și când configurarea tipurilor de concediu este incompletă.

#### 2. Funcționalități Cheie

- **Câmpuri pe angajat** (în tab-ul *Payroll*, sub *Schedule*): *Hours per Day* (2, 4, 6 sau 8 ore), *Meal Voucher Value* și *Full Name* (numele tipărit în fișierul pentru bancă; dacă lipsește, se folosește numele angajatului). CNP-ul și contul bancar din tab-ul *Personal* sunt tipărite tot în fișierul pentru bancă.
- **Cod pe tipul de concediu:** câmpul *Code* (implicit `L`) pe *Time Off Types*; un tip cu cod gol apare ca `ABS`.
- **Export în masă din lista de angajați** (*Actions*, pentru grupul HR Officer): *Export Working Days* și *Export Bank Meal Vouchers*; se alege perioada în *Date* și se apasă *Apply*, apoi se descarcă fișierul `work_day_report.xlsx` (ambele exporturi folosesc același nume de fișier). Dacă prima dată este după ultima, exportul este refuzat cu mesajul *Please make sure the second date is after the first*.
- **Foaia de prezență (Excel):** un rând pe angajat, cu *Norma* (ore pe zi), câte o coloană pe zi, câte o coloană pe cod de concediu, *Total number of hours* și *Meal Vouchers*.
  - Zilele din afara programului angajatului rămân goale (pentru program flexibil sau fără program se folosește luni–vineri); o sâmbătă programată este zi lucrată.
  - Zilele de sărbătoare legală apar ca `SL`, cele de concediu aprobat cu codul tipului, iar zilele din afara contractului ca `-`; doar concediile aprobate contează.
  - Un concediu în ore sau pe jumătate de zi păstrează orele lucrate și codul (de exemplu `6/CO`): orele intră în total, ziua în coloana codului și ziua dă în continuare un tichet de masă.
- **Fișier pentru bancă (tichete de masă pe card):** format Banca Transilvania (singurul disponibil), cu un rând pe angajat, sortat după nume: *Nr.*, *Name and Surname*, *SSN No*, *Value* (zilele cu tichet × *Meal Voucher Value*), *IBAN code* și *Details* (luna primei date). Zilele cu tichet sunt zilele din program și din contract care nu sunt sărbători legale și nu sunt concediu aprobat pe zi întreagă, indiferent de *Hours per Day*.
- **Migrare către `l10n_ro_hr_pontaj`:** *Export Working Days* corespunde cu *Time Off → Management → Timesheet*, iar *Export Bank Meal Vouchers* cu *Time Off → Management → Export Meal Vouchers*; câmpurile `meal_voucher_value` și `full_name` au aceleași nume tehnice, în timp ce *Hours per Day* nu este citit acolo (orele vin din programul de lucru). Diferență de verificat: aici se acordă un tichet pentru fiecare zi lucrătoare care nu e sărbătoare sau concediu, acolo pentru fiecare zi lucrată în pontaj. Detalii și pașii de migrare, în `readme/CONFIGURE.md`; valoarea maximă a tichetului este stabilită prin lege și nu este verificată de niciun modul.

*Notă:* textul vechi din pagină (README indicând „18.0” și lipsa exportului bancar) era depășit; informațiile au fost aliniate la `readme/` și la codul 19.0.

#### 3. Dependențe

- `hr`
- `hr_holidays`

> Dependență externă Python: `xlsxwriter`.

#### 4. Componente Cheie

**Modele**

- `hr.employee` (extins): câmpurile `hours_per_day` (2/4/6/8 ore), `meal_voucher_value` (implicit 15) și `full_name`.
- `hr.employee.public` (extins): aceleași câmpuri prin `related`, pentru ca exporturile să funcționeze și fără acces complet la `hr.employee`.
- `hr.leave.type` (extins): câmpul `type_code` („Code”, implicit `L`) pentru categorisirea concediilor în rapoarte.
- `work.days.common` (model abstract): logică comună celor două exporturi.
- `working.days.export` (wizard): construiește fișierul Excel cu foaia de prezență, orele lucrate, codurile de concediu și totalul tichetelor de masă.
- `bank.meal.voucher.export` (wizard): construiește fișierul Excel pentru bancă (`bank_format` = Banca Transilvania).

**Vizualizări**

- `employee_hors_form`: extinde formularul angajatului cu norma zilnică, valoarea tichetului de masă și numele complet.
- `leave_type_form`: extinde formularul tipului de concediu cu câmpul „Code”.
- `view_working_days_export_form`: formularul wizard-ului de export al zilelor lucrate.
- `view_bank_meal_vouchers_export_form`: formularul wizard-ului de export al tichetelor de masă pentru bancă.

**Acțiuni Automate / Acțiuni Server**

- `action_working_days_export` („Export Working Days”): acțiune legată de lista de angajați, deschide wizard-ul de raport Excel.
- `action_bank_meal_vouchers_export_export` („Export Bank Meal Vouchers”): acțiune legată de lista de angajați, deschide wizard-ul pentru fișierul bancar.

#### 5. Conexiuni

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md): modulul care înlocuiește acest modul (fișa de pontaj, export de tichete de masă); câmpurile `meal_voucher_value` și `full_name` sunt declarate în ambele.
- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): extensia de salarizare a pontajului, de instalat doar dacă se folosește salarizarea.
