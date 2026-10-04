# Romania - Declarația D112 ANAF (FR-44) (localizat la `l10n_ro_anaf_d112/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d112`
- **Versiune:** `19.0.2.9.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d112
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d112`
- **Ultima Ingestie:** `2026-10-04`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează întocmirea, validarea și exportul Declarației D112 ANAF — raportarea lunară a contribuțiilor sociale (CAS/CASS/CAM) și a impozitului pe venitul din salarii, cu evidență nominală per angajat. Permite atât importul automat al datelor din statele de plată Odoo Enterprise (prin modulul-punte `l10n_ro_anaf_d112_payroll`), cât și completarea manuală pentru firmele care importă salariile din sisteme externe (de exemplu Nexus, Charisma), reducând semnificativ efortul de conformare fiscală lunară.

#### 2. Funcționalități Cheie

- **Import automat din statele de plată** Odoo Enterprise (coduri `BASIC`, `GROSS`, `CAS`, `CASS`, `INCOMETAX`, `WORK100`) prin modulul-punte [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md); completare manuală pentru firme care importă salarii din sisteme externe (de exemplu Nexus, Charisma) — acest modul nu depinde de `hr_payroll`.
- **State machine** pentru declarație: ciornă → calculat → validat → exportat; butonul „Calculează" importă din statele de plată, „Validează" blochează modificările, iar „Descarcă XML" produce fișierul de depus la ANAF.
- **Linii nominale per angajat** cu CNP, venit brut, CAS/CASS/impozit, zile lucrate, zile cu contract activ, concediu de odihnă și concediu medical.
- **Împărțirea numelui salariaților** în nume/prenume delegă la funcția din `l10n_ro_anaf_base`, cu convenția „Nume Prenume” identică în toate declarațiile ANAF (înainte, D112 avea o funcție proprie cu convenția opusă).
- **Calcul automat al deducerilor** (orientativ, buton „Recalculează deduceri"): sumă neimpozabilă la salariul minim (S1/S2), deducere personală de bază, deducere suplimentară tineri sub 26 ani (15% × salariu minim) și copii (100 lei/copil), contribuții CAS/CASS și impozit 10%. Parametrii fiscali sunt grupați în `SALARY_PARAMS` și se revizuiesc anual; liniile importate din statul de plată păstrează valorile autoritare. Deducerea personală de bază folosește grila oficială art. 77 pe tranșe de 50 lei (venitul rotunjit la leu), aliniată cu `l10n_ro_hr_payroll_enhancement`.
- **Tichete de masă** — câmp dedicat; suportă CASS (10%) și impozit (10%), scutite de CAS și CAM; în XML se declară în `E3_10` (8.3.1), din `E3_60`, cu `E3_8` care le include (structura ANAF cere E3_8 ≥ E3_60 ≥ E3_10).
- **CAS suplimentar angajator** pentru condiții de muncă deosebite (+4%) / speciale (+8%), raportat distinct în obligațiile de plată (coduri 481/482).
- **Baza minimă de CAS/CASS** (art. 146 alin. (5^6) și art. 168 alin. (6^1) Cod fiscal): când baza reală e sub salariul minim pro-rata cu zilele în care contractul a fost activ (câmpul *Zile cu contract activ* de pe linia nominală, `zile_contract_activ`), se declară pragul, iar diferența de contribuție o suportă angajatorul în numele angajatului, raportată la codurile de obligație proprii **458** (CAS) și **459** (CASS). Pragul folosește salariul minim al perioadei — (4050 − 300) pe lunile 01–06/2026, (4325 − 200) de la 07/2026 — iar dacă acel câmp e gol, pragul rămâne pe zilele lucrate + CO + CM, iar zilele libere plătite și absențele nemotivate fără decizie de suspendare nu mai scad pragul când e completat; numitorul e tabelul oficial ANAF de zile lucrătoare pe lună (`WORKING_DAYS`). Declarația scrie acum și `asigExc`/`motivExc` (poziția salariatului față de prag și motivul, art. 146 alin. (5^7)) — câmpurile Odoo existau deja, dar validatorul oficial ANAF (J27.0.5) respingea declarația fiindcă nu erau scrise în XML.
- **Excepții de la baza minimă** (art. 146 alin. (5^7)), marcabile pe linia nominală: elev/student sub 26 ani, ucenic sub 18, persoană cu dizabilități sau îndreptățită legal la sub 8 ore/zi, pensionar pentru limită de vârstă, sau salariat cu mai multe contracte a căror bază cumulată atinge salariul minim; se aplică doar veniturilor dintr-un contract individual de muncă (nu mandat/funcții elective) și rămân o decizie de dosar, cu documente justificative la angajator.
- **Ore lucrate part-time raportate corect** (`A_6`): pentru un contract `Pi` (ex. `P6`), orele raportate se calculează din cifra contractului (6 ore/zi), nu din norma de referință a contractului (`A_4`, de regulă 8); etichetele tipului de contract au fost rescrise „Part-time, N hours/day" pentru a elimina confuzia că cifra ar fi un număr de variantă.
- **Generator XML D112** conform structurii oficiale `declaratieUnica`, cu trei profile pe perioadă: `v6` (namespace `mfp:anaf:dgti:declaratie_unica:declaratie:v6`) pentru perioade până la 31.12.2025, și două structuri distincte pe același namespace `v7` pentru 2026 — una pentru lunile 01–06/2026 (Ordin comun 2066/248/1377/3103/2026) și una de la luna de raportare 07/2026 (Ordin comun 605/95/928/2314/2026) — cu secțiunile `angajator`, `angajatorA` (obligații de plată cu cod bugetar), `angajatorB` (număr asigurați, fond de salarii), `asigurat`/`asiguratA`/`asiguratE1`/`asiguratE3` (nominal).
- **Validare XSD automată** la generare, reactivată pe toate cele trei profile cu schemele oficiale ANAF: `d112_10102024.xsd` (v6), `d112_06082026.xsd` (v7, 01–06/2026) și `d112_0726_140826.xsd` (v7, de la 07/2026) — inclusiv trei patch-uri documentate în cod pe XSD-ul 07/2026, unde schema publicată de ANAF contrazice propria documentație a structurii (tipul câmpurilor `A_sal1`/`A_sal2`, enumerarea codurilor de obligație 458/459/486/487/488, și tipul câmpurilor `asigExc`/`motivExc`).
- **Reconciliere contabilă** D112 vs. rulajul conturilor 4315/4316/436/444 din perioadă, cu conturi și toleranță configurabile pe companie; opțional blocarea exportului la diferențe peste toleranță.
- **Raport de previzualizare** (`D112 — Previzualizare obligații` în meniu): obligațiile lunii proiectate live din statele de plată sau din declarația materializată, cu butoanele „Generează ciorna D112" și export XML.
- **Declarație rectificativă** legată de declarația inițială exportată.
- **Ordine de plată pentru obligații** (buton *Pregătește plăți*, din 19.0.2.9.0): câte o plată în ciornă pe obligație cu sumă de plată (602, 412, 432, 480, 481/482/458/459), către contul IBAN unic al Trezoreriei (setare pe companie), cu suma datorat − scutit, scadența 25 a lunii următoare (weekend → luni) și contul de datorie al obligației drept contrapartidă (4315, 4316, 436, 444); buton *Plăți* pe declarație; nu se pregătesc de două ori și nu din rectificativă. De verificat: structura IBAN-ului Trezoreriei și datele OP, termenul în zi nelucrătoare, codurile 458/459/481/482; fără plată de grup și fără tipărirea OP.
- **Integrare în tabloul de declarații** (`account.return`): tip de declarație lunar cu termen 25 a lunii următoare, pași de verificare (pregătire declarație, reconciliere, atașare XML semnat/recipisă SPV).
- **Validări blocante** la validare: checksum CNP, CNP duplicat, dată angajare obligatorie/coerentă, zile lucrate raportate la numărul de zile LUCRĂTOARE din lună (nu cele calendaristice), ore normă 6/7/8, venit pozitiv; avertismente neblocante pentru CAS/CASS recalculate.
- **Cod CAEN obligatoriu** pe companie (`angajator/@caen`), citit acum din `l10n_ro_anaf_base` (nu mai depinde tacit de `l10n_ro_config`); câmpul lipsă e prins de o gardă cu mesaj acționabil în locul unui fallback tăcut „0000".
- **Concediul de odihnă la zile lucrate** (19.0.2.8.0): structura D112 nu are câmp pentru concediul de odihnă, iar zilele nu sunt suspendate, deci se declară ca zile lucrate (`A_6` / `A_8`, `B1_6`, `B2_*`, `B4_1`); validarea zilelor lucrate (1…NZL) folosește lucrate + CO. Interpretare dedusă din structură și din instrucțiuni (rd. «Total zile lucrate», «Ore suspendate»).
- **Concedii medicale (secțiunea D, GrupB)** (19.0.2.7.0): salariatul cu concediu medical se declară pe GrupB — `asiguratB1…B4`, câte un `asiguratD` pe certificat (`D_1`…`D_28`, cu `Data_CMI`, `D_3`/`D_4` la continuări, `D_9b`, `D_14a`, `D_20a`/`D_21a`) și `E3_1="B"`. `B2_5` = baza CAS a salariului, `B3_7` = baza CAS a indemnizațiilor (`B3_12` + `B3_13`), `B4_7` = `B2_5` + `B3_7`, `B4_14` = baza CAM fără partea din FNUASS; `E1_1`, `E3_8`, `E3_16` și baza impozabilă includ indemnizația din FNUASS. Secțiunea angajator `angajatorC2` (cazuri, zile și sume pe categorii: incapacitate 1.1–1.4, prevenire, sarcină, copil bolnav, oncologic, risc maternal; `C2_T6`, `C2_10`, `C2_140`), `C1_12` / `C1_T2` și `C1_11` pe baza salariului. Validări blocante pe secțiunea D (certificat dublat, `D_8` la copil bolnav, `D_11` / `D_12`, `D_7` în luna raportată, zile) și avertisment pentru codurile neimpozabile (08, 09, 91, 92, 15, 17). Verificat cu DUKIntegrator: declarație mixtă GrupA + GrupB, certificat inițial + continuare, carantină.
- **`E3_8` și venituri neimpozabile** (19.0.2.6.0): de la perioada 07/2026 rândul 8 cuprinde art. 76 alin. (1)–(4¹) (OPANAF 605/2026, Anexa 6), deci `E3_8` și `E1_1` includ veniturile neimpozabile 8.4 / 8.5. Câmpuri noi pe linia nominală: venit neimpozabil alin. (4) → `E3_69`, diurnă neimpozabilă (din care, 8.4.3) → `E3_62`, venit neimpozabil alin. (4¹) → `E3_90`; nu intră în bazele CAS / CASS / impozit și nu se declară înainte de 07/2026. `A_sal2` = `E3_8` − `E3_69` (include și tichetele). Verificat cu DUKIntegrator (`E3_8` 5.200, `A_sal2` 5.085).
- **Scutirea de impozit art. 60** (pct. 1 handicap, pct. 3 cercetare-dezvoltare), declarată (XML 09/2026 validat de DUKIntegrator): câmpul de linie *Scutire impozit (art. 60)* → `asigScu` 1/3; `E3_23`/`E3_24` sau `E3_27`/`E3_28` = baza impozabilă și impozitul care s-ar fi datorat (10%); `E3_15` = 0; la angajator obligația 602 cu `A_datorat` = reținut + scutit, `A_scutit` și `angajatorF1`; `E3_16` include tichetele; XSD 07/2026 admite tipul de asigurat 51.
- **Deduceri și în `asiguratE3`**: persoanele în întreținere și deducerile personale se declară și în `E3_11`, `E3_12`, `E3_121`, `E3_122`, `E3_1221`, `E3_1222`, `E3_13` (structura ANAF cere ca E1_x să fie sumele câmpurilor E3).
- **Totaluri** CAS/CASS/impozit/CAM calculate automat din linii; baza CAM (`cam_baza`, `A_5`, `B1_5`, `B4_14`, `C4_baza`) = venit brut − suma neimpozabilă la salariul minim.

Fluxul complet lunar (previzualizare → ciornă → verificare linii → reconciliere contabilă → validare → generare/descărcare XML → înregistrarea depunerii în tabloul de declarații), precum și declarația rectificativă, sunt detaliate pas cu pas în [FISA_CONSULTANT.md](FISA_CONSULTANT.md). Setările obligatorii dinaintea primei utilizări (cod CAEN, județ, date contact ANAF, conturile și toleranța de reconciliere din Contabilitate → Configurare → Setări) sunt descrise în `readme/CONFIGURE.md`.

#### 3. Dependențe

- `account`
- `hr`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.d112` (`mail.thread`, `mail.activity.mixin`, `l10n_ro_anaf.report.handler.mixin`): declarația D112 propriu-zisă — state machine, calculul deducerilor și al bazei minime CAS/CASS (inclusiv `asigExc`/`motivExc`), reconcilierea contabilă și generatorul de XML (profilele v6, v7-0126, v7-0726).
- `l10n.ro.d112.employee.line`: liniile nominale per angajat (CNP, venituri, contribuții, zile lucrate/concediu, `zile_contract_activ` pentru pragul CAS/CASS, excepții de la baza minimă, condiții de muncă, ore efective calculate din tipul de contract).
- `l10n.ro.d112.medical.leave`: certificatele de concediu medical (secțiunea D) ale unei linii nominale; pagina *Concedii medicale* a declarației.
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
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): modul-punte (`auto_install`) care leagă D112 de `hr_payroll` — importul nominal din statele de plată și proiecția live a obligațiilor din raportul de previzualizare; fără el, D112 funcționează cu completare manuală a liniilor.

---

**Notă modificări față de pagina anterioară (19.0.2.3.3):** 19.0.2.4.0 (2026-09-29) adaugă pe linia nominală câmpul *Zile cu contract activ* (`zile_contract_activ`); pragul minim CAS/CASS se calculează pe zilele lucrătoare cu contract nesuspendat, nu doar pe zilele lucrate + CO + CM. Gol, se păstrează comportamentul anterior.
