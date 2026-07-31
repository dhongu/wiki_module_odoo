# Products Category User Group (localizat la `deltatech_product_category_group/index.md`)

- **Nume Tehnic:** `deltatech_product_category_group`
- **Versiune:** `19.0.1.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_category_group`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_category_group`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul leagă categoriile de produse de grupurile de utilizatori Odoo, astfel încât fiecare categorie de produs să aibă un „responsabil de echipă" implicit. Pe această bază, transferurile de stoc (`stock.picking`) își pot atribui automat responsabilul, echilibrând volumul de lucru între utilizatorii din grupul asociat categoriei produselor din transfer. Valoarea de business este operațională: elimină atribuirea manuală a responsabilului pe fiecare transfer și distribuie automat sarcinile de pregătire a comenzilor între operatorii de depozit competenți pentru acel tip de produs.

#### 2. Funcționalități Cheie

- Grup de utilizatori (User Group) pe categoria de produs.
- Atribuire automată a responsabilului pe transfer, pe baza grupului de utilizatori asociat categoriei produselor din linia de transfer.

#### 3. Dependențe

- `product`
- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea Componente Cheie este omisă deoarece fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit analiza codului.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate în cod către alte module cu pagină wiki proprie, în afara dependențelor directe (`product`, `stock`).
