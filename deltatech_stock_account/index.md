# Stock Account Extension (localizat la `deltatech_stock_account/index.md`)

- **Nume Tehnic:** `deltatech_stock_account`
- **Versiune:** `19.0.1.0.10`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_account
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_account`
- **Ultima Ingestie:** `2026-11-04`

#### 1. Sumar

Mici completări la evaluarea stocurilor din Odoo: valoarea fiecărui transfer afișată în lista de transferuri, setările contabile ale unei categorii de produse transmise subcategoriilor și controlul asupra cine poate schimba costul unui produs aflat în stoc. Echipele de logistică și contabilitate văd imediat valoarea bunurilor în mișcare, iar costurile nu pot fi modificate de oricine.

#### 2. Funcționalități Cheie

- **Valoarea transferurilor**: adaugă coloana **Amount** în lista de transferuri (de exemplu **Inventar → Operațiuni → Transferuri → Recepții**), cu total la subsol. Suma este totalul **Valorii** de evaluare a mișcărilor de stoc ale transferului; mișcările neevaluate (de exemplu transferurile interne) contează zero.
- **Conturi propagate către subcategorii**: când se schimbă **Stock Account** pe o categorie de produse, setările contabile ale categoriei se copiază în toate subcategoriile: **Income Account**, **Expense Account**, **Stock Account**, **Price Difference Account**, **Stock Journal**, **Costing Method** și **Inventory Valuation**. Aceeași copiere se poate rula oricând cu acțiunea **Propagate Accounts** de pe formularul categoriei (mod dezvoltator).
- **Setări moștenite de la categoria părinte**: la alegerea unei **Parent Category**, aceleași setări contabile se copiază de la părinte.
- **Modificarea costului restricționată**: doar utilizatorii din grupul **Change Product Price** pot schimba **Costul** unui produs care are cantitate în stoc; ceilalți primesc o eroare de acces. Administratorul e în grup implicit. Utilizatorii se adaugă în grup la **Setări → Utilizatori și companii → Grupuri** (mod dezvoltator).
- Limitări: valoarea transferului apare doar în lista de transferuri, nu și pe formularul transferului; **Stock Variation Account** al categoriei nu se propagă.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie au fost preluate din `readme/DESCRIPTION.md`, care descrie și configurarea; componentele de mai jos sunt reperele confirmate în cod.

**Modele**

- `stock.picking` (extins): câmpul calculat `amount` (monetar), suma valorii de evaluare a mișcărilor transferului.
- `stock.move` (extins): moștenire goală, fără câmpuri sau metode.
- `product.category` (extins): propagarea conturilor către descendenți (`propagate_account`, declanșată la scrierea `property_stock_valuation_account_id`) și copierea setărilor de la părinte la schimbarea `parent_id`.
- `product.product` (extins): `_change_standard_price` ridică `AccessError` dacă produsul are cantitate în stoc, iar utilizatorul nu e în grupul `group_change_product_price`.

**Vizualizări**

- `vpicktree` (`stock.picking.tree`): moștenește lista de transferuri și adaugă coloana **Amount**.
- `action_product_category_propagate`: acțiune server „Propagate Accounts” pe categoria de produse, vizibilă doar în modul dezvoltator.

**Acțiuni Automate / Acțiuni Server**

- `action_product_category_propagate` („Propagate Accounts”): copiază setările contabile ale categoriei în subcategorii, la cerere; nu există cron-uri.

#### 5. Conexiuni

- `stock_account`: modulul standard Odoo de evaluare a stocurilor, pe care această extensie îl completează cu valoarea la nivel de transfer, propagarea conturilor și controlul costului.
