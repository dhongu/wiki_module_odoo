# Delivery Tracking Dashboard (localizat la `deltatech_delivery_dashboard/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dashboard`
- **Versiune:** `19.0.1.8.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dashboard
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dashboard`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o bandă de carduri KPI deasupra listei de AWB-uri de livrare, astfel încât cine urmărește expedierile să vadă dintr-o privire ce colete cer atenție azi, fără să filtreze manual lista. Fiecare card numără AWB-urile aflate într-o anumită situație, iar un click pe card filtrează lista exact pe ce a numărat cardul. Pentru colete întârziate, cu risc de retur sau fără AWB, modulul programează automat activități de alertă, ca cineva să sune curierul sau clientul înainte ca coletul să se întoarcă. Înainte ca ștafeta să ajungă la curier, un al doilea tablou, **Shipping Desk**, ajută depozitul să urmărească livrările de expediat. Modulul folosește doar datele deja colectate de `deltatech_delivery` (starea livrării raportată de curier) și nu adaugă câmpuri noi pe livrări sau comenzi; câmpurile noi stau pe AWB, iar transportatorul primește un SLA de livrare.

#### 2. Funcționalități Cheie

- Nouă carduri KPI pe lista de AWB-uri: **În tranzit**, **Livrate azi** (de la miezul nopții, în fusul orar al utilizatorului), **Întârziate**, **La timp, 4 săptămâni**, **Risc retur ≥ N zile**, **Retururi luna asta**, **Ramburs pe drum** (un total per monedă de încasare), **Fără AWB** și **Fără urmărire** (colete în tranzit al căror status nu mai este interogat: curierul nu mai răspunde sau sunt mai vechi de 30 de zile).
- **SLA de livrare per transportator**, în zile lucrătoare (luni–vineri, sărbătorile legale nu se scad), de la predarea coletului la curier; se setează pe transportator (*Inventar → Configurare → Livrare → Metode de expediere*). Predarea = primul eveniment al curierului care pune coletul în tranzit, la oficiul curierului sau în livrare; fiecare AWB primește o dată-limită SLA (coloană ascunsă implicit). Modificarea SLA-ului recalculează doar coletele aflate încă pe drum; valoarea 0 lasă transportatorul pe pragul în zile de mai jos.
- **Întârziat** = predat curierului și nelivrat după data-limită SLA; pentru un transportator fără SLA, după N zile de la data AWB-ului.
- **La timp, 4 săptămâni**: ponderea coletelor livrate în SLA în ultimele 28 de zile și câte au întârziat; apare doar când cel puțin un transportator are SLA, iar click-ul listează livrările întârziate. Rezultatul se înregistrează o singură dată, la livrare, deci o schimbare ulterioară a SLA-ului nu rescrie istoricul.
- **Fără AWB**: livrări validate pentru un curier care emite AWB-uri și rămase fără AWB după o perioadă de grație, în cele 30 de zile urmărite de cronul de stare; tipurile standard Odoo „Preț fix” și „Pe bază de reguli” sunt excluse. Click-ul deschide Shipping Desk pe cardul *Fără AWB* (singurul card care nu filtrează lista de AWB-uri, fiindcă nu există AWB de listat).
- **Alerte prin activități**: coletele din *Întârziat* și *Risc retur* primesc o activitate **Delivery Alert** pe livrare, iar livrările din *Fără AWB* o activitate **Delivery without AWB**; câte una per livrare, închise automat când coletul e livrat/returnat, respectiv când se emite AWB-ul. Alertele se scriu în limba și fusul orar ale utilizatorului căruia îi sunt atribuite; fiecare tip de activitate poate fi arhivat independent. Se atribuie utilizatorului implicit al tipului de activitate, altfel responsabilului livrării, altfel agentului de vânzări al comenzii (fără niciunul, livrarea e sărită).
- **Shipping Desk** (*Inventar → Operațiuni → Delivery AWB → Shipping Desk*), partea depozitului, pe livrările de ieșire până la preluarea de către curier, cu șase carduri care filtrează lista: **Gata de expediere** (implicit; livrări pregătite, cu transportator, neamânate și fără AWB), **Întârziate**, **Amânate**, **Fără AWB**, **Neridicate** (AWB emis de peste `pickup_wait_hours` ore și coletul încă neluat de curier: sunați curierul) și **Predate azi**. Are listă și meniu proprii; listele standard de transferuri rămân neatinse.
- Coloana **Zile la curier** în listă (de la preluarea coletului, altfel de la data AWB, până acum sau până la livrare/retur) și coloana **Următoarea activitate** a livrării, colorată după termen; filtre *Cu alertă* și *Cu activitate deschisă*.
- Tooltip-ul cardurilor **Întârziat** și **Ramburs pe drum** arată defalcarea pe transportator, cel mai mare primul.
- Click pe un card filtrează lista pe exact ce a numărat cardul; un click pe alt card înlocuiește filtrul, al doilea click pe același card îl șterge; filtrele de transportator, text și dată se păstrează. Lista de AWB-uri se deschide implicit pe **În tranzit**.
- Cardurile se suprapun intenționat (un colet la locker de o săptămână e și „Întârziat”, și „Risc retur”). Doar AWB-ul curent al livrării este listat.
- Pragurile, în parametri de sistem (*Setări → Tehnic → Parametri de sistem*): `delivery_dashboard.overdue_days` (5), `delivery_dashboard.without_awb_hours` (2), `delivery_dashboard.pickup_wait_hours` (24), `delivery_dashboard.return_risk_days` (3).
- Cronul **Delivery: Alerts for overdue and uncollected parcels** rulează la 4 ore; pentru a trimite toate alertele unei singure persoane, se setează un *Utilizator implicit* pe tipul de activitate (*Setări → Tehnic → Tipuri de activități*). Cifrele sunt la fel de bune ca stările raportate de curieri: cronul de stare din `deltatech_delivery` trebuie să rămână activ.
- Într-o bază multi-companie, fiecare companie vede doar propriile AWB-uri (necesită `deltatech_delivery` 19.0.6.8.1 sau mai nou). Dashboardul și meniurile sunt accesibile utilizatorilor Inventar / Utilizator.
- Fluxul complet pas-cu-pas de configurare și testare este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.awb` (extindere): `delivery_state` (stocat), `delivery_state_date`, `is_current`, `cod_currency_id`, `handover_date`, `sla_due_date`, `sla_result`, `days_with_courier`, câmpuri înrudite cu livrarea (client, telefon, activitate următoare) și câmpurile căutabile `dashboard_bucket` și `dashboard_alert`, pe care se bazează filtrele cardurilor. `get_delivery_dashboard` furnizează datele cardurilor; `_cron_dashboard_alerts` programează și închide activitățile de alertă.
- `delivery.carrier` (extindere): `delivery_sla_days`; la modificare recalculează data-limită a coletelor aflate pe drum.
- `stock.picking` (extindere): `shipping_bucket` (căutabil) și `get_shipping_dashboard` pentru cardurile Shipping Desk; la schimbarea reală a `delivery_state` actualizează data stării pe AWB-uri cu data evenimentului curierului (nu data interogării).

**Vizualizări**

- `view_delivery_awb_dashboard_list` / `view_delivery_awb_dashboard_search`: lista de urmărire a AWB-urilor și filtrele câte unul pe card, toate pe `dashboard_bucket`; `action_delivery_awb_dashboard` și meniul „Delivery Tracking”.
- `view_shipping_desk_list` / `view_shipping_desk_search`: lista și filtrele Shipping Desk pe `stock.picking`; `action_shipping_desk` și `menu_shipping_desk`.
- `view_delivery_carrier_form_dashboard`: câmpul „Delivery SLA (business days)” pe transportator.
- Componentele OWL ale cardurilor, în `static/src/dashboard/` (pe baza `deltatech_web_kpi_cards`), plus tururi de test pentru ambele tablouri.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_delivery_dashboard_alerts`: la 4 ore, programează activitățile *Delivery Alert* și *Delivery without AWB* și le închide când motivul dispare.
- Tipuri de activitate: `mail_activity_type_delivery_alert`, `mail_activity_type_delivery_without_awb`.
- `pre_init_hook` creează și populează în SQL coloanele noi din `delivery_awb` la instalare; migrarea 19.0.1.1.0 setează predarea coletelor aflate pe drum la data AWB-ului.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): sursa stărilor de livrare și a cronului de interogare a curierilor, pe care se bazează toate cardurile.
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md): componentele de carduri KPI partajate cu celelalte tablouri de bord.
