# Template BoMs for Variants (localizat la `deltatech_mrp_bom/index.md`)

- **Nume Tehnic:** `deltatech_mrp_bom`
- **Versiune:** `19.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_bom
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_bom`
- **Ultima Ingestie:** `2026-11-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îmbunătățește gestionarea listelor de materiale (BoM) în Odoo printr-o abordare bazată pe șabloane pentru variantele de produs. Utilizatorul definește o listă de materiale „Bază" (Base), care se propagă automat către variantele specifice, ceea ce asigură consistența datelor și reduce configurarea manuală a structurilor de fabricație complexe.

#### 2. Funcționalități Cheie

- **Categorizare extinsă a listelor de materiale**: câmpul `Base Type` pe BoM, cu trei opțiuni:
  - `Normal`: comportamentul standard Odoo.
  - `Base`: șablon principal pentru un template de produs, care definește structura generală de componente.
  - `Derived`: BoM specializat pentru o variantă de produs, care moștenește și adaptează structura din BoM-ul `Base`.
- **Sincronizare automată a componentelor**: pentru BoM-urile `Derived`, butonul „Recompute Components" sincronizează componentele din BoM-ul `Base` al aceluiași template de produs; varianta corectă a fiecărei componente se găsește prin potrivirea atributelor dintre produsul principal și șablonul componentei.
- **Copierea rețetei din BoM-ul de bază**: BoM-ul derivat preia cantitatea și unitatea de măsură ale BoM-ului `Base` (nu mai este creat cu cantitatea 1, indiferent de randament), operațiunile (cu dependențele lor) și produsele secundare. Liniile, operațiunile și produsele secundare restricționate la alte variante nu se copiază, iar la recalculare operațiunile anterioare sunt arhivate, nu șterse, ca ordinele de lucru existente să nu rămână fără operațiune.
- **Integrare cu ordinele de fabricație**:
  - la alegerea unei variante de produs pe un ordin de fabricație se creează (dacă nu există) și se calculează automat un BoM `Derived` pornind de la BoM-ul `Base`;
  - butonul „Compute Derived BoM" de pe ordinul de fabricație (în starea ciornă) declanșează manual crearea și calculul BoM-ului derivat;
  - BoM-ul derivat primește automat o referință de forma `DX` (ex.: D1, D2), unde X este numărul versiunii de variantă pentru template-ul de produs;
  - înainte de confirmarea ordinului, BoM-ul `Derived` este recalculat, pentru ca variantele componentelor să respecte ultima configurație de atribute.
- **Navigare îmbunătățită**: pe liniile de BoM, un buton (eticheta „Show" în formular, vizibil doar dacă componenta are BoM propriu) deschide direct sub-lista de materiale a componentei, util la structuri pe mai multe niveluri.
- **Persistența atributelor**: valorile de atribute de pe liniile de BoM rămân sincronizate când se schimbă template-ul de produs principal.

> Notă: în Odoo Apps modulul apare sub numele „Template BoMs for Variants" (anterior „MRP Bom"); numele tehnic nu s-a schimbat.

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

Secțiunile Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md`, care nu cere explicit detalierea componentelor; mai jos sunt doar extinderile identificate la o privire rapidă în `models/` și `views/`.

**Modele**

- `mrp.bom` (extins): câmpul `base_type` (`Normal` / `Base` / `Derived`), recalcularea din BoM-ul de bază (`recompute_from_base`) și copierea rețetei (`_copy_recipe_from_base`).
- `mrp.bom.line` (extins): valorile de atribute ale liniei (`bom_product_template_attribute_value_ids`) și acțiunea `open_bom`.
- `mrp.production` (extins): câmpul `bom_base_type`, butonul `action_compute_derived_bom`, calculul BoM-ului derivat la schimbarea produsului și la `action_confirm`.

**Vizualizări**

- `mrp_bom_form_view`: extinde formularul BoM cu tipul bazei, butonul „Recompute Components" (vizibil doar pe BoM-uri `Derived`) și butonul de deschidere a sub-BoM-ului pe linii.
- `mrp_production_form_view`: extinde formularul ordinului de fabricație cu butonul „Compute Derived BoM".

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nicio conexiune către alte module documentate în wiki nu a fost confirmată în manifest sau în cod. Modulul extinde exclusiv modelele native ale `mrp` (fără pagină wiki proprie).
