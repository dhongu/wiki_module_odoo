# eCommerce Product sort (localizat la `deltatech_website_sale_sort/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_sort`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_sort`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_sort`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul adaugă criterii suplimentare de sortare a produselor în magazinul online (eCommerce), pe lângă cele standard oferite de Odoo. Astfel, vizitatorii pot ordona produsele după popularitate reală — cele mai vândute, cele mai vizitate sau cele mai bine cotate. Pentru a funcționa rapid, modulul calculează periodic (printr-o sarcină programată) o serie de statistici pe fiecare produs, pe care le stochează direct în baza de date, evitând calcule grele la fiecare afișare a paginii.

#### 2. Funcționalități Cheie

- Criterii suplimentare de sortare a produselor în magazinul online: cele mai vândute, cele mai vizitate, după număr de recenzii, după nota medie și după disponibilitatea în stoc.
- Câmpuri statistice stocate pe produs (număr vânzări, vizite, recenzii), recalculate periodic pentru performanță.
- Calcul automat al statisticilor printr-o sarcină programată (cron) care rulează zilnic.
- Procesare pe loturi (2000 produse/lot) la recalcularea statisticilor, pentru a evita erorile de memorie pe cataloage mari (~476k șabloane); dacă modulul `queue_job` este instalat, fiecare lot este delegat ca job separat (`with_delay()`), altfel se rulează în proces cu golirea cache-ului ORM între loturi.

#### 3. Dependențe

- `website_sale`
- `stock`

#### 4. Componente Cheie

Notă: Readme-ul (`DESCRIPTION.md`) menționează explicit existența unui câmp pe produs calculat periodic printr-un cron; componentele de mai jos detaliază aceste elemente, inclusiv mecanismul de procesare pe loturi introdus în versiunea curentă.

**Modele**

- `product.template` (extins): adaugă câmpurile stocate `sales_count2` (vânzări), `visit_count` (vizite), `comment_count`, `rating_count2`, `rating_avg2` și `in_stock`; agregă statisticile la nivel de șablon din variantele de produs și din recenzii (`rating.rating`). Metoda `_cron_update_statistics()` împarte produsele în loturi de 2000 și, opțional, delegă fiecare lot prin `queue_job` (`with_delay()`) dacă acesta este instalat.
- `product.product` (extins): adaugă câmpurile stocate `sales_count2` și `visit_count`; calculează vânzările din `sale.report` (ultimele 365 de zile, doar comenzile în stări finalizate) și vizitele din `website.track`; folosește aceeași strategie de procesare pe loturi.
- `website` (extins): suprascrie `_get_product_sort_mapping` pentru a adăuga noile opțiuni de sortare în magazinul online.

**Vizualizări**

- Nu sunt definite vizualizări proprii (fișierul `views/templates.xml` este comentat în manifest); modulul intervine asupra interfeței exclusiv prin extinderea opțiunilor de sortare ale magazinului online.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_product_sale_scheduled` (`ir.cron`): „Products: Update products statistics" — rulează zilnic ca utilizator root și apelează `_cron_update_statistics()`, care recalculează statisticile pentru toate produsele și șabloanele, pe loturi.

#### 5. Conexiuni

- [deltatech_website_sale_attributes](../deltatech_website_sale_attributes/index.md): extinde tot magazinul online (`website_sale`) cu funcționalități complementare de filtrare/afișare a produselor.
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): modul din zona de eCommerce/website legat de urmărirea interacțiunilor pe site (sursă a datelor de tip vizită).
- `queue_job`: dependență opțională (nu figurează în `depends`), folosită doar dacă e instalată, pentru a delega procesarea pe loturi ca joburi asincrone.
