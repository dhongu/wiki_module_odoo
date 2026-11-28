# Romania - Nondeductible VAT (localizat la `l10n_ro_nondeductible_vat/index.md`)

- **Nume Tehnic:** `l10n_ro_nondeductible_vat`
- **Versiune:** `20.0.0.4.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_nondeductible_vat
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_nondeductible_vat`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite înregistrarea TVA-ului nedeductibil, atât din facturi, cât și din operațiuni de stoc (consum, minus de inventar). Ajută contabilitatea să reflecte corect partea de TVA care nu se poate deduce, mutând-o pe conturi de cheltuială dedicate.

#### 2. Funcționalități Cheie

- Taxă marcată ca nedeductibilă, selectabilă pe linia facturii, pe mișcarea de stoc de consum sau pe linia de minus de inventar.
- Procent de nedeductibilitate pe linie (facturi, mișcări de stoc, stoc cantitativ), pentru TVA parțial nedeductibil.
- Cont nedeductibil asociat contului de TVA și etichetă (tag) de cont corespondentă, pentru generarea automată a liniilor de TVA nedeductibil.
- Opțiune pe linia de repartizare a taxei pentru excluderea sumei din valoarea stocului.
- Câmpuri adăugate în formularul facturii, al transferului de stoc și al liniilor de inventar.
- Recalcularea la reconcilierea parțială a plăților, în cazul TVA la încasare.

#### 3. Dependențe

- `l10n_ro_stock_account`
- [l10n_ro_vat_on_payment](../l10n_ro_vat_on_payment/index.md)

#### 4. Componente Cheie

**Modele**

- `account.tax`: indicator `l10n_ro_is_nondeductible`.
- `account.account` / `account.account.tag`: cont și etichetă nedeductibile asociate.
- `account.move.line`: procent nedeductibil și legătura către linia de TVA nedeductibil generată.
- `account.tax.repartition.line`: indicator de excludere din stoc.
- `stock.move` / `stock.quant`: taxă, procent și utilizare nedeductibilă pe consum și minus de inventar.
- `account.partial.reconcile`: ajustări la reconcilierea parțială.

**Vizualizări**

- `view_account_form`, `account_tag_view_form`: cont și etichetă nedeductibile.
- `view_move_form`, `view_move_line_tree`: câmpuri pe factură.
- `view_picking_add_nondeductible_vat_form`, `view_inventory_line_add_nondeductible_vat_tree`: câmpuri pe transfer și inventar.
- `account_tax_repartition_line_tree`: excluderea din stoc.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_vat_on_payment](../l10n_ro_vat_on_payment/index.md): TVA la încasare, cu care se combină la reconcilierea parțială.
- `l10n_ro_stock_account`: contabilitatea mișcărilor de stoc în care se aplică TVA-ul nedeductibil.
