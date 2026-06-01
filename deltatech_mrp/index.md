# MRP Extension (localizat la `deltatech_mrp/index.md`)

- **Nume Tehnic:** `deltatech_mrp`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul extinde funcționalitatea standard de producție (MRP) din Odoo pentru a oferi un control mai precis asupra costurilor de fabricație. Principala valoare de business constă în includerea automată a cheltuielilor indirecte în costul produselor fabricate, prin adăugarea unui coeficient procentual peste costul materialelor (de exemplu, un adaos de 20% pentru costuri indirecte). În plus, modulul rafinează modul de calcul al cantităților la explozia listei de materiale, gestionează automat loturile de producție și pune la dispoziție un raport dedicat pentru analiza costurilor de producție.

#### 2. Funcționalități Cheie

- Adăugarea unui câmp de procent pentru cheltuieli indirecte (`value_overhead`) pe lista de materiale (BOM), care permite includerea costurilor indirecte în costul produsului finit.
- Rotunjirea cantităților la explozia listei de materiale (BOM) în conformitate cu definiția unității de măsură.
- Ajustarea procesului de confirmare a comenzii de producție (modificarea metodei de confirmare și a datelor estimate pentru mișcările de stoc generate).
- Generarea automată a unui lot de producție pentru produsele gestionate pe loturi.
- Afișarea cantității disponibile pe liniile de produse din comanda de producție, cu actualizare la schimbarea produsului.
- Raport dedicat pentru analiza costurilor de producție.

#### 3. Dependențe

- `base`
- `mrp`
- `stock`
- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `mrp.bom`: extins cu câmpul `value_overhead` (procent pentru cheltuieli indirecte) și logica de rotunjire a cantităților la explozia BOM.
- `mrp.production`: ajustat la confirmarea comenzii, la datele estimate ale mișcărilor de stoc și pentru generarea automată a lotului de producție.
- `mrp.production.product.line`: extins cu cantitatea disponibilă și logica `onchange_product_id`.
- `deltatech.mrp.report`: model de raportare pentru analiza costurilor de producție.

**Vizualizări**

- `views/mrp_view.xml`: ajustări ale interfețelor pentru lista de materiale și comenzile de producție.
- `views/product_view.xml`: ajustări ale vizualizărilor de produs relevante pentru costuri.
- `report/deltatech_mrp_report.xml`: definirea raportului de analiză a costurilor de producție.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server dedicate în modul.

#### 5. Conexiuni

- `mrp`: modulul standard de producție pe care acest modul îl extinde.
- `stock`: gestionarea mișcărilor de stoc și a loturilor generate de comenzile de producție.
- `product`: definirea produselor și a listelor de materiale.
