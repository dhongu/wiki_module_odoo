# Website Stock Availability (localizat la `deltatech_website_stock_availability/index.md`)

- **Nume Tehnic:** `deltatech_website_stock_availability`
- **Versiune:** `20.0.1.0.12`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_stock_availability`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_stock_availability`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite afișarea stocului pe website sub un anumit prag, oferind clienților posibilitatea de a comanda un produs chiar dacă stocul disponibil nu este suficient. Pe lângă disponibilitate, modulul estimează și numărul de zile în care se va face livrarea, luând în calcul timpul de livrare definit pe produs, numărul de zile de siguranță și numărul de zile de livrare de la furnizor pentru produsele care nu se află pe stoc. Astfel, magazinul online comunică transparent atât disponibilitatea, cât și termenul realist de livrare.

#### 2. Funcționalități Cheie

- Afișarea pe pagina produsului a disponibilității („În stoc”, „În stoc la furnizor”, „Nu este în stoc”) și a unui termen de livrare estimat („Livrare imediată”, „Livrare mâine”, „Livrare în 2 - 3 zile”, „Livrare în N săptămâni”).
- Posibilitatea de a comanda produse chiar dacă stocul curent nu este suficient (opțiunea standard *Sell when Out-of-Stock*).
- Calculul automat al termenului de livrare: timpul de livrare al produsului, zilele de siguranță (*Customer Safety Lead Time*, implicit 1 zi) și, pentru produsele fără stoc propriu, termenul și stocul primei linii de furnizor (*Lead Time* cu zecimale, *Quantity Available* din `deltatech_vendor_stock`).
- Opțiune pe produs pentru ascunderea mesajului „Nu este în stoc”.
- Status de stoc pe cardurile din magazin („Livrare imediată” / „Livrare ulterioară”), configurat din editorul website-ului, în panoul *Products Design*: text, LED sau LED cu text, deasupra prețului, pe imagine (stânga jos sau stânga sus) sau lângă preț, cu portocaliu, gri sau roșu pentru produsele fără stoc.
- În coș, fiecare linie arată dacă se livrează imediat sau ulterior. Mesajele sunt vizualizări opționale, care se pot activa sau opri din vizualizările tehnice.
- Fluxul detaliat de configurare și verificare este în fișa consultantului.

#### 3. Dependențe

- `website`
- `website_sale_stock`
- `purchase`
- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template`: câmpurile *Customer Safety Lead Time* și *Hide Out-of-Stock Message*, plus calculul disponibilității și al termenului de livrare în informațiile combinației afișate pe website.
- `product.supplierinfo`: termenul de livrare al furnizorului acceptă zecimale.
- `ir.http`: extensie pentru încărcarea traducerilor modulului în magazin.

**Vizualizări**

- `views/product_view.xml`: câmpurile noi pe formularul produsului.
- `views/website_sale_stock_templates.xml`: mesajele de stoc și termen de livrare pe pagina produsului, în coș și în rezumatul comenzii.
- `static/src/website_builder/products_design_panel.xml`: opțiunea *Stock Status* în panoul *Products Design* din editorul website-ului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md): furnizează cantitatea disponibilă la furnizor, folosită la estimarea disponibilității și a termenului pentru produsele care nu sunt pe stoc.
