# Coeficient K Diferențe Preț Stocuri România (localizat la `l10n_ro_stock_k_coefficient/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_k_coefficient`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_k_coefficient
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_k_coefficient`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul implementează calculul lunar al coeficientului K de repartizare a diferențelor de preț la stocuri, conform OMFP 1802/2014 (Cap. IV), pentru entitățile care evaluează stocurile la prețuri de înregistrare standard (prestabilite). La finele fiecărei luni, diferențele de preț din conturile 3028 sau 378 se repartizează proporțional cu ieșirile din stoc prin coeficientul K, generând nota contabilă aferentă și stornarea automată în roșu la începutul lunii următoare.

## 2. Funcționalități Cheie

- **Wizard calcul lunar** cu previzualizare completă (K per pereche de conturi) înainte de confirmare.
- **Perechi de conturi configurabile:** 302↔3028↔602, 371↔378↔607 sau orice combinație.
- **Stornare automată în roșu** la ziua 1 a lunii următoare, conform practicii contabile RO (valori negative, nu inversate).
- **Protecție division by zero:** dacă numitorul = 0, K = 0 fără eroare fatală.
- **Blocare recalcul** dacă luna este deja postată.
- **Audit trail complet** în modelul `l10n_ro.k_coefficient_line` și job cron lunar (inactiv implicit).

## 3. Dependențe

- `account`
- `l10n_ro`
- `stock`
- `stock_account`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `l10n_ro.k_coefficient_line`: Audit trail al calculelor K per pereche de conturi și perioadă.
- Model pereche de conturi K (cont stoc + cont diferențe + cont cheltuieli).

### Vizualizări / Date

- `wizard/k_coefficient_wizard_views.xml`: Wizardul de calcul K cu previzualizare.
- `views/k_account_pair_views.xml`: Configurarea perechilor de conturi.
- `views/k_coefficient_line_views.xml`: Registrul de audit.
- `views/product_category_views.xml`, `views/res_config_settings_views.xml`: Activare pe categorii și setări.
- `data/k_coefficient_cron.xml`: Cron-ul lunar de calcul.

### Acțiuni Automate / Acțiuni Server

- **Calcul coeficient K:** cron lunar (inactiv implicit, activabil din setări).

## 5. Conexiuni

- `l10n_ro_stock_cmp_periodic`
- `l10n_ro_stock_provision`
