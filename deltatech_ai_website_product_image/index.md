# AI - Asistent magazin: căutare după fotografie (localizat la `deltatech_ai_website_product_image/index.md`)

- **Nume Tehnic:** `deltatech_ai_website_product_image`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_website_product_image
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_website_product_image`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Agentul AI al magazinului online găsește produsele care seamănă cu fotografia trimisă de vizitator în Live Chat: o piesă, o prindere, o decorațiune al cărei nume sau cod vizitatorul nu îl cunoaște. Fotografiile produselor și ale vizitatorilor sunt trimise către Google.

#### 2. Funcționalități Cheie

- **Căutare vizuală:** fotografia fiecărui produs urmărit de agent este transformată în vector de Gemini (`gemini-embedding-2`, cheia Google); fotografia vizitatorului este comparată cu ele, iar produsele cele mai asemănătoare ajung la agent cu scorul de similaritate, apoi agentul citește prețul și disponibilitatea cu uneltele asistentului de magazin.
- **Același fel, nu aceeași mărime:** fotografia arată tipul produsului, nu dimensiunea; în teste pe 300 de produse, produsul corect a fost primul la 23 din 40 de poze și printre primele cinci la 34, iar fiecare ratare a fost același produs în altă mărime. Agentul cere dimensiunea sau codul.
- **Nimic asemănător:** produsele sub **Similaritate minimă** (0,75 implicit) nu sunt date.
- **Sincronizare automată:** o fotografie nouă sau schimbată se vectorizează după câteva minute; una neschimbată își păstrează vectorul; la atingerea cotei cheii sincronizarea continuă singură.
- **Împreună cu descrierea fotografiei:** cu *Citește fotografii* al asistentului, agentul primește și descrierea, și produsele similare.
- Configurare: cheia Gemini în **Website › Configurare › Setări** (sau `ODOO_AI_GEMINI_TOKEN`; pentru magazin se recomandă cheie plătită), apoi pe agent (tab **Magazin**) bifa **Căutare după fotografie**, **Produse per fotografie** (5) și **Similaritate minimă**; **Sincronizează acum** pornește imediat vectorizarea.
- Utilizare: vizitatorul atașează poza în chat (**+** › **Atașează fișiere**), cu sau fără întrebare.

#### 3. Dependențe

- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md)

#### 4. Componente Cheie

**Modele**

- `ai.product.image.vector`: vectorul fotografiei unui produs.
- `product.template`, `ai.agent`, `res.config.settings` (extinderi): sincronizarea pozelor, setările de căutare pe agent și cheia Gemini.

**Vizualizări**

- `ai_agent_views`: opțiunile de căutare după fotografie pe agent; `res_config_settings_views`: cheia Gemini.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_product_image_sync`: vectorizarea fotografiilor produselor.

#### 5. Conexiuni

- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md): asistentul de magazin pe care îl completează (uneltele de preț și stoc).
