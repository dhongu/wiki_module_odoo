# eCommerce Wishlist

- **Nume Tehnic:** `deltatech_website_sale_wishlist`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_wishlist
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_wishlist`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul extinde lista de dorințe din magazinul online cu o vedere în backend, în care administratorii văd ce produse au adăugat clienții la favorite și cât stoc există pentru ele. Astfel, cererea exprimată de clienți, dar încă neconvertită în comenzi, poate fi folosită pentru reaprovizionare, campanii de marketing sau oferte personalizate.

#### 2. Funcționalități Cheie

- Meniu dedicat **Wishlists**, în **Website > eCommerce > Products** (sub Catalog), cu vizualizare listă și formular pentru toate elementele din listele de dorințe de pe platformă.
- Vizibilitate pe partener: se vede ce client a adăugat ce produs, împreună cu prețul.
- Conștientizarea stocului: coloana **Quantity On Hand** (cantitate disponibilă) pentru fiecare produs, inclusiv căutare/filtrare după ea, utilă pentru identificarea cererii la produse fără stoc.
- Buton **Replenish** în antetul listei: lansează aprovizionarea (regulile de stoc, `stock.rule`) pentru produsele selectate, câte 1 unitate în unitatea de măsură a produsului, pe depozitul implicit al utilizatorului. Referința comenzii este „Required for wishlist" / „wishlist", iar partenerul este responsabilul produsului.

#### 3. Dependențe

- `website_sale_wishlist`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.wishlist` (extins): adaugă câmpul calculat și căutabil `qty_available`, plus metodele `action_launch_replenishment` și `_prepare_run_values` (creează un `stock.reference` pentru aprovizionare, în locul `procurement.group` din versiunile anterioare).

**Vizualizări**

- `product_wishlist_tree`: listă cu partener, produs, cantitate disponibilă, preț și butonul Replenish.
- `product_wishlist_form`: formular simplu cu aceleași câmpuri.
- `product_wishlist_action` și `menu_product_wishlist`: acțiunea și meniul Wishlists, sub `website_sale.menu_catalog`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `website_sale`: meniul este plasat sub catalogul eCommerce.
- `stock`: cantitățile disponibile și regulile de aprovizionare folosite de butonul Replenish.
