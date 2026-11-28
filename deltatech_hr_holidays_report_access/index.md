# Acces Prezentare Generală Concedii (localizat la `deltatech_hr_holidays_report_access/index.md`)

- **Nume Tehnic:** `deltatech_hr_holidays_report_access`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_hr_holidays_report_access
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_hr_holidays_report_access`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

În Odoo standard, ecranul *Time Off → Overview* arată concediile întregii companii oricărui utilizator intern, iar filtrul *My Team* este doar o căutare. Modulul adaugă aceleași reguli de citire pe care le are deja `hr.leave`, astfel încât fiecare utilizator să vadă doar concediile la care are dreptul: ale sale, ale echipei pe care o aprobă sau, pentru administratori, ale întregii companii.

#### 2. Funcționalități Cheie

- Angajații văd în prezentarea generală doar propriile concedii.
- Aprobatorii de concedii (grupul *Time Off Responsible*) văd concediile proprii și ale angajaților pe care îi aprobă.
- Responsabilii (*Officer*) și administratorii modulului Time Off văd toată compania.
- Fără configurare dedicată: grupul *Time Off Responsible* se atribuie automat când un utilizator este setat ca aprobator în câmpul *Time Off* (fila *Settings*, secțiunea *Approvers*) al unui angajat; pentru a da unei persoane vizibilitate asupra unei echipe, se setează persoana respectivă ca aprobator pe fiecare angajat din echipă.

#### 3. Dependențe

- `hr_holidays`

#### 4. Componente Cheie

**Modele**

- `hr.leave.report.calendar` (standard): primește reguli de acces pe grupuri, prin `security/ir.access.csv`.

**Vizualizări**

- Modulul nu adaugă vizualizări; schimbă doar ce înregistrări apar în *Time Off → Overview*.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `hr_holidays`: aplică pe raportul de calendar aceleași reguli de citire ca pe cererile de concediu.
