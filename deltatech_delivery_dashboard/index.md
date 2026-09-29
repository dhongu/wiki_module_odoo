# Delivery Tracking Dashboard (localizat la `deltatech_delivery_dashboard/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dashboard`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dashboard
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dashboard`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o bandă de carduri KPI deasupra listei de AWB-uri de livrare, astfel încât cine urmărește expedierile să vadă dintr-o privire ce colete cer atenție azi — fără să filtreze manual lista. Fiecare card numără AWB-urile aflate într-o anumită situație (în tranzit, livrate azi, întârziate față de SLA-ul transportatorului, cu risc de retur, returnate luna asta, cu ramburs pe drum sau fără urmărire), iar un click pe card filtrează lista exact pe ce a numărat cardul respectiv. Modulul folosește doar datele deja colectate de `deltatech_delivery` (starea livrării raportată de curier) și nu adaugă câmpuri noi pe livrări sau comenzi; câmpurile noi stau pe AWB, iar transportatorul primește un SLA de livrare.

#### 2. Funcționalități Cheie

- Opt carduri KPI: **În tranzit**, **Livrate azi** (de la miezul nopții, în fusul orar al utilizatorului), **Întârziate**, **La timp, 4 săptămâni**, **Risc retur ≥ N zile**, **Retururi luna asta**, **Ramburs pe drum** (un total per monedă de încasare) și **Fără urmărire** (colete în tranzit al căror status nu mai este interogat — curierul nu mai răspunde sau sunt mai vechi de 30 de zile).
- **SLA de livrare per transportator**, în zile lucrătoare (luni–vineri, sărbătorile legale nu se scad), de la predarea coletului la curier; se setează pe transportator (*Inventar → Configurare → Livrare → Metode de expediere*). Predarea = primul eveniment al curierului care pune coletul în tranzit, la oficiul curierului sau în livrare; fiecare AWB primește o dată-limită SLA (coloană ascunsă implicit în listă). Modificarea SLA-ului recalculează doar coletele aflate încă pe drum; valoarea 0 lasă transportatorul pe pragul în zile de mai jos.
- **Întârziat** = predat curierului și nelivrat după data-limită SLA; pentru un transportator fără SLA, după N zile de la data AWB-ului.
- **La timp, 4 săptămâni**: ponderea coletelor livrate în SLA în ultimele 28 de zile și câte au întârziat; apare doar când cel puțin un transportator are SLA, iar click-ul listează livrările întârziate. Rezultatul (*SLA Result*) se înregistrează o singură dată, la livrare, deci o schimbare ulterioară a SLA-ului nu rescrie istoricul.
- Coloana **Zile la curier** în listă: de la preluarea coletului de către curier (altfel de la data AWB), până acum cât e pe drum, sau până la livrare/retur când s-a încheiat.
- Tooltip-ul cardurilor **Întârziat** și **Ramburs pe drum** arată defalcarea pe transportator (ex. „GLS: 812”), cel mai mare primul.
- Click pe un card filtrează lista de AWB-uri pe exact ce a numărat cardul; un click pe alt card înlocuiește filtrul, un al doilea click pe același card îl șterge. Filtrele de transportator, text și dată deja setate se păstrează.
- Lista se deschide implicit pe **În tranzit** (coletele încă la curier), nu pe tot istoricul; click pe card șterge filtrul și arată toate AWB-urile.
- Cardurile se suprapun intenționat (un colet la locker de o săptămână e și „Întârziat”, și „Risc retur”) — fiecare răspunde la propria întrebare, nu se adună.
- Doar AWB-ul curent al livrării este listat; un AWB retrimis după o anulare își păstrează vechiul AWB, care nu mai este numărat.
- Data „în stare din” este data evenimentului raportat de curier (nu ora interogării): un colet livrat seara și interogat după miezul nopții contează ca livrat în seara respectivă.
- Pragurile din parametrii de sistem (*Setări → Tehnic → Parametri de sistem*): `delivery_dashboard.overdue_days` (implicit 5 zile, pentru transportatori fără SLA) și `delivery_dashboard.return_risk_days` (implicit 3 zile).
- Cifrele sunt la fel de bune ca stările raportate de curieri: cronul de interogare a stărilor din `deltatech_delivery` trebuie să rămână activ.
- Într-o bază multi-companie, fiecare companie vede doar propriile AWB-uri (necesită `deltatech_delivery` 19.0.6.8.1 sau mai nou).
- Accesibil din *Inventar → Operațiuni → Delivery AWB → Delivery Tracking*, pentru utilizatorii cu grupul Inventar / Utilizator; grupul e verificat și de cererea care calculează cardurile.
- Fluxul complet pas-cu-pas de configurare și testare este detaliat în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `delivery.awb` (extindere): adaugă `delivery_state` (stocat, pentru performanță — cardurile numără direct pe `delivery.awb`), `delivery_state_date` (data intrării în starea curentă), `is_current` (AWB-ul curent al livrării), `cod_currency_id` (moneda rambursului), `handover_date` (predarea la curier), `sla_due_date` (data-limită SLA), `sla_result` (rezultatul SLA la livrare), `days_with_courier` și câmpul tehnic `dashboard_bucket`, căutabil, pe care se bazează filtrele cardurilor. Metoda `get_delivery_dashboard` furnizează datele cardurilor.
- `delivery.carrier` (extindere): adaugă `delivery_sla_days` (SLA de livrare în zile lucrătoare); la modificare recalculează data-limită a coletelor aflate pe drum.
- `stock.picking` (extindere): la schimbarea reală a `delivery_state`, actualizează data stării pe AWB-urile livrării cu data evenimentului curierului (nu data interogării).

**Vizualizări**

- `view_delivery_awb_dashboard_list`: listă de AWB-uri cu coloane relevante urmăririi (transportator, client, telefon, stare, dată, zile la curier, ramburs) și butoane pentru deschiderea livrării, vizualizarea comenzii și reluarea interogării de stare.
- `view_delivery_awb_dashboard_search`: filtrele de căutare, câte unul pentru fiecare card, toate pe `dashboard_bucket` — un card și lista pe care o deschide nu pot fi în dezacord.
- `view_delivery_carrier_form_dashboard`: adaugă pe formularul transportatorului câmpul „Delivery SLA (business days)”.
- `action_delivery_awb_dashboard` / `menu_delivery_awb_dashboard`: acțiunea și meniul „Delivery Tracking” din *Inventar → Operațiuni*, restricționate la `stock.group_stock_user`.

**Acțiuni Automate / Acțiuni Server**

- Nu definește acțiuni automate; `pre_init_hook` creează și populează în SQL coloanele noi din `delivery_awb` la instalare, iar migrarea 19.0.1.1.0 setează predarea coletelor aflate pe drum la data AWB-ului.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): sursa stărilor de livrare și a cronului de interogare a curierilor pe care se bazează toate cardurile.
- `deltatech_web_kpi_cards`: componentele de carduri KPI partajate cu celelalte tablouri de bord din suite.
