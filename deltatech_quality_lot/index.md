# Deltatech Quality Lot (localizat la `deltatech_quality_lot/index.md`)

- **Nume Tehnic:** `deltatech_quality_lot`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_quality_lot
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_quality_lot`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul extinde funcționalitatea de control al calității din Odoo pentru a lega verificările de calitate direct de loturile de produse. Astfel, un lot de marfă poate avea propriul istoric de verificări și alerte de calitate, ceea ce ajută echipele de recepție și producție să urmărească rapid dacă un lot este conform, în așteptare sau respins.

#### 2. Funcționalități Cheie

- Verificări și alerte de calitate asociate fiecărui lot, folosind relațiile multi-lot din Odoo 19.
- Dispozitive de laborator disponibile pe punctele de control, pe verificări și în asistentul (wizard) de verificare calitate.
- Generare automată a verificărilor din punctele de control „la cerere” (on-demand).
- Indicatori vizuali pe fișa lotului pentru verificările în așteptare și cele eșuate.
- Raport PDF de control al calității per lot.

#### 3. Dependențe

- `quality_control`

#### 4. Componente Cheie

**Modele**

- `quality.laboratory.device`: model nou care definește dispozitivele de laborator (nume, cod, notă), utilizate pentru a marca ce echipament a efectuat o verificare.
- `quality.check` (extins): adaugă câmpul `laboratory_device_id` pentru a lega verificarea de dispozitivul de laborator folosit.
- `quality.point` (extins): adaugă `laboratory_device_id` și suprascrie `_get_checks_values` pentru a propaga dispozitivul de laborator și titlul punctului de control către verificările generate.
- `quality.check.wizard` (extins): expune `laboratory_device_id` (câmp related pe verificarea curentă) în asistentul de completare a verificărilor.
- `stock.lot` (extins): adaugă `check_ids` (verificări), `quality_alert_ids` (alerte), câmpurile calculate `quality_check_todo`/`quality_check_fail`/`quality_alert_count`, plus metodele `action_open_quality_checks` (deschide verificările cu context implicit pentru lot/produs/companie), `check_quality` (generează și deschide verificările de calitate ale lotului) și `action_generate_quality_checks` (creează verificări noi pornind de la punctele de control „on-demand” aplicabile produsului/categoriei lotului).

**Vizualizări**

- `quality_laboratory_device_view_list` / `quality_laboratory_device_view_form`: listă și formular pentru configurarea dispozitivelor de laborator.
- `quality_laboratory_device_action` / `menu_quality_laboratory_device`: acțiune și meniu de configurare (Quality > Configuration > Laboratory Devices).
- `stock_production_lot_form_quality_control`: extinde formularul lotului cu secțiunea de verificări/alerte de calitate și indicatorii vizuali.
- `quality_check_view_form` / `quality_point_view_form`: adaugă câmpul dispozitiv de laborator pe formularele verificării, respectiv punctului de control.
- `view_quality_check_wizard`: adaugă selecția dispozitivului de laborator în asistentul de verificare.

**Rapoarte**

- Raport PDF „Quality Control Report” per lot, definit în `report/stock_lot_reports.xml` și `report/stock_lot_report_templates.xml`, tipărit din fișa lotului.

#### 5. Conexiuni

- `quality_control`: modulul de bază Odoo pentru managementul calității, extins de acest modul pentru a lucra la nivel de lot.
- `stock`: furnizează modelul `stock.lot`, extins pentru a găzdui verificările și alertele de calitate.
