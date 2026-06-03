# Website Dezactivare Căutare Fuzzy

- **Nume Tehnic:** `deltatech_website_disable_fuzzy_search`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_disable_fuzzy_search`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_disable_fuzzy_search`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul dezactivează căutarea „fuzzy" (aproximativă) din bara de căutare a magazinului online. În mod implicit, Odoo tolerează micile greșeli de scriere și returnează rezultate apropiate de termenul căutat. După instalarea acestui modul, căutarea devine exactă: clientul primește doar produsele care corespund efectiv termenului introdus, fără sugestii aproximative. Este util pentru magazinele care doresc rezultate de căutare precise și predictibile.

#### 2. Funcționalități Cheie

- Dezactivează căutarea fuzzy (aproximativă) pentru bara de căutare din magazinul online.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile pentru componente nu sunt detaliate atunci când există un fișier `readme/DESCRIPTION.md`. Acest modul nu definește modele, vizualizări sau acțiuni automate proprii; funcționalitatea este implementată prin extinderea controllerelor web ale modulului `website_sale` (forțarea opțiunii `allowFuzzy = False` în autocomplete și în opțiunile de căutare).

#### 5. Conexiuni

- `website_sale`: modulul de bază pentru magazinul online ale cărui controllere de căutare sunt extinse pentru a dezactiva potrivirea aproximativă.
