# Sale Cost on Order (localizat la `deltatech_sale_cost_product/index.md`)

- **Nume Tehnic:** `deltatech_sale_cost_product`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_cost_product
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_cost_product`
- **Ultima Ingestie:** `2026-11-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul oferă managerilor de vânzări și controllerilor vizibilitate asupra costului mărfurilor din comenzile de vânzare. Costul comenzii se calculează în momentul confirmării, din prețul de cost al produselor, se păstrează pe comandă și apare ca o coloană în listele de comenzi și cotații, cu total pe grup. Costul este vizibil doar utilizatorilor din grupul dedicat, ceilalți vânzători neputându-l citi.

#### 2. Funcționalități Cheie

- **Costul mărfurilor pe comandă**: la trecerea comenzii în starea „Comandă de vânzare” se calculează suma (cost produs × cantitate) pentru fiecare linie, cu costul convertit în unitatea de măsură a liniei și în moneda comenzii, citit în compania comenzii. Cotațiile neconfirmate au costul 0.
- **Coloană în liste**: coloana opțională **Costul mărfurilor** (afișată implicit, îngroșată) în listele de **Vânzări → Comenzi → Comenzi** și **Cotații**, cu total la subsol (**Total Cost of Goods**).
- **Securitate**: câmpul este restricționat grupului **Poate vedea costul mărfurilor** (`Can See Cost Of Goods`); utilizatorii din afara grupului nu îl pot citi nici prin export sau RPC.
- **Duplicare fără eroare de acces**: costul nu se copiază la duplicarea comenzii, deci și un vânzător fără grupul de cost poate duplica o comandă.
- **Recalculare în masă**: acțiunea de server **Calculează costul mărfurilor** (doar administratori) recalculează costul tuturor comenzilor confirmate, cu prețurile de cost de la momentul rulării; utilă la instalare sau după schimbarea prețurilor de cost. Costul nu se actualizează singur după confirmare.
- Este un cost de management (câmpul **Cost** al produsului), nu o evaluare contabilă a stocului; modulul nu generează note contabile.

#### 3. Dependențe

- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `sale.order`: model extins cu câmpul `cost_of_goods` (monetar, `copy=False`, restricționat grupului `group_view_cost_on_sale`); costul se calculează la confirmare (`_update_cost_of_goods`) sau prin `calculate_cost_of_goods_for_confirmed_orders`.

**Vizualizări**

- `view_order_list_inherit`: extinde lista comenzilor de vânzare cu coloana **Total Cost of Goods**, vizibilă doar pentru grupul dedicat.
- `view_quotation_list_inherit`: aceeași coloană în lista de cotații.

**Acțiuni Automate / Acțiuni Server**

- `action_calculate_cost_of_goods` (Calculate Cost of Goods): acțiune server pe `sale.order`, rezervată grupului de administrare (`base.group_system`), care apelează `calculate_cost_of_goods_for_confirmed_orders()`.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale verificate către alte module documentate în wiki.
