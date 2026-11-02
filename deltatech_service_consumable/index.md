# Services Consumable (localizat la `deltatech_service_consumable/index.md`)

- **Nume Tehnic:** `deltatech_service_consumable`
- **Versiune:** `19.0.1.1.11`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_consumable
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_consumable`
- **Ultima Ingestie:** `2026-11-02`

#### 1. Sumar

Modulul urmărește consumabilele echipamentelor aflate sub un contract de service: ce s-a livrat, cât a mai rămas și cât costă livrările. Pentru fiecare echipament se văd consumabilele sub formă de indicatori, livrările pentru service se pregătesc direct din echipament, iar costul total al livrărilor se adună pe contract și se compară cu valoarea facturată. Un raport de eficiență pune în paralel consumabilele livrate și consumul citit de pe contoarele echipamentelor.

#### 2. Funcționalități Cheie

**Consumabile pe echipament**

- Pentru fiecare tip de echipament se definesc consumabilele (produse stocabile), cu cantitatea maximă permisă.
- Formularul echipamentului arată consumabilele ca indicatori: cantitatea rămasă este cantitatea livrată înmulțită cu durata de viață a produsului (de exemplu paginile unui toner), minus consumul citit de pe contorul echipamentului, în aceeași unitate de măsură.
- Livrările pentru service se pregătesc din echipament, cu consumabilele, adresa și contractul acestuia; produsele livrate sunt listate pe echipament.
- O verificare raportează consumabilele a căror cantitate ar depăși maximul permis.
- Tipul de operațiune pentru livrările de service se setează în setările de stoc (parametrul `service.picking_type_for_service`).

**Cost total**

- Fiecare livrare pentru service validată adaugă valoarea de stoc la costul contractului (retururile îl scad) și reîmprospătează totalurile echipamentului.
- Contractul afișează costul total și costul ca procent din suma facturată, recalculat la postarea unei facturi; acțiunea „Recompute costs" reconstruiește totalul din livrări.

**Raport de eficiență a serviciilor**

- `service.efficiency.report` pune consumabilele livrate pe echipament și contract lângă consumul citit de pe contoare, pentru o perioadă; este limitat la companiile active ale utilizatorului.

**Novități 19.0**

- Costul total se calculează mai rapid, iar raportul de eficiență filtrează corect pe unități de măsură.
- Manipularea mișcărilor de stoc este aliniată la modul standard din Odoo 19 (colete/pachete).

#### 3. Dependențe

- [deltatech_service_agreement](../deltatech_service_agreement/index.md)
- [deltatech_service_equipment](../deltatech_service_equipment/index.md)
- [deltatech_product_extension](../deltatech_product_extension/index.md)
- [deltatech_stock_report](../deltatech_stock_report/index.md)

#### 4. Componente Cheie

**Modele**

- `service.consumable.item`: consumabilul unui tip de echipament (produs, cantitate rămasă calculată, durata de viață, cantitate maximă, culorile indicatorului).
- `service.equipment.type`: extins cu lista consumabilelor (`consumable_item_ids`).
- `service.equipment`: extins cu consumabilele echipamentului, butonul de livrare pentru service și lista produselor livrate.
- `service.agreement`: extins cu `total_costs` și `total_percent` (cost total și procent din suma facturată), plus recalcularea costurilor din livrări.
- `stock.picking`: extins cu echipamentul și contractul; la validare actualizează costul contractului și totalurile echipamentului, iar `check_consumable` verifică depășirea cantității maxime.
- `account.move`: la postarea facturii se recalculează procentul de cost al contractului.
- `service.efficiency.report`: raport SQL (bazat pe `stock.picking.report`) cu consumabilele livrate și consumul din contoare.

**Vizualizări**

- `view_service_equipment_form`: butonul „Delivery for service", costurile și fila „Consumable" cu indicatorii pe echipament.
- `view_service_equipment_type_form`: consumabilele definite pe tipul de echipament.
- `view_service_agreement_form` / `view_service_agreement_tree`: butonul de livrări, costul total și procentul pe contract.
- `view_picking_form`: grupul „Service" (echipament, contract) pe transferul de stoc.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele de service pe care se acumulează costul livrărilor și se calculează procentul față de facturat.
- [deltatech_service_equipment](../deltatech_service_equipment/index.md): echipamentele, tipurile și contoarele extinse de acest modul.
- [deltatech_stock_report](../deltatech_stock_report/index.md): raportul de transferuri de stoc, pe care se bazează raportul de eficiență.
- [deltatech_product_extension](../deltatech_product_extension/index.md): furnizează durata de viață a produsului, folosită la calculul cantității rămase.
