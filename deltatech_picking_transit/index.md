# Stock Auto Transfer (localizat la `deltatech_picking_transit/index.md`)

- **Nume Tehnic:** `deltatech_picking_transit`
- **Versiune:** `20.0.0.0.16`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_picking_transit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_transit`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul mută marfa între două depozite în doi pași, printr-o locație de tranzit: depozitul expeditor trimite marfa în tranzit, iar depozitul primitor primește un transfer propriu, cu aceleași produse, din tranzit în stocul său. Se câștigă trasabilitate asupra mărfii aflate în drum.

#### 2. Funcționalități Cheie

- **Tipuri de operațiune pentru cei doi pași:** pe un tip de operațiune internă, **Two Step Transfer Use** are valorile *Delivery* (transferul spre tranzit) și *Reception* (transferul din tranzit în depozitul primitor).
- **Buton Create Transfer:** pe un transfer intern de tip *Delivery*, fără **Source Document**, deschide un wizard în care se alege tipul de operațiune de recepție. Se creează și se confirmă al doilea transfer, cu aceleași produse și cantități, iar cele două transferuri sunt legate prin mesaje în chatter. Butonul dispare după crearea celui de-al doilea transfer.
- **Al doilea transfer automat:** cu **Auto Second Transfer** bifat pe tipul *Delivery*, transferul de recepție se creează la validarea primului, fără wizard. Depozitul primitor este cel a cărui **Address** este **Contact** pe transfer; transferurile cu **Source Document** sunt omise.
- **Verificări la recepție:** al doilea transfer se validează doar cu produse venite din primul transfer sau din backorder-urile lui; un backorder nu creează un nou transfer secund, ci un mesaj în chatter indică transferul care va primi produsele.
- **Reassign Location (opțional):** dacă parametrul de sistem `deltatech_picking_transit.use_sub_locations` este setat, transferurile interne arată butonul care setă, pe fiecare operațiune detaliată, prima sublocație a sursei ce are produsul în stoc.
- **Configurare:** se creează o locație de tranzit; în *Inventory > Configuration > Warehouse Management > Operations Types* se definesc tipul *Delivery* (destinație implicită tranzitul) în depozitul expeditor și tipul *Reception* (sursă implicită tranzitul) în cel primitor; pentru modul automat se completează **Address** pe fiecare depozit.
- Limitare: primul transfer rămâne editabil după crearea celui de-al doilea, iar modificările nu se copiază.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Sumarul provine din `readme/DESCRIPTION.md`.

**Modele**

- `stock.picking` (extins): crearea celui de-al doilea transfer, verificările la recepție și reasignarea locației.
- `stock.picking.type` (extins): câmpurile **Two Step Transfer Use** și **Auto Second Transfer**.

**Vizualizări**

- `views/stock_picking_views.xml`: butoanele **Create Transfer** și **Reassign Location** pe transfer.
- `views/stock_picking_type_view.xml`: câmpurile de transfer în doi pași pe tipul de operațiune.
- `wizard/stock_picking_transfer_wizard_views.xml`: wizardul de alegere a tipului de operațiune de recepție.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `stock`: extinde direct transferurile și tipurile de operațiune din modulul standard.
