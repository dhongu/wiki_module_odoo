# Sale Return Cause (localizat la `deltatech_sale_return_cause/index.md`)

- **Nume Tehnic:** `deltatech_sale_return_cause`
- **Versiune:** `20.0.0.0.12`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_return_cause`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_return_cause`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă o modalitate sistematică de a urmări și analiza motivele retururilor din vânzări. Permite categorisirea retururilor, monitorizarea valorii returnate și raportarea, pentru a identifica problemele frecvente din procesul de vânzare sau de livrare.

#### 2. Funcționalități Cheie

- **Cauza returului** atribuită direct pe comanda de vânzare, dintr-un catalog configurabil (calitate, erori de livrare, greșeli ale clientului etc.). Catalogul se administrează din *Sales > Configuration > Return Causes*.
- **Calcul automat al valorii returnate:** suma notelor de credit postate din facturile comenzii (pentru comenzi cu cel puțin două facturi). Parametrul `deltatech_sale_return_cause.auto_calculate` (implicit activ) comută între calculul automat, când câmpul este readonly, și introducerea manuală.
- **Data returului** se înregistrează automat la prima atribuire a unei cauze; datele existente se păstrează.
- **Actualizare zilnică (cron)** a valorilor returnate pentru comenzile din ultimul an care au cauză de retur.
- **Raportare:** cauza, data returului și filtrul de căutare apar în *Sales Analysis*, utilizabile în vizualizările pivot și grafic; cauza apare și în lista comenzilor.
- Câmpul vechi de tip selecție `return_cause` (*Legacy*) este păstrat pentru compatibilitate.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.return.cause`: catalogul cauzelor de retur (nume traductibil, secvență, activ).
- `sale.order` (extins): `return_cause_id`, `return_cause` (legacy), `return_cause_date`, `return_amount` și logica de calcul din notele de credit.
- `sale.report` (extins): `return_cause_id`, `return_cause`, `return_cause_date` în analiza vânzărilor.

**Vizualizări**

- `view_sale_return_cause_tree` / `view_sale_return_cause_form`: catalogul de cauze (acțiunea `action_sale_return_cause`, meniul `menu_sale_return_cause`).
- `view_order_form` și `view_order_tree` (`sale.order`): cauza și valoarea returului pe formular, cauza în listă.
- `view_order_product_search` (`sale.report`): căutare după cauza returului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_check_and_update_return_amount`: cron zilnic, apelează `_cron_check_and_update_return_amount()`; nu face nimic dacă auto-calculul e dezactivat.
- `param_auto_calculate_return_amount`: parametru de configurare (`deltatech_sale_return_cause.auto_calculate`).

#### 5. Conexiuni

- `sale`: comenzile de vânzare și Sales Analysis, extinse cu urmărirea cauzelor de retur.
