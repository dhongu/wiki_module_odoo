# Romania - Terrabit - Picking Reports (localizat la `l10n_ro_stock_picking_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_picking_report`
- **Versiune:** `19.0.1.2.8`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_picking_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_picking_report`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul adaugă rapoarte specifice gestiunii de stoc din România pentru documentele de mișcare a mărfurilor: recepție (NIR), livrare (aviz de însoțire) și transfer intern (bon de consum). Pe lângă tipărirea acestor documente conforme cu practicile locale, modulul propagă referința din comanda de achiziție în NIR și în factură și oferă opțiuni de configurare pentru afișarea taxelor pe recepție și a conturilor bancare pe rapoarte. Valoarea de afaceri constă în obținerea, direct din Odoo, a documentelor de gestiune uzuale folosite în România, fără prelucrări manuale suplimentare.

#### 2. Funcționalități Cheie

- Rapoarte pentru recepție (NIR), livrare (aviz) și transfer intern (bon de consum).
- Referința din comanda de achiziție este copiată în NIR și în factură.
- Opțiune în setări (România) pentru tipărirea taxelor pe recepție.
- Opțiune în setări (România) pentru tipărirea conturilor bancare pe rapoarte.

#### 3. Dependențe

- `base`
- `stock`
- `l10n_ro_config`
- `purchase_stock`
- `sale_stock`
- `l10n_ro_stock`
- `delivery`

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit detalierea componentelor tehnice; conform fluxului de ingestie, analiza codului pentru această secțiune nu a fost efectuată.

#### 5. Conexiuni

- `l10n_ro_stock`: gestiunea de stoc localizată pe care se bazează rapoartele de picking.
- `l10n_ro_config`: configurarea localizării române (opțiuni de tipărire taxe/bănci).
- `l10n_ro_stock_picking_comment_template`: modul exclus reciproc (`excludes`), care oferă o abordare alternativă pentru comentariile pe rapoartele de picking.
