# Customer Analysis

- **Nume Tehnic:** `deltatech_customer_analysis`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_customer_analysis
- **Cale Locală:** `odoo-addons/bitshop/deltatech_customer_analysis`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un tablou de bord care îi spune fiecărui agent de vânzări ce are de făcut azi cu fiecare client din portofoliu: să sune, să încaseze sau să vândă mai mult. Citește rândurile nocturne din [Customer Segment](../deltatech_customer_segment/index.md), fără să recitească istoricul vânzărilor la fiecare filtru.

#### 2. Funcționalități Cheie

- **De făcut acum**: trei liste, *To call* (clienți care se răcesc), *To collect* (restanțele cele mai mari) și *You can sell them more* (în creștere, potențial ridicat, comenzi mici dese).
- **Decizie în cuvinte pe fiecare rând** (ex. „Collect 9.075 lei”, „Call: off his rhythm”), cu scorurile în detaliu.
- **Semnale** în loc de scoruri: creștere/scădere, produse necumpărate, zile de tăcere față de ritmul propriu, client de top, ultimul contact.
- **No longer buys**: produsele cumpărate în perioada precedentă și (aproape) necumpărate acum, cu sumele; este subiectul apelului.
- Mini-grafic pe ultimele 12 luni și ce cumpără clientul acum (produse și categorii de top).
- **Acțiuni din rând**: programează un apel pentru mâine agentului clientului, ofertă nouă, facturi de încasat, fișa clientului, rândul de segment; export CSV pe filtrul curent.
- Carduri KPI (clienți, vânzări, top, creștere, în scădere, inactivi, restanțe) care filtrează tabelul.
- Rolurile din Customer Segment: *Own customers* vede doar clienții proprii (impus pe server), *All customers* vede tot, filtrează după agent și recalculează la cerere.
- Meniu: *Vânzări > Portofoliu clienți > Customer Analysis*. Adaugă două setări în grupul Portfolio: *Lost product from* (500 implicit) și *Lost product below (%)* (30 % implicit).

#### 3. Dependențe

- [deltatech_customer_segment](../deltatech_customer_segment/index.md)
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `deltatech.customer.analysis`: model fără stocare proprie pentru serviciul tabloului de bord (interogări limitate la clienții afișați).
- `deltatech.customer.segment.config` (extins): cele două setări suplimentare pentru produsele nemaicumpărate.

**Vizualizări**

- `action_customer_analysis`: acțiune client (tablou de bord OWL).
- `view_customer_segment_config_form_analysis`: câmpurile adăugate în setările segmentării.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_customer_map](../deltatech_customer_map/index.md): harta vânzărilor, același meniu Customer Portfolio.
