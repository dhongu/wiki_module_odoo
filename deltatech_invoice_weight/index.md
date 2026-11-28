# Invoice Weight (localizat la `deltatech_invoice_weight/index.md`)

- **Nume Tehnic:** `deltatech_invoice_weight`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_weight
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_weight`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul afișează greutatea netă și brută totală a mărfurilor pe comenzile de vânzare, comenzile de achiziție și facturi, și o tipărește pe factură. Este util pentru documentele de transport și pentru cererile clienților.

#### 2. Funcționalități Cheie

- **Greutăți pe documente:** câmpurile **Gross Weight** și **Net Weight** pe comenzile de vânzare și de achiziție (fila nouă **Weight**) și pe facturi (fila *Other Info*, după *Fiscal Position*); facturile au în plus **Package Weight**, completat manual.
- **Calcul la crearea documentului:** suma pe liniile de produs, cu cantitatea convertită în unitatea de măsură a produsului și înmulțită cu greutatea produsului; greutatea brută vine din câmpul standard **Weight** (convertit în kg dacă se lucrează în livre), cea netă din `l10n_ro_net_weight`, câmp pe care modulul nu-l afișează pe produs (îl afișează, de ex., localizarea română de stoc).
- **Totaluri editabile:** câmpurile pot fi corectate manual.
- **Greutate pe factura tipărită:** dacă factura are greutate brută, greutățile brută și netă se tipăresc sub comunicarea de plată.
- **Configurare:** greutatea se setează pe produs (fila *Inventory*), iar unitatea (kg sau livre) în *Inventory > Configuration > Settings*.
- Limitări: greutățile se calculează o singură dată, la creare (liniile modificate ulterior nu le actualizează); nu apar în rapoartele de analiză; pe factura tipărită greutatea netă are eticheta „New weight".

#### 3. Dependențe

- `account`
- `purchase`
- `stock`
- `sale`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): `weight`, `weight_net`, `weight_package` și calculul greutăților la creare (`_compute_weights`).
- `sale.order` și `purchase.order` (extinse): `weight_gross` și `weight_net`, calculate la creare.
- `product.template` (extins): câmpul `l10n_ro_net_weight`.
- `product.product` (extins): `_get_line_weights`, greutatea unei linii în funcție de cantitate și unitate.

**Vizualizări**

- `view_move_form`, `view_purchase_form`, `view_sale_form`: adaugă câmpurile de greutate pe factură, comanda de achiziție și comanda de vânzare.
- `views/invoice_report.xml`: extinde raportul tipărit al facturii cu greutățile.

#### 5. Conexiuni

Nu au fost identificate conexiuni cu alte module documentate în wiki.
