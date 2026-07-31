# MRP Bom (localizat la `deltatech_mrp_bom/index.md`)

- **Nume Tehnic:** `deltatech_mrp_bom`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_bom
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_bom`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Deltatech MRP Bom îmbunătățește gestionarea Listelor de Materiale (BoM) în Odoo printr-o abordare bazată pe șabloane pentru variantele de produs. Modulul simplifică crearea și întreținerea structurilor de fabricație complexe, permițând definirea unei liste de materiale „Bază" (Base) care se propagă automat către variantele specifice, asigurând consistența datelor și reducând configurarea manuală.

#### 2. Funcționalități Cheie

- **Categorizare extinsă a Listelor de Materiale (BoM)**: adaugă un câmp `Base Type` (Tip Bază) pe BoM, cu trei opțiuni:
  - `Normal`: comportamentul standard Odoo pentru BoM.
  - `Base`: acționează ca șablon principal pentru un template de produs, definind structura generală de componente.
  - `Derived`: BoM specializate pentru variante specifice de produs, care moștenesc și adaptează structura dintr-un BoM `Base`.
- **Sincronizare automată a componentelor**: pentru BoM-urile marcate `Derived`, butonul „Recompute Components" sincronizează componentele din BoM-ul `Base` al aceluiași template de produs; sistemul identifică automat varianta corectă pentru fiecare componentă, potrivind atributele între produsul principal și cel al componentei.
- **Integrare cu Ordinele de Fabricație**:
  - la selectarea unei variante de produs pe un Ordin de Fabricație, se declanșează automat crearea (dacă nu există) și calculul unui BoM `Derived` pornind de la BoM-ul `Base`.
  - butonul „Compute Derived BoM" pe Ordinul de Fabricație (în starea ciornă) permite declanșarea manuală a creării și calculului BoM-ului derivat.
  - BoM-ul derivat primește automat o referință (cod) în formatul `DX` (ex: D1, D2), unde X reprezintă numărul versiunii de variantă pentru template-ul de produs.
  - înainte de confirmarea unui Ordin de Fabricație, sistemul recalculează BoM-ul `Derived` pentru a se asigura că toate variantele de componente sunt corect selectate conform ultimei configurații de atribute.
- **Navigare îmbunătățită**: adaugă un buton „Open BoM" direct pe liniile de BoM, oferind acces instant la sub-lista de materiale a oricărei componente, util în special pentru structuri de fabricație complexe, pe mai multe niveluri.
- **Persistența atributelor**: asigură că valorile de atribute de pe liniile de BoM rămân sincronizate atunci când templateul de produs principal este schimbat, menținând integritatea datelor la actualizările de configurație.

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de mai sus (Sumar și Funcționalități Cheie) sunt preluate din `readme/DESCRIPTION.md`, iar acesta nu solicită explicit detalierea Componentelor Cheie (Modele, Vizualizări, Acțiuni Automate). În consecință, analiza dedicată a codului pentru această secțiune a fost omisă intenționat.

Notă: din `readme/DESCRIPTION.md` reies, ca elemente tehnice menționate explicit, extinderile modelelor standard `mrp.bom` (câmpul `Base Type`, butonul de recalculare) și `mrp.bom.line` (butonul „Open BoM"), precum și integrarea pe `mrp.production` (butonul „Compute Derived BoM" și recalcularea la confirmare).

#### 5. Conexiuni

Nicio conexiune către alte module documentate în wiki nu a fost confirmată în manifest sau în cod. Modulul extinde exclusiv modelele native ale `mrp` (fără pagină wiki proprie în acest monorepo).
