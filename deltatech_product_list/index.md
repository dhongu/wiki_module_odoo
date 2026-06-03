# Listă de Produse (localizat la `deltatech_product_list/index.md`)

- **Nume Tehnic:** `deltatech_product_list`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_list
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_list`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul permite definirea de liste de produse — colecții denumite de produse selectate printr-un filtru (domeniu) configurabil. În loc să întrețină manual o listă fixă de produse, utilizatorul descrie odată criteriile (de exemplu „produsele vandabile" sau o anumită categorie), iar lista returnează automat produsele care le îndeplinesc, până la o limită stabilită. Modulul oferă structura de bază pe care alte module o folosesc pentru a expune grupuri de produse, fără să introducă el însuși o funcționalitate vizibilă suplimentară.

#### 2. Funcționalități Cheie

- Definirea de liste de produse, fiecare cu un nume propriu.
- Selectarea produselor pe baza unui filtru (domeniu) configurabil, în loc de selecție manuală.
- Stabilirea unei limite a numărului de produse returnate de listă.
- Listele pot fi arhivate (dezactivate) fără a fi șterse.

#### 3. Dependențe

- `product`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.list`: Listă de produse denumită. Câmpuri principale: `name` (denumire), `products_domain` (filtrul de tip domeniu care selectează produsele, implicit `[["sale_ok", "=", True]]`), `limit` (numărul maxim de produse, implicit 80), `active` (arhivare) și `company_id` (compania).

**Vizualizări**

- `view_product_list_tree`: Vizualizare listă cu denumirea listelor de produse.
- `view_product_list_form`: Vizualizare formular pentru configurarea unei liste — denumire, filtru de produse (widget `domain` pe `product.product`) și limită; afișează un indicator „Archived" pentru listele dezactivate.
- `action_product_list` / `menu_product_list`: Acțiune și element de meniu „Product List" plasat în catalogul de produse din Vânzări (`sale.product_menu_catalog`).

#### 5. Conexiuni

- [deltatech_feed](../deltatech_feed/index.md): folosește listele de produse definite aici ca sursă de produse pentru generarea fluxurilor (feed-uri); depinde direct de acest modul.
