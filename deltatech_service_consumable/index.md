# Services Consumable (localizat la `deltatech_service_consumable/index.md`)

- **Nume Tehnic:** `deltatech_service_consumable`
- **Versiune:** `20.0.1.1.10`
- **Cale:** `https://github.com/dhongu/deltatech_service/tree/20.0/deltatech_service_consumable`
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_consumable`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul extinde suita de service Deltatech cu gestiunea consumabilelor măsurate prin contoare. Permite urmărirea echipamentelor și a contoarelor asociate, înregistrarea citirilor și facturarea pe baza lor. Pentru perioadele fără citire reală, modulul calculează estimări și poate introduce automat, la sfârșitul perioadei, valori estimate, reducând efortul manual și erorile de facturare.

#### 2. Funcționalități Cheie

- Gestiunea echipamentelor și a contoarelor.
- Gestiunea citirilor de contor.
- Facturare pe baza citirilor.
- Calculul estimărilor de citire.
- Introducerea automată, la sfârșitul perioadei, a valorilor estimate.
- Raport de eficiență a serviciilor (`service.efficiency.report`), restricționat la companiile active ale utilizatorului.
- Costul livrărilor legate de contract se adaugă la costurile contractului doar la finalizarea transferului.

#### 3. Dependențe

- [deltatech_service_agreement](../deltatech_service_agreement/index.md)
- [deltatech_service_equipment](../deltatech_service_equipment/index.md)
- [deltatech_product_extension](../deltatech_product_extension/index.md)
- [deltatech_stock_report](../deltatech_stock_report/index.md)

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru componente.

#### 5. Conexiuni

- [deltatech_service_equipment](../deltatech_service_equipment/index.md): echipamentele, contoarele și citirile pe care se bazează consumabilele.
- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele și consumurile din care rezultă facturarea.
