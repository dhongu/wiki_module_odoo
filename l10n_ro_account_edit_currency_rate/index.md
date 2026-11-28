# Romania - Invoice Edit Currency Rate

- **Nume Tehnic:** `l10n_ro_account_edit_currency_rate`
- **Versiune:** `20.0.0.5.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_account_edit_currency_rate
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_account_edit_currency_rate
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite editarea cursului valutar folosit pentru calculul debitului și creditului liniilor de factură, util când cursul trebuie corectat manual față de cel implicit.

#### 2. Funcționalități Cheie

- Cursul facturii (`invoice_currency_rate`) devine editabil în formularul facturii.
- La schimbarea monedei, a datei facturii sau a cursului, prețurile liniilor se recalculează pentru companiile din România.
- Pentru facturile provenite din comenzi de vânzare, prețul se convertește din moneda comenzii; liniile de avans dedus în factura finală folosesc prețul facturii de avans postate, astfel încât suma dedusă să corespundă celei deja facturate.

#### 3. Dependențe

- `account`
- `sale_management`

#### 4. Componente Cheie

**Modele**

- `account.move`: onchange `_onchange_currency_rate_to_invoice_line`, care recalculează liniile.
- `sale.order.line`: extins pentru transferul prețului în factură.

**Vizualizări**

- `l10n_ro_view_move_form_edit_currency`: face editabile câmpul și widgetul de curs din formularul facturii.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `sale_management`: comenzile de vânzare sunt sursa prețurilor convertite.
