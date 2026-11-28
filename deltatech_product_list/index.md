# Liste de Produse (localizat la `deltatech_product_list/index.md`)

- **Nume Tehnic:** `deltatech_product_list`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_list
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_list`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Fluxurile de produse (feed-urile) și exporturile similare au nevoie de o listă de produse definită printr-o regulă, care rămâne la zi când se adaugă produse. Modulul păstrează o astfel de regulă ca *Listă de produse* reutilizabilă, citită de alte module.

#### 2. Funcționalități Cheie

- **Regulă, nu produse**: o listă are denumire, un filtru de produse (*Produse*) și o *Limită*. Filtrul se construiește cu editorul de domeniu pe variante de produs; o listă nouă pornește cu filtrul pe produsele vandabile (`sale_ok`).
- **Limită**: numărul maxim de produse, implicit 80. Modulul nu o aplică el însuși; o aplică modulul care folosește lista.
- **Arhivare**: lista poate fi arhivată, iar formularul afișează atunci panglica *Arhivat*.
- **Companie**: lista nouă primește compania curentă; o regulă multi-companie arată listele companiilor active și pe cele fără companie.
- Meniul *Product List* se află în catalogul de produse din Vânzări. Toți utilizatorii interni pot citi listele; utilizatorii din `sales_team.group_sale_salesman` le pot crea, modifica și șterge.

#### 3. Dependențe

- `product`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.list`: `name`, `products_domain` (filtrul, implicit `[["sale_ok", "=", True]]`), `limit` (implicit 80), `active`, `company_id`.

**Vizualizări**

- `views/product_list_view.xml`: lista, formularul (widget de domeniu pe `product.product`, panglica *Arhivat*), acțiunea și meniul din catalogul de produse din Vânzări.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_feed](../deltatech_feed/index.md): citește filtrul și limita listelor definite aici ca sursă de produse pentru fluxuri.
