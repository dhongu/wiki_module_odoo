# ANAF D394 - Jurnale TVA Romania (localizat la `l10n_ro_anaf_d394/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d394`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d394
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d394`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul oferă contabililor din România instrumentele necesare pentru generarea Jurnalului de Vânzări, a Jurnalului de Cumpărări și a Declarației Informative D394, conform Codului Fiscal (Art. 321), OMFP 2734/2011 și OPANAF 3769/2015. Jurnalele de TVA servesc ca bază pentru Decontul de TVA (D300), iar D394 conține lista partenerilor cu care s-au efectuat tranzacții pe teritoriul național. Datele sunt preluate direct din facturile înregistrate, asigurând corelația între contabilitate și raportarea fiscală.

#### 2. Funcționalități Cheie

- **Automatizare completă:** date preluate direct din facturile înregistrate.
- **Detaliere pe cote de TVA** și pe tipuri de operațiuni (taxabile, scutite, taxare inversă).
- **Gestionare TVA la încasare (CABA):** identifică facturile sub regimul de încasare și raportează exigibilitatea în momentul plății, evidențiind sume neexigibile și exigibile.
- **Taxare inversă (Reverse Charge):** clasificare corectă tip V (livrări) și tip C (achiziții), incluse în D394 chiar la cotă 0.
- **Export XLSX avansat** cu coloane dinamice per tip de taxă, optimizat pentru audit.
- **Generare D394 (XDP și XML Soft J):** butoanele „D394 file XDP" și „D394 file XML" direct pe rapoartele de Vânzări și Cumpărări, compatibile cu PDF inteligent și DUKIntegrator.
- **Clasificare automată Partener 1 / Partener 2** (Cartușul C vs. Cartușul D) conform structurii XML.
- **Gestionare parteneri inactivi fiscal** clasificați corect în Cartușul C (perioada activă) și D (perioada de inactivitate).
- **Validare CNP** persoane fizice înainte de generare.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- `[[l10n_ro_anaf_base]]`

#### 4. Componente Cheie

**Date / Vizualizări**

- `data/l10n_ro_tax_report.xml`: structura raportului de taxe RO.
- `data/d394_report.xml`: definiția raportului D394.
- `data/d394_menu.xml`: intrările de meniu.
- `views/res_config_settings_views.xml`: opțiunile de configurare.
- `views/d394_report_export.xml`: exportul XDP.
- `views/d394_report_xml_export.xml`: exportul XML.
- `static/src/components/**`: componente web (assets backend) pentru rapoarte.
- `demo/demo_data.xml`: date de test.

**Rapoarte**

- Tax Sale Report (RO) și Tax Purchase Report (RO): jurnalele de vânzări și cumpărări, accesibile din Contabilitate → Raportare → Taxe și Fiscal.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din rapoarte.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d394_pos]]`
- `[[l10n_ro_anaf_d300]]`
- `[[l10n_ro_anaf_d390]]`
