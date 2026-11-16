# Doraly Connector (localizat la `deltatech_marketplace_doraly/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_doraly`
- **Versiune:** `19.0.0.0.15`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_doraly
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_doraly`
- **Ultima Ingestie:** `2026-11-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un conector între Odoo și marketplace-ul Doraly, extinzând cadrul general de integrare cu marketplace-uri din suita Terrabit. Scopul său principal este să sincronizeze datele comerciale dintre magazinul Doraly și sistemul ERP Odoo: permite autentificarea către platforma Doraly, importul catalogului de produse, exportul parțial al produselor, importul comenzilor primite în marketplace și trimiterea către Doraly a linkului facturii PDF. Astfel, comercianții care vând prin Doraly își pot gestiona produsele și comenzile direct din Odoo, fără introducere manuală a datelor. Modulul are statut de dezvoltare *Alpha*.

#### 2. Funcționalități Cheie

- Logare (autentificare) către platforma Doraly: da
- Import produse din Doraly în Odoo: da
- Export produse din Odoo către Doraly: parțial (brandul nu este încă preluat din produs)
- Import comenzi din Doraly în Odoo: da
- Export comenzi din Odoo către Doraly: nu
- Generare AWB: nu
- Trimitere factură PDF: da (linkul facturii PDF, după postare)
- Configurarea backend-ului: în **Marketplace > Backends** se creează un backend cu **Provider** = **Doraly**; alegerea furnizorului completează **Location** (fila **Credentials**), apoi, cu **Access Type** = **User and password**, se introduc e-mailul contului de vendor Doraly (**Username**) și **Password**, iar **Test connection** trece backend-ul din **Not Confirmed** în **Confirmed**.
- Transportator implicit: în fila **Orders and Products**, grupul **Settings**, câmpul **Default Carrier** — Doraly trimite doar valoarea transportului, nu curierul, deci acest transportator se folosește pentru linia de transport a comenzilor importate; fără el, comenzile se importă fără linie de transport.
- Importul obiectelor: în fila **Objects**, din meniul **⋮** al unui card, se alege **Import** pentru **Categories**, **Products**, apoi **Sale Order**; importul rulează ca job în fundal, iar cardul **Categories** nu este creat automat de backend-ul Doraly — se adaugă manual în fila **Objects**.
- Produse: se listează în **Marketplace > Bindings > Product Variants**; fiecare produs Doraly este legat de un produs Odoo (codul vendorului devine referința internă, codul Doraly este **External Code**); se importă doar codul și denumirea, fără preț, stoc sau descriere. Categoriile apar în **Marketplace > Bindings > Categories**, dar în această versiune importul de categorii ignoră răspunsul Doraly și creează mereu aceeași categorie-exemplu (*Termometre*).
- Comenzi: fiecare comandă Doraly devine o comandă de vânzare cu numele numărului comenzii Doraly, clientul (identificat după telefon sau e-mail), adresele de facturare și livrare, **Phase** preluată din statusul Doraly, linie de transport pe transportatorul implicit (valoare fără TVA) și liniile de produs; Doraly trimite valoarea liniei cu TVA, iar prețul unitar fără TVA se extrage din ea cu taxa produsului, astfel încât totalul comenzii să fie egal cu totalul Doraly; **Order Date** devine data confirmării în Odoo.
- Trimiterea facturii: din comandă se apasă **Create Invoice** (**Regular invoice**), se verifică egalitatea totalului facturii cu totalul comenzii Doraly, apoi **Confirm**; confirmarea facturii pune în coadă jobul `marketplace.sale.order.after_invoice_post`, care trimite către Doraly linkul de portal al facturii PDF, construit din parametrul de sistem `web.base.url` (trebuie să fie adresa publică a Odoo); starea **Done** a jobului (vizibil prin butonul **Jobs**, după scoaterea filtrelor implicite) înseamnă că Doraly a acceptat apelul.
- Maparea câmpurilor de produs: ID produs (`external_id`) și cod Doraly (`external_code`) Doraly → Odoo; referința internă (`default_code` ↔ `productCode`) și denumirea (`name` ↔ `productName`) în ambele sensuri; greutate, categorie (cea mapată pentru `categ_id` sau categoria implicită a backend-ului) și descriere (`website_short_description` → `longDescription`) Odoo → Doraly; brandul este trimis fix ca „Philips”.
- Limitări cunoscute: erorile HTTP 429/5xx nu sunt reîncercate automat (jobul eșuat se repune în coadă din **Jobs**); exportul de produse trimite mereu brandul „Philips”; exportul comenzilor și al stocului, precum și generarea AWB nu sunt implementate; integrarea de livrare (`delivery.py`) este doar un schelet, iar pentru importul de curieri se folosește tipul de livrare `emag`, copiat din conectorul eMAG; nu există paginare la importuri.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_website_short_description](../deltatech_website_short_description/index.md)
- `delivery`
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)

#### 4. Componente Cheie

Documentația din `readme/DESCRIPTION.md` acoperă scopul și funcționalitățile modulului, fără a detalia componentele tehnice. Conform fluxului de ingestie, analiza detaliată a modelelor, vizualizărilor și acțiunilor automate a fost omisă, întrucât nu este menționată explicit în Readme. Singurele componente menționate în readme sunt jobul `marketplace.sale.order.after_invoice_post` (trimiterea linkului facturii) și vizualizarea backend-ului (`views/backend_views.xml`) cu câmpul **Default Carrier**.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază pentru conectarea Odoo la marketplace-uri (backend, adaptoare, binding-uri), pe care se construiește conectorul Doraly.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionarea importului și sincronizării comenzilor de vânzare din marketplace.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): cartografierea stadiilor comenzilor între Doraly și Odoo.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): gestionarea metodelor de livrare asociate marketplace-ului; câmpul **Default Carrier** a fost mutat de acolo în acest conector (19.0.0.0.8).
