# Advanced Planner AI Assistant (localizat la `deltatech_advanced_planner_ai/index.md`)

- **Nume Tehnic:** `deltatech_advanced_planner_ai`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_advanced_planner_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_advanced_planner_ai`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Planificatorul avansat calculează când poate fi livrată cu adevărat o comandă de vânzare, ce componente lipsesc și ce centre de lucru sunt suprasolicitate. Acest modul adaugă un asistent AI care **explică** rezultatele în limbaj simplu și **propune** măsuri: planificatorul calculează, AI-ul explică, oamenii decid. Nimic nu se modifică automat — răspunsurile sunt doar notițe sau mesaje.

#### 2. Funcționalități Cheie

- Butonul **Explain planning** pe comenzile de vânzare și pe comenzile planificate: asistentul citește rezultatul planificatorului (stare, dată calculată, componentă critică, termene furnizori, cereri de ofertă și ordine de producție, încărcarea centrelor de lucru) și postează o notiță internă cu:
  - **cauza** întârzierii (componentă, furnizor sau centru de lucru, cu zilele implicate);
  - până la trei **opțiuni** disponibile în Odoo (urgentarea unei cereri de ofertă, alt furnizor, livrare parțială, mutarea datei promise), fiecare cu efectul în zile;
  - un scurt **mesaj către client**, fără detalii interne.
- **Rezumat zilnic de planificare**: în fiecare dimineață, într-un canal Discuss, comenzile nou blocate, abaterile, centrele de lucru suprasolicitate și comenzile de lansat în ziua respectivă. Cron-ul este inactiv la instalare și se activează din setări.
- **Confidențialitate**: către furnizorul AI pleacă doar date de planificare (numere de documente, produse, cantități, date, stări, nume de furnizori, termene, încărcări). Fără prețuri, sume, nume sau contact de client.
- **Control al costurilor**: limită zilnică de cereri AI per companie (implicit 50; 0 = fără limită) și listă de audit a tuturor cererilor (utilizator, document, stare, eroare). La atingerea limitei, butonul anunță, iar rezumatul zilnic se omite până a doua zi.
- **Furnizor AI la alegere**, prin framework-ul AI din Odoo: Claude (cu modulul de furnizor Anthropic), OpenAI sau Google Gemini.
- Configurare: **Setări → Inventar → Planning AI Assistant** (activare asistent, alegerea modelului agentului *Planning Assistant*, limita zilnică, rezumatul zilnic și canalul; **Send the digest now** verifică configurarea).
- Audit: **Producție → Planificare avansată → AI Requests** (managerii de planificare).
- Cerințe: Odoo 19 Enterprise (framework AI) și modulul Advanced Planner.

#### 3. Dependențe

- [deltatech_advanced_planner](../deltatech_advanced_planner/index.md)
- `ai`

#### 4. Componente Cheie

**Modele**

- `advanced.planner.ai`: serviciul care construiește contextul de planificare, apelează agentul AI, postează răspunsul și rulează rezumatul zilnic (`_cron_daily_digest`).
- `advanced.planner.ai.request`: jurnalul de audit al cererilor AI (utilizator, document, stare, eroare), folosit și pentru limita zilnică.
- `advanced.planned.order` (extins): butonul de explicare a planificării.
- `sale.order` (extins): butonul **Explain planning**.
- `res.company` (extins): limita zilnică, activarea rezumatului și canalul.
- `res.config.settings` (extins): setările asistentului AI.

**Vizualizări**

- `views/advanced_planner_ai_request_views.xml`: lista de audit a cererilor AI.
- `views/sale_order_views.xml`: butonul în antetul comenzii de vânzare.
- `views/advanced_planned_order_views.xml`: butonul pe comanda planificată.
- `views/res_config_settings_views.xml`: secțiunea de setări a asistentului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_planning_ai_digest`: rezumatul zilnic de planificare, la 05:00; inactiv la instalare.
- `ai_agent_planner_assistant`: agentul AI *Planning Assistant* (date).
- `channel_planning_digest`: canalul Discuss *Planning digest* (date).

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): furnizor Claude pentru framework-ul AI din Odoo, folosit opțional de agent.
