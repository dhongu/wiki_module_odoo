# Sale Add Extra Line (localizat la `deltatech_sale_add_extra_line/index.md`)

- **Nume Tehnic:** `deltatech_sale_add_extra_line`
- **Versiune:** `19.0.1.3.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_add_extra_line`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_add_extra_line`
- **Ultima Ingestie:** `2026-07-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul introduce un proces automat de adăugare a unor linii suplimentare pe comenzile de vânzare din Odoo, în funcție de produsele vândute. Atunci când pe un produs s-a configurat un *produs extra* (grupul „Linie suplimentară" din fila Vânzări), sistemul adaugă automat o linie nouă pe comandă (de exemplu o taxă de serviciu, un accesoriu obligatoriu, costuri de ambalare sau o garanție), calculând cantitatea și prețul pe baza setărilor de pe fișa produsului. Un preț introdus manual pe linia extra este păstrat, iar linia mai poate fi recalculată prin ștergere; comenzile din magazinul online primesc și ele linia suplimentară. Astfel se asigură consecvența proceselor de vânzare și se reduc erorile manuale la adăugarea produselor sau serviciilor complementare în comenzile clienților. Modulul funcționează atât pe comenzile de vânzare obișnuite, cât și — printr-un modul separat — în tranzacțiile din Punctul de Vânzare (Point of Sale).

#### 2. Funcționalități Cheie

- **Adăugare automată a liniei extra**: pentru produsele configurate, sistemul adaugă automat o linie suplimentară pe comanda de vânzare, poziționată direct sub linia principală.
- **Configurare pe șablonul de produs**: produsul extra, procentul de calcul al prețului și multiplicatorul de cantitate se configurează direct pe șablonul de produs (*product template*), în grupul **Linie suplimentară**.
- **Calcul inteligent al prețului**: prețul unitar al liniei extra se calculează din procentul configurat pe produs; dacă procentul este zero, se aplică **recalculul standard Odoo** al prețului (listă de prețuri, valuta comenzii și unitatea de măsură), nu mai prețul de listă brut al produsului.
- **Preț manual păstrat**: un preț introdus manual pe linia extra nu mai este rescris de recalculul automat la orice schimbare a cantității sau a prețului liniei principale. Cantitatea continuă însă să urmeze linia principală. Revenirea la prețul calculat se face prin ștergerea liniei extra — se regenerează la următoarea modificare a comenzii.
- **Detectarea prețului manual pe orice cale**: intervenția manuală este recunoscută prin câmpul tehnic `extra_price_computed` (ultimul preț calculat de modul), deci este detectată și când linia e modificată prin `write()`, import, XML-RPC sau coșul din magazinul online — nu doar din formularul comenzii.
- **Calcul al cantității în funcție de cantitatea principală**: cantitatea produsului extra se calculează pornind de la cantitatea produsului principal și de la un multiplicator configurabil (**Cantitate suplimentară**, implicit 1.0).
- **Actualizare dinamică**: la modificarea cantităților produselor principale, cantitățile produselor extra sunt recalculate și actualizate automat.
- **Ștergere în cascadă**: ștergerea liniei principale șterge automat și linia extra asociată, ca să nu rămână orfană pe comandă.
- **Integrare cu magazinul online**: coșul din e-commerce generează linia suplimentară prin hook-ul `_verify_cart_after_update` (apelat după `_cart_add` și `_cart_update_line_quantity`); linia nu poate fi ștearsă de cumpărător — reapare la următoarea actualizare a coșului, cât timp produsul principal rămâne în coș.
- **Interfață tradusă integral în română** (`i18n/ro.po`): grupul **Linie suplimentară**, câmpurile **Produs suplimentar**, **Procent suplimentar**, **Cantitate suplimentară**.
- **Migrare automată**: la actualizarea de pe o versiune veche, un script de migrare completează `extra_price_computed` pe liniile extra existente, ca să nu fie confundate cu linii cu preț manual.

#### 3. Dependențe

- `sale`
- `website_sale`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpurile `extra_product_id` (produsul adăugat automat ca linie extra), `extra_percent` (procentul din prețul liniei principale folosit la calculul prețului liniei extra; zero = se aplică recalculul standard Odoo pe produsul extra) și `extra_qty` (multiplicatorul de cantitate pentru produsul extra, implicit 1.0).
- `sale.order` (extins): `onchange_order_line` declanșează `check_extra_product()` cu `backend=True` la editarea comenzii în formular; `_verify_cart_after_update` (înlocuiește vechiul `_cart_update`, eliminat în Odoo 19) resincronizează liniile extra după orice actualizare a coșului din `website_sale`, înaintea `super()`, ca prețul livrării și `cart_quantity` din sesiune să țină cont de liniile suplimentare.
- `sale.order.line` (extins): adaugă `line_uuid` (identificator stabil care perechează linia principală cu linia extra generată) și `extra_price_computed` (ultimul preț calculat de modul pe linia extra, folosit pentru a distinge o intervenție manuală de un simplu recalcul de listă de prețuri). Metoda `check_extra_product()` creează/actualizează linia extra și îi recalculează cantitatea; `_has_manual_price()` decide dacă prețul curent a fost tastat de utilizator (nu coincide nici cu `extra_price_computed`, nici cu `technical_price_unit`); `unlink()` șterge în cascadă linia extra perechea liniei principale.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs cu grupul **Linie suplimentară** (`extra_product_id`, `extra_percent`, `extra_qty`) în fila Vânzări.
- `view_order_form_extra`: extinde formularul comenzii de vânzare cu câmpurile tehnice invizibile `line_uuid` și `extra_price_computed` pe liniile comenzii, necesare mecanismului de asociere și de detectare a prețului manual.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`. Automatizarea se realizează prin `onchange` pe liniile comenzii (backend) și prin hook-ul `_verify_cart_after_update` (magazin online).

**Migrări**

- `migrations/19.0.1.1.0/post-migration.py`: după actualizarea la 19.0.1.1.0 (care a introdus reținerea prețului manual), completează `extra_price_computed = price_unit` pe toate liniile extra existente (identificate prin `line_uuid`), altfel ar fi fost considerate tăcut linii cu preț manual și ar fi ieșit din sincronizarea cu prețul liniei principale.

#### 5. Conexiuni

- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md): modul soră care aplică același mecanism de linii suplimentare pe comenzile de achiziție (Purchase) în loc de vânzări.
- [deltatech_sale_add_extra_line_pos](../deltatech_sale_add_extra_line_pos/index.md): duce mecanismul în Punctul de Vânzare (POS) — sincronizează doar cantitatea liniei extra, nu procentul.
- [l10n_ro_sgr](../l10n_ro_sgr/index.md): folosește acest mecanism pentru garanția de ambalaj SGR (produsul extra este garanția, în afara sferei TVA conform art. 315^5 alin. 2 Cod fiscal).
