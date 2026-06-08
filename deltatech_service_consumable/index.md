# Services Consumable (localizat la `deltatech_service_consumable/index.md`)

- **Nume Tehnic:** `deltatech_service_consumable`
- **Versiune:** `19.0.1.1.6`
- **Cale:** `https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_consumable`
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_consumable`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul extinde suita de service Deltatech cu gestiunea consumabilelor măsurate prin contoare. Permite urmărirea echipamentelor și a contoarelor asociate, înregistrarea citirilor de contor și facturarea pe baza acestor citiri. Pentru perioadele în care nu există o citire reală, modulul poate calcula estimări de consum și poate introduce automat, la sfârșitul perioadei, valori estimate. Valoarea principală constă în legarea consumului real (sau estimat) de procesul de facturare a serviciilor, reducând efortul manual și erorile.

#### 2. Funcționalități Cheie

- Gestiunea echipamentelor.
- Gestiunea contoarelor.
- Gestiunea citirilor de contor.
- Facturare pe baza citirilor.
- Calculul estimat al citirilor.
- Introducerea automată, la sfârșitul perioadei, a valorilor estimate.

#### 3. Dependențe

- `deltatech_service_agreement`
- `deltatech_service_equipment`
- `deltatech_product_extension`
- `deltatech_stock_report`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, această secțiune nu a fost detaliată: descrierea acoperă Sumarul și Funcționalitățile Cheie, iar conform schemei de ingestie analiza codului pentru componente este omisă atunci când Readme-ul este prezent și nu o solicită explicit.

#### 5. Conexiuni

- `deltatech_service_agreement`: contractele de service pe baza cărora se generează facturarea consumului.
- `deltatech_service_equipment`: echipamentele și contoarele extinse de acest modul.
- `deltatech_stock_report`: raportarea de stoc reutilizată în contextul consumabilelor.
