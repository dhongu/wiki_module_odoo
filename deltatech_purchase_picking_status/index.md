# Purchase Picking Status (localizat la `deltatech_purchase_picking_status/index.md`)

- **Nume Tehnic:** `deltatech_purchase_picking_status`
- **Versiune:** `20.0.2.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_picking_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_picking_status`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul completează statusul standard de recepție al comenzii de achiziție (Nerecepționat, Parțial recepționat, Complet recepționat), calculat de Odoo din recepții. Un agent de achiziții vede stadiul recepțiilor direct în listele de cereri de ofertă și comenzi, le poate filtra și grupa după el, iar schimbările de status rămân în istoricul comenzii.

#### 2. Funcționalități Cheie

- Statusul de recepție este afișat implicit în listele de cereri de ofertă și de comenzi de achiziție.
- Filtre de căutare *Recepție în curs*, *Parțial recepționat* și *Complet recepționat*, plus grupare după statusul de recepție.
- Schimbările de status sunt urmărite (tracking) în chatter-ul comenzii.
- Până la versiunea 19 modulul calcula propriul „Delivery Status” (Done / In Progress); la actualizare, filtrele salvate, șabloanele de export și gruparea pe câmpul vechi sunt mutate pe statusul standard de recepție.

#### 3. Dependențe

- `purchase_stock`
- `mail_tracking`

#### 4. Componente Cheie

Descrierea modulului (`readme/DESCRIPTION.md`) nu detaliază componente tehnice individuale; analiza suplimentară a codului a fost omisă conform schemei.

**Modele**

- `purchase.order`: câmpul standard `receipt_status` primește `tracking=True`.

**Vizualizări**

- `view_rfq_tree_picking_status`, `view_purchase_tree_picking_status`: coloana de status în liste.
- `view_purchase_order_filter_picking_status`: filtrele de căutare după statusul recepției.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki.
