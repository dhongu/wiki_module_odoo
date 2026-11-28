# Deltatech Advanced Planner (localizat la `deltatech_advanced_planner/index.md`)

- **Nume Tehnic:** `deltatech_advanced_planner`
- **Versiune:** `20.0.1.14.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_advanced_planner
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_advanced_planner`
- **Ultima Ingestie:** `2026-11-28`
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
- `sale_stock`
- `mrp`
- `purchase`
- `purchase_stock`
- `stock`
- `resource`
- `mail`
- `web_gantt`
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)
- [deltatech_purchase_lead_time](../deltatech_purchase_lead_time/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, completat din `USAGE.md` / `CONFIGURE.md` (interfața este în engleză în cod, cu traducerea română în `i18n/ro.po`). DESCRIPTION.md nu cere detalierea componentelor; mai jos sunt doar reperele tehnice principale, din cod.

**Modele**

- `advanced.planned.order`: comanda planificată (ciclul `draft → planned → done`, fixare prin `is_fixed`, legătură cu PO/MO).
- `advanced.planner.engine` (model abstract) și `advanced.planner.log`: motorul de planificare și jurnalul de execuție.
- `advanced.workcenter.load`, `advanced.crp.slot`, `advanced.workcenter.efficiency`: încărcarea și eficiența posturilor de lucru (RCCP/CRP).
- `advanced.material.situation` (+ `.line`) și `advanced.stock.projection` (+ `.line`): Situația Material și Stocul Proiectat Agregat.
- Wizarduri: `advanced.planner.wizard`, `advanced.global.planner.wizard`, `advanced.crp.leveling.wizard`, `advanced.ctp.wizard`, `advanced.report.wizard`, `advanced.material.situation.snapshot.wizard`.
- Extinse: `sale.order`, `sale.order.line`, `purchase.order`, `purchase.order.line`, `mrp.production`, `mrp.workcenter`, `stock.move`, `stock.picking`, `stock.warehouse.orderpoint`, `product.product`, `product.template`, `res.config.settings`.

**Vizualizări**

- Meniul rădăcină al planificatorului cu: panou de bord (componentă OWL), tabloul riscului de livrare, comenzi planificate (listă, pivot, Gantt), planificare globală, Situație Material și snapshot-uri, stoc proiectat, încărcarea posturilor de lucru, CRP, eficiența posturilor, nivelare CRP și rapoarte.
- Banner de status și rezultatul planificării pe formularul comenzii de vânzare; raportul PDF „Plan Livrări" și raportul de situație material.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_detect_deviations` — detecția zilnică a abaterilor (PO nelansat, PO întârziat, MO blocat), cu note în chatter și activități.
- `ir_cron_replan_active_orders` — replanificarea nocturnă a comenzilor de vânzare active.
- `ir_cron_clean_planner_logs` — curățarea jurnalelor vechi ale planificatorului.
- Acțiune de server pentru planificare bulk din lista comenzilor de vânzare.

#### 5. Conexiuni

- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md): cardurile KPI folosite de panoul de bord al planificatorului.
- [deltatech_purchase_lead_time](../deltatech_purchase_lead_time/index.md): termenele de aprovizionare ale furnizorilor, luate în calcul la planificarea înapoi.

Modulele `APS4MFG` și `frePPLe`, menționate în documentație pentru cerințe APS avansate, sunt sisteme externe fără pagină wiki.
