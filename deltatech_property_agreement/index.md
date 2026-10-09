# Property Agreement (Contracte pentru proprietăți)

- **Nume Tehnic:** `deltatech_property_agreement`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_property_agreement
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_property_agreement`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modul-punte între gestiunea proprietăților (clădiri) și modulele de servicii: permite asocierea unei clădiri cu un chiriaș, cu un contract de servicii și cu un echipament de serviciu, astfel încât pentru clădire să poată fi urmărite contorizările (de exemplu utilitățile) direct din fișa ei.

#### 2. Funcționalități Cheie

- În formularul clădirii apar câmpurile noi **Chiriaș** (Tenant), **Contract** (Agreement) și, ascuns, **Echipament de serviciu**.
- Buton inteligent **Contoare** (Meters) în formularul clădirii, care deschide lista contoarelor echipamentului asociat, filtrată automat și cu echipamentul precompletat la creare.
- Opțiunea **Building** adăugată la câmpul „Tip intern” al echipamentului de serviciu, pentru a marca echipamentele care reprezintă clădiri.

#### 3. Dependențe

- `deltatech_property`
- [deltatech_service_agreement](../deltatech_service_agreement/index.md)
- [deltatech_service_equipment](../deltatech_service_equipment/index.md)
- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md)

#### 4. Componente Cheie

**Modele**

- `property.building` (extins): adaugă `tenant_id` (`res.partner`), `agreement_id` (`service.agreement`) și `service_equipment_id` (`service.equipment`).
- `service.equipment` (extins): adaugă valoarea `building` în selecția `internal_type`.

**Vizualizări**

- `view_property_building_form`: moștenește formularul clădirii din `deltatech_property`; adaugă butonul Meters în `button_box` și câmpurile chiriaș/contract/echipament după proprietar.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele de servicii la care se leagă clădirea.
- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): furnizează acțiunea contoarelor folosită de buton.
