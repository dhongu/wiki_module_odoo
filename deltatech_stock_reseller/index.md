# Raport Stoc pentru Reselleri (localizat la `deltatech_stock_reseller/index.md`)

- **Nume Tehnic:** `deltatech_stock_reseller`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_reseller`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_reseller`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul oferă un raport de stoc gândit pentru partenerii revânzători (reselleri). Pornind de la o locație de stoc aleasă, generează o listă a produselor disponibile, afișând atât prețul de catalog, cât și prețul de revânzare calculat pe baza unei liste de prețuri sau a unui partener. Pentru situațiile în care cantitatea exactă nu trebuie comunicată revânzătorului, raportul poate înlocui cifrele cu etichete text (de exemplu „Stoc limitat", „În stoc"), pe baza unor praguri configurabile. Astfel, echipa de vânzări poate trimite rapid unui reseller o ofertă cu disponibilitate și prețuri adaptate fără a expune informații interne sensibile.

#### 2. Funcționalități Cheie

- Raport cu pozițiile dintr-o locație de stoc, însoțit de lista de prețuri.
- Alegerea locației de stoc pentru care se generează raportul.
- Alegerea unui partener sau a unei liste de prețuri pentru calculul prețului de revânzare.
- Două praguri configurabile pentru afișarea cantităților ca text (ex. Stoc redus, Stoc limitat, În stoc), fiecare cu textul aferent.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `stock.quant.report` (model tranzient): wizardul de configurare a raportului — locația sursă, partenerul/lista de prețuri pentru calculul prețului de revânzare și pragurile pentru afișarea cantităților ca text.
- `stock.quant.report.value` (model tranzient): liniile rezultate ale raportului, fiecare reprezentând un produs cu cantitatea disponibilă, categoria, prețul de catalog și prețul de revânzare.

**Vizualizări**

- `view_stock_quant_report_form`: formularul wizardului de generare a raportului.
- `view_stock_quant_report_value_tree`: lista cu rezultatele raportului (produse, cantități/text, prețuri).
- `view_stock_quant_report_report_filter`: filtrele de căutare pentru liniile raportului.
- `action_stock_quant_report` / `menu_stock_quant_report`: acțiunea și elementul de meniu pentru deschiderea raportului.
- `action_stock_quant_report_value`: acțiunea care afișează rezultatele calculate.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în modul.

#### 5. Conexiuni

- `sale_stock`: modul standard Odoo pe care se bazează raportul pentru integrarea vânzări–stoc.
- `product.pricelist`: listele de prețuri standard Odoo sunt folosite pentru calculul prețului de revânzare.
