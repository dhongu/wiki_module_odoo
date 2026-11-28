# Fleet Map Sheets & Fuel (localizat la `deltatech_fleet/index.md`)

- **Nume Tehnic:** `deltatech_fleet`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_fleet
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fleet`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde aplicația Fleet cu foi de parcurs (fișe de traseu), jurnale de combustibil și carduri de combustibil. Permite evidența consumului și a kilometrilor pe vehicul și pe perioadă, cu raport PDF.

#### 2. Funcționalități Cheie

- Date suplimentare pe vehicul: indicativ, șofer de rezervă, categorie, serie motor, capacitate de masă, masă utilă, capacitate rezervor, consum mediu (urban / exterior / mixt), viteză medie, proprietate și alocare, carduri de combustibil.
- Carduri de combustibil alocate vehiculelor și alimentărilor.
- Jurnale de combustibil: alimentări pe vehicul, legate de card și de foaia de parcurs; nivelul rezervorului se calculează la momentul alimentării.
- Locații, distanțe și durate între ele, cu creare dintr-un clic a traseului invers.
- Foi de parcurs: jurnale de traseu și de combustibil pe vehicul și perioadă, odometru la început și sfârșit, distanță totală, consum normat, nivel rezervor la început și sfârșit, raport PDF.
- Calcul automat al nivelului din rezervor din alimentări și din consumul normat al traseelor.
- Raport de cost pe kilometru pe vehicul și perioadă.

#### 3. Dependențe

- `fleet`

#### 4. Componente Cheie

**Modele**

- `fleet.map.sheet`: foaia de parcurs.
- `fleet.route`, `fleet.route.log`, `fleet.location`, `fleet.vehicle.location`: trasee și locații.
- `fleet.fuel`, `fleet.vehicle.log.fuel`, `fleet.card`, `fleet.reservoir.level`: combustibil și carduri.
- `fleet.distance.report`, `fleet.distance.report.line`: raport de distanțe.
- `fleet.vehicle.category`, `fleet.scope`, `fleet.scope.categ`, `fleet.division`: clasificări.
- `fleet.vehicle`, `fleet.vehicle.odometer`, `fleet.vehicle.cost.report`, `fleet.service.type`: extinse.

**Vizualizări**

- `fleet_map_sheet_gantt`, `fleet_map_sheet_calendar`, `fleet_map_sheet_graph`, `fleet_map_sheet_list_report`: foile de parcurs.
- `view_fleet_distance_report_form`, `view_fleet_distance_report_line_tree`: raportul de distanțe.
- `fleet_vehicle_log_fuel_view_graph`: graficul alimentărilor.
- `report_map_sheet`: raportul PDF al foii de parcurs.

**Acțiuni Automate / Acțiuni Server**

- Niciuna (doar secvențele foii de parcurs și categoriile de vehicule din date).

#### 5. Conexiuni

- [deltatech_fleet_geo](../deltatech_fleet_geo/index.md): adaugă coordonate geografice pe locații și trasee.
