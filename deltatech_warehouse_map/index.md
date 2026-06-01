# Deltatech Warehouse Map (localizat la `deltatech_warehouse_map/index.md`)

- **Nume Tehnic:** `deltatech_warehouse_map`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_warehouse_map
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warehouse_map`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul oferă o hartă vizuală a depozitului, care permite navigarea ierarhică prin amplasamentele de stoc (niveluri, linii, rafturi, polițe, celule). Pornind de la un amplasament, utilizatorul vede amplasamentele direct subordonate sub formă de rânduri, fiecare rând fiind o bară împărțită în segmente egale pentru nivelul următor, ceea ce permite o explorare rapidă în adâncime. Fiecare segment afișează gradul de ocupare al sub-amplasamentului printr-o bară de progres colorată, astfel încât utilizatorul să identifice imediat zonele aglomerate sau libere. Valoarea de afaceri constă în vizualizarea intuitivă a capacității și ocupării depozitului, facilitând planificarea spațiului și deciziile de stocare.

#### 2. Funcționalități Cheie

- Hartă generică a depozitului pentru orice amplasament (`stock.location`), în backend prin QWeb: selectarea unui amplasament și afișarea copiilor direcți ca rânduri.
- Fiecare rând este o bară pe toată lățimea, împărțită în segmente egale pentru nivelul următor (nepoți), pentru explorare rapidă în adâncime.
- Clic pe orice segment deschide vizualizarea grafică a sub-amplasamentului respectiv; un link "Back" revine la părinte.
- Ocupare vizuală pe fiecare sub-amplasament: fiecare segment conține o bară de progres internă care reprezintă procentul de ocupare.
- Praguri de culoare: verde (<60%), galben (60–90%), roșu (≥90%), cu etichete de contrast ridicat ce afișează numele și valorile `(curent/maxim)` și borduri clare între segmente.
- Urmărirea capacității și ocupării pe `stock.location`: maxim manual pentru amplasamentele frunză, maxim calculat pentru cele non-frunză (sumă a copiilor), cantitate curentă calculată și raport de ocupare = curent/maxim (protejat la împărțirea cu zero).
- Integrare în interfață: buton "Map" în vizualizarea listă a Amplasamentelor și buton inteligent "Open Map" în formular.
- Meniu: Inventar → Warehouse Map deschide rădăcina Stock în vizualizarea generică.
- Generare opțională de date demo: un hook post-init poate crea o structură ierarhică de probă sub amplasamentul Stock pentru testare rapidă.

#### 3. Dependențe

- `stock`
- `web`
- `deltatech_putaway_strategy`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, secțiunile de mai jos sunt acoperite de Funcționalitățile Cheie (secțiunea 2). Documentul Readme menționează explicit câteva detalii tehnice relevante:

**Modele**

- `stock.location`: extins cu câmpurile de capacitate și ocupare — `max_products_leaf` (manual, pentru amplasamente frunză), `max_products` (calculat, sumă a copiilor pentru amplasamentele non-frunză), `current_products` (calculat: pentru frunze, suma `quantity` din `stock.quant` cu cantitate > 0; pentru non-frunze, suma copiilor) și `occupancy_ratio` (calculat = curent/maxim, protejat la împărțirea cu zero).

**Rute (Controllers)**

- `/deltatech/warehouse_map`: harta generică a depozitului, pornind de la amplasamentul rădăcină.
- `/deltatech/warehouse_map/location/<id>`: vizualizarea grafică pentru un amplasament specific.

#### 5. Conexiuni

- `deltatech_putaway_strategy`: dependență directă care furnizează strategii de stocare; harta vizuală completează gestionarea amplasamentelor pe care se bazează aceste strategii.
- `stock`: modulul de bază pentru amplasamente (`stock.location`) și cantități (`stock.quant`) pe care se construiește harta.
