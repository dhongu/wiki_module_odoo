# Romania - Declarația D112 ANAF (FR-44) (localizat la `l10n_ro_anaf_d112/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d112`
- **Versiune:** `19.0.2.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d112
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d112`
- **Ultima Ingestie:** 2026-09-12
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează întocmirea, validarea și exportul Declarației D112 ANAF — raportarea lunară a contribuțiilor sociale (CAS/CASS/CAM) și a impozitului pe venitul din salarii, cu evidență nominală per angajat. Permite atât importul automat al datelor din statele de plată Odoo Enterprise (prin modulul-punte `l10n_ro_anaf_d112_payroll`), cât și completarea manuală pentru firmele care importă salariile din sisteme externe (SAGA, Nexus), reducând semnificativ efortul de conformare fiscală lunară.

#### 2. Funcționalități Cheie

- **Import automat din statele de plată** Odoo Enterprise (coduri `BASIC`, `GROSS`, `CAS`, `CASS`, `INCOMETAX`, `WORK100`) prin modulul-punte `l10n_ro_anaf_d112_payroll`; completare manuală pentru firme care importă salarii din sisteme externe (SAGA, Nexus).
- **State machine** pentru declarație: ciornă → calculat → validat → exportat; butonul „Calculează" importă din statele de plată, „Validează" blochează modificările, iar „Descarcă XML" produce fișierul de depus la ANAF.
- **Linii nominale per angajat** cu CNP, venit brut, CAS/CASS/impozit, zile lucrate, concediu de odihnă și concediu medical.
- **Calcul automat al deducerilor** (orientativ, buton „Recalculează deduceri"): sumă neimpozabilă la salariul minim (S1/S2), deducere personală de bază, deducere suplimentară tineri sub 26 ani (15% × salariu minim) și copii (100 lei/copil), contribuții CAS/CASS și impozit 10%. Parametrii fiscali sunt grupați în `SALARY_PARAMS` și se revizuiesc anual; liniile importate din statul de plată păstrează valorile autoritare.
- **Tichete de masă** — câmp dedicat; suportă CASS (10%) și impozit (10%), scutite de CAS și CAM.
- **CAS suplimentar angajator** pentru condiții de muncă deosebite (+4%) / speciale (+8%), raportat distinct în obligațiile de plată (coduri 481/482).
- **Baza minimă de CAS/CASS** (art. 146 alin. (5^6) și art. 168 alin. (6^1) Cod fiscal): când baza reală e sub salariul minim pro-rata cu zilele în care contractul a fost activ, se declară pragul, iar diferența de contribuție o suportă angajatorul în numele angajatului, raportată la codurile de obligație proprii **458** (CAS) și **459** (CASS). Pragul folosește salariul minim al perioadei — (4050 − 300) pe lunile 01–06/2026, (4325 − 200) de la 07/2026 — iar numitorul e tabelul oficial ANAF de zile lucrătoare pe lună (`WORKING_DAYS`).
- **Excepții de la baza minimă** (art. 146 alin. (5^7)), marcabile pe linia nominală: elev/student sub 26 ani, ucenic sub 18, persoană cu dizabilități sau îndreptățită legal la sub 8 ore/zi, pensionar pentru limită de vârstă, sau salariat cu mai multe contracte a căror bază cumulată atinge salariul minim; se aplică doar veniturilor dintr-un contract individual de muncă (nu mandat/funcții elective) și rămân o decizie de dosar, cu documente justificative la angajator.
- **Generator XML D112** conform structurii oficiale `declaratieUnica`, cu trei profile pe perioadă: `v6` (namespace `mfp:anaf:dgti:declaratie_unica:declaratie:v6`) pentru perioade până la 31.12.2025, și două structuri distincte pe același namespace `v7` pentru 2026 — una pentru lunile 01–06/2026 (Ordin comun 2066/248/1377/3103/2026) și una de la luna de raportare 07/2026 (Ordin comun 605/95/928/2314/2026) — cu secțiunile `angajator`, `angajatorA` (obligații de plată cu cod bugetar), `angajatorB` (număr asigurați, fond de salarii), `asigurat`/`asiguratA`/`asiguratE1`/`asiguratE3` (nominal).
- **Validare XSD automată** la generare, reactivată pe toate cele trei profile cu schemele oficiale ANAF: `d112_10102024.xsd` (v6), `d112_06082026.xsd` (v7, 01–06/2026) și `d112_0726_140826.xsd` (v7, de la 07/2026) — inclusiv două patch-uri documentate în cod pe XSD-ul 07/2026, unde schema publicată de ANAF contrazice propria documentație a structurii (tipul câmpurilor `A_sal1`/`A_sal2` și enumerarea codurilor de obligație 458/459/486/487/488).
- **Reconciliere contabilă** D112 vs. rulajul conturilor 4315/4316/436/444 din perioadă, cu conturi și toleranță configurabile pe companie; opțional blocarea exportului la diferențe peste toleranță.
- **Raport de previzualizare** („D112 — Obligations Preview" în meniu): obligațiile lunii proiectate live din statele de plată sau din declarația materializată, cu butoanele „Generează ciorna D112" și export XML.
- **Declarație rectificativă** legată de declarația inițială exportată.
- **Integrare în tabloul de declarații** (`account.return`): tip de declarație lunar cu termen 25 a lunii următoare, pași de verificare (pregătire declarație, reconciliere, atașare XML semnat/recipisă SPV).
- **Validări blocante** la validare: checksum CNP, CNP duplicat, dată angajare obligatorie/coerentă, zile lucrate raportate la numărul de zile LUCRĂTOARE din lună (nu cele calendaristice), ore normă 6/7/8, venit pozitiv; avertismente neblocante pentru CAS/CASS recalculate.
- **Cod CAEN obligatoriu** pe companie (`angajator/@caen`), citit acum din `l10n_ro_anaf_base` (nu mai depinde tacit de `l10n_ro_config`); câmpul lipsă e prins de o gardă cu mesaj acționabil în locul unui fallback tăcut „0000".
- **Totaluri** CAS/CASS/impozit/CAM calculate automat din linii.

#### 3. Dependențe

- `account`
- `hr`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.d112` (`mail.thread`, `mail.activity.mixin`, `l10n_ro_anaf.report.handler.mixin`): declarația D112 propriu-zisă — state machine, calculul deducerilor și al bazei minime CAS/CASS, reconcilierea contabilă și generatorul de XML (profilele v6, v7-0126, v7-0726).
- `l10n.ro.d112.employee.line`: liniile nominale per angajat (CNP, venituri, contribuții, zile lucrate/concediu, excepții de la baza minimă, condiții de muncă).
- `l10n.ro.d112.reconcile.line`: liniile de reconciliere D112 vs. conturile contabile 4315/4316/436/444.
- `l10n_ro_anaf_d112.report.handler` (`account.report.custom.handler`, `l10n_ro_anaf.report.handler.mixin`): handler-ul raportului de previzualizare a obligațiilor D112; sursa implicită sunt totalurile declarației persistente, iar dacă e instalat modulul-punte de salarizare contribuie o proiecție live din statele de plată.
- `account.return` (extindere): calculul termenului legal (25 a lunii următoare) și verificările specifice D112 (declarație + reconciliere) în tabloul de declarații.
- `res.company` / `res.config.settings` (extindere): conturile contabile și toleranța folosite la reconcilierea D112.

**Vizualizări**

- `views/l10n_ro_d112_views.xml`: formularele și listele declarației D112 și ale liniilor nominale per angajat.
- `views/menus.xml`: meniurile „D112 Declaration" și „D112 — Obligations Preview" în Rapoarte financiare.
- `views/res_config_settings_views.xml`: setările de reconciliere D112 (conturi și toleranță) în Setări Contabilitate.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); calculul, validarea și exportul se declanșează manual prin butoanele din formular.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează infrastructura comună ANAF (profilele de declarație v6/v7, mixin-ul de handler de raport, codul CAEN al companiei) folosită de D112.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): altă declarație ANAF din aceeași familie, integrată similar în tabloul `account.return`.
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md) (fără pagină wiki): modul-punte care leagă D112 de `hr_payroll` — importul nominal din statele de plată și proiecția live a obligațiilor din raportul de previzualizare; fără el, D112 funcționează cu completare manuală a liniilor.
