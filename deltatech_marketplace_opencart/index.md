# OpenCart Marketplace Connector (localizat la `deltatech_marketplace_opencart/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_opencart`
- **Versiune:** `19.0.0.2.2`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_marketplace_opencart
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_opencart`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul este un conector între platforma de comerț electronic OpenCart și Odoo, construit peste cadrul generic Marketplace al suitei Deltatech. El sincronizează bidirecțional informațiile esențiale dintr-un magazin online OpenCart: aduce în Odoo clienții, categoriile, metodele de plată și de livrare, opțiunile (atributele) și produsele cu variantele lor, precum și comenzile cu liniile și adresele aferente. În sens invers, trimite din Odoo către OpenCart stocurile și actualizările de produse (produse noi sau modificate). Astfel, o afacere care folosește OpenCart ca vitrină online își poate gestiona centralizat catalogul, stocul și comenzile direct din Odoo. Conectorul se bazează pe REST Admin API-ul OpenCart (https://opencart-api.com/product/rest-admin-api/).

#### 2. Funcționalități Cheie

- Import șabloane de produs cu variante din OpenCart și export produse din Odoo către OpenCart.
- Import atribute (opțiuni) și valorile lor; crearea automată a atributelor lipsă în OpenCart la exportul produselor.
- Import comenzi de vânzare, inclusiv liniile de comandă, clienții asociați și costul de livrare.
- Import metode de livrare din OpenCart.
- Import categorii publice (categorii de ecommerce) din OpenCart în Odoo.
- Import clienți din OpenCart (nume și prenume concatenate, localitate, cod poștal, telefon, stradă).
- Maparea manuală a metodelor de plată din OpenCart cu metodele de plată din Odoo.
- Preluarea comenzilor cu adrese de livrare și de facturare (un singur contact dacă adresele coincid) și preluarea statutului comenzii în câmpul de etapă.
- Maparea automată produs Odoo ↔ produs OpenCart pe baza SKU; preluare nume, sku, model, masă, preț de listă, meta date, descriere website, stare publicare, imagine principală și imagini suplimentare, cod de bare, opțiuni și id-ul produsului OpenCart.
- Transmiterea stocului din Odoo în OpenCart pentru produs și pentru fiecare opțiune.
- Completarea câmpului `product_seo_url` din `website_url`-ul Odoo doar pentru produsele noi.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `deltatech_marketplace_brand`
- `deltatech_marketplace_website`
- `deltatech_marketplace_sale_stage`
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform DESCRIPTION.md, modulul definește următoarele evenimente și automatizări (singurele componente menționate explicit în Readme):

**Acțiuni Automate / Acțiuni Server**

- Preluarea comenzilor din OpenCart în Odoo se execută automat printr-o sarcină programată (`ir.cron`), cu o periodicitate de 2 ore.
- Transmiterea stocului din Odoo în OpenCart se face automat după modificarea stocului în Odoo.
- Actualizarea unui produs Odoo deja mapat cu un produs OpenCart declanșează automat actualizarea produsului corespondent din OpenCart.
- Adăugarea unui produs nou în Odoo NU declanșează automat crearea produsului în OpenCart; utilizatorul trebuie să lanseze manual acțiunea de transmitere a produsului.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul generic Marketplace peste care este construit acest conector (backend, binding-uri, sincronizare).
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionează importul comenzilor de vânzare aduse din OpenCart.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): gestionează metodele de livrare preluate din OpenCart.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): gestionează maparea metodelor de plată dintre OpenCart și Odoo.
