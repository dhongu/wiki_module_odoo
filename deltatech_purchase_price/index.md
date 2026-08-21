# Purchase Price (localizat la `deltatech_purchase_price/index.md`)

- **Nume Tehnic:** `deltatech_purchase_price`
- **Versiune:** `19.0.1.2.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_price`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul actualizează automat prețurile de achiziție atunci când o recepție de marfă este validată. La fiecare recepție, modulul preia ultimul preț de achiziție și, în funcție de parametrii de sistem configurați, poate rescrie costul standard al produsului, prețul furnizorului, poate adăuga automat furnizorul în lista de furnizori ai produsului și poate recalcula prețul de vânzare pe baza adaosului comercial. Astfel, datele de preț ale produselor rămân mereu sincronizate cu realitatea aprovizionării, fără intervenție manuală.

#### 2. Funcționalități Cheie

- Actualizarea prețurilor după recepția mărfii, controlată prin parametri de sistem:
  - `purchase.update_standard_price` — dacă este setat pe True, costul standard (`standard_price`) al produsului este suprascris.
  - `purchase.update_product_price` — dacă este False, prețul furnizorului nu se modifică; dacă este True, prețul furnizorului produsului este întotdeauna suprascris.
  - `purchase.add_supplier_to_product` — dacă este True, furnizorul și prețul sunt adăugate automat în informațiile de furnizor ale produsului; dacă este False, nu se fac modificări în aceste informații.
  - `purchase.update_list_price` — dacă este True, prețul de listă este actualizat conform valorii adaosului comercial; dacă este False, prețul de listă nu se actualizează.
  - `sale.list_price_round` — numărul zecimal la care se rotunjește prețul de listă.
- Câmpuri noi adăugate pe șablonul de produs:
  - `last_purchase_price` — ultimul preț de achiziție, actualizat la validarea recepției.
  - `trade_markup` — adaosul comercial al produsului, care poate fi setat printr-un wizard (Acțiune → Set trade markup).
- Dacă adaosul comercial (`trade_markup`) este setat pentru un produs, la recepție prețul de vânzare se calculează automat din `last_purchase_price` și `trade_markup`.

> **Notă de ingestie:** codul modulului (versiunea `19.0.1.2.8`) conține și funcționalități care nu mai sunt descrise în `readme/DESCRIPTION.md` — vezi avertismentele din raportul de ingestie (parametru `purchase.force_price_at_validation`, tip nou de bază `last_purchase_price` pentru reguli de preț, calcul `last_purchase_price` pentru șabloane multi-variantă). Secțiunea de mai sus respectă strict conținutul readme-ului, conform fluxului de ingestie.

#### 3. Dependențe

- `stock`
- `stock_account`
- `purchase_stock`
- [deltatech_product_trade_markup](../deltatech_product_trade_markup/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template` / `product.product`: extinse cu câmpurile `last_purchase_price` (ultimul preț de achiziție, actualizat la recepție) și `trade_markup` (adaosul comercial al produsului).

**Vizualizări**

- Wizard de setare a adaosului comercial: accesibil prin meniul de acțiuni (Acțiune → Set trade markup) pentru actualizarea valorii `trade_markup` la nivel de produs.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau de server în acest modul; logica de actualizare a prețurilor se declanșează la validarea recepției și este guvernată de parametrii de sistem listați mai sus.

#### 5. Conexiuni

- [deltatech_product_trade_markup](../deltatech_product_trade_markup/index.md): furnizează conceptul de adaos comercial pe care acest modul îl folosește pentru a calcula prețul de vânzare la recepție.
