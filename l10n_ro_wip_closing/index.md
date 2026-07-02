# Producție în Curs (331/711) OMFP 1802 România (localizat la `l10n_ro_wip_closing/index.md`)

- **Nume Tehnic:** `l10n_ro_wip_closing`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_wip_closing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_wip_closing`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul implementează evaluarea și stornarea în roșu a producției în curs de execuție (WIP) conform OMFP 1802/2014 pct. 302–305. Corectează comportamentul Odoo 19 Community, care generează storno WIP la data+1 zi, impunând stornarea corectă la prima zi a lunii următoare. Adaugă un model persistent cu audit trail, generează nota corectă Dr 331 = Cr 711 și produce un Proces-Verbal de Evaluare în PDF.

## 2. Funcționalități Cheie

- **Corectarea datei de stornare:** override pe wizardul standard `mrp.account.wip.accounting` pentru companiile RO, astfel încât stornarea să fie la 1 a lunii următoare (în loc de date+1).
- **Model persistent `l10n.ro.wip.closing`:** cu state machine `draft → posted → cancelled` și audit trail complet.
- **Calcul automat WIP** din ordinele de fabricație în curs (`progress`, `to_close`, `confirmed`).
- **Nota corectă Dr 331 = Cr 711** (nu contul generic `account_production_wip_account_id`), cu storno în roșu (`is_storno=True`).
- **PV PDF:** Proces-Verbal de Evaluare cu semnături Director Economic / Contabil Șef.
- **Cron opțional** de închidere automată în ultima zi a lunii (inactiv implicit) și integrare cu checklist-ul de închidere de perioadă.

## 3. Dependențe

- `mrp_account`
- `l10n_ro`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `l10n.ro.wip.closing`: Modelul persistent al închiderii WIP, cu state machine și audit trail.
- `mrp.account.wip.accounting`: Wizard core extins pentru a corecta data de stornare pe companiile RO.
- `res.company`: Extins cu `l10n_ro_wip_closing_date` pentru integrarea cu închiderea de perioadă.

### Vizualizări / Date

- `views/l10n_ro_wip_closing_views.xml`: Interfața de gestionare a închiderilor WIP.
- `views/res_config_settings_views.xml`: Configurarea jurnalului WIP.
- `report/report_wip_closing.xml`: Șablonul PV PDF de evaluare.
- `data/ir_cron.xml`: Cron-ul de închidere automată.

### Acțiuni Automate / Acțiuni Server

- **Închidere WIP automată:** cron care rulează în ultima zi a lunii (inactiv implicit).

## 5. Conexiuni

- `l10n_ro_stock_cmp_periodic`
- `l10n_ro_stock_k_coefficient`
