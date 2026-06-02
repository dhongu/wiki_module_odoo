# Products Alternative (localizat la `deltatech_alternative/index.md`)

- **Nume Tehnic:** `deltatech_alternative`
- **Versiune:** `19.0.2.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_alternative
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul extinde gestiunea produselor cu coduri alternative și cu un catalog de date master pentru produse. Permite asocierea mai multor coduri alternative pentru același produs, astfel încât căutarea după aceste coduri să identifice corect produsul în comenzi, achiziții și mișcări de stoc. În plus, dispune de un catalog amplu de produse din care, atunci când o căutare după cod nu returnează rezultate, se poate genera automat un produs nou. Modulul ajută companiile care lucrează cu nomenclatoare extinse sau cu coduri venite de la furnizori și clienți diferiți.

#### 2. Funcționalități Cheie

- Model nou `product_catelog` pentru baze mari de date master de produse.
- Generarea automată a unui produs nou din catalog: dacă o căutare după cod nu returnează rezultate, se face o căutare suplimentară în catalogul de produse și se generează automat un produs, dacă a fost găsit.
- Adăugarea de coduri alternative pe fișa produsului.
- Căutarea produsului după codul alternativ.
- Câmp nou pe produs („used for”) care indică pentru ce poate fi utilizat produsul.
- Câmp `search_index` adăugat pe produs, în care se face căutarea dacă este setat parametrul `deltatech_alternative_website.search_index`.

#### 3. Dependențe

- `product`
- `stock`
- `sale`
- `purchase`

#### 4. Componente Cheie

*Secțiune populată din `readme/DESCRIPTION.md`; analiza detaliată a codului a fost omisă conform fluxului de ingestie.*

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki.
