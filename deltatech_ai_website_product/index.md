# AI - Asistent magazin online (localizat la `deltatech_ai_website_product/index.md`)

- **Nume Tehnic:** `deltatech_ai_website_product`
- **Versiune:** `20.0.1.2.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_website_product
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_website_product`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un agent AI din Odoo 20 Enterprise răspunde vizitatorilor magazinului online pe baza produselor publicate și citește în timp real prețul și disponibilitatea. Costul, furnizorii și notele interne nu sunt folosite niciodată.

#### 2. Funcționalități Cheie

- **O sursă per produs:** fiecare produs publicat devine sursă a agentului (nume, cod, categorii, atribute, descrierea paginii și câmpuri suplimentare alese pe agent, ex. marcă, specificații).
- **Sincronizare automată:** un produs creat, modificat, publicat, depublicat sau arhivat se sincronizează după câteva minute; un cron zilnic reverifică tot, iar un catalog mare se procesează în pași.
- **Preț și disponibilitate live:** unealta *AI: Shop Product Price and Availability* dă prețul din magazin (lista de prețuri, taxe ca în magazin), disponibilitatea (în stoc, la comandă, indisponibil) și linkul; skill-ul *Shop Assistant* o adaugă agentului — prețul și stocul vin doar din unealtă.
- **Căutare după model și an:** unealta *AI: Shop Product Search* găsește produsele ale căror nume conțin toate cuvintele vizitatorului și păstrează pe cele ale căror ani de fabricație, citiți din nume, se potrivesc; fără ani, se cere verificarea compatibilității.
- **Fotografiile vizitatorilor:** cu **Citește fotografii**, o poză trimisă în chat este descrisă de model (marcă, model, generație, ani, coduri), iar descrierea se adaugă întrebării; ce nu e sigur este marcat incert. Pozele se trimit furnizorului modelului.
- **Citări către magazin** și suport pentru **mai multe site-uri** (un agent urmărește produsele unui site).
- Configurare: în **AI › Agenți**, tab **Magazin** (site, produse, câmpuri suplimentare), skill-ul Shop Assistant pe agent, apoi regula de **Website › Configurare › Live Chat** (mai întâi pe un URL de test, ex. `?assistant=test`).

#### 3. Dependențe

- `website_sale`
- `ai_agentic`
- [deltatech_ai_source_sync](../deltatech_ai_source_sync/index.md)

#### 4. Componente Cheie

**Modele**

- `ai.agent`, `ai.agent.source`, `ai.session` (extinderi): setările magazinului pe agent, sursele-produs și sesiunile de chat.
- `product.template` (extindere): declanșează sincronizarea sursei la modificare.
- `mail.message` (extindere): citirea fotografiilor din chat.

**Vizualizări**

- `ai_agent_views`: tab-ul **Magazin** pe agent.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_product_sync`: sincronizarea produselor magazinului.
- `ir_actions_server_product_info`: unealta de preț și disponibilitate.
- `ir_actions_server_product_search`: unealta de căutare produse după model și an.
- `ai_topic_shop_assistant`: skill-ul *Shop Assistant*.

#### 5. Conexiuni

- [deltatech_ai_website_product_image](../deltatech_ai_website_product_image/index.md): adaugă căutarea după fotografie.
- [deltatech_ai_source_sync](../deltatech_ai_source_sync/index.md): mecanismul de surse și embeddings al agentului.
