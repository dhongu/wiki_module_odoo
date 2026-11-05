# Stock Report for Resellers (localizat la `deltatech_stock_reseller/index.md`)

- **Nume Tehnic:** `deltatech_stock_reseller`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_reseller
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_reseller`
- **Ultima Ingestie:** `2026-11-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un raport de stoc gândit pentru partenerii revânzători (reselleri). Pornind de la o locație de stoc aleasă, generează o listă a produselor disponibile, afișând atât prețul de catalog, cât și prețul de revânzare calculat pe baza unei liste de prețuri sau a unui partener. Pentru situațiile în care cantitatea exactă nu trebuie comunicată revânzătorului, raportul poate înlocui cifrele cu etichete text (de exemplu „Stoc limitat”, „În stoc”), pe baza unor praguri configurabile. Astfel, echipa de vânzări poate trimite rapid unui reseller o ofertă cu disponibilitate și prețuri adaptate fără a expune informații interne sensibile.

#### 2. Funcționalități Cheie

- Raport cu produsele dintr-o locație de stoc (doar cele cu cantitate liberă pozitivă), însoțit de prețuri.
- Alegerea locației de stoc pentru care se generează raportul (locații interne), din meniul **Vânzări > Raportare > Location Stock**.
- Alegerea unui partener (care propune lista lui de prețuri) sau direct a unei liste de prețuri pentru calculul prețului de revânzare. Fără listă de prețuri, prețul de revânzare apare în moneda companiei (corecție din 19.0.1.0.6).
- Două praguri configurabile pentru afișarea cantităților ca text (implicit 5 și 20), cu trei texte: sub primul prag, între praguri și peste al doilea prag (ex. Stoc redus, Stoc limitat, În stoc).
- Opțiunea „Refresh Report”: dacă e debifată, se refolosește un raport deja generat, dar numai dacă a fost creat cu aceeași locație, același partener, aceeași listă de prețuri și aceleași setări de praguri (corecție din 19.0.1.0.4).
- Rezultatul e o listă (cu variantă pivot) grupabilă pe produs sau categorie internă, cu cantitate sau text, preț de revânzare și preț de catalog.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

Readme-ul nu cere explicit detalierea componentelor; mai jos sunt cele verificate în cod.

**Modele**

- `stock.quant.report` (model tranzient): wizardul de configurare a raportului — locația sursă, partenerul/lista de prețuri pentru calculul prețului de revânzare, pragurile pentru afișarea cantităților ca text și opțiunea de reîmprospătare. Calculează liniile raportului și gestionează refolosirea rapoartelor existente.
- `stock.quant.report.value` (model tranzient): liniile rezultate ale raportului, fiecare reprezentând un produs cu cantitatea liberă, textul de cantitate, categoria, prețul de catalog și prețul de revânzare (cu monedele aferente).

**Vizualizări**

- `view_stock_quant_report_form`: formularul wizardului de generare a raportului.
- `view_stock_quant_report_value_tree`: lista cu rezultatele raportului (produse, cantități/text, prețuri).
- `view_stock_quant_report_report_filter`: căutare și grupare pe produs și categorie.
- `action_stock_quant_report` / `menu_stock_quant_report`: acțiunea și meniul „Location Stock”, sub Vânzări > Raportare.
- `action_stock_quant_report_value`: acțiunea care afișează rezultatele calculate (listă și pivot).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în modul.

#### 5. Conexiuni

- `sale_stock`: modul standard Odoo pe care se bazează raportul pentru integrarea vânzări–stoc.
- `product.pricelist`: listele de prețuri standard Odoo sunt folosite pentru calculul prețului de revânzare.
