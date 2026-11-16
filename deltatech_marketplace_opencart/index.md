# OpenCart Marketplace Connector (localizat la `deltatech_marketplace_opencart/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_opencart`
- **Versiune:** `19.0.0.2.17`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_opencart
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_opencart`
- **Ultima Ingestie:** `2026-11-16`

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
- Importul comenzilor include și liniile de discount și comentariile, iar clienții înregistrați și cei ocazionali sunt importați cu adrese de livrare și facturare; metodele de livrare importate creează un produs de tip serviciu corespunzător, dacă nu există deja.
- Importul produselor și clienților rulează pe pagini, fiecare pagină următoare fiind pusă în coadă cu o cheie de identitate per backend și pagină, iar un import nou se oprește la început cât timp paginile altuia încă rulează.
- Webhook în timp real: OpenCart poate apela Odoo (clienți, produse, comenzi), după înregistrarea magazinului pe URL-ul standard de webhook al Marketplace, astfel încât o modificare din magazin să ajungă în Odoo fără a aștepta următorul import programat; rulează alături de import, nu în locul lui.
- Transportatorul unei comenzi importate provine exclusiv din binding-ul `marketplace.delivery.carrier` (găsit sau creat din codul de livrare OpenCart); câmpul *Default Carrier* al backend-ului nu mai este folosit ca alternativă — dacă nu se poate determina un transportator, linia de livrare este omisă și se loghează un avertisment. Punctul de ridicare (locker) importat se stochează pe `marketplace.sale.order.marketplace_locker`.
- Limitări: anularea unei comenzi în OpenCart nu ajunge în Odoo; nu există flux automat de retur/notă de credit în niciun sens; cupoanele apar doar ca linii simple de comandă; nu se verifică stocul la import (fără protecție la supravânzare); nu există tablou de bord de analiză sau puncte de loialitate; mai multe magazine OpenCart pot fi configurate ca backend-uri separate, dar scenariul nu a fost validat; evenimentele de sincronizare se scriu în logul serverului, nu într-un istoric dedicat pe înregistrare.
- Cerințe: magazin OpenCart cu acces la REST Admin API și credențiale API.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_brand](../deltatech_marketplace_brand/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform DESCRIPTION.md, modulul definește următoarele evenimente și automatizări (singurele componente menționate explicit în Readme):

**Acțiuni Automate / Acțiuni Server**

- Preluarea comenzilor din OpenCart în Odoo se execută automat printr-o sarcină programată (`ir.cron`), cu o periodicitate de 2 ore.
- Transmiterea stocului din Odoo în OpenCart se face automat după modificarea stocului în Odoo.
- Actualizarea unui produs Odoo deja mapat cu un produs OpenCart declanșează automat actualizarea produsului corespondent din OpenCart.
- Adăugarea unui produs nou în Odoo NU declanșează automat crearea produsului în OpenCart; utilizatorul trebuie să lanseze manual acțiunea de transmitere a produsului (sau o acțiune programată pe o listă selectată), astfel încât nimic să nu ajungă în vitrină înainte de momentul dorit.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul generic Marketplace peste care este construit acest conector (backend, binding-uri, sincronizare).
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionează importul comenzilor de vânzare aduse din OpenCart.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): gestionează metodele de livrare preluate din OpenCart.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): gestionează maparea metodelor de plată dintre OpenCart și Odoo.
- [deltatech_marketplace_brand](../deltatech_marketplace_brand/index.md): oferă gestiunea brandurilor produselor sincronizate.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): expune informațiile de website (descriere, SEO, stare publicare) folosite la sincronizarea produselor.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): furnizează etapele de comandă în care se mapează statutul comenzii din OpenCart.
