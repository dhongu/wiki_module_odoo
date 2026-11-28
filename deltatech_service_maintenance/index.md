# Services Maintenance (localizat la `deltatech_service_maintenance/index.md`)

- **Nume Tehnic:** `deltatech_service_maintenance`
- **Versiune:** `20.0.1.2.9`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/20.0/deltatech_service_maintenance
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_maintenance`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul gestionează activitatea de service și mentenanță a echipamentelor. Permite înregistrarea sesizărilor primite de la clienți, transformarea lor în comenzi de service și planificarea reviziilor periodice ale echipamentelor. Pe baza planurilor de revizii, comenzile de service pot fi generate automat, ceea ce ajută echipa de service să țină evidența intervențiilor și să respecte termenele de mentenanță.

#### 2. Funcționalități Cheie

- Gestionare sesizări.
- Gestionare comenzi de service, fiecare cu propriul token de acces la portal (generat distinct la crearea comenzii).
- Gestionare planuri de revizii.
- Generare automată a comenzilor de service pe baza planului.
- Documentele de service (sesizare, comandă, garanție) pot genera livrări de stoc cu produsele și cantitățile aferente.

#### 3. Dependențe

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md)
- `sale`
- `sales_team`
- `sale_stock`
- `stock`

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice. (Notă: DESCRIPTION.md menționează ca temă viitoare utilizarea și a modulului standard de mentenanță.)

#### 5. Conexiuni

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): dependență de bază pentru gestionarea echipamentelor de service.
- `sale_stock`: legătură cu comenzile de vânzare și mișcările de stoc aferente intervențiilor de service.
