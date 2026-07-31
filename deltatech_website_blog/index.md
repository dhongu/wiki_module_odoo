# Deltatech Web Site Blog (localizat la `deltatech_website_blog/index.md`)

- **Nume Tehnic:** `deltatech_website_blog`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_blog](https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_blog)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_blog`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul ordonează articolele din Blogul de pe website după data de publicare, astfel încât cele mai recente postări apar mereu primele — o corecție simplă, dar utilă, pentru afișarea implicită a blogului Odoo.

#### 2. Funcționalități Cheie

- Sortează articolele de blog descrescător după data de publicare (`published_date`).
- Pentru articole cu aceeași dată de publicare, aplică o sortare secundară descrescătoare după ID, ca să păstreze o ordine consistentă și previzibilă.

#### 3. Dependențe

- `website_blog`

#### 4. Componente Cheie

**Modele**

- `blog.post`: extinde modelul standard de articole de blog, suprascriind ordinea implicită (`_order`) la `published_date desc, id desc`.

**Vizualizări**

Nu sunt definite vizualizări noi — modulul modifică doar ordinea de bază a modelului, ordine moștenită automat de toate listele/kanban-urile standard de blog.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `website_blog`: modulul standard Odoo al cărui comportament de sortare este ajustat.
