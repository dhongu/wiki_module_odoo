# Sale Add Extra Line (localizat la `deltatech_sale_add_extra_line/index.md`)

- **Nume Tehnic:** `deltatech_sale_add_extra_line`
- **Versiune:** `19.0.1.0.9`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_add_extra_line`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_add_extra_line`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul introduce un proces automat de adăugare a unor linii suplimentare pe comenzile de vânzare din Odoo, în funcție de produsele vândute. Atunci când pe un produs s-a configurat un *produs extra*, sistemul adaugă automat o linie nouă pe comandă (de exemplu o taxă de serviciu, un accesoriu obligatoriu, costuri de ambalare sau o garanție), calculând cantitatea și prețul pe baza setărilor de pe fișa produsului. Astfel se asigură consecvența proceselor de vânzare și se reduc erorile manuale la adăugarea produselor sau serviciilor complementare în comenzile clienților. Modulul funcționează atât pe comenzile de vânzare obișnuite, cât și în tranzacțiile din Punctul de Vânzare (Point of Sale).

#### 2. Funcționalități Cheie

- **Adăugare automată a liniei extra**: pentru produsele configurate, sistemul adaugă automat o linie suplimentară pe comanda de vânzare.
- **Configurare pe șablonul de produs**: produsul adăugat în linia extra se configurează direct pe șablonul de produs (*product template*).
- **Calcul inteligent al prețului**: prețul unitar al liniei extra se calculează din procentul configurat pe produs; dacă procentul este zero, prețul folosit este prețul de listă (*List Price*) al produsului adăugat.
- **Calcul al cantității în funcție de cantitatea principală**: cantitatea produsului extra se calculează pornind de la cantitatea produsului principal și de la un multiplicator configurabil.
- **Actualizare dinamică**: la modificarea cantităților produselor principale, cantitățile produselor extra sunt recalculate și actualizate automat.
- **Integrare cu Punctul de Vânzare**: funcționează atât pe comenzile de vânzare standard, cât și în tranzacțiile POS, prin patch-uri JavaScript.

#### 3. Dependențe

- `sale`
- `website_sale`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpurile `extra_product_id` (produsul vândut ca extra), `extra_percent` (procentul folosit la calculul prețului liniei extra) și `extra_qty` (multiplicatorul de cantitate pentru produsul extra, implicit 1.0).
- `sale.order` (extins): logica de adăugare automată a liniilor extra; tratează `_cart_update` pentru integrarea cu website/POS și recalcularea liniilor.
- `sale.order.line` (extins): metoda `check_extra_product` care declanșează crearea/actualizarea liniei extra și gestionarea corectă la ștergerea liniilor (`unlink`).

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs cu câmpurile de configurare a liniei extra (`extra_product_id`, `extra_percent`, `extra_qty`).
- `view_order_form_extra`: extinde formularul comenzii de vânzare pentru a susține mecanismul liniilor extra.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`. Automatizarea se realizează prin logica de model la modificarea liniilor comenzii.

#### 5. Conexiuni

- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md): modul soră care aplică același mecanism de linii suplimentare pe comenzile de achiziție (Purchase) în loc de vânzări.
