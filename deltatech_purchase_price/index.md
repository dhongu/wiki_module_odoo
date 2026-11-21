# Purchase Price (localizat la `deltatech_purchase_price/index.md`)

- **Nume Tehnic:** `deltatech_purchase_price`
- **Versiune:** `19.0.1.2.16`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_price`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul actualizează automat prețurile de achiziție atunci când o recepție de marfă este validată. La fiecare recepție pe baza unei comenzi de achiziție, preia ultimul preț de achiziție și, în funcție de opțiunile configurate, poate actualiza prețul furnizorului, poate adăuga furnizorul în lista produsului și poate recalcula prețul de vânzare pe baza adaosului comercial. Astfel, datele de preț ale produselor rămân sincronizate cu realitatea aprovizionării, fără intervenție manuală.

#### 2. Funcționalități Cheie

Prețul de vânzare se calculează ca **ultimul preț de achiziție × (1 + adaos comercial / 100)**, fără taxe.

- **Opțiuni în Settings → Purchase, secțiunea Products** (parametri de sistem):
  - **Update product price** (`purchase.update_product_price`): la recepție, prețul furnizorului din tabul *Purchase* al produsului se înlocuiește cu prețul din comanda de achiziție (doar liniile de furnizor fără cantitate minimă peste 1 și fără perioadă de valabilitate);
  - **Update list price** (`purchase.update_list_price`): prețul de vânzare se recalculează din ultimul preț de achiziție și adaosul comercial — la recepție, la setarea adaosului pe mai multe produse și la modificarea adaosului sau a ultimului preț pe produs;
  - **Add supplier to product** (`purchase.add_supplier_to_product`): furnizorul și prețul se adaugă pe produs la confirmarea comenzii de achiziție;
  - **Force supplier price at PO and bill confirmation** (`purchase.force_price_at_validation`): prețul furnizorului se actualizează și la confirmarea comenzii și la postarea facturii de furnizor;
  - `purchase.update_standard_price`: dacă este True, costul standard este forțat la ultimul preț de achiziție (în cod este marcat ca nerecomandat; implicit costul vine din evaluarea stocului);
  - `sale.list_price_round`: numărul de zecimale la care se rotunjește prețul de vânzare calculat (implicit 2).
- **Câmpuri noi pe produs:** `last_purchase_price` (**Last Purchase Price**, actualizat la validarea recepției, convertit în moneda companiei și în unitatea de măsură a produsului; afișat verde când nu depășește costul, roșu când îl depășește) și `trade_markup` (**Trade Markup**, 30.00 înseamnă 30%).
- **Setare în masă a adaosului:** din listă, **Actions → Set Trade Markup**; cu **Selected Line** bifat se aplică produselor selectate, altfel se alege un **Vendor** și adaosul se aplică tuturor produselor lui.
- **Recepții fără comandă de achiziție** nu modifică prețurile.
- **Cu Update list price dezactivat**, prețul de vânzare se introduce manual, iar adaosul se recalculează din el (de exemplu preț de vânzare 13.00 și preț de achiziție 12.50 dau adaos 4.00); un adaos introdus manual se păstrează. Un produs fără adaos își păstrează prețul de vânzare.
- **Regulă de listă de prețuri:** **Last Purchase Price** poate fi folosit ca preț de bază.

Fluxul pas-cu-pas, cu exemple numerice, este în fișa consultant.

#### 3. Dependențe

- `stock`
- `stock_account`
- `purchase_stock`
- [deltatech_product_trade_markup](../deltatech_product_trade_markup/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template` / `product.product` (extinse): `last_purchase_price` și `trade_markup`, cu recalcularea adaosului și a prețului de vânzare.
- `stock.move` (extins): `update_prices()` este apelat la `_action_done` pentru mișcările de intrare cu linie de achiziție; actualizează `last_purchase_price`, prețul furnizorului, prețul de listă și, opțional, costul standard.
- `purchase.order` (extins): adaugă furnizorul pe produs la confirmare și, opțional, forțează prețul furnizorului.
- `account.move` (extins): forțează prețul furnizorului la postarea facturii, când parametrul `purchase.force_price_at_validation` este activ.
- `product.pricelist.item` (extins): bază nouă de calcul **Last Purchase Price**.
- `res.config.settings` (extins): opțiunile de mai sus în Settings → Purchase.
- Wizard `Set Trade Markup` (`TransientModel`): setarea adaosului pe produsele selectate sau pe cele ale unui furnizor.

**Vizualizări**

- `product_template_form_view`, `product_product_tree_view`, `product_variant_easy_edit_view`: afișează ultimul preț de achiziție și adaosul pe produs.
- `res_config_settings_view_form`: opțiunile de actualizare a prețurilor.
- `product_markup_wizard_form`: wizard-ul de setare a adaosului.

**Acțiuni Automate / Acțiuni Server**

- `action_product_template_markup_wizard`: acțiune de fereastră legată de produse (**Actions → Set Trade Markup**). Nu există cron-uri sau acțiuni server; logica rulează la validarea recepției.

#### 5. Conexiuni

- [deltatech_product_trade_markup](../deltatech_product_trade_markup/index.md): furnizează conceptul de adaos comercial folosit pentru calculul prețului de vânzare la recepție.
