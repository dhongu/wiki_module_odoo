# Romania - Stock Accounting tracking

- **Nume Tehnic:** `l10n_ro_stock_account_tracking`
- **Versiune:** `20.0.0.3.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock_account_tracking
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_stock_account_tracking`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaugă un tabel care păstrează rezervările dintre mișcările de stoc pentru produsele evaluate FIFO. Astfel se poate urmări, pentru fiecare ieșire, din ce intrări (mișcări sursă) a fost acoperită, cu cantitatea și valoarea aferentă.

#### 2. Funcționalități Cheie

- Legătură explicită între mișcarea sursă (intrarea) și mișcarea destinație (ieșirea) pentru produsele FIFO.
- Pentru fiecare legătură se păstrează cantitatea și valoarea alocată.
- Informațiile sunt vizibile din vizualizările mișcărilor de stoc (operațiuni detaliate și formularul mișcării).

#### 3. Dependențe

- `l10n_ro_stock_account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.move.tracking`: înregistrare de urmărire între mișcarea sursă și cea destinație, cu cantitate și valoare.
- `stock.move` (extins, cu `l10n.ro.mixin`): relația către înregistrările de urmărire.

**Vizualizări**

- `view_stock_move_operations`: extinde vizualizarea operațiunilor mișcării de stoc.
- `view_move_form`: extinde formularul mișcării de stoc.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `l10n_ro_stock_account`: baza contabilității de stoc pentru România, de care depinde modulul.
