# AI Dashboard Assistant

- **Nume Tehnic:** `deltatech_dashboard_builder_ai`
- **Versiune:** `20.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_dashboard_builder_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_dashboard_builder_ai`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă un agent Odoo AI, **Dashboard Assistant**, care redactează tablouri de bord la cerere („vânzări pe lună și top clienți") și modifică tablourile existente. Asistentul vede doar structura modelelor, niciodată datele: tabloul este calculat de Odoo, cu drepturile utilizatorului, la deschidere.

#### 2. Funcționalități Cheie

- **Vede structura, nu datele**: AI-ul primește doar nume de modele și câmpuri; nicio înregistrare sau cifră nu pleacă spre serviciul AI.
- **Ciornă, nu surpriză**: rezultatul este o ciornă vizibilă doar constructorilor, care o verifică și apasă **Publish**.
- **Verificare pe baza reală**: fiecare model și câmp propus este validat (inclusiv tipul); un widget greșit anulează întreaga propunere, iar asistentul află motivul și corectează.
- **Editează tablouri existente**: citește structura (widgeturi și setări), apoi modifică, șterge sau reordonează widgeturi, redenumește tabloul sau schimbă perioada; modificarea e „totul sau nimic", un tablou publicat rămâne publicat, iar chatterul păstrează o notă.
- **Fiecare widget își amintește de ce există**: cererile care l-au creat sunt păstrate (**AI context**); în modul editare, butonul AI al widgetului deschide asistentul pe acel widget.
- **Formule între KPI-uri** (marjă, valoare medie a comenzii).
- **Doar drepturile utilizatorului**: uneltele rulează ca utilizatorul; fără grupul *Dashboards / Builder* cererea este refuzată.
- **Doar propria abilitate**: agentul primește doar skill-ul *Dashboard builder*, nu pe cele native care caută și modifică înregistrări.
- **Explicarea cifrelor este opțională**: skill-ul *Dashboard insights (sends figures to the AI provider)* nu e legat de niciun agent; atașarea lui este decizia de a trimite cifrele către AI.
- Utilizare: **AI ▸ Agents ▸ Dashboard Assistant**; ciornele apar în **KPI Dashboards ▸ Configuration ▸ Dashboards** cu panglica **Draft**. Rulează pe Odoo AI (`ai`, `ai_agentic`, Enterprise) și consumă credite.
- Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_dashboard_builder](../deltatech_dashboard_builder/index.md)
- `ai_agentic`

#### 4. Componente Cheie

**Modele**

- `deltatech.dashboard` (extins): ciornă/publicare, note în chatter la modificările AI.
- `deltatech.dashboard.item` (extins): contextul AI al widgetului.

**Vizualizări**

- `view_deltatech_dashboard_item_form_ai`: butonul AI și câmpul **AI context** pe formularul widgetului.

**Acțiuni Automate / Acțiuni Server**

- Unelte AI (`ir.actions.server`): `ai_tool_dashboard_list`, `ai_tool_dashboard_find_models`, `ai_tool_dashboard_describe_model`, `ai_tool_dashboard_propose`, `ai_tool_dashboard_read`, `ai_tool_dashboard_update_widgets`, `ai_tool_dashboard_delete_widgets`, `ai_tool_dashboard_reorder_widgets`, `ai_tool_dashboard_update`, `ai_tool_dashboard_facts`.
- `ai_skill_dashboard_builder` și `ai_skill_dashboard_insights` (`ai.skill`); `ai_agent_dashboard_builder` (`ai.agent`).

#### 5. Conexiuni

- `ai`: framework-ul Odoo AI pe care rulează agentul.
- `deltatech_web_kpi_cards`: cardurile KPI folosite de tablouri.
