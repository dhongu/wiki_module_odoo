# Product Attribute Role (Rolul atributului de produs)

- **Nume Tehnic:** `deltatech_product_attribute_role`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_attribute_role
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_attribute_role`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un **Rol** pe atributele de produs, astfel încât alte module să găsească atributul potrivit (soiul, calibrul, calitatea etc.) după rol, nu după nume. Numele unui atribut se traduce și poate fi corectat de consultanți, iar clienții îl denumesc diferit; legarea după rol face ca loturile, rapoartele și documentele tipărite să nu se strice la redenumire sau traducere. Modulul este o bază tehnică și nu definește roluri proprii: acestea sunt aduse de modulele care le folosesc.

#### 2. Funcționalități Cheie

- Câmpul **Rol** pe atribut, vizibil în formular și ca coloană opțională în lista atributelor (**Inventar → Configurare → Atribute**).
- Redenumirea și traducerea atributului nu afectează codul care îl caută după rol.
- Un rol poate fi ținut de un singur atribut; baza de date refuză un al doilea atribut cu același rol. Pentru a muta rolul, se golește mai întâi atributul care îl deține.
- Lista de roluri se completează cu rolurile adăugate de modulele instalate; fără un astfel de modul lista e goală și câmpul nu are efect. Rolul se alege o singură dată per bază de date.
- Pentru dezvoltatori: modulele extind selecția cu `selection_add`, apoi folosesc `product.attribute._get_attribute_by_role(rol)` (include și atributele arhivate), `product.product._get_attribute_value_by_role(rol)` sau filtrul `attribute_id.attribute_role` în domenii.
- Configurarea pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `product.attribute` (extins): câmpul `attribute_role` (Selection, inițial goală, necopiată la duplicare), constrângerea `UNIQUE(attribute_role)` și metoda `_get_attribute_by_role`.
- `product.product` (extins): metoda `_get_attribute_value_by_role`, care întoarce valoarea variantei pentru atributul ce deține rolul.

**Vizualizări**

- `product_attribute_view_form`: adaugă câmpul Rol în formularul atributului, după „Create Variants".
- `attribute_tree_view`: adaugă coloana opțională Rol în lista atributelor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `inedit_apple_grading`: modul care adaugă rolurile Soi, Calitate și Calibru (menționat în fișa consultantului; nu are pagină wiki).
