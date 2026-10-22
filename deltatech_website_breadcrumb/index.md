# eCommerce Category Breadcrumb (localizat la `deltatech_website_breadcrumb/index.md`)

- **Nume Tehnic:** `deltatech_website_breadcrumb`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_breadcrumb
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_breadcrumb`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Acest modul îmbunătățește navigarea în magazinul online Odoo, afișând o linie de navigare (breadcrumb) în partea de sus a paginii de produs, care reflectă ierarhia categoriei publice din care face parte produsul. Astfel, clientul vede întotdeauna unde se află în structura catalogului și poate reveni rapid la categoriile părinte sau la lista de produse, ceea ce ușurează explorarea ofertei și crește gradul de orientare în magazin.

#### 2. Funcționalități Cheie

- Adaugă o linie de navigare (breadcrumb) în partea de sus a paginii de produs din website, în locul celei standard.
- Traseul pornește de la *Products* și cuprinde categoria publică a produsului, inclusiv toate categoriile părinte, fiecare fiind link activ.
- Numele produsului de la finalul traseului poate fi dezactivat din setările website-ului (*Product Name in Breadcrumb*), când titlul paginii îl afișează deja; opțiunea se setează per website.
- Un produs fără categorie afișează în continuare *Products*; când produsul are mai multe categorii, se folosește una disponibilă pe website-ul curent și, dacă există, una afișată în meniul de categorii.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

DESCRIPTION.md nu acoperă această secțiune; componentele de mai jos au fost sintetizate din `__manifest__.py` și din cod.

**Modele**

- `website` (extins): adaugă câmpul boolean `breadcrumb_show_product_name` (implicit activ).
- `res.config.settings` (extins): expune câmpul de mai sus în setările website-ului.
- `product.template` (extins): metoda `_breadcrumb_category()` alege categoria afișată în breadcrumb (disponibilă pe website-ul curent, preferând una vizibilă în meniu dacă există câmpul `tb_menu_hidden`).

**Vizualizări**

- `deltatech_website_breadcrumb.product`: extinde șablonul `website_sale.product`, ascunde breadcrumb-ul standard și inserează breadcrumb-ul personalizat.
- `deltatech_website_breadcrumb.breadcrumb`: șablonul principal al traseului de navigare.
- `deltatech_website_breadcrumb.breadcrumb_recursive`: șablon recursiv care parcurge categoriile părinte.
- `res_config_settings_view_form`: adaugă în setările `website_sale` opțiunea *Product Name in Breadcrumb*.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `website_sale`: modulul de bază al magazinului online ale cărui pagini de produs și categorii publice sunt extinse de acest breadcrumb.
- [deltatech_website_shop_snippets](../deltatech_website_shop_snippets/index.md): opțional; categoriile marcate `tb_menu_hidden` (ex. campanii) sunt evitate în breadcrumb.
