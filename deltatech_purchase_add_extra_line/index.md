# Purchase Add Extra Line (localizat la `deltatech_purchase_add_extra_line/index.md`)

- **Nume Tehnic:** `deltatech_purchase_add_extra_line`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_add_extra_line`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_add_extra_line`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul introduce un proces automat de adăugare a unor linii suplimentare (de exemplu taxe de serviciu, costuri de manipulare sau produse adiacente) pe comenzile de achiziție din Odoo. Este conceput pentru a ajuta echipele de aprovizionare să aplice consecvent costuri sau articole suplimentare în funcție de produsele principale comandate, reducând erorile de introducere manuală și asigurând că toate costurile obligatorii sunt incluse în fiecare comandă relevantă.

#### 2. Funcționalități Cheie

- **Produse extra configurabile**: permite definirea unui *produs extra* direct pe șablonul de produs și adăugarea automată a liniei suplimentare ori de câte ori produsul principal este introdus într-o comandă de achiziție.
- **Logică flexibilă de prețuri**: prețul unitar al liniei extra poate fi calculat ca *procent* din prețul produsului principal; dacă procentul este zero, sistemul folosește prețul de listă standard (*List Price*) al produsului extra.
- **Eficiență în aprovizionare**: reduce erorile de introducere manuală și garantează includerea tuturor costurilor sau articolelor suplimentare obligatorii.
- **Utilizare**: pe fișa produsului (Achiziție > Produse) se configurează *Extra Product*, *Percentage* și cantitatea; la crearea unei comenzi de achiziție și adăugarea produsului principal, linia extra este generată automat ca linie separată cu prețul precalculat.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpurile `extra_product_id` (produsul extra asociat), `extra_percent` (procentul aplicat la prețul produsului principal) și `extra_qty` (cantitatea liniei extra, implicit 1.0).
- `purchase.order` (extins): logica de adăugare automată a liniilor extra pe comanda de achiziție.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs cu grupul „Extra Line” (câmpurile `extra_product_id`, `extra_percent`, `extra_qty`) în zona de achiziție.
- `purchase_order_form`: extinde formularul comenzii de achiziție, expunând câmpul tehnic `line_uuid` pe liniile comenzii (coloană invizibilă) pentru corelarea liniilor extra.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`. Automatizarea se realizează prin logica de model la modificarea liniilor comenzii.

#### 5. Conexiuni

- `deltatech_sale_add_extra_line`: modul soră care aplică același mecanism de linii suplimentare pe comenzile de vânzare (Sales) în loc de achiziții.
