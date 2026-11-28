# MCP Server - Acces AI Guvernat pentru Claude și ChatGPT (localizat la `deltatech_mcp_server/index.md`)

- **Nume Tehnic:** `deltatech_mcp_server`
- **Versiune:** `20.0.2.5.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_mcp_server
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_mcp_server`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă Claude, ChatGPT, Cursor și Codex acces la Odoo pe care îl poți explica unui auditor: AI-ul fiecărei persoane vede doar modelele și câmpurile rolului ei, accesul suplimentar este aprobat de o persoană și expiră singur, datele personale rămân mascate, iar fiecare apel este înregistrat pe serverul propriu. Se construiește peste serverul MCP din Odoo 20 Enterprise (`ai_mcp`), fără niciun serviciu extern; clientul AI se conectează la `https://<odoo>/mcp` și lucrează mereu cu drepturile Odoo ale persoanei care l-a conectat.

#### 2. Funcționalități Cheie

- **Politici de acces pe rol**: lista modelelor, drepturile read/create/write și câmpurile vizibile (ascunse, limitate sau mascate ca `***`); șabloane pentru suport, vânzări, achiziții, catalog produse, prețuri, stoc, contabilitate și raportare, combinabile și salvabile ca șabloane proprii.
- **Acces temporar aprobat de o persoană**: prin `request_access`, AI-ul cere un model cu motiv; un administrator aprobă pentru acel utilizator, până la o dată, iar accesul se oprește singur.
- **Date personale mascate implicit** (CUI/VAT, IBAN, CNP, data nașterii, salariu), fără a putea fi deduse prin filtre, sortări sau grupări; câmpurile binare nu se returnează niciodată.
- **Doar citire până la activare**: uneltele de scriere sunt ascunse până se bifează *Allow AI clients to write*; `create`/`write` nu schimbă starea documentelor, o comandă se confirmă doar prin butonul expus ca unealtă.
- **Code Mode** (*Scripts*, oprit implicit): `run_script` rulează în sandbox-ul Odoo un script care înlănțuie uneltele de citire, iar în chat revine doar rezultatul final.
- **Unelte proprii și prompturi**: acțiuni de server sau metode-buton (ex. `action_confirm`) în *MCP Server → Configuration → Tools*; întrebări gata făcute în *Prompts*, cu argumente `{{client}}`.
- Unelte standard pentru client: `whoami`, `list_models`, `describe_model`, `search`, `read`, `aggregate`, `list_attachments`, `read_attachment`, iar cu scrierea activă `create`, `write`, `post_message`, `schedule_activity`, `add_followers`.
- **Limite per politică**: înregistrări pe apel, buget zilnic de înregistrări și date, apeluri pe minut, adrese IP permise.
- **Jurnal complet** (*Call Log*) cu utilizator, client, unealtă, argumente, durată, rezultat și valorile vechi/noi; ecranul *Daily Usage* arată consumul; ambele se șterg după 90 de zile (configurabil); autentificările refuzate sunt și ele înregistrate.
- Conectare cu cheie API cu scopul *MCP* (Claude Code, Cursor, VS Code), valabilă doar pe `/mcp`, sau prin OAuth 2.1 (Claude.ai, ChatGPT) din *Settings → Integrations → MCP OAuth*; pot conecta doar membrii grupului *MCP Server / User*, recomandat un utilizator dedicat AI.
- Generic data tools din aplicațiile AI Odoo (`ai_tool_search` etc.) sunt ascunse pe `/mcp`, ca să nu ocolească politicile; funcționează doar cu Odoo Enterprise, nu cu Community.
- Susține evidența și supravegherea umană cerute de EU AI Act (articolele 12 și 26), fără a garanta singur conformitatea. Pașii de configurare și utilizare sunt în fișa consultantului.

#### 3. Dependențe

- `ai_mcp` (Odoo 20 Enterprise, *AI MCP Server*)

#### 4. Componente Cheie

**Modele**

- `deltatech.mcp.policy` și `deltatech.mcp.policy.line`: politica de acces și liniile ei pe model.
- `deltatech.mcp.policy.template` și `deltatech.mcp.policy.template.line`: șabloanele de politici.
- `deltatech.mcp.access.request`: cererile de acces temporar.
- `deltatech.mcp.tool`: uneltele proprii expuse clientului AI.
- `deltatech.mcp.prompt` și `deltatech.mcp.prompt.argument`: prompturile și argumentele lor.
- `deltatech.mcp.log` și `deltatech.mcp.usage`: jurnalul apelurilor și consumul zilnic.
- `deltatech.mcp.server`: logica serverului MCP.
- `ai.mcp.request.dispatcher`, `ir.http`, `res.users`, `res.config.settings`: extinse pentru politici, autentificare, politica utilizatorului și setări.
- `deltatech.mcp.policy.template.wizard`: wizardul *Create from Template* / *Add Template*.

**Vizualizări**

- `views/mcp_policy_views.xml`, `mcp_policy_template_views.xml`: politici și șabloane.
- `views/mcp_access_request_views.xml`: cereri de acces de aprobat.
- `views/mcp_tool_views.xml`, `mcp_prompt_views.xml`: unelte și prompturi.
- `views/mcp_log_views.xml`, `mcp_usage_views.xml`: jurnal și consum.
- `views/res_users_views.xml`, `res_config_settings_views.xml`, `mcp_menus.xml`: politica pe utilizator, setări și meniuri.

**Acțiuni Automate / Acțiuni Server**

- `data/mcp_policy_template_data.xml`: șabloanele predefinite de politici (nu există cron declarat în date; curățarea jurnalului după 90 de zile este setare).

#### 5. Conexiuni

- `ai_mcp`: același endpoint `/mcp`, aceleași chei și același server OAuth; modulul adaugă politici, mascare, limite și jurnal.
