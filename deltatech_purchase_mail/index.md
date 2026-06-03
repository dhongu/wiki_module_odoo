# Achiziții: Trimitere comenzi multiple pe email cu XLSX (localizat la `deltatech_purchase_mail/index.md`)

- **Nume Tehnic:** `deltatech_purchase_mail`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_mail`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_mail`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul adaugă o funcție avansată de trimitere prin email pentru modulul de Achiziții din Odoo. Permite echipelor de aprovizionare să selecteze mai multe comenzi de achiziție și să le transmită simultan furnizorilor sau persoanelor interesate din companie, însoțite de un sumar agregat în format XLSX și de atașamentele PDF individuale ale fiecărei comenzi. Astfel se reduce semnificativ efortul manual în operațiunile de achiziție cu volum mare.

#### 2. Funcționalități Cheie

- **Trimitere în lot pe email**: adaugă o acțiune dedicată **Send Multi Orders** în vizualizarea de tip listă a comenzilor de achiziție, permițând expedierea simultană a mai multor comenzi.
- **Sumar XLSX automat**: generează și atașează automat un fișier Excel (XLSX) cu detaliile cheie din toate comenzile selectate, oferind o privire de ansamblu agregată asupra lotului de achiziții.
- **Atașamente PDF individuale**: include în emailul de ieșire rapoartele PDF oficiale ale fiecărei comenzi de achiziție selectate, pentru confirmare formală.
- **Șabloane de email personalizabile**: folosește un șablon de email dedicat, ușor de adaptat la standardele de comunicare ale companiei.

#### 3. Dependențe

- `purchase`
- `mail`

#### 4. Componente Cheie

**Modele**

- `purchase.send.xlsx.wizard`: vrăjitor (wizard) care orchestrează compunerea emailului, generarea sumarului XLSX agregat și atașarea PDF-urilor pentru comenzile de achiziție selectate.
- `purchase.order`: model extins pentru a expune logica de trimitere a mai multor comenzi pe email.

**Vizualizări**

- `purchase_order_actions.xml`: definește acțiunea **Send Multi Orders by Email** disponibilă din meniul Action al listei de comenzi de achiziție.

**Acțiuni Automate / Acțiuni Server**

- `data/mail_template.xml`: șablonul de email folosit pentru transmiterea comenzilor multiple.

#### 5. Conexiuni

- [deltatech_fast_purchase](../deltatech_fast_purchase/index.md): extinde fluxul de achiziții din aceeași suită deltatech.
- [deltatech_purchase_price](../deltatech_purchase_price/index.md): completează modulul de achiziții cu logică de prețuri.
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md): extensie pe comenzile de achiziție.
