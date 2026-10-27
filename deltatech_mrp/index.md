# MRP Extension (localizat la `deltatech_mrp/index.md`)

- **Nume Tehnic:** `deltatech_mrp`
- **Versiune:** `19.0.1.0.9`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp`
- **Ultima Ingestie:** `2026-10-27`

#### 1. Sumar

Modulul completează producția (MRP) standard din Odoo cu o analiză detaliată a costurilor de fabricație. Pentru fiecare comandă de producție se calculează automat, dintr-o vizualizare SQL, valoarea consumurilor din stoc grupată pe categorii de cost (materii prime, semifabricate, ambalaje), la care se adaugă un coeficient fix de 20% pentru cheltuieli indirecte. Rezultatele sunt disponibile pe comanda de producție (pagina „Costs”) și într-un raport dedicat de analiză a costurilor de producție, util managerilor de producție pentru a înțelege structura reală a costului produselor fabricate.

**Notă de corecție:** `readme/DESCRIPTION.md` și rezumatul din manifest descriu o versiune mai veche a funcționalității (câmp `value_overhead` pe lista de materiale, rotunjire cantități la explozia BOM, generare automată de lot, cantitate disponibilă pe liniile de produs). Codul 19.0 nu mai conține aceste elemente: vizualizările aferente sunt comentate în `views/mrp_view.xml`, iar `mrp.bom` și `mrp.production.product.line` nu mai sunt extinse. Pagina reflectă funcționalitatea reală din cod. Singurul element păstrat din DESCRIPTION.md este coeficientul de 20% pentru costurile indirecte, fixat în raport.

#### 2. Funcționalități Cheie

- Clasificarea costurilor pe categorii (materii prime, semifabricate, materiale de ambalare) prin câmpul `cost_categ` de pe categoria de produs.
- Calcul automat al valorii consumurilor de stoc validate ale unei comenzi de producție, grupate pe categoria de cost (`deltatech.cost.detail`).
- Pagina „Costs” pe formularul comenzii de producție, cu lista costurilor pe categorii și butonul „Update” pentru recalculare.
- Raportul „Production Cost Analysis” (listă, pivot, grafic), accesibil din meniul de raportare al producției: compară cantitatea și valoarea planificată cu cele efective, afișează valoarea consumată pe categorii (materii prime, ambalaje, semifabricate), aplică un coeficient de 20% peste costul consumat pentru valoarea producției (`val_prod`) și calculează prețul unitar efectiv (`actually_price`).
- Raportul folosește stările Odoo 19 (Draft, Confirmed, In Progress, To Close, Done, Cancelled) și coloana „MO Readiness”; filtrele „Ready to Produce” și „Waiting Goods” se bazează pe disponibilitatea componentelor, iar „In Production” pe comenzile în desfășurare.
- Cantitatea planificată se convertește în unitatea de măsură a produsului când unitatea comenzii diferă de cea a produsului.
- Regulă multi-companie pe raport și pe detaliul de costuri; detaliul de costuri este vizibil doar utilizatorilor de Producție și de Inventar, iar raportul oricărui utilizator intern.

#### 3. Dependențe

- `base`
- `mrp`
- `stock`
- `stock_account`
- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `deltatech.cost.detail` (`_auto=False`, vizualizare SQL): suma valorii mișcărilor de stoc validate (`stock_move.value`) ale materiilor prime consumate de o comandă de producție, pe categoria de cost; expune și compania comenzii.
- `mrp.production` (extins): câmpul calculat `cost_detail_ids` și metoda `recompute_cost_detail`.
- `product.category` (extins): câmpul de selecție `cost_categ` (Raw materials / Semi-products / Packing Material).
- `deltatech.mrp.report` (`_auto=False`, vizualizare SQL): analiza costurilor de producție; cantități și valori planificate și efective, consumuri pe categorii, valoarea producției cu coeficientul de 20% și prețul efectiv.

**Vizualizări**

- `deltatech_mrp_production_form_view`: adaugă pagina „Costs” pe formularul comenzii de producție (restul vizualizărilor din `views/mrp_view.xml` sunt comentate).
- `views/product_view.xml`: adaugă `cost_categ` pe formularul categoriei de produs.
- `view_deltatech_mrp_report_list`, `view_deltatech_mrp_report_graph`, `view_deltatech_mrp_report_pivot`, `view_deltatech_mrp_report_filter`: listă, grafic, pivot și căutare pentru raportul de costuri.
- `action_deltatech_mrp_report` și `menu_deltatech_mrp_report_list`: acțiunea și meniul „Production Cost Analysis”, sub raportarea MRP.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `mrp`: comenzile de producție și consumurile lor sunt sursa datelor de cost.
- `stock`: mișcările de stoc validate stau la baza valorii consumurilor.
- `product`: categoria de produs poartă clasificarea costurilor.
