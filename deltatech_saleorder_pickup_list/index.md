# Sale Order Pickup List (localizat la `deltatech_saleorder_pickup_list/index.md`)

- **Nume Tehnic:** `deltatech_saleorder_pickup_list`
- **Versiune:** `20.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_saleorder_pickup_list`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_saleorder_pickup_list`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaugă pe comenzile de vânzare un raport specializat „Listă de ridicare” (Pickup List), care ușurează munca din depozit: oferă o listă clară a articolelor de scos din stoc pentru comenzile alese, reducând erorile de culegere și crescând viteza de pregătire a comenzilor.

#### 2. Funcționalități Cheie

- Raport dedicat de ridicare pe comanda de vânzare, cu informațiile de care are nevoie cine culege marfa: produs, cantitate și amplasare.
- Integrare cu `sale_stock` și [deltatech_stock_inventory](../deltatech_stock_inventory/index.md) pentru informații de stoc corecte; echipa de inventar identifică rapid articolele de ridicat.
- Machetă simplă și ușor de citit, pentru mai puține greșeli la culegere.
- Utilizare: din **Sales > Orders** se deschid sau se selectează una ori mai multe comenzi, din meniul **Print** se alege „Lista de ridicare”, iar PDF-ul se tipărește pentru depozit.

#### 3. Dependențe

- `sale_stock`
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)

#### 4. Componente Cheie

Secțiunea se bazează pe `readme/DESCRIPTION.md`; verificarea codului a confirmat doar elementele de mai jos.

**Modele**

- Modulul nu definește modele Python; adaugă un raport tipăribil pe `sale.order`.

**Vizualizări**

- Șabloanele QWeb ale raportului (container și document), definite în `views/sale_order.xml`.

**Acțiuni Automate / Acțiuni Server**

- `action_report_saleorder_pickup_list`: acțiune `ir.actions.report` pe `sale.order`, denumită „Lista de ridicare”, disponibilă din meniul Print.

#### 5. Conexiuni

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): furnizează informațiile de amplasare din depozit și datele de inventar folosite în raport.
