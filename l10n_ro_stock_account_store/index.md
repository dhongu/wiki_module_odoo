# România - Contabilitate stocuri la magazin (preț de vânzare)

- **Nume Tehnic:** `l10n_ro_stock_account_store`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_account_store
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_store`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul ține contabilitatea mărfurilor păstrate la preț de vânzare, cu TVA inclus, în locațiile de tip magazin (comerț cu amănuntul) ale firmelor din România. Pe lângă nota contabilă obișnuită a stocului la cost, fiecare mișcare care intră sau iese dintr-o astfel de locație primește o notă separată pentru adaosul comercial (378) și pentru TVA neexigibilă (4428), astfel încât soldul contului 371 să reflecte prețul de vânzare.

#### 2. Funcționalități Cheie

- O locație marcată ca **Magazin** (câmpul *Romania - Merchandise type*) păstrează marfa la preț de vânzare, TVA inclus.
- Recepție de la furnizor cu factură: 371 = 401 (cost) și 4426 = 401 (TVA) din factură, plus adaosul 371 = 378 și TVA neexigibilă 371 = 4428.
- Recepție cu aviz, fără factură: la recepție 371 = 408, apoi 371 = 378 și 371 = 4428; la sosirea facturii 408 = 401 și 4426 = 401.
- Transfer din depozit (la cost) în magazin: transferul intern la cost, apoi 371 = 378 și 371 = 4428.
- Ieșiri din magazin (livrare, consum, minus de inventar, transfer către depozit): 378 = 371 și 4428 = 371, alături de ieșirea la cost.
- Retururile (către furnizor, de la client) stornează în roșu adaosul și TVA din mișcarea returnată, la prețul ei de vânzare.
- Prețul de vânzare se ia de pe produs (*Preț de vânzare* și *Taxe client*) la intrarea în magazin; același preț este folosit și de NIR-ul la preț de vânzare (preț înghețat pe mișcare, apoi lista de prețuri a magazinului, apoi prețul produsului). La ieșire se eliberează adaosul și TVA la prețul ultimei intrări a produsului în magazin, deci 378 și 4428 se închid chiar dacă prețul s-a schimbat între timp.
- Sumele rămân pe mișcarea de stoc (*Store Sale Amount*, *Store Markup*, *Store Uneligible VAT*) și sunt vizibile în grupul **Store Valuation** din *Inventar > Raportare > Istoric mișcări*, inclusiv ca coloane opționale în listă, împreună cu nota contabilă.
- Configurare: contul de TVA neexigibilă (4428) în *Contabilitate > Configurare > Setări*; pe categoria de produse contul de adaos (378) și, opțional, un cont dedicat de TVA neexigibilă (ex. 4428.02), cu evaluare perpetuă; pe produse prețul de vânzare și taxele client.
- Limitări (de tratat în afara modulului): modificarea prețului de vânzare pentru marfa deja în magazin cere un raport de modificare de preț (371 = 378 / 4428 pe diferență), altfel rămân solduri reziduale pe 378 și 4428; când factura vine cu alt cost decât recepția, stocul se corectează (371 = 401), dar adaosul nu, deci diferența se regularizează manual pe 378.
- În afara scopului: eliberarea lunară a adaosului cu coeficientul K, vânzările prin Point of Sale, rapoartele de modificare de preț și raportul de inventar al magazinului la preț de vânzare.

#### 3. Dependențe

- `l10n_ro_stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.move` (extins): câmpurile `l10n_ro_store_sale_amount`, `l10n_ro_store_markup_amount`, `l10n_ro_store_tax_amount`, `l10n_ro_store_account_move_id`; determină direcția intrare/ieșire din magazin, calculează sumele și generează nota contabilă separată pentru 378 / 4428.
- `stock.location` (extins): câmpul `l10n_ro_merchandise_type` (tip marfă, valoarea *Magazin*).
- `product.category` (extins): conturile `l10n_ro_property_store_markup_account_id` (378) și `l10n_ro_property_store_uneligible_tax_account_id` (TVA neexigibilă).
- `product.template` (extins): suprascrie `_get_product_accounts` pentru a expune conturile de magazin.

**Vizualizări**

- `view_move_form_store` / `view_move_tree_store`: grupul *Store Valuation* și coloanele de sume pe mișcarea de stoc.
- `view_location_store_form`, `view_location_tree_store`, `view_location_search_store`: tipul de marfă pe locație (formular, listă, căutare).
- `view_product_category_store_form`: conturile de adaos și TVA neexigibilă pe categoria de produse.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate sau acțiuni server. Există o migrare `19.0.1.0.0/post-migration.py`.

#### 5. Conexiuni

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): NIR la preț de vânzare, care folosește același preț ca nota de adaos din magazin (aliniat din 19.0.1.0.1).
