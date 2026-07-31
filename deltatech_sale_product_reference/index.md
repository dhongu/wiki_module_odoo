# Sale Product Reference (localizat la `deltatech_sale_product_reference/index.md`)

- **Nume Tehnic:** `deltatech_sale_product_reference`
- **Versiune:** `19.0.1.2.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_product_reference`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_product_reference`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul preia automat referința proprie a clientului pentru un produs (codul/numele de furnizor înregistrat pe fișa produsului) și o folosește ca descriere a liniei pe comanda de vânzare, în locul denumirii interne a produsului. Astfel, atunci când un client este el însuși listat drept furnizor al unui produs (printr-un rând „Vendor Pricelists” din fișa produsului), oferta trimisă către el va folosi automat propriul lui cod/nume de produs, eliminând căutarea manuală și reducând erorile de comunicare pe documentele de vânzare.

#### 2. Funcționalități Cheie

- La adăugarea sau schimbarea unui produs pe o linie de comandă de vânzare, verifică automat dacă partenerul comenzii se regăsește printre furnizorii produsului respectiv (`product.supplierinfo`).
- Dacă găsește o potrivire, descrierea liniei folosește numele/codul de produs specific acelui furnizor (clientul propriu-zis), în loc de denumirea internă a produsului.
- Revine la descrierea standard a produsului atunci când clientul comenzii nu este furnizor înregistrat pentru acel produs sau comanda nu are încă un client stabilit.
- Descrierea se regenerează exact ca în comportamentul standard Odoo: la schimbarea produsului sau a clientului comenzii; editările manuale nu sunt suprascrise decât de aceste două declanșatoare.
- Reaplică logica și pentru liniile create cu descriere explicită (de exemplu import EDI/API), care altfel ar ocoli mecanismul standard de calcul al descrierii.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order.line`: extins pentru a determina furnizorul de referință (`_get_reference_seller`, pe baza `product.product._select_seller()` cu partenerul comenzii) și pentru a suprascrie `_get_sale_order_line_multiline_description_sale()`, construind descrierea liniei din perspectiva acelui furnizor (`seller_id` în context) când există o potrivire. Adaugă și `order_partner_id` ca dependență a `_compute_name`, astfel încât schimbarea clientului pe comandă retrigger-uiește descrierea, la fel ca schimbarea produsului. Suprascrie și `create()` pentru a reaplica referința de furnizor pe liniile create cu `name` explicit (import EDI/API), care în mod normal ocolesc `_compute_name`.

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): la importul comenzilor EDI, liniile create au deja o descriere explicită (`name`) și un `product.supplierinfo` asociat clientului-furnizor; mecanismul de reaplicare a referinței din `create()` al acestui modul acoperă exact acest caz, ocolit de `_compute_name`.
