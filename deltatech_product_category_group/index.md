# Products Category User Group (localizat la `deltatech_product_category_group/index.md`)

- **Nume Tehnic:** `deltatech_product_category_group`
- **Versiune:** `19.0.1.0.10`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_category_group
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_category_group`
- **Ultima Ingestie:** `2026-11-10`

#### 1. Sumar

Într-un depozit în care fiecare echipă se ocupă de propriile familii de produse, transferurile gata de procesat trebuie să ajungă la oamenii potriviți, iar munca să fie împărțită echilibrat între ei. Modulul leagă categoriile de produse de un grup de utilizatori și, la cerere, atribuie responsabilul transferurilor din acel grup. Atribuirea nu este automată: rulează din butonul **Responsible** de pe lista transferurilor sau din cod personalizat.

#### 2. Funcționalități Cheie

- **Grup de utilizatori pe categoria de produs**: câmpul **User Group** pe formularul categoriei; membrii grupului sunt persoanele care se ocupă de produsele categoriei.
- **Butonul Responsible pe lista transferurilor**: se selectează transferuri în listă și se apasă **Responsible** pentru a completa câmpul **Responsible**. Se procesează doar transferurile în starea **Ready** fără responsabil; celelalte rămân neschimbate. Butonul este vizibil administratorilor Inventory (grupul `stock.group_stock_manager`).
- **Atribuire echilibrată**: pentru fiecare transfer se strâng grupurile de utilizatori ale categoriilor produselor din transfer (inclusiv până la trei niveluri de categorii părinte) și se iau membrii lor care sunt utilizatori interni activi, cu dreptul Inventory **User** și cu acces la compania transferului. Dintre ei se alege mai întâi un utilizator fără niciun transfer Ready; altfel, cel cu cei mai puțini transferuri Ready din aceeași companie. Dacă niciun candidat nu este eligibil, transferul rămâne neatribuit.
- Metoda `responsible_determination` poate fi apelată și din cod personalizat, de exemplu după rezervare.
- **Limitări**: se iau în calcul doar membrii direcți ai grupului, nu și utilizatorii care îl primesc printr-un grup implicat.

#### 3. Dependențe

- `product`
- `stock`

#### 4. Componente Cheie

Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md`; mai jos, o verificare punctuală a codului.

**Modele**

- `product.category` (extins): câmpul `user_group_id` („User Group", Many2one către `res.groups`).
- `stock.picking` (extins): câmpul `user_group_id` (grupul folosit la atribuire) și metoda `responsible_determination()`, care alege responsabilul și scrie `user_id` și `user_group_id` prin `write()`; numărul de transferuri Ready pe utilizator se calculează printr-o interogare SQL.

**Vizualizări**

- `product_category_form_view`: moștenește `product.product_category_form_view` și adaugă `user_group_id`.
- `vpicktree`: moștenește `stock.vpicktree` și adaugă în antetul listei butonul „Responsible" (`responsible_determination`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki proprie, în afara dependențelor directe (`product`, `stock`).
