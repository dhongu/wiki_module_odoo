# Produse Furnizori (localizat la `deltatech_vendor_products/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/19.0/deltatech_vendor_products
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Deltatech Vendor Products automatizează și simplifică gestiunea datelor de produs provenite de la mai mulți furnizori. Modulul creează o punte între cataloagele de produse ale furnizorilor și inventarul Odoo, facilitând importul, actualizarea și sincronizarea informațiilor despre produse — inclusiv prețuri, disponibilitate și imagini. Astfel, companiile care lucrează cu mulți furnizori pot administra cataloage mari fără intervenție manuală: economisesc timp, păstrează informațiile la zi, asigură consistența prețurilor și reduc erorile de introducere a datelor. Un avantaj important este că permite definirea unui catalog de produse furnizor fără ca acestea să fie create obligatoriu ca produse în baza de date Odoo, iar pe baza listei importate se pot crea produse noi sau actualiza cele existente.

#### 2. Funcționalități Cheie

- Import produse furnizor din formate variate de fișier (XLSX, CSV, XML)
- Import date de produs din URL-uri sau feed-uri de furnizor
- Procesarea feed-urilor de produse de la furnizori, inclusiv format feed XML [Google Merchant Center](https://support.google.com/merchants/answer/7052112)
- Potrivire automată a produselor cu cele existente în Odoo (algoritmi avansați de matching)
- Creare de produse noi din datele furnizorului
- Actualizare prețuri pe baza unor reguli configurabile (preț de bază, adaos, discount) cu suport pentru conversie valutară
- Sincronizarea disponibilității produselor de la furnizori
- Descărcarea și atașarea automată a imaginilor de produs
- Atribuire automată a categoriei de produs și maparea codurilor de produs furnizor către coduri interne
- Importul unui număr foarte mare de produse (50.000 în ~30 secunde) cu procesare în fundal
- Coloanele specifice furnizorului (greutate, referințe OEM, dimensiuni etc.) sunt stocate în câmpul jsonb `attributes` al produsului de furnizor; la importul CSV, coloanele fixe (cod, denumire, prețuri, cod de bare) rămân în câmpurile proprii, iar restul ajung în `attributes`
- Butonul *Load Price* din feed este vizibil pentru orice conector API (Kramp, Bepco, Granit etc.), nu doar pentru tipul generic `api`; rămâne ascuns pentru tipurile `none` și `url`
- Acțiunile *Generate Product* și *Update Purchase Price* afișează, la selecții de 80 de rânduri sau mai multe, un dialog de progres: selecția e procesată în loturi de `deltatech_vendor_products.page_size` rânduri (câte o cerere pe lot), cu procent, timp estimat rămas și număr de lot; fiecare lot se salvează separat, loturile eșuate sunt listate, iar *Stop after this batch* oprește rularea. Nu necesită queue_job
- Produsele se creează în pagini de `page_size` rânduri (în fundal dacă e instalat queue_job, direct altfel); *Update Purchase Price* creează mereu produsele înainte de a scrie prețurile
- Codurile duplicate din același lot de import sunt îmbinate înainte de inserarea în masă (se păstrează ultimul rând, cu avertisment în log), pentru toate căile de import (CSV, xls/xlsx, Google XML, conectori API)
- Stă la baza altor module care permit căutarea pe website după codul de produs al furnizorului

#### 3. Dependențe

- `product`
- `purchase`
- `stock`
- `purchase_stock`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie au fost preluate din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune este omisă, cu excepția celor de mai jos, verificate în cod.

**Modele**

- `vendor.feed`: feed-ul/conectorul unui furnizor (format, mapare, reguli de preț, conexiune).
- `vendor.product`: catalogul de produse al furnizorului, independent de produsele Odoo.
- `vendor.product.import` (wizard): importul catalogului din fișier (CSV, xls/xlsx).
- `product.supplierinfo` (extins): recalculează termenul de livrare din data de disponibilitate.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_vendor_feed_update_product_list`: importă periodic lista de produse din feed-uri.
- `ir_cron_update_purchase_price` și `ir_cron_update_list_price`: actualizează zilnic prețul de achiziție, respectiv prețul de listă.

#### 5. Conexiuni

- [deltatech_vendor_products_granit](../deltatech_vendor_products_granit/index.md): extensie care adaugă integrarea specifică furnizorului Granit peste cadrul de import al acestui modul.
- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): extensie care expune produsele de furnizor pe website, permițând căutarea după codul de produs al furnizorului.
- [deltatech_vendor_products_bepco](../deltatech_vendor_products_bepco/index.md): extensie care adaugă integrarea specifică furnizorului Bepco peste cadrul de import al acestui modul.
- [deltatech_vendor_products_kramp](../deltatech_vendor_products_kramp/index.md): extensie care adaugă integrarea specifică furnizorului Kramp peste cadrul de import al acestui modul.
