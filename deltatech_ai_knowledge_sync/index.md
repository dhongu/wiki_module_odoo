# AI - Knowledge Sync (localizat la `deltatech_ai_knowledge_sync/index.md`)

- **Nume Tehnic:** `deltatech_ai_knowledge_sync`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_knowledge_sync
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_knowledge_sync`
- **Ultima Ingestie:** `2026-10-20`

#### 1. Sumar

Modulul păstrează articolele din aplicația **Knowledge** ca surse pentru un agent AI din Odoo 19 Enterprise, fără ca ele să fie adăugate manual, una câte una, și fără re-adăugare după fiecare modificare. Agentul răspunde din documentația companiei, iar citările trimit către articolul exact, nu către un întreg arbore.

#### 2. Funcționalități Cheie

- **O sursă per articol:** fiecare articol din spațiul de lucru aflat sub articolele urmărite devine o sursă separată, denumită după calea sa (ex: `Documentație › Vânzări › Avize de livrare`), cu textul exclusiv al acelui articol. Sursa standard Knowledge pune articolul și toți descendenții într-o singură sursă.
- **Sincronizare automată:** un articol adăugat, editat, mutat, redenumit, arhivat sau șters este sincronizat după câteva minute (modificările sunt grupate, fiindcă editorul salvează în timpul scrierii). Articolele nemodificate își păstrează sursa și embedding-urile; un cron zilnic reverifică totul.
- **Text românesc corect:** textul se stochează ca text simplu UTF-8, astfel încât ă, ș, ț, î, â se păstrează în embedding-uri (indexarea standard a HTML-ului păstrează doar caractere ASCII).
- **Articolele private și partajate nu sunt folosite:** doar articolele din spațiul de lucru, lizibile de toți utilizatorii interni, devin surse. Un utilizator vede citarea unui articol doar dacă îl poate citi.
- **Configurare:** în **AI › Agents**, fila **Knowledge**, se aleg în **Followed Articles** articolele-rădăcină ale documentației (ex: *Documentație*). La salvare, articolele sunt adăugate ca surse în fundal, apoi indexate de cron-ul standard AI; de acolo, modificările din Knowledge ajung singure la agent.

#### 3. Dependențe

- `ai_knowledge`
- [deltatech_ai_source_sync](../deltatech_ai_source_sync/index.md)

#### 4. Componente Cheie

**Modele**

- `ai.agent` (extins): câmpul `knowledge_article_ids` (articole urmărite), cererea de sincronizare la create/write și metodele `_sync_knowledge_sources`, `_cron_knowledge_sync`.
- `ai.agent.source` (extins): câmpul boolean `knowledge_follow`, calculul accesului utilizatorului la sursă și selecția surselor de procesat.
- `knowledge.article` (extins): la create/write solicită sincronizarea agenților care îl urmăresc; calculează calea sursei.

**Vizualizări**

- `views/ai_agent_views.xml`: fila **Knowledge** pe formularul agentului, cu articolele urmărite.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_knowledge_sync`: „AI: synchronize the followed Knowledge articles”, rulează zilnic și reverifică toate articolele urmărite.

#### 5. Conexiuni

- `ai`, `ai_knowledge`: aplicațiile standard Odoo Enterprise (agenți AI și Knowledge) pe care le extinde.
- [deltatech_ai_source_sync](../deltatech_ai_source_sync/index.md): mecanismul de sincronizare a surselor (colecții Markdown/RST din GitHub sau ZIP).
- [deltatech_ai_agent_delegate](../deltatech_ai_agent_delegate/index.md): agenții alimentați din Knowledge pot fi specialiști consultați de un agent integrator.
