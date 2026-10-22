# Time Off Overview Access (localizat la `deltatech_hr_holidays_report_access/index.md`)

- **Nume Tehnic:** `deltatech_hr_holidays_report_access`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_hr_holidays_report_access
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_hr_holidays_report_access`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

În Odoo standard, *Time Off → Overview* arată concediile întregii companii oricărui utilizator intern. Acest modul restrânge vizibilitatea pe grupuri: angajații își văd doar propriile concedii, aprobatorii văd și concediile echipei pe care o aprobă, iar responsabilii de concedii văd tot. Astfel se protejează confidențialitatea absențelor, fără configurări complicate.

#### 2. Funcționalități Cheie

- Angajații văd în *Time Off → Overview* doar propriile concedii.
- Aprobatorii de concedii (grupul *Time Off Responsible*) văd propriile concedii și pe cele ale angajaților pe care îi aprobă. Grupul se atribuie automat de Odoo când utilizatorul e setat ca aprobator al unui angajat.
- Grupurile *Officer* și *Administrator* de Time Off văd toată compania.
- Regulile sunt doar de citire și replică regulile de citire existente pe `hr.leave`.
- Fără configurare: pentru ca o persoană să vadă concediile unei echipe, se completează câmpul *Time Off* (fila *Settings*, secțiunea *Approvers*) pe fiecare angajat din echipă.

#### 3. Dependențe

- `hr_holidays`

#### 4. Componente Cheie

**Modele**

- `hr.leave.report.calendar` (din `hr_holidays`): nu este extins în cod, i se adaugă doar reguli de acces.

**Vizualizări**

- Nu adaugă vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu are. Securitate (`security/hr_leave_report_calendar_security.xml`, `noupdate`), trei reguli `ir.rule` de citire:
  - `hr_leave_report_calendar_rule_employee`: `employee_id.user_id = user.id`, pentru `base.group_user`;
  - `hr_leave_report_calendar_rule_responsible`: `employee_id.leave_manager_id = user.id`, pentru `group_hr_holidays_responsible`;
  - `hr_leave_report_calendar_rule_officer`: acces total, pentru `group_hr_holidays_user`.

#### 5. Conexiuni

- `hr_holidays`: modulul standard ale cărui reguli de acces pe raportul calendar sunt completate (nu există alte legături funcționale verificate).
