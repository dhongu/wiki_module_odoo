# Invoice Weight (localizat la `deltatech_invoice_weight/index.md`)

- **Nume Tehnic:** `deltatech_invoice_weight`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_weight
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_weight`
- **Ultima Ingestie:** `2026-11-04`

#### 1. Sumar

Modulul afișează greutatea netă și brută totală a mărfurilor pe comenzile de vânzare, comenzile de achiziție și facturi și tipărește greutățile pe factură, pentru documentele de transport și pentru cererile clienților. Este util companiilor care trebuie să raporteze greutatea articolelor facturate, achiziționate sau vândute.

#### 2. Funcționalități Cheie

- **Greutăți pe documente**: adaugă **Gross Weight** și **Net Weight** pe comenzile de vânzare și de achiziție (într-o filă nouă **Weight**) și pe facturi (în fila *Other Info*, după *Fiscal Position*). Facturile primesc și câmpul **Package Weight**, completat manual.
- **Calcul la crearea documentului**: totalurile sunt suma pe liniile de produs; cantitatea liniei se convertește în unitatea de măsură a produsului și se înmulțește cu greutatea produsului (o duzină dintr-un produs de 2 kg dă 24 kg). Greutatea brută vine din câmpul standard **Weight** al produsului și se convertește în kg când greutățile sunt configurate în livre. Greutatea netă vine din câmpul `l10n_ro_net_weight` al produsului; modulul nu îl afișează pe formularul produsului, ci alte module (de exemplu localizarea română de stoc).
- **Totaluri editabile**: câmpurile de greutate sunt câmpuri obișnuite, deci pot fi corectate manual pe document.
- **Greutate pe factura tipărită**: când factura are greutate brută, greutățile brută și netă se tipăresc sub comunicarea de plată.
- **Configurare**: **Weight** se setează pe fiecare produs, fila *Inventory*; unitatea de greutate (kilograme sau livre) se alege la **Inventar → Configurare → Setări**.
- Limitări: greutățile se calculează o singură dată, la crearea comenzii sau a facturii, deci liniile adăugate sau modificate ulterior nu le actualizează; greutățile nu sunt disponibile în *Analiza facturilor* sau în rapoartele de analiză a vânzărilor și achizițiilor (corecție față de descrierea veche, care promitea analiză pivot); pe factura tipărită greutatea netă apare cu eticheta „New weight".

#### 3. Dependențe

- `account`
- `purchase`
- `stock`
- `sale`

#### 4. Componente Cheie

Funcționalitățile provin din `readme/DESCRIPTION.md`; mai jos sunt reperele confirmate în cod. `readme/ROADMAP.md` descrie retragerea câmpului `l10n_ro_net_weight` (calcul din `product.weight`); clienții care depind de modul: `terrabit_agroamat`, `terrabit_datus`.

**Modele**

- `account.move` (extins): `weight` („Gross Weight”), `weight_net`, `weight_package`; calculul se face la `create`.
- `sale.order` și `purchase.order` (extinse): `weight_gross` și `weight_net`, calculate la `create`.
- `product.template` (extins): definește câmpul `l10n_ro_net_weight`.
- `product.product` (extins): `_get_line_weights(quantity, uom)`, greutatea unei linii.

**Vizualizări**

- `view_move_form`: moștenește `account.view_move_form` și adaugă câmpurile de greutate în *Other Info*.
- `view_sale_form`: moștenește `sale.view_order_form` (fila *Weight*).
- `view_purchase_form`: moștenește `purchase.purchase_order_form` (fila *Weight*).
- `report_invoice_document_weight`: moștenește `account.report_invoice_document` și tipărește greutățile pe factură.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_hide_net_weight](../l10n_ro_hide_net_weight/index.md): ascunde pe formularul produsului câmpul `l10n_ro_net_weight`, din care acest modul citește greutatea netă; valorile rămân și sunt folosite în continuare la calcul.
- `l10n_ro_stock_base`: modul de localizare care afișează câmpul `l10n_ro_net_weight` pe produs.
