# AI - Shop Assistant: Search by Photo (localizat la `deltatech_ai_website_product_image/index.md`)

- **Nume Tehnic:** `deltatech_ai_website_product_image`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_website_product_image
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_website_product_image`
- **Ultima Ingestie:** `2026-10-20`

#### 1. Sumar

Agentul AI al magazinului online găsește **produsele care seamănă cu poza** trimisă de un vizitator în Live Chat: o piesă, un accesoriu sau o decorațiune al cărei nume sau cod vizitatorul nu le cunoaște. Agentul primește produsele cele mai asemănătoare, împreună cu gradul de similitudine, și le citește apoi prețul și disponibilitatea în timp real cu uneltele asistentului de magazin. Modulul este în stadiul Alpha.

#### 2. Funcționalități Cheie

- **Căutare vizuală**: poza fiecărui produs urmărit de agent este transformată într-un vector de către Gemini (`gemini-embedding-2`, cu cheia Google din setările AI); poza vizitatorului este comparată cu aceste vectori, iar cele mai similare produse sunt date agentului.
- **Același tip, nu aceeași dimensiune**: o poză arată tipul produsului, nu mărimea lui. Pe un test cu 300 de produse (elemente de fixare, piese pentru prelate, semnalizare, decorațiuni), produsul corect a fost primul pentru 23 din 40 de poze și printre primele cinci pentru 34; toate ratările au fost același produs în altă dimensiune. Agentul este instruit să ceară dimensiunea sau codul.
- **Nimic similar**: produsele sub *Similaritate minimă* (implicit 0,75) nu sunt oferite. În teste, produsele de același tip au depășit 0,80, iar pozele fără legătură cu magazinul au rămas sub 0,70.
- **Sincronizare automată**: o poză de produs adăugată sau schimbată este vectorizată după câteva minute; o poză nemodificată își păstrează vectorul. La atingerea cotei cheii, sincronizarea continuă singură când Gemini permite.
- **Compatibil cu descrierea pozei**: cu opțiunea *Read Photos* a asistentului de magazin, agentul primește atât descrierea pozei, cât și produsele similare.
- **Configurare**: în **AI › Configuration › Settings** se activează Google și se introduce cheia Gemini (sau variabila de mediu `ODOO_AI_GEMINI_TOKEN`); cheia se folosește pentru poze chiar dacă agentul răspunde cu alt furnizor. Pentru un magazin se recomandă cheie plătită (planul gratuit permite 100 de poze pe minut, iar Google poate folosi datele trimise).
- **Activare pe agent**: la **AI › Agents**, fila **Shop**, se bifează *Search by Photo* și se setează *Products per Photo* (implicit 5) și *Minimum Similarity* (implicit 0,75). Vectorii se calculează în fundal prin cron sau imediat cu **Synchronize now**.
- **Utilizare**: vizitatorul deschide chatul, apasă **+ › Attach files**, trimite poza (cu sau fără întrebare) și primește produsele cu preț, disponibilitate și link.
- **Atenție la confidențialitate**: pozele produselor și ale vizitatorilor sunt trimise către Google.

#### 3. Dependențe

- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md)

#### 4. Componente Cheie

**Modele**

- `ai.agent` (extins): câmpurile `product_photo_search`, `product_photo_matches`, `product_photo_threshold`; sincronizarea vectorilor (`_sync_product_image_vectors`, `_cron_product_image_sync`), extragerea pozei din mesaj și căutarea produselor similare (`_get_photo_matches`, `_search_similar_products`).
- `ai.product.image.vector`: vectorul unei poze de produs, cu `product_tmpl_id`, `checksum` (detectează pozele schimbate) și `embedding_model`.
- `product.template` (extins): extinde lista câmpurilor care declanșează sincronizarea AI (`_get_ai_synced_fields`).
- `utils/gemini_embedding.py`: clientul pentru embeddings Gemini.

**Vizualizări**

- `ai_agent_view_form`: moștenește formularul agentului și adaugă, în fila Shop, opțiunile de căutare după poză (vizibile doar dacă agentul are website de produse).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_product_image_sync` (*AI: vectors of the product photos*): rulează zilnic `_cron_product_image_sync()`; sincronizarea e programată și la câteva minute după modificarea unei poze.

#### 5. Conexiuni

- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md): asistentul de magazin pe care îl completează cu căutarea după poză.
