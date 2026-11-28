# eCommerce - Cantitate maximă pe comandă (Max Order Quantity)

- **Nume Tehnic:** `deltatech_sale_max_qty_website`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sale_max_qty_website
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_max_qty_website`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul limitează câte unități dintr-un produs se pot cumpăra într-o singură comandă din magazinul online. Limita se setează pe produs sau, ca valoare implicită, pe categoria de eCommerce, iar clientul este oprit politicos în pagina produsului, în coș și la plată. Opțional, aceeași limită se poate aplica și comenzilor introduse de utilizatorii interni.

#### 2. Funcționalități Cheie

- **Pe produs:** câmpul *Cantitate maximă pe comandă* din fila *Vânzări* a produsului (0 = fără limită), în unitatea de măsură a produsului și pentru toate variantele împreună.
- **Pe categorie eCommerce:** limită implicită pentru produsele categoriei (și ale subcategoriilor) care nu au limită proprie; dacă produsul are mai multe categorii se folosește cea mai mică, iar limita de pe produs are întotdeauna prioritate.
- **Pagina produsului:** limita apare sub *Adaugă în coș*, iar butonul + se oprește la maxim; dacă se trimite totuși o cantitate mai mare, se adaugă doar ce mai încape, ținând cont de ce e deja în coș.
- **Coșul:** butonul + se oprește la maxim, o cantitate mai mare introdusă manual este redusă automat cu un avertisment; liniile în alte unități de măsură sunt convertite înainte de verificare.
- **Finalizarea comenzii:** dacă limita este scăzută după ce clientul și-a umplut coșul, plata rămâne blocată până la reducerea cantității (blocare și pe server).
- **Backend (opțional):** în *Website > Configurare > Setări*, bifa *Cantitate maximă pe comandă în backend* aplică limita și comenzilor introduse de utilizatorii interni, cu excepția grupului *Poate depăși cantitatea maximă pe comandă* (implicit managerii de vânzări).
- Cantitatea este verificată întotdeauna pe server. Modul cu plată pe Odoo Apps (10 EUR, licență OPL-1, stadiu Alpha). Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): `max_order_qty`, limita pe produs.
- `product.public.category` (extins): `max_order_qty`, limita implicită pe categorie.
- `sale.order` / `sale.order.line` (extinse): verificarea limitei la coș, la plată și, opțional, în backend.
- `res.config.settings` (extins): `max_order_qty_backend`, aplicarea limitei în backend.

**Vizualizări**

- `product_template_view.xml`: grupul *Limită comandă* în fila Vânzări a produsului.
- `product_public_category_view.xml`: câmpul limită pe categoria de eCommerce.
- `res_config_settings_view.xml`: setarea pentru backend.
- `templates.xml`: mesajele de pe pagina produsului și din coș.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Grupul de securitate *Poate depăși cantitatea maximă pe comandă* este definit în `security/security.xml`.

#### 5. Conexiuni

- Nu există conexiuni cu alte module cu pagină wiki.
