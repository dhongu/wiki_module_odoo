# ANAF D300 (localizat la `l10n_ro_anaf_d300/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d300`
- **Versiune:** `19.0.0.0.12`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d300
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d300`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul destinat departamentelor financiar-contabile din România care au obligația depunerii Decontului de TVA (Declarația 300) la ANAF. Permite generarea și exportul D300 direct din Odoo, în două formate acceptate oficial, fără re-introducerea manuală a datelor.

#### 2. Funcționalități Cheie

- **Export XDP (Soft A)**: generează un fișier Adobe XDP care poate fi importat instantaneu în formularul PDF inteligent oficial ANAF (D300 v12).
- **Export XML (Soft J)**: generează fișierul XML conform structurii oficiale ANAF v12.0.0+, gata pentru validare și semnare digitală în DUKIntegrator.
- **Validare XSD automată**: fișierul XML este validat față de schema XSD oficială înainte de export; erorile de structură sunt raportate înainte de descărcare.
- **Mapare rânduri de decont**: corelează automat codurile liniilor din raportul de taxe Odoo cu câmpurile corespunzătoare din declarația D300 (rânduri R1–R44).
- **Date de identificare completate automat**: CUI, denumire companie, reprezentant legal, județ (prin mapare ANAF din `l10n_ro_anaf_base`).
- **Calcul sold reportat TVA**: preia automat soldul conturilor 4423 (TVA de plată) și 4424 (TVA de recuperat) din perioada precedentă pentru rândurile R35/R38.
- **Suport TVA la încasare (CABA)**: calculează baza și TVA neexigibil din facturile neîncasate la sfârșitul perioadei.
- **Integrare account.return**: buton „Generează D300" disponibil în fluxul de închidere lunară/trimestrială, cu pre-filtrare automată pe perioada return-ului.
- **Tip decont automat**: detectează tipul perioadei (lunar L, trimestrial T, semestrial S, anual A) și generează numărul de evidență al plății conform algoritmului ANAF.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): completează CAEN-ul demo al companiei (`l10n_ro_caen_code`) la instalarea planului de conturi românesc.
- `account.report` / `tax_report_handler` (extins): logica de mapare a rândurilor raportului de taxe RO pe structura D300 și generarea fișierelor XDP/XML, inclusiv validarea companiei (`_validate_anaf_export_company`, cu `require_caen=True`).
- `res.company` (extins): câmpuri și configurări necesare identificării companiei/reprezentantului legal în decont.
- `res.config.settings` (extins): opțiuni de configurare aferente D300 în setările de contabilitate.
- `check.action.review` (extins): verificările de corelație D300 integrate în fluxul `account.return`.

**Vizualizări**

- `data/d300_grid_report.xml`: definirea grilei/structurii raportului D300.
- `data/d300_menu.xml`: intrările de meniu pentru D300.
- `data/return_checks.xml`: verificările de corelație asociate decontului, afișate în fluxul de închidere (`account.return`).
- `views/tax_report_xdp_export.xml`: butonul și template-ul de export XDP (Soft A).
- `views/tax_report_xml_export.xml`: butonul și template-ul de export XML (Soft J).
- `views/res_config_settings_views.xml`: opțiunile de configurare în setări.
- `demo/demo_data.xml`: date de test pentru demonstrații.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raportul de taxe sau din verificările fluxului de închidere (`account.return`).*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează mapările comune ANAF (ex: coduri de județ) folosite la completarea automată a datelor de identificare.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): aduce codul CAEN pe partener, cerut obligatoriu la export (`require_caen=True`).
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
