# Culori pe Categoriile de Produse (localizat la `deltatech_product_category_color/index.md`)

- **Nume Tehnic:** `deltatech_product_category_color`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_category_color
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_category_color`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o culoare fiecărei categorii de produse și afișează, pe cardurile transferurilor în vizualizarea Kanban, etichete colorate cu categoriile produselor din transfer. Operatorul de depozit vede dintr-o privire ce fel de marfă conține un transfer, fără să deschidă documentul. Culoarea este doar informație de afișare, fără efect asupra stocului sau contabilității.

#### 2. Funcționalități Cheie

- Câmpul de culoare (**Color Index**) pe categoria de produse, cu valoare aleatorie implicită.
- Etichete colorate cu categoriile produselor pe cardurile Kanban ale transferurilor.
- Modificarea culorii cere dreptul **Produse: Creează**; etichetele sunt vizibile utilizatorilor **Inventar: Utilizator**.
- Detaliile de utilizare sunt în fișa consultantului.

#### 3. Dependențe

- `product`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.category`: câmpul `color`.
- `stock.picking`: câmpul calculat `categ_ids` cu categoriile produselor din transfer.

**Vizualizări**

- `views/product_category_view.xml`: câmpul de culoare pe categorie.
- `views/stock_picking_view.xml`: etichetele colorate pe cardul Kanban al transferului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_product_category_group](../deltatech_product_category_group/index.md): modul înrudit, tot pe categoriile de produse și transferurile de stoc, fără dependență declarată.
