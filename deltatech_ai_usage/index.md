# AI Usage and Cost Tracking (Consum și costuri AI)

- **Nume Tehnic:** `deltatech_ai_usage`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_usage
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_usage`
- **Ultima Ingestie:** `2026-10-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Firma plătește furnizorul de AI cu propria cheie API. Modulul arată cât costă fiecare apel AI din Odoo, astfel încât factura să poată fi estimată și controlată. Înregistrează fiecare cerere trimisă către un furnizor AI (OpenAI, Google Gemini, Anthropic Claude), cu tokenii consumați și costul estimat, și arată cine a făcut-o.

#### 2. Funcționalități Cheie

- **Fiecare cerere facturată, nu un total**: fiecare rundă a buclei de unelte a agentului, fiecare reîncercare Gemini, câmpurile AI, embedding-urile surselor agentului (RAG), transcrierile. Odoo păstrează singur doar o linie în logul serverului.
- **Tokenii reali ai furnizorului**: intrare, citire din cache, scriere în cache, ieșire și raționament, plus căutările web. Tokenii de „thinking” Gemini, facturați ca ieșire și omiși de Odoo, sunt incluși.
- **Cine a cerut**: agentul, modulul sau funcția (preluat din agent), documentul, utilizatorul și compania. Cererile unui răspuns sunt grupate într-un apel; un agent care consultă alt agent apare ca apel copil.
- **Cost estimat**: listă de prețuri per model și per 1 milion de tokeni, cu date de valabilitate, astfel încât cererile vechi își păstrează costul. Prețurile de listă Anthropic sunt incluse; modelele OpenAI și Google se adaugă manual. Un nume de model terminat cu `*` se potrivește cu toate modelele cu acel prefix (câștigă potrivirea cea mai lungă).
- **Raportare**: pivot și grafic pe lună, model, agent, modul, utilizator și companie; filtre pentru erori, consum estimat (furnizorul nu a returnat utilizarea) și modele fără preț. Meniu: **AI → Raportare → Consum AI**; prețurile: **AI → Configurare → Prețuri modele AI**.
- **Recalculare cost**: după adăugarea prețului lipsă, cererile se selectează în listă și se rulează **Acțiuni → Recalculează costul**.
- **Sigur**: nu se stochează niciun prompt sau răspuns, doar contoare. Înregistrarea nu întrerupe niciodată un apel AI, iar rândul se scrie în tranzacție proprie, deci o cerere anulată după răspuns este totuși numărată.
- **Pentru dezvoltatori**: un modul care apelează direct `LLMApiService.request_llm` se poate numi prin cheile de context `ai_usage_origin`, `ai_usage_res_model`, `ai_usage_res_id`; un furnizor care nu trece prin `LLMApiService._request` poate folosi `_ai_usage_record(...)`.

Costurile sunt estimări; factura furnizorului rămâne referința. Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `ai_app` (Odoo Enterprise)

#### 4. Componente Cheie

**Modele**

- `ai.usage.log`: jurnalul cererilor AI, cu tokeni, cost estimat, origine, apel părinte, utilizator și companie.
- `ai.model.price`: lista de prețuri per model (potrivire pe tipar, cu `*`) și per 1 milion de tokeni, cu dată de valabilitate.
- `ai.agent`, `ai.embedding`, `ir.actions.server` (extinse): leagă cererile de agent, de indexarea surselor, respectiv de acțiunile server AI, pentru atribuirea originii.

**Vizualizări**

- `ai_usage_log_view_list`, `ai_usage_log_view_form`, `ai_usage_log_view_pivot`, `ai_usage_log_view_graph`, `ai_usage_log_view_search`: consultarea și analiza consumului.
- `ai_model_price_view_list`, `ai_model_price_view_search`: administrarea prețurilor.

**Acțiuni Automate / Acțiuni Server**

- `ai_usage_log_action_recompute_cost`: acțiune server „Recalculează costul” pe cererile selectate. Nu există acțiuni cron.

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): din versiunea 19.0.1.3.0 trimite cererile Claude în acest jurnal.
- Modulele AI Terrabit care definesc agenți (ex. `deltatech_bank_reconcile_ai`) apar ca **origine** a cererilor; [deltatech_ai_agent_delegate](../deltatech_ai_agent_delegate/index.md) generează apeluri copil (un agent care consultă alt agent).
