# AI - Product Catalog Review

- **Nume Tehnic:** `deltatech_ai_product_catalog_review`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_product_catalog_review
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_product_catalog_review`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modelul de limbaj al unui agent AI al magazinului online parcurge produsele publicate și propune categoria de magazin și produsele alternative, accesorii și opționale ale fiecăruia. Nimic nu se modifică pe produs până când o propunere nu este acceptată, astfel încât echipa păstrează controlul asupra catalogului.

#### 2. Funcționalități Cheie

- **Candidați prin similaritate:** cele mai similare produse ale magazinului sunt găsite cu embedding-urile pe care agentul magazinului le ține deja pentru fiecare produs (modulul *AI - Shop Assistant*), fără apeluri noi către furnizor.
- **O întrebare per produs:** modelul primește produsul, categoriile magazinului și candidații și răspunde cu categoria potrivită și cu relația fiecărui candidat (alternativ, accesoriu, opțional sau niciuna), cu grad de încredere și motiv scurt. Costul, furnizorii și notele interne nu sunt trimise niciodată.
- **Potrivire și sens verificate:** modelul spune dacă candidatul e făcut pentru același vehicul sau utilaj; alternativele și accesoriile pentru altă marcă, model, generație, versiune sau alți ani nu se propun. Un accesoriu găsit la analiza lui (ex. spray de curățat) se propune pe produsul principal (ex. covorașele).
- **Propuneri de revizuit:** grupate pe produs, cu categoriile curente, încrederea și motivul; se acceptă sau se resping pe rând, ori se acceptă toate cele peste încrederea minimă.
- **Acceptarea** înlocuiește categoriile produsului pe acel magazin (cele ale altor site-uri rămân) sau adaugă produsul la *Produse alternative*, *Accesorii* ori *Produse opționale*.
- **Fără propuneri repetate:** ce e deja setat pe produs, așteaptă într-o altă analiză sau a fost respins nu se mai propune.
- **Cataloage mari:** analizate în fundal de un cron care continuă de unde a rămas; câteva produse se analizează imediat din lista sau formularul produselor (*Acțiune > Review Category and Related Products with AI*).
- **Flux operațional:** *Website > eCommerce > Products > AI Catalog Review* → creezi analiza (agent, filtru opțional de produse, tipurile de propuneri, numărul de candidați, încrederea minimă) → *Start* (cron) sau *Analyze Now* → butonul *Proposed* → *Accept* / *Reject* sau *Accept All Above the Minimum*. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `website_sale`
- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md)

#### 4. Componente Cheie

**Modele**

- `ai.product.review`: analiza de catalog (agent, filtru, tipuri de propuneri, candidați, încrederea minimă); acțiuni Start, Stop, Analyze Now, Accept All.
- `ai.product.review.line`: o propunere (categorie sau relație) cu încredere și motiv; acțiuni Accept, Reject, Reset.
- `product.template` (extins): acțiunea `action_ai_review_catalog` pentru analiza produselor selectate.

**Vizualizări**

- `ai_product_review_view_list` / `ai_product_review_view_form`: lista și formularul analizelor.
- `ai_product_review_line_view_list` / `ai_product_review_line_view_search`: propunerile, grupate pe produs.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_product_review` (*AI: review the product catalog*): rulează din oră în oră `_cron_run()` și continuă analizele pornite.
- `action_server_ai_review_catalog`: acțiune server pe produse (*Review Category and Related Products with AI*).

#### 5. Conexiuni

- [deltatech_ai_website_product](../deltatech_ai_website_product/index.md): folosește agentul magazinului și textul produselor din acest modul.
