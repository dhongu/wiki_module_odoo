# Deltatech MCP Server

- **Nume Tehnic:** `deltatech_mcp_server`
- **Versiune:** `19.0.1.13.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_mcp_server
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_mcp_server`
- **Ultima Ingestie:** `2026-10-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul transformă Odoo într-un server MCP (Model Context Protocol), astfel încât aplicații AI precum Claude, ChatGPT sau Cursor să poată citi, iar dacă se permite explicit și modifica, datele din Odoo. Funcționează pe Community și pe Enterprise și nu depinde de modulul Odoo AI. Asistentul vede exact ce are voie să vadă utilizatorul cu care s-a conectat, iar administratorul stabilește prin politici de acces ce modele și câmpuri sunt expuse, ce date personale sunt mascate și ce limite de consum se aplică. Fiecare apel este înregistrat, inclusiv ce a modificat (valoarea veche și cea nouă), deci există evidență a ceea ce a făcut asistentul.

#### 2. Funcționalități Cheie

- **Conectare** la `https://<odoo>/mcp` prin cheie API valabilă doar pe acest endpoint (Claude Code, Cursor) sau prin OAuth 2.1 cu PKCE, cu descoperire, auto-înregistrare și documente de metadate ale clientului (Claude.ai, ChatGPT, Codex). Cheia se generează din *MCP Server > Generate API Key*, de către utilizatorul AI, și se afișează o singură dată. Cheia funcționează doar pe `/mcp`, nu și pe XML-RPC/JSON.
- **Conexiuni OAuth** cu token de acces de scurtă durată (60 de minute implicit) și token de reîmprospătare rotit la fiecare folosire; refolosirea lui închide conexiunea (motiv *Refresh token used twice*). Scope-uri `mcp:read` și `mcp:write`: când clientul cere scriere și serverul o permite, pagina de consimțământ oferă și **Read only**; o scriere încercată totuși este refuzată și marcată *Denied*.
- **MCP Server > OAuth Connections**: fiecare utilizator își vede și își revocă propriile conexiuni, administratorul pe toate; conexiunea neutilizată mai mult decât valabilitatea din Setări (30 de zile implicit) expiră.
- **Utilizator dedicat AI**: pot să se conecteze doar membrii grupului *MCP Server / User*; se recomandă un utilizator separat, nu un administrator. Se aplică mereu drepturile de acces și regulile de înregistrare normale.
- **Politică de acces** per utilizator (*MCP Server > Policies*): lista modelelor permise, cu drepturi separate de citire, creare și scriere, controlul câmpurilor (ascunse, doar unele vizibile sau mascate ca `***`), câmpuri *Read-only* (ex. `active`), *Notes and activities* și *Attachments* per model.
- **Șabloane de politici** (*MCP Server > Policy Templates*): wizardul *Create from Template* de pe lista politicilor face o politică dintr-unul sau mai multe profiluri gata făcute: *Support*, *Sales*, *Purchase*, *Product Catalog*, *Product Prices*, *Stock*, *Accounting* și *Reporting* (ultimele trei doar citire). Liniile numesc modelele ca text, deci modelele, câmpurile și metodele modulelor neinstalate se sar și se afișează într-o notificare; pentru fiecare metodă-buton se găsește sau se creează unealta. Mai multe șabloane se combină (drepturile se adună, restricțiile rămân, limita cea mai strictă câștigă). Pe o politică, *Add Template* adaugă un șablon, iar *Save as Template* o păstrează ca șablon nou. Șablonul nu dă drepturi Odoo: utilizatorul AI are nevoie în continuare de grupurile aplicațiilor.
- **Only these writable** pe linia politicii: când e completat, `create` și `write` pot seta doar acele câmpuri, iar `describe_model` le marchează pe celelalte ca nescriibile (folosit de șablonul *Product Prices*: doar `list_price` pe produs, prețul și datele pe prețurile furnizorilor).
- **Date personale** (CUI/TVA, IBAN, CNP, data nașterii, salariu) mascate implicit și protejate împotriva deducerii prin filtre, sortări sau agregări.
- **Limite per politică**: înregistrări per apel, buget zilnic de înregistrări și de date, apeluri pe minut, adrese IP permise.
- **Doar citire implicit**: uneltele de scriere rămân ascunse până la bifarea *Allow AI clients to write* în Setări și a drepturilor pe modelele dorite. Nu există unealtă de ștergere, câmpurile cu linii nu se pot scrie, iar câmpurile binare și modelele de sistem (`ir.*`, chei API, grupuri) nu se expun niciodată. `create`/`write` nu setează niciodată statusul (`state`), câmpurile calculate de Odoo sau câmpurile marcate *Read-only* în politică; statusul se schimbă doar printr-o unealtă-buton.
- **Unelte standard**: `whoami`, `list_models`, `describe_model`, `search`, `read`, `aggregate`; cu scrierea activată `create`, `write`, `post_message` (notă internă în chatter, niciodată trimisă urmăritorilor) și `schedule_activity` (necesită Discuss); `list_attachments` și `read_attachment` pentru fișierele atașate (text, imagini, PDF), până la dimensiunea maximă din Setări (5 MB implicit), și în mod doar-citire.
- **Unelte proprii** (*MCP Server > Tools*): o acțiune de server sau o metodă-buton a unui model (ex. `action_confirm` pe comenzi de vânzare), activată per politică și rulată cu drepturile utilizatorului conectat. Se acceptă doar metodele care încep cu `action_` sau `button_` ori sunt declarate în `_mcp_methods`. Dacă butonul deschide un dialog, apelul este refuzat. Parametrii ajung în acțiunea de server prin `env.context["mcp_arguments"]`.
- **Prompturi** (*MCP Server > Prompts*): întrebări gata făcute, cu argumente `{{nume}}`, oferite politicilor alese (sau tuturor, dacă lista e goală); apar în clientul AI ca comenzi (ex. `/mcp__odoo__customer_review` în Claude Code).
- **Mai multe companii**: `whoami` listează companiile și moneda lor; `company_id` pe `search`, `read`, `aggregate`, `create`, `write` și `list_attachments` lucrează într-o singură companie. Fără el, citirea acoperă toate companiile utilizatorului, iar înregistrările noi merg la compania principală.
- **Monitorizare**: `GET /mcp/health` răspunde fără autentificare și fără date.
- **Audit**: *Call Log* (utilizator, client, unealtă, argumente, durată, rezultat, aplicația OAuth; erorile în roșu; conectările refuzate sunt înregistrate ca *authentication* / *Denied*), cu secțiunea **Changes** (valoarea veche și nouă a fiecărui câmp modificat, sau statusul înainte/după pentru un buton) și filtrul *With changes*; *Daily Usage* (consum pe utilizator și zi, față de bugetul politicii). Jurnalul se șterge după 90 de zile (configurabil). Poate sprijini obligațiile de păstrare a evidenței și supraveghere umană din Regulamentul UE 2024/1689 (art. 12 și 26), fără a face sistemul conform prin el însuși.
- **Protocol**: MCP 2026-07-28 (fără stare, fără handshake), cu suport pentru clienții din 2025-11-25 și mai vechi.
- **Compatibilitate** cu serverul MCP integrat în Odoo 20 Enterprise: același endpoint (`/mcp`) și același scope de cheie (`mcp`), deci clienții își păstrează configurația la upgrade. Pe 20.0 modulul extinde *AI MCP Server* (`ai_mcp`) în loc să-l înlocuiască: cheile (din *My Profile > Account Security*, scope *MCP*) și serverul OAuth sunt cele standard, uneltele generice `ai_tool_*` ale aplicațiilor AI sunt ascunse pe `/mcp`, iar utilizatorii conectați prin OAuth în 19.0 se reconectează o dată.
- Pașii de configurare pentru consultant sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_setup`

#### 4. Componente Cheie

**Modele**

- `deltatech.mcp.server`: logica protocolului MCP (inițializare, listarea și apelarea uneltelor).
- `deltatech.mcp.policy` / `deltatech.mcp.policy.line`: politica de acces și liniile ei (model, drepturi, câmpuri ascunse/mascate/read-only, *Only these writable*, limite).
- `deltatech.mcp.policy.template` / `deltatech.mcp.policy.template.line`: șabloanele de politici, cu modelele, câmpurile și metodele-buton scrise ca text.
- `deltatech.mcp.policy.template.wizard` (transient): *Create from Template* / *Add Template*.
- `deltatech.mcp.tool`: uneltele proprii definite de administrator (acțiune de server sau metodă de model).
- `deltatech.mcp.prompt` / `deltatech.mcp.prompt.argument`: prompturile gata făcute și argumentele lor.
- `deltatech.mcp.log`: jurnalul apelurilor, inclusiv modificările făcute (*Changes*).
- `deltatech.mcp.usage`: consumul zilnic pe utilizator.
- `deltatech.mcp.oauth.client` / `deltatech.mcp.oauth.code` / `deltatech.mcp.oauth.connection`: aplicațiile OAuth, codurile de autorizare și conexiunile aprobate (cu tokeni stocați doar ca hash).
- `deltatech.mcp.key.wizard` (transient): generarea cheii API pentru endpoint-ul `/mcp`.
- `ir.http` (extins): autentificarea `mcp_key`, cheia fiind acceptată doar pe `/mcp`.
- `res.users` (extins): politica atribuită utilizatorului.
- `res.config.settings` (extins): scrierea permisă, OAuth, limite generale.

**Vizualizări**

- `mcp_policy_view_form` / `mcp_policy_view_list`: politicile de acces, cu butoanele *Create from Template*, *Add Template* și *Save as Template*.
- `mcp_policy_template_view_form` / `mcp_policy_template_view_list` / `mcp_policy_template_wizard_view_form`: șabloanele și wizardul.
- `mcp_tool_view_form` / `mcp_tool_view_list`: uneltele proprii.
- `mcp_prompt_view_form` / `mcp_prompt_view_list` / `mcp_prompt_view_search`: prompturile.
- `mcp_oauth_client_view_form` / `mcp_oauth_client_view_list`: aplicațiile OAuth.
- `mcp_oauth_connection_view_form` / `mcp_oauth_connection_view_list` / `mcp_oauth_connection_view_search`: conexiunile OAuth.
- `mcp_log_view_list` / `mcp_log_view_form`: jurnalul apelurilor.
- `mcp_usage_view_list`: consumul zilnic.
- `mcp_key_wizard_view_form`: generarea cheii API.
- `res_users_view_form_mcp`: atribuirea politicii pe utilizator (tab *Access Rights*).
- `res_config_settings_view_form_mcp`: setările *MCP Server*.
- `mcp_oauth_templates.xml`: pagina de consimțământ OAuth (*Allow* / *Deny*).

**Acțiuni Automate / Acțiuni Server**

- Date: cele 8 șabloane livrate (`data/mcp_policy_template_data.xml`). Nu definește `ir.cron` sau acțiuni server. Endpoint-uri HTTP: `/mcp` (POST/GET/DELETE), `/mcp/health` (GET) și `/oauth/mcp/*` (`register`, `authorize`, `consent`, `token`, `revoke`).

#### 5. Conexiuni

- Nu există legături funcționale verificate în cod cu alte module cu pagină wiki (modulul depinde doar de `base_setup`).
