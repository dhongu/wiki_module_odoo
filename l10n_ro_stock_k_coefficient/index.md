# Romania - Coeficient K pentru diferențe de preț la stocuri (localizat la `l10n_ro_stock_k_coefficient/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_k_coefficient`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_k_coefficient
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_stock_k_coefficient
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează calculul lunar al coeficientului K de repartizare a diferențelor de preț la stocuri, conform OMFP 1802/2014, pentru entitățile care evaluează stocurile la prețuri de înregistrare standard (prestabilite), cu stocul în `302`/`371` și diferențele de preț în `3028`/`378`. La finele lunii, diferențele acumulate se repartizează proporțional cu ieșirile din stoc, iar modulul generează nota contabilă și, opțional, stornarea în roșu la începutul lunii următoare. Firmele care evaluează la cost efectiv (CMP sau FIFO) nu au nevoie de el.

#### 2. Funcționalități Cheie

- **Wizard de calcul lunar** din **Contabilitate → Contabilitate → Coeficient K Stocuri → Calcul Coeficient K**: perioada implicită este luna anterioară, iar previzualizarea arată per pereche de conturi soldul inițial și rulajul debit pe stoc și pe diferențe, ieșirile din stoc (Rc), numitorul, K (6 zecimale) și Suma K.
- **Formula:** `K = (Si dif. + Rd dif.) / (Si stoc + Rd stoc)`, iar `Suma K = K × ieșiri stoc`; dacă numitorul este zero, K = 0 (marcaj Div/0) și pentru acea pereche nu se generează notă.
- **Perechi de conturi configurabile** (cont stoc, cont diferențe, cont cheltuieli), de exemplu 302↔3028↔602 și 371↔378↔607, din setările de contabilitate sau din **Coeficient K Stocuri → Perechi conturi K**.
- **Nota K:** postată în jurnalul K (de tip *Operațiuni diverse*), în ultima zi a lunii; cheltuiala (602/607) se debitează și diferențele (3028/378) se creditează.
- **Stornare automată în roșu** la 1 a lunii următoare (opțiune implicit activă): aceleași conturi cu valori negative, care reduc rulajele în loc să le inverseze.
- **Registru Coeficient K** cu istoricul calculelor (stări Calculat / Postat / Stornat) și legături la nota K și la stornare.
- **Protecții:** recalculul este blocat pentru o lună deja postată; nota nu se generează dacă perioada este blocată fiscal.
- **Blocarea recepțiilor cu preț standard zero** (opțional, pe categoria de produs, metoda Preț standard): refuză validarea recepțiilor pentru produse fără cost standard, premisa unui K corect.
- **Cerințe pe produs și categorie:** metoda de cost Preț standard, „Cont diferențe preț" identic cu contul de diferențe din pereche, iar prețul standard stabilit o dată pe an (modificarea lui în cursul lunii reevaluează stocul și distorsionează K).
- **Job lunar opțional**, inactiv implicit, care calculează și postează automat K pentru luna precedentă.
- Modulul nu generează note la recepție sau vânzare; acestea rămân în sarcina `stock_account` și `purchase_stock`, iar K repartizează doar diferențele deja înregistrate în 3028/378.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `stock`
- `stock_account`

#### 4. Componente Cheie

**Modele**

- `l10n_ro.k_coefficient_line`: audit trail al calculelor K per pereche de conturi și perioadă, cu valorile de calcul și referințele la note.
- `l10n_ro.k_account_pair`: perechea de conturi stoc / diferențe / cheltuieli folosită la calcul.
- `l10n_ro.k_coefficient_wizard` / `l10n_ro.k_coefficient_wizard_line` (wizard): calculul previzual și generarea notei K.
- `res.company`, `res.config.settings`, `product.category`, `stock.move`, `account.move` (extinse): jurnal și perechi pe companie, comutatorul pentru preț standard zero pe categorie, validarea recepțiilor, legătura notelor cu registrul.

**Vizualizări**

- `view_l10n_ro_k_coefficient_wizard_form`: wizardul de calcul K cu previzualizare.
- `view_l10n_ro_k_account_pair_list` / `view_l10n_ro_k_account_pair_form`: configurarea perechilor de conturi.
- `view_l10n_ro_k_coefficient_line_list` / `view_l10n_ro_k_coefficient_line_form`: Registrul Coeficient K.
- `view_product_category_form_k_coefficient`: comutatorul de blocare a recepțiilor cu preț standard zero.
- `res_config_settings_view_form_k_coefficient`: setările K (jurnal, stornare, perechi).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_k_coefficient_monthly` („Calcul automat coeficient K (lunar)"): rulează în prima zi a lunii și calculează și postează K pentru luna precedentă; inactiv implicit, se activează din **Setări tehnice → Automatizări**.

#### 5. Conexiuni

- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): metodă alternativă de evaluare (CMP periodic), independentă; pot fi active simultan.
