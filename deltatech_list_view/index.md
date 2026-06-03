# List View Select Text (localizat la `deltatech_list_view/index.md`)

- **Nume Tehnic:** `deltatech_list_view`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_list_view
- **Cale Locală:** `odoo-addons/deltatech/deltatech_list_view`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul îmbunătățește experiența de utilizare a vizualizărilor de tip listă din Odoo. În mod implicit, un simplu clic pe un rând dintr-o listă deschide înregistrarea respectivă, ceea ce face dificilă selectarea și copierea textului dintr-o celulă. Modulul rezolvă acest neajuns: atunci când utilizatorul selectează text într-un rând, deschiderea înregistrării este blocată, permițând astfel copierea comodă a informațiilor direct din listă.

#### 2. Funcționalități Cheie

- Blochează deschiderea unei înregistrări din listă atunci când utilizatorul selectează (evidențiază) text într-un rând.
- Permite copierea facilă a textului din celulele listei, fără a deschide accidental înregistrarea.
- Include o ajustare de stil pentru modul de afișare întunecat (dark mode).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, modulul are un scop strict de interfață (blocarea deschiderii unui element din listă la selectarea textului) și nu definește modele de date. Implementarea se face prin extinderea componentelor front-end:

**Active front-end**

- `static/src/js/list_renderer.esm.js`: extinde randarea listei (List Renderer) pentru a intercepta selecția de text și a împiedica deschiderea înregistrării (încărcat în `web.assets_backend`).
- `static/src/scss/style_dark.scss`: ajustări de stil pentru modul de afișare întunecat (încărcat în `web.assets_web_dark`).

**Modele**

- Modulul nu definește și nu extinde modele Odoo.

#### 5. Conexiuni

Modulul este o utilitate generică de interfață, fără conexiuni funcționale specifice către alte module documentate în acest wiki.
