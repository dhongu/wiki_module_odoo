# Template BoMs for Variants (localizat la `deltatech_mrp_bom/index.md`)

- **Nume Tehnic:** `deltatech_mrp_bom`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp_bom
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_bom`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îmbunătățește gestionarea listelor de materiale (BoM) printr-o abordare bazată pe șabloane pentru variantele de produs. Utilizatorul definește o structură „Base", care se propagă automat către variantele specifice, ceea ce asigură consistența datelor și reduce configurarea manuală a structurilor de fabricație complexe. În Odoo Apps modulul apare sub numele „Template BoMs for Variants" (fost „MRP Bom"); numele tehnic nu s-a schimbat.

#### 2. Funcționalități Cheie

- **Categorizare extinsă a BoM:** câmpul `Base Type` are trei valori:
  - `Normal`: comportamentul standard Odoo.
  - `Base`: șablon principal pentru un template de produs, cu structura generală de componente.
  - `Derived`: BoM specializate pentru variante, care moștenesc și adaptează structura unui BoM `Base`.
- **Sincronizare automată a componentelor:** pentru BoM-urile `Derived`, butonul „Recompute Components" sincronizează componentele din BoM-ul `Base` al aceluiași template; varianta corectă a fiecărei componente se află potrivind atributele produsului principal cu cele ale componentei.
- **Integrare cu ordinele de fabricație:**
  - la alegerea unei variante pe un ordin de fabricație se creează (dacă nu există) și se calculează un BoM `Derived` pornind de la `Base`;
  - butonul „Compute Derived BoM" (ordin în ciornă) declanșează manual crearea și calculul;
  - BoM-ul derivat primește automat o referință `DX` (ex. D1, D2), unde X e numărul versiunii de variantă pentru template;
  - înainte de confirmare, BoM-ul `Derived` se recalculează pentru a reflecta ultima configurație de atribute.
- **Copiere completă a structurii:** BoM-ul derivat preia cantitatea și unitatea de măsură ale bazei, operațiile (cu dependențele lor) și subprodusele; liniile, operațiile și subprodusele restricționate la alte variante nu se copiază. La recalculare, operațiile vechi se arhivează, ca ordinele existente să nu rămână fără operație.
- **Navigare:** buton „Open BoM" pe liniile de BoM, pentru acces direct la sub-lista de materiale a componentei (util la structuri pe mai multe niveluri).
- **Persistența atributelor:** valorile de atribute de pe liniile de BoM rămân sincronizate când se schimbă template-ul de produs principal.
- Fluxul pas-cu-pas și capturile sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.bom`: extins cu `Base Type` și recalcularea componentelor.
- `mrp.bom.line`: extins cu butonul „Open BoM" și sincronizarea atributelor.
- `mrp.production`: extins cu butonul „Compute Derived BoM" și recalcularea la confirmare.
- `report.mrp.report_bom_structure` (model abstract): extins în raportul de structură BoM.

**Vizualizări**

- `mrp_bom_form_view`: câmpul `Base Type` și butoanele pe formularul BoM.
- `mrp_production_form_view`: butonul „Compute Derived BoM" pe ordinul de fabricație.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `mrp`: modulul standard de producție, ale cărui modele (BoM, linii de BoM, ordine de fabricație) sunt extinse.
