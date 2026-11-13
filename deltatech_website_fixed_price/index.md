# eCommerce Display Fixed Price As Discount

- **Nume Tehnic:** `deltatech_website_fixed_price`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_fixed_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_fixed_price`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Magazinele online oferă adesea unui produs un preț special printr-o regulă de listă de prețuri cu preț fix și vor ca prețul vechi să apară barat. Modulul face ca magazinul eCommerce să trateze regulile cu preț fix ca reguli a căror reducere se afișează. Conform descrierii din manifest, prețul tăiat apare când prețul fix este mai mic decât prețul de listă.

#### 2. Funcționalități Cheie

- **Reguli cu preț fix:** o regulă de listă de prețuri al cărei calcul este „preț fix” cere acum întotdeauna magazinului să afișeze reducerea. Orice altă regulă păstrează răspunsul dat de codul standard.
- **Unde se aplică:** conform comentariului din cod, modificarea acoperă magazinul, pagina de produs și configuratoarele de produs, nu coșul și nici finalizarea comenzii.
- **Compararea prețurilor:** modulul nu compară el însuși prețurile; afișarea prețului tăiat numai când prețul fix este mai mic decât cel de listă rămâne în seama mecanismului standard de afișare din `website_sale`.
- **Fără configurare:** modulul nu adaugă setări, câmpuri, ecrane sau meniuri. Se aplică tuturor regulilor de listă de prețuri imediat după instalare.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.pricelist.item` (extins): suprascrie `_show_discount_on_shop` și întoarce adevărat și pentru regulile cu `compute_price == "fixed"`, pe lângă răspunsul standard.

**Vizualizări**

- Modulul nu definește vizualizări proprii (lista `data` din manifest este goală).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `website_sale`: modulul standard Odoo de magazin online, ale cărui mecanisme de afișare a prețurilor și reducerilor sunt ajustate de acest modul.
