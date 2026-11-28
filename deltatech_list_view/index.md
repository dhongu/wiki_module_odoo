# List View Select Text (localizat la `deltatech_list_view/index.md`)

- **Nume Tehnic:** `deltatech_list_view`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_list_view
- **Cale Locală:** `odoo-addons/deltatech/deltatech_list_view`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face listele din Odoo mai comode: la selectarea unui text dintr-un rând (un email, un telefon, o referință), înregistrarea nu se mai deschide, iar textul poate fi copiat direct din listă. Este doar front-end, fără cod Python, deci poate fi importat și pe Odoo Online.

#### 2. Funcționalități Cheie

- Blochează deschiderea unei înregistrări din listă atunci când utilizatorul selectează text într-un rând; un clic simplu pe rând o deschide ca de obicei.
- Corectează salvarea formularului după ce o linie one2many nesalvată a fost ștearsă de două ori (de exemplu Enter apăsat de două ori pe iconița de ștergere), care producea eroarea `virtual_N`.
- În tema întunecată, elimină fundalul deschis al imaginilor din formulare și kanban.
- Nu necesită configurare; pe Odoo Online (plan Custom) se instalează din **Apps > Import Module**.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Modulul nu definește modele; este un strat de interfață.

**Active front-end**

- `static/src/js/list_renderer.esm.js` și `static/src/js/static_list.esm.js`: extind randarea listei și lista statică (`web.assets_backend`).
- `static/src/scss/style_dark.scss`: stil pentru modul întunecat (`web.assets_web_dark`).

#### 5. Conexiuni

Utilitar generic de interfață, fără conexiuni funcționale către alte module documentate.
