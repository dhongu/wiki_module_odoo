# Stock Auto Transfer (localizat la `deltatech_picking_transit/index.md`)

- **Nume Tehnic:** `deltatech_picking_transit`
- **Versiune:** `19.0.0.0.16`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_transit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_transit`
- **Ultima Ingestie:** `2026-11-05`

#### 1. Sumar

Modulul mută marfa între două depozite în doi pași, printr-o locație de tranzit: depozitul expeditor trimite marfa în tranzit, iar depozitul destinatar primește propriul transfer, cu aceleași produse, din tranzit în stocul său. Astfel se câștigă trasabilitate și control asupra mărfurilor aflate „în drum", cu fiecare etapă urmărită separat.

#### 2. Funcționalități Cheie

- **Tipuri de operațiune pentru cei doi pași**: pe un tip de operațiune internă se setează **Two Step Transfer Use**: *Delivery* pentru transferul care trimite marfa în locația de tranzit, *Reception* pentru transferul care o aduce din tranzit în depozitul destinatar.
- **Butonul Create Transfer**: pe un transfer intern al cărui tip e marcat *Delivery* și care nu are **Source Document**, butonul deschide un wizard în care se alege **Operation Type**-ul de recepție. Modulul creează și confirmă al doilea transfer, de la destinația primului la destinația implicită a tipului ales, cu aceleași produse și cantități. Fiecare transfer primește ca contact adresa celuilalt depozit, iar cele două sunt legate prin mesaje în chatter. Butonul dispare după ce există al doilea transfer.
- **Al doilea transfer automat**: dacă **Auto Second Transfer** e bifat pe tipul *Delivery*, al doilea transfer se creează la validarea primului, fără wizard. Depozitul destinatar este cel a cărui **Address** este **Contact**-ul transferului, și se folosește tipul său intern marcat *Reception*. Transferurile cu **Source Document** (reaprovizionare, comenzi de vânzare) sunt omise, fiindcă transferul lor de recepție există deja.
- **Verificări la recepție**: al doilea transfer se poate valida doar cu produse provenite din primul transfer sau din backorder-urile lui. Un backorder al primului transfer nu creează un nou al doilea transfer; un mesaj în chatter indică transferul care va primi produsele.
- **Reassign Location (opțional)**: când parametrul de sistem `deltatech_picking_transit.use_sub_locations` este setat, transferurile interne afișează butonul **Reassign Location**, care setează pe fiecare operațiune detaliată prima sublocație a locației sursă ce are produsul în stoc.
- **Configurare**: se creează o locație de tranzit și, în *Inventory > Configuration > Warehouse Management > Operations Types*, un tip intern în depozitul expeditor cu tranzitul ca destinație implicită (*Delivery*, opțional **Auto Second Transfer**); în depozitul destinatar un tip intern cu tranzitul ca sursă implicită (*Reception*); pentru modul automat se completează **Address** pe fiecare depozit și se folosește ca **Contact** pe transferul de livrare.
- **Limitare**: primul transfer rămâne editabil după crearea celui de-al doilea, iar modificările nu se copiază în al doilea.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului este omisă. Din structura modulului:

**Modele**

- `stock.picking` și `stock.picking.type` (extinse în `models/`): tipul de utilizare în doi pași, crearea celui de-al doilea transfer, verificările la recepție.
- Wizard de transfer în `wizard/stock_picking_transfer_wizard.py`: alegerea tipului de operațiune pentru recepție.

**Vizualizări**

- `views/stock_picking_views.xml`: extinderi ale formularului de transfer (butoanele Create Transfer și Reassign Location).
- `views/stock_picking_type_view.xml`: extinderi ale formularului tipului de operațiune (**Two Step Transfer Use**, **Auto Second Transfer**).
- `wizard/stock_picking_transfer_wizard_views.xml`: wizard-ul pentru crearea celui de-al doilea transfer.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt declarate în fișierele de date din manifest.

#### 5. Conexiuni

- `stock`: modulul extinde direct fluxul de transferuri și tipurile de operațiuni din modulul standard de stoc Odoo.
