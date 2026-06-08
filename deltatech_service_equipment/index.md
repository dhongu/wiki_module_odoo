# Services Equipment (localizat la `deltatech_service_equipment/index.md`)

- **Nume Tehnic:** `deltatech_service_equipment`
- **Versiune:** `19.0.1.1.11`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_equipment
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_equipment`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul gestionează echipamentele de service și contoarele asociate acestora. Permite înregistrarea citirilor de contoare și facturarea pe baza acestor citiri, inclusiv calculul unei estimări a citirilor. La finalul perioadei, valorile estimate pot fi introduse automat, simplificând astfel procesul de facturare periodică legat de utilizarea echipamentelor.

#### 2. Funcționalități Cheie

- Gestionarea echipamentelor
- Gestionarea contoarelor
- Gestionarea citirilor de contoare
- Facturare pe baza citirilor
- Calculul estimării citirilor
- Introducerea automată, la finalul perioadei, a valorilor estimate

#### 3. Dependențe

- [deltatech_service_agreement](../deltatech_service_agreement/index.md)
- `deltatech_service_equipment_base`
- `analytic`
- `stock`

Dependențe externe Python: `xlwt`.

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, secțiunea de funcționalități este acoperită de Readme; analiza detaliată a codului pentru Componente Cheie (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server) este omisă deoarece nu este solicitată explicit în Readme.

#### 5. Conexiuni

- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele de service pe baza cărora se facturează utilizarea echipamentelor.
- `deltatech_service_equipment_base`: modulul de bază pentru definirea echipamentelor de service.
