# MRP Extension (localizat la `deltatech_mrp/index.md`)

- **Nume Tehnic:** `deltatech_mrp`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul completează producția (MRP) standard din Odoo cu o analiză detaliată a costurilor de fabricație. Pe fiecare comandă de producție se calculează automat, dintr-o vizualizare SQL, valoarea consumurilor din stoc grupată pe categorii de cost (materii prime, semifabricate, ambalaje), la care se adaugă un coeficient fix de 20% pentru cheltuieli indirecte. Rezultatele sunt disponibile atât direct pe comanda de producție (pagina „Costs"), cât și într-un raport dedicat de analiză a costurilor de producție, util managerilor de producție pentru a înțelege structura reală a costului produselor fabricate.

**Notă de corecție:** `readme/DESCRIPTION.md` din modul descrie o versiune mai veche a funcționalității (câmp `value_overhead` pe lista de materiale, rotunjire cantități la explozia BOM, generare automată de lot, câmp de cantitate disponibilă pe liniile de produs din comanda de producție). Codul curent (19.0.1.0.4) nu mai conține aceste elemente — view-urile aferente sunt comentate în `views/mrp_view.xml`, iar modelele `mrp.bom` și `mrp.production.product.line` nu mai sunt extinse. Secțiunile de mai jos reflectă funcționalitatea reală din cod, nu conținutul DESCRIPTION.md.

#### 2. Funcționalități Cheie

- Categorisirea costurilor de producție pe categorii (materii prime, semifabricate, materiale de ambalare) prin câmpul `cost_categ` adăugat pe categoria de produs.
- Calcul automat, printr-o vizualizare SQL (`deltatech.cost.detail`), al valorii consumurilor de stoc validate ale unei comenzi de producție, grupate pe categoria de cost.
- Pagina „Costs" pe formularul comenzii de producție, cu lista detaliată a costurilor și un buton „Update" pentru recalcularea acestora.
- Raport dedicat „Production Cost Analysis" (pivot/listă/grafic), care compară cantitatea și valoarea planificată cu cea efectivă, calculează valoarea consumurilor pe categorie și aplică un coeficient de 20% peste costul consumat pentru a estima costul de producție și prețul unitar efectiv.
- Regulă de acces multi-companie pentru raportul de costuri de producție.

#### 3. Dependențe

- `base`
- `mrp`
- `stock`
- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `deltatech.cost.detail` (`_auto=False`, vizualizare SQL): agregă valoarea mișcărilor de stoc validate ale unei comenzi de producție, grupată pe categoria de cost a produsului.
- `mrp.production`: extins cu câmpul calculat `cost_detail_ids` (liniile de cost asociate) și metoda `recompute_cost_detail` pentru recalcularea acestora.
- `product.category`: extins cu câmpul de selecție `cost_categ` (Materii prime / Semifabricate / Materiale de ambalare).
- `deltatech.mrp.report` (`_auto=False`, vizualizare SQL): model de raportare pentru analiza costurilor de producție — combină cantitățile/valorile planificate și efective cu valoarea consumurilor pe categorie și aplică coeficientul de 20% pentru cheltuieli indirecte (`val_prod`, `actually_price`).

**Vizualizări**

- `views/mrp_view.xml`: adaugă pagina „Costs" (cu lista `cost_detail_ids` și butonul de recalculare) pe formularul comenzii de producție; conține și vizualizări vechi comentate (nu mai sunt active).
- `views/product_view.xml`: adaugă câmpul `cost_categ` pe formularul categoriei de produs.
- `report/deltatech_mrp_report.xml`: listă, grafic, pivot, filtru de căutare, acțiune și meniu (`Production Cost Analysis`, sub raportarea MRP) pentru modelul `deltatech.mrp.report`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server dedicate în modul.

#### 5. Conexiuni

- `mrp`: modulul standard de producție ale cărui comenzi și consumuri de stoc sunt sursa datelor de cost.
- `stock`: mișcările de stoc validate (`stock.move`) stau la baza calculului valorii consumurilor.
- `product`: categoria de produs este extinsă cu clasificarea costurilor folosită în agregări.
