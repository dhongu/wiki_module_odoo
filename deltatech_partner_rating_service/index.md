# Partner rating in service (localizat la `deltatech_partner_rating_service/index.md`)

- **Nume Tehnic:** `deltatech_partner_rating_service`
- **Versiune:** `19.0.0.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_partner_rating_service
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_rating_service`
- **Ultima Ingestie:** `2026-11-01`

#### 1. Sumar

Acest modul extinde vizibilitatea rating-ului de partener în modulele Odoo de gestiune a service-ului și a echipamentelor, permițând echipelor de service să vadă scorul de fiabilitate al partenerilor pe care îi deservesc. Din punct de vedere business, această transparență permite departamentelor de service să își adapteze activitățile de suport și mentenanță în funcție de poziția generală și istoricul clientului cu compania.

#### 2. Funcționalități Cheie

- Livrare de servicii informată: vizualizarea rating-ului partenerului direct pe fișele de echipament, pe contractele de service și pe informațiile de garanție.
- Fluxuri de suport prioritizate: utilizarea datelor de fiabilitate a partenerului pentru a prioritiza sarcinile de service sau pentru a ajusta nivelul de servicii așteptat.
- Management proactiv al garanției: decizii mai bune privind cererile de garanție și mentenanța, pe baza istoricului clientului.
- Interacțiune de service îmbunătățită: personalul tehnic poate avea o conversație mai bine informată cu partenerii, cunoscând rating-ul lor general.
- Strategie de service integrată: alinierea activităților de service și mentenanță cu politicile mai largi de relație cu partenerii și de management al riscului.

#### 3. Dependențe

- [deltatech_partner_rating](../deltatech_partner_rating/index.md)
- [deltatech_service_agreement](../deltatech_service_agreement/index.md)
- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md)
- [deltatech_service_maintenance](../deltatech_service_maintenance/index.md)

#### 4. Componente Cheie

Modulul adaugă pe modelele și vizualizările existente de service afișarea rating-ului partenerului provenit din modulul de bază `deltatech_partner_rating`. Readme-ul nu cere explicit detalierea componentelor; extensia e mică și a fost verificată în cod.

**Modele**

- `service.equipment` (extins): câmpul `partner_rating` („Customer rating”), citit de la partenerul comercial al echipamentului.
- `service.agreement` (extins): câmpul `partner_rating`, citit de la partenerul comercial al contractului de service.
- `service.warranty` (extins): câmpul `partner_rating`, citit de la partenerul comercial al garanției.

**Vizualizări**

- `views/service_equipment.xml`: afișează rating-ul în formularul de echipament.
- `views/service_agreement.xml`: afișează rating-ul în formularul contractului de service.
- `views/service_warranty.xml`: afișează rating-ul în formularul de garanție.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_partner_rating](../deltatech_partner_rating/index.md): modulul de bază care definește rating-ul de partener afișat de acest modul.
- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele de service pe care este afișat rating-ul.
- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): echipamentele și garanțiile pe care este afișat rating-ul.
