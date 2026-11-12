# Product Category Colors (localizat la `deltatech_product_category_color/index.md`)

- **Nume Tehnic:** `deltatech_product_category_color`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_category_color
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_category_color`
- **Ultima Ingestie:** `2026-11-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o culoare distinctă fiecărei categorii de produse, culoare care se regăsește apoi pe cardurile transferurilor de stoc din vizualizarea Kanban. Astfel, la o simplă privire asupra unui transfer (recepție, livrare, transfer intern), utilizatorul vede din ce categorii fac parte produsele, fără a deschide documentul. Valoarea de business constă în viteza de citire și de împărțire a muncii în depozite cu multe categorii de produse. Culoarea este doar o informație de afișare: nu are efect asupra stocului sau contabilității.

#### 2. Funcționalități Cheie

- Câmp de culoare (**Color Index**, selector de culori Odoo) pe categoria de produse, sub câmpul părinte. La instalare, fiecare categorie existentă primește o culoare aleasă la întâmplare (la fel orice categorie nouă); prima căsuță a paletei înseamnă „fără culoare" (etichetă gri).
- Pe fiecare card din Kanban-ul transferurilor (**Inventory > Operations > Transfers / Receipts / Deliveries**) apare câte o etichetă colorată pentru fiecare categorie a produselor din transfer, o singură dată per categorie.
- Categoriile se iau din liniile de mișcare ale transferului, fără cele anulate (nu din cantitățile rezervate), deci și transferurile nerezervate afișează categoriile.
- Categoriile se aleg din **Inventory > Configuration > Product Categories**. Fluxul pas cu pas este în fișa consultant.

> Notă: în Odoo Apps modulul apare sub numele „Product Category Colors" (anterior „Products Category Color"); numele tehnic nu s-a schimbat.

#### 3. Dependențe

- `product`
- `stock`

#### 4. Componente Cheie

Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md` (un singur rând), completat cu fișa consultant și istoricul; mai jos, o verificare punctuală a codului.

**Modele**

- `product.category` (extins): câmpul `color` („Color Index", întreg), cu valoare implicită aleatorie între 1 și 11.
- `stock.picking` (extins): câmpul calculat `categ_ids` (Many2many către `product.category`), derivat din produsele mișcărilor care nu sunt anulate.

**Vizualizări**

- `product_category_form_view`: moștenește `product.product_category_form_view` și adaugă câmpul `color` (widget `color_picker`).
- `stock_picking_kanban`: moștenește `stock.stock_picking_kanban` și afișează `categ_ids` ca etichete colorate (`many2many_tags`, `color_field: color`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în acest wiki; modulul extinde modele native din `product` și `stock`.
