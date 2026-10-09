# Romania - Terrabit - Picking batch Report (localizat la `l10n_ro_stock_picking_batch_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_picking_batch_report`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_picking_batch_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_picking_batch_report`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă un raport de livrare (aviz) care se tipărește direct dintr-un lot de transfer (batch picking). În loc să emiți câte un aviz pentru fiecare transfer, obții un singur document care însumează produsele din toate transferurile lotului, cu valoarea lor, pentru destinatarul comun.

#### 2. Funcționalități Cheie

- Raport PDF „Delivery” (aviz de livrare) disponibil în meniul Tipărire al lotului de transfer (`stock.picking.batch`).
- Antet cu datele expeditorului (companie, depozit, adresă, CIF, NRC) și ale destinatarului (preluat de pe primul transfer din lot, cu adresă, CIF și NRC).
- Titlu „Delivery of goods” cu numele lotului și data programată a acestuia.
- Tabel cu produsele lotului, agregate pe produs: cantitate totală, preț unitar mediu și valoare, plus totalul general în moneda companiei.
- Prețul se calculează din linia comenzii de achiziție sau de vânzare asociată mișcării de stoc.
- Bloc de semnături preluat din raportul de aviz din `l10n_ro_stock_picking_report`.
- Este incompatibil (`excludes`) cu `l10n_ro_stock_picking_comment_template`.

#### 3. Dependențe

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md)
- `stock_picking_batch`

#### 4. Componente Cheie

**Modele**

- Nu definește modele proprii; extinde doar `stock.picking.batch` prin acțiunea de raport.

**Vizualizări**

- `report_batch_address`: șablon QWeb pentru blocul de adrese expeditor/destinatar.
- `report_batch_delivery`: șablonul principal al avizului pentru lot.

**Acțiuni Automate / Acțiuni Server**

- `action_report_delivery_batch`: `ir.actions.report` (qweb-pdf) legat de `stock.picking.batch`.

#### 5. Conexiuni

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): oferă raportul de aviz pe transfer și blocul de semnături refolosit aici.
