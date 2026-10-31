# List View Select Text (localizat la `deltatech_list_view/index.md`)

- **Nume Tehnic:** `deltatech_list_view`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_list_view
- **Cale Locală:** `odoo-addons/deltatech/deltatech_list_view`
- **Ultima Ingestie:** `2026-10-31`

#### 1. Sumar

Acest modul îmbunătățește experiența de utilizare a vizualizărilor de tip listă din Odoo. În mod implicit, un simplu clic pe un rând dintr-o listă deschide înregistrarea respectivă, ceea ce face dificilă selectarea și copierea textului dintr-o celulă. Modulul rezolvă acest neajuns: atunci când utilizatorul selectează text într-un rând, deschiderea înregistrării este blocată, permițând copierea comodă a informațiilor direct din listă. În plus, corectează o eroare la ștergerea repetată a unei linii nesalvate dintr-un câmp one2many.

#### 2. Funcționalități Cheie

- Blochează deschiderea unei înregistrări din listă atunci când utilizatorul selectează (evidențiază) text într-un rând.
- Permite copierea facilă a textului din celulele listei, fără a deschide accidental înregistrarea.
- Ștergerea de două ori a unei linii one2many nesalvate (de exemplu, Enter apăsat de două ori pe pictograma de ștergere) nu mai blochează salvarea formularului cu eroarea `virtual_N`.
- Include o ajustare de stil pentru modul de afișare întunecat (dark mode).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Modulul are un scop strict de interfață și nu definește modele de date. Implementarea se face prin extinderea componentelor front-end:

**Active front-end**

- `static/src/js/list_renderer.esm.js`: extinde `ListRenderer.onCellClicked` astfel încât clicul pe celulă să deschidă înregistrarea doar dacă nu există text selectat în browser (încărcat în `web.assets_backend`).
- `static/src/js/static_list.esm.js`: extinde `StaticList._applyCommands` și elimină comenzile DELETE/UNLINK cu id virtual (șir de caractere), pentru linii care nu au fost niciodată salvate (încărcat în `web.assets_backend`).
- `static/src/scss/style_dark.scss`: ajustări de stil pentru modul de afișare întunecat (încărcat în `web.assets_web_dark`).
- `static/tests/static_list_delete.test.js`: test unitar pentru ștergerea repetată a liniei nesalvate (încărcat în `web.assets_unit_tests`).

**Modele**

- Modulul nu definește și nu extinde modele Odoo.

#### 5. Conexiuni

Modulul este o utilitate generică de interfață, fără conexiuni funcționale specifice către alte module documentate în acest wiki.
