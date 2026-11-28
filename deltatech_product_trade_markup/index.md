# Product trade markup (localizat la `deltatech_product_trade_markup/index.md`)

- **Nume Tehnic:** `deltatech_product_trade_markup`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_trade_markup
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_trade_markup`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Companiile care își stabilesc prețurile ca „cost plus un procent fix” au nevoie de un loc unde să păstreze acel procent pe fiecare produs. Modulul adaugă pe produse câmpul **Trade Markup** (adaos comercial). Acesta stochează doar procentul; nu calculează singur niciun preț.

#### 2. Funcționalități Cheie

- Câmp **Trade Markup** (procent) pe formularul de produs, în fila *General Information*, lângă *Sales Price* și *Cost*.
- Valoarea este comună tuturor variantelor produsului, iar modificările ei sunt urmărite în chatter-ul produsului.
- Fundament pentru modulul Terrabit `deltatech_purchase_price`, care recalculează prețul de vânzare pornind de la ultimul preț de achiziție și adaos și oferă un wizard de setare a adaosului pe mai multe produse deodată.
- Limitare: instalat singur, modulul nu modifică prețul de vânzare; adaosul este informativ până când un modul precum `deltatech_purchase_price` îl folosește.

#### 3. Dependențe

- `account`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpul `trade_markup` (Float, `tracking=True`) și metoda `set_inverse_trade_markup()` ca punct de extensie.
- `product.product` (extins): metoda `set_inverse_trade_markup()` ca punct de extensie la nivel de variantă.

**Vizualizări**

- `product_view.xml`: moștenește formularul de produs și inserează `trade_markup` lângă preț și cost.

**Acțiuni Automate / Acțiuni Server**

- Nu există sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_purchase_price](../deltatech_purchase_price/index.md): folosește câmpul `trade_markup` pentru recalcularea prețului de vânzare din ultimul preț de achiziție.
