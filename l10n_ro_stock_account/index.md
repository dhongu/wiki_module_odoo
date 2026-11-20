# Romania - Stock Accounting (localizat la `l10n_ro_stock_account/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_account`
- **Versiune:** `19.0.1.17.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/19.0/l10n_ro_stock_account
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_stock_account`
- **Ultima Ingestie:** `2026-11-17`

#### 1. Sumar

Modulul adaptează contabilitatea de stoc din Odoo la cerințele standardelor și reglementărilor contabile românești. Permite configurarea conturilor de stoc pe locații, categorii de produs și depozite și evaluează stocul FIFO separat pe fiecare locație, nu la nivel de companie. Astfel, notele contabile generate de mișcările de stoc (recepții, livrări, transferuri, dropshipping) corespund cu raportul de evaluare a stocului.

#### 2. Funcționalități Cheie

- Configurări contabile specifice pe locație, conturi de evaluare a stocului specifice României, personalizarea conturilor de stoc pe categoria de produs, gestionarea poziției fiscale pe depozit și conturi dedicate operațiunilor de stoc.
- **FIFO pe locație**: pentru produsele cu metoda de cost FIFO, ieșirile se evaluează din stiva FIFO a locației sursă; fiecare ieșire este împărțită automat într-o mișcare pe fiecare strat FIFO. Controlat prin opțiunea de companie `fifo_per_location` (implicit activă pentru companiile din România).
- **Transferuri interne** (și prin locații de tranzit): consumă din stiva locației sursă, intră în stiva locației destinație cu valoarea preluată și generează notă contabilă prin contul de evaluare al locației (sau contul de transfer al companiei, 482, dacă locațiile au același cont). Din 19.0.1.15/1.16, contrapartida unui transfer este mereu contul de stoc al locației destinație (fără postări pe cheltuieli 607); notele deja înregistrate nu se modifică.
- **Compensarea stocului negativ** pentru produsele FIFO: ieșirea fără intrare corespunzătoare se evaluează la `standard_price`, iar la recepția ulterioară valoarea reală este alocată (FIFO) peste ieșirile în așteptare, cu generarea unei note de corecție (variație/cheltuială față de contul de stoc), legată de mișcarea de intrare. Operațiunea este idempotentă. Controlat prin `fifo_location_negative_compensation` (implicit activă pentru România).
- **Dropshipping**: livrarea directă furnizor → client este evaluată și contabilizată simetric cu o livrare obișnuită (debit cheltuială 607 / credit stoc 371; retururile `dropshipped_return` în stornare, cu sumă negativă). 408 nu se aplică dropship-ului. Se aplică mișcărilor validate după instalarea corecției; istoricul necesită regularizare separată.
- Dropshipping-ul unui produs nu influențează valoarea stocului real al aceluiași produs (nici FIFO, nici cost mediu).
- **Performanță**: indecși parțiali pe `stock_move` pentru stiva FIFO și pentru mișcările cu cantitate negativă în așteptare, plus cache pe cerere pentru calculul valorii în rapoartele mari de evaluare.

#### 3. Dependențe

- `stock_dropshipping`
- `l10n_ro_stock`

#### 4. Componente Cheie

**Modele**

Extinderi ale modelelor standard (din `models/`): `account.account`, `account.move`, `account.move.line`, `product.category`, `product.template`, `res.company`, `stock.location`, `stock.move`, `stock.picking`, `stock.warehouse`, plus logica FIFO în `models/fifo/`.

- `res.company`: opțiunile `fifo_per_location` și `fifo_location_negative_compensation`.
- `stock.move`: câmpurile `fifo_neg_pending_qty` și `fifo_neg_origin_value` pentru compensarea stocului negativ.
- `account.move`: câmpul `fifo_neg_origin_move_id` pentru trasabilitatea corecțiilor.

**Vizualizări**

Extinderi de vizualizări pentru cont contabil, categorie de produs, produs, companie, locație, mișcare de stoc, transfer și depozit (`views/*.xml`).

**Acțiuni Automate / Acțiuni Server**

Nu are.

#### 5. Conexiuni

- `l10n_ro_stock_account_date`: dată contabilă pentru mișcările de stoc, depinde de acest modul.
- `l10n_ro_stock_account_tracking`: urmărire contabilă, depinde de acest modul.
- `l10n_ro_stock_report`: raport de stoc, depinde de acest modul.
- `l10n_ro_nondeductible_vat`: TVA nedeductibil, depinde de acest modul.
