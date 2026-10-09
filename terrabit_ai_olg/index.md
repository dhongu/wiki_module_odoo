# AI Agent - Odoo OLG provider (localizat la `terrabit_ai_olg/index.md`)

- **Nume Tehnic:** `terrabit_ai_olg`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_ai_olg
- **Cale Locală:** `odoo-addons/terrabit/terrabit_ai_olg`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă **Odoo OLG** (serviciul text găzduit de Odoo prin IAP, la `olg.api.odoo.com`) ca furnizor de model în lista agenților AI din Odoo 19. Astfel, agenții AI pot rula fără o cheie OpenAI sau Gemini, fără costuri și administrare de chei la un furnizor extern. Serviciul acoperă doar conversația text, iar modulul semnalează explicit când o cerere depășește această limită. Starea de dezvoltare din manifest este Alpha.

#### 2. Funcționalități Cheie

- Modelul `olg-default`, afișat ca „Odoo OLG (conversation only)", apare în lista de modele a `ai.agent` și se alege ca orice alt model. Comutarea între OLG și un model extern se face din configurarea agentului.
- OLG suportă doar text-in/text-out cu istoric conversațional. Cererile cu tool-uri (function calling), JSON schema, fișiere (imagini/PDF) sau web grounding sunt respinse cu o eroare clară, iar embeddings nu sunt disponibile.
- Pe agenții cu OLG:
  - topicurile fără tool-uri sunt permise, instrucțiunile lor ajung ca text în system prompt;
  - topicurile cu tool-uri sunt respinse la salvare;
  - sursele (RAG) sunt respinse, deoarece OLG nu are endpoint de embeddings.
- Prompturile de sistem sunt înglobate ca preambul în prompt (OLG nu are rol system); ultimul mesaj de utilizator devine promptul, iar restul intră în istoricul conversației.
- Mesaje de eroare explicite pentru prompt prea lung, limită de apeluri atinsă și răspuns negenerat.
- Endpoint-ul se poate schimba prin parametrul de sistem `html_editor.olg_api_endpoint` (implicit `https://olg.api.odoo.com`).
- Pentru agenți care au nevoie de instrumente, imagini, PDF sau căutare web, agentul trebuie comutat pe un model OpenAI sau Google.

#### 3. Dependențe

- `ai` (Odoo Enterprise)

#### 4. Componente Cheie

**Modele**

- `ai.agent` (extins): constrângerea `_check_olg_no_tools_or_sources` blochează sursele și topicurile cu tool-uri pe agenții cu `llm_model = olg-default`.
- `ai.agent.source` (extins): constrângerea `_check_agent_not_olg` dublează verificarea direct pe sursă, deoarece constrângerea de pe `sources_ids` nu se declanșează la crearea directă a unei surse.

**Mecanism tehnic (`utils/olg_patch.py`)**

- Providerul `olg` este adăugat în `PROVIDERS` din `odoo.addons.ai.utils.llm_providers`, iar `LLMApiService` este patch-uit (monkey-patch) pentru `__init__` și `_request_llm`. Cauza: modulul `ai` nu oferă hook-uri de extensie.
- Construirea `Provider` tolerează câmpuri apărute upstream (le completează cu valori goale și loghează avertisment), ca să nu oprească încărcarea registry-ului.
- Cererea merge prin `iap_jsonrpc` la `/api/olg/1/chat` (timeout 30 s), cu `prompt`, `conversation_history` și `database_id`.

**Vizualizări**

- Modulul nu definește vizualizări proprii (`data` gol în manifest).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `ai`: modulul Odoo Enterprise extins; nu are pagină wiki.
- `iap`: folosit pentru apelul către serviciul OLG.
