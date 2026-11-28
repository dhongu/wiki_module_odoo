# Fleet Geo Coordinates (localizat la `deltatech_fleet_geo/index.md`)

- **Nume Tehnic:** `deltatech_fleet_geo`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_fleet_geo
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fleet_geo`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă informații geografice extensiilor de flotă din `deltatech_fleet`: coordonate pentru locații, trasee și pozițiile vehiculelor.

#### 2. Funcționalități Cheie

- Latitudine, longitudine și rază pe locațiile de flotă.
- Latitudine și longitudine pentru locația de start și de sfârșit pe trasee.
- Latitudine și longitudine pe înregistrările de poziție ale vehiculelor.

#### 3. Dependențe

- [deltatech_fleet](../deltatech_fleet/index.md)

#### 4. Componente Cheie

**Modele**

- `fleet.location`, `fleet.route`, `fleet.vehicle.location`, `fleet.vehicle`: extinse cu câmpurile de coordonate.

**Vizualizări**

- `fleet_location_form`: coordonatele și raza pe locație.
- `fleet_vehicle_view_form`: coordonatele pe vehicul.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_fleet](../deltatech_fleet/index.md): modulul de bază extins.
