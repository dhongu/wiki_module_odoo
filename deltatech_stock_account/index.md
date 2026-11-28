# Stock Account Extension (localizat la `deltatech_stock_account/index.md`)

- **Nume Tehnic:** `deltatech_stock_account`
- **Versiune:** `20.0.1.0.10`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_account
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_account`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Mici completări la evaluarea stocurilor: valoarea fiecărui transfer în lista de transferuri, setările contabile ale unei categorii de produse propagate către subcategorii și controlul asupra cine poate modifica costul unui produs aflat în stoc. Utile pentru echipele de logistică și contabilitate, care văd imediat valoarea mărfii în mișcare și păstrează conturile coerente pe tot arborele de categorii.

#### 2. Funcționalități Cheie

- **Valoarea transferurilor:** coloana **Amount** în lista de transferuri (ex. *Inventar > Operațiuni > Transferuri > Recepții*), cu total la subsol; suma valorilor de evaluare ale mișcărilor de stoc ale transferului, iar mișcările neevaluate (ex. transferurile interne) contează zero. În livrări arată costul mărfii ieșite din stoc, nu prețul de vânzare. Valoarea apare doar în listă, nu pe formular.
- **Conturi propagate la subcategorii:** la modificarea **Stock Account** a unei categorii, setările ei (**Income Account**, **Expense Account**, **Stock Account**, **Price Difference Account**, **Stock Journal**, **Costing Method**, **Inventory Valuation**) se copiază la toate subcategoriile; copierea suprascrie setările lor, inclusiv valorile goale. Aceeași copiere se poate rula oricând cu acțiunea **Propagate Accounts** de pe formularul categoriei (mod dezvoltator). **Stock Variation Account** nu se propagă.
- **Setări moștenite de la categoria părinte:** la alegerea unei **Parent Category**, aceleași setări contabile se copiază de la părinte.
- **Modificarea costului restricționată:** doar utilizatorii din grupul **Change Product Price** pot schimba **Cost** pe un produs cu cantitate în stoc; ceilalți primesc o eroare de acces. Administratorul este în grup implicit; grupul se administrează în *Setări > Utilizatori și companii > Grupuri* (mod dezvoltator). Costul produselor fără stoc și actualizările automate (ex. costul mediu la recepție) nu sunt restricționate.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `product.category` (extins): propagarea setărilor contabile către subcategorii și preluarea lor de la părinte.
- `product.product` (extins): controlul modificării costului pe baza grupului.
- `stock.picking` (extins): suma valorilor de evaluare pe transfer.

**Vizualizări**

- `views/stock_picking_view.xml`: coloana **Amount** în lista de transferuri.
- `views/product_category_view.xml`: acțiunea **Propagate Accounts** pe categoria de produse.

**Acțiuni Automate / Acțiuni Server**

- `action_product_category_propagate`: acțiune server **Propagate Accounts**, rulată manual de pe formularul categoriei.
- Grupul `group_change_product_price` (**Change Product Price**), din `security/service_security.xml`.

#### 5. Conexiuni

- `stock_account`: modulul standard de evaluare a stocurilor, pe care această extensie îl completează cu valoarea la nivel de transfer și cu propagarea conturilor.
