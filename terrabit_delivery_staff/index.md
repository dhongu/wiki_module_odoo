# Delivery Staff (localizat la `terrabit_delivery_staff/index.md`)

- **Nume Tehnic:** `terrabit_delivery_staff`
- **Versiune:** `20.0.0.0.18`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/terrabit_delivery_staff
- **Cale Locală:** `odoo-addons/bitshop/terrabit_delivery_staff`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite distribuirea livrărilor către personalul propriu de livrare (curieri/șoferi interni). Fiecare livrare se atribuie unui angajat din grupul „Delivery staff", iar acești utilizatori văd și gestionează doar propriile livrări. Modulul oferă și un raport PDF dedicat personalului de livrare, util la organizarea traseelor și a predării coletelor.

#### 2. Funcționalități Cheie

- Distribuirea livrărilor pe angajați (personal de livrare propriu), cu meniu și vedere kanban dedicate.
- Restricționarea accesului: utilizatorii din grupul „Delivery staff" nu pot modifica livrările altor utilizatori.
- Raport PDF pe livrare, pentru personalul de livrare (pickup list).
- Parametrul de sistem `delivery_staff.allow_change_responsible` controlează dacă personalul poate schimba responsabilul de pe livrare (implicit `False`).
- Tipul de operațiune are bifa **Visible on delivery staff pickings**; livrarea are stările *delivered* și *invoice done* (facturarea marchează livrarea).

#### 3. Dependențe

- `sale`
- `stock`
- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- [deltatech_logistic_docs](../deltatech_logistic_docs/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` (completat sumar din cod); modulul nu are fișă consultant.

**Modele**

- `stock.picking` (extins): `responsible_id` („Assigned to", grupat kanban), `delivered`, `invoice_done`, `action_confirm_delivery`, restricții la `write`.
- `stock.picking.type` (extins): `visible_on_delivery_staff`.
- `stock.move.line`, `stock.move` (extinse): restricții la scriere și deschiderea produsului.
- `account.move` (extins): la postare/revenire în ciornă/anulare actualizează `invoice_done` pe livrări.

**Vizualizări**

- `delivery_staff_form_view`, `delivery_view_kanban`, `delivery_staff_picking_search`, `delivery_staff_picking_type_form_view`: interfața personalului de livrare.
- `staff_delivery_action` și meniul `staff_delivery_menu`.
- `report_pickup_list` / `action_report_pickup_list`: raportul PDF.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`. Grupul `group_delivery_staff` este definit în `security/groups.xml`.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): completează gestionarea livrărilor prin stări/etape, util alături de distribuirea pe personal.
