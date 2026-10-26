# AI - Source Sync (colecții Markdown)

- **Nume Tehnic:** `deltatech_ai_source_sync`
- **Versiune:** `19.0.1.8.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_source_sync
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_source_sync`
- **Ultima Ingestie:** `2026-10-20`

#### 1. Sumar

Alimentează agenții AI din Odoo 19 Enterprise cu documentație Markdown ținută într-un depozit GitHub sau într-o arhivă ZIP, fără încărcarea fișierelor unul câte unul. O colecție de surse este legată de un agent și îi păstrează sursele sincronizate cu fișierele. Modulul corectează și extragerea textului din fișierele Markdown și text, astfel încât cuvintele cu diacritice să nu mai fie deformate înainte de generarea embedding-urilor.

#### 2. Funcționalități Cheie

- **Origine:** depozit GitHub (ramură, token opțional pentru depozite private, subdirector) sau arhivă ZIP încărcată (un singur folder rădăcină este ignorat).
- **Selecția fișierelor:** modele de includere și excludere pe calea relativă (`*/index.md`, `*.md` etc.).
- **Împărțire după titluri:** un fișier mare (lege, manual) devine câte o sursă pe secțiune, până la nivelul de titlu ales. Numele sursei păstrează titlurile părinte, deci citările indică secțiunea corectă.
- **Secțiuni eliminate:** titlurile listate pe colecție sunt scoase împreună cu conținutul lor (ex. secțiunile tehnice, pentru un agent folosit de clienți).
- **reStructuredText:** fișierele `*.rst` (ex. documentația Odoo) sunt convertite în Markdown și împărțite la fel, fără directive și roluri.
- **Linkuri de citare:** sursele din GitHub trimit la pagina fișierului pe GitHub; un model **Page URL** (cu `{path}`) poate trimite către un site publicat.
- **Text curățat:** imaginile rămân doar cu textul alternativ, linkurile doar cu textul lor.
- **Sincronizare incrementală:** fișierele noi adaugă surse, cele modificate înlocuiesc doar secțiunile schimbate, cele șterse elimină sursele. Fișierele neschimbate sunt sărite (din GitHub nici nu se descarcă), iar fișierele care nu dau nicio sursă sunt reținute prin hash și ignorate.
- **Rulare în fundal:** butonul *Synchronize* pune lucrarea în coadă, rulată de cron, care reia de unde a rămas; un cron zilnic actualizează colecțiile GitHub cu *Daily Synchronization* bifat.
- **Limite de rată:** cererile de embedding refuzate sunt reîncercate după pauza cerută de furnizor, iar sursele eșuate sunt puse înapoi în coadă (până la 3 ori).
- **Glosar de căutare** pe agent: termeni (conturi, abrevieri, termeni străini, greșeli frecvente) în forma `termen[, variantă...] = sens`; sensul termenilor din întrebare se adaugă înainte de căutare.
- **Setări de căutare pe agent** (tab *Source Search*): numărul de fragmente date modelului și opțiunea *One Fragment per Source*, utilă pentru întrebări de tip listă.
- **Prefix folder:** numele sursei poate începe cu folderul fișierului (ex. numele tehnic al modulului într-un wiki de module).
- **Indexare UTF-8** pentru toate atașamentele Markdown/text, inclusiv cele încărcate manual ca surse (fișierele încărcate înainte de instalare își păstrează indexul vechi).
- **Flux de lucru:** *AI › Configuration › Source Collections* sau butonul inteligent *Collections* de pe agent; rezultatul (adăugate, actualizate, șterse, neschimbate, eșuate) apare pe colecție, iar sursele sunt apoi embedded de cronul standard AI.
- **Exemple:** wiki de module în două colecții cu prefix folder: paginile modulelor (`*/index.md`, împărțire la titlul 2; secțiunile sunt pe titlul 4, deci de regulă o sursă pe pagină) și fișele consultant (`*/FISA_CONSULTANT*.md`, împărțire la titlul 2, cam zece surse pe fișă, deci peste 2.000 de surse la 220 de fișe, cu citări pe secțiune), legislație (root `references`, `*.md`, împărțire la titlul 2), documentația Odoo (`odoo/documentation`, `*.rst`, Page URL către odoo.com).

#### 3. Dependențe

- `ai_app`

#### 4. Componente Cheie

**Modele**

- `ai.source.collection`: colecția de surse (agent, origine, depozit/ZIP, tipare, nivel de împărțire, secțiuni eliminate, Page URL, stare sincronizare, hash-uri ale fișierelor goale).
- `ai.agent` (extins): colecțiile agentului, glosarul de căutare (`rag_glossary`), `rag_top_n`, `rag_one_chunk_per_source`.
- `ai.agent.source` (extins): `collection_id`, `sync_path`, `sync_hash`, `sync_retry_count`.
- `ai.embedding` (extins): reîncercare la limitele de rată ale furnizorului.
- `ir.attachment` (extins): extragerea textului Markdown/text ca UTF-8.

**Vizualizări**

- `ai_source_collection_view_list` / `_form` / `_search`: gestionarea colecțiilor, cu meniu în configurarea AI.
- `ai_agent_view_form` (moștenită): buton inteligent *Collections* și tab-ul *Source Search*.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_source_collection_sync`: „AI: synchronize the source collections”, zilnic, apelează `_cron_sync()`.

#### 5. Conexiuni

- [deltatech_ai_knowledge_sync](../deltatech_ai_knowledge_sync/index.md): aceeași idee pentru articolele din Knowledge; depinde de acest modul.
- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md): produsele publicate ale magazinului ca surse; depinde de acest modul.
- [deltatech_ai_agent_delegate](../deltatech_ai_agent_delegate/index.md): agenții alimentați din colecții pot fi specialiști consultați de un agent integrator.
