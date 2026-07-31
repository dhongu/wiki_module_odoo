# Website Sale Cost Price (localizat la `deltatech_website_sale_cost_price/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_cost_price`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_cost_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_cost_price`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul extinde funcționalitatea standard Odoo "Previne Vânzarea Produselor cu Preț Zero" din magazinul online, astfel încât să blocheze și vânzarea produselor al căror preț este mai mic decât costul lor (prețul standard). Practic, protejează comercianții de vânzarea sub cost pe website, cu posibilitatea de a impune și o marjă minimă de profit configurabilă.

#### 2. Funcționalități Cheie

- **Prevenire dinamică a vânzării sub cost**: blochează automat adăugarea în coș a unui produs dacă prețul de vânzare este sub prețul de cost.
- **Marjă configurabilă**: se poate seta un procent minim de marjă în setările website-ului (ex: dacă e setat la 10%, prețul de vânzare trebuie să fie cel puțin 110% din costul produsului).
- **Comparație corectă cu/fără TVA**: se poate configura dacă prețul de cost include sau nu taxa, pentru o comparație corectă față de prețul afișat pe website.
- **Conversie valutară**: gestionează automat diferențele de monedă între moneda de cost a produsului și moneda listei de prețuri a website-ului.

#### 3. Dependențe

- `website_sale`
- `stock_account`

#### 4. Componente Cheie

**Modele**

- `product.template` (extindere): adaugă `_get_cost_price_for_comparison()` — calculează pragul de cost (ajustat pentru TVA, monedă și marjă) folosit pentru comparație; suprascrie `_get_additionnal_combination_info()` pentru a seta `prevent_zero_price_sale` când prețul e sub cost, și `_website_show_quick_add()` pentru a ascunde butonul "Adăugare rapidă" în același caz.
- `product.product` (extindere): suprascrie `_website_show_quick_add()` și `_is_add_to_cart_allowed()` — blochează adăugarea în coș dacă prețul e sub costul calculat, cu excepția utilizatorilor din grupul `base.group_system` (administratori).
- `website` (extindere): adaugă câmpurile `cost_price_include_tax` (Boolean) și `cost_price_margin_percentage` (Float).
- `res.config.settings` (extindere, tranzitoriu): expune câmpurile de mai sus (`related` pe `website_id`) în ecranul de configurare Website.

**Vizualizări**

- `views/res_config_settings_views.xml`: adaugă în secțiunea Website > Configurare > Setări, la "Shop - Checkout Process", câmpurile **Cost Price Includes Tax** și **Cost Price Margin Percentage**, vizibile când opțiunea standard "Prevent Sale of Zero Priced Product" este activă.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `website_sale`: modulul se bazează pe fluxul standard de e-commerce (coș, "Quick Add", combinare de preț) pe care îl extinde cu verificarea de cost.
- `stock_account`: folosește `standard_price` (prețul de cost contabil) al produsului ca prag de comparație.
