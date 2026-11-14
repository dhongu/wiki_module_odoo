# List View Select Text (localizat la `deltatech_list_view/index.md`)

- **Nume Tehnic:** `deltatech_list_view`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_list_view
- **Cale Locală:** `odoo-addons/deltatech/deltatech_list_view`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul îmbunătățește experiența de utilizare a vizualizărilor de tip listă din Odoo. În mod implicit, un simplu clic pe un rând dintr-o listă deschide înregistrarea respectivă, ceea ce face dificilă selectarea și copierea textului dintr-o celulă. Modulul rezolvă acest neajuns: atunci când utilizatorul selectează text într-un rând, deschiderea înregistrării este blocată, permițând copierea comodă a informațiilor direct din listă. În plus, corectează o eroare la ștergerea repetată a unei linii nesalvate dintr-un câmp one2many.

#### 2. Funcționalități Cheie

- Blochează deschiderea unei înregistrări din listă atunci când utilizatorul selectează (evidențiază) text într-un rând.
- Permite copierea facilă a textului din celulele listei, fără a deschide accidental înregistrarea.
- Ștergerea de două ori a unei linii one2many nesalvate (de exemplu, Enter apăsat de două ori pe pictograma de ștergere) nu mai blochează salvarea formularului cu eroarea `virtual_N`.
- În tema întunecată, elimină fundalul deschis al imaginilor din formulare și din vizualizările kanban.
- Utilizare: după instalare nu e nimic de configurat; selectezi textul cu mouse-ul (trage de la începutul la sfârșitul valorii) și îl copiezi cu Ctrl+C, iar un clic simplu pe rând deschide înregistrarea ca de obicei.
- Modulul nu conține cod Python, doar JavaScript și o foaie de stil, deci poate fi folosit și pe Odoo Online (plan Custom): arhiva zip se încarcă din **Apps > Import Module**, pe lângă Odoo.sh și instalările on-premise.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Modulul are un scop strict de interfață și nu definește modele de date. Implementarea se face prin extinderea componentelor front-end:

**Active front-end**

- `static/src/js/list_renderer.esm.js`: extinde `ListRenderer.onCellClicked` astfel încât clicul pe celulă să deschidă înregistrarea doar dacă nu există text selectat în browser (încărcat în `web.assets_backend`).
- `static/src/js/static_list.esm.js`: extinde `StaticList._applyCommands` și elimină comenzile DELETE/UNLINK cu id virtual (șir de caractere), pentru linii care nu au fost niciodată salvate (încărcat în `web.assets_backend`).
- `static/src/scss/style_dark.scss`: elimină fundalul imaginilor (`.o_field_image`, imaginile din `.o_kanban_renderer`) în tema întunecată (încărcat în `web.assets_web_dark`).
- `static/tests/static_list_delete.test.js`: test unitar JavaScript pentru ștergerea repetată a liniei nesalvate (încărcat în `web.assets_unit_tests`, rulează cu testele web: `/web/tests?filter=deltatech_list_view`).

**Modele**

- Modulul nu definește și nu extinde modele Odoo.

#### 5. Conexiuni

Modulul este o utilitate generică de interfață, fără conexiuni funcționale specifice către alte module documentate în acest wiki.
