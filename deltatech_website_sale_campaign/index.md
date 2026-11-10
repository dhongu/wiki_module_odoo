# Website Sales Campaigns

- **Nume Tehnic:** `deltatech_website_sale_campaign`
- **Versiune:** `19.0.1.2.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_sale_campaign
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_campaign`
- **Ultima Ingestie:** `2026-11-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite rularea campaniilor de tip Black Friday în magazinul online Odoo, fără intervenții manuale la ora începerii sau a încheierii. Campania se planifică o singură dată: etapele, prețurile și aspectul. La start, site-ul se schimbă automat (temă dedicată, bară de sus cu numărătoare inversă, panglici și insigne -X%), iar la final revine la normal. Prețul tăiat este cel mai mic preț din ultimele 30 de zile dinaintea campaniei, conform directivei Omnibus (UE 2019/2161), nu prețul de listă standard din Odoo.

#### 2. Funcționalități Cheie

**Campania**

- **Etape**: una sau mai multe perioade (ex. Runda 1, Weekend bonus, Prelungire), fiecare cu start, final, text pentru bara de sus și numărătoare; etapele nu se pot suprapune.
- **Produse**: pe produs, variantă sau categorie, cu discount sau preț fix, pe toate etapele sau doar pe unele.
- **Prețuri**: la programare se scriu regulile de listă de prețuri ale fiecărei etape, cu date, în listele de prețuri ale site-ului; prețurile pornesc și se opresc singure, iar anularea campaniei șterge regulile. Regula de campanie are prioritate față de regulile existente.
- **Preț de referință**: cel mai mic preț din ultimele 30 de zile (din istoricul de prețuri), cu posibilitatea unui preț de referință manual, cu motiv obligatoriu.
- **Verificare marjă**: marjă minimă peste cost, cu politică de avertizare în chatter sau de blocare a programării.
- **Stări**: Ciornă, Programată, În desfășurare, Încheiată, Anulată (anularea scoate regulile campaniei din listele de prețuri); din Programată se poate reveni la Ciornă pentru modificări.
- **Previzualizare**: designerul site-ului vede site-ul ca în prima etapă, cu prețurile ei, înainte de start; vizitatorii văd în continuare site-ul normal.

**Site-ul în timpul campaniei**

- **Temă** (Black Friday și Crăciun livrate): culoare principală, fundal, text, carduri de produs, preț de campanie, aplicate pe antet, pagină, carduri, butoane și subsol (fiecare opțional), plus CSS propriu; se configurează în *Website > Configuration > Campaign Themes*.
- **Bară de sus** cu textul etapei și numărătoare până la finalul etapei sau al campaniei.
- **Stil numărătoare**: Simplu sau Flip (ceas cu cifre care se întorc), cu sau fără unități (d, h, m, s); fără animație pentru vizitatorii care au cerut mișcare redusă.
- **Panglică** cu numele campaniei pe produsele din campanie și **insignă -X%** lângă preț.
- **Blocuri vizibile pe etapă**: în editor, *Visibility > Conditionally > Campaign Stage* afișează sau ascunde un bloc pe etapele alese.

**Pagina campaniei și blocuri**

- **Pagina campaniei** `/shop?campaign=<id>`, adresa de promovat în newslettere și reclame: magazinul cu produsele campaniei, sub un antet cu titlu public, descriere, banner și numărătoare. Filtrele, sortarea și paginarea păstrează campania; o campanie încheiată afișează o notificare, iar una în ciornă e vizibilă doar designerilor.
- **Filtrul Campaign Products** pentru blocul standard *Products*: produsele etapei curente; gol când nu rulează nicio campanie.
- **Blocul Campaign Countdown**: numărătoare mare până la finalul etapei curente, ascunsă vizitatorilor când nu rulează nicio campanie.

**Configurare prealabilă**: activarea *Pricelists* în *Sales > Configuration > Settings* (altfel site-ul ignoră listele de prețuri) și instalarea modulului cu cel puțin 30 de zile înainte de prima campanie, pentru un istoric complet al prețurilor. Meniu campanii: *Website > eCommerce > Products > Campaigns*. Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `website_sale`
- `deltatech_product_price_history`

#### 4. Componente Cheie

Secțiune omisă din analiza codului, DESCRIPTION.md fiind prezent și neprecizând componente. Repere de bază, din structura modulului:

**Modele**

- `website.sale.campaign`: campania (cu `mail.thread`), cu etape, linii de produse și stări.
- `website.sale.campaign.stage`: etapa campaniei (interval, text bară, numărătoare).
- `website.sale.campaign.line`: linia de produs/variantă/categorie cu discount sau preț fix, preț de referință și marjă.
- `website.sale.campaign.theme`: tema vizuală a campaniei.
- Extinderi: `product.pricelist`, `product.pricelist.item`, `product.template`, `sale.order.line`, `website`, `website.page`, `website.snippet.filter`.

**Vizualizări**

- Formulare/liste pentru campanii și teme (`views/campaign_views.xml`, `views/campaign_theme_views.xml`) și șabloanele site-ului (`views/website_templates.xml`).

**Acțiuni Automate / Acțiuni Server**

- `ir.cron` „Website campaigns: start, end and record the prices”: rulează din oră în oră `_cron_update_state()`.
- Acțiunea server `dynamic_snippet_campaign_products_action` și filtrul `dynamic_filter_campaign_products` (Campaign Products, limită 16).

#### 5. Conexiuni

- `deltatech_product_price_history`: sursa prețului de referință (cel mai mic preț din 30 de zile).
