# Romania - ANAF D318 Declaration (localizat la `l10n_ro_anaf_d318/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d318`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d318
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d318`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite generarea Declarației 318 (Cerere de rambursare a TVA de către persoanele impozabile stabilite în România, depusă în alt stat membru UE) direct din Odoo Enterprise. Modulul este esențial pentru companiile românești care efectuează achiziții în alte state membre UE (combustibil, transport, cazare etc.) și doresc să recupereze TVA-ul plătit local în acele țări, conform procedurii stabilite prin Directiva 2008/9/CE.

#### 2. Funcționalități Cheie

- **Categorisire automată:** maparea cheltuielilor pe codurile standard ANAF (1-10) pentru o raportare corectă.
- **Filtrare inteligentă:** identificarea facturilor de furnizor din UE care conțin TVA plătit în statul respectiv.
- **Integrare nativă:** export XML direct din interfața de raportare fiscală Odoo, gata pentru validare și depunere.
- **Gestionare Pro-rata:** posibilitatea de a aplica procentul de deducere specific fiecărei cereri de rambursare.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `account.account` (extins în `models/account_account.py`): adaugă maparea codului de cheltuieli ANAF D318 (1-10) pe planul de conturi.
- `res.config.settings` (extins în `models/res_config_settings.py`): opțiuni de configurare pentru declarația D318.
- `res.company` (extins în `models/res_company.py`): parametri companie folosiți la generarea declarației.
- Handler de raport fiscal (`models/account_report_handler.py`): logica de identificare a facturilor eligibile și de generare a export-ului XML D318.

**Vizualizări**

- `views/account_account_views.xml`: câmp de configurare a codului de cheltuieli ANAF pe fișa contului contabil.
- `views/res_config_settings_views.xml`: setări specifice D318 în ecranul de configurare Contabilitate.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul XML se declanșează manual din raportul de taxe (`data/d318_report.xml` + `report/d318_xml_template.xml`).*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează infrastructura comună de generare/depunere a declarațiilor ANAF (semnare, ZIP/XDP, submisie SPV).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarație conexă de decont TVA, parte din același ecosistem de raportare fiscală RO.
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): declarație informativă privind TVA la încasare, parte din același ecosistem de raportare fiscală RO.
