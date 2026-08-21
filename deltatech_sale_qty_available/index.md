# Sale Qty Available (localizat la `deltatech_sale_qty_available/index.md`)

- **Nume Tehnic:** `deltatech_sale_qty_available`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_qty_available`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_qty_available`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul ajută echipa de vânzări să vadă rapid care comenzi pot fi livrate imediat, pe baza stocului disponibil. În lista de comenzi de vânzare, comenzile care sunt gata de livrare sunt evidențiate cu verde, astfel încât operatorii pot prioritiza expedierile fără a deschide fiecare comandă în parte. Pe formularul comenzii, fiecare linie poate afișa o sinteză a disponibilității produsului (stoc, ieșiri și intrări prognozate), oferind context util în momentul ofertării sau confirmării.

#### 2. Funcționalități Cheie

- Evidențierea cu verde a comenzilor „gata de livrare" în listele de comenzi și de oferte de vânzare.
- Indicator „Is ready" (gata) calculat în funcție de starea comenzii, statusul de facturare, politica de livrare (livrare directă sau completă) și stocul disponibil/rezervat, atât pentru comenzi în ofertă cât și pentru comenzi confirmate (unde se verifică suplimentar rezervarea pe transferurile de livrare).
- Filtru dedicat „Is Ready" pentru a afișa doar comenzile pregătite de expediere.
- Coloană opțională cu textul disponibilității pe linia de comandă, ce arată disponibilul virtual, stocul curent, ieșirile și intrările prognozate (calculat pe locația din ruta liniei, dacă este definită).

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

> Sumarul și funcționalitățile au fost sintetizate din `__manifest__.py` și din cod, întrucât `readme/DESCRIPTION.md` este minimal. Componentele de mai jos provin din analiza codului.

**Modele**

- `sale.order` (extins): adaugă câmpul calculat și stocat `is_ready` (cu metodă de căutare proprie `_search_is_ready`) care determină dacă o comandă este pregătită de livrare — pentru comenzile în ofertă/deschise, verifică disponibilul (stoc minus ieșiri) față de cantitatea de livrat pe fiecare linie; pentru comenzile confirmate, verifică dacă transferurile de livrare au cantitatea rezervată/efectuată egală cu cea planificată.
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
