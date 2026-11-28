# AI - Product Catalog Review

- **Nume Tehnic:** `deltatech_ai_product_catalog_review`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_product_catalog_review
- **Cale Locală:** odoo-addons/bitshop_ent/deltatech_ai_product_catalog_review
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modelul de limbaj al unui agent AI al magazinului online analizează produsele publicate și propune **categoria de magazin** și produsele **alternative, accesorii și opționale**. Nimic nu se schimbă pe produs până când o propunere nu este acceptată.

#### 2. Funcționalități Cheie

- **Candidați după similaritate**: cele mai similare produse sunt găsite cu embeddings-urile pe care agentul magazinului le ține deja pentru fiecare produs (modulul *AI - Shop Assistant*), fără apeluri noi către furnizor.
- **O întrebare per produs**: modelul primește produsul, categoriile magazinului și candidații și răspunde cu cea mai potrivită categorie și relația fiecărui candidat (alternativ, accesoriu, opțional sau niciuna), cu încredere și motiv scurt. Costul, furnizorii și notele interne nu sunt trimise niciodată.
- **Compatibilitate și direcție verificate**: nu se propune alternativă sau accesoriu făcut pentru altă marcă, model, generație, versiune sau ani; un accesoriu găsit la analiza lui (spray de curățare) este propus pe produsul principal (covorașe).
- **Propuneri de revizuit**: grupate pe produs, cu categoriile curente, încrederea și motivul; se acceptă sau se resping pe rând, ori toate cele peste încrederea minimă.
- **Acceptarea** înlocuiește categoriile produsului pe acel magazin (cele de pe alte site-uri rămân) sau adaugă produsul la *Alternative Products*, *Accessory Products* sau *Optional Products*.
- **Fără propuneri repetate**: ce este deja setat, așteaptă în altă analiză sau a fost respins nu se mai propune.
- **Cataloage mari**: analiza rulează în fundal printr-un cron care continuă de unde a rămas; pentru câteva produse, analiza rapidă se face din lista sau formularul produselor.
- **Flux**: *Website > eCommerce > Products > AI Catalog Review* → analiză nouă (agent, filtru de produse, tipuri de propuneri, număr de candidați, încrederea minimă) → *Start* sau *Analyze Now* → butonul *Proposed* → *Accept* / *Reject* / *Accept All Above the Minimum*; din lista de produse, *Action > Review Category and Related Products with AI*.

#### 3. Dependențe

- `website_sale`
- `deltatech_ai_website_product`

#### 4. Componente Cheie

**Modele**

- `ai.product.review`: analiza de catalog (agent, filtru, tipuri de propuneri, încredere minimă, stare).
- `ai.product.review.line`: propunerea per produs (categorie sau relație, încredere, motiv).
- `product.template` (extins): acțiunea de analiză din lista și formularul produselor.

**Vizualizări**

- `views/ai_product_review_views.xml`: formular, listă și propuneri ale analizei.
- `views/product_template_views.xml`: acțiunea de analiză pe produse.

**Acțiuni Automate / Acțiuni Server**

- Cron (`data/ir_cron.xml`): analizează în fundal produsele analizelor pornite.

#### 5. Conexiuni

- `deltatech_ai_website_product`: agentul magazinului și embeddings-urile produselor, folosite pentru candidați.
- `website_sale`: categoriile magazinului și produsele alternative, accesorii, opționale.
