# Romania - Coeficient K pentru diferențe de preț la stocuri (localizat la `l10n_ro_stock_k_coefficient/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_k_coefficient`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_k_coefficient
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_k_coefficient`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează calculul lunar al coeficientului K de repartizare a diferențelor de preț la stocuri, conform OMFP 1802/2014, pentru entitățile care evaluează stocurile la prețuri de înregistrare standard (prestabilite) și folosesc conturile `302`/`371` cu diferențele aferente în `3028`/`378`. Automatizează procesul lunar, de la calculul previzual până la postarea notei contabile și a stornării în roșu la prima zi a lunii următoare. Firmele care evaluează la cost efectiv (CMP sau FIFO) nu au nevoie de el.

#### 2. Funcționalități Cheie

- **Wizard de calcul lunar** cu previzualizare completă înainte de confirmare: tabel cu K per pereche de conturi (Si/Rd stoc, Si/Rd diferențe, ieșiri stoc, numitor, K cu 6 zecimale, suma K) și avertisment dacă K = 0.
- **Perechi de conturi configurabile** (cont stoc, cont diferențe, cont cheltuieli): 302↔3028↔602, 371↔378↔607 sau orice altă combinație, din Contabilitate → Contabilitate → Coeficient K Stocuri → Perechi conturi K.
- **Stornare automată în roșu** la ziua 1 a lunii următoare, cu valori negative pe aceleași conturi, conform practicii contabile românești.
- **Protecție la numitor zero:** dacă (Si stoc + Rd stoc) = 0, K = 0, fără eroare.
- **Blocare recalcul** dacă luna este deja postată.
- **Audit trail** în Registrul Coeficient K (stări Calculat / Postat / Stornat), cu trimitere la nota K și la stornare.
- **Cron lunar** (inactiv implicit, activabil din setări) pentru companiile cu proces standardizat.
- Setări pe companie în Contabilitate → Configurare → Setări (jurnal K, stornare automată) și activare pe categorii de produse. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `stock`
- `stock_account`

#### 4. Componente Cheie

**Modele**

- `l10n_ro.k_account_pair`: perechea de conturi K (cont stoc, cont diferențe, cont cheltuieli).
- `l10n_ro.k_coefficient_line`: registrul de audit al calculelor K, cu valorile de calcul și referințele la notele generate.
- `l10n_ro.k_coefficient_wizard` / `l10n_ro.k_coefficient_wizard_line`: wizardul de calcul cu previzualizare.
- `account.move`, `stock.move`, `product.category`, `res.company`, `res.config.settings` (extinse): legătura cu notele K, activarea pe categorii și setările companiei.

**Vizualizări**

- `view_l10n_ro_k_coefficient_wizard_form`: wizardul Calcul Coeficient K.
- `view_l10n_ro_k_account_pair_list` / `view_l10n_ro_k_account_pair_form`: perechile de conturi.
- `view_l10n_ro_k_coefficient_line_list` / `view_l10n_ro_k_coefficient_line_form`: Registrul Coeficient K.
- `view_product_category_form_k_coefficient`, `res_config_settings_view_form_k_coefficient`: categorii de produse și setări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_k_coefficient_monthly`: calcul automat lunar al coeficientului K; inactiv implicit.

#### 5. Conexiuni

- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): alternativă pentru firmele care evaluează la cost efectiv (CMP).
- [l10n_ro_stock_provision](../l10n_ro_stock_provision/index.md): ajustări pentru deprecierea stocurilor, la închiderea lunii.
