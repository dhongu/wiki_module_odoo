# Warehouse Map (localizat la `deltatech_warehouse_map/index.md`)

- **Nume Tehnic:** `deltatech_warehouse_map`
- **Versiune:** `20.0.1.0.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_warehouse_map`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warehouse_map`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Într-un depozit organizat ca arbore adânc de locații (zone, linii, rafturi, polițe, celule), lista standard de locații nu arată unde mai este loc. Modulul adaugă o hartă vizuală a ierarhiei de locații, colorată după gradul de ocupare, ca să se vadă dintr-o privire ce rafturi și celule sunt pline și să se poată ajunge la produsele stocate într-o celulă.

#### 2. Funcționalități Cheie

- **Harta locației:** pentru o locație aleasă, fiecare locație copil apare ca bară, cu toți descendenții imbricați dedesubt, nivel cu nivel; clic pe numele unei locații deschide harta cu un nivel mai jos, iar butonul înapoi din antet revine la părinte.
- **Culori de ocupare:** bara se umple proporțional cu ocuparea și arată procentul și cantitatea curentă; verde sub 60%, galben între 60% și 90%, roșu de la 90%. Un tooltip arată numele complet, ocuparea și cantitatea curentă / maximă.
- **Stoc curent:** procentul și cantitatea de pe bară deschid *Current Stock* cu stocul locației și al sublocațiilor, grupat pe produs.
- **Conținutul celulei:** când locația aleasă nu are copii, harta listează produsele stocate cu cantitatea disponibilă.
- **Deschiderea hărții:** butonul **Map** de pe fiecare linie din *Inventar > Configurare > Locații* și butonul inteligent **Open Map** din formular; harta locației principale *Stock* este disponibilă și la URL-ul `/deltatech/warehouse_map`.
- **Configurare:** capacitatea vine din `deltatech_putaway_strategy`; se setează **Max products (leaf)** pe locațiile frunză (celule), iar maximul, cantitatea curentă și ocuparea părinților se însumează din copii.
- **Acces:** doar utilizatorii din grupul *Inventory / User*; se aplică drepturile de acces și regulile multi-company.
- **Limitări:** nu există intrare de meniu pentru hartă; etichetele paginii hărții sunt în română și nu sunt traduse.

#### 3. Dependențe

- `stock`
- `web`
- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md)

#### 4. Componente Cheie

Funcționalitățile sunt descrise în `readme/DESCRIPTION.md`; mai jos sunt doar elementele tehnice vizibile în modul.

**Modele**

- `stock.location` (extins): metoda `action_open_map` care deschide harta locației; câmpurile de capacitate și ocupare provin din `deltatech_putaway_strategy`.

**Vizualizări**

- `view_stock_location_tree_inherit_deltatech_map`: butonul **Map** în lista de locații.
- `view_stock_location_form_inherit_deltatech_map`: butonul inteligent **Open Map** în formular.
- `view_location_generic` și `location_recursive_node`: șabloanele QWeb ale hărții.

**Rute (Controllere)**

- `/deltatech/warehouse_map`: harta locației principale de stoc.
- `/deltatech/warehouse_map/location/<id>`: harta unei locații anume.
- `/deltatech/warehouse_map/location_open_quants/<id>`: stocul curent al unei locații și al sublocațiilor.

**Acțiuni Automate / Acțiuni Server**

- `action_location_open_quants`: acțiune de fereastră pentru *Current Stock*; nu sunt definite `ir.cron` sau reguli de automatizare.

#### 5. Conexiuni

- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md): furnizează capacitatea (maxim pe locațiile frunză) din care se calculează ocuparea.
- [deltatech_warehouse_arrangement](../deltatech_warehouse_arrangement/index.md): organizare fizică paralelă a depozitului (magazie, zonă, raft, secțiune, poliță).
