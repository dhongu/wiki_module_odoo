# Purchase picking status

- **Nume Tehnic:** `deltatech_purchase_picking_status`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_picking_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_picking_status`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Agenții de achiziții care primesc marfa în mai multe livrări trebuie să vadă dintr-o privire care comenzi de achiziție mai așteaptă marfă. Modulul adaugă pe comanda de achiziție un *Delivery Status*, calculat din recepțiile comenzii, astfel încât nu mai e nevoie să deschidă fiecare transfer în parte.

#### 2. Funcționalități Cheie

- **Statusul livrării:** este *In Progress* cât timp o recepție a comenzii nu este nici finalizată, nici anulată, și *Done* când toate recepțiile sunt finalizate sau anulate.
- **Comenzi fără recepții:** o comandă confirmată fără recepții, de exemplu una de servicii, este *Done*; înainte de confirmare este *In Progress*.
- **Insignă și coloană:** statusul apare ca insignă (badge) pe formularul comenzii și ca o coloană, vizibilă implicit, în listele de cereri de ofertă și de comenzi de achiziție.
- **Filtre:** două filtre de căutare, *Done* și *In progress*, selectează comenzile după statusul livrării.
- **Actualizare automată:** statusul nu este stocat și urmărește comanda imediat ce este confirmată sau când o recepție este validată ori anulată.
- **Drepturi și comenzi anulate:** modulul nu adaugă grupuri, deci oricine vede comenzile de achiziție vede și statusul. O comandă anulată urmează aceeași regulă: fără recepții afișează *In Progress*.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): câmpul calculat, nestocat și căutabil `picking_status` (*Delivery Status*: `done` / `in_progress`), cu urmărire în chatter; `_compute_picking_status` aplică regulile de mai sus, iar `_search_picking_status` reproduce aceeași regulă ca domeniu de căutare (inclusiv pentru comenzile anulate).

**Vizualizări**

- `view_purchase_form_picking_status`: insigna *Delivery Status* pe formularul comenzii, după câmpul `origin`.
- `view_rfq_tree_picking_status` și `view_purchase_tree_picking_status`: coloana-insignă în listele de cereri de ofertă și de comenzi de achiziție.
- `view_purchase_order_filter_picking_status`: filtrele *Done* și *In progress* în căutarea comenzilor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `purchase_stock`: modulul standard care leagă comenzile de achiziție de recepțiile din stoc, din care se calculează statusul.
