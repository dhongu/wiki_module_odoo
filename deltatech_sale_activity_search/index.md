# Sale Order activity type search (localizat la `deltatech_sale_activity_search/index.md`)

- **Nume Tehnic:** `deltatech_sale_activity_search`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_activity_search
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_activity_search`
- **Ultima Ingestie:** `2026-11-10`

#### 1. Sumar

Modulul păstrează pe fiecare comandă de vânzare un câmp text cu tipurile activităților sale în așteptare, astfel încât comenzile să poată fi găsite după felul de follow-up pe care îl așteaptă (de exemplu „Apel", „E-mail" sau un tip de activitate personalizat). Este util echipelor de vânzări și managerilor care vor să identifice rapid comenzile ce necesită atenție.

#### 2. Funcționalități Cheie

- **Câmpul stocat „Active Activity Types":** conține, separate prin virgulă, numele tipurilor activităților deschise ale comenzii.
- **Actualizare automată:** câmpul se reîmprospătează la programarea unei activități pe comandă, la modificarea ei (inclusiv în masă), la mutarea pe altă comandă sau alt document, la marcarea ca efectuată sau la anulare.
- **Căutare după tipul activității:** fiind stocat, câmpul se folosește într-un filtru personalizat: în **Vânzări > Comenzi > Oferte** sau **Vânzări > Comenzi > Comenzi**, din meniul de filtre alegeți **Adaugă filtru personalizat** și construiți o condiție pe „Active Activity Types" (ex. *conține* „Call").
- **Limitări:**
  - modulul nu adaugă vizualizări, filtre sau coloane; câmpul e accesibil doar prin filtru personalizat, grupare personalizată sau export;
  - câmpul se completează doar pentru activitățile create, modificate sau șterse după instalare; comenzile cu activități programate înainte rămân goale până la prima modificare a unei activități.

#### 3. Dependențe

- `sale`
- `mail`

#### 4. Componente Cheie

*Secțiune omisă conform fluxului de ingestie: `readme/DESCRIPTION.md` nu menționează explicit componente tehnice, iar modulul nu are fișiere de date sau vizualizări (`data: []`).*

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki.
