# Deltatech Services Task (localizat la `deltatech_service_task/index.md`)

- **Nume Tehnic:** `deltatech_service_task`
- **Versiune:** `19.0.0.0.18`
- **Cale:** `https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_task`
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_task`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul extinde sarcinile de proiect (project.task) cu informații specifice activităților de service și mentenanță. El leagă fiecare sarcină de locul funcțional și de echipamentul vizat, astfel încât echipele de teren și de proiect să poată identifica imediat unde și pe ce utilaj se desfășoară intervenția. Valoarea de afaceri constă în trasabilitatea sarcinilor de mentenanță în contextul echipamentelor gestionate.

#### 2. Funcționalități Cheie

- Adăugarea câmpului de loc funcțional (`service.location`) în sarcina de proiect.
- Adăugarea câmpului de echipament (`service.equipment`) în sarcina de proiect.

#### 3. Dependențe

- `deltatech_service_equipment_base`
- `project`
- `hr`

#### 4. Componente Cheie

`readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit detalierea componentelor tehnice. Conform fluxului de ingestie din `schema.md`, analiza codului pentru această secțiune (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server) este omisă.

#### 5. Conexiuni

- `deltatech_service_equipment_base`: furnizează modelele de loc funcțional (`service.location`) și echipament (`service.equipment`) folosite de câmpurile adăugate în sarcină.
- `project`: modulul nativ de proiecte ale cărui sarcini (`project.task`) sunt extinse.
- `deltatech_service`: suita de service Deltatech din care face parte acest modul.
