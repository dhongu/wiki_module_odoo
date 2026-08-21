# ANAF D394 - Jurnale TVA Romania (localizat la `l10n_ro_anaf_d394/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d394`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d394
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d394`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul dedicat contabililor care lucrează cu legislația fiscală din România, oferind instrumentele necesare pentru generarea Jurnalului de Vânzări, a Jurnalului de Cumpărări și a Declarației Informative D394 conform cerințelor ANAF. Utilizează infrastructura centralizată din `l10n_ro_anaf_base` (validare XSD, mixin date companie/reprezentant, înregistrare MIME fișiere XDP).

#### 2. Funcționalități Cheie

- **Automatizare completă:** datele sunt preluate direct din facturile înregistrate, asigurând corelația între contabilitate și raportarea fiscală.
- **Detaliere pe cote de TVA:** rapoartele separă automat tranzacțiile pe cotele de TVA și pe tipuri de operațiuni (taxabile, scutite, taxare inversă).
- **Control și audit:** permite verificarea rapidă a sumelor prin accesarea directă a documentului sursă.
- **Gestionare TVA la încasare (CABA):** identifică automat facturile sub regimul TVA la încasare și raportează exigibilitatea taxei în momentul plății; evidențiază sumele neexigibile (din facturile neplătite) și sumele devenite exigibile în urma încasărilor/plăților din perioada curentă.
- **Taxare inversă (Reverse Charge):** identifică automat tranzacțiile cu taxare inversă și le clasifică corect — tip V pentru livrări RC, tip C pentru achiziții RC; ambele tipuri sunt incluse corect în D394, chiar dacă cota TVA este 0.
- **Export XLSX avansat:** jurnalele pot fi exportate în format Excel cu coloane dinamice pentru fiecare tip de taxă identificat în documente, optimizat pentru audit și verificare detaliată.
- **Generare D394 (XDP și XML Soft J):** butoanele „D394 file XDP" și „D394 file XML" sunt disponibile direct pe rapoartele de vânzări și cumpărări; fișierul generat poate fi importat în formularul PDF inteligent ANAF sau validat direct în aplicația DUKIntegrator (Soft J).
- **Clasificare automată Partener 1 / Partener 2:** partenerii înregistrați în scopuri TVA (Cartușul C) sunt separați automat de persoanele fizice și juridice neînregistrate TVA (Cartușul D), conform structurii XML D394.
- **Gestionare parteneri inactivi fiscal:** operațiunile cu parteneri declarați inactivi sunt clasificate corect în Cartușul C (perioada activă) și Cartușul D (perioada de inactivitate).
- **Opțiuni declarație configurabile:** periodicitate TVA, sistem TVA la încasare, opțiune contribuabil și persoane afiliate — configurabile per companie în Setări.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d394.report.mixin`: model abstract cu logica de construcție a datelor D394 (clasificare parteneri Cartuș C/D, CABA, taxare inversă, generare XDP/XML, filtre de export).
- `l10n_ro_account_vat_journal.sale.tax.report.handler` / `l10n_ro_account_vat_journal.purchase.tax.report.handler`: extind handler-ele jurnalelor de vânzări/cumpărări din `l10n_ro_account_vat_journal` cu mixin-ul D394.
- `res.company` (extindere): opțiuni de declarație configurabile per companie.
- `res.config.settings` (extindere): expune opțiunile D394 în ecranul de setări.

**Date / Vizualizări**

- `data/d394_report.xml`: definiția raportului D394.
- `data/d394_menu.xml`: intrările de meniu.
- `views/res_config_settings_views.xml`: opțiunile de configurare (periodicitate TVA, TVA la încasare, contribuabil, persoane afiliate).
- `views/d394_report_export.xml`: exportul XDP.
- `views/d394_report_xml_export.xml`: exportul XML.
- `static/src/components/**`: componente web (assets backend) pentru rapoarte.
- `demo/demo_data.xml`: date de test.

**Rapoarte**

- Tax Sale Report (RO) și Tax Purchase Report (RO): jurnalele de vânzări și cumpărări, accesibile din Contabilitate → Raportare → Taxe și Fiscal, cu butoane de export D394 (XDP/XML).

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din rapoarte.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructură comună (validare XSD, mixin companie/reprezentant, MIME fișiere XDP) reutilizată direct de acest modul.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): aduce codul CAEN pe partener, cerut la exportul companiei (`_validate_anaf_export_company(require_caen=True)`).
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md): furnizează handler-ele de bază ale jurnalelor de TVA extinse de acest modul cu logica D394.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): extinde declarația D394 cu datele din vânzările Punct de Vânzare (POS).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): Decontul de TVA (D300), pentru care jurnalele TVA din acest modul servesc drept bază.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): altă declarație informativă ANAF din același ecosistem de raportare fiscală RO.
