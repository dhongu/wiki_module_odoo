# Dashboard Builder AI

- **Nume Tehnic:** `deltatech_dashboard_builder_ai`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_dashboard_builder_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_dashboard_builder_ai`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite utilizatorilor să ceară AI-ului din Odoo să schițeze un tablou de bord. Utilizatorul descrie ce vrea să vadă (de exemplu „vânzări pe lună și top clienți"), iar **Dashboard Assistant** găsește modelele potrivite, le verifică câmpurile și construiește widgeturile unui tablou pe care utilizatorul îl verifică. Asistentul vede doar structura (nume de modele și câmpuri), niciodată datele: cifrele sunt calculate de Odoo, cu drepturile utilizatorului, la deschiderea tabloului.

#### 2. Funcționalități Cheie

- **Structura, nu datele:** furnizorului AI i se trimit doar numele modelelor și ale câmpurilor; nicio înregistrare și nicio cifră nu pleacă din Odoo.
- **Ciornă, nu surpriză:** rezultatul este un tablou în stare *Draft* (panglică „Draft"), vizibil doar constructorilor de tablouri. Aceștia verifică widgeturile și apasă **Publish**.
- **Verificat pe baza de date reală:** fiecare model și câmp propus este validat, inclusiv tipul. Un widget greșit anulează întreaga propunere, iar asistentul primește motivul și poate corecta.
- **Drepturile utilizatorului, nu mai multe:** uneltele rulează ca utilizatorul care discută cu asistentul; cine nu poate citi un model nu poate construi widget pe el, iar un simplu vizualizator nu poate crea tablouri (este necesar grupul *Dashboards / Builder*).
- **Flux de utilizare:** chat AI ▸ alegi **Dashboard Assistant** ▸ descrii nevoia ▸ deschizi **KPI Dashboards ▸ Configuration ▸ Dashboards** ▸ verifici și publici. Pentru a adăuga widgeturi la un tablou existent, îl numești în cerere.
- **Orice furnizor din framework-ul AI Odoo:** OpenAI, Google și, cu *Deltatech AI - Anthropic (Claude)*, Claude. Furnizorul și cheia se configurează o singură dată, în **Settings ▸ Technical ▸ AI**.
- **Explicarea cifrelor este opțională:** un al doilea topic, *Dashboard insights (sends figures to the AI provider)*, permite unui agent să citească cifrele calculate și să le explice. Nu este legat de niciun agent; adăugarea lui în **Settings ▸ Technical ▸ AI ▸ Agents** este decizia explicită de a trimite cifrele către furnizor.
- Modul comercial (20 EUR, licență OPL-1), stadiu de dezvoltare Beta.

#### 3. Dependențe

- [deltatech_dashboard_builder](../deltatech_dashboard_builder/index.md)
- `ai` (Odoo Enterprise)

#### 4. Componente Cheie

**Modele**

- `deltatech.dashboard` (extins, `models/dashboard.py`): metode folosite ca unelte AI: listarea tablourilor, căutarea modelelor, descrierea unui model (câmpuri), propunerea de widgeturi (cu validare model/câmp/tip și creare ca ciornă) și citirea cifrelor unui tablou (doar pentru topicul de insights).

**Vizualizări**

- Modulul nu adaugă vizualizări proprii; tabloul creat apare în vizualizările din `deltatech_dashboard_builder`.

**Acțiuni Automate / Acțiuni Server**

- `ai_tool_dashboard_list`, `ai_tool_dashboard_find_models`, `ai_tool_dashboard_describe_model`, `ai_tool_dashboard_propose`: acțiuni server care expun uneltele către agent.
- `ai_tool_dashboard_facts`: unealta de citire a cifrelor (folosită doar de topicul de insights).
- `ai_topic_dashboard_builder`: topic AI cu instrucțiunile și uneltele de construire.
- `ai_topic_dashboard_insights`: topic opțional pentru explicarea cifrelor, nelegat de niciun agent.
- `ai_agent_dashboard_builder`: agentul **Dashboard Assistant**.

Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): adaugă Claude ca furnizor în framework-ul AI Odoo; folosit opțional cu asistentul.
