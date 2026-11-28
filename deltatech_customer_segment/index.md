# Customer Segment

- **Nume Tehnic:** `deltatech_customer_segment`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_customer_segment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_customer_segment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În fiecare noapte modulul calculează, pentru fiecare client și companie, unde se află clientul în portofoliul de vânzări: ritmul de cumpărare, vânzările, soldul restant și segmentul de portofoliu. Rezultatele stau într-un tabel propriu și servesc drept bază pentru tabloul de analiză a clienților și pentru misiunile săptămânale de vânzări.

#### 2. Funcționalități Cheie

- **Ritm de cumpărare**: numărul mediu de zile între zilele de cumpărare, măsurat pe istoricul clientului, plus zilele de tăcere; mai multe facturi în aceeași zi contează o singură achiziție.
- **Segment de ritm**: nou, activ, în risc, adormit sau pierdut, raportat la ritmul propriu al clientului, nu la media companiei.
- **Vânzări**: total, ultimele 12 luni, perioada curentă față de precedentă, achiziția medie, creșterea.
- **Creanțe**: sold deschis, restanță, număr de facturi restante și vechimea celei mai vechi, din liniile deschise ale conturilor de client; plățile nepotrivite încă reduc restanța.
- **Clasificare de portofoliu**: client de top, în creștere, potențial ridicat, comenzi mici, stabil, în scădere, inactiv (trei niveluri) sau risc de plată, plus scor de risc și de potențial.
- Date din facturile postate (note de credit scăzute) sau din comenzile confirmate, fără TVA, în moneda companiei; vânzările contactelor se adună la companie.
- Meniu *Vânzări > Portofoliu clienți > Segmente clienți*, filtre (În scădere, Inactiv, Risc de plată, În risc, Cumpărat o singură dată, Clienții mei), vedere pivot; din fișa partenerului, *Acțiune > Customer Segment*.
- Roluri: *Own customers* (doar clienții proprii) și *All customers* (toți clienții și editarea pragurilor), acordate din *Setări > Utilizatori > Customer Portfolio*.
- Setări în *Vânzări > Portofoliu clienți > Setări*: sursa (facturi/comenzi), excluderea persoanelor fizice, prefixele conturilor de venituri (`70` implicit), perioada de comparație, pragurile; buton *Recompute now* sau acțiunea programată nocturnă.

#### 3. Dependențe

- `sale_management`
- `account`

#### 4. Componente Cheie

**Modele**

- `deltatech.customer.segment`: un rând per client și companie cu ritmul, vânzările, creanțele și clasificarea.
- `deltatech.customer.segment.config`: setările și pragurile motorului de segmentare.

**Vizualizări**

- `view_customer_segment_list`, `view_customer_segment_form`, `view_customer_segment_pivot`, `view_customer_segment_graph`, `view_customer_segment_search`: lista, fișa, pivotul, graficul și căutarea segmentelor.
- `view_customer_segment_config_form`: formularul de setări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_customer_segment_recompute`: recalculare nocturnă a segmentelor.
- `action_server_partner_customer_segment`: deschide din partener rândul de segment al clientului.
- `action_server_customer_segment_config`: deschide setările segmentării.

#### 5. Conexiuni

- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md): tablou de bord ce citește rândurile nocturne.
- [deltatech_customer_map](../deltatech_customer_map/index.md): harta vânzărilor, cu aceleași roluri și conturi de vânzări.
