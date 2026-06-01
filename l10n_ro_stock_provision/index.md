# Provizioane Stocuri Slow-Moving (39x) România (localizat la `l10n_ro_stock_provision/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_provision`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_provision
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_provision`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Acest modul identifică automat stocurile fără rulaj (slow-moving) și generează note contabile de ajustare pentru depreciere conform OMFP 1802/2014, pct. 143–148. Contabilul stabilește numărul de zile fără mișcare și procentul de depreciere, sistemul scanează stocurile și propune liniile, iar la confirmare generează nota Dr 6814 = Cr 39x la constituire și Dr 39x = Cr 7814 la reluare, cu mapare a conturilor 39x per categorie de produs.

## 2. Funcționalități Cheie

- **Identificare automată slow-moving:** scanează stocurile fără rulaj pe baza zilelor configurate și a procentului de depreciere.
- **Propuneri editabile:** contabilul poate debifa liniile pe care nu dorește să le provizioneze înainte de confirmare.
- **Generare note contabile:** Dr 6814 = Cr 39x la constituire/majorare și Dr 39x = Cr 7814 la reluare/diminuare.
- **Mapare conturi 39x per categorie:** 391 (materii prime), 392 (consumabile), 394 (produse finite), 397 (mărfuri).
- **Surse de date flexibile:** folosește `product.valuation.history` din `deltatech_stock_valuation` dacă e disponibil, altfel fallback pe `stock.quant.in_date`.
- **Cron lunar opțional** pentru generarea automată a analizelor în stare draft.

## 3. Dependențe

- `stock`
- `account`
- `l10n_ro_stock_age_report`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Vizualizări / Date

- `views/l10n_ro_stock_provision_views.xml`: Interfața de analiză a provizioanelor și propunerilor.
- `views/res_config_settings_views.xml`: Setările (conturi 6814/7814, zile slow-moving implicit).
- `data/ir_cron.xml`: Cron-ul de generare propuneri.

### Acțiuni Automate / Acțiuni Server

- **Generare propuneri provizioane stocuri slow-moving:** cron lunar (inactiv implicit) care creează analize draft pentru confirmare manuală.

## 5. Conexiuni

- `l10n_ro_stock_k_coefficient`
- `l10n_ro_stock_cmp_periodic`
