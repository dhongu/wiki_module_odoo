# Deltatech AI - Anthropic (Claude) (localizat la `deltatech_ai_anthropic/index.md`)

- **Nume Tehnic:** `deltatech_ai_anthropic`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_anthropic
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_anthropic`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul adaugă Anthropic (Claude) ca furnizor de inteligență artificială în framework-ul nativ de AI al Odoo 19 Enterprise. Practic, permite companiei să folosească modelele Claude (Opus, Sonnet, Haiku) peste tot unde Odoo folosește deja un model de limbaj — agenți AI, câmpuri AI, acțiuni de server AI sau butoane de tip prompt — inclusiv cu suport pentru apelarea de unelte (tool use) definite în Odoo.

#### 2. Funcționalități Cheie

- Înregistrează Anthropic ca furnizor LLM suplimentar în framework-ul nativ `ai`, alături de OpenAI/Google.
- Modele disponibile oriunde framework-ul nativ folosește un LLM (agenți AI `ai.agent`, câmpuri AI `ai_fields`, acțiuni de server AI `ai_server_actions`, butoane prompt etc.): `claude-opus-5-5` (Opus 5.5, recomandat implicit), `claude-sonnet-5-5`, `claude-haiku-5-5` și `claude-fable-5-1` (cel mai capabil model Anthropic); modelele `claude-opus-4-8`, `claude-sonnet-4-6` și `claude-haiku-4-5` rămân disponibile ca agenții existenți să continue să funcționeze.
- Suportă tool use (apelare de funcții/unelte) prin mecanismul nativ, astfel încât Claude poate invoca uneltele definite în Odoo.
- Nivelul de efort Claude este dedus din stilul de răspuns al agentului: Analytical → `high`, Balanced → `medium`, Creative → `low`. Gândirea adaptivă se folosește pe toate modelele care o suportă (toate, mai puțin Haiku 4.5); parametrii de eșantionare (`temperature`, `top_p`, `top_k`) nu se trimit niciodată.
- Refuzurile Claude (clasificatoare de siguranță) produc o eroare clară cu categoria refuzului; un răspuns tăiat de limita de ieșire, fără text, produce de asemenea eroare, nu un răspuns gol. Pe Fable 5.1, Opus 5.5 și Sonnet 5.5, cererea se reîncearcă mai întâi pe server cu modelul de rezervă recomandat de Anthropic (`fallbacks: "default"`); se dezactivează cu parametrul de sistem `ai.anthropic_fallbacks` = `False` și este omisă automat când `ANTHROPIC_BASE_URL` indică un proxy.
- Prompt caching automat pe fiecare cerere (promptul de sistem și istoricul conversației se facturează la tarif de citire din cache); tokenii de citire/creare cache sunt înregistrați în log.
- Căutare web (web grounding) cu versiunea uneltei suportată de modelul ales (versiunea de bază `web_search_20250305` pe modelele Haiku).
- Limita implicită de ieșire este 16000 tokeni; se schimbă cu parametrul de sistem `ai.anthropic_max_tokens`.
- Configurare cheie API din **Setări → General → Integrări → Anthropic**, sau prin variabila de mediu `ODOO_AI_ANTHROPIC_TOKEN`.
- Limitări cunoscute: Fable 5.1 cere retenție de date de 30 de zile (organizațiile cu zero data retention primesc eroare HTTP 400, exceptând autorizarea expresă Anthropic); la efort ridicat (stil Analytical) și pe Fable 5.1 un apel poate dura câteva minute, deci `limit_time_real` al workerului Odoo trebuie să lase loc suficient sau se alege un stil mai ușor; Anthropic nu expune un API de embeddings, deci pentru RAG (`ai_knowledge`, `ai_documents`) embeddings rămân pe OpenAI/Google; Anthropic Skills (pachete `SKILL.md`) nu sunt disponibile prin Messages API — echivalentul în Odoo este tool use.
- Necesită pachetul Python `anthropic` (`pip install anthropic`); fallback-ul pe server cere o versiune recentă a pachetului.

#### 3. Dependențe

- `ai`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extindere): adaugă câmpul `anthropic_api_key` (parametru de configurare `ai.anthropic_key`), folosit pentru a salva cheia API de pe console.anthropic.com necesară modelelor Claude.

**Vizualizări**

- `res_config_settings_view_form_anthropic`: extinde formularul de setări generale al framework-ului `ai` (după secțiunea Google) cu o secțiune dedicată „Use your own Anthropic (Claude) account", unde se introduce cheia API.

**Alte componente tehnice**

- `utils/llm_providers_patch.py`: înregistrează Anthropic ca furnizor LLM nativ, cu lista modelelor Claude (5.x primele, 4.x păstrate) și corespondența stil de răspuns → model/efort.
- `utils/llm_api_service_patch.py`: patch peste serviciul nativ de apelare a API-urilor LLM, pentru a adăuga integrarea cu API-ul Anthropic (Messages API), inclusiv suport pentru tool use, efort/gândire adaptivă, tratarea refuzurilor, fallback pe server și prompt caching.

#### 5. Conexiuni

- `ai`: modul Enterprise nativ al cărui framework de furnizori LLM este extins de acest modul; nu are încă pagină proprie în wiki.
