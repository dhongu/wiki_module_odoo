# Product Attribute Extension (localizat la `deltatech_product_attribute/index.md`)

- **Nume Tehnic:** `deltatech_product_attribute`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_product_attribute
- **Cale Locală:** `odoo-addons/bitshop/deltatech_product_attribute`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă reguli pentru atributele produselor, verificate la salvarea produsului (inclusiv la import sau prin API), astfel încât catalogul să rămână complet și coerent: grupuri de atribute cu limite, atribute obligatorii pe categorii și atribute de tip Da/Nu.

#### 2. Funcționalități Cheie

- **Grupuri de atribute cu limite**: fiecare atribut dintr-un grup acceptă pe produs fie o singură valoare, fie între un minim și un maxim de valori (0: fără limită). Schimbarea limitelor sau mutarea unui atribut într-un grup este refuzată cât timp un produs nu le respectă. Grupurile se găsesc în *Sales → Products → Attribute group* (necesită activarea *Variants*).
- **Atribute obligatorii pe categorie de produs**, moștenite de subcategorii. Un setare de companie alege între avertisment pe formularul produsului (implicit) și blocarea salvării; un buton pe categorie listează produsele care nu au un atribut obligatoriu.
- **Atribute Da/Nu**: tip nou de afișare (*Boolean*). Atributul primește singur valorile Da și Nu (traduse) și are mereu exact aceste două valori (pot fi redenumite); a treia valoare sau ștergerea uneia este refuzată. În numele variantei apare doar numele atributului, și doar pentru Da: „Cămașă Oxford (S, Mânecă lungă)”.
- **Ordonare pe grup**: o linie nouă de atribut pe produs se așază după grup, apoi după atribut; lista de atribute și liniile produsului arată grupul, cu filtru și grupare după grup.

#### 3. Dependențe

- `product`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.attribute.group`: grupul de atribute (tip, minim, maxim, ordine).
- `product.attribute`, `product.attribute.value`: grupul atributului, tipul Boolean și valorile Da/Nu.
- `product.template`, `product.template.attribute.line`, `product.template.attribute.value`: verificarea limitelor și numele curat al variantelor.
- `product.category`: atributele obligatorii.
- `res.company`, `res.config.settings`: setarea de avertisment sau blocare.

**Vizualizări**

- `product_attribute_group_view_tree` / `_form`, `action_attribute_group`: grupurile de atribute.
- `product_attribute_view_form`, `attribute_tree_view`, `product_attribute_search`: grupul pe atribut, filtru și grupare.
- `product_template_only_form_view`: avertismentul pe produs.
- `product_category_form_view`: atributele obligatorii și butonul de produse fără ele.
- `res_config_settings_view_form`: setarea de blocare.

**Acțiuni Automate / Acțiuni Server**

- Nu are sarcini cron sau acțiuni server. Controllerul `product_configurator` afișează atributele Da/Nu ca butoane radio în configuratorul de produs din vânzări.

#### 5. Conexiuni

- [deltatech_product_attribute_website](../deltatech_product_attribute_website/index.md): afișează atributele Da/Nu pe site (se instalează automat cu `website_sale`).
