# MRP Cost (localizat la `deltatech_mrp_cost/index.md`)

- **Nume Tehnic:** `deltatech_mrp_cost`
- **Versiune:** `20.0.2.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp_cost
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_cost`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite adăugarea de costuri suplimentare în comanda de producție, dincolo de costul materiilor prime consumate. Pe lângă valoarea materialelor, costul produsului finit poate include regie, consum de utilități, salarii nete și contribuții salariale, calculate în funcție de durata de producție. Astfel, prețul de cost al produsului fabricat reflectă mai fidel costul real, fiind util pentru o evaluare corectă a stocurilor și a marjelor.

#### 2. Funcționalități Cheie

- Adăugarea de costuri suplimentare (extra) în comanda de producție, peste costul materiilor prime.
- Definirea pe lista de materiale (BOM) a parametrilor de cost: regie, consum de utilități pe oră, rată salariu net, contribuții salariale și durată.
- Preluarea automată a acestor parametri din BOM în comanda de producție la crearea acesteia; durata se scalează după cantitatea comandată față de cantitatea din BOM.
- Calculul costurilor de manoperă și utilități proporțional cu durata de producție.
- Calculul automat al valorii totale a producției și al prețului de cost unitar al produsului fabricat; la finalizare, costul suplimentar este împărțit la cantitatea produsă și intră în costul produsului.

#### 3. Dependențe

- `mrp_account`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): adaugă câmpurile `overhead_amount` (regie), `utility_consumption` (consum utilități pe oră), `net_salary_rate` (rată salariu net), `salary_contributions` (contribuții salariale) și `duration_cost` (durată). Câmpurile calculate `amount` (valoarea producției) și `calculate_price` (prețul de cost unitar) însumează costul materialelor și costurile suplimentare. Metoda `_cal_price` injectează costul suplimentar (`extra_cost`) proporțional cu cantitatea produsă.
- `mrp.bom` (extins): adaugă câmpurile-șablon de cost `overhead_amount`, `duration`, `utility_consumption`, `net_salary_rate` și `salary_contributions`, valori implicite pentru comenzile generate din lista de materiale.

**Vizualizări**

- `bom_form_view`: extinde formularul listei de materiale (`mrp.bom`) cu parametrii de cost suplimentar.
- `mrp_production_form_view`: extinde formularul comenzii de producție (`mrp.production`) pentru afișarea costurilor suplimentare și a prețului de cost calculat.
- `report_mrporder`, `report_production_components`: extind rapoartele comenzii de producție (`mrp.report_mrporder`, `mrp.report_mrp_production_components`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): extinde și adaptează modulul de producție; ambele intervin asupra modelului `mrp.production`.
