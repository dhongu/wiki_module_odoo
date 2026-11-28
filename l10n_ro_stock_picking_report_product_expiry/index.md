# Romania - Picking Reports - Product Expiry (localizat la `l10n_ro_stock_picking_report_product_expiry/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_picking_report_product_expiry`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_picking_report_product_expiry
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_picking_report_product_expiry`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul de legătură care adaugă data de expirare a produselor pe rapoartele de livrare și transfer din localizarea românească. Când produsele sunt urmărite pe loturi cu dată de expirare, bonul de livrare tipărit arată valabilitatea fiecărui lot, atât pentru expeditor, cât și pentru client. Se instalează automat când sunt prezente raportul de picking românesc și modulul standard de expirare a produselor.

#### 2. Funcționalități Cheie

- Adaugă coloana „Expiration Date" în raportul de livrare/transfer (`report_delivery`) din `l10n_ro_picking_report`.
- Preia data din lotul asociat fiecărei linii de mișcare (`move_line.lot_id.expiration_date`).
- Coloana apare doar dacă cel puțin o linie are lot cu dată de expirare și doar pentru utilizatorii din grupul `product_expiry.group_expiry_date_on_delivery_slip`.
- Se instalează automat (`auto_install`), fără configurare suplimentară.

#### 3. Dependențe

- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md)
- `product_expiry`

#### 4. Componente Cheie

> Notă: `readme/DESCRIPTION.md` este gol, deci informațiile provin din `__manifest__.py` și cod. Modulul nu definește modele, formulare/liste sau acțiuni automate, doar un template QWeb.

**Vizualizări (rapoarte QWeb)**

- `report_delivery` (moștenit din `l10n_ro_picking_report.report_delivery`): adaugă antetul de coloană și celula cu data de expirare a lotului.

#### 5. Conexiuni

- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md): raportul de bază pe care modulul îl extinde cu data de expirare.
- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): suita de rapoarte de picking românești înrudită.
- `product_expiry`: modulul standard care introduce data de expirare pe loturi și grupul de drepturi folosit pentru afișare.
