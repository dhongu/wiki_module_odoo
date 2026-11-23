# MCP Server - Governed AI Access for Claude & ChatGPT (localizat la `deltatech_mcp_server/index.md`)

- **Nume Tehnic:** `deltatech_mcp_server`
- **Versiune:** `19.0.1.19.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_mcp_server
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_mcp_server`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul transformă Odoo într-un server MCP (Model Context Protocol), astfel încât aplicații AI precum Claude, ChatGPT, Cursor sau Codex să poată accesa datele din Odoo într-un mod pe care îl poți explica unui auditor. Funcționează pe Community și pe Enterprise, fără modulul Odoo AI și fără un serviciu extern intermediar. Asistentul lucrează mereu cu drepturile Odoo ale persoanei care l-a conectat, iar administratorul stabilește prin politici pe roluri ce modele și câmpuri sunt expuse. Accesul suplimentar este aprobat de o persoană și se oprește singur, datele personale sunt mascate implicit, iar fiecare apel este înregistrat pe serverul propriu, inclusiv valoarea veche și cea nouă a câmpurilor modificate.

#### 2. Funcționalități Cheie

- **Conectare** la `https://<odoo>/mcp` prin OAuth 2.1 cu PKCE (Claude.ai, ChatGPT, Codex: descoperire, auto-înregistrare, token de acces de scurtă durată, token de reîmprospătare rotit, scope-uri *read* / *write*) sau prin cheie API valabilă doar pe `/mcp` și refuzată pe XML-RPC/JSON (Claude Code, Cursor). Cheia se generează din *MCP Server > My Access > Generate API Key* și se afișează o singură dată.
- **Conexiuni OAuth** (*MCP Server > My Access > OAuth Connections*): token de acces de 60 de minute implicit; refolosirea tokenului de reîmprospătare închide conexiunea (*Refresh token used twice*). Pagina de consimțământ oferă *Read only* când clientul cere scriere și serverul o permite; o scriere încercată totuși este refuzată (*Denied*). Fiecare utilizator își revocă propriile conexiuni, administratorul pe toate; conexiunea neutilizată expiră (30 de zile implicit, din Setări).
- **Utilizator dedicat AI**: se pot conecta doar membrii grupului *MCP Server / User*; se recomandă un utilizator separat, nu un administrator. Drepturile de acces și regulile de înregistrare Odoo se aplică mereu; politica le poate doar restrânge.
- **Politică de acces** per utilizator (*MCP Server > Configuration > Policies*): modelele permise, cu drepturi separate de citire, creare și scriere, controlul câmpurilor (ascunse, doar unele vizibile sau mascate ca `***`), câmpuri *Read-only*, *Only these writable*, precum și drepturile per model *Notes and activities*, *Attachments*, *Delete* și *Send emails*.
- **Șabloane de politici** (*Policy Templates*): wizardul *Create from Template* construiește o politică dintr-unul sau mai multe profiluri: *Support*, *Sales*, *Purchase*, *Product Catalog*, *Product Prices*, *Stock*, *Accounting* și *Reporting*. Modelele modulelor neinstalate se sar, cu notificare; mai multe șabloane se combină (drepturile se adună, limita cea mai strictă câștigă). *Add Template* și *Save as Template* sunt pe politică. Șablonul nu dă drepturi Odoo.
- **Cereri de acces** (*My Access > Access Requests*), dezactivate implicit (setarea *MCP access requests*, cu *MCP access approver* opțional): utilizatorul, sau clientul AI prin `request_access`, cere cu motiv o operație (read, create, write, notes and activities, attachments, delete, email) pe un model. Aprobatorul poate schimba *Valid Until* și aprobă sau refuză. Accesul aprobat este o linie personală a politicii (tab *Personal Access*), doar pentru acel utilizator, păstrează restricțiile de câmp ale politicii și se oprește singur la data de sfârșit; *Revoke* îl oprește imediat. Un utilizator are cel mult cinci cereri în așteptare.
- **Date personale** (CUI/TVA, IBAN, CNP, data nașterii, salariu) mascate implicit și protejate împotriva deducerii prin filtre, sortări sau agregări.
- **Limite per politică**: înregistrări per apel, buget zilnic de înregistrări și de date, apeluri pe minut (numărate din jurnalul din baza de date, deci identic pe toți workerii) și adrese IP permise.
- **Doar citire implicit**: uneltele de scriere rămân ascunse până la bifarea *Allow AI clients to write* în Setări și a drepturilor pe modele. `create` și `write` nu schimbă niciodată statusul unui document și nu scriu câmpuri calculate sau marcate *Read-only*; statusul se schimbă doar printr-o unealtă-buton. Ștergerea și trimiterea de emailuri sunt drepturi separate, oprite implicit. Câmpurile binare și modelele de sistem (`ir.*`, chei API, grupuri) nu se expun niciodată.
- **Unelte de citire**: `whoami`, `list_models`, `describe_model`, `search`, `count`, `name_search` (doar pe câmpurile de nume vizibile în politică), `read`, `aggregate` și `glossary` (când glosarul are termeni).
- **Unelte pentru fișiere** (pe modelele cu *Attachments*): `list_attachments` și `read_attachment` (text, imagini, PDF, până la dimensiunea maximă din Setări, 5 MB implicit, și în mod doar-citire), `print_report` (PDF-ul rapoartelor modelului, nesalvat pe document) și `attach_file` (cu scrierea activată).
- **Unelte de scriere** (cu scrierea activată): `create` (o înregistrare sau o listă), `find_or_create`, `copy`, `write`, `post_message` (notă internă în chatter, niciodată trimisă urmăritorilor), `schedule_activity` (necesită Discuss); `unlink` și `send_email` (din șabloanele de email ale modelului) doar unde politica le acordă. `request_access` apare când cererile de acces sunt activate.
- **Unelte proprii** (*MCP Server > Configuration > Tools*): o acțiune de server, o metodă-buton a unui model (`action_*`, `button_*` sau declarată în `_mcp_methods`, ex. `action_confirm` pe comenzi de vânzare) sau un tip **Aggregate**: o metrică numită, cu domeniu fix, grupare și totaluri (ex. restanța pe client), pe care AI-ul o apelează în loc să ghicească. Fiecare unealtă se activează per politică și rulează cu drepturile utilizatorului conectat. Butoanele care deschid dialog sunt refuzate; parametrii ajung în acțiunea de server prin `env.context["mcp_arguments"]`.
- **Glosar** (*MCP Server > Configuration > Glossary*): termenii afacerii (înțeles, sinonime, model, domeniu exemplu), citiți de AI prin `glossary`; sunt vizibili doar termenii modelelor pe care politica le poate citi.
- **Prompturi** (*MCP Server > Configuration > Prompts*): întrebări gata făcute cu argumente `{{nume}}`, oferite politicilor alese (sau tuturor, dacă lista e goală); apar în clientul AI ca comenzi.
- **Mai multe companii**: `whoami` listează companiile; `company_id` pe uneltele de citire și scriere lucrează într-o singură companie. Fără el, citirea acoperă toate companiile utilizatorului, iar înregistrările noi merg la compania principală.
- **Monitorizare**: `GET /mcp/health` răspunde fără autentificare și fără date.
- **Meniu pe roluri** (*MCP Server*): *My Access*, *Reporting* (*Daily Usage*, *Call Log*) și *Configuration* (*Settings*, *Policies*, *Policy Templates*, *Tools*, *Glossary*, *Prompts*, *OAuth Applications*). Un utilizator MCP fără drepturi de administrator vede doar *My Access*.
- **Audit**: *Call Log* (utilizator, client, unealtă, argumente, durată, rezultat, aplicația OAuth; conectările refuzate sunt înregistrate), cu secțiunea **Changes** (valoarea veche și nouă a fiecărui câmp, sau statusul înainte/după pentru un buton) și filtrul *With changes*; *Daily Usage* arată consumul pe utilizator față de buget. Jurnalul se șterge după 90 de zile (configurabil). Poate sprijini obligațiile de păstrare a evidenței și supraveghere umană din Regulamentul UE 2024/1689 (art. 12 și 26), fără a face sistemul conform prin el însuși.
- **Protocol**: MCP 2026-07-28 (fără stare, fără handshake), cu suport pentru clienții din 2025-11-25 și mai vechi.
- **Compatibilitate** cu serverul MCP integrat în Odoo 20: același endpoint (`/mcp`) și același scope de cheie (`mcp`), deci clienții își păstrează configurația la upgrade.
- **Interfață în română**: traducere completă (`i18n/ro.po`) pentru interfață, șabloane și mesajele returnate clientului AI.
- Pașii de configurare pentru consultant sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_setup`

#### 4. Componente Cheie

**Modele**

- `deltatech.mcp.server`: logica protocolului MCP (inițializare, listarea și apelarea uneltelor).
- `deltatech.mcp.policy` / `deltatech.mcp.policy.line`: politica de acces și liniile ei (model, drepturi, câmpuri ascunse/mascate/read-only, *Only these writable*, limite); liniile personale au prioritate față de linia politicii pentru același model.
- `deltatech.mcp.policy.template` / `deltatech.mcp.policy.template.line`: șabloanele de politici, cu modelele, câmpurile și metodele-buton scrise ca text.
- `deltatech.mcp.policy.template.wizard` (transient): *Create from Template* / *Add Template*.
- `deltatech.mcp.access.request`: cererea de acces, aprobată sau refuzată de aprobator; la aprobare generează linia personală a politicii.
- `deltatech.mcp.tool`: uneltele proprii (acțiune de server, metodă de model sau metrică *Aggregate*).
- `deltatech.mcp.glossary`: termenii afacerii expuși prin unealta `glossary`.
- `deltatech.mcp.prompt` / `deltatech.mcp.prompt.argument`: prompturile gata făcute și argumentele lor.
- `deltatech.mcp.log`: jurnalul apelurilor, inclusiv modificările făcute (*Changes*).
- `deltatech.mcp.usage`: consumul zilnic pe utilizator.
- `deltatech.mcp.oauth.client` / `deltatech.mcp.oauth.code` / `deltatech.mcp.oauth.connection`: aplicațiile OAuth, codurile de autorizare și conexiunile aprobate.
- `deltatech.mcp.key.wizard` (transient): generarea cheii API pentru `/mcp`.
- `ir.http` (extins): autentificarea `mcp_key`, cheia fiind acceptată doar pe `/mcp`.
- `res.users` (extins): politica atribuită utilizatorului.
- `res.config.settings` (extins): scrierea permisă, OAuth, limite generale, cererile de acces și aprobatorul.

**Vizualizări**

- `mcp_policy_view_form` / `mcp_policy_view_list`: politicile de acces.
- `mcp_policy_template_view_form` / `mcp_policy_template_view_list` / `mcp_policy_template_wizard_view_form`: șabloanele și wizardul.
- `mcp_access_request_view_form` / `mcp_access_request_view_list` / `mcp_access_request_view_search`: cererile de acces.
- `mcp_tool_view_form` / `mcp_tool_view_list` / `mcp_tool_view_search`: uneltele proprii.
- `mcp_glossary_view_form` / `mcp_glossary_view_list` / `mcp_glossary_view_search`: glosarul.
- `mcp_prompt_view_form` / `mcp_prompt_view_list` / `mcp_prompt_view_search`: prompturile.
- `mcp_oauth_client_view_form` / `mcp_oauth_client_view_list`: aplicațiile OAuth.
- `mcp_oauth_connection_view_form` / `mcp_oauth_connection_view_list` / `mcp_oauth_connection_view_search`: conexiunile OAuth.
- `mcp_log_view_list` / `mcp_log_view_form`: jurnalul apelurilor.
- `mcp_usage_view_list`: consumul zilnic.
- `mcp_key_wizard_view_form`: generarea cheii API.
- `res_users_view_form_mcp`: atribuirea politicii pe utilizator.
- `res_config_settings_view_form_mcp`: setările *MCP Server*.
- `mcp_menus.xml`: meniul *My Access* / *Reporting* / *Configuration*.
- `mcp_oauth_templates.xml`: pagina de consimțământ OAuth (*Allow* / *Deny*).

**Acțiuni Automate / Acțiuni Server**

- Date: cele 8 șabloane livrate (`data/mcp_policy_template_data.xml`). Nu definește `ir.cron` sau acțiuni server; curățarea se face prin metode `@api.autovacuum` (jurnalul vechi, aplicațiile OAuth nefolosite, conexiunile și codurile OAuth expirate sau închise, liniile personale expirate).
- Endpoint-uri HTTP: `/mcp` (POST/GET/DELETE), `/mcp/health` (GET) și `/oauth/mcp/*` (`register`, `authorize`, `consent`, `token`, `revoke`).

#### 5. Conexiuni

- Nu există legături funcționale verificate în cod cu alte module cu pagină wiki (modulul depinde doar de `base_setup`).
