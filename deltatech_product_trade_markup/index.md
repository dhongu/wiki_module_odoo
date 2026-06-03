# Product trade markup (localizat la `deltatech_product_trade_markup/index.md`)

- **Nume Tehnic:** `deltatech_product_trade_markup`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_trade_markup
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_trade_markup`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul introduce un mecanism de stabilire a prețurilor pentru produsele Odoo bazat pe un procent de adaos comercial (trade markup). Este conceput pentru a ajuta companiile să mențină marje de profit consecvente, prin calcularea prețului de vânzare pornind de la un cost de bază sau de la prețul de achiziție. Prin standardizarea logicii de adaos pe întreg catalogul de produse, reduce riscul erorilor de tarifare manuală.

#### 2. Funcționalități Cheie

- **Calcul al prețului de vânzare pe baza costului**: adaugă un câmp **Trade Markup Percent** (procent de adaos comercial) pe formularul de șablon și de variantă de produs și permite calcularea **prețului de listă** (preț de vânzare) pe baza costului produsului și a adaosului definit.
- **Fundament flexibil**: permite alegerea între diferite prețuri de bază pentru calculul adaosului (ex.: preț de cost sau ultimul preț de achiziție) și gestionează actualizările de preț dinamic, atunci când se modifică prețul de cost sau procentul de adaos.
- **Monitorizarea consecvenței**: asigură că prețurile de vânzare din catalog respectă o logică standardizată de adaos, reducând riscul erorilor de tarifare manuală.

> Notă de implementare: în versiunea curentă (19.0.1.0.1) codul adaugă câmpul `trade_markup` pe produs (cu urmărire/tracking), iar metodele de recalculare a prețului sunt definite ca puncte de extensie (stub `pass`), pregătite pentru personalizare per client. Comportamentul automat de calcul descris mai sus reprezintă scopul funcțional al modulului.

#### 3. Dependențe

- `account`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpul `trade_markup` (Float, cu `tracking=True`) — procentul de adaos comercial la nivel de șablon de produs. Expune metoda `set_inverse_trade_markup()` ca punct de extensie.
- `product.product` (extins): expune metoda `set_inverse_trade_markup()` ca punct de extensie la nivel de variantă.

**Vizualizări**

- `product_template_form_view`: moștenește `product.product_template_form_view` și inserează câmpul `trade_markup` în grupul `group_standard_price` (lângă prețul standard / cost).

**Acțiuni Automate / Acțiuni Server**

- Nu există sarcini `ir.cron`, reguli `base.automation` sau acțiuni server definite în modul.

#### 5. Conexiuni

- `product`: modulul extinde direct `product.template` și `product.product` pentru a adăuga adaosul comercial.
- `account`: dependență de manifest, pentru contextul de prețuri și contabilitate al produsului.
