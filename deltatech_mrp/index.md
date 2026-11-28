# MRP Extension (localizat la `deltatech_mrp/index.md`)

- **Nume Tehnic:** `deltatech_mrp`
- **Versiune:** `20.0.1.0.10`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Comanda de producție standard din Odoo arată costul componentelor doar ca total. Modulul împarte valoarea componentelor consumate pe categorii de cost (materii prime, semifabricate, materiale de ambalare) și adaugă o analiză a costului de producție, care compară valoarea consumată cu cantitatea produsă. Este util managerilor de producție pentru a înțelege structura reală a costului produselor fabricate.

#### 2. Funcționalități Cheie

- **Categorie de cost pe categoria de produs:** câmpul **Cost Category** clasifică produsele din categorie ca *Raw materials*, *Semi-products* sau *Packing Material*. Se setează la *Inventory > Configuration > Products > Categories*. Componentele a căror categorie nu are categorie de cost intră în totalul consumat, dar în nicio coloană din împărțire.
- **Fila „Costs" pe comanda de producție:** listează valoarea componentelor consumate, grupată pe categorii de cost; se numără doar mișcările de componente efectuate. Butonul **Update** reîmprospătează lista.
- **Raport „Production Cost Analysis"** (*Manufacturing > Reporting*; pivot, listă, grafic), per comandă de producție:
  - cantitatea planificată și valoarea ei la costul produsului (*Qty Plan*, *Val Plan*), cantitatea și valoarea produse (*Qty Efective*, *Val Efective*);
  - valoarea consumată, total și pe categorii (*Val Consumed*, *Val Consumed Raw*, *Val Consumed Packing*, *Val Consumed Semifinish*);
  - valoarea producției (*Value production*) = valoarea consumată + 20% cheltuieli indirecte, costul unitar rezultat (*Actually Price*) lângă costul produsului (*Price Standard*);
  - starea și disponibilitatea comenzii.
- Filtre pentru comenzi curente, în producție, finalizate, în așteptare de marfă și gata de produs; grupări pe categorie, produs, comandă, stare, companie și lună. Raportul se deschide pe comenzile finalizate din luna anterioară.
- **Limitare:** coeficientul de 20% pentru cheltuieli indirecte este fix în raport și nu se poate configura.
- Acces multi-companie pe modelele de cost și de raport.

#### 3. Dependențe

- `base`
- `mrp`
- `stock`
- `stock_account`
- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `deltatech.cost.detail` (`_auto=False`, vizualizare SQL): agregă valoarea mișcărilor de stoc efectuate ale unei comenzi de producție, grupată pe categoria de cost.
- `mrp.production`: extins cu câmpul calculat `cost_detail_ids` și metoda de recalculare a costurilor.
- `product.category`: extins cu câmpul de selecție `cost_categ`.
- `deltatech.mrp.report` (`_auto=False`, vizualizare SQL): model de raportare pentru analiza costurilor de producție.

**Vizualizări**

- `views/mrp_view.xml`: fila „Costs" pe formularul comenzii de producție.
- `views/product_view.xml`: câmpul `cost_categ` pe formularul categoriei de produs.
- `report/deltatech_mrp_report.xml`: listă, grafic, pivot, filtre, acțiune și meniu pentru raportul de analiză a costurilor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `mrp`: comenzile de producție și consumurile sunt sursa datelor de cost.
- `stock`: mișcările de stoc efectuate stau la baza valorii consumurilor.
- `product`: categoria de produs poartă clasificarea costurilor.
