# Delivery Tracking Dashboard

- **Nume Tehnic:** `deltatech_delivery_dashboard`
- **Versiune:** `20.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_dashboard
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dashboard`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un rând de carduri cu indicatori (KPI) deasupra listei de AWB-uri, astfel încât cine urmărește coletele să vadă dintr-o privire ce necesită atenție și să ajungă cu un clic la lista din spatele fiecărui număr. Cardurile folosesc doar datele deja colectate de `deltatech_delivery` (starea livrării raportată de curieri), fără câmpuri noi pe livrări sau comenzi.

#### 2. Funcționalități Cheie

- Carduri: **În tranzit**, **Livrate azi** (fusul orar al utilizatorului), **Întârziate** (peste SLA-ul curierului, în zile lucrătoare de la predare; fără SLA, N zile de la data AWB), **La timp, 4 săptămâni** (procent livrat în SLA în ultimele 28 de zile, apare când un curier are SLA), **Risc retur ≥ N zile** (colet la sediu/locker/în livrare de N zile sau mai mult), **Returnate luna aceasta**, **Ramburs pe drum** (total pe monedă) și **Fără urmărire** (colete în tranzit a căror stare nu mai este interogată).
- Clic pe un card filtrează lista exact pe ce a numărat cardul; clic pe alt card înlocuiește filtrul, al doilea clic îl șterge. Filtrele de curier, text și dată rămân active.
- Cardurile se suprapun intenționat (un colet la locker o săptămână e și *Întârziat*, și la *Risc retur*).
- Meniu: *Inventar → Operațiuni → Delivery AWB → Delivery Tracking*, listă deschisă pe *În tranzit*; coloana *Days with Courier*; acțiuni pe selecție *View Order* și *Resume Status Polling*. Se listează doar AWB-ul curent al unei livrări.
- Configurare: *Delivery SLA (business days)* pe metoda de livrare (curier), cu *SLA Due Date* calculat pe AWB; parametri de sistem `delivery_dashboard.overdue_days` (implicit 5) și `delivery_dashboard.return_risk_days` (implicit 3). Cronul de status din `deltatech_delivery` trebuie să rămână activ; în multi-company fiecare companie își vede doar AWB-urile (necesită `deltatech_delivery` 20.0.6.8.1+).
- Disponibil utilizatorilor de inventar (*Inventory / User*). Flux detaliat: vezi fișa consultant.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `delivery.awb` (extins): starea, data stării, data predării, data scadentă SLA și indicatorul de AWB curent.
- `delivery.carrier` (extins): SLA-ul de livrare în zile lucrătoare.
- `stock.picking` (extins).

**Vizualizări**

- `view_delivery_awb_dashboard_list` / `view_delivery_awb_dashboard_search` / `action_delivery_awb_dashboard`: lista AWB cu cardurile KPI și filtrele.
- `view_delivery_carrier_form_dashboard`: câmpul SLA pe metoda de livrare.

**Acțiuni Automate / Acțiuni Server**

- Nu definește cronuri proprii; se bazează pe cronul de status din `deltatech_delivery`.

#### 5. Conexiuni

- [deltatech_delivery_handover](../deltatech_delivery_handover/index.md): o predare confirmată datează predarea pe AWB, pornește SLA-ul și numără coletul ca predat azi.
