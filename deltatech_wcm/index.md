# World Class Manufacturing Dashboard (localizat la `deltatech_wcm/index.md`)

- **Nume Tehnic:** `deltatech_wcm`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_wcm
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_wcm`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un singur tablou de bord pentru cei zece piloni tehnici World Class Manufacturing (WCM): Siguranță, Cost Deployment, Îmbunătățire focalizată, Mentenanță autonomă, Mentenanță planificată, Controlul calității, Logistică și servicii clienți, Managementul timpuriu al echipamentelor, Dezvoltarea oamenilor, Mediu și energie. Fiecare pilon grupează indicatori cu țintă, prag de avertizare și semafor, iar pilonul arată starea celui mai slab indicator.

#### 2. Funcționalități Cheie

- **Semafor**: verde, galben, roșu sau „fără date" (un pilon fără valori nu apare niciodată verde). Cu *Mai mare e mai bine*, valoarea peste țintă e verde, peste prag galbenă; cu *Mai mic e mai bine* comparația se inversează. Pragul trebuie să stea între țintă și zona roșie.
- **Indicatori citiți din Odoo**: disponibilitate OEE (centre de lucru), MTBF și MTTR (echipamente de mentenanță), rata de respingere la controlul calității și rata de rebuturi, livrări la timp (transferuri de ieșire).
- **Cost Deployment**: compară costul unitar real (raportul MO Overview) cu costul standard din rețetă (BoM Structure) și arată cât costă fiecare pierdere pe unitate bună: rebuturi, opriri, schimbări de serie, energie, deșeuri. Indicatorul de abatere se calculează live.
- **Costuri energie și deșeuri** introduse per centru de lucru și perioadă; se repartizează pe unitățile bune produse.
- **Unit Costs**: se recalculează cu *Recompute (last 30 days)*; pierderea cu cel mai mare cost pe unitate e candidatul pentru un proiect de îmbunătățire.
- **Introducere manuală** (valoare și dată) pentru indicatorii fără sursă în Odoo, de exemplu Siguranță.
- Meniu: *Producție > World Class Manufacturing* (Tablou de bord, Indicatori, Costuri energie și deșeuri, Costuri unitare). Țintele implicite sunt orientative și se confirmă cu fabrica.

Fluxul detaliat este în fișa de consultant.

#### 3. Dependențe

- `mrp`
- `mrp_account`
- `mrp_workorder`
- `maintenance`
- `quality`
- `stock`

#### 4. Componente Cheie

**Modele**

- `wcm.pillar`: pilonul WCM, cu starea cea mai slabă a indicatorilor.
- `wcm.indicator`: indicator cu sursă, țintă, prag, valoare și stare.
- `wcm.cost.line`: costul unitar real vs. standard și pierderile pe produs.
- `wcm.cost.manual`: costuri de energie și deșeuri per centru de lucru și perioadă.

**Vizualizări**

- `wcm_pillar_view_kanban`, `wcm_pillar_view_list`: tabloul pilonilor (`action_wcm_pillar_dashboard`).
- `wcm_indicator_view_list`, `wcm_indicator_view_form`, `wcm_indicator_view_search`: indicatorii.
- `wcm_cost_line_view_list`, `wcm_cost_line_view_search`, `wcm_cost_manual_view_list`: costurile.

**Acțiuni Automate / Acțiuni Server**

- Nu există; pilonii și indicatorii inițiali vin din `data/wcm_pillar_data.xml` și `data/wcm_indicator_data.xml`.

#### 5. Conexiuni

- Nu există legături funcționale verificate cu alte module cu pagină wiki.
