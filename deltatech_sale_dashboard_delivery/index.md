# Sales Dashboard - Parcels (localizat la `deltatech_sale_dashboard_delivery/index.md`)

- **Nume Tehnic:** `deltatech_sale_dashboard_delivery`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_dashboard_delivery
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_dashboard_delivery`
- **Ultima Ingestie:** `2026-10-06`

#### 1. Sumar

Adaugă pe tabloul de bord de vânzări coloanele despre coletele comenzilor: ce trebuie pregătit în depozit, ce așteaptă preluarea de către curier și ce este deja pe drum. Vânzătorul vede dintr-o privire starea livrărilor comenzilor sale, pe baza statusului de livrare urmărit de modulul `deltatech_delivery_status`. Se instalează automat când ambele module sunt prezente.

#### 2. Funcționalități Cheie

În banda **To Do Now** (după cardul *Orders to Deliver*), accesibilă din **Sales ▸ Dashboard**:

- **Parcels to Prepare** — livrări pregătite în depozit (stare „Pregătit”), cu transportator și fără AWB încă.
- **Awaiting Courier Pickup** — colete cu AWB pe care curierul nu le-a preluat încă (status de livrare „pre-aviz”).
- **Parcels on the Way** — colete preluate de curier și nelivrate încă: în tranzit, în depozitul curierului sau în curs de livrare.
- Coletul aparține vânzătorului și echipei de vânzări ale comenzii, deci filtrele *My Sales*, *My Team* și *Whole Company* funcționează ca la celelalte carduri.
- Un click pe card deschide transferurile numărate.
- Se numără doar transferurile de livrare (outgoing) legate de comenzi de vânzare, necanceleate, create în ultimele 60 de zile. Un colet cu statusul needitat de luni de zile e o problemă de date, nu muncă de azi.
- Numărul de zile se configurează prin parametrul de sistem `deltatech_sale_dashboard_delivery.recent_days` (**Settings ▸ Technical ▸ System Parameters**, mod dezvoltator); implicit 60, și când lipsește sau nu e număr.
- Întârzierile față de SLA-ul curierului, returnările și rambursul se urmăresc în tabloul de bord de livrări ([deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md)).

#### 3. Dependențe

- [deltatech_sale_dashboard](../deltatech_sale_dashboard/index.md)
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.dashboard` (model abstract, extins): adaugă trei KPI-uri în `_dashboard_work_kpis` (`parcels_to_prepare`, `parcels_to_pick_up`, `parcels_on_the_way`, secvențele 45–47) peste `stock.picking`, cu domeniul de bază și parametrul de zile din `_dashboard_parcel` / `_dashboard_parcel_days`.

**Vizualizări**

- Nu are vizualizări XML proprii; cardurile apar în tabloul de bord existent, iar acțiunea deschisă este `stock.action_picking_tree_all`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_sale_dashboard_rma](../deltatech_sale_dashboard_rma/index.md): puntea soră, care adaugă pe același tablou de bord cardurile de RMA.
- [deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md): tabloul de bord de livrări, unde se urmăresc SLA, returnările și rambursul.
