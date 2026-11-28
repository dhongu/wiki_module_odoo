# Grup de Utilizatori pe Categoria de Produse (localizat la `deltatech_product_category_group/index.md`)

- **Nume Tehnic:** `deltatech_product_category_group`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_category_group
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_category_group`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul leagă categoriile de produse de un grup de utilizatori și atribuie responsabilul transferurilor din acel grup, repartizând munca echilibrat între membri. Într-un depozit în care fiecare echipă se ocupă de propriile familii de produse, transferurile pregătite ajung la oamenii potriviți.

#### 2. Funcționalități Cheie

- Câmpul **User Group** pe categoria de produse; membrii grupului sunt cei care procesează produsele categoriei.
- Butonul **Responsible** pe lista de transferuri: completează **Responsible** doar pe transferurile în starea **Ready** fără responsabil, celelalte rămân neschimbate. Butonul este vizibil administratorilor Inventar.
- Repartizare echilibrată: pentru fiecare transfer se adună grupurile categoriilor produselor (până la trei niveluri de părinți), apoi membrii activi, utilizatori interni cu dreptul Inventar **User** și permiși în compania transferului. Se alege întâi un utilizator fără transferuri Ready, altfel cel cu cele mai puține.
- Metoda `responsible_determination` poate fi apelată și din cod, de exemplu după rezervare.
- Limitări: atribuirea nu este automată (doar din buton sau din cod) și contează doar membrii direcți ai grupului, nu cei care îl primesc printr-un grup implicat.

#### 3. Dependențe

- `product`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.category`: câmpul `user_group_id`.
- `stock.picking`: câmpul `user_group_id` și metoda `responsible_determination`.

**Vizualizări**

- `views/product_category_view.xml`: câmpul pe categoria de produse.
- `views/stock_picking_view.xml`: butonul **Responsible** pe lista de transferuri.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_product_category_color](../deltatech_product_category_color/index.md): modul înrudit, tot pe categoriile de produse și transferurile de stoc, fără dependență declarată.
