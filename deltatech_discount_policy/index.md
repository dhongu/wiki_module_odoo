# Deltatech Discount Policy (localizat la `deltatech_discount_policy/index.md`)

- **Nume Tehnic:** `deltatech_discount_policy`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_discount_policy](https://github.com/dhongu/deltatech/tree/19.0/deltatech_discount_policy)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_discount_policy`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul readuce în Odoo 19 politica de discount din Odoo 17, oferind posibilitatea de a alege cum sunt afișate reducerile pe comenzile de vânzare. Standardul Odoo elimină în versiunile mai noi opțiunea de a alege între prețul cu discount inclus și afișarea prețului public plus procentul de discount — acest modul restaurează acel comportament, util mai ales pentru companiile migrate din Odoo 17 care doresc să-și păstreze modul de prezentare a prețurilor către clienți.

#### 2. Funcționalități Cheie

- **Restaurarea selecției politicii de discount**: adaugă câmpul `discount_policy` pe lista de prețuri (Pricelist), cu două opțiuni:
    - **Discount inclus în preț**: prețul unitar de pe linia comenzii de vânzare este prețul final, redus, iar câmpul de discount rămâne 0.
    - **Afișează prețul public și discountul către client**: prețul unitar afișează prețul public (de bază), iar procentul de discount este evidențiat explicit.
- **Suport pentru reguli de preț fix**: restaurează comportamentul din Odoo 17 pentru regulile de tip preț fix — atunci când politica este "afișează prețul public și discountul", modulul calculează procentul de discount echivalent chiar și pentru regulile cu preț fix, astfel încât clientul vede prețul original și reducerea aplicată.
- **Parcurgerea lanțului de reguli din lista de prețuri**: identifică corect prețul de bază urmărind lanțul de reguli al listei de prețuri (inclusiv liste de prețuri bazate pe alte liste de prețuri), replicând logica disponibilă în Odoo 17.
- **Transparență îmbunătățită**: oferă flexibilitate în modul de prezentare a prețurilor către clienți, comportament care a fost modificat în versiunile standard mai noi ale Odoo.

#### 3. Dependențe

- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.pricelist` (extindere): adaugă câmpul `discount_policy` (selecție, implicit `with_discount`) care controlează modul de afișare a reducerilor pentru toate regulile listei de prețuri respective.
- `product.pricelist.item` (extindere): suprascrie `_show_discount()` și `_compute_price_before_discount()` pentru a respecta politica de discount a listei de prețuri și pentru a calcula prețul de bază inclusiv pentru regulile de tip preț fix, parcurgând lanțul de liste de prețuri de bază.
- `sale.order.line` (extindere): suprascrie `_get_display_price_ignore_combo()` și `_compute_discount()` pentru a determina prețul afișat și procentul de discount pe linia comenzii de vânzare, în funcție de politica listei de prețuri aplicate.

**Vizualizări**

- `product_pricelist_view_inherit`: extinde formularul standard al listei de prețuri (`product.product_pricelist_view`) adăugând câmpul `discount_policy` (widget `radio`) în grupul de setări ale listei de prețuri.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `sale`: liniile comenzii de vânzare (`sale.order.line`) folosesc politica de discount pentru a decide dacă afișează prețul public cu discount sau prețul deja redus.
- `product`: listele de prețuri (`product.pricelist`) și regulile acestora (`product.pricelist.item`) sunt extinse pentru a susține noua politică de discount.
