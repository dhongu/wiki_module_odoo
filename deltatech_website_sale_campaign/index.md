# Campanii de vânzări pe site (Black Friday, Crăciun)

- **Nume Tehnic:** `deltatech_website_sale_campaign`
- **Versiune:** `20.0.1.2.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_sale_campaign
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_sale_campaign`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite rularea unei campanii de tip Black Friday pe magazinul Odoo fără intervenție la miezul nopții și fără a anunța o reducere care nu poate fi dovedită. Campania se planifică o dată (etape, prețuri, aspect); la start site-ul se schimbă singur (temă întunecată, bară de sus cu numărătoare inversă, panglici și insigne -X%), iar la final totul revine. Prețul tăiat este cel mai mic preț din ultimele 30 de zile dinaintea campaniei, conform Directivei Omnibus (UE) 2019/2161, nu prețul de vânzare pe care Odoo îl taie în mod standard.

#### 2. Funcționalități Cheie

- **Etape**: una sau mai multe perioade (*Runda 1*, *Bonus de weekend*, *Prelungire*), fiecare cu început, sfârșit, textul barei de sus și numărătoarea ei.
- **Produse**: pe produs, variantă sau categorie, cu reducere procentuală sau preț fix, pe toate etapele sau doar pe unele.
- **Prețuri**: programarea scrie regulile datate din listele de prețuri ale site-ului; prețurile pornesc și se opresc singure, iar anularea campaniei șterge regulile. Regula campaniei câștigă în fața regulilor existente.
- **Preț de referință**: cel mai mic preț din ultimele 30 de zile (modulul *Istoric prețuri produs*); poate fi înlocuit manual pe un produs, cu motivul consemnat.
- **Verificarea marjei**: marjă minimă peste cost, cu avertisment în chatter sau blocare la programare.
- **Previzualizare**: designerul site-ului vede site-ul ca în campanie înainte de start; vizitatorii văd site-ul normal.
- **Tema campaniei** (*Black Friday* și *Crăciun* livrate): culori, fundal, carduri de produs, preț de campanie, aplicate pe antet, pagină, carduri, butoane și subsol, plus CSS propriu; site-ul revine la aspectul normal la final.
- **Bara de sus** cu textul etapei și numărătoare inversă, stil *Simplu* sau *Flip* (fără animație pentru cei cu mișcare redusă), **panglică** cu numele campaniei și insignă **-X%** lângă preț.
- **Blocuri vizibile pe etapă**: în editor, *Vizibilitate > Condiționat > Etapa campaniei*.
- **Pagina campaniei** `/shop?campaign=<id>`, de distribuit în newslettere și reclame, cu titlu public, descriere, banner și numărătoare; filtrele de produse *Produse din campanie* și blocul *Numărătoare campanie*.
- Cerințe de configurare: listele de prețuri activate în Vânzări, modulul instalat cu cel puțin 30 de zile înainte de prima campanie (pentru istoricul de preț), teme în *Website > Configurare > Teme de campanie*. Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `website_sale`
- [deltatech_product_price_history](../deltatech_product_price_history/index.md)

#### 4. Componente Cheie

**Modele**

- `website.sale.campaign`: campania, cu ciclul ei de stări.
- `website.sale.campaign.stage`: etapele campaniei.
- `website.sale.campaign.line`: produsele campaniei și regulile lor de preț.
- `website.sale.campaign.theme`: tema vizuală a campaniei.
- `product.pricelist`, `product.pricelist.item`, `product.template`, `sale.order.line`, `website`, `website.snippet.filter` (extinse): reguli de preț ale campaniei, preț de referință, filtrul *Produse din campanie* și aplicarea temei.

**Vizualizări**

- Formularul și lista campaniilor, formularul temelor de campanie, pagina publică `/shop?campaign=<id>` și blocurile *Produse din campanie* și *Numărătoare campanie* (controlere `main.py` și `shop.py`).

**Acțiuni Automate / Acțiuni Server**

- `Website campaigns: start, end and record the prices` (`ir.cron`, la fiecare oră): pornește și oprește etapele și înregistrează prețurile.

#### 5. Conexiuni

- [deltatech_product_price_history](../deltatech_product_price_history/index.md): sursa prețului de referință din ultimele 30 de zile.
