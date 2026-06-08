# Romania - Picking Reports - Product Expiry (localizat la `l10n_ro_stock_picking_report_product_expiry/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_picking_report_product_expiry`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_picking_report_product_expiry`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_picking_report_product_expiry`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul este o extensie de tip „punte" care adaugă data de expirare a produselor pe rapoartele de livrare/transfer din suita de rapoarte de stoc pentru România. Atunci când produsele sunt urmărite pe loturi/serii cu dată de expirare, modulul afișează coloana „Expiration Date" în bonul de livrare tipărit, astfel încât atât expeditorul, cât și clientul să vadă valabilitatea fiecărui lot direct pe document. Modulul se instalează automat când sunt prezente atât modulul de rapoarte de picking pentru România, cât și modulul standard de expirare a produselor.

#### 2. Funcționalități Cheie

- Adaugă coloana „Expiration Date" (data de expirare) în raportul de livrare/transfer (`report_delivery`) moștenit din `l10n_ro_stock_picking_report`.
- Preia data de expirare din lotul/seria asociat fiecărei linii de mișcare (`move_line.lot_id.expiration_date`).
- Afișează coloana doar dacă există cel puțin o linie cu lot ce are dată de expirare și doar pentru utilizatorii din grupul `product_expiry.group_expiry_date_on_delivery_slip`.
- Se instalează automat (`auto_install`) când dependențele sunt prezente, fără configurare suplimentară.

#### 3. Dependențe

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md)
- `product_expiry`

#### 4. Componente Cheie

> Notă: Fișierul `readme/DESCRIPTION.md` este gol, deci secțiunile „Sumar" și „Funcționalități Cheie" au fost sintetizate din `__manifest__.py` și din codul modulului. Componentele de mai jos sunt limitate la unica modificare adusă de modul (un template QWeb); modulul nu definește modele, vizualizări de tip formular/listă sau acțiuni automate.

**Vizualizări (rapoarte QWeb)**

- `report_delivery` (moștenit din `l10n_ro_stock_picking_report.report_delivery`): adaugă antetul de coloană și celula pentru data de expirare a lotului în bonul de livrare/transfer.

#### 5. Conexiuni

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): raportul de bază (NIR/bon/aviz) pe care acest modul îl extinde cu data de expirare.
- `product_expiry`: modulul standard Odoo care introduce data de expirare pe loturi/serii și grupul de drepturi folosit pentru afișarea coloanei.
