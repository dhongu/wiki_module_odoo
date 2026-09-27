# Many2one Badge Widget (localizat la `deltatech_widget_many2one_badge/index.md`)

- **Nume Tehnic:** `deltatech_widget_many2one_badge`
- **Versiune:** `20.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_widget_many2one_badge`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_widget_many2one_badge`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Modulul adaugă un widget web personalizat care afișează câmpurile de tip Many2one sub forma unor etichete (badge-uri) colorate, într-un mod similar cu widget-ul standard `many2many_tags`. Scopul este de a îmbunătăți lizibilitatea și aspectul vizual al interfețelor Odoo, permițând utilizatorilor să distingă rapid valorile prin culoare, atât în formulare cât și în liste. Culoarea poate fi modificată direct din interfață, fiind salvată pe înregistrarea relaționată.

#### 2. Funcționalități Cheie

- Afișează câmpul Many2one ca badge colorat în modul readonly.
- Permite schimbarea culorii prin click pe badge, folosind un selector de culori (popover cu `ColorList`) în modul de editare.
- Buton de ștergere (`×`) care apare la trecerea cu mouse-ul peste badge.
- Câmp de autocomplete (`Many2XAutocomplete`) pentru selectarea unei noi valori atunci când câmpul este gol.
- Opțiune configurabilă `color_field` (câmp de tip `integer` de pe modelul relaționat) pentru a indica de unde se citește/salvează indexul de culoare; implicit `'color'`.
- Compatibil cu toate cele 12 culori standard Odoo (indecșii 0–11).
- Design modern, cu badge rotunjit (`o_tag_color_<index>`).
- Se activează pe orice câmp Many2one existent prin `widget="many2one_badge"` și `options="{'color_field': 'color'}"`, fără modificări de model — modelul relaționat trebuie doar să aibă câmpul de culoare respectiv.

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

**Asset-uri (web.assets_backend / web.assets_unit_tests)**

- `static/src/js/many2one_badge_field.esm.js`: componenta OWL `Many2oneBadgeField` a widget-ului `many2one_badge`, înregistrată în `registry.category("fields")`; folosește `useProps` (compatibil Owl 3 — `static props`/`static defaultProps` nu mai sunt permise) și un popover `Many2oneBadgeColorPopover` cu `ColorList` din `@web/core/colorlist/colorlist`.
- `static/src/xml/many2one_badge_field.xml`: template-urile QWeb ale widget-ului (`Many2oneBadgeField` și `ColorPopover`); folosește `t-out` (nu `t-esc`/`t-raw`, ignorate în Odoo 20 pe server-side, dar corect și pentru client-side QWeb).
- `static/src/css/many2one_badge_field.css`: stilurile pentru badge-ul colorat.
- `static/tests/many2one_badge_field.test.esm.js`: teste unitare JS (`web.assets_unit_tests`), rulate cu suita de teste OWL/Hoot, nu QUnit.

#### 5. Conexiuni

- Niciuna identificată. Modulul este un utilitar de interfață generic, fără legături funcționale specifice către alte module din suită.
