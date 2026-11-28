# Manager mărci produse

- **Nume Tehnic:** `product_brand`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/others_addons/tree/20.0/product_brand
- **Cale Locală:** `odoo-addons/others_addons/product_brand`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite gestionarea simplă a mărcilor de produse. Fiecare marcă poate avea logo, partener asociat și descriere, iar produsele se pot grupa și analiza pe marcă în rapoartele de vânzări și facturare.

#### 2. Funcționalități Cheie

- Mărci în **Vânzări > Configurare > Produse > Product Brands**, cu logo, partener asociat și descriere.
- Câmpul Brand pe produs, sub numele acestuia.
- Marca devine dimensiune de grupare în **Vânzări > Raportare > Vânzări** (inclusiv pivot) și în **Facturare > Raportare > Management > Invoice Analysis**.
- Căutare, kanban și liste de produse cu informația mărcii.
- Planificat (roadmap): câmp cu mărcile asociate unui client sau furnizor în formularul partenerului.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `product.brand`: marca de produs.
- `product.template` (extins): câmpul marcă.

**Vizualizări**

- `view_product_brand_form`, `view_product_brand_tree`, `view_product_brand_kanban`, `product_brand_search_form_view`: gestionarea mărcilor.
- `product_template_form_brand_add`, `view_product_template_search_brand`, `view_product_template_tree_brand`, `view_product_template_kanban_brand`, `view_product_variant_tree_brand`, `view_product_variant_kanban_brand`: marca pe produse și variante.

**Acțiuni Automate / Acțiuni Server**

- `action_product_brand`, `action_open_brand_products`, `action_open_single_product_brand`: acțiuni de fereastră pentru mărci și produsele lor. Nu există cron-uri.

#### 5. Conexiuni

- `website_sale_product_brand` ([pagină](../website_sale_product_brand/index.md)): filtrare și pagini de marcă în magazinul online.
