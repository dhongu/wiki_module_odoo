# Website Searchbar Typing Examples

- **Nume Tehnic:** `deltatech_website_searchbar_typing`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_searchbar_typing
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_searchbar_typing`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Placeholder-ul casetei de căutare de pe site „scrie” pe rând exemple de căutări: fiecare exemplu este tastat literă cu literă, ținut o clipă, șters, apoi urmează următorul. Vizitatorii văd dintr-o privire ce pot căuta (un cod de piesă, o denumire de produs, un subiect din ghidurile de utilizare). Funcția se activează individual pentru fiecare casetă de căutare; instalarea modulului nu schimbă nimic altceva pe site.

#### 2. Funcționalități Cheie

- Activare la cerere, per casetă de căutare: se animă doar formularele de căutare care conțin exemple.
- Exemplele sunt text simplu în formular (listă ascunsă `ul.o_searchbar_typing` cu elemente `li`), deci se traduc odată cu pagina și se editează ca orice alt text. Se folosesc `li`, nu `span`, pentru ca fiecare exemplu să fie tradus ca termen separat.
- Prefix opțional (`li.o_searchbar_typing_prefix`, ex. „ex.”), afișat înaintea fiecărui exemplu.
- Animația se oprește definitiv când vizitatorul face clic în casetă sau începe să scrie, iar placeholder-ul original revine.
- Nu rulează dacă vizitatorul a cerut mișcare redusă (`prefers-reduced-motion`) și se oprește dacă setarea este activată în timpul vizitei.
- Așteaptă cât timp tab-ul browserului este ascuns sau caseta este în afara ecranului.
- Nume accesibil stabil: dacă caseta nu are etichetă, placeholder-ul original devine `aria-label`, ca cititoarele de ecran să nu citească fiecare literă.
- Funcționează cu snippetul standard de căutare și cu template-ul `website.website_search_box_input`, alături de dropdown-ul standard de autocompletare.
- Opțiune în Website Builder pe câmpul de căutare, „Typing examples”: pornește/oprește animația, iar prefixul și exemplele se editează în panou (adăugare, ștergere, reordonare prin tragere), fără editorul HTML.
- Viteza se reglează prin atribute `data-*` pe elementul `o_searchbar_typing`, în milisecunde: `data-start-delay` (1500), `data-type-delay` (70), `data-hold-delay` (1800), `data-erase-delay` (30), `data-next-delay` (400).
- Recomandare: alegeți exemple care returnează rezultate.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele Python; este exclusiv front-end.

**Vizualizări**

- `static/src/interactions/searchbar_typing.esm.js`: interacțiunea publică (`web.assets_frontend`) care rulează animația de tastare.
- `static/src/website_builder/searchbar_typing_option.xml` și `searchbar_typing_option_plugin.esm.js`: opțiunea „Typing examples” din Website Builder (se aplică pe `.s_searchbar_input`, input `.search-query`).

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- Nicio legătură funcțională verificată cu alte module; completează standard `website` (căutare, autocompletare).
