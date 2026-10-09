# Product Attribute Search (localizat la `deltatech_product_attribute_search/index.md`)

- **Nume Tehnic:** `deltatech_product_attribute_search`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_attribute_search
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_attribute_search`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

La produsele cu variante, singurul lucru care deosebește două variante pe ecran sunt valorile atributelor din nume, de exemplu `Mere (Gala Mast, 70/75 mm)`. Odoo standard caută însă doar după numele șablonului, referința internă și codul de bare, deci cine tastează soiul sau calibrul într-un câmp de produs (linie de comandă de vânzare sau achiziție) nu primește nimic. Modulul face valorile atributelor căutabile în orice câmp de produs și în orice vedere de căutare, astfel încât operatorul găsește varianta după cuvintele de pe marfă.

#### 2. Funcționalități Cheie

- **Căutare după valori de atribute** în orice câmp de produs (comenzi de vânzare/achiziție, mișcări de stoc) și în vederile de căutare: `gala` găsește toate variantele cu valoarea *Gala Mast*, indiferent de șablon.
- **Cuvinte combinate, în orice ordine:** fiecare cuvânt trebuie să se potrivească undeva (nume, referință sau o valoare de atribut), iar cuvintele se combină cu ȘI. `mere gala 80` restrânge la o singură variantă; adăugarea unui cuvânt doar îngustează rezultatul. Un prefix e suficient (`ga` găsește *Gala Mast*).
- **Aceleași rezultate în vânzări și achiziții**, pentru aceeași interogare.
- **Referința internă rămâne prioritară:** `GALA-13` se potrivește tot primul după referință, ca înainte.
- **Excluderea atributelor „zgomotoase”:** în **Inventar → Configurare → Atribute**, debifarea câmpului **Căutabil** (`search_ok`) scoate atributul din căutare (de ex. o clasă numită `1/5` sau o mărime numită `2`). Bifa e per atribut, nu per valoare, și afectează doar căutarea.
- **Fără cost pe căutările care funcționau deja:** Odoo răspunde primul, iar căutarea suplimentară rulează doar dacă pagina de rezultate a rămas incompletă.
- Fără configurare obligatorie: toate atributele sunt căutabile implicit după instalare.
- Limite: se aplică doar operatorilor de tip text (`=`, `like`, `ilike`, `=like`, `=ilike`); intrările goale sau cu mai mult de 5 cuvinte sunt lăsate pe seama căutării standard.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `product.attribute` (extins): adaugă câmpul boolean `search_ok` („Căutabil”, implicit activ), care decide dacă valorile atributului intră în căutare.
- `product.product` (extins): suprascrie `name_search` (calea câmpului de produs din liniile de comandă) și `_search_display_name` (vederi de căutare, import); construiește domeniul de căutare pe nume, referință și valori de atribute prin `_attribute_search_domain`.

**Vizualizări**

- `product_attribute_view_form`: afișează câmpul **Căutabil** în formularul atributului.
- `attribute_tree_view`: afișează câmpul **Căutabil** în lista atributelor.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `sale`, `purchase`, `stock`: câmpurile de produs din liniile de comandă și din mișcările de stoc beneficiază de căutarea extinsă (modulul nu depinde de ele).
