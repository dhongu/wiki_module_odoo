# Romania - Stock Accounting Reception In progress

- **Nume Tehnic:** `l10n_ro_stock_account_reception_in_progress`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock_account_reception_in_progress
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_stock_account_reception_in_progress
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite înregistrarea recepțiilor în curs: marfa recepționată înainte de sosirea facturii furnizorului, pe baza unei comenzi de achiziție marcate corespunzător. Pentru a păstra corectitudinea contabilă, cantitatea din facturile legate de o astfel de comandă nu mai poate fi modificată.

#### 2. Funcționalități Cheie

- Marcaj `Recepție în curs` pe comanda de achiziție, propagat pe picking-urile asociate.
- Restricție: nu se poate schimba cantitatea din liniile de factură legate de comenzi marcate ca recepții în curs.
- Câmpul apare în formularul comenzii de achiziție.

#### 3. Dependențe

- `l10n_ro_stock_price_difference`

#### 4. Componente Cheie

**Modele**

- `purchase.order`: câmpul `l10n_ro_reception_in_progress`.
- `stock.picking`: preia marcajul de recepție în curs.
- `account.move.line`: blochează modificarea cantității pe liniile legate de recepții în curs.

**Vizualizări**

- `purchase_order_form`: marcajul în comanda de achiziție.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md): conturile pentru recepții în curs (câmp definit pe contul contabil).
