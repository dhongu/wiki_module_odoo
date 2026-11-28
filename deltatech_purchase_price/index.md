# Purchase Price (localizat la `deltatech_purchase_price/index.md`)

- **Nume Tehnic:** `deltatech_purchase_price`
- **Versiune:** `20.0.1.2.14`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_price`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul actualizează prețurile după validarea recepției: păstrează ultimul preț de achiziție, poate actualiza prețul furnizorului și poate recalcula prețul de vânzare pornind de la adaosul comercial. Datele de preț ale produselor rămân astfel sincronizate cu aprovizionarea reală, fără intervenție manuală.

#### 2. Funcționalități Cheie

- Prețul de vânzare = **ultimul preț de achiziție × (1 + adaos comercial / 100)**, fără taxe.
- Opțiuni în **Setări → Achiziții**, secțiunea Produse: *Update product price* (prețul furnizorului din fila Achiziții e înlocuit la recepție), *Update list price* (recalcul al prețului de vânzare la recepție, la aplicarea adaosului pe mai multe produse și la schimbarea adaosului sau a ultimului preț), *Add supplier to product* (furnizorul și prețul se adaugă la confirmarea comenzii) și *Force supplier price at PO and bill confirmation* (prețul furnizorului se actualizează și la confirmarea comenzii și la postarea facturii).
- Câmpuri noi pe produs: `last_purchase_price` (actualizat la validarea recepției, convertit în moneda companiei și în UM-ul produsului; recepțiile fără comandă nu schimbă prețurile) și `trade_markup` (adaos comercial).
- Adaosul se poate seta pe mai multe produse din **Actions → Set Trade Markup**: pe liniile selectate sau pe toate produsele unui furnizor.
- Cu *Update list price* dezactivat, adaosul este recalculat după prețul de vânzare; un adaos introdus manual se păstrează.
- Rotunjirea prețului se face prin parametrul `sale.list_price_round`; o regulă de listă de prețuri poate folosi ultimul preț de achiziție ca bază.
- Costul produsului nu este modificat de modul, el provine din evaluarea stocului. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `stock`
- `stock_account`
- `purchase_stock`
- [deltatech_product_trade_markup](../deltatech_product_trade_markup/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template`, `product.product`: `last_purchase_price` și `trade_markup`.
- `purchase.order`, `purchase.order.line`: actualizarea prețului furnizorului la confirmare.
- `stock.move`: actualizarea prețurilor la validarea recepției.
- `product.supplierinfo`: prețul furnizorului.
- `account.move`: actualizarea prețului furnizorului la postarea facturii.
- `product.pricelist.item`: ultimul preț de achiziție ca bază de preț.
- `res.config.settings`: opțiunile de actualizare a prețurilor.
- wizard `trade_markup_view.xml`: setarea adaosului pe mai multe produse.

**Vizualizări**

- `product_template_form_view`, `product_product_tree_view`: câmpurile de preț și adaos pe produs.
- `res_config_settings_view_form`: opțiunile din Setări.

#### 5. Conexiuni

- [deltatech_product_trade_markup](../deltatech_product_trade_markup/index.md): oferă calculul adaosului comercial pe care modulul îl aplică la recepție.
