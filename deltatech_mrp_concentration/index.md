# MRP Concentration (localizat la `deltatech_mrp_concentration/index.md`)

- **Nume Tehnic:** `deltatech_mrp_concentration`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp_concentration
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_concentration`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul recalculează cantitatea ingredientului principal al unei rețete pornind de la concentrația dorită în produsul finit și de la concentrația ingredientului disponibil, apoi echilibrează șarja cu un diluant sau cu un subprodus. Este destinat produselor chimice, alimentare sau farmaceutice obținute prin diluarea sau concentrarea unui ingredient activ.

#### 2. Funcționalități Cheie

- **Concentrații pe lista de materiale (BoM):** câmpurile *Concentration* (a produsului finit) și *Concentration Primary* (a ingredientului principal), lângă produs. Sunt numere simple, deci se folosește aceeași unitate pentru ambele, de exemplu procente.
- **Tip de ingredient pe componente:** *Primary* (ingredientul activ), *Secondary* (diluantul) sau *Normal* (implicit, nerecalculat).
- **Recalculare pe BoM:** la schimbarea unei concentrații sau a cantității BoM, componenta *Primary* devine cantitate BoM × *Concentration* / *Concentration Primary*. Restul șarjei se echilibrează:
  - diluare (rezultatul e sub cantitatea BoM): componenta *Secondary* primește diferența;
  - concentrare (rezultatul e peste cantitatea BoM): subprodusele primesc excesul, iar *Secondary* devine zero.
- **Recalculare pe ordinul de fabricație:** ordinul afișează aceleași două câmpuri, copiate din BoM la alegerea ei; schimbarea unei concentrații sau a cantității de produs recalculează necesarul componentelor primare și secundare și al subproduselor ordinului, după aceeași regulă. Astfel concentrația reală a unui lot primit se poate folosi pentru un ordin, fără a modifica BoM-ul.
- **Unde se găsește:** *Manufacturing > Products > Bills of Materials* și *Manufacturing > Operations > Manufacturing Orders*. Subprodusele se introduc în fila *By-products* a BoM, disponibilă când opțiunea *By-Products* e activă în setările de producție.
- **Limitări:** recalcularea rulează doar la editarea formularului de BoM sau de ordin; ordinele create automat (din comandă de vânzare sau regulă de reaprovizionare) păstrează cantitățile din BoM până se modifică câmpurile pe formular. Dacă BoM-ul are mai multe subproduse, toate primesc aceeași cantitate de exces.

#### 3. Dependențe

- `base`
- `mrp`
- `stock`
- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `mrp.bom`: extins cu `concentration` și `concentration_primary` și cu recalcularea cantităților.
- `mrp.bom.line`: extins cu `ingredient_type` (Primary / Secondary / Normal).
- `mrp.production`: extins cu aceleași două câmpuri de concentrație și cu recalcularea necesarului.

**Vizualizări**

- `mrp_bom_form_view`: câmpurile de concentrație și tipul de ingredient pe formularul BoM.
- `mrp_production_form_view`: câmpurile de concentrație pe ordinul de fabricație.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): extensie de producție din aceeași suită, cu aria funcțională a listelor de materiale și a ordinelor de producție.
- [deltatech_mrp_bom_formula](../deltatech_mrp_bom_formula/index.md): ajustează tot cantitățile liniilor de BoM, dar pe baza atributelor variantei.
