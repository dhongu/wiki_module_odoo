# Internal Category Groups (localizat la `deltatech_category_group/index.md`)

- **Nume Tehnic:** `deltatech_category_group`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_category_group
- **Cale Locală:** odoo-addons/deltatech/deltatech_category_group
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Modulul adaugă două dimensiuni de grupare categoriilor interne de produse: „Tipul categoriei” și „Clasa categoriei”. Ele permit segmentarea portofoliului la un nivel mai fin decât ierarhia standard de categorii, fără a modifica structura existentă. Valoarea principală este în raportare: marja de vânzare, stocurile și facturile pot fi analizate grupat după aceste două criterii.

#### 2. Funcționalități Cheie

- Câmpurile **Category type** și **Category class** pe fiecare categorie de produs, ca relații către liste de configurare dedicate.
- Liste configurabile de tipuri și clase, cu secvență (ordonare prin drag-and-drop), în **Inventar → Configurare → Category options → Category types / Category classes**.
- Căutare și grupare după tip și clasă în raportul de marjă de vânzare (Sale Margin), în analiza stocurilor (`stock.quant`, **Inventar → Raportare → Inventar**) și în analiza facturilor (**Contabilitate → Raportare → Invoice Analysis**).
- Accesul la listele de configurare este controlat de grupul **Manage category groups**, atribuit implicit administratorului; alți utilizatori se adaugă din **Setări → Utilizatori și companii → Grupuri**.
- Pași de configurare: se definesc tipurile și clasele, apoi se atribuie pe categorii (**Inventar → Configurare → Product Categories**); filtrele de grupare devin utile doar după ce categoriile sunt etichetate.

#### 3. Dependențe

- [deltatech_sale_commission](../deltatech_sale_commission/index.md)

#### 4. Componente Cheie

**Modele**

- `category.group.type` și `category.group.class`: listele de tipuri și clase ale categoriilor (nume, secvență).
- `product.category` (extins): `category_group_type` și `category_group_class`.
- `stock.quant` (extins): aceleași două câmpuri, pentru căutare și grupare în analiza stocurilor.
- `sale.margin.report` (extins): `category_type` și `category_class`.
- `account.invoice.report` (extins): `category_type` și `category_class`.

**Vizualizări**

- `category_group_form` și `category_group_search`: câmpurile pe formularul și căutarea categoriilor de produs.
- `view_category_type_tree` / `view_category_type_form` și `view_category_class_tree` / `view_category_class_form`: listele de configurare, cu meniurile aferente.
- `quant_search_view`: filtre pentru stocuri.
- `view_sale_margin_report_filter_group`: filtre pentru raportul de marjă.
- `view_account_invoice_report_search`: filtre pentru analiza facturilor.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. Migrarea `post-migration` (19.0.0.0.6) elimină din grupul „Manage category groups” legăturile implicate greșit către utilizatorii root și admin.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): definește raportul de marjă de vânzare (`sale.margin.report`) extins aici cu tipul și clasa categoriei; ajunge în dependențe prin `deltatech_sale_commission`.
- `stock`: extinde analiza stocurilor (`stock.quant`) cu cele două criterii.
- `account`: extinde raportul de facturi (`account.invoice.report`) cu cele două criterii.
