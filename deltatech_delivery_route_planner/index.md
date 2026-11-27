# Delivery Route Planner (localizat la `deltatech_delivery_route_planner/index.md`)

- **Nume Tehnic:** `deltatech_delivery_route_planner`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_delivery_route_planner
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_route_planner`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Planifică livrările zilei (sau ale unei săptămâni) cu vehiculele proprii: le împarte între vehicule și ordonează opririle astfel încât mașinile să parcurgă cât mai puțini kilometri, apoi creează câte un transfer în lot (batch) pentru fiecare vehicul. Dispecerul vede traseul pe hartă, iar șoferul primește lista de opriri cu ora estimată de sosire. Modulul este în versiunea 19.0, portat din 20.0 (Beta, licență OPL-1, preț 220 EUR).

#### 2. Funcționalități Cheie

- **Asistentul „Planifică livrări”** (*Inventar → Operațiuni → Plan deliveries*): se alege data, depozitul și vehiculele disponibile; livrările de ieșire ale zilei sunt propuse pe vehicule, cu opririle în ordine, ora de sosire, încărcarea și procentul de capacitate, kilometrii și ora de întoarcere. Sunt eligibile livrările de ieșire gata sau în așteptare, programate la data aleasă și neincluse încă într-un lot.
- **Constrângeri**: sarcina utilă a categoriei de vehicul (din *Stock Transport*), lungimea maximă a articolului pe care îl poate transporta caroseria, ziua de lucru a fiecărui vehicul și intervalul de livrare al adresei. Ce nu încape este **amânat**, cu motiv (capacitate, articol prea lung, zi de lucru, lipsă coordonate).
- **Distanțe rutiere** de la propriul server OSRM (OpenStreetMap); când acesta nu răspunde, planul folosește linia dreaptă înmulțită cu un factor de drum și este marcat „estimat”. Adresele fără coordonate sunt geocodate automat.
- **Planificare pe săptămână**: se alege o perioadă, iar planificatorul stabilește și ziua fiecărei livrări, între data pregătirii mărfii și termenul promis clientului, astfel încât livrările din aceeași zonă să circule împreună. Livrările cu **dată fixă** își păstrează ziua, weekendul doar la cerere, iar cele mutate primesc noua dată programată (cu notă în chatter).
- **Optimizare** cu Google OR-Tools (rutare de vehicule cu capacități și ferestre de timp).
- **Loturi**: unul pe vehicul și zi, cu vehicul, șofer, ordinea opririlor, kilometri și durată planificate și o **hartă** cu linia traseului și opririle numerotate.
- **Recalculare rută** pe lot după ce dispecerul adaugă sau scoate o livrare; avertizează la depășirea capacității sau la întoarcere după sfârșitul programului.
- **Raport „Listă opriri”** pentru șofer: opriri, ora de sosire, adresă, telefon și greutate; pe fiecare livrare apare **Sosire planificată**.
- **Configurare** (*Inventar → Configurare → Setări → Route planning*): serverul OSRM și cheia API (header `X-Api-Key`), factorul de drum, viteza medie și timpii de descărcare pe oprire și la 100 kg. Pe vehicul, fila *Route planning*: lungimea maximă a articolului și orele de început/sfârșit ale zilei; pe adresă (*Sales & Purchase*): fereastra de livrare. Adresa depozitului trebuie să aibă coordonate, iar categoriile de vehicul au *Max Weight* completat.
- Două puncte de extensie pentru alte module: greutatea și cel mai lung articol al unei livrări.
- Necesită pachetul Python `ortools` pe server și un server OSRM propriu (nu serverul demo public în producție).

Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock_picking_batch`
- `stock_fleet`
- `base_geolocalize`
- `web_map` (Enterprise)
- Dependență externă Python: `ortools`

#### 4. Componente Cheie

**Modele**

- `delivery.route.plan` (wizard): asistentul de planificare; calculează propunerea și creează loturile.
- `delivery.route.plan.vehicle`, `delivery.route.plan.line`, `delivery.route.plan.postponed`: rezultatul propunerii (pe vehicul/zi, opririle în ordine, livrările amânate cu motiv).
- `delivery.route.solver`: optimizarea traseelor cu OR-Tools.
- `delivery.route.matrix`: matricea de distanțe/durate (OSRM sau estimare pe linie dreaptă).
- Extinderi: `stock.picking` (sosire planificată, termen, greutate, lungime articol), `stock.picking.batch` (traseu, hartă, recalculare), `fleet.vehicle`, `res.partner`, `res.config.settings`.

**Vizualizări**

- `delivery_route_plan_view_form`: formularul asistentului de planificare.
- `stock_picking_batch_form`: fila *Route* cu harta și butonul de recalculare.
- `res_config_settings_view_form`: blocul de setări *Route planning*.
- `fleet_vehicle_view_form`, `view_partner_form`, `view_picking_form`: câmpurile suplimentare pe vehicul, adresă și livrare.
- `report_route_stop_list`: lista de opriri pentru șofer.

**Acțiuni Automate / Acțiuni Server**

- `action_delivery_route_plan` (meniul *Plan deliveries*) și `action_report_route_stop_list`. Nu există acțiuni programate.

#### 5. Conexiuni

- `stock_picking_batch`: loturile create de planificator sunt transferuri în lot (dependență directă; integrat în `stock` pe Odoo 20).
- `fleet`: vehiculul, șoferul și categoria cu capacitate de greutate provin din flota Odoo.
- [deltatech_fleet](../deltatech_fleet/index.md): foile de parcurs și rutele flotei înregistrează ce s-a parcurs efectiv; planificatorul propune traseul dinainte.
