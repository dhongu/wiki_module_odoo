# Sale Cost on Order (localizat la `deltatech_sale_cost_product/index.md`)

- **Nume Tehnic:** `deltatech_sale_cost_product`
- **Versiune:** `20.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_cost_product
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_cost_product`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă managerilor de vânzări și controllerilor mai multă vizibilitate asupra profitabilității comenzilor. Costul mărfurilor este calculat pe comanda de vânzare din costul actual al produselor și afișat în listele de oferte și comenzi, doar pentru utilizatorii care au dreptul să-l vadă. Astfel se pot identifica rapid comenzile cu marjă mică sau vândute sub cost, fără a deschide produsele una câte una.

#### 2. Funcționalități Cheie

- Câmpul **Costul mărfurilor** (`cost_of_goods`) pe comanda de vânzare, calculat din costul produselor la confirmarea comenzii.
- Costul este adus în moneda comenzii și în unitatea de măsură a liniei, în compania comenzii.
- Coloana cu total în listele de oferte și de comenzi, în `Vânzări > Comenzi`, vizibilă doar grupului **Poate vedea costul mărfurilor**.
- Lucrează împreună cu modulul standard de marjă pentru a vedea marja pe linie și totalul comenzii și a filtra comenzile sub un anumit prag.
- Acțiunea server **Calculează costul mărfurilor** (doar administratori) recalculează în masă costul comenzilor confirmate.
- Informația este de analiză; nu generează înregistrări contabile.

#### 3. Dependențe

- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `sale.order`: câmpul `cost_of_goods` (restricționat pe grup), calculul `_get_cost_of_goods` și actualizarea la trecerea în starea `sale`.

**Vizualizări**

- `view_order_list_inherit`: coloana costului în lista de comenzi.
- `view_quotation_list_inherit`: coloana costului în lista de oferte.

**Acțiuni Automate / Acțiuni Server**

- `action_calculate_cost_of_goods`: acțiune server, doar pentru administratori, care recalculează costul pentru toate comenzile confirmate.

#### 5. Conexiuni

- `sale_margin`: modulul standard de marjă, folosit în paralel pentru analiza marjei pe comandă.
