# Services Task

- **Nume Tehnic:** `deltatech_service_task`
- **Versiune:** `19.0.0.0.25`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_task
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_task`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Tehnicienii care intervin la echipamentele clienților au nevoie de o listă de verificare pentru fiecare vizită și de o evidență a rezultatului. Modulul leagă sarcinile de proiect de echipamente, încarcă operațiunile echipamentului ca listă de verificare în sarcină și permite tipărirea unui raport de service. Astfel, intervențiile de mentenanță devin trasabile pe fiecare echipament gestionat.

#### 2. Funcționalități Cheie

- **Loc funcțional și echipament:** sarcinile primesc câmpurile *Functional Location* și *Service Equipment*. Lista de echipamente urmează locul ales, iar clientul se completează din oricare dintre ele.
- **Listă de verificare din echipament:** alegerea echipamentului copiază în sarcină piesele, verificările și măsurătorile lui, înlocuind liniile existente. Tehnicianul bifează *Is OK* sau *Not Applicable* și introduce valori și note; listele nu permit adăugarea de rânduri.
- **Tipuri de mentenanță:** liniile echipamentului și șabloanele tipului de echipament pot fi marcate cu unul sau mai multe *Maintenance Types* (ex. primăvară, toamnă, intermediară). O sarcină cu tip încarcă doar liniile potrivite și pe cele nemarcate, iar subsarcinile noi moștenesc tipul. Lista tipurilor se gestionează în Configurare.
- **Raport de service:** un PDF tipărit din sarcină arată starea fiecărei linii (*OK*, *Not OK*, *N/A*) sau valoarea ei; fiecare subsarcină cu echipament urmează pe pagină separată.
- **Istoric pe echipament:** butoanele *Tasks*, *Parts*, *Checks* și *Measurements* din formularul echipamentului arată contoare și deschid înregistrările aferente.
- **Echipa urmează persoanele alocate:** câmpul *Team* listează angajații utilizatorilor alocați și se actualizează odată cu ei; angajații fără utilizator sunt păstrați.
- **Drepturi de acces:** liniile (piese, verificări, măsurători) urmează drepturile sarcinii lor. Lista de verificare se încarcă doar la alegerea echipamentului în formular, nu la import.

#### 3. Dependențe

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md)
- `project`
- `hr`

#### 4. Componente Cheie

**Modele**

- `project.task` (extins): adaugă locul funcțional, echipamentul, tipul de mentenanță, echipa (`employee_ids`), liniile `part_ids` / `check_ids` / `measurement_ids` și un sumar al tipurilor de echipament; la schimbarea echipamentului sau a tipului de mentenanță reface lista de verificare (tipul de mentenanță o reface doar cât timp nu s-a lucrat pe linii).
- `project.task.part`, `project.task.check`, `project.task.measurement`: liniile de operațiuni ale sarcinii (piesă cu cantitate, verificare, măsurătoare cu valoare și unitate), cu note și bife *Is OK* / *Not Applicable*.
- `project.task.line.access.mixin` (abstract): face ca liniile să urmeze drepturile sarcinii — citirea cere acces de citire pe sarcină, crearea, modificarea și ștergerea cer acces de scriere.
- `service.maintenance.type`: tip de mentenanță gestionat de utilizator; `service.maintenance.types.mixin` adaugă marcajul `maintenance_type_ids` pe șabloanele de piese/verificări/măsurători și pe liniile echipamentului (nemarcat = valabil la toate tipurile).
- `service.equipment` (extins): contoarele și acțiunile de istoric (sarcini, piese, verificări, măsurători) și copierea tipurilor de mentenanță din șablon.

**Vizualizări**

- `view_task_form2_inherited`: formularul sarcinii extins cu locul, echipamentul, echipa și listele de operațiuni; `view_task_search_form_inherited` extinde căutarea.
- `view_task_form2_maintenance_type`: câmpul tipului de mentenanță în sarcină.
- `view_service_equipment_form_inherited`: butoanele de istoric pe echipament; `view_project_task_part_tree`, `view_project_task_check_tree`, `view_project_task_measurement_tree`: listele istoricului.
- `view_service_maintenance_type_list` și `action_service_maintenance_type`: gestionarea tipurilor de mentenanță (meniu în Configurare); `view_service_equipment_type_form_maintenance` și `view_service_equipment_form_maintenance`: marcarea operațiunilor pe tipuri de mentenanță.

**Acțiuni Automate / Acțiuni Server**

- `action_report_project_task_service` (`ir.actions.report`, cu formatul de hârtie `paperformat_service_report`): raportul PDF de service al sarcinii. Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): furnizează modelele de loc funcțional (`service.location`) și echipament (`service.equipment`) folosite de sarcină.
- [deltatech_service](../deltatech_service/index.md): suita de service Deltatech din care face parte acest modul.
- `project`: modulul nativ de proiecte ale cărui sarcini (`project.task`) sunt extinse.
