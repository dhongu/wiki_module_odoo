# ANAF D300 (localizat la `l10n_ro_anaf_d300/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d300`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d300
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d300`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite generarea Decontului de TVA (D300) direct din Odoo, conform formatului solicitat de ANAF. Decontul de TVA este principalul document de raportare a TVA-ului către fisc, reglementat de Codul Fiscal și de OPANAF nr. 1253/2021, și se depune de orice persoană impozabilă înregistrată în scopuri de TVA pentru fiecare perioadă fiscală. Modulul preia datele direct din evidența contabilă, minimizând erorile de operare manuală.

#### 2. Funcționalități Cheie

- **Generare fișier XDP (Soft A):** export în format Adobe XDP, importabil în formularul PDF inteligent ANAF.
- **Generare fișier XML (Soft J):** export XML nativ conform structurii oficiale ANAF (v12.0.0+), pentru validare cu DUKIntegrator.
- **Validare XSD automată:** XML-ul generat este verificat împotriva schemei XSD oficiale înainte de export.
- **Mapare rânduri de decont:** corelează rândurile din raportul de taxe Odoo cu rândurile din declarația D300.
- **Date identificare automate:** datele firmei și ale reprezentantului legal sunt completate din configurările Odoo.
- **Mapare județe:** codurile de județ sunt mapate conform nomenclatorului ANAF prin `l10n_ro_anaf_base`.
- **Tratare corectă** a taxării inverse, operațiunilor intracomunitare, deducerii limitate și soldului de TVA din perioada precedentă.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`
- `[[l10n_ro_anaf_base]]`
- `l10n_ro_reports`

#### 4. Componente Cheie

**Date / Vizualizări**

- `data/d300_menu.xml`: intrările de meniu pentru D300.
- `data/return_checks.xml`: verificările de corelație asociate decontului.
- `views/tax_report_xdp_export.xml`: butonul și template-ul de export XDP (Soft A).
- `views/tax_report_xml_export.xml`: butonul și template-ul de export XML (Soft J).
- `views/res_config_settings_views.xml`: opțiunile de configurare în setări.
- `demo/demo_data.xml`: date de test pentru demonstrații.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raportul de taxe.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d394]]`
- `[[l10n_ro_anaf_d390]]`
- `[[l10n_ro_anaf_d398]]`
- `[[l10n_ro_anaf_d100]]`
