# Many2one Badge Widget (localizat la `deltatech_widget_many2one_badge/index.md`)

- **Nume Tehnic:** `deltatech_widget_many2one_badge`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_widget_many2one_badge`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_widget_many2one_badge`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul adaugă un widget web personalizat care afișează câmpurile de tip Many2one sub forma unor etichete (badge-uri) colorate, într-un mod similar cu widget-ul standard `many2many_tags`. Scopul este de a îmbunătăți lizibilitatea și aspectul vizual al interfețelor Odoo, permițând utilizatorilor să distingă rapid valorile prin culoare, atât în formulare cât și în liste. Culoarea poate fi modificată direct din interfață, fiind salvată pe înregistrarea relaționată.

#### 2. Funcționalități Cheie

- Afișează câmpul Many2one ca badge colorat în modul readonly.
- Permite schimbarea culorii prin click pe badge, folosind un selector de culori (popover) în modul de editare.
- Buton de ștergere (`×`) care apare la trecerea cu mouse-ul peste badge.
- Câmp de autocomplete pentru selectarea unei noi valori atunci când câmpul este gol.
- Opțiune configurabilă `color_field` pentru a indica numele câmpului care stochează indexul de culoare.
- Compatibil cu toate cele 12 culori standard Odoo (indecșii 0–11).
- Design modern, cu badge rotunjit.

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

- Niciuna identificată. Modulul este un utilitar de interfață generic, fără legături funcționale specifice către alte module din suită.
