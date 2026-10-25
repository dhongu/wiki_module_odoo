# Dashboard Builder AI

- **Nume Tehnic:** `deltatech_dashboard_builder_ai`
- **Versiune:** `19.0.1.3.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_dashboard_builder_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_dashboard_builder_ai`
- **Ultima Ingestie:** `2026-10-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite utilizatorilor să ceară AI-ului din Odoo să schițeze un tablou de bord și să modifice tablourile existente. Utilizatorul descrie ce vrea să vadă (de exemplu „vânzări pe lună și top clienți") sau ce vrea să schimbe („arată comenzile pe săptămână, nu pe lună"), iar **Dashboard Assistant** găsește modelele potrivite, le verifică câmpurile și construiește sau modifică widgeturile, pentru ca utilizatorul să le verifice. Asistentul vede doar structura (nume de modele și câmpuri), niciodată datele: cifrele sunt calculate de Odoo, cu drepturile utilizatorului, la deschiderea tabloului.

#### 2. Funcționalități Cheie

- **Structura, nu datele:** furnizorului AI i se trimit doar numele modelelor și ale câmpurilor; nicio înregistrare și nicio cifră nu pleacă din Odoo.
- **Ciornă, nu surpriză:** un tablou nou este creat în stare *Draft* (panglică „Draft"), vizibil doar constructorilor de tablouri. Aceștia verifică widgeturile și apasă **Publish**.
- **Verificat pe baza de date reală:** fiecare model și câmp propus este validat, inclusiv tipul. Un widget greșit anulează întreaga propunere (totul sau nimic), iar asistentul primește motivul și poate corecta. Căutarea modelelor înțelege cum scriu oamenii (cuvinte din numele tehnic sau din numele în limba utilizatorului), iar descrierea unui model include valorile câmpurilor de tip selecție.
- **Tipuri de widget propuse:** pe lângă KPI, grafice și tabele, asistentul propune indicator tip gauge (cu țintă), grafic de tip arie, pâlnie (funnel) și grafic bară + linie (cu agregatul liniei), conform tipurilor din *Dashboard Builder*. Poate seta și lățimea widgetului.
- **Formule între KPI-uri:** un KPI sau un gauge poate combina alte KPI-uri ale tabloului (de ex. marja sau valoarea medie a comenzii). Widgeturile cu formulă se creează după KPI-urile din aceeași propunere; un KPI deja existent primește un cod în loc să fie recreat.
- **Editarea unui tablou existent:** asistentul citește structura tabloului (widgeturile cu id și setări, niciodată cifrele), apoi modifică widgeturi după id (doar cheile care se schimbă), le șterge, le reordonează, redenumește tabloul sau schimbă perioada implicită. Modificarea este verificată ca un widget nou, totul sau nimic; o ștergere sau modificare care ar strica o formulă este refuzată. Un tablou publicat rămâne publicat, iar vizualizatorii văd schimbarea imediat. O notă în chatter-ul tabloului consemnează ce a schimbat asistentul (inclusiv widgeturile adăugate unui tablou existent).
- **Butonul AI pe widget și contextul lui:** în modul de editare al tabloului (pictograma creion din bara de unelte), fiecare widget are un buton AI (bagheta magică) care deschide un chat nou cu asistentul, pornind de la widget: tabloul, structura și contextul lui, fără cifre. Fiecare widget păstrează un **AI context**: câte o linie datată pentru fiecare cerere care l-a creat sau schimbat, în cuvintele utilizatorului. Contextul se citește și se corectează în formularul widgetului (butonul cu rotiță), iar după modificare se apasă butonul de reîmprospătare al tabloului. Conversațiile cu agentul AI sunt șterse de Odoo după o zi fără activitate; contextul widgetului este ceea ce rămâne între conversații. Doar pentru constructori.
- **Flux de utilizare:** chat AI ▸ alegi **Dashboard Assistant** ▸ descrii nevoia ▸ deschizi **KPI Dashboards ▸ Configuration ▸ Dashboards** ▸ verifici și publici. Pentru a adăuga sau modifica widgeturi la un tablou existent, îl numești în cerere. Pașii detaliați și capturile sunt în fișa consultantului.
- **Drepturile utilizatorului, nu mai multe:** uneltele rulează ca utilizatorul care discută cu asistentul; cine nu poate citi un model nu poate construi widget pe el. Este necesar grupul *Dashboards / Builder*: un simplu vizualizator este refuzat explicit, indiferent de topicul agentului.
- **Orice furnizor din framework-ul AI Odoo:** OpenAI, Google și, cu *Deltatech AI - Anthropic (Claude)*, Claude. Furnizorul și cheia se configurează o singură dată, în **Settings ▸ Technical ▸ AI**; pentru Claude se alege un model Claude pe agent.
- **Explicarea cifrelor este opțională:** un al doilea topic, *Dashboard insights (sends figures to the AI provider)*, permite unui agent să citească cifrele calculate și să le explice. Nu este legat de niciun agent; adăugarea lui în **Settings ▸ Technical ▸ AI ▸ Agents** este decizia explicită de a trimite cifrele către furnizor.
- Traducere în română a termenilor noi (note de chatter, AI context, mesaje de eroare); liniile contextului sunt scrise în limba utilizatorului.
- Modul comercial (20 EUR, licență OPL-1), stadiu de dezvoltare Beta.

#### 3. Dependențe

- [deltatech_dashboard_builder](../deltatech_dashboard_builder/index.md)
- `ai` (Odoo Enterprise)

#### 4. Componente Cheie

**Modele**

- `deltatech.dashboard` (extins, `models/dashboard.py`): metodele `_ai_tool_*` folosite ca unelte AI: listarea tablourilor, căutarea modelelor, descrierea unui model, propunerea de widgeturi (cu validare model/câmp/tip, creare ca ciornă sau adăugare la un tablou existent), citirea structurii, modificarea, ștergerea și reordonarea widgeturilor, redenumirea tabloului / schimbarea perioadei, verificarea formulelor, nota în chatter și citirea cifrelor (doar pentru topicul de insights).
- `deltatech.dashboard.item` (extins, `models/dashboard_item.py`): câmpul `ai_context` (istoricul cererilor care au creat/modificat widgetul) și `action_ai_edit`, care deschide chatul cu asistentul pornind de la widget.

**Vizualizări**

- `view_deltatech_dashboard_item_form_ai`: extinde formularul widgetului cu grupul **AI context**.
- Buton AI în modul de editare al tabloului (`static/src/item_tools.esm.js`, înregistrat în `itemToolsRegistry`, pictograma `fa-magic`).

**Acțiuni Automate / Acțiuni Server**

- Unelte de citire/propunere: `ai_tool_dashboard_list`, `ai_tool_dashboard_find_models`, `ai_tool_dashboard_describe_model`, `ai_tool_dashboard_propose`.
- Unelte de editare: `ai_tool_dashboard_read` (citire structură), `ai_tool_dashboard_update_widgets`, `ai_tool_dashboard_delete_widgets`, `ai_tool_dashboard_reorder_widgets`, `ai_tool_dashboard_update` (redenumire / perioadă implicită).
- `ai_tool_dashboard_facts`: unealta de citire a cifrelor (folosită doar de topicul de insights).
- `ai_topic_dashboard_builder`: topic AI cu instrucțiunile și toate uneltele de construire și editare.
- `ai_topic_dashboard_insights`: topic opțional pentru explicarea cifrelor, nelegat de niciun agent.
- `ai_agent_dashboard_builder`: agentul **Dashboard Assistant**.

Nu există cron-uri. Topicurile și uneltele sunt date de configurare: la o actualizare pe o bază existentă, textul nou trebuie copiat din `data/ai_topic.xml` și `data/ai_tools.xml`.

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): adaugă Claude ca furnizor în framework-ul AI Odoo; folosit opțional cu asistentul.
