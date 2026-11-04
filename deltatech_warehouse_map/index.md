# Warehouse Map (localizat la `deltatech_warehouse_map/index.md`)

- **Nume Tehnic:** `deltatech_warehouse_map`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_warehouse_map
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warehouse_map`
- **Ultima Ingestie:** `2026-11-04`

#### 1. Sumar

Într-un depozit organizat ca arbore adânc de amplasamente (zone, linii, rafturi, polițe, celule), lista standard de amplasamente nu arată unde mai este loc. Modulul adaugă o hartă vizuală a ierarhiei de amplasamente, colorată după gradul de ocupare, astfel încât să se vadă dintr-o privire ce rafturi și celule sunt pline și să se poată coborî până la produsele stocate într-o celulă. Valoarea de afaceri constă în planificarea mai ușoară a spațiului și a deciziilor de stocare.

#### 2. Funcționalități Cheie

- **Harta amplasamentului**: pentru un amplasament ales, fiecare copil apare ca o bară, iar toți descendenții lui sunt afișați dedesubt, nivel cu nivel. Clic pe numele unui amplasament deschide harta cu un nivel mai jos; butonul înapoi din antet revine la părinte.
- **Culori de ocupare**: fiecare bară este umplută proporțional cu ocuparea amplasamentului și arată procentul și cantitatea curentă. Umplerea este verde sub 60%, galbenă între 60% și 90% și roșie de la 90%. Un tooltip arată numele complet al amplasamentului, ocuparea și cantitatea curentă / maximă.
- **Conținutul celulei**: când amplasamentul ales nu are copii, harta listează produsele stocate în el, cu cantitatea disponibilă.
- **Deschiderea hărții**: butonul **Map** de pe fiecare linie din **Inventar → Configurare → Amplasamente** și butonul inteligent **Open Map** de pe formularul amplasamentului. Harta amplasamentului principal *Stock* este disponibilă și la URL-ul `/deltatech/warehouse_map`.
- **Capacitate și ocupare** provin din `deltatech_putaway_strategy`: se setează **Max products (leaf)** pe amplasamentele frunză (celulele); maximul, cantitatea curentă și ocuparea amplasamentelor părinte se însumează din copii. Ocuparea este cantitatea disponibilă a amplasamentului împărțită la maximul lui.
- **Acces**: harta e disponibilă doar utilizatorilor din grupul *Inventory / User* (ceilalți primesc 404); se aplică drepturile de acces și regulile multi-companie pentru amplasamentele și cantitățile afișate.
- Limitări: nu există intrare de meniu pentru hartă (se deschide dintr-un amplasament sau prin URL); etichetele paginii hărții sunt în română și nu sunt traduse; linkurile de procent și cantitate de pe bare trimit la o acțiune de stoc care nu mai există în Odoo 19, deci nu deschid stocul amplasamentului.

#### 3. Dependențe

- `stock`
- `web`
- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md)

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, funcționalitățile de mai sus acoperă modulul; mai jos sunt reperele confirmate în cod.

**Modele**

- `stock.location` (extins): metoda `action_open_map`, apelată de butoanele **Map** și **Open Map**. Câmpurile de capacitate și ocupare (`max_products_leaf`, `max_products`, `current_products`, `occupancy_ratio`) sunt definite de `deltatech_putaway_strategy`, nu de acest modul.

**Vizualizări**

- `view_stock_location_tree_inherit_deltatech_map`: adaugă butonul **Map** în lista de amplasamente.
- `view_stock_location_form_inherit_deltatech_map`: adaugă butonul inteligent **Open Map** în formularul amplasamentului.
- `location_recursive_node` (șablon QWeb): desenează recursiv o bară de amplasament cu bara de progres de ocupare.
- `view_location_generic` (șablon QWeb): pagina hărții generice.

**Rute (Controllers)**

- `/deltatech/warehouse_map`: harta amplasamentului principal Stock.
- `/deltatech/warehouse_map/location/<id>`: harta unui amplasament specific.
- `/deltatech/warehouse_map/location_open_quants/<id>`: deschiderea stocului unui amplasament (linkurile de pe bare, nefuncționale pe Odoo 19, conform limitărilor din readme).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md): dependență directă care furnizează câmpurile de capacitate și ocupare pe amplasamente, pe care se bazează culorile hărții.
- `stock`: modulul de bază pentru amplasamente (`stock.location`) și cantități (`stock.quant`) pe care se construiește harta.
