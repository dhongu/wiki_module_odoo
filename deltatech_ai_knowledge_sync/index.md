# AI - Knowledge Sync

- **Nume Tehnic:** `deltatech_ai_knowledge_sync`
- **Versiune:** `20.0.2.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_knowledge_sync
- **Cale Locală:** odoo-addons/bitshop_ent/deltatech_ai_knowledge_sync
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În Odoo 20 Enterprise, articolele din Knowledge sunt surse standard pentru un agent AI: din fila *Sources*, opțiunea *Add › Add from Knowledge* adaugă un articol împreună cu subarticolele sale, ca folder, câte o sursă per articol, fiecare cu propriile embeddings. Standardul păstrează aceste surse așa cum au fost adăugate. Modulul le ține la zi: când un articol este editat, mutat sau șters, agentul răspunde pe baza conținutului actual, fără re-indexare manuală.

#### 2. Funcționalități Cheie

- **Articolele editate sunt re-indexate**: un articol al cărui nume sau text se schimbă este re-încorporat de cronul standard de embeddings după câteva minute (editorul salvează în timpul scrierii). Un articol redenumit își redenumește și sursele.
- **Articolele noi sau mutate intră în folder**: un articol creat sau mutat sub un articol adăugat cu subarticole primește sursă; unul mutat în altă parte, arhivat sau șters o pierde. Standardul face asta doar la re-indexarea manuală a folderului.
- **Verificare zilnică**: acțiunea programată *AI: synchronize the Knowledge folder sources* verifică încă o dată toate folderele; poate fi rulată manual (*Run Manually*) când o modificare nu a ajuns la agent.
- **Upgrade din Odoo 19**: *Followed Articles* ale unui agent devin surse Knowledge standard (articolul și subarticolele lui), în locul surselor de tip text din Odoo 19.
- **Configurare**: în *AI › Agents*, fila *Sources*, se adaugă articolul rădăcină (ex. *Documentation*) cu *Include child articles*; fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `ai_agentic`
- `ai_knowledge`

#### 4. Componente Cheie

**Modele**

- `ai.agent` (extins): sincronizarea surselor de tip folder Knowledge ale agentului.
- `knowledge.article` (extins): reacție la creare, editare, mutare, arhivare și ștergere de articole.

**Vizualizări**

- Fără vizualizări proprii; modulul lucrează în fila *Sources* a agentului standard.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_knowledge_sync` (*AI: synchronize the Knowledge folder sources*): rulează zilnic și verifică toate folderele de surse Knowledge.

#### 5. Conexiuni

- `ai`: agenții AI standard Odoo, ale căror surse sunt sincronizate.
