# Website Searchbar Optimization (localizat la `deltatech_website_searchbar/index.md`)

- **Nume Tehnic:** `deltatech_website_searchbar`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/deltatech_website_searchbar
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_searchbar`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul reduce numărul de cereri de autocompletare trimise de bara de căutare de pe site (endpoint-ul `/website/snippet/autocomplete`), pentru a scădea încărcarea serverului și traficul inutil generat în timp ce utilizatorul tastează. Este util mai ales pe site-uri e-commerce cu trafic ridicat, unde fiecare literă tastată în căutare poate genera altfel o cerere separată către server.

#### 2. Funcționalități Cheie

- Crește întârzierea de „debounce" a barei de căutare de la valoarea implicită de 400ms la 800ms, astfel încât cererea de autocompletare pornește abia după ce utilizatorul se oprește din tastat.
- Introduce o lungime minimă a termenului de căutare de 4 caractere (după eliminarea spațiilor) înainte de a trimite orice cerere către server.
- Când termenul introdus este mai scurt de 4 caractere, lista de sugestii se golește local (fără cerere către server), evitând rezultate prea multe și nespecifice.
- Nu necesită nicio configurare — optimizările se aplică automat tuturor barelor de căutare de pe site după instalare.
- Constantele `MIN_SEARCH_TERM_LENGTH` (4) și `DEBOUNCE_DELAY` (800ms) pot fi ajustate direct în cod (`static/src/js/searchbar.esm.js`) dacă sunt necesare alte valori.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

Modulul nu introduce modele, vizualizări sau acțiuni server/automate — este o extensie pur front-end (JavaScript), care aplică un `patch()` peste interacțiunea publică standard `SearchBar` din modulul `website`.

**Modele**

- Nu sunt definite sau extinse modele.

**Vizualizări**

- Nu sunt definite vizualizări.

**Componentă JavaScript**

- `static/src/js/searchbar.esm.js`: patch peste interacțiunea `SearchBar` a modulului `website` — în `setup()` înlocuiește handler-ul `t-on-input` din `dynamicContent` cu o versiune debounced (800ms), iar în `onInput()` adaugă verificarea lungimii minime a termenului (4 caractere) înainte de a apela `fetch()`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `website`: extinde direct widget-ul de căutare (bara de căutare/autocomplete) al modulului de site.
