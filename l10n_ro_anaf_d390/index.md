# ANAF D390 (localizat la `l10n_ro_anaf_d390/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d390`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d390
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d390`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Acest modul automatizează generarea Declarației recapitulative D390 (VIES) privind livrările, achizițiile și prestările intracomunitare de TVA către ANAF. Declarația este obligatorie pentru toate persoanele impozabile înregistrate în scopuri de TVA care efectuează operațiuni intracomunitare. Modulul extrage automat datele din raportul standard Odoo „Listă Vânzări/Achiziții EC", bazându-se pe tag-urile fiscale românești, eliminând completarea manuală pe fiecare partener UE și asigurând corelația cu evidența contabilă.

#### 2. Funcționalități Cheie

- **Handler dedicat** `l10n_ro_anaf_d390.tax.report.handler` care moștenește handlerul standard Odoo EC Sales fără a-l modifica, plus mixin-ul ANAF din `l10n_ro_anaf_base`.
- **Export XDP (Soft A):** import în formularul PDF inteligent ANAF.
- **Export XML (Soft J):** XML nativ conform structurii oficiale ANAF (v3, schema 2020+), validat XSD automat și compatibil DUKIntegrator.
- **Clasificare pe tax tags** (XML IDs stabile din `l10n_ro`): goods (L), services (P), triangular (T), goods_acquisition (A), services_acquisition (S).
- **Date declarant automate** din câmpul `l10n_ro_anaf_declaration_contact_id` (funcție fallback „CONTABIL").
- **Validări automate** înainte de export: cod TVA companie, adresă fiscală completă, cod TVA pentru toți partenerii incluși.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`
- `[[l10n_ro_anaf_base]]`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d390.tax.report.handler`: handlerul care moștenește `account.ec.sales.report.handler` și mixin-ul ANAF, atașat raportului `l10n_ro_d390_report`.

**Date / Vizualizări**

- `views/account_report_views.xml`: configurarea raportului D390.
- `views/d390_report_export.xml`: butonul/template-ul de export XDP.
- `views/d390_report_xml_export.xml`: butonul/template-ul de export XML.
- `views/d390_menu.xml`: intrările de meniu.
- `demo/demo_data.xml`: date de test.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raport.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d300]]`
- `[[l10n_ro_anaf_d394]]`
