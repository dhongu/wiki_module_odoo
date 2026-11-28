# Sale Delivery Status (localizat la `deltatech_sale_picking_status/index.md`)

- **Nume Tehnic:** `deltatech_sale_picking_status`
- **Versiune:** `20.0.2.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_picking_status`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_picking_status`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează starea standard de livrare a comenzii de vânzare (`delivery_status`, calculată de Odoo din transferurile de livrare) cu filtre, coloană implicită în liste și urmărire în chatter. Echipa de vânzări vede dintr-o privire cât din comandă a fost livrat, fără să deschidă fiecare transfer.

#### 2. Funcționalități Cheie

- Starea de livrare (*Not Delivered*, *Started*, *Partially Delivered*, *Fully Delivered*) afișată implicit în listele de oferte și comenzi.
- Filtre de căutare *Delivery in Progress*, *Partially Delivered* și *Fully Delivered*, plus grupare după starea de livrare.
- Schimbările de stare sunt urmărite în chatter-ul comenzii.
- Până la versiunea 19 modulul calcula propriul *Picking Status* (Done / In Progress); la actualizare, filtrele salvate, șabloanele de export și gruparea pe vechiul câmp trec pe starea standard de livrare.

#### 3. Dependențe

- `sale_stock`
- `mail_tracking`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): activează `tracking=True` pe câmpul standard `delivery_status`.

**Vizualizări**

- `view_quotation_tree_picking_status` / `view_order_tree_picking_status`: starea de livrare în listele de oferte și comenzi.
- `view_sales_order_filter_picking_status`: filtrele și gruparea după starea de livrare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, cron sau acțiuni server.

#### 5. Conexiuni

- `sale_stock`: calculează starea standard de livrare pe care o extinde modulul.
- `mail_tracking`: oferă urmărirea modificărilor în chatter.
