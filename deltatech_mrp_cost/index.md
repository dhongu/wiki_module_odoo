# MRP Cost (localizat la `deltatech_mrp_cost/index.md`)

- **Nume Tehnic:** `deltatech_mrp_cost`
- **Versiune:** `19.0.2.0.10`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_cost
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_cost`
- **Ultima Ingestie:** `2026-11-12`

#### 1. Sumar

Manopera, utilitățile și regia sunt costuri de producție pe care componentele nu le arată. Modulul le înregistrează pe lista de materiale și pe comanda de producție și le adaugă la costul comenzii. Astfel, prețul de cost al produsului fabricat reflectă mai fidel costul real, fiind util pentru o evaluare corectă a stocurilor și a marjelor în activitatea de producție.

#### 2. Funcționalități Cheie

- **Fila *Costs*:** pe lista de materiale și pe comanda de producție, o filă *Costs* conține *Overhead* (regie), *Utility consumption*, *Net Salary Rate*, *Salary Contributions* și o *Duration* în ore. O comandă nouă preia valorile din lista de materiale, scalând durata la cantitatea comenzii.
- **Costul comenzii:** regia este o sumă fixă; utilitățile, salariul net și contribuțiile sunt tarife înmulțite cu durata. *Production Amount* și *Calculate Price* arată costul total și cel unitar: componentele stocabile la preț standard plus aceste costuri sau, după producție, valoarea mișcărilor produselor finite.
- **Costul produsului finit:** înainte ca Odoo să evalueze produsul finit, modulul setează `extra_cost` al comenzii la costurile împărțite la cantitatea comenzii (dacă nu sunt zero), apoi rulează calculul standard.
- **Comanda tipărită:** raportul comenzii de producție adaugă data de start, valorile de cost nenule, un tabel *Finished Products* și coloanele *Effective Quantity*, *Price* și *Amount* pe componente.
- **Limitări:** modificările ulterioare ale listei de materiale nu ajung în comenzile existente, iar costurile introduse pe o comandă nouă sunt înlocuite la prima salvare cu cele din lista de materiale.

#### 3. Dependențe

- `mrp_account`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): adaugă câmpurile `overhead_amount` (regie), `utility_consumption` (consum utilități pe oră), `net_salary_rate` (rată salariu net), `salary_contributions` (contribuții salariale) și `duration_cost` (durată). Câmpurile calculate `amount` (valoarea producției) și `calculate_price` (prețul de cost unitar) însumează costul materialelor și costurile suplimentare. La creare, parametrii de cost se preiau din BOM, iar metoda `_cal_price` setează `extra_cost` proporțional cu cantitatea comenzii.
- `mrp.bom` (extins): adaugă câmpurile-șablon de cost `overhead_amount`, `duration`, `utility_consumption`, `net_salary_rate` și `salary_contributions`, care servesc drept valori implicite pentru comenzile de producție generate din această listă de materiale.

**Vizualizări**

- `bom_form_view`: extinde formularul listei de materiale (`mrp.bom`) pentru a expune parametrii de cost suplimentar.
- `mrp_production_form_view`: extinde formularul comenzii de producție (`mrp.production`) pentru afișarea costurilor suplimentare și a prețului de cost calculat.
- `views/mrp_production_templates.xml`: șablonul raportului comenzii de producție, cu valorile de cost, tabelul *Finished Products* și coloanele suplimentare pe componente.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): extinde și adaptează modulul de producție; ambele intervin asupra modelului `mrp.production`.
