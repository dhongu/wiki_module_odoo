# Deltatech MCP Server

- **Nume Tehnic:** `deltatech_mcp_server`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_mcp_server
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_mcp_server`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul transformă Odoo într-un server MCP (Model Context Protocol), astfel încât aplicații AI precum Claude, ChatGPT sau Cursor să poată citi, iar dacă se permite explicit și modifica, datele din Odoo. Funcționează pe Community și pe Enterprise și nu depinde de modulul Odoo AI. Asistentul vede exact ce are voie să vadă utilizatorul cu care s-a conectat, iar administratorul stabilește prin politici de acces ce modele și câmpuri sunt expuse, ce date personale sunt mascate și ce limite de consum se aplică. Fiecare apel este înregistrat, deci există evidență a ceea ce a făcut asistentul.

#### 2. Funcționalități Cheie

- **Conectare** la `https://<odoo>/mcp` prin cheie API valabilă doar pe acest endpoint (Claude Code, Cursor) sau prin OAuth 2.1 cu PKCE, cu descoperire și auto-înregistrare (Claude.ai, ChatGPT, Codex). Cheia se generează din *MCP Server > Generate API Key*, de către utilizatorul AI, și se afișează o singură dată.
- **Utilizator dedicat AI**: pot să se conecteze doar membrii grupului *MCP Server / User*; se recomandă un utilizator separat, nu un administrator. Se aplică mereu drepturile de acces și regulile de înregistrare normale.
- **Politică de acces** per utilizator (*MCP Server > Policies*): lista modelelor permise, cu drepturi separate de citire, creare și scriere, și controlul câmpurilor (ascunse, doar unele vizibile sau mascate ca `***`).
- **Date personale** (CUI/TVA, IBAN, CNP, data nașterii, salariu) mascate implicit și protejate împotriva deducerii prin filtre, sortări sau agregări.
- **Limite per politică**: înregistrări per apel, buget zilnic de înregistrări și de date, apeluri pe minut, adrese IP permise.
- **Doar citire implicit**: uneltele `create` și `write` rămân ascunse până la bifarea *Allow AI clients to write* în Setări și a drepturilor pe modelele dorite. Nu există unealtă de ștergere, câmpurile cu linii (one2many, many2many) nu se pot scrie, iar câmpurile binare și modelele de sistem (`ir.*`, chei API, grupuri) nu se expun niciodată.
- **Unelte standard** pentru clientul AI: `whoami`, `list_models`, `describe_model`, `search`, `read`, `aggregate` și, cu scrierea activată, `create` și `write`.
- **Unelte proprii** (*MCP Server > Tools*): o acțiune de server sau o metodă-buton a unui model (ex. `action_confirm` pe comenzi de vânzare), activată per politică și rulată cu drepturile utilizatorului conectat. Se acceptă doar metodele care încep cu `action_` sau `button_` ori sunt declarate de model în `_mcp_methods`. Dacă butonul deschide un dialog, apelul este refuzat și nu se modifică nimic.
- **Aplicații OAuth** (*MCP Server > OAuth Applications*): aplicațiile care pot cere acces; pot fi adăugate manual sau arhivate. Accesul apare ca cheie API *OAuth: <aplicație>* în preferințele utilizatorului și expiră după numărul de zile din Setări. Auto-înregistrarea și gazdele permise se configurează în *Setări > Integrări > MCP Server*.
- **Audit**: *Call Log* (fiecare apel: utilizator, unealtă, argumente, durată, rezultat; erorile în roșu) și *Daily Usage* (consum pe utilizator și zi, față de bugetul politicii); jurnalul se șterge după 90 de zile.
- **Compatibilitate** cu serverul MCP integrat în Odoo 20 Enterprise: același endpoint (`/mcp`) și același scope de cheie (`mcp`), deci clienții își păstrează configurația la upgrade.
- Pașii de configurare pentru consultant sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_setup`

#### 4. Componente Cheie

**Modele**

- `deltatech.mcp.server`: logica protocolului MCP (inițializare, listarea și apelarea uneltelor).
- `deltatech.mcp.policy` / `deltatech.mcp.policy.line`: politica de acces și liniile ei (model, drepturi, câmpuri ascunse/mascate, limite).
- `deltatech.mcp.tool`: uneltele proprii definite de administrator (acțiune de server sau metodă de model).
- `deltatech.mcp.log`: jurnalul apelurilor.
- `deltatech.mcp.usage`: consumul zilnic pe utilizator.
- `deltatech.mcp.oauth.client` / `deltatech.mcp.oauth.code`: aplicațiile OAuth și codurile de autorizare.
- `deltatech.mcp.key.wizard` (transient): generarea cheii API pentru endpoint-ul `/mcp`.
- `ir.http` (extins): autentificarea `mcp_key`, cheia fiind acceptată doar pe `/mcp`.
- `res.users` (extins): politica atribuită utilizatorului.
- `res.config.settings` (extins): scrierea permisă, OAuth, limite generale.

**Vizualizări**

- `mcp_policy_view_form` / `mcp_policy_view_list`: politicile de acces.
- `mcp_tool_view_form` / `mcp_tool_view_list`: uneltele proprii.
- `mcp_oauth_client_view_form` / `mcp_oauth_client_view_list`: aplicațiile OAuth.
- `mcp_log_view_list` / `mcp_log_view_form`: jurnalul apelurilor.
- `mcp_usage_view_list`: consumul zilnic.
- `mcp_key_wizard_view_form`: generarea cheii API.
- `res_users_view_form_mcp`: atribuirea politicii pe utilizator (tab *Access Rights*).
- `res_config_settings_view_form_mcp`: setările *MCP Server*.
- `mcp_oauth_templates.xml`: pagina de consimțământ OAuth (*Allow* / *Deny*).

**Acțiuni Automate / Acțiuni Server**

- Nu definește `ir.cron` sau acțiuni server. Endpoint-uri HTTP: `/mcp` (POST/GET/DELETE) și `/oauth/mcp/*` (`register`, `authorize`, `consent`, `token`, `revoke`).

#### 5. Conexiuni

- Nu există legături funcționale verificate în cod cu alte module cu pagină wiki (modulul depinde doar de `base_setup`).
