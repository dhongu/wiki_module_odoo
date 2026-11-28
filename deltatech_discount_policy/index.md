# Deltatech Discount Policy (localizat la `deltatech_discount_policy/index.md`)

- **Nume Tehnic:** `deltatech_discount_policy`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_discount_policy
- **Cale Locală:** `odoo-addons/deltatech/deltatech_discount_policy`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul readuce politica de discount din Odoo 17, oferind posibilitatea de a alege cum sunt afișate reducerile pe comenzile de vânzare. Standardul Odoo a eliminat opțiunea de a alege între prețul cu discount inclus și afișarea prețului public plus procentul de discount; modulul restaurează acel comportament, util mai ales companiilor migrate din Odoo 17 care vor să-și păstreze modul de prezentare a prețurilor către clienți.

#### 2. Funcționalități Cheie

- **Restaurarea selecției politicii de discount**: adaugă câmpul `discount_policy` pe lista de prețuri, cu două opțiuni:
    - **Discount inclus în preț**: prețul unitar de pe linia comenzii de vânzare este prețul final, redus, iar câmpul de discount rămâne 0.
    - **Afișează prețul public și discountul către client**: prețul unitar afișează prețul public (de bază), iar procentul de discount este evidențiat explicit.
- **Suport pentru reguli de preț fix**: cu politica „afișează prețul public și discountul”, modulul calculează procentul de discount echivalent și pentru regulile cu preț fix, astfel încât clientul vede prețul original și reducerea aplicată.
- **Parcurgerea lanțului de reguli din lista de prețuri**: identifică corect prețul de bază urmărind lanțul de reguli, replicând logica din Odoo 17.
- **Transparență îmbunătățită**: flexibilitate în modul de prezentare a prețurilor către clienți.

#### 3. Dependențe

- `sale`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.pricelist` (extindere): adaugă câmpul `discount_policy` (selecție, implicit `with_discount`) care controlează afișarea reducerilor pentru regulile listei de prețuri.
- `product.pricelist.item` (extindere): suprascrie `_show_discount()` și `_compute_price_before_discount()` pentru a respecta politica listei și a calcula prețul de bază inclusiv pentru regulile cu preț fix.
- `sale.order.line` (extindere): suprascrie `_get_display_price_ignore_combo()` și `_compute_discount()` pentru prețul afișat și procentul de discount, în funcție de politica listei de prețuri aplicate.

**Vizualizări**

- `product_pricelist_view_inherit`: extinde formularul listei de prețuri adăugând câmpul `discount_policy` (widget `radio`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `sale`: liniile comenzii de vânzare folosesc politica de discount pentru a decide dacă afișează prețul public cu discount sau prețul deja redus.
- `product`: listele de prețuri și regulile lor sunt extinse pentru a susține politica de discount.
