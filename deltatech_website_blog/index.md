# Blog Post Sorting (localizat la `deltatech_website_blog/index.md`)

- **Nume Tehnic:** `deltatech_website_blog`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_blog
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_blog`
- **Ultima Ingestie:** `2026-11-14`

#### 1. Sumar

Un blog se citește de obicei de la cea mai nouă postare la cea mai veche, după data publicării. Modulul setează aceasta ca ordine implicită de sortare a articolelor de blog de pe website, astfel încât cele mai recente postări apar mereu primele.

#### 2. Funcționalități Cheie

- **Data publicării:** articolele sunt sortate descrescător după data publicării (`published_date`).
- **Aceeași dată:** articolele cu aceeași dată de publicare sunt sortate descrescător după ID, deci cel creat cel mai recent apare primul.
- **Doar ordinea implicită:** ordinea e setată pe modelul articolului și se aplică oriunde articolele sunt citite fără o ordine cerută explicit; un ecran, filtru sau interogare care cere altă ordine și-o păstrează.
- **Fără alte schimbări:** modulul nu adaugă câmpuri, vizualizări, meniuri, setări sau drepturi de acces și nu modifică articolele în sine.

#### 3. Dependențe

- `website_blog`

#### 4. Componente Cheie

**Modele**

- `blog.post`: extinde modelul standard de articole de blog, suprascriind ordinea implicită (`_order`) la `published_date desc, id desc`.

**Vizualizări**

Nu sunt definite vizualizări noi.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `website_blog`: modulul standard Odoo al cărui comportament de sortare este ajustat.
