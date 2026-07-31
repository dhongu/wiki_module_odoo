# CMP Periodic Lunar România (localizat la `l10n_ro_stock_cmp_periodic/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_cmp_periodic`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_cmp_periodic
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_cmp_periodic`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul recalculează lunar Costul Mediu Ponderat (CMP) conform OMFP 1802/2014, pentru firmele care folosesc CMP periodic (lunar) în loc de CMP perpetuu folosit nativ de Odoo 19. La finele lunii, modulul calculează CMP-ul lunar din toate intrările, determină diferența față de valoarea perpetuă deja postată și generează o singură notă contabilă de corecție, cu audit trail complet. Este util în special firmelor care migrează de la WinMentor sau SAGA.

## 2. Funcționalități Cheie

- **Recalcul CMP lunar:** `CMP_lunar = (Val_stoc_final_luna_prec + Val_intrări_luna_crt) / (Qty_stoc_final_luna_prec + Qty_intrări_luna_crt)`.
- **Notă de corecție (Abordarea B):** generează o singură notă `602/607 ↔ 302/371` pentru diferența Δ dintre evaluarea periodică și cea perpetuă.
- **Wizard cu previzualizare:** tabel cu Δ per produs înainte de confirmare.
- **Activare per categorie de produs:** flag pe categoriile dorite și jurnal CMP dedicat.
- **Audit trail:** registru cu stoc inițial, intrări perioadă, CMP perpetuu vs. periodic, Δ corecție și nota asociată.

## 3. Dependențe

- `account`
- `stock_account`
- `l10n_ro`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Vizualizări / Date

- `wizard/cmp_periodic_wizard_views.xml`: Wizardul de recalcul CMP cu previzualizare.
- `views/cmp_period_line_views.xml`: Registrul de audit CMP periodic.
- `views/product_category_views.xml`: Activarea flag-ului pe categorii de produse.
- `views/account_move_views.xml`, `views/stock_move_views.xml`: Extinderi pe note contabile și mișcări de stoc.
- `views/res_config_settings_views.xml`: Setările CMP periodic.
- `data/cmp_periodic_cron.xml`: Cron-ul de recalcul.

### Acțiuni Automate / Acțiuni Server

- **Recalcul CMP periodic:** cron lunar pentru recalculul automat al CMP.

## 5. Conexiuni

- `l10n_ro_stock_k_coefficient`
- `l10n_ro_stock_gestiune`
