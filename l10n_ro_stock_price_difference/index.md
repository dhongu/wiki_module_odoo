# Romania - Stock Accounting Price Difference

- **Nume Tehnic:** `l10n_ro_stock_price_difference`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock_price_difference
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_stock_price_difference`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul gestionează diferențele de preț dintre facturi și recepții. La postarea facturii creează automat un cost suplimentar (landed cost) cu produsul „Price Difference” definit în configurare, astfel încât valoarea stocului să reflecte prețul facturat. Se aplică doar produselor evaluate FIFO.

#### 2. Funcționalități Cheie

- Detectarea diferențelor de preț între factura de achiziție și recepție la postarea facturii.
- Generarea automată a unui landed cost cu produsul „Price Difference”, creat sau preluat din configurare.
- Dialog de confirmare a diferențelor de preț înainte de postare.
- La recepțiile pe aviz, diferența se calculează din reziduul rămas pe contul pivot 408 după recunoașterea diferenței de curs valutar, nu prin compararea valorii facturii cu valoarea stocului. Diferența de curs nu mai este capitalizată în stoc (corecție introdusă în 19.0.1.0.0). Calculul este analitic, deci disponibil înainte de postare și corect la facturarea parțială.

#### 3. Dependențe

- `l10n_ro_stock_account_landed_cost`
- `stock_landed_costs`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): la `action_post` calculează diferențele de preț și deschide dialogul de confirmare.
- `account.move.line` (extins, cu `l10n.ro.mixin`): calculul diferenței de valoare de stoc și crearea landed cost-ului de diferență de preț.
- `stock.landed.cost` (extins): aplicare doar pe liniile distribuite și generarea notelor contabile.
- `l10n_ro.price_difference_confirm_dialog` și `l10n_ro.price_difference_item`: wizard-ul de confirmare și liniile sale.

**Vizualizări**

- `view_price_difference_confirmation_form`: formularul dialogului de confirmare.

**Acțiuni Automate / Acțiuni Server**

- `action_price_difference_confirmation`: acțiune de fereastră pentru dialogul de confirmare.

#### 5. Conexiuni

- `l10n_ro_stock_account_landed_cost`: furnizează mecanismul de landed cost pe care îl folosește modulul.
