# Produse Furnizori (localizat la `deltatech_vendor_products/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products`
- **Versiune:** `20.0.1.4.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/20.0/deltatech_vendor_products
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Deltatech Vendor Products automatizează gestiunea datelor de produs provenite de la mai mulți furnizori. Modulul creează o punte între cataloagele furnizorilor și inventarul Odoo și facilitează importul, actualizarea și sincronizarea informațiilor despre produse — prețuri, disponibilitate și imagini. Un avantaj important este că un catalog de furnizor poate fi definit fără ca produsele să fie create obligatoriu în baza Odoo, iar pe baza listei importate se pot crea produse noi sau actualiza cele existente.

#### 2. Funcționalități Cheie

- Import produse furnizor din fișiere (XLSX, CSV, XML) sau din URL-uri și feed-uri, inclusiv feed XML [Google Merchant Center](https://support.google.com/merchants/answer/7052112).
- Potrivire automată cu produsele existente în Odoo, crearea de produse noi din datele furnizorului și maparea codurilor furnizorului către coduri interne.
- Actualizare de prețuri pe baza unor reguli configurabile (preț de bază, adaos, discount), cu conversie valutară.
- Sincronizarea disponibilității, atribuirea automată a categoriei și descărcarea imaginilor de produs.
- Import foarte rapid (50.000 de produse în ~30 de secunde), cu procesare în fundal.
- Baza altor module care permit căutarea pe website după codul de produs al furnizorului.
- Fluxul pas-cu-pas (feed, import fișier, mapare coloane, asociere produse, actualizare preț), cu capturi, în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `product`
- `purchase`
- `stock`
- `purchase_stock`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`; componentele de mai jos rezultă din cod și din fișierele de date.

**Modele**

- `vendor.feed` / `vendor.feed.column`: feed-ul unui furnizor (format, mapare de câmpuri, reguli de preț, categorie implicită, monedă) și coloanele sale.
- `vendor.product`: catalogul de produse al furnizorului.
- `vendor.product.import` / `vendor.product.import.column`: wizardul de import din fișier și maparea coloanelor.
- `product.supplierinfo` (extins): legătura cu catalogul furnizorului.

**Vizualizări**

- `view_vendor_feed_form` / `_tree` / `_filter` și `action_vendor_feed`: feed-urile furnizorilor.
- `view_vendor_product_form` / `_tree` / `_filter` și `action_vendor_product`: catalogul furnizorilor.
- `view_vendor_product_import_form` și `action_vendor_product_import`: importul din fișier.
- `product_supplierinfo_tree_view` / `product_supplierinfo_form_view`: extensiile listei de furnizori a produsului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_vendor_feed_update_product_list`: actualizarea periodică a listei de produse din feed-uri.
- `ir_cron_update_purchase_price`: actualizarea prețului de achiziție.
- `ir_cron_update_list_price`: actualizarea prețului de listă.

#### 5. Conexiuni

- [deltatech_vendor_products_granit](../deltatech_vendor_products_granit/index.md): integrarea specifică furnizorului Granit.
- [deltatech_vendor_products_kramp](../deltatech_vendor_products_kramp/index.md): integrarea specifică furnizorului Kramp.
- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): expune produsele de furnizor pe website, cu căutare după codul furnizorului.
