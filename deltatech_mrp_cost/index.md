# MRP Cost (localizat la `deltatech_mrp_cost/index.md`)

- **Nume Tehnic:** `deltatech_mrp_cost`
- **Versiune:** `19.0.2.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_cost
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_cost`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul permite adăugarea de costuri suplimentare în comanda de producție, dincolo de costul materiilor prime consumate. Pe lângă valoarea materialelor, costul produsului finit poate include regie, consum de utilități, salarii nete și contribuții salariale, calculate în funcție de durata de producție. Astfel, prețul de cost calculat al produsului fabricat reflectă mai fidel costul real, fiind util pentru o evaluare corectă a stocurilor și a marjelor în activitatea de producție.

#### 2. Funcționalități Cheie

- Adăugarea de costuri suplimentare (extra) în comanda de producție, peste costul materiilor prime.
- Definirea pe lista de materiale (BOM) a parametrilor de cost: regie, consum de utilități, rată salariu net, contribuții salariale și durată.
- Preluarea automată a acestor parametri din BOM în comanda de producție la crearea acesteia.
- Calculul costurilor de manoperă și utilități proporțional cu durata estimată de producție.
- Calculul automat al valorii totale a producției și al prețului de cost unitar al produsului fabricat.

#### 3. Dependențe

- `mrp_account`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): adaugă câmpurile `overhead_amount` (regie), `utility_consumption` (consum utilități pe oră), `net_salary_rate` (rată salariu net), `salary_contributions` (contribuții salariale) și `duration_cost` (durată). Câmpurile calculate `amount` (valoarea producției) și `calculate_price` (prețul de cost unitar) însumează costul materialelor și costurile suplimentare. La creare, parametrii de cost se preiau din BOM, iar metoda `_cal_price` injectează costul suplimentar (`extra_cost`) proporțional cu cantitatea produsă.
- `mrp.bom` (extins): adaugă câmpurile-șablon de cost `overhead_amount`, `duration`, `utility_consumption`, `net_salary_rate` și `salary_contributions`, care servesc drept valori implicite pentru comenzile de producție generate din această listă de materiale.

**Vizualizări**

- `bom_form_view`: extinde formularul listei de materiale (`mrp.bom`) pentru a expune parametrii de cost suplimentar.
- `mrp_production_form_view`: extinde formularul comenzii de producție (`mrp.production`) pentru afișarea costurilor suplimentare și a prețului de cost calculat.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): extinde și adaptează modulul de producție; ambele intervin asupra modelului `mrp.production`.
