# Raport Stoc pentru Reselleri (localizat la `deltatech_stock_reseller/index.md`)

- **Nume Tehnic:** `deltatech_stock_reseller`
- **Versiune:** `20.0.1.0.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_reseller`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_reseller`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un raport de stoc gândit pentru partenerii revânzători (reselleri). Pornind de la o locație de stoc aleasă, generează lista produselor disponibile, cu prețul de listă și prețul de revânzare calculat din lista de prețuri a partenerului. Cantitățile pot fi înlocuite cu etichete de nivel de stoc (de exemplu „Stoc redus”, „Stoc limitat”, „Stoc”), astfel încât partenerul să primească informația de disponibilitate fără cifrele exacte.

#### 2. Funcționalități Cheie

- Raport cu pozițiile din stocul unei locații, cu prețuri din lista de prețuri.
- Alegerea locației sursă de stoc.
- Alegerea partenerului sau a listei de prețuri pentru calculul prețului de revânzare (fără listă, prețul de revânzare este egal cu prețul de listă).
- Două praguri configurabile pentru afișarea cantităților sub formă de text, fiecare cu textul propriu (sub primul prag, sub al doilea prag, peste al doilea prag).
- Acces din *Vânzări > Raportare > Stoc pe locație*; raportul listă doar cantitățile libere (fără cele rezervate), cu grupare pe categorie sau produs și vedere pivot.
- Liniile se pot exporta cu *Acțiuni > Export*; coloana cantitate se omite când partenerul trebuie să vadă doar textele de nivel de stoc.
- Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `stock.quant.report` (model tranzient): wizardul de configurare a raportului — locația sursă, partenerul/lista de prețuri și pragurile pentru textele de stoc.
- `stock.quant.report.value` (model tranzient): liniile raportului, cu produsul, cantitatea, categoria, prețul de listă și prețul de revânzare.

**Vizualizări**

- Formularul wizardului `stock.quant.report` și lista/filtrele liniilor raportului, definite în `wizard/stock_quant_report_view.xml`, cu acțiunea și meniul de deschidere.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `sale_stock`: integrarea vânzări–stoc pe care se bazează raportul.
- `product.pricelist`: listele de prețuri standard sunt folosite pentru prețul de revânzare.
