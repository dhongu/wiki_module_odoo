# Website Dezactivare Căutare Fuzzy

- **Nume Tehnic:** `deltatech_website_disable_fuzzy_search`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_disable_fuzzy_search
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_disable_fuzzy_search`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Acest modul dezactivează căutarea „fuzzy” (aproximativă) din bara de căutare a magazinului online. În mod implicit, Odoo tolerează micile greșeli de scriere și returnează rezultate apropiate de termenul căutat. După instalare, căutarea devine exactă: clientul primește doar produsele care corespund termenului introdus, fără sugestii aproximative.

#### 2. Funcționalități Cheie

- Dezactivează căutarea fuzzy pentru bara de căutare din magazinul online, atât la sugestiile din autocomplete, cât și la rezultatele căutării din magazin.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

Modulul nu definește modele.

**Controllere**

- `Website` (extinde controllerul `website_sale`): `autocomplete` forțează `allowFuzzy = False`.
- `WebsiteSale`: `_get_search_options` forțează `allowFuzzy = False`.

**Vizualizări**

Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- `website_sale`: modulul de bază pentru magazinul online, ale cărui controllere de căutare sunt extinse pentru a dezactiva potrivirea aproximativă.
