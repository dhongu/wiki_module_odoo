# Împărțirea livrării (Picking Split)

- **Nume Tehnic:** `deltatech_picking_split`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_picking_split
- **Cale Locală:** odoo-addons/deltatech/deltatech_picking_split
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite operatorului să decidă manual, linie cu linie, ce cantitate pleacă acum dintr-un transfer și ce rămâne într-o livrare parțială (backorder), în loc de comportamentul automat din Odoo.

#### 2. Funcționalități Cheie

- **Generare manuală de backorder:** un wizard afișează liniile transferului cu cererea (Demand) și cantitatea păstrată (Kept); pentru fiecare linie operatorul stabilește cât rămâne în transferul curent, iar restul trece în backorder.
- **Valori implicite din disponibil:** cantitatea păstrată este propusă din disponibilitatea prognozată.
- **Validări:** cantitățile păstrate sunt verificate (fiecare mișcare trebuie să aparțină transferului), iar la creare utilizatorul primește un link către backorder.
- **Atenție, bug-uri deschise (bugs.md, 2026-10-02):** PICKSPLIT-001 (UoM diferit de unitatea de stoc: prognoza nu e convertită) și PICKSPLIT-002 (cantități trimise prin RPC pot crea backorder negativ).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking.manual.backorder`: wizardul de împărțire a transferului.
- `stock.picking.manual.backorder.line`: linia wizardului (produs, mișcare, cerere, cantitate păstrată).

**Vizualizări**

- `view_manual_backorder_form`: formularul wizardului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `stock`: transferurile și backorder-urile standard pe care le împarte.
