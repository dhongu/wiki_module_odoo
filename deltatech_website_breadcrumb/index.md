# eCommerce Category Breadcrumb (localizat la `deltatech_website_breadcrumb/index.md`)

- **Nume Tehnic:** `deltatech_website_breadcrumb`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_breadcrumb
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_breadcrumb`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul îmbunătățește navigarea în magazinul online Odoo, afișând o linie de navigare (breadcrumb) în partea de sus a paginii de produs, care reflectă ierarhia categoriei publice din care face parte produsul. Astfel, clientul vede întotdeauna unde se află în structura catalogului și poate reveni rapid la categoriile părinte sau la lista de produse, ceea ce ușurează explorarea ofertei și crește gradul de orientare în magazin.

#### 2. Funcționalități Cheie

- Adaugă o linie de navigare (breadcrumb) în partea de sus a paginii de produs din website.
- Construiește traseul de navigare pe baza categoriei publice a produsului, inclusiv toate categoriile părinte (recursiv).
- Fiecare element din breadcrumb este un link activ către categoria respectivă sau către lista generală de produse.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

DESCRIPTION.md nu acoperă această secțiune; componentele de mai jos au fost sintetizate din `__manifest__.py` și din cod.

**Vizualizări**

- `deltatech_website_breadcrumb.product`: extinde șablonul `website_sale.product`, ascunde breadcrumb-ul standard și inserează breadcrumb-ul personalizat al modulului.
- `deltatech_website_breadcrumb.breadcrumb`: șablonul principal care construiește lista de navigare pornind de la prima categorie publică a produsului și până la numele produsului curent.
- `deltatech_website_breadcrumb.breadcrumb_recursive`: șablon recursiv care parcurge categoriile părinte pentru a genera traseul complet al ierarhiei de categorii.

#### 5. Conexiuni

- `website_sale`: modulul de bază al magazinului online ale cărui pagini de produs și categorii publice sunt extinse de acest breadcrumb.
