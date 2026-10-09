# Deltatech Advanced Planner (localizat la `deltatech_advanced_planner/index.md`)

- **Nume Tehnic:** `deltatech_advanced_planner`
- **Versiune:** `19.0.1.6.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_advanced_planner
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_advanced_planner`
- **Ultima Ingestie:** `2026-10-09`
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
- **MOQ automat** — cantitatea de comandat este ajustată la cantitatea minimă a furnizorului; prețul furnizorului este convertit în UoM-ul și moneda comenzii planificate, cu discount aplicat.
- **Mai multe depozite în aceeași companie** — fiecare comandă planificată poartă depozitul comenzii de vânzare (inclusiv subansamblele și componentele); stocul alocat la planificarea globală se numără per depozit, RFQ-urile se recepționează și se consolidează doar în depozitul comenzii planificate, iar MO-urile generate folosesc tipul de operație și locațiile depozitului. Planificarea globală fără depozit rulează reaprovizionarea pentru toate depozitele companiei.
- **Rapoarte pe depozit** — Situația Material și Stocul Proiectat au un Depozit opțional (gol = toată compania); transferul între depozite contează ca ieșire și intrare; depozitul apare în exporturile PDF/Excel, în wizardul de snapshot și ca filtru/grupare pe comenzile planificate și pe tabloul riscurilor de livrare.
- **Dashboard cu carduri KPI** — rândul de statistici (Blocate, Avertismente, OK, Reaprovizionări) folosește cardurile partajate din `deltatech_web_kpi_cards`; click pe card deschide înregistrările numărate; selector de depozit (când sunt mai multe depozite). Încărcarea posturilor de lucru rămâne pe toate depozitele.
- **Tablou riscuri livrare** (Delivery Risk Board) — vedere dedicată a comenzilor planificate cu risc, filtrabilă și grupabilă pe depozit.
- **Comenzi planificate partajate** — subansamblele și materiile prime comune mai multor linii de SO (ex. variante ale aceluiași produs finit) sunt planificate o singură dată, cu cantitatea cumulată; în Gantt, fiecare comandă care consumă o componentă comună depinde de ea.
- **Cumulare linii în RFQ** — la consolidare, cantitatea se adaugă la linia existentă cu același produs, UoM, preț și discount, în loc să se creeze o linie duplicat; generarea în masă (acțiune pe listă) rulează fiecare AP într-un savepoint și afișează erorile într-o notificare.
- **Multi-companie și unități de măsură** — reguli multi-companie pe comenzile planificate, încărcarea posturilor, sloturile CRP, situații material și proiecții de stoc; cantitățile din BOM, PO, MO și mișcări sunt convertite în UoM-ul de bază al produsului înainte de netting și pegging.
- **MO generat de planificator** — la confirmarea MO-ului generat din AP, componentele nu mai sunt planificate a doua oară prin ruta MTO („Replenish on Order"); MO-urile create manual sau din reaprovizionare păstrează comportamentul MTO.

#### 3. Dependențe

- `sale_management`
- `mrp`
- `purchase`
- `stock`
- `resource`
- `mail`
- `web_gantt`
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` (completat cu `readme/HISTORY.md` pentru funcționalitățile apărute după redactarea lui), care nu solicită explicit detalierea componentelor; mai jos sunt doar elementele tehnice menționate explicit în documentație sau vizibile în manifest.

**Modele**

- `advanced.planned.order`: comanda planificată (AP), cu ciclu de viață `draft → planned → done`, depozit, fixare (`is_fixed`) și legături către SO, PO și MO.
- `advanced.planner.log`: logul de execuție al planificatorului (pas, severitate, detalii).
- `advanced.planner.engine`: motorul de planificare (netting, explozie BOM, backward/forward scheduling, detecție abateri).
- `advanced.workcenter.load` și `advanced.crp.slot`: încărcarea posturilor de lucru și sloturile CRP (workcenter × săptămână × companie).
- `advanced.material.situation` și `advanced.stock.projection`: Situația Material și Stocul Proiectat Agregat (cu linii și wizard de snapshot).

**Vizualizări**

Meniuri sub aplicația Planificator: Dashboard, Tablou riscuri livrare, Comenzi planificate (listă, pivot, Gantt), Planificare globală, Situație Material (+ snapshot-uri), Stoc Proiectat, Încărcare posturi, CRP și nivelare, Rapoarte. Setările sunt în Setări → Inventar.

**Acțiuni Automate / Acțiuni Server**

- Curățare log-uri vechi: săptămânal, activ implicit.
- Detecție abateri zilnică: zilnic, activat din Setări (parametrul comută acțiunea programată).
- Replanificare nocturnă SO active: zilnic, dezactivat implicit.

#### 5. Conexiuni

- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md): cardurile KPI partajate afișate pe dashboard-ul planificatorului (dependență din 19.0.1.4.0).

Modulele de referință menționate în documentație pentru cerințe APS avansate (`APS4MFG`, `frePPLe`) sunt sisteme externe, nu module din acest monorepo, și nu au pagină wiki.
