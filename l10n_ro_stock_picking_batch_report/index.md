# Romania - Batch Delivery Note

- **Nume Tehnic:** `l10n_ro_stock_picking_batch_report`
- **Versiune:** `20.0.0.0.8`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_picking_batch_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_picking_batch_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă pe lotul de transferuri raportul **Aviz**, un aviz de însoțire a mărfii pentru tot transportul, în locul câte unui aviz pe livrare. Formatul este cel al avizului din `l10n_ro_picking_report`.

#### 2. Funcționalități Cheie

- Antet cu firma, depozitul, CIF și NRC, și cu destinatarul (cel al primei livrări din lot; modulul nu verifică dacă toate livrările au același destinatar).
- O linie pe produs, cu cantitățile cumulate din toate livrările lotului și unitatea de măsură (afișată doar cu setarea Unități de măsură activă).
- Preț unitar și valoare luate din comenzile de vânzare sau de achiziție, plus total.
- Bloc de semnături: întocmit, delegat, mijloc de transport, recepție.
- Se tipărește din lot, din meniul de rapoarte; incompatibil (`excludes`) cu `l10n_ro_stock_picking_comment_template`.

#### 3. Dependențe

- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md)
- `stock`

#### 4. Componente Cheie

**Modele**

- Nu definește modele noi; lucrează pe `stock.picking.batch`.

**Vizualizări**

- `report_batch_delivery`, `report_batch_address`: șabloanele QWeb ale avizului pe lot.

**Acțiuni Automate / Acțiuni Server**

- `action_report_delivery_batch`: acțiunea de raport legată de `stock.picking.batch`.

#### 5. Conexiuni

- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md): sursa formatului avizului.
