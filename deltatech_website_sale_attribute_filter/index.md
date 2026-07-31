# Website Sale Attribute Filter (localizat la `deltatech_website_sale_attribute_filter/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_attribute_filter`
- **Versiune:** `19.0.0.1.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_attribute_filter`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_attribute_filter`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul filtrează dinamic valorile atributelor afișate în panoul de filtre al magazinului online, astfel încât clientul să vadă doar opțiunile relevante pentru produsele afișate în acel moment (de exemplu, în urma unei căutări sau la navigarea într-o categorie). În mod implicit, Odoo listează toate valorile posibile ale unui atribut, chiar dacă unele nu mai corespund niciunui produs vizibil pe pagină — ceea ce derutează clientul. Modulul rezolvă această problemă și, în plus, păstrează starea panoului de filtre (acordeoane deschise, panoul mobil off-canvas, poziția de scroll) la fiecare reîncărcare a paginii declanșată de o selecție de filtru, pentru o experiență de cumpărare mai fluidă.

#### 2. Funcționalități Cheie

- Filtrează dinamic valorile atributelor de produs din pagina magazinului online, pe baza produselor afișate efectiv la momentul respectiv.
- Asigură că în bara laterală de filtre și în meniul off-canvas apar doar valorile de atribut relevante (aparținând produselor vizibile).
- Suportă toate tipurile standard de afișare a atributelor din Odoo: liste derulante (select), butoane radio, pastile (pills), selecție multiplă (checkbox-uri) și atribute de culoare.
- Actualizează automat filtrele la căutare sau la navigarea între categorii.
- Păstrează starea interfeței de filtrare (acordeoane extinse, panou mobil off-canvas deschis, poziția de scroll) la reîncărcarea paginii provocată de fiecare selecție de filtru, astfel încât clientul nu trebuie să redeschidă filtrele de fiecare dată.
- Optimizat pentru performanță, identificând eficient valorile de atribut active pornind din liniile de atribute ale șablonului de produs (`product.template.attribute.line`).
- Compatibil cu structura standard eCommerce a Odoo și cu filtrele responsive de tip off-canvas.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie de mai sus provin din `readme/DESCRIPTION.md`. Conform fluxului de ingestie, componentele tehnice detaliate mai jos completează informația doar cu elementele structurale (controller, șabloane, interacțiune frontend), fără o analiză suplimentară a modelelor (modulul nu definește modele noi).

- **Controller** (`controllers/main.py`): `WebsiteSaleAttributeFilter` extinde `WebsiteSale.shop()` din `website_sale` — pentru produsele găsite (`search_product`), caută liniile `product.template.attribute.line` corespunzătoare și populează contextul șablonului cu `active_attribute_value_ids`, mulțimea de identificatori ai valorilor de atribut relevante.
- **Șabloane** (`views/templates.xml`): moștenește sub-șabloanele Odoo 19 ale panoului de filtre (`website_sale.filter_select_attributes`, `filter_color_attributes`, `filter_image_attributes`, `filter_pills_attributes`, `filter_radio_and_multi_attributes`) și le filtrează bucla `value_ids` astfel încât să afișeze doar valorile prezente în `active_attribute_value_ids`.
- **Interacțiune frontend** (`static/src/interactions/attribute_filter_state.esm.js`, încărcat în `web.assets_frontend`): componentă OWL de interacțiune care salvează și restaurează starea vizuală a panoului de filtre (acordeoane deschise, panoul off-canvas mobil, poziția de scroll) la reîncărcările de pagină declanșate de selectarea unui filtru.

**Vizualizări**

- Nu sunt definite vizualizări noi (formulare/liste/kanban); modulul intervine exclusiv prin moștenirea șabloanelor QWeb ale filtrelor de atribute din `website_sale`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_website_sale_attributes](../deltatech_website_sale_attributes/index.md): rezolvă o problemă complementară de filtrare a atributelor — filtrează valorile afișate pe pagina fișei de produs (`website_sale.products_attributes`), în timp ce acest modul filtrează valorile din panoul de filtre al paginii de listă a magazinului (`shop`).
- [deltatech_website_sale_sort](../deltatech_website_sale_sort/index.md): modul din aceeași zonă a paginii de magazin online, care adaugă criterii suplimentare de sortare a produselor afișate.
