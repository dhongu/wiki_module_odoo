# Deltatech Advanced Planner (localizat la `deltatech_advanced_planner/index.md`)

- **Nume Tehnic:** `deltatech_advanced_planner`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_advanced_planner
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_advanced_planner`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Deltatech Advanced Planner este un planificator avansat de stoc care răspunde la o întrebare pe care planificarea nativă Odoo nu o acoperă: este realizabilă data de livrare promisă clientului, ținând cont de stocul disponibil, lead time-urile furnizorilor și durata producției? Modulul adaugă capabilități de tip APS (Advanced Planning & Scheduling) cu capacitate finită direct în Odoo, fără integrări externe: planificare backward de la data de livrare, verificare a capacității reale a posturilor de lucru (RCCP/CRP), netting cronologic al stocului proiectat și validare automată a plauzibilității datei de livrare (OK / Avertisment / Blocat). Pe lângă comenzile de vânzare, planificatorul analizează și mișcările de stoc independente, generând automat comenzi planificate de reaprovizionare pentru a preveni stocul negativ. Oferă vizibilitate completă în stil SAP (Situație Material, Stoc Proiectat Agregat cu pegging) și escaladare automată a abaterilor față de plan.

#### 2. Funcționalități Cheie

- **Netting cronologic** — calculează stocul proiectat la data livrării, nu stocul brut curent; ieșirile de după `commitment_date` nu reduc disponibilul calculat.
- **Backward scheduling cu validare dată livrare** — pornind de la data dorită, calculează înapoi datele de producție și de lansare a achizițiilor; emite verdict OK / Avertisment / Blocat și propune o dată alternativă realizabilă când data e imposibilă.
- **Forward scheduling automat** — când SO-ul nu are dată de livrare sau datele ar cădea în trecut, propune automat cea mai devreme dată realizabilă.
- **Explozie BOM recursivă și netting componente** — descompune produsul finit pe toate nivelurile și calculează necesarul net de aprovizionat per componentă, cu alocare globală partajată la rularea în batch (fără supraplanificarea aceluiași stoc).
- **Capacitate producție RCCP** — lead time-ul de producție este derivat din operațiile BOM grupate pe workcenter, determinat de workcenter-ul bottleneck (cu eficiență și ore de calendar).
- **CRP complet cu nivelare greedy (load leveling)** — agregă încărcarea reală a posturilor de lucru pe sloturi (workcenter × săptămână × companie) și mută automat AP-urile cu cel mai mult slack din sloturile supraîncărcate, cu cascadă recursivă pe AP-urile copil; opțiune `dry_run`.
- **Reaprovizionare independentă** — generează AP-uri pentru mișcările de stoc de ieșire fără comandă de vânzare (transferuri, consum intern, ajustări), prevenind stocul negativ.
- **Ciclu de viață SAP-style** — comenzile planificate trec prin `draft → planned → done`, cu tranziții automate la trimiterea/retragerea ofertei și fixare (firming) prin `is_fixed`.
- **Planificare în fază de ofertare (simulare)** — rulare pe SO în stare `draft`, fără rezervare de stoc sau generare PO/MO; rezultatul apare pe liniile SO.
- **Situație Material și Stoc Proiectat Agregat** — ecran de stoc proiectat cronologic per produs cu trasabilitate completă SO → AP → PO/MO → mișcare de stoc și pegging FIFO (ATP, detecție shortage).
- **Sincronizare bidirecțională PO/MO ↔ AP** — modificarea datelor pe liniile PO sau pe MO propagă noile date în AP-uri și cascadează prin ierarhia BOM, actualizând statusul; sincronizarea livrărilor reflectă data efectivă pe picking.
- **Consolidare automată RFQ-uri** — RFQ-urile pentru același furnizor cu dată în fereastra ±N zile sunt adăugate la un PO existent (relație Many2many AP ↔ PO).
- **Generare manuală RFQ / MO** — comenzile de achiziție și de producție se lansează manual din formularul comenzii planificate, cu verificare de duplicat.
- **Detecție abateri zilnică (cron)** — detectează PO nelansat, PO întârziat și MO blocat; actualizează statusul, postează note în chatter și creează activități pentru responsabil.
- **Escaladare automată** — AP-urile rămase `blocked` peste pragul configurat declanșează escaladarea activităților expirate.
- **Replanificare automată la schimbarea datei SO** — retrigerează planificatorul când `commitment_date` se modifică pe un SO confirmat (activabil din Setări).
- **Planificare globală** — wizard pentru rularea pe toate SO-urile active, sortate după `commitment_date`, cu protecție la rulări concurente prin advisory lock PostgreSQL.
- **Planificare bulk din lista SO** — acțiune de server pe selecție multiplă; SO-urile fără BOM sunt marcate `not_applicable`.
- **Rapoarte și export** — PDF „Plan Livrări", Excel AP-uri (toate nivelele BOM, celule colorate per status) și Excel Workcenter Load; raport de încărcare a posturilor (pivot, grafic).
- **Banner status pe SO și notificare email** — verde/galben/roșu pe formularul SO și alertă către managerul de logistică la starea `blocked`.
- **MOQ automat** — cantitatea de comandat este ajustată la cantitatea minimă a furnizorului.

#### 3. Dependențe

- `sale_management`
- `mrp`
- `purchase`
- `stock`
- `resource`
- `mail`
- `web_gantt`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de mai sus (Sumar și Funcționalități Cheie) sunt preluate din `readme/DESCRIPTION.md`, iar acesta nu solicită explicit detalierea Componentelor Cheie (Modele, Vizualizări, Acțiuni Automate). În consecință, analiza dedicată a codului pentru această secțiune a fost omisă intenționat.

Notă: din `readme/DESCRIPTION.md` reies, ca elemente tehnice menționate explicit, modelele `advanced.planned.order` (comanda planificată), `advanced.planner.log` (logul de execuție), precum și un job `ir.cron` zilnic de detecție a abaterilor.

#### 5. Conexiuni

Nicio conexiune către alte module documentate în wiki nu a fost confirmată în manifest sau în cod. Modulele de referință menționate în documentație pentru cerințe APS avansate (`APS4MFG`, `frePPLe`) sunt sisteme externe, nu module din acest monorepo, și nu au pagină wiki.
