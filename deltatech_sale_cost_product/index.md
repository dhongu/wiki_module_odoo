# Deltatech Sale Cost on Order (localizat la `deltatech_sale_cost_product/index.md`)

- **Nume Tehnic:** `deltatech_sale_cost_product`
- **Versiune:** `19.0.0.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_cost_product`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_cost_product`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă instrumente specializate pentru monitorizarea și analiza costurilor și a marjelor comenzilor de vânzare în Odoo. Este destinat managerilor de vânzări și controllerilor care au nevoie de o vizibilitate sporită asupra profitabilității tranzacțiilor, atât la nivel de comandă, cât și la nivel de linie de comandă. Modulul aduce costul de achiziție direct în comanda de vânzare, facilitând identificarea rapidă a comenzilor cu marjă redusă sau a produselor vândute sub cost.

#### 2. Funcționalități Cheie

- **Vizibilitate detaliată a costurilor**: adaugă un câmp dedicat **Cost de achiziție** direct pe liniile comenzii de vânzare și completează automat costul pe baza prețului de cost curent al produsului în momentul creării comenzii.
- **Analiză de marjă și ierarhie**: se integrează cu modulul standard de marjă din Odoo pentru o imagine mai clară a ierarhiei profitului între echipele de vânzări, ajutând la depistarea rapidă a comenzilor sau produselor cu marjă mică.
- **Raportare și acțiuni server fără cod**: include acțiuni server preconfigurate pentru recalcularea sau actualizarea în masă a costurilor pe mai multe comenzi de vânzare.
- **Model de securitate rafinat**: controlează ce utilizatori pot vizualiza sau modifica datele sensibile privind costul și marja, prin grupul de acces dedicat.

#### 3. Dependențe

- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `sale.order`: model extins pentru a adăuga costul bunurilor (`cost_of_goods`) la nivel de comandă și metoda de calcul al costului pentru comenzile confirmate (`calculate_cost_of_goods_for_confirmed_orders`).

**Vizualizări**

- `view_order_list_inherit`: extinde lista de comenzi de vânzare cu coloana **Total Cost of Goods**, vizibilă doar pentru grupul de acces dedicat.
- `view_quotation_list_inherit`: extinde lista de oferte (quotations) cu aceeași coloană de cost al bunurilor.

**Acțiuni Automate / Acțiuni Server**

- `action_calculate_cost_of_goods` (Calculate Cost of Goods): acțiune server legată de modelul `sale.order`, disponibilă utilizatorilor din grupul de sistem, care apelează `calculate_cost_of_goods_for_confirmed_orders()` pentru recalcularea costurilor comenzilor confirmate.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): modul complementar pentru analiza marjelor pe comenzile de vânzare.
