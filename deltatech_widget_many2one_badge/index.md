# Many2one Badge Widget (localizat la `deltatech_widget_many2one_badge/index.md`)

- **Nume Tehnic:** `deltatech_widget_many2one_badge`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_widget_many2one_badge
- **Cale Locală:** `odoo-addons/deltatech/deltatech_widget_many2one_badge`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un widget care afișează câmpurile de tip Many2one sub forma unor etichete (badge-uri) colorate, asemănător widget-ului standard `many2many_tags`. Utilizatorii disting rapid valorile prin culoare, atât în formulare, cât și în liste, iar culoarea poate fi schimbată direct din interfață. Culoarea se salvează pe înregistrarea relaționată, deci toate documentele care folosesc aceeași valoare (de exemplu aceeași fază a comenzii) afișează noua culoare.

#### 2. Funcționalități Cheie

- Afișează câmpul Many2one ca badge colorat, în formulare și în liste.
- Modulul nu are meniuri proprii: badge-ul apare pe câmpurile unde îl folosesc alte module, de exemplu coloana **Phase** din **Sales → Orders → Orders** (faza comenzii din `deltatech_sale_stage`) sau faza comenzii de achiziție (`deltatech_purchase_phase`).
- Schimbarea culorii: click pe badge deschide un selector de culori (popover) cu 11 culori (indecșii 1–11); culoarea aleasă se scrie imediat pe înregistrarea relaționată, nu pe document. Pentru salvare e nevoie de drept de scriere pe modelul relaționat (de exemplu Sales / Administrator pentru fazele comenzilor). Indexul 0 (fără culoare, gri) se setează din formularul înregistrării relaționate.
- Buton de ștergere (`×`) care apare la trecerea cu mouse-ul peste badge și golește valoarea, readucând câmpul de căutare pentru a alege alta.
- Câmp de autocomplete pentru selectarea unei valori noi când câmpul este gol.
- Opțiunea `color_field` indică câmpul întreg al modelului relaționat care stochează indexul culorii.
- Compatibil cu cele 12 culori standard Odoo (indecșii 0–11).
- Performanță: culorile tuturor badge-urilor afișate pe ecran se citesc cu un singur apel către server (o listă de 80 de comenzi nu mai generează 80 de cereri), iar culoarea nu se recitește dacă valoarea câmpului rămâne aceeași.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Modulul nu definește și nu extinde modele Python, vizualizări sau acțiuni automate. El furnizează exclusiv un widget de interfață (JavaScript/OWL) înregistrat în asset-urile backend.

**Modele**

- Niciun model definit sau extins.

**Vizualizări**

- Nicio vizualizare definită. Widget-ul se utilizează în vizualizările existente prin atributul `widget="many2one_badge"` pe un câmp Many2one, cu opțiunea `options="{'color_field': 'color'}"`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

**Asset-uri (web.assets_backend)**

- `static/src/js/many2one_badge_field.esm.js`: implementarea componentei OWL a widget-ului `many2one_badge`.
- `static/src/xml/many2one_badge_field.xml`: template-ul QWeb al widget-ului.
- `static/src/css/many2one_badge_field.css`: stilurile pentru badge-ul colorat.

#### 5. Conexiuni

- `deltatech_sale_stage`: folosește widget-ul pentru faza comenzii de vânzare (exemplul din fișa consultant); modulul nu e o dependență.
- `deltatech_purchase_phase`: folosește widget-ul pentru faza comenzii de achiziție, în același mod.
