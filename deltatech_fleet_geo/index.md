# Deltatech Fleet Geo (localizat la `deltatech_fleet_geo/index.md`)

- **Nume Tehnic:** `deltatech_fleet_geo`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_fleet_geo
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fleet_geo`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă informații geografice (coordonate) la extensiile de flotă din `deltatech_fleet`. Locațiile, rutele și pozițiile vehiculelor pot fi astfel identificate pe hartă, ca bază pentru urmărirea și analiza deplasărilor. Modulul este în stadiu Beta.

#### 2. Funcționalități Cheie

- Latitudine, longitudine și rază pe locațiile de flotă (`fleet.location`); latitudinea și longitudinea apar în formularul locației, după câmpul „Tip”. Raza (implicit 1.0) este definită pe model, dar nu este afișată în formular.
- Latitudine și longitudine pentru punctul de plecare și cel de sosire al rutelor; valorile sunt câmpuri related, preluate din locațiile de plecare/sosire (nu se introduc direct pe rută) și sunt afișate în formularul rutei.
- Latitudine și longitudine pe înregistrările de locație ale vehiculelor (`fleet.vehicle.location`), doar la nivel de model (fără vizualizare dedicată).
- Buton „Get location” în formularul vehiculului, înainte de câmpul Stare. Metoda `action_get_location` este deocamdată un stub (nu face nimic) — pregătit pentru o viitoare integrare cu un serviciu de poziționare.

#### 3. Dependențe

- [deltatech_fleet](../deltatech_fleet/index.md)

#### 4. Componente Cheie

**Modele**

- `fleet.location` (extins): câmpurile `lat`, `lng` (precizie 9,6) și `radius`.
- `fleet.vehicle.location` (extins): câmpurile `lat`, `lng`.
- `fleet.route` (extins): câmpurile related `from_lat`, `from_lng`, `to_lat`, `to_lng` din `from_loc_id` / `to_loc_id`.
- `fleet.vehicle` (extins): metoda `action_get_location` (stub).

**Vizualizări**

- `fleet_location_form`: extinde formularul locației din `deltatech_fleet` cu `lat` și `lng`.
- `fleet_route_form`: extinde formularul rutei din `deltatech_fleet` cu coordonatele de plecare și sosire.
- `fleet_vehicle_view_form`: extinde formularul `fleet.vehicle` cu butonul „Get location”.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_fleet](../deltatech_fleet/index.md): modulul de bază ale cărui locații și rute sunt extinse cu coordonate.
- `fleet`: modulul standard Odoo a cărui vizualizare de vehicul este extinsă (fără pagină wiki).
- Dependența comentată `web_map` în manifest indică o posibilă afișare pe hartă, neactivă în prezent.
