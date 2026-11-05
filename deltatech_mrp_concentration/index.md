# MRP Concentration (localizat la `deltatech_mrp_concentration/index.md`)

- **Nume Tehnic:** `deltatech_mrp_concentration`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_concentration
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_concentration`
- **Ultima Ingestie:** `2026-11-05`

#### 1. Sumar

Modulul recalculează cantitatea ingredientului principal dintr-o rețetă pornind de la concentrația dorită în produsul finit și de la concentrația ingredientului disponibil, apoi echilibrează lotul cu un diluant sau cu un produs secundar. Este destinat produselor chimice, alimentare sau farmaceutice obținute prin diluarea sau concentrarea unui ingredient activ.

#### 2. Funcționalități Cheie

- **Concentrații pe lista de materiale (BoM)**: formularul BoM primește două câmpuri lângă produs, *Concentration* (a produsului finit) și *Concentration Primary* (a ingredientului principal). Sunt numere simple, deci se folosește aceeași unitate pentru ambele (de ex. procente).
- **Tip de ingredient pe componente**: fiecare linie de componentă are *Ingredient Type*: *Primary* (ingredientul activ), *Secondary* (diluantul) sau *Normal* (implicit, nu se recalculează).
- **Recalculare pe BoM**: la modificarea oricărei concentrații sau a cantității din BoM, cantitatea componentei *Primary* devine cantitate BoM × *Concentration* / *Concentration Primary*. Restul lotului se echilibrează:
  - diluare (rezultatul e sub cantitatea BoM): componenta *Secondary* primește diferența;
  - concentrare (rezultatul e peste cantitatea BoM): produsele secundare (by-products) primesc excesul, iar componenta *Secondary* devine zero.
- **Recalculare pe comanda de producție (MO)**: formularul MO afișează aceleași două câmpuri, copiate din BoM la alegerea acesteia. Modificarea unei concentrații sau a cantității de produs recalculează necesarul componentelor principală și secundară și al produselor secundare ale comenzii, cu aceeași regulă; astfel concentrația reală a unui lot primit se poate folosi pentru o singură comandă, fără a modifica BoM-ul.
- **Unde se găsește**: *Manufacturing > Products > Bills of Materials* pentru BoM și *Manufacturing > Operations > Manufacturing Orders* pentru comenzi. Produsele secundare se introduc în fila *By-products* a BoM-ului, disponibilă când opțiunea *By-Products* e activată în setările Manufacturing.
- **Limitări**: recalcularea rulează doar la editarea formularului de BoM sau de MO; comenzile create automat (din comandă de vânzare sau regulă de reaprovizionare) nu primesc concentrațiile și păstrează cantitățile din BoM până când câmpurile sunt modificate pe formular. Când BoM-ul are mai multe produse secundare, toate primesc aceeași cantitate în exces.

#### 3. Dependențe

- `base`
- `mrp`
- `stock`
- `sale`
- `product`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune este omisă, Readme-ul nu o solicită explicit. Verificare punctuală în cod: modelele extinse sunt `mrp.bom` (câmpurile `concentration`, `concentration_primary`), `mrp.bom.line` (`ingredient_type`) și `mrp.production`; vizualizările sunt în `views/mrp_bom_view.xml` și `views/mrp_production_view.xml`. Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

Nu există legături funcționale verificate cu alte module cu pagină wiki, dincolo de dependențele de mai sus.
