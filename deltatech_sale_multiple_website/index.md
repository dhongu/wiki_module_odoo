# eCommerce Qty Multiple (localizat la `deltatech_sale_multiple_website/index.md`)

- **Nume Tehnic:** `deltatech_sale_multiple_website`
- **Versiune:** `20.0.1.1.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_multiple_website`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_multiple_website`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde regulile de cantitate minimă și de multiplu de vânzare (definite de [deltatech_sale_multiple](../deltatech_sale_multiple/index.md)) și pe canalul eCommerce. Restricțiile pot fi aplicate doar coșurilor de pe website sau global, iar restricțiile active sunt afișate pe pagina produsului și în coș, astfel încât clientul vede imediat ce cantități poate comanda. Cantitatea din coș este normalizată înainte ca Odoo să verifice stocul; dacă stocul limitează cererea, coșul revine la cea mai mare cantitate disponibilă care respectă ambele reguli.

#### 2. Funcționalități Cheie

- Reguli de cantitate aplicate doar comenzilor de pe website sau și ofertelor din backend, prin bifa **Website Check Quantity** de pe produs (activă implicit); în tabul **Sales**, grupul **Quantity**, se setează **Qty Multiple** și **Qty Minim**.
- Afișarea restricțiilor (**Min** și **Multiple of**) sub butonul de adăugare în coș, cu pictogramă informativă care explică fiecare regulă.
- Afișarea acelorași reguli sub numele produsului în coș.
- Reîmprospătarea restricțiilor la schimbarea variantei; regulile se setează pe fiecare variantă.
- Rotunjirea cantității din coș mai întâi la minim, apoi la următorul multiplu (130 cerute devin 150).
- Când stocul limitează cantitatea, coșul păstrează cea mai mare cantitate disponibilă care respectă ambele reguli; sub minim, produsul nu se adaugă.
- Comenzile venite de pe website păstrează regulile și la editarea în backend.

#### 3. Dependențe

- [deltatech_sale_multiple](../deltatech_sale_multiple/index.md)
- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.template`: câmpul `check_min_website` și informațiile de combinație transmise în frontend (minim, multiplu, precizie).
- `product.product`: `_should_enforce_sale_quantity_rules` dezactivă verificarea în afara website-ului când `check_min_website` este activ.
- `sale.order`: `_verify_updated_quantity` normalizează cantitatea înainte de verificările standard de stoc.
- `sale.order.line`: `_prepare_quantity_rule_values` transmite `website_id` al comenzii la evaluarea regulilor.

**Vizualizări**

- `product_qty_restrictions` (`views/templates.xml`): extinde `website_sale.cta_wrapper` cu minimul și multiplul, plus popover.
- `cart_line_description_following_lines`: restricțiile pe linia din coș.
- `product_template_form_view` / `product_variant_easy_edit_view`: câmpul `check_min_website` pe formularul produsului și al variantei.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, cron sau acțiuni server.

#### 5. Conexiuni

- [deltatech_sale_multiple](../deltatech_sale_multiple/index.md): definește minimul și multiplul la nivel de produs; acest modul le extinde pe eCommerce.
- `website_sale_stock`: legarea stocului de vânzarea pe website; coșul se recalibrează când stocul limitează cererea.
