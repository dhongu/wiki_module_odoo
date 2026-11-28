# Product Attribute Extension - Website (localizat la `deltatech_product_attribute_website/index.md`)

- **Nume Tehnic:** `deltatech_product_attribute_website`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_product_attribute_website
- **Cale Locală:** `odoo-addons/bitshop/deltatech_product_attribute_website`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează pe site atributele de produs de tip Da/Nu din [deltatech_product_attribute](../deltatech_product_attribute/index.md). Se instalează automat când sunt instalate atât acel modul, cât și eCommerce (`website_sale`). Magazinul standard nu are un șablon pentru acest tip de afișare: fără modul, atributul nu apare pe pagina produsului și nu are filtru.

#### 2. Funcționalități Cheie

- **Pagina produsului**: un atribut Da/Nu se oferă ca două butoane radio, Da și Nu, prin care clientul alege varianta (de exemplu cămașă cu sau fără mânecă lungă).
- **Filtre în magazin**: atributul Da/Nu are filtrul său în coloana din stânga, cu valorile Da și Nu.

#### 3. Dependențe

- [deltatech_product_attribute](../deltatech_product_attribute/index.md)
- `website_sale`

#### 4. Componente Cheie

**Modele**

- Nu definește modele.

**Vizualizări**

- `variants` (moștenește `website_sale.variants`): butoanele radio Da/Nu pe pagina produsului.
- `product_attribute_filters_form` (moștenește `website_sale.product_attribute_filters_form`): filtrul Da/Nu din magazin.

**Acțiuni Automate / Acțiuni Server**

- Nu are. Modulul este `auto_install`.

#### 5. Conexiuni

- `website_sale`: magazinul standard ale cărui șabloane (pagina produsului și filtrele) sunt extinse.
