# Price Category (localizat la `deltatech_price_categ/index.md`)

- **Nume Tehnic:** `deltatech_price_categ`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_price_categ
- **Cale Locală:** `odoo-addons/deltatech/deltatech_price_categ`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul introduce prețuri pe niveluri (Bronze, Copper, Silver, Gold) pentru produse, calculate prin adaosuri procentuale configurabile peste un preț de bază. Fiecare produs poate avea astfel automat prețuri diferențiate pe categorii de clienți sau canale de vânzare.

#### 2. Funcționalități Cheie

- **Prețuri pe niveluri:** pe șablonul de produs se completează adaosul procentual pentru fiecare nivel, iar prețurile se calculează automat din prețul de bază ales.
- **Preț de bază:** **List Price**, **Cost Price** sau **Last Purchase Price** (implicit); prețurile cu sau fără TVA inclus sunt tratate corect. Câmpurile se găsesc pe tabul **Sales** sau **Inventory** al produsului.
- **Liste de prețuri:** elementele de listă de prețuri primesc nivelurile ca opțiuni de bază, pentru reguli dinamice care pornesc de la prețul Bronze, Silver etc.
- **Monitorizarea problemelor de preț:** un câmp calculat semnalează inconsecvențe în ierarhie (de exemplu Gold mai mare decât Silver).

#### 3. Dependențe

- `product`
- `account`
- `sale`
- [deltatech_purchase_price](../deltatech_purchase_price/index.md)
- `website_sale`

#### 4. Componente Cheie

Sumarul provine din `readme/DESCRIPTION.md`; componentele au fost verificate punctual în cod.

**Modele**

- `product.template` (extins): adaosurile `percent_*`, prețurile `list_price_*`, `list_price_base` și `price_issue`; urmărire în chatter pentru `list_price` și `standard_price`.
- `product.pricelist.item` (extins): câmpul `base` primește opțiunile de preț pe niveluri.

**Vizualizări**

- `views/product_view.xml`: câmpurile de nivel de preț în formularul produsului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_purchase_price](../deltatech_purchase_price/index.md): furnizează ultimul preț de achiziție, folosit ca bază de calcul.
