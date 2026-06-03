# Price Category (localizat la `deltatech_price_categ/index.md`)

- **Nume Tehnic:** `deltatech_price_categ`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_price_categ
- **Cale Locală:** `odoo-addons/deltatech/deltatech_price_categ`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul introduce un sistem de prețuri pe niveluri (categorii de preț) pentru produse în Odoo. Permite companiilor să definească mai multe trepte de preț — Bronze, Copper, Silver și Gold — pornind de la un preț de bază și aplicând adaosuri procentuale configurabile. Astfel, fiecare produs poate avea automat prețuri diferențiate pentru diverse categorii de clienți sau canale de vânzare, fără calcule manuale.

#### 2. Funcționalități Cheie

- **Structură de prețuri pe niveluri**: adaugă pe șablonul de produs câmpuri de adaos procentual pentru Bronze, Copper, Silver și Gold și calculează automat prețurile corespunzătoare pe baza prețului de bază selectat.
- **Selectarea flexibilă a prețului de bază**: prețul de bază pentru calculul adaosului poate fi prețul de listă (List Price), prețul de cost (Cost Price) sau ultimul preț de achiziție (Last Purchase Price); gestionează corect prețurile cu sau fără TVA inclus.
- **Integrare cu listele de prețuri**: extinde elementele standard de pricelist din Odoo pentru a include noile trepte de preț ca opțiuni de bază, permițând reguli de prețuri dinamice care fac referire la prețurile calculate (Bronze, Silver etc.).
- **Monitorizarea problemelor de preț**: include un câmp calculat care detectează inconsistențe în ierarhia de prețuri (de exemplu, când prețul Gold este mai mare decât prețul Silver).

#### 3. Dependențe

- `product`
- `account`
- `sale`
- [deltatech_purchase_price](../deltatech_purchase_price/index.md)
- `website_sale`

#### 4. Componente Cheie

Documentat din `readme/DESCRIPTION.md`; analiza detaliată a codului (modele, vizualizări, acțiuni) nu a fost necesară conform fluxului de ingestie. La nivel general, modulul extinde modelele de produs (`product.template`) cu câmpuri pentru treptele de preț și adaosurile procentuale, extinde elementele de listă de prețuri (`product.pricelist.item`) cu noile baze de preț și adaugă câmpurile aferente în vizualizarea de formular a produsului (`views/product_view.xml`).

#### 5. Conexiuni

- [deltatech_purchase_price](../deltatech_purchase_price/index.md): furnizează ultimul preț de achiziție folosit ca posibilă bază pentru calculul adaosurilor pe trepte.
