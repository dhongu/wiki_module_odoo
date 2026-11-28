# Romania - CMP periodic lunar (localizat la `l10n_ro_stock_cmp_periodic/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_cmp_periodic`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_cmp_periodic
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_cmp_periodic`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul recalculează lunar Costul Mediu Ponderat (CMP) conform OMFP 1802/2014, pentru firmele care evaluează ieșirile din stoc la CMP periodic (lunar), nu la CMP perpetuu, cum face Odoo implicit. La finele lunii calculează CMP-ul din stocul inițial și toate intrările, determină diferența față de valoarea perpetuă deja postată și generează o singură notă contabilă de corecție, cu audit trail complet. Este util mai ales firmelor care migrează de la WinMentor sau SAGA.

#### 2. Funcționalități Cheie

- **Recalcul CMP lunar:** `CMP_lunar = (Val_stoc_inițial + Val_intrări) / (Cant_stoc_inițial + Cant_intrări)`, cu fallback la `standard_price` când numitorul este zero.
- **Notă de corecție (Abordarea B):** o singură notă echilibrată `602/607 ↔ 302/371` pe ultima zi a lunii, pentru diferența dintre evaluarea periodică și cea perpetuă.
- **Wizard cu previzualizare:** tabel cu diferența per produs înainte de generarea notei.
- **Activare per companie și per categorie de produs:** se procesează doar categoriile bifate explicit; setările (activare, jurnal de corecție, recalcul automat) sunt în Contabilitate → Configurare → Setări, secțiunea „CMP Periodic Lunar".
- **Registru CMP Periodic:** audit trail cu stoc inițial, intrări, CMP perpetuu vs. periodic, diferența de corecție și nota asociată, cu stări draft / calculat / postat; fiecare mișcare de ieșire păstrează valoarea provizorie și cea finală.
- **Recalcul automat opțional:** cron lunar; recalculul e blocat pentru luna deja postată sau pentru perioada blocată fiscal.
- **Coexistență cu coeficientul K:** metodele sunt independente și pot fi active simultan.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

**Modele**

- `l10n_ro.cmp_period_line`: registrul de audit CMP periodic.
- `l10n_ro.cmp_periodic_wizard` / `l10n_ro.cmp_periodic_wizard.line`: wizardul de recalcul și liniile de previzualizare (tranzitorii).
- `stock.move`, `account.move`, `product.category`, `res.company`, `res.config.settings` (extinse): valori provizorii/finale pe ieșiri, legătura cu nota de corecție, flag-ul pe categorie și setările.

**Vizualizări**

- `wizard/cmp_periodic_wizard_views.xml`: wizardul de recalcul cu previzualizare.
- `views/cmp_period_line_views.xml`: registrul de audit.
- `views/product_category_views.xml`: activarea pe categorii de produse.
- `views/account_move_views.xml`, `views/stock_move_views.xml`: extinderi pe note contabile și mișcări de stoc.
- `views/res_config_settings_views.xml`: setările CMP periodic.

**Acțiuni Automate / Acțiuni Server**

- `Monthly Periodic WAC — Automatic Recalculation` (`data/cmp_periodic_cron.xml`): cron lunar care apelează `run_cmp_periodic_cron()` pentru recalculul automat.

#### 5. Conexiuni

- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md): metodă independentă de evaluare, poate coexista cu CMP periodic.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): gestiunile contabile de stoc pe ale căror conturi se pot posta corecțiile.
