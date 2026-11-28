# Services Task (localizat la `deltatech_service_task/index.md`)

- **Nume Tehnic:** `deltatech_service_task`
- **Versiune:** `20.0.0.0.24`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/20.0/deltatech_service_task
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_task`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul extinde sarcinile de proiect (project.task) cu informații specifice activităților de service și mentenanță. El leagă fiecare sarcină de locul funcțional și de echipamentul vizat, astfel încât echipele de teren și de proiect să poată identifica imediat unde și pe ce utilaj se desfășoară intervenția. Valoarea de afaceri constă în trasabilitatea sarcinilor de mentenanță în contextul echipamentelor gestionate.

#### 2. Funcționalități Cheie

- Adăugarea câmpului de loc funcțional (`service.location`) în sarcina de proiect.
- Adăugarea câmpului de echipament (`service.equipment`) în sarcina de proiect.

#### 3. Dependențe

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md)
- `project`
- `hr`

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit detalierea componentelor tehnice.

#### 5. Conexiuni

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): furnizează modelele de loc funcțional (`service.location`) și echipament (`service.equipment`) folosite de câmpurile adăugate în sarcină.
- `project`: modulul nativ de proiecte ale cărui sarcini (`project.task`) sunt extinse.
- [deltatech_service](../deltatech_service/index.md): suita de service Deltatech din care face parte acest modul.
