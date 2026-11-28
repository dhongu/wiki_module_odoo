# Change Unit of measure

- **Nume Tehnic:** `deltatech_change_uom`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_change_uom
- **Cale Locală:** odoo-addons/deltatech/deltatech_change_uom
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un produs creat cu unitatea de măsură greșită este adesea deja folosit în comenzi, facturi și mișcări de stoc. Modulul adaugă acțiunea *Change Uom*, care înlocuiește unitatea pe produs și pe aceste documente dintr-un singur pas.

#### 2. Funcționalități Cheie

- **Acțiunea Change Uom** pe formularul produsului (meniul de acțiuni ⋮); fereastra arată *Unit of Measure* și *Default Purchase Unit*, iar *Apply* execută schimbarea.
- **Alegerea unităților**: *Unit of Measure* acceptă orice unitate; *Default Purchase Unit* oferă doar unități convertibile în noua unitate și se golește dacă nu se mai potrivește.
- **Documente actualizate**, pentru toate variantele: comenzi de vânzare, comenzi de achiziție, facturi, mișcări de stoc, linii de mișcare și liste de prețuri de furnizor. Liniile din vechea unitate de achiziție trec în noua unitate de achiziție implicită sau, dacă aceasta lipsește, în noua unitate.
- **Fără conversie**: cantitățile, prețurile și sumele rămân neschimbate; unitatea este doar reetichetată. Actualizarea merge direct în baza de date, deci facturile postate și perioadele blocate nu o opresc.
- Acțiunea este disponibilă doar grupului *Allow to change unit of measure* (administratorii o au implicit); necesită activarea setării Units of Measure în Inventar.
- Pașii detaliați, cu capturi, sunt în fișa consultantului.

#### 3. Dependențe

- `product`
- `account`
- `stock`
- `sale`
- `purchase`
- `deltatech_uom_domain`

#### 4. Componente Cheie

**Modele**

- `product.change.uom`: asistent (wizard) care înlocuiește unitatea de măsură pe produs și pe documentele asociate.

**Vizualizări**

- `wizard/product_change_uom_view.xml`: fereastra *Change Uom* și acțiunea de pe formularul produsului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `deltatech_uom_domain`: furnizează *Default Purchase Unit* și domeniul unităților (dependență).
