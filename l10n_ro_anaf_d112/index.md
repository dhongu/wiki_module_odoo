# Romania - Declarația D112 ANAF (FR-44) (localizat la `l10n_ro_anaf_d112/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d112`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d112
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d112`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează întocmirea, validarea și exportul Declarației D112 ANAF — raportarea lunară a contribuțiilor sociale (CAS/CASS/CAM) și a impozitului pe venitul din salarii, cu evidență nominală per angajat. Permite atât importul automat al datelor din statele de plată Odoo Enterprise, cât și completarea manuală pentru firmele care importă salariile din sisteme externe (SAGA, Nexus), reducând semnificativ efortul de conformare fiscală lunară.

#### 2. Funcționalități Cheie

- **Import automat din statele de plată** Odoo Enterprise (coduri `BASIC`, `GROSS`, `CAS`, `CASS`, `INCOMETAX`, `WORK100`); completare manuală pentru firme care importă salarii din sisteme externe (SAGA, Nexus).
- **State machine** pentru declarație: ciornă → calculat → validat → exportat; butonul „Calculează" importă din statele de plată, „Validează" blochează modificările, iar „Descarcă XML" produce fișierul de depus la ANAF.
- **Linii nominale per angajat** cu CNP, venit brut, CAS/CASS/impozit, zile lucrate, concediu de odihnă și concediu medical.
- **Calcul automat al deducerilor** (orientativ, buton „Recalculează deduceri"): sumă neimpozabilă la salariul minim (S1/S2), deducere personală de bază, deducere suplimentară tineri sub 26 ani (15% × salariu minim) și copii (100 lei/copil), contribuții CAS/CASS și impozit 10%. Parametrii fiscali sunt grupați în `SALARY_PARAMS` și se revizuiesc anual; liniile importate din statul de plată păstrează valorile autoritare.
- **Tichete de masă** — câmp dedicat; suportă CASS (10%) și impozit (10%), scutite de CAS și CAM.
- **CAS suplimentar angajator** pentru condiții de muncă deosebite (+4%) / speciale (+8%), raportat distinct în obligațiile de plată (coduri 481/482).
- **Generator XML D112** conform structurii oficiale `declaratieUnica`, cu suport pentru două namespace-uri în funcție de perioada raportată — `v6` (`mfp:anaf:dgti:declaratie_unica:declaratie:v6`) pentru perioade până la 31.12.2025 și `v7` de la 01.01.2026 — cu secțiunile `angajator`, `angajatorA` (obligații de plată cu cod bugetar), `angajatorB` (număr asigurați, fond de salarii), `asigurat`/`asiguratA`/`asiguratE1`/`asiguratE3` (nominal).
- **Validare XSD automată** la generare contra schemei oficiale ANAF `d112_10102024.xsd` (profilul v6; pentru v7 ANAF nu a publicat încă un XSD liber).
- **Reconciliere contabilă** D112 vs. rulajul conturilor 4315/4316/436/444 din perioadă, cu conturi și toleranță configurabile pe companie; opțional blocarea exportului la diferențe peste toleranță.
- **Raport de previzualizare** („D112 — Obligations Preview" în meniu): obligațiile lunii proiectate live din statele de plată sau din declarația materializată, cu butoanele „Generează ciorna D112" și export XML.
- **Declarație rectificativă** legată de declarația inițială exportată.
- **Integrare în tabloul de declarații** (`account.return`): tip de declarație lunar cu termen 25 a lunii următoare, pași de verificare (pregătire declarație, reconciliere, atașare XML semnat/recipisă SPV).
- **Validări blocante** la validare: checksum CNP, CNP duplicat, dată angajare obligatorie/coerentă, zile lucrate în interval, ore normă 6/7/8, venit pozitiv; avertismente neblocante pentru CAS/CASS recalculate.
- **Totaluri** CAS/CASS/impozit/CAM calculate automat din linii.

#### 3. Dependențe

- `account`
- `hr`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.d112` (`mail.thread`, `mail.activity.mixin`, `l10n_ro_anaf.report.handler.mixin`): declarația D112 propriu-zisă — state machine, calculul deducerilor, reconcilierea contabilă și generatorul de XML (profile v6/v7).
- `l10n.ro.d112.employee.line`: liniile nominale per angajat (CNP, venituri, contribuții, zile lucrate/concediu).
- `l10n.ro.d112.reconcile.line`: liniile de reconciliere D112 vs. conturile contabile 4315/4316/436/444.
- `l10n_ro_anaf_d112.report.handler` (`account.report.custom.handler`, `l10n_ro_anaf.report.handler.mixin`): handler-ul raportului de previzualizare a obligațiilor D112.
- `account.return` (extindere): calculul termenului legal (25 a lunii următoare) și verificările specifice D112 (declarație + reconciliere) în tabloul de declarații.
- `res.company` / `res.config.settings` (extindere): conturile contabile și toleranța folosite la reconcilierea D112.

**Vizualizări**

- `views/l10n_ro_d112_views.xml`: formularele și listele declarației D112 și ale liniilor nominale per angajat.
- `views/menus.xml`: meniurile „D112 Declaration" și „D112 — Obligations Preview" în Rapoarte financiare.
- `views/res_config_settings_views.xml`: setările de reconciliere D112 (conturi și toleranță) în Setări Contabilitate.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); calculul, validarea și exportul se declanșează manual prin butoanele din formular.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează infrastructura comună ANAF (profile de declarație, mixin-ul de handler de raport) folosită de D112.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): altă declarație ANAF din aceeași familie, integrată similar în tabloul `account.return`.
