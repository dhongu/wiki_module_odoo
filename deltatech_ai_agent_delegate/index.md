# AI - Agent Delegation (localizat la `deltatech_ai_agent_delegate/index.md`)

- **Nume Tehnic:** `deltatech_ai_agent_delegate`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_agent_delegate
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_agent_delegate`
- **Ultima Ingestie:** `2026-10-20`

#### 1. Sumar

Modulul permite unui **agent AI integrator** din Odoo 19 Enterprise să consulte alți agenți AI, numiți **specialiști** (de exemplu contabilitate, module, documentație), și să combine răspunsurile lor într-un singur răspuns. Fiecare specialist răspunde cu propriile surse, prompt și model, iar citările lui sunt transmise mai departe utilizatorului.

#### 2. Funcționalități Cheie

- **Agenți specialiști**: în fișa agentului apare fila *Specialists* (vizibilă doar administratorilor), unde se aleg agenții pe care îi poate consulta. Numele și descrierea (subtitlul) fiecărui specialist sunt transmise integratorului, ca să știe pe cine să întrebe și despre ce.
- **Topic „Specialist Agents"**: adaugă unealta *AI: Ask a Specialist Agent* (parametri: agent, întrebare) și instrucțiunile de folosire. Topicul trebuie adăugat explicit agentului integrator.
- **Întrebări pe mai multe domenii**: integratorul împarte întrebarea în câte una pentru fiecare specialist (ex.: ce modul înregistrează avizele și ce cont folosește), apoi combină răspunsurile, precizând ce specialist a dat fiecare parte și spunând deschis când specialiștii se contrazic sau nu știu.
- **Întrebări autonome**: specialistul nu vede conversația, deci fiecare întrebare trebuie să fie completă în sine.
- **Fără bucle**: un specialist nu poate consulta un agent deja implicat în consultare, iar lanțul se oprește la două niveluri.
- **Mod de lucru**: se creează specialiștii (cu sursele lor și o descriere clară), apoi agentul integrator cu topicul *Specialist Agents* și lista de specialiști în fila *Specialists*; se întreabă integratorul.

#### 3. Dependențe

- `ai_app`

#### 4. Componente Cheie

**Modele**

- `ai.agent` (extins): câmpul `delegate_agent_ids` (Many2many, „Specialist Agents", tabel `ai_agent_delegate_rel`); adaugă lista specialiștilor în contextul de sistem și metoda `_ai_tool_ask_agent`, care validează specialistul, verifică lanțul (adâncime maximă 2) și îi transmite întrebarea.

**Vizualizări**

- `ai_agent_view_form` (moștenește `ai_app.ai_agent_view_form`): fila *Specialists* cu câmpul `delegate_agent_ids`.

**Acțiuni Automate / Acțiuni Server**

- `ir_actions_server_ask_agent`: acțiune server folosită ca unealtă AI („AI: Ask a Specialist Agent"), apelează `_ai_tool_ask_agent`.
- `ai_topic_specialist_agents`: topic AI „Specialist Agents" care leagă unealta de instrucțiunile de delegare.
- Nu există acțiuni cron.

#### 5. Conexiuni

- [deltatech_ai_source_sync](../deltatech_ai_source_sync/index.md): alimentează agenții specialiști din documentație Markdown/RST (GitHub sau ZIP).
- [deltatech_ai_knowledge_sync](../deltatech_ai_knowledge_sync/index.md): alimentează agenții specialiști din articolele Knowledge.
- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md): agentul magazinului poate fi unul dintre specialiști.
