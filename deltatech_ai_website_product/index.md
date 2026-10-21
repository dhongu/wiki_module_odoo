# AI - Shop Assistant

- **Nume Tehnic:** `deltatech_ai_website_product`
- **Versiune:** `19.0.1.2.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_website_product
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_website_product`
- **Ultima Ingestie:** `2026-10-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un agent AI din Odoo 19 Enterprise răspunde vizitatorilor magazinului online pe baza produselor publicate, citind în timp real prețul și disponibilitatea. Fiecare produs publicat devine o sursă de cunoștințe a agentului, sincronizată automat, iar vizitatorul poate căuta după marcă, model și an de fabricație sau poate trimite o poză în chat. Modulul este în stadiul Beta și este licențiat OPL-1 (100 EUR în Odoo Apps).

#### 2. Funcționalități Cheie

- **O sursă pe produs:** fiecare produs publicat pe magazin devine sursă a agentului, cu denumire, cod, categorii de magazin, atribute și valori, descrierea paginii de magazin și câmpuri suplimentare alese pe agent (marcă, specificații tehnice). Costul, furnizorii și notele interne nu sunt folosite niciodată.
- **Sincronizare automată:** un produs creat, modificat, publicat, depublicat sau arhivat se sincronizează după câteva minute; un produs nemodificat își păstrează sursa și embeddings. Un cron zilnic reverifică tot, iar un catalog mare se procesează pe etape, care continuă de unde s-au oprit.
- **Preț și disponibilitate live:** unealta *AI: Shop Product Price and Availability* returnează prețul din magazin (lista de prețuri, taxe afișate ca pe site), disponibilitatea (în stoc, la comandă, indisponibil) și linkul produsului. Prețul și stocul vin doar din unealtă, niciodată din surse.
- **Căutare după model și an:** unealta *AI: Shop Product Search* găsește produsele al căror nume conține toate cuvintele vizitatorului (marcă, model, tip de produs; cu sau fără diacritice) și păstrează doar produsele ai căror ani de fabricație, citiți din nume („2016 - prezent”, „02.2015 - 07.2020”, „din 2011”), se potrivesc cu anul vizitatorului. Produsele fără ani sunt indicate cu nota că trebuie verificată compatibilitatea.
- **Citirea pozelor vizitatorilor:** cu opțiunea *Read Photos*, o poză trimisă în chat (mașină, piesă, etichetă) este descrisă de modelul de limbaj al agentului (marcă, model, generație, ani, coduri și text vizibile, cel mult 2 poze redimensionate la 1024 px; o poză WEBP este convertită în JPEG înainte de trimitere). Descrierea se adaugă la întrebare și se păstrează în istoricul conversației; ce nu e sigur este marcat „uncertain”, iar agentul cere confirmarea. Pozele sunt trimise furnizorului modelului.
- **Topicul *Shop Assistant*:** adaugă ambele unelte agentului, cu reguli: răspunde în limba vizitatorului, recomandă doar produse din surse sau din unelte, cu link, nu inventează specificații, nu dă prețuri din surse și trimite către un coleg prin butonul „Ask a Human”.
- **Citări către magazin:** răspunsurile conțin linkul paginii produsului.
- **Mai multe site-uri:** fiecare agent urmărește produsele unui singur website.
- **Configurare:** în **AI › Agents**, fila **Shop** (vizibilă doar administratorilor): se alege site-ul, opțional un domeniu de produse și câmpuri suplimentare, bifa *Read Photos* și butonul *Synchronize now*. Apoi se adaugă topicul *Shop Assistant* și se setează agentul pe o regulă a canalului Live Chat din **Website › Configuration › Live Chat** (întâi pe un URL de test, ex. `?assistant=test`).

#### 3. Dependențe

- `website_sale`
- `ai_app`
- [deltatech_ai_source_sync](../deltatech_ai_source_sync/index.md)

#### 4. Componente Cheie

**Modele**

- `ai.agent` (extins): câmpurile `product_website_id`, `product_domain`, `product_field_ids`, `product_read_photos`, cursorul de sincronizare; sincronizarea surselor, descrierea pozelor și uneltele de preț/disponibilitate și de căutare după cuvinte-cheie și an.
- `ai.agent.source` (extins): legătura `product_tmpl_id` către produs și marcajul de urmărire `product_follow`.
- `product.template` (extins): la creare/modificare a câmpurilor relevante cere sincronizarea surselor agenților.
- `mail.message` (extins): `ai_photo_description`, descrierea pozei din chat păstrată în istoric.

**Vizualizări**

- `ai_agent_view_form` (moștenește `ai_app.ai_agent_view_form`): fila *Shop* pe agent, cu site, domeniu, câmpuri suplimentare, *Read Photos* și butonul de sincronizare.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_product_sync`: cron zilnic „AI: synchronize the products of the shop”, reverifică produsele tuturor agenților.
- `ir_actions_server_product_info`: unealta AI „AI: Shop Product Price and Availability”.
- `ir_actions_server_product_search`: unealta AI „AI: Shop Product Search”.
- `ai_topic_shop_assistant` (`ai.topic`): topicul *Shop Assistant* cu instrucțiunile și uneltele de mai sus.

#### 5. Conexiuni

- `ai`: modulul Enterprise de bază pentru agenți, topicuri și unelte AI.
- [deltatech_ai_source_sync](../deltatech_ai_source_sync/index.md): oferă mecanismul de sincronizare a surselor refolosit aici.
- [deltatech_ai_agent_delegate](../deltatech_ai_agent_delegate/index.md): un agent public (de ex. pe livechat) poate delega întrebările de produs agentului magazinului.
- [deltatech_ai_website_product_image](../deltatech_ai_website_product_image/index.md): căutarea produselor după poză; depinde de acest modul.
