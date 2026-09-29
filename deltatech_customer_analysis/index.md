# Analiză Clienți (Deltatech Customer Analysis)

- **Nume Tehnic:** `deltatech_customer_analysis`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_customer_analysis
- **Cale Locală:** `odoo-addons/bitshop/deltatech_customer_analysis`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Tablou de bord care le spune agenților de vânzări **ce au de făcut astăzi** cu fiecare client din portofoliu: să sune, să încaseze sau să vândă mai mult. Folosește rândurile calculate noaptea de modulul Segmentare Clienți și nu reparcurge istoricul vânzărilor la fiecare filtrare, deci răspunde rapid. Face parte din familia „portofoliu clienți”.

#### 2. Funcționalități Cheie

- **De făcut acum:** trei liste în partea de sus. *De sunat* (clienții care se răcesc, întâi cei care au lăsat cei mai mulți bani), *De încasat* (cele mai mari solduri restante) și *Poți vinde mai mult* (clienți în creștere, cu potențial ridicat sau cu comenzi mici și dese). Un clic pe client aduce rândul în vârful tabelului și îl deschide.
- **Decizie în cuvinte pe fiecare rând:** de exemplu „Încasează 9.075 lei”, „Sună: nu mai cumpără țeavă PPR 20 mm”, „Sună: iese din ritm”, „Propune un volum mai mare”. Scorurile rămân în detaliu.
- **Semnale în loc de scoruri:** creștere sau scădere față de perioada anterioară, numărul de produse necumpărate, „tăcut de 30 de zile, ritm 7” (din ritmul propriu de cumpărare), client de top, ultimul contact înregistrat. Coloana *Zile peste ritmul propriu* găsește cumpărătorii regulați care au tăcut.
- **Nu mai cumpără:** produsele cumpărate în perioada anterioară și (aproape) necumpărate acum, cu sumele de atunci și de acum — subiectul apelului.
- **Grafic de 12 luni** pe fiecare client și, la deschiderea rândului, ce cumpără acum (top produse și categorii).
- **Acțiuni din rând:** programează un apel mâine pentru agentul clientului (activitate cu decizia în notă), ofertă nouă, facturi de încasat, fișa clientului, rândul de segment.
- **Carduri KPI** (clienți, vânzări, top, creștere, în scădere, inactivi, restanți) care filtrează tabelul; un al doilea clic arată din nou toți clienții. Export *CSV* pentru filtrul curent.
- **Roluri din Segmentare Clienți:** *Clienții proprii* vede și acționează doar pe clienții la care e agent (impus pe server, indiferent ce trimite browserul); *Toți clienții* vede tot, filtrează pe agent și poate apăsa *Recalculează acum*.
- **Configurare** (Vânzări > Portofoliu clienți > Setări, grupul *Portofoliu*): *Produs pierdut de la* (suma minimă cumpărată în perioada anterioară, implicit 500) și *Produs pierdut sub (%)* (implicit 30 %). Datele afișate sunt cele calculate noaptea; după schimbarea setărilor se apasă *Recalculează acum*.
- Doar trei interogări rulează live (vânzări lunare pentru grafic, produse pierdute, top produse la deschiderea rândului), limitate pe dată și pe clienții afișați; numără aceleași linii ca motorul nocturn. Nu adaugă câmpuri pe modele standard.

Meniu: *Vânzări > Portofoliu clienți > Analiză Clienți*. Pașii detaliați sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_customer_segment](../deltatech_customer_segment/index.md)
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.customer.analysis` (model abstract): datele tabloului (`get_dashboard_data`, `get_partner_details`), deciziile și semnalele, verificarea accesului pe rol, acțiunile `action_schedule_call`, `action_open_invoices`, `action_recompute`.
- `deltatech.customer.segment.config` (extins): adaugă `lost_product_min_amount` și `lost_product_ratio_pct` (cu validare).

**Vizualizări**

- `action_customer_analysis` / `menu_customer_analysis`: acțiune client și meniu pentru tablou (componentă OWL în `static/src/dashboard/`).
- `view_customer_segment_config_form`: extinde formularul setărilor de segmentare cu grupul *Portofoliu*.

**Acțiuni Automate / Acțiuni Server**

- Niciuna; cifrele vin din cronul nocturn al `deltatech_customer_segment`.

#### 5. Conexiuni

- [deltatech_sale_missions](../deltatech_sale_missions/index.md): misiuni de vânzare (F3), depinde de acest modul.
- [deltatech_customer_segment](../deltatech_customer_segment/index.md): sursa rândurilor nocturne, a rolurilor și a setărilor (F1).
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md): cardurile KPI din partea de sus a tabloului.
