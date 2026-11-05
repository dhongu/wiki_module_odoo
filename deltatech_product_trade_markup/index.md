# Product trade markup (localizat la `deltatech_product_trade_markup/index.md`)

- **Nume Tehnic:** `deltatech_product_trade_markup`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_trade_markup
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_trade_markup`
- **Ultima Ingestie:** `2026-11-05`

#### 1. Sumar

Companiile care stabilesc prețul ca cost plus un procent fix au nevoie de un loc unde să păstreze acel procent pentru fiecare produs. Modulul adaugă pe produs câmpul **Trade Markup** (adaos comercial). Stochează doar procentul și nu calculează niciun preț singur; calculul este făcut de alte module care folosesc câmpul.

#### 2. Funcționalități Cheie

- **Câmpul Trade Markup** (procent) pe formularul produsului, în fila *General Information*, lângă *Sales Price* și *Cost*. Este comun tuturor variantelor produsului, iar modificările lui sunt înregistrate în chatter-ul produsului.
- **Bază pentru alte module**: câmpul este folosit de modulul Terrabit [deltatech_purchase_price](../deltatech_purchase_price/index.md), care recalculează prețul de vânzare din ultimul preț de achiziție și din adaos și oferă un wizard pentru setarea adaosului pe mai multe produse deodată. Acel modul se instalează dacă prețul de vânzare trebuie să urmeze automat adaosul.
- **Limitare**: instalat singur, modulul nu modifică prețul de vânzare; adaosul este doar informativ până când un modul precum `deltatech_purchase_price` îl folosește.

#### 3. Dependențe

- `account`
- `product`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; analiza codului pentru această secțiune a fost totuși făcută punctual, fiindcă pagina anterioară o descria diferit.

**Modele**

- `product.template` (extins): adaugă câmpul `trade_markup` (Float, `tracking=True`) și metoda `set_inverse_trade_markup()`, definită gol (`pass`) ca punct de extensie.
- `product.product` (extins): expune `set_inverse_trade_markup()` ca punct de extensie la nivel de variantă (tot `pass`).

**Vizualizări**

- `product_template_form_view` (`views/product_view.xml`): moștenește `product.product_template_form_view` și inserează câmpul `trade_markup` în grupul `group_standard_price`.

**Acțiuni Automate / Acțiuni Server**

- Nu există sarcini `ir.cron`, reguli `base.automation` sau acțiuni server definite în modul.

#### 5. Conexiuni

- [deltatech_purchase_price](../deltatech_purchase_price/index.md): folosește câmpul `trade_markup` pentru a recalcula prețul de vânzare din ultimul preț de achiziție.
