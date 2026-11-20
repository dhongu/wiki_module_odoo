# Sale Qty Available (localizat la `deltatech_sale_qty_available/index.md`)

- **Nume Tehnic:** `deltatech_sale_qty_available`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_qty_available
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_qty_available`
- **Ultima Ingestie:** `2026-11-20`

#### 1. Sumar

Modulul ajută vânzătorii și personalul din depozit să vadă dintr-o privire care comenzi pot fi livrate, pe baza stocului disponibil. Comenzile deschise (oferte și comenzi confirmate) primesc un indicator „Is ready”, iar cele gata de livrare sunt evidențiate cu verde în liste, astfel încât operatorii pot prioritiza expedierile fără a deschide fiecare comandă în parte. Pe formularul comenzii, fiecare linie poate afișa o sinteză a disponibilității produsului (stoc, ieșiri și intrări prognozate), oferind context util în momentul ofertării sau confirmării.

#### 2. Funcționalități Cheie

- **Rânduri verzi:** listele de oferte și de comenzi de vânzare afișează cu verde o comandă gata de livrare; filtrul „Is Ready” din căutare returnează doar comenzile pregătite.
- **Oferte (ciornă sau trimise):** o ofertă e gata când stocul la îndemână minus cantitatea de ieșire acoperă cantitatea rămasă de livrat pe fiecare linie, sau pe cel puțin o linie când politica de livrare (`picking_policy`) este `direct`.
- **Comenzi confirmate:** o comandă e gata când transferurile ei au stoc rezervat: orice mișcare rezervată la politica `direct`, respectiv toate mișcările transferurilor neterminate în caz contrar. Comenzile rămân gata și după livrare, până la facturarea completă; cele anulate nu sunt niciodată gata.
- **Coloana „Available”:** coloană opțională pe liniile comenzii, ascunsă implicit și vizibilă pentru utilizatorii de inventar; arată prognoza (disponibil virtual) cu părțile ei (stoc la îndemână, ieșiri, intrări) sau *N/A* când toate sunt zero. Citește locația sursă din ruta liniei, dacă aceasta are una.
- Indicatorul este stocat pe comandă și poate fi căutat; la calculul cantității la dată pe linia comenzii, modulul setează cheia de context `all_warehouses`, deci se iau în calcul toate depozitele.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

Componentele de mai jos provin din analiza codului (`models/sale.py`, `views/sale_view.xml`).

**Modele**

- `sale.order` (extins): adaugă câmpul calculat și stocat `is_ready` (cu metodă de căutare proprie `_search_is_ready`) care determină dacă o comandă este pregătită de livrare — pentru comenzile în ofertă/deschise, verifică disponibilul (stoc minus ieșiri) față de cantitatea de livrat pe fiecare linie; pentru comenzile confirmate, verifică rezervarea pe transferurile de livrare (orice mișcare rezervată la politica `direct`, cantitate rezervată egală cu cea planificată în caz contrar, transferurile terminate fiind sărite).
- `sale.order.line` (extins): adaugă câmpul calculat `qty_available_text` cu o sinteză text a disponibilității produsului (disponibil virtual = stoc - ieșiri + intrări), calculată pe locația sursă a rutei liniei dacă există; supraîncarcă `_compute_qty_at_date` pentru a lua în calcul toate depozitele (`all_warehouses=True`).

**Vizualizări**

- `view_order_tree`: extinde lista comenzilor de vânzare, adăugând decorarea cu verde (`decoration-success`) pentru comenzile gata de livrare.
- `view_quotation_tree`: extinde lista de oferte cu aceeași decorare pe baza câmpului `is_ready`.
- `view_order_form`: adaugă pe liniile comenzii coloana opțională `qty_available_text`, vizibilă pentru utilizatorii de stoc.
- `view_sales_order_filter`: adaugă filtrul „Is Ready" în vizualizarea de căutare a comenzilor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- `sale_stock`: modulul standard Odoo de integrare vânzări–stoc, pe care se bazează calculul disponibilității și al rezervărilor.
