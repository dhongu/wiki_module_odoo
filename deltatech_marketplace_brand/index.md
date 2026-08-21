# Marketplace Brand addon (localizat la `deltatech_marketplace_brand/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_brand`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_brand
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_brand`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde funcționalitatea Odoo Marketplace cu un sistem complet de gestionare a brandurilor pentru produsele vândute pe diverse platforme de tip marketplace. Din perspectivă de business, permite companiilor să mențină o identitate de brand unitară și asigură faptul că produsele sunt corect categorizate și pot fi căutate după brand pe toate canalele conectate.

#### 2. Funcționalități Cheie

- Gestionarea centralizată a brandurilor de produse în cadrul ecosistemului Odoo.
- Reprezentare consecventă a brandului pe mai multe platforme marketplace (de exemplu eMAG, MerchantPro, Odoo-to-Odoo).
- Raportare și analize îmbunătățite, prin urmărirea vânzărilor în funcție de performanța pe brand.
- Experiență de client îmbunătățită, prin afișarea clară a informațiilor de brand în vitrinele marketplace.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_product_brand](../deltatech_product_brand/index.md)

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost generată din fișierul `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă, întrucât Readme-ul nu menționează explicit componente tehnice. Pentru detalii despre modele, vizualizări și acțiuni, consultați direct codul sursă al modulului (`models/backend.py`, `models/binding_brand.py`, `models/binding_product_template.py`, `views/binding_brand_view.xml`).

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): modulul de bază pentru funcționalitatea de marketplace, pe care acest addon o extinde cu gestionarea brandurilor.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionarea vânzărilor prin marketplace, complementară urmăririi performanței pe brand.
