# eCommerce Product sort (localizat la `deltatech_website_sale_sort/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_sort`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_sort
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_sort`
- **Ultima Ingestie:** `2026-11-21`

#### 1. Sumar

Cumpărătorii preferă să înceapă cu ce cumpără, vizitează și apreciază alții sau cu ce este în stoc. Modulul adaugă cinci astfel de criterii în lista de sortare a produselor din website și ține la zi cifrele din spatele lor printr-o acțiune programată zilnică. Statisticile sunt stocate direct pe produs, evitând calcule grele la fiecare afișare a paginii.

#### 2. Funcționalități Cheie

- **Opțiuni noi de sortare:** *Best sellers*, *Most Visited*, *Reviews*, *Best Review* și *Availability* se adaugă în lista de sortare a produselor din website, fiecare cu valoarea cea mai mare prima.
- **Vânzări și vizite:** *Best sellers* folosește cantitatea vândută în ultimele 365 de zile, citită din raportul de vânzări pentru stările finalizate; *Most Visited* folosește vizitele înregistrate pe pagina produsului.
- **Recenzii:** *Reviews* ordonează produsele după numărul de evaluări primite, iar *Best Review* după media lor.
- **Disponibilitate:** *Availability* pune primele produsele cu cantitate în stoc mai mare de zero.
- **Reîmprospătare zilnică:** acțiunea programată *Products: Update products statistics* recalculează cifrele o dată pe zi pentru fiecare produs și variantă, în loturi de 2.000 (job-uri în coadă dacă `queue_job` este instalat, altfel în proces cu golirea cache-ului ORM între loturi).
- **Limitări:** cifrele sunt stocate pe produse și variante, deci vânzările, vizitele și evaluările noi contează în sortare abia după următoarea rulare; produsele arhivate sunt omise. Acțiunea rulează ca utilizator de sistem, iar modulul nu are grupuri de securitate.

#### 3. Dependențe

- `website_sale`
- `stock`

#### 4. Componente Cheie

Notă: `readme/DESCRIPTION.md` menționează explicit câmpurile calculate periodic prin cron; componentele de mai jos detaliază aceste elemente (verificate în ultima analiză a codului), inclusiv procesarea pe loturi.

**Modele**

- `product.template` (extins): adaugă câmpurile stocate `sales_count2` (vânzări), `visit_count` (vizite), `comment_count`, `rating_count2`, `rating_avg2` și `in_stock`; agregă statisticile la nivel de șablon din variantele de produs și din recenzii (`rating.rating`). Metoda `_cron_update_statistics()` împarte produsele în loturi de 2000 și, opțional, delegă fiecare lot prin `queue_job` (`with_delay()`) dacă acesta este instalat.
- `product.product` (extins): adaugă câmpurile stocate `sales_count2` și `visit_count`; calculează vânzările din `sale.report` (ultimele 365 de zile, doar comenzile în stări finalizate) și vizitele din `website.track`; folosește aceeași strategie de procesare pe loturi.
- `website` (extins): suprascrie `_get_product_sort_mapping` pentru a adăuga noile opțiuni de sortare în magazinul online.

**Vizualizări**

- Nu sunt definite vizualizări proprii (fișierul `views/templates.xml` este comentat în manifest); modulul intervine asupra interfeței exclusiv prin extinderea opțiunilor de sortare ale magazinului online.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_product_sale_scheduled` (`ir.cron`): „Products: Update products statistics" — rulează zilnic ca utilizator root și apelează `_cron_update_statistics()`, care recalculează statisticile pentru toate produsele și șabloanele, pe loturi.

#### 5. Conexiuni

- `queue_job`: dependență opțională (nu figurează în `depends`), folosită doar dacă e instalată, pentru a delega procesarea pe loturi ca joburi asincrone.
