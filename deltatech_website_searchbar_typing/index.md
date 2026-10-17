# Website Searchbar Typing Examples (localizat la `deltatech_website_searchbar_typing/index.md`)

- **Nume Tehnic:** `deltatech_website_searchbar_typing`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_searchbar_typing
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_searchbar_typing`
- **Ultima Ingestie:** `2026-10-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face ca textul de ajutor (placeholder-ul) dintr-o casetă de căutare a site-ului să scrie, literă cu literă, câteva exemple de căutări, unul după altul: exemplul se scrie, rămâne o clipă, se șterge și urmează următorul. Vizitatorul vede dintr-o privire ce poate căuta (un cod de piesă, o denumire de produs, un subiect din ghidurile de utilizare). Animația pornește doar pe casetele în care s-au pus exemple; instalarea singură nu schimbă nimic pe site.

#### 2. Funcționalități Cheie

- Opțiune per casetă: exemplele se pun în formularul de căutare, ca listă ascunsă `<ul class="o_searchbar_typing d-none" aria-hidden="true">`, câte un `li` pe exemplu; un `li` opțional cu clasa `o_searchbar_typing_prefix` (de ex. „ex.:”) apare în fața fiecărui exemplu.
- Opțiune în Website Builder pe caseta de căutare: **Typing examples** pornește sau oprește animația, iar **Prefix** și **Examples** (adăugare, ștergere, reordonare prin tragere) se editează în panou, fără editorul HTML; opțiunea scrie aceeași listă ascunsă (20.0.1.1.0).
- Exemplele sunt text obișnuit al paginii, deci se traduc cu pagina: fiecare `li` e un termen de traducere separat (cu `span` s-ar traduce tot blocul ca un singur termen).
- Animația se oprește definitiv la click în casetă sau la prima tastă, iar placeholder-ul inițial revine; căutarea și sugestiile standard (autocomplete) funcționează normal.
- Nu rulează când vizitatorul a cerut mișcare redusă (`prefers-reduced-motion`) și se oprește dacă preferința se activează în timpul vizitei; stă pe loc cât timp tab-ul e ascuns sau caseta nu e pe ecran; nu rulează în Website Builder.
- Accesibilitate: dacă și caseta nu are etichetă, placeholder-ul inițial devine `aria-label`, ca cititoarele de ecran să nu citească fiecare literă schimbată.
- Viteza se reglează cu atribute pe lista de exemple, în milisecunde: `data-start-delay` (1500), `data-type-delay` (70), `data-hold-delay` (1800), `data-erase-delay` (30), `data-next-delay` (400).
- Merge cu snippet-ul standard de căutare și cu șablonul `website.website_search_box_input`. Pe Odoo 20, parametrii șablonului se dau ca atribute pe `t-call` (`search_type.f`, `action.f`, `placeholder.f`), nu prin `t-set` în corpul apelului.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni server/automate: este o componentă front-end (JavaScript).

**Modele**

- Nu sunt definite sau extinse modele.

**Vizualizări**

- Nu sunt definite vizualizări. Lista de exemple se adaugă în vizualizarea paginii sau în snippet-ul de căutare al site-ului.

**Componentă JavaScript**

- `static/src/website_builder/searchbar_typing_option_plugin.esm.js` + `searchbar_typing_option.xml`: opțiunea „Typing examples” din panoul Website Builder, pe `.s_searchbar_input` (fără caseta din antet).
- `static/src/interactions/searchbar_typing.esm.js`: interacțiunea publică `SearchbarTyping` (API-ul `Interaction` din 20.0), pe `.o_searchbar_form` care conține `.o_searchbar_typing`. Testată cu Hoot (`static/tests/searchbar_typing.test.js`, rulat din `tests/test_js.py`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_website_searchbar](../deltatech_website_searchbar/index.md): optimizează cererile de autocompletare ale aceleiași bare de căutare; cele două module se pot folosi împreună.
