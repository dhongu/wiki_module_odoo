# AI - Sincronizare surse (colecții Markdown) (localizat la `deltatech_ai_source_sync/index.md`)

- **Nume Tehnic:** `deltatech_ai_source_sync`
- **Versiune:** `20.0.1.11.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_source_sync
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_source_sync`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Alimentează agenții AI din Odoo 20 Enterprise cu documentație Markdown ținută într-un depozit GitHub sau într-o arhivă ZIP, fără încărcarea fișierelor unul câte unul. O colecție de surse este legată de un agent și menține sursele agentului sincronizate cu fișierele. Modulul corectează și extragerea textului din fișierele Markdown și text, astfel încât cuvintele cu diacritice să fie indexate corect.

#### 2. Funcționalități Cheie

- **Origine:** depozit GitHub (ramură, token opțional pentru depozit privat, subdirector opțional), arhivă ZIP, fluxuri RSS sau pagini urmărite. Meniu: **AI › Configurare › Colecții de surse** sau butonul inteligent **Colecții** de pe agent.
- **Fluxuri RSS:** fiecare articol devine o sursă (site, dată, titlu, link, rezumatul din flux); articolele mai vechi decât retenția nu se adaugă, iar sursele lor se elimină; fluxurile paginate pot fi citite pe mai multe pagini; RSS 2.0 și Atom, fără entități externe.
- **Pagini urmărite:** un text oficial lung republicat pe loc (ex. Codul fiscal adnotat ANAF) nu e copiat; liniile potrivite de **modelul de actualizare** dau starea paginii, iar fiecare stare nouă devine o sursă; stările vechi se șterg după retenție.
- **Selecție fișiere și împărțire:** tipare de includere/excludere, rădăcină, împărțire pe titluri până la un nivel ales (numele sursei păstrează titlurile de deasupra), secțiuni eliminate; fișierele `*.rst` se convertesc în Markdown.
- **Linkuri pentru citări:** sursele din GitHub trimit la fișier; un tipar **Page URL** trimite la un site publicat; opțiunea **Public links** scrie linkul sub titlul sursei și arată citările tuturor utilizatorilor, inclusiv vizitatorilor de livechat.
- **Text mai curat:** imaginile se reduc la text alternativ, linkurile la textul lor.
- **Sincronizare incrementală:** fișierele noi adaugă surse, cele modificate înlocuiesc doar secțiunile schimbate, cele șterse elimină sursele; fișierele neschimbate nu se descarcă, iar embeddings-urile rămân. Butonul **Sincronizează** pune lucrarea în coadă (cron, reia de unde s-a oprit); sincronizare zilnică opțională.
- **Limite de rată:** cererile de embeddings refuzate sunt reluate după așteptarea cerută de furnizor; sursele eșuate sunt repuse în coadă (până la 3 ori).
- **Glosar de căutare** pe agent (`termen[, variantă...] = sens`) adăugat întrebării înainte de căutare; setări de căutare (fragmente în context, un fragment per sursă) și **fragmente rezervate** pe o colecție mică.
- **Prefix de folder:** numele surselor poate începe cu folderul fișierului (numele tehnic al modulului într-un wiki de module).
- **GitHub App** în loc de token personal: ID aplicație și cheie `.pem` în **Setări › Integrări**, bifat pe fiecare colecție.
- Detaliile pas cu pas și exemplele (wiki de module, legislație, știri legislative, documentația Odoo) sunt în fișa consultantului.

#### 3. Dependențe

- `ai_agentic`

#### 4. Componente Cheie

**Modele**

- `ai.source.collection`: colecția de surse, cu origine, filtre, împărțire, retenție și rezultatul sincronizării.
- `ai.agent`, `ai.agent.source`, `ai.embedding` (extinderi): glosar și setări de căutare pe agent, legătura sursă-colecție, reluarea embeddings-urilor refuzate.
- `ir.attachment` (extindere): indexare UTF-8 pentru fișierele Markdown și text.
- `res.config.settings` (extindere): setările GitHub App.

**Vizualizări**

- `ai_source_collection_views`: lista și formularul colecțiilor; `ai_agent_views`: tab-ul de căutare în surse și butonul Colecții; `res_config_settings_views`: setările GitHub App.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_source_collection_sync`: sincronizarea zilnică a colecțiilor GitHub, RSS și pagini urmărite.

#### 5. Conexiuni

- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md): folosește sursele agentului pentru produsele magazinului.
