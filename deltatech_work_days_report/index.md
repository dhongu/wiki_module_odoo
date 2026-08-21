# Work Days Report (localizat la `deltatech_work_days_report/index.md`)

- **Nume Tehnic:** `deltatech_work_days_report`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_work_days_report
- **Cale Locală:** `odoo-addons/bitshop/deltatech_work_days_report`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul **Work Days Report** generează rapoarte Excel cuprinzătoare pentru urmărirea prezenței angajaților și gestionarea tichetelor de masă. Este util departamentelor de resurse umane și proceselor de salarizare, oferind automat fișiere Excel cu orele lucrate zilnic, totalurile pe angajat, tichetele de masă cuvenite și perioadele de concediu. Astfel se simplifică monitorizarea tiparelor de lucru ale angajaților și administrarea drepturilor la tichete de masă, asigurând raportări consecvente chiar și atunci când configurarea tipurilor de concediu este incompletă.

#### 2. Funcționalități Cheie

- **Îmbunătățirea tipurilor de concediu**: adaugă un câmp configurabil „code" în formularele de tip de concediu (Time Off Type), pentru o mai bună categorisire și raportare.
- **Export Excel în masă**: permite exportul în masă accesibil din vizualizarea de listă a angajaților (Acțiune → „Export Working Days").
- **Raportare cuprinzătoare**: generează rapoarte Excel detaliate care conțin informații despre angajat și orele lucrate zilnic, totalul orelor lucrate, tichetele de masă câștigate per angajat și perioadele/datele de concediu.
- **Flexibilă codificare a concediilor**: afișează automat „ABS" (absență) pentru tipurile de concediu fără cod specificat, asigurând o raportare consecventă chiar și cu o configurare incompletă.
- **Export tichete de masă către bancă**: acțiune suplimentară „Export Bank Meal Vouchers", disponibilă tot din lista de angajați, care generează un fișier Excel în formatul cerut de Banca Transilvania (nume, CNP, valoare, cont IBAN), calculând automat numărul de zile lucrate eligibile pentru tichete în intervalul selectat.

> Notă corecție: `readme/DESCRIPTION.md` din sursă indică încă „Version: 18.0.0.0.2" și nu menționează exportul bancar de tichete de masă; informațiile de mai sus au fost aliniate la manifestul curent (`19.0.0.0.3`) și la codul din `wizard/back_meal_vouchers_export.py`, adăugat ulterior redactării README-ului.

#### 3. Dependențe

- `hr`
- `hr_holidays`

#### 4. Componente Cheie

**Modele**

- `hr.employee` (extins): adaugă câmpurile `hours_per_day` (normă zilnică: 2/4/6/8 ore), `meal_voucher_value` (valoare tichet de masă) și `full_name` (nume complet folosit la export).
- `hr.employee.public` (extins): expune aceleași câmpuri (`hours_per_day`, `meal_voucher_value`, `full_name`) prin câmpuri `related`, pentru ca wizard-urile de export să funcționeze și pentru utilizatori fără acces complet la `hr.employee` (fallback pe profilul public).
- `hr.leave.type` (extins): adaugă câmpul `type_code` („Code") pentru categorisirea tipurilor de concediu în rapoarte.
- `working.days.export` (wizard, tranzitoriu): construiește fișierul Excel cu foaia de prezență lunară, orele lucrate, codurile de concediu și totalul tichetelor de masă.
- `bank.meal.voucher.export` (wizard, tranzitoriu): construiește fișierul Excel de export al tichetelor de masă către bancă (momentan suportă formatul Banca Transilvania).

**Vizualizări**

- `employee_hors_form`: extinde formularul angajatului (`hr.view_employee_form`) cu norma zilnică, valoarea tichetului de masă și numele complet.
- `leave_type_form`: extinde formularul tipului de concediu (`hr_holidays.edit_holiday_status_form`) cu câmpul „Code".
- `view_working_days_export_form`: formularul wizard-ului de export al zilelor lucrate (selecție interval de date, apoi descărcare fișier).
- `view_bank_meal_vouchers_export_form`: formularul wizard-ului de export al tichetelor de masă către bancă (format bancă + interval de date, apoi descărcare fișier).

**Acțiuni Automate / Acțiuni Server**

- `action_working_days_export` („Export Working Days"): acțiune legată de lista de angajați (`binding_model_id` pe `hr.employee`), deschide wizard-ul care generează raportul Excel cu orele lucrate și tichetele de masă.
- `action_bank_meal_vouchers_export_export` („Export Bank Meal Vouchers"): acțiune legată de lista de angajați, deschide wizard-ul care generează fișierul Excel de export al tichetelor de masă pentru bancă.

#### 5. Conexiuni

- Nicio conexiune funcțională suplimentară identificată către alte module cu pagină wiki.
