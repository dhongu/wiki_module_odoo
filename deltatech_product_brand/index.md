# Manager Mărci Produse (Product Brand Manager)

- **Nume Tehnic:** `deltatech_product_brand`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_product_brand
- **Cale Locală:** `odoo-addons/bitshop/deltatech_product_brand`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Acest modul oferă un sistem centralizat de gestionare a mărcilor de produse în Odoo, ajutând companiile să-și organizeze și să-și categorisească întregul catalog în funcție de marcă. Din perspectivă de business, extensia ajută la menținerea unei baze de produse structurate și ușor de căutat, ceea ce îmbunătățește performanța de marketing și vânzări.

#### 2. Funcționalități Cheie

- Identitate de marcă unificată: creare și gestionare a unei ierarhii consistente de mărci pentru toate produsele din Odoo.
- Căutare și descoperire îmbunătățite: filtrare și căutare facilă după marcă.
- Marketing țintit: campanii și strategii de vânzări specifice pe marcă.
- Analize detaliate pe marcă: rapoarte de vânzări și de facturare grupate sau pivotate după marca produsului.
- Gestionare scalabilă a catalogului: organizarea eficientă a unui număr mare de produse și mărci într-o singură interfață.
- Mărcile se administrează din **Sales > Configuration > Products > Product Brands** (logo, partener asociat, descriere); în formularul produsului, câmpul **Brand** apare sub denumire.
- Rapoarte: **Sales > Reporting > Sales** și **Invoicing > Reporting > Management > Invoice Analysis** permit gruparea după marcă sau adăugarea ei ca dimensiune în pivot.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `product.brand`: marca de produs, cu nume, logo, partener asociat, descriere și numărul de produse.
- `product.template`: extins cu câmpul `product_brand_id` (Brand).
- `sale.report`, `account.invoice.report`: extinse cu marca, pentru grupare în rapoarte.

**Vizualizări**

- `views/product_brand_view.xml`: formular/listă pentru mărci și câmpul de marcă în formularul produsului.
- `reports/sale_report_view.xml`, `reports/account_invoice_report_view.xml`: marca adăugată în rapoartele de vânzări și de facturi.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_brand_field](../deltatech_brand_field/index.md): câmp de marcă pe produs, complementar modelului `product.brand` definit aici.
- [deltatech_marketplace_brand](../deltatech_marketplace_brand/index.md): depinde de acest modul și extinde mărcile în contextul marketplace.
