# Purchase Picking Status (localizat la `deltatech_purchase_picking_status/index.md`)

- **Nume Tehnic:** `deltatech_purchase_picking_status`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_picking_status`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_picking_status`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul **Purchase Picking Status** adaugă pe comanda de achiziție un indicator sintetic al stadiului livrărilor asociate, calculat automat pe baza transferurilor de stoc (pickings) legate de acea comandă. Astfel, un agent de achiziții poate vedea dintr-o privire dacă o comandă este complet recepționată/finalizată sau dacă mai are livrări în curs, fără a fi nevoit să deschidă fiecare transfer în parte.

#### 2. Funcționalități Cheie

- Adaugă statusul de livrare (picking status) pe comanda de achiziție
- Marchează statusul ca **Done** (finalizat) atunci când toate transferurile asociate sunt în stare `done` sau `cancel`
- Marchează statusul ca **In Progress** (în curs) atunci când cel puțin un transfer asociat nu este încă în stare `done` sau `cancel`

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru modele, vizualizări și acțiuni automate a fost omisă, deoarece Readme-ul este prezent și nu solicită explicit această analiză.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale documentate către alte module cu pagină în wiki.
