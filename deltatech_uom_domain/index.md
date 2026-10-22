# UoM Domain by Reference (localizat la `deltatech_uom_domain/index.md`)

- **Nume Tehnic:** `deltatech_uom_domain`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_uom_domain
- **Cale Locală:** `odoo-addons/deltatech/deltatech_uom_domain`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Până în Odoo 18, un document accepta orice unitate de măsură din categoria unității produsului (de exemplu „10 buc" pentru orice produs în bucăți). Odoo 19 a eliminat categoriile și cere legarea fiecărei unități, manual, de fiecare produs în parte, ceea ce nu e realist pe cataloage mari. Modulul reface comportamentul dinainte de 19.0 pe fluxul de achiziție și readuce o unitate implicită de achiziție pe produs: lista de unități conține orice unitate convertibilă la unitatea produsului. În plus, pe linia de furnizor împiedică alegerea unei unități dintr-un alt arbore de conversie (de exemplu mililitri pentru un produs în metri).

#### 2. Funcționalități Cheie

- Pe liniile comenzilor de achiziție și ale facturilor de achiziție, lista de unități include toate unitățile din același arbore de referință cu unitatea produsului (criteriul intern `uom.uom._has_common_reference()`, care ține locul vechii categorii). Un produs în bucăți oferă „Duzina", „10 buc", „100 buc", dar nu „kg".
- Pe linia de furnizor (lista de prețuri a furnizorului) se restrânge alegerea la unitatea produsului, ambalajele lui (`uom_ids`) și unitățile din același arbore. Standardul nu are niciun domeniu aici și accepta tăcut conversii fără sens (ex. 22,5 m devenind 22.500 ml pe cererea de ofertă).
- Pentru cazuri precum metrul liniar se recomandă o unitate proprie (ex. „mlin.", cu referința „m" și raport 1), care apare automat la toate produsele în metri.
- Ce calculează standardul se păstrează: unitatea produsului, `uom_ids` și unitatea de pe linia de furnizor rămân în listă. Pe comenzi și facturi modulul doar adaugă.
- Facturile de vânzare rămân intenționat cu domeniul standard: e-Factura și e-Transport folosesc `_get_unece_code()`, care cade pe `C62` pentru unitățile fără cod UNECE, deci cantitatea transmisă către ANAF ar fi falsă. Dacă unitatea e necesară și la vânzări, mai întâi se mapează un cod UNECE real (`deltatech_uom_unece`).
- Pe produs, în tab-ul Achiziție, câmpul „Unitate implicită de achiziție" (`purchase_uom_id`) înlocuiește `uom_po_id`, dispărut în 19.0. Fără el, comanda ia unitatea doar de pe linia de furnizor valabilă la data comenzii, iar dacă linia lipsește, a expirat sau e pentru alt furnizor, pune tăcut unitatea produsului (ex. cherestea cumpărată la mc intrată în stoc la buc). Lista permisă conține unitatea produsului, ambalajele lui și unitățile din același arbore.
- Când unitatea implicită e completată, linia de furnizor nouă o preia automat și nu se mai poate alege alta; pe comanda de achiziție linia o preia la alegerea produsului și rămâne fixă, chiar dacă linia de furnizor lipsește sau a expirat. Liniile de furnizor existente nu se modifică; dacă au altă unitate, se corectează manual împreună cu prețul.
- Nu acoperă: multiplul din regula de reaprovizionare și codurile de bare pe ambalaj (citesc `product.uom_ids`), vânzările, mișcările de stoc, rebutul și eCommerce, lăsate neatinse intenționat.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `deltatech.uom.domain.mixin` (abstract): logica comună; determină rădăcina arborelui de unități a produsului (prin `parent_path`) și adaugă la lista permisă toate unitățile din arbore, cu un singur `search` per rădăcină.
- `purchase.order.line` (extins): `_compute_allowed_uom_ids` extins cu unitățile din același arbore (sau doar unitatea implicită de achiziție a produsului, dacă există); `_suggest_quantity` aplică unitatea implicită.
- `product.template` (extins): câmpul `purchase_uom_id` („Unitate implicită de achiziție"), domeniu calculat `purchase_allowed_uom_ids` și constrângere care interzice o unitate din alt arbore decât cea a produsului.
- `account.move.line` (extins): `_compute_allowed_uom_ids` extins doar pentru documentele de achiziție.
- `product.supplierinfo` (extins): câmp nou `allowed_uom_ids` și domeniu pe `product_uom_id`, limitat la unitatea produsului, `uom_ids` și arborele ei; suportă și linii pe șablon, fără variantă.

**Vizualizări**

- `product_template_form_view`: moștenește `purchase.view_product_supplier_inherit` și adaugă în tab-ul Achiziție câmpul „Unitate implicită de achiziție" (vizibil cu grupul `uom.group_uom`).
- Domeniul unităților pe comenzi, facturi și linii de furnizor se aplică prin câmpurile calculate ale modelelor.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_uom_unece](../deltatech_uom_unece/index.md): mapare coduri UNECE, necesară dacă se dorește extinderea unităților și pe documentele de vânzare transmise la ANAF.
- `stock`: mișcarea de stoc generată de o achiziție se convertește în unitatea produsului (`stock.propagate_uom` dezactivat).
