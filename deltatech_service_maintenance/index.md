# Services Maintenance (localizat la `deltatech_service_maintenance/index.md`)

- **Nume Tehnic:** `deltatech_service_maintenance`
- **Versiune:** `19.0.1.2.10`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_maintenance
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_maintenance`
- **Ultima Ingestie:** `2026-11-02`

#### 1. Sumar

Modulul gestionează service-ul corectiv și preventiv pentru echipamentele și locațiile clienților, de la prima sesizare până la procesul-verbal de predare. Sesizările primite de la clienți se transformă în comenzi de service, livrări, transferuri interne sau comenzi de vânzare, iar comenzile de service urmăresc operațiile, piesele folosite și semnătura clientului. Modulul gestionează și garanțiile și recondiționările, cu aprobare dedicată, și oferă rapoartele de predare-primire. Nu include planuri de revizii și nici generare automată de comenzi de service.

#### 2. Funcționalități Cheie

**Sesizări** (`service.notification`)

- Înregistrarea unei sesizări pentru un echipament sau o locație de service, cu client, contact, adresă, responsabil, centru de lucru, prioritate, subiect și note.
- Categoria sesizării: constatare defect, livrare, transfer sau vânzare; tip extern sau intern.
- Flux: Nouă, Alocată, În lucru, Finalizată, cu datele de alocare, început și finalizare completate automat.
- Linii cu produsele cerute și operațiile planificate; disponibilitatea în stoc a fiecărui produs este afișată pe linie.
- Din sesizare se creează comanda de service, o livrare, un transfer intern sau o comandă de vânzare, toate legate înapoi de sesizare.

**Comenzi de service** (`service.order`)

- Tip de comandă cu categorie **Corectivă** sau **Preventivă**, plus opțiunile pentru deplasare, livrare și vânzare.
- Flux: Draft, Acknowledge, On the way, In Progress, Work Done, Completed, cu Rejected și Cancel; date de deplasare, început și finalizare.
- Operații (cu durată și produsul de serviciu asociat), componente (piesele folosite, cu disponibilitate în stoc), motiv, parametri de funcționare ai echipamentului după intervenție și semnătura clientului.
- Livrări și comenzi de vânzare create din comandă și legate de ea.

**Garanții și recondiționări** (`service.warranty`)

- Dosare de garanție sau recondiționare pentru un echipament, cu clientul, produsele folosite și suma totală.
- Flux: New, Assigned, In Progress, Approval requested, Approved, Done; aprobarea și validarea livrărilor de garanție sunt rezervate grupului de aprobare a garanțiilor.
- Produsele livrate actualizează liniile garanției cu costul real.
- Stare de clarificări și legături către livrare, comanda de vânzare și factură.

**Rapoarte**

- Service Order, Handover report și Minutes of receipt, tipărite din comanda de service; Notification, tipărit din sesizare.

**Configurare**

- Centre de lucru cu locație de stoc, tip de operațiune, rute de vânzare și transfer și cost pe oră; locația de stoc se poate seta și pe locația de service.
- Tipuri de sesizări, tipuri de comenzi, motive, operații și parametri de funcționare.

#### 3. Dependențe

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md)
- `sale`
- `sales_team`
- `sale_stock`
- `stock`

#### 4. Componente Cheie

**Modele**

- `service.notification` (cu `service.notification.item`, `service.notification.operation`, `service.notification.type`): sesizările de service, cu linii de produse, operații și tipuri.
- `service.order` (cu `service.order.component`, `service.order.operation`, `service.order.reason`, `service.order.type`, `service.operating.parameter`, `service.operation`): comenzile de service și nomenclatoarele lor.
- `service.warranty` (cu `service.warranty.item`): garanții și recondiționări.
- `service.work.center`: centrul de lucru, cu locație de stoc, tip de operațiune, rute și cost pe oră.
- `service.equipment`, `service.location`, `product.template`, `res.config.settings`, `sale.order`, `sale.order.line`, `stock.picking`, `stock.lot`: extinse pentru legăturile cu service-ul.

**Vizualizări**

- `view_service_notification_form` / `_tree` / `_kanban` / `_filter`: lucrul cu sesizările.
- `view_service_order_form` / `view_service_order_tree`: comenzile de service.
- `view_service_warranty_form` / `_tree` / `_filter`: garanțiile și recondiționările.
- `view_service_work_center_form` / `_tree`: centrele de lucru.
- `view_service_operation_form` / `_tree`: operațiile de service.
- `view_service_equipment_form`, `view_service_location_form`, `view_order_form`, `view_picking_form`, `view_production_lot_form`: legăturile cu echipamentul, locația, vânzarea și stocul.
- `report_notification.xml`, `report_order.xml`: rapoartele tipărite.

**Acțiuni Automate / Acțiuni Server**

- `action_clear_clarifications`: acțiune server (`ir.actions.server`) pentru ștergerea stării de clarificări a garanțiilor.
- Secvențe `ir.sequence` pentru numerotarea sesizărilor, comenzilor de service și garanțiilor. Nu există acțiuni `ir.cron` sau `base.automation`.

#### 5. Conexiuni

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): echipamentele și locațiile de service pe care lucrează sesizările și comenzile.
- `sale_stock`: comenzile de vânzare și livrările create din sesizări, comenzi de service și garanții.
