# Pricelist Currency Extension (localizat la `deltatech_pricelist/index.md`)

- **Nume Tehnic:** `deltatech_pricelist`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pricelist
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist`
- **Ultima Ingestie:** `2026-11-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite unei companii să păstreze **prețul de vânzare** al produselor într-o altă monedă decât moneda contabilă, de exemplu prețuri în EUR într-o companie care își ține contabilitatea în RON. Comenzile de vânzare și listele de prețuri convertesc prețul în propria monedă, la cursul zilei.

#### 2. Funcționalități Cheie

- **Moneda listei de prețuri pe companie**: câmpul **Price List Currency** pe formularul companiei, sub **Currency**. Moneda **Sales Price** a produselor devine această monedă pentru toate produsele companiei; produsele partajate între companii folosesc moneda listei de prețuri a companiei principale. Setarea este pe companie, nu pe produs.
- **Conversie în liste de prețuri și vânzări**: când lista de prețuri sau comanda de vânzare este în altă monedă, prețul de vânzare se convertește din moneda listei de prețuri, cu cursurile standard Odoo (ultimul curs până la data documentului). **Cost** rămâne în moneda companiei. O listă de prețuri în aceeași monedă cu prețul de vânzare nu îl convertește; la regulile **Discount** și **Formula** pornește de la prețul convertit, iar sumele **Fixed Price** sunt deja în moneda listei. Facturile client create fără comandă de vânzare convertesc prețul la fel.
- **Ofertă**: păstrează prețul calculat la adăugarea liniei, la cursul datei ofertei/comenzii; nu urmărește singură un curs ulterior.
- **Configurare**: **Settings > Users & Companies > Companies** → se setează **Price List Currency**; pentru a păstra prețurile în moneda companiei, se alege aceeași monedă ca la **Currency**. Moneda listei trebuie să aibă curs (**Invoicing > Configuration > Accounting > Currencies**, tab **Rates**).
- **Limitări**: setarea se aplică întregii companii (nu se poate alege pe produs); la instalare fiecare companie primește EUR ca **Price List Currency**, deci într-o companie cu altă monedă prețurile existente sunt citite ca sume în EUR până la schimbarea câmpului.

> Notă: în Odoo Apps modulul apare sub numele „Pricelist Currency Extension"; titlul paginii a fost aliniat la manifest. Fluxul pas cu pas este în fișa consultant.

#### 3. Dependențe

- `base`
- `product`
- `sale`

#### 4. Componente Cheie

Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md` și `readme/USAGE.md`; mai jos, o verificare punctuală a codului.

**Modele**

- `res.company` (extins): câmpul `price_currency_id` („Price List Currency"), cu EUR ca valoare implicită.
- `product.template` (extins): `_compute_currency_id` setează moneda produsului din moneda listei de prețuri a companiei produsului, sau a companiei principale.
- `product.pricelist.item` (extins): câmpul calculat `price_text`, definit în cod dar afișat doar de vizualizările din `oca_data_manual` (nu se încarcă la instalare).

**Vizualizări**

- `view_company_form`: adaugă câmpul „Price List Currency" pe formularul companiei (încărcată la instalare).
- `product_template_form_view`, `product_template_kanban_view`, `product_variant_easy_edit_view`, `product_pricelist_item_tree_view`, `product_pricelist_item_action`: declarate sub `oca_data_manual` în manifest, deci nu se încarcă automat la instalare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni suplimentare către alte module documentate în wiki, în afara dependențelor directe de mai sus.
