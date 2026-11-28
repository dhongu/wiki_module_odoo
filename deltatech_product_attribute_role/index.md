# Product Attribute Role (localizat la `deltatech_product_attribute_role/index.md`)

- **Nume Tehnic:** `deltatech_product_attribute_role`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_attribute_role
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_attribute_role`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un **rol** atributelor de produs, astfel încât codul să găsească un atribut după rolul lui (de exemplu soi, mărime, calitate), nu după numele său, care e traductibil și poate fi redenumit. Este o bază tehnică pentru alte module care definesc rolurile de care au nevoie.

#### 2. Funcționalități Cheie

- Redenumirea sau traducerea unui atribut nu mai strică loturile, rapoartele sau documentele tipărite care se bazează pe el.
- Un singur atribut per rol: baza de date refuză un al doilea atribut cu același rol.
- Rolurile sunt partajate între module: fiecare modul adaugă rolurile necesare, iar câmpul, regula și căutările sunt comune. Modulul nu definește roluri proprii.
- Rolul se alege în *Inventory > Configuration > Attributes*, în formularul atributului; lista e goală dacă niciun modul instalat nu adaugă roluri. Pentru a muta un rol, se golește mai întâi atributul care îl deține.
- Pentru dezvoltatori: `_get_attribute_by_role(rol)` returnează atributul, `_get_attribute_value_by_role(rol)` valoarea variantei, iar în domenii se filtrează după `attribute_id.attribute_role`.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `product.attribute`: câmpul `attribute_role` (selecție extensibilă, unic) și metoda de căutare după rol.
- `product.product`: metoda `_get_attribute_value_by_role`.

**Vizualizări**

- `product_attribute_views.xml`: afișează rolul în lista și formularul atributelor.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu există conexiuni verificate cu alte pagini wiki; modulele de clasificare a merelor (soi, calitate, mărime) adaugă roluri aici.
