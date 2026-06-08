# Deltatech Services Maintenance (localizat la `deltatech_service_maintenance/index.md`)

- **Nume Tehnic:** `deltatech_service_maintenance`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_maintenance
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_maintenance`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul gestionează activitatea de service și mentenanță a echipamentelor. Permite înregistrarea sesizărilor primite de la clienți, transformarea lor în comenzi de service și planificarea reviziilor periodice ale echipamentelor. Pe baza planurilor de revizii, comenzile de service pot fi generate automat, ceea ce ajută echipa de service să țină evidența intervențiilor și să respecte termenele de mentenanță.

#### 2. Funcționalități Cheie

- Gestionare sesizări
- Gestionare comenzi de service
- Gestionare planuri de revizii
- Generare automată a comenzilor de service pe baza planului

#### 3. Dependențe

- `deltatech_service_equipment_base`
- `sale`
- `sales_team`
- `sale_stock`
- `stock`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, această secțiune nu este detaliată: descrierea acoperă Sumarul și Funcționalitățile Cheie fără a solicita explicit documentarea componentelor tehnice. Analiza codului pentru Modele, Vizualizări și Acțiuni Automate a fost omisă conform schemei wiki.

#### 5. Conexiuni

- `deltatech_service_equipment_base`: dependență de bază pentru gestionarea echipamentelor de service.
- `sale_stock`: legătură cu comenzile de vânzare și mișcările de stoc aferente intervențiilor de service.
