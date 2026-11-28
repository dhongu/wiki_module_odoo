# Sales Dashboard - Parcels

- **Nume Tehnic:** `deltatech_sale_dashboard_delivery`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_sale_dashboard_delivery
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_dashboard_delivery`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaugă coletele comenzilor de vânzare pe bordul de vânzări din `deltatech_sale_dashboard`, pe baza statusului de livrare din `deltatech_delivery_status`. Se instalează automat când ambele module sunt prezente.

#### 2. Funcționalități Cheie

- În banda **To Do Now**, după *Orders to Deliver*: **Parcels to Prepare** (livrări gata în depozit, cu curier și fără AWB), **Awaiting Courier Pickup** (AWB emis, necolectat) și **Parcels on the Way** (în tranzit, în depozitul curierului sau la livrare).
- Coletul aparține agentului și echipei comenzii, deci *My Sales*, *My Team* și *Whole Company* funcționează ca la celelalte carduri; click pe card deschide transferurile numărate.
- Se numără doar transferurile din ultimele 60 de zile (parametrul de sistem `deltatech_sale_dashboard_delivery.recent_days`, **Settings ▸ Technical ▸ System Parameters**, mod developer).
- Întârzierile față de SLA-ul curierului, retururile și ramburs se urmăresc în bordul de livrări (`deltatech_delivery_dashboard`).

#### 3. Dependențe

- [deltatech_sale_dashboard](../deltatech_sale_dashboard/index.md)
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.dashboard` (extins): cardurile de colete.

**Vizualizări**

- Nu are vizualizări proprii; cardurile apar pe **Sales ▸ Dashboard**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `deltatech_delivery_dashboard`: bordul de livrări cu SLA, retururi și ramburs.
