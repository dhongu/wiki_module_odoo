# OpenCart Marketplace Connector (localizat la `deltatech_marketplace_opencart/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_opencart`
- **Versiune:** `20.0.0.3.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_opencart
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_opencart`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectorul leagă un magazin OpenCart de Odoo, peste cadrul Marketplace al suitei Deltatech. Produsele, variantele, atributele, clienții, comenzile și metodele de livrare și de plată circulă automat între cele două sisteme dintr-un singur backend, fără reintroducere manuală. Magazinul online rămâne vitrina, iar catalogul, stocul și comenzile se gestionează centralizat în Odoo. Conectorul folosește extensia REST Admin API a OpenCart.

#### 2. Funcționalități Cheie

- Import șabloane de produs cu variante din opțiunile OpenCart, atribute (opțiuni și caracteristici), categorii publice și metode de livrare (cu crearea unui produs-serviciu dacă lipsește).
- Export de produse către OpenCart (preț, stoc, imagini, câmpuri SEO). Produsele noi se trimit doar manual; modificările la produse deja mapate se trimit automat dacă este bifat **Active On Write** pe cardul **Product Template**.
- Mapare automată pe codul produsului (Model, SKU sau ID, ales în **Opencart Code**); produsele existente cu același cod intern se leagă, nu se dublează.
- Import comenzi, cu clienți înregistrați sau ocazionali, adrese de facturare și livrare (un singur contact dacă coincid), linii fără TVA, cost de livrare, plată și comentariu. Cuponul devine notă plus linie negativă pe **Discount Product**, care trebuie setat, altfel comanda nu se importă. Statusul OpenCart devine **Phase** a comenzii și, cu **Active On Write** pe cardul **Sale Order**, schimbarea fazei în Odoo se trimite înapoi.
- Stoc trimis la OpenCart pe produs și pe valoare de opțiune, după bifarea **Can send stock** și activarea acțiunii programate **Marketplace: export stock**.
- Comenzile se importă prin acțiunea programată **Marketplace: Get Orders** (orară, inactivă după instalare) sau prin webhook.
- Setări pe backend: motorul de joburi (Background Jobs sau queue_job, în **Marketplace → Configuration → Settings**), **Opencart Lang**, **Opencart Version** (3.0 sau 4.0), **Opencart Seo**, **Opencart Tax Class**, **Use Variants** și **Use Attribute**. Ordinea recomandată a importurilor: Delivery Carrier, Public category, Characteristics, Product Template, Sale Order.
- Limite: nu există flux de anulare, retur sau notă de credit între sisteme; prețul de listă nu se preia din OpenCart; un produs fără opțiuni creat de import nu primește variantă, deci linia de comandă devine notă (se creează întâi în Odoo, cu referința egală cu codul OpenCart).

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_brand](../deltatech_marketplace_brand/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, componentele nu au fost analizate în cod (readme-ul acoperă funcționalitatea).

**Modele**

- `marketplace.backend` (extins): provider-ul `opencart` și opțiunile de conectare.
- Modele de legătură extinse: `marketplace.product.template`, `marketplace.product`, `marketplace.product.attribute`, `marketplace.product.attribute.value`, `marketplace.public.category`, `marketplace.product.brand`, `marketplace.delivery.carrier`, `marketplace.customer`, `marketplace.lang`, `marketplace.product.pricelist`, `marketplace.sale.order`.
- `product.template` și `delivery.carrier` (extinse).

**Vizualizări**

- `views/backend_views.xml`, `views/product_template_view.xml`, `views/attribute_view.xml`: setările backend-ului, câmpurile OpenCart de pe produs și de pe atribute.

**Acțiuni Automate / Acțiuni Server**

- `data/job_spec.xml`: specificațiile joburilor de fundal ale conectorului.
- Importul comenzilor folosește acțiunea programată comună **Marketplace: Get Orders** (orară, inactivă implicit), iar stocul **Marketplace: export stock** (inactivă implicit).

#### 5. Conexiuni

- Nu există conexiuni suplimentare față de dependențele din secțiunea 3 (verificat în manifest; \`deltatech_marketplace_website\` nu mai este dependență pe 20.0).
