# Deltatech Fleet

- **Nume Tehnic:** `deltatech_fleet`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_fleet
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fleet`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul extinde aplicația Flotă din Odoo cu foi de parcurs (fișe de traseu), jurnale de alimentare cu carburant și carduri de combustibil. Permite urmărirea rutelor, a kilometrilor parcurși și a consumului pe vehicul și pe perioadă, inclusiv calculul automat al nivelului de combustibil din rezervor și un raport al costului pe kilometru.

#### 2. Funcționalități Cheie

- Date suplimentare pe vehicul: indicativ, șofer de rezervă, categorie de vehicul (M1, N1, O1 etc.), serie motor, capacitate de încărcare, masă utilă, capacitatea rezervorului, consum mediu (urban / extraurban / mixt), viteză medie, detalii de proprietate și alocare, carduri de combustibil.
- Carduri de combustibil: alocare pe vehicule și pe alimentări.
- Jurnal de alimentări: intrări de alimentare per vehicul, legate de cardul de combustibil și de foaia de parcurs; nivelul din rezervor se calculează la momentul alimentării.
- Rute și locații: locații, distanțe și durate de parcurs între ele, cu creare dintr-un click a rutei inverse.
- Foi de parcurs: jurnale de rute și de alimentări per vehicul și perioadă, kilometraj la început/sfârșit, distanță totală, consum normat, nivel rezervor la început și la sfârșit, raport PDF.
- Calcul automat al nivelului de combustibil din alimentări și din consumul normat al rutelor parcurse.
- Raport de cost pe kilometru per vehicul și perioadă.
- Raport de distanțe (wizard) pe vehicule.

Sursă: `readme/DESCRIPTION.md`.

#### 3. Dependențe

- `fleet`

#### 4. Componente Cheie

**Modele**

- `fleet.map.sheet`: foaia de parcurs, cu jurnale de rute și de alimentări.
- `fleet.route.log`: jurnal de rută parcursă în foaia de parcurs.
- `fleet.route`, `fleet.location`: rute și locații cu distanțe și durate.
- `fleet.vehicle.log.fuel`, `fleet.fuel`: alimentări cu carburant.
- `fleet.card`: card de combustibil.
- `fleet.reservoir.level`: nivelul din rezervor.
- `fleet.vehicle.category`, `fleet.scope`, `fleet.division`: nomenclatoare (categorie vehicul, scop, divizie).
- `fleet.vehicle.location`: locația vehiculului.
- `fleet.distance.report`, `fleet.distance.report.line`: wizard de raport distanțe.
- Extinse: `fleet.vehicle`, `fleet.vehicle.odometer`, `fleet.vehicle.cost.report`, `fleet.service.type`.

**Vizualizări**

- Vizualizări de listă, formular, calendar, gantt și grafic pentru foi de parcurs, jurnale de rute, alimentări, rute, locații și carduri; meniuri în Flotă (date de bază).
- `report_map_sheet`: raportul PDF al foii de parcurs.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Datele includ secvența `fleet.map.sheet`, tipul de serviciu pentru combustibil și locația implicită „acasă".

#### 5. Conexiuni

- `fleet`: aplicația standard extinsă de modul.
