# Website Cost Price Protection (localizat la `deltatech_website_sale_cost_price/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_cost_price`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_sale_cost_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_cost_price`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde opțiunea standard Odoo „Prevent Sale of Zero Priced Product” din magazinul online, astfel încât să blocheze și vânzarea produselor al căror preț este mai mic decât costul lor plus o marjă minimă. Pentru un astfel de produs clientul nu mai vede prețul și butonul **Add to Cart**, ci butonul **Contact Us** (ca la produsele cu preț zero), iar butonul de coș dispare din lista de produse. Astfel, comerciantul este protejat de vânzarea sub cost pe website.

#### 2. Funcționalități Cheie

- **Protecție la preț sub cost**: prețul de pe website (după lista de prețuri a website-ului) este comparat cu costul produsului (câmpul **Cost**).
- **Marjă minimă**: procent setat pe website (cu 10%, prețul trebuie să fie cel puțin 110% din cost).
- **Comparație cu/fără taxe**: costul (ținut fără taxe) este majorat cu taxele atunci când website-ul afișează prețuri cu taxe; opțiunea **Cost Price Includes Tax** se lasă debifată când costul e ținut fără taxe.
- **Conversie valutară**: costul este convertit în moneda website-ului.
- **Setări**: *Website > Configuration > Settings*, secțiunea **eCommerce**; câmpurile apar după bifarea **Prevent Sale of Zero Priced Product**.
- Utilizatorii din grupul *Settings* pot totuși adăuga în coș un produs blocat, de aceea verificarea se face ca vizitator.
- Fluxul pas cu pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `website_sale`
- `stock_account`

#### 4. Componente Cheie

**Modele**

- `product.template` (extindere): adaugă `_get_cost_price_for_comparison()` — calculează pragul de cost (ajustat pentru TVA, monedă și marjă) folosit pentru comparație; suprascrie `_get_additional_combination_info()` pentru a seta `prevent_zero_price_sale` când prețul e sub cost, și `_website_show_quick_add()` pentru a ascunde butonul "Adăugare rapidă" în același caz.
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
