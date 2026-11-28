# Extensie Monedă Listă de Prețuri (localizat la `deltatech_pricelist/index.md`)

- **Nume Tehnic:** `deltatech_pricelist`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_pricelist
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite unei companii să păstreze **Prețul de vânzare** al produselor într-o altă monedă decât cea contabilă, de exemplu prețuri în EUR într-o companie care ține contabilitatea în RON. Comenzile de vânzare și listele de prețuri convertesc prețul în moneda proprie, la cursul zilei.

#### 2. Funcționalități Cheie

- Câmpul **Price List Currency** pe formularul companiei, sub **Moneda**: devine moneda prețului de vânzare pentru toate produsele companiei. Produsele partajate între companii folosesc moneda de listă a companiei principale.
- Conversie automată în liste de prețuri și comenzi de vânzare când moneda lor diferă, cu cursurile standard Odoo; la regulile de tip *Discount* și *Formula* calculul pornește de la prețul convertit, iar la *Fixed Price* sumele sunt deja în moneda listei.
- **Costul** produselor rămâne în moneda companiei.
- Oferta păstrează prețul calculat la adăugarea liniei, la cursul datei comenzii; facturile create fără comandă convertesc prețul în același mod.
- Configurare: *Setări > Utilizatori și companii > Companii*. Pentru prețuri în moneda companiei, setați aceeași monedă ca la **Moneda**.
- Limitări: setarea se aplică la nivel de companie, nu per produs; la instalare fiecare companie primește EUR, deci într-o companie cu altă monedă prețurile existente sunt citite ca sume în EUR până la schimbarea câmpului.
- Fluxul pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `base`
- `product`
- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company`: adaugă câmpul `price_currency_id` (Price List Currency), implicit EUR.
- `product.template`: moneda prețului de vânzare este calculată din moneda de listă a companiei (`_compute_currency_id`, `_compute_sql_currency_id`).

**Vizualizări**

- `views/res_company_view.xml`: adaugă câmpul pe formularul companiei.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_pricelist_bulk](../deltatech_pricelist_bulk/index.md): lucrează tot pe listele de prețuri, fără dependență declarată.
- [deltatech_pricelist_vat_cost](../deltatech_pricelist_vat_cost/index.md): modul înrudit pe prețurile din listă, fără dependență declarată.
