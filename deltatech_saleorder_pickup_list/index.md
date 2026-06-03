# Deltatech Sale Order Pickup List (localizat la `deltatech_saleorder_pickup_list/index.md`)

- **Nume Tehnic:** `deltatech_saleorder_pickup_list`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_saleorder_pickup_list`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_saleorder_pickup_list`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul adaugă un raport specializat de tip **Listă de ridicare** (Pickup List) pentru comenzile de vânzare din Odoo. Scopul său este să simplifice activitatea din depozit, oferind o listă clară și ușor de urmărit cu produsele ce trebuie ridicate din stoc pentru o comandă de vânzare. Astfel, echipa de logistică identifică rapid articolele de pregătit, reducând erorile de culegere și îmbunătățind fluxul de lucru în depozit.

#### 2. Funcționalități Cheie

- **Raport dedicat de ridicare**: adaugă o acțiune de raport **Listă de ridicare** pe comanda de vânzare, accesibilă din meniul de tipărire.
- **Informații utile pentru culegător**: raportul afișează denumirea produsului, cantitatea și amplasarea în depozit (raft, rând, cutie).
- **Integrare cu stocul**: funcționează împreună cu modulele `sale_stock` și [deltatech_stock_inventory](../deltatech_stock_inventory/index.md) pentru informații de stoc corecte.
- **Layout simplu și clar**: format ușor de citit, gândit să minimizeze erorile de culegere și să crească productivitatea în depozit.

#### 3. Dependențe

- `sale_stock`
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)

#### 4. Componente Cheie

**Modele**

Modulul nu definește modele Python noi; extinde funcțional `sale.order` prin adăugarea unui raport tipăribil.

**Vizualizări**

- `report_saleorder_pickup_list`: șablonul QWeb container al raportului Listă de ridicare, care iterează peste comenzile selectate.
- `report_saleorder_document_pickup_list`: șablonul QWeb al documentului propriu-zis; afișează antetul comenzii (partener, referințe, agent) și un tabel cu liniile comenzii — imagine produs, descriere, cantitate și amplasarea în depozit (`loc_rack` / Raft, `loc_row` / Rând, `loc_case` / Cutie).

**Acțiuni Automate / Acțiuni Server**

- `action_report_saleorder_pickup_list`: acțiune `ir.actions.report` de tip `qweb-pdf` pe modelul `sale.order`, denumită „Lista de ridicare", legată ca raport (`binding_type="report"`) și disponibilă din meniul de tipărire al comenzilor de vânzare.

#### 5. Conexiuni

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): furnizează informațiile de amplasare în depozit (raft, rând, cutie) și datele de inventar folosite în raport.
