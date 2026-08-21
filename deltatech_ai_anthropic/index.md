# Deltatech AI - Anthropic (Claude) (localizat la `deltatech_ai_anthropic/index.md`)

- **Nume Tehnic:** `deltatech_ai_anthropic`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_anthropic
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_anthropic`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul adaugă Anthropic (Claude) ca furnizor de inteligență artificială în framework-ul nativ de AI al Odoo 19 Enterprise. Practic, permite companiei să folosească modelele Claude (Opus, Sonnet, Haiku) peste tot unde Odoo folosește deja un model de limbaj — agenți AI, câmpuri AI, acțiuni de server AI sau butoane de tip prompt — inclusiv cu suport pentru apelarea de unelte (tool use) definite în Odoo.

#### 2. Funcționalități Cheie

- Înregistrează Anthropic ca furnizor LLM suplimentar în framework-ul nativ `ai`, alături de OpenAI/Google.
- Pune la dispoziție modelele Claude (`claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5`) oriunde framework-ul nativ folosește un LLM: agenți AI (`ai.agent`), câmpuri AI (`ai_fields`), acțiuni de server AI (`ai_server_actions`), butoane prompt etc.
- Suportă tool use (apelare de funcții/unelte) prin mecanismul nativ, astfel încât Claude poate invoca uneltele definite în Odoo.
- Configurare cheie API din **Setări → General → Integrări → Anthropic**, sau prin variabila de mediu `ODOO_AI_ANTHROPIC_TOKEN`.
- Limitări cunoscute: Anthropic nu expune un API de embeddings, deci pentru RAG (`ai_knowledge`, `ai_documents`) embeddings rămân pe OpenAI/Google; Anthropic Skills (pachete `SKILL.md`) nu sunt disponibile prin Messages API — echivalentul în Odoo este tool use.
- Necesită pachetul Python `anthropic` instalat (`pip install anthropic`).

#### 3. Dependențe

- `ai`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extindere): adaugă câmpul `anthropic_api_key` (parametru de configurare `ai.anthropic_key`), folosit pentru a salva cheia API de pe console.anthropic.com necesară modelelor Claude.

**Vizualizări**

- `res_config_settings_view_form_anthropic`: extinde formularul de setări generale al framework-ului `ai` (după secțiunea Google) cu o secțiune dedicată „Use your own Anthropic (Claude) account", unde se introduce cheia API.

**Alte componente tehnice**

- `utils/llm_providers_patch.py`: extinde/patch-uiește lista de furnizori LLM nativi din Odoo pentru a înregistra Anthropic ca opțiune.
- `utils/llm_api_service_patch.py`: patch peste serviciul nativ de apelare a API-urilor LLM, pentru a adăuga integrarea cu API-ul Anthropic (Messages API), inclusiv suport pentru tool use.

#### 5. Conexiuni

- `ai`: modul Enterprise nativ al cărui framework de furnizori LLM este extins de acest modul; nu are încă pagină proprie în wiki.
