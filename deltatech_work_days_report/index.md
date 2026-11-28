# Work Days Report (localizat la `deltatech_work_days_report/index.md`)

- **Nume Tehnic:** `deltatech_work_days_report`
- **Versiune:** `20.0.0.0.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_work_days_report
- **Cale Locală:** `odoo-addons/bitshop/deltatech_work_days_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează rapoarte Excel pentru pontajul angajaților și pentru tichetele de masă pe card. **Este în curs de retragere în favoarea modulului [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md)** (*Romania - Timesheet*), care face același lucru din programul real de lucru și din contract, cu corecții, luni închise și export de tichete; modulul primește doar remedieri, fără funcționalități noi.

#### 2. Funcționalități Cheie

- **Cod pe tipul de concediu:** câmp **Code** pe *Time Off Type* (implicit `L`); un tip cu codul gol apare ca `ABS`.
- **Câmpuri pe angajat** (tab-ul **Payroll**, grupul **Schedule**): **Hours per Day** (2, 4, 6 sau 8), **Meal Voucher Value** și **Full Name** (numele din fișierul bancar; dacă e gol se folosește numele angajatului).
- **Export în masă** din lista de angajați (*Actions*): **Export Working Days** și **Export Bank Meal Vouchers** (grupul HR Officer).
- **Foaie de prezență:** câte un rând pe angajat, cu orele lucrate pe fiecare zi din programul de lucru (programul flexibil sau lipsa lui înseamnă luni–vineri), codul concediului aprobat și total pe cod, `SL` în sărbători legale, `-` în afara contractului, total ore și număr de tichete; un concediu în ore sau pe jumătate de zi păstrează orele lucrate (de ex. `6/CO`).
- **Fișier bancar pentru tichete:** Excel în formatul Banca Transilvania (singurul disponibil), cu nume, CNP, valoare (zile cu tichet × **Meal Voucher Value**), IBAN și detaliul lunii primei date; ziua cu tichet = zi din program, în contract, fără sărbătoare legală sau zi întreagă de concediu aprobat.
- Contează doar concediile aprobate; sărbătorile legale se introduc în *Time Off > Configuration > Public Holidays*. Dacă prima dată e după ultima, exportul este refuzat.
- Migrare recomandată la `l10n_ro_hr_pontaj`: câmpurile `meal_voucher_value` și `full_name` se păstrează, **Hours per Day** nu mai e citit (se folosește programul de lucru), iar tichetele se acordă pe zi lucrată în pontaj; pașii de migrare sunt în `readme/CONFIGURE.md`.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `hr`
- `hr_holidays`
- Dependență externă Python: `xlsxwriter`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` (completat cu `USAGE.md` / `CONFIGURE.md`), deci analiza componentelor este sumară.

**Modele**

- `hr.employee` (extins): `hours_per_day`, `meal_voucher_value`, `full_name`.
- `hr.leave.type` (extins): `type_code` (**Code**).
- `working.days.export` (wizard): construiește foaia Excel de prezență.
- `bank.meal.voucher.export` (wizard): construiește fișierul Excel pentru bancă.

**Vizualizări**

- `employee_hors_form`: extinde formularul angajatului cu cele trei câmpuri, în tab-ul Payroll.
- `view_working_days_export_form`: wizard-ul de export al prezenței (interval de date).
- `view_bank_meal_vouchers_export_form`: wizard-ul de export al tichetelor (format bancă + interval).

**Acțiuni Automate / Acțiuni Server**

- `action_working_days_export` și `action_bank_meal_vouchers_export_export`: acțiuni legate de lista de angajați, care deschid wizard-urile. Nu există sarcini `ir.cron`.

#### 5. Conexiuni

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md): modulul care înlocuiește acest raport (pontaj din programul real, export de tichete).
