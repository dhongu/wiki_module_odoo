# Romania - Situații Financiare Anuale ANAF (FR-31) (localizat la `l10n_ro_financial_statements/index.md`)

- **Nume Tehnic:** `l10n_ro_financial_statements`
- **Versiune:** `19.0.1.9.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_financial_statements
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_financial_statements`
- **Ultima Ingestie:** 2026-09-12
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Generează documentul de depunere a situațiilor financiare anuale în formatul cerut de ANAF, pornind de la rapoartele Enterprise din `l10n_ro_reports`. Piesa centrală este documentul unic `<Bilant1003>` — un singur fișier cu F10 (Bilanț), F20 (Cont de profit și pierdere) și F30 (Date informative) ca elemente, cu valorile scrise ca atribute `F<formular>_<rând><coloană>`, format verificat prin rulare efectivă cu validatorul oficial ANAF. Modulul mai oferă exporturi XML separate pe formular (pre-completare, cu un singur slot pe rând), numerotarea oficială a rândurilor derivată din grila extrasă din validator, pre-validarea a 290 din cele 303 reguli de corelație ale formularului (nemaiverificate de validatorul ANAF 2025), validarea echilibrului bilanțului și rapoartele Enterprise F30 (Date informative) și F40 (Situația activelor imobilizate). Se adresează contabililor și directorilor financiari din companiile românești care depun anual situațiile financiare la ANAF și Registrul Comerțului, conform OMFP 1802/2014.

#### 2. Funcționalități Cheie

- **Documentul unic de depunere `<Bilant1003>`** — buton „Export ANAF submission (full set)" pe raportul F10, care produce un singur fișier XML cu F10/F20/F30 (F40 opțional) ca elemente ale aceleiași rădăcini, confirmat prin round-trip cu validatorul oficial (`S1003`, namespace `mfp:anaf:dgti:s1003:declaratie:v15`). Exportul e blocat până când numerotarea formularelor obligatorii e verificată rând cu rând (în prezent F10, F20, F30).
- **Exporturi XML pe formular (pre-completare)** — butonul „Export XML ANAF (pre-fill, single form)" pe rapoartele F10/F20/F30, cu convenția `<rd nr="N" val="V"/>`, un singur slot pe rând (coloana de închidere la F10/F20).
- **Numerotarea oficială a rândurilor** — maparea liniilor de raport pe rândurile ANAF se face pe codul liniei, insensibil la limbă; grila de rânduri și coloane valide e extrasă automat din validatorul ANAF decompilat (`scripts/extract_fs_layout.py`), nu scrisă manual, și se regenerează la fiecare republicare a validatorului.
- **Pre-validarea corelațiilor** — 290 din cele 303 reguli ale formularului (totaluri, inegalități, rânduri de profit/pierdere de tipul `X = max(A − B, 0)`, excluderi reciproce), extrase automat din validator (`scripts/extract_fs_rules.py`) și verificate înainte de export; sunt necesare fiindcă validatorul ANAF 2025 nu mai aplică nicio regulă de business. Cele 13 reguli neacoperite rămân documentate ca text brut. Regulile ale căror câmpuri nu au fost emise se sar, nu se numără ca zero, ca să nu producă alarme false.
- **Validare bilanț echilibrat** — blocare export dacă Total Activ ≠ Total Pasiv, cu toleranță de 1 RON.
- **Avertismente pentru ce nu ajunge în depunere** — bannere pe raport și comentarii în fișierul XML pentru: rândurile F30 fără număr oficial confirmat (se completează manual în formularul ANAF) și rândurile F10/F20/F30 exportate cu unele coloane oficiale goale (ex. soldul de la începutul exercițiului la F10/F20, defalcarea pe vechime la F30).
- **Formularul 40 — Situația activelor imobilizate:** raport Enterprise, cu coloane Sold inițial/Creșteri/Reduceri/Sold final, calculat pe categorii (imobilizări necorporale, corporale, financiare, amortizare, ajustări de depreciere) din rulajele conturilor 20x/21x/23x/26x/28x/29x.
- **Formularul 30 — Date informative:** combină rânduri derivate din contabilitate (rezultat profit/pierdere, plăți restante furnizori/buget/credite, dobânzi/dividende, creanțe/datorii pe scadențe) cu rânduri introduse manual (număr mediu de salariați, structura capitalului social, cheltuieli de cercetare-dezvoltare pe surse) prin modelul persistent `l10n.ro.f30.manual.value`, cheie unică pe companie + perioadă + cod de rând.
- **Antetul companiei pentru document (Setări → Contabilitate)** — câmpuri specifice ANAF care nu se pot deduce din contabilitate: cod CAEN (rezervă, folosită doar dacă lipsește modulul OCA `l10n_ro_config`), formă de proprietate (codPP), administrator, întocmitor (nume/calitate/nr. înregistrare CECCAR), entitate de interes public, steaguri ANAF fără etichetă în validator (bifaMC/DD/GG/AA, codJJ) — completate exact conform formularului oficial tipărit.
- **Implementat ca `account.report.custom.handler`** — trei handlere (`l10n.ro.fs.handler` pentru F10/F20, `l10n.ro.f40.handler`, `l10n.ro.f30.handler`) integrate nativ în frameworkul Enterprise de rapoarte, plus modelul `l10n.ro.fs.document` (moștenește mixin-ul `l10n_ro_anaf.report.handler.mixin`) pentru construcția documentului unic — fără rapoarte duplicate și fără wizard separat.

#### 3. Dependențe

- `l10n_ro_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- `account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fs.document` (`l10n_ro_anaf.report.handler.mixin`): constructorul documentului unic `<Bilant1003>` — antet, colectarea celulelor pe formular, verificarea formularelor obligatorii cu numerotare confirmată și emiterea XML-ului final.
- `l10n.ro.fs.handler` (`account.report.custom.handler`): handler ce adaugă butoanele de export pe rapoartele F10 (Bilanț) și F20 (CPP) — exportul unic `<Bilant1003>` de pe F10, exportul pre-fill pe formular, validarea de echilibru a bilanțului și pre-validarea corelațiilor înainte de export.
- `l10n.ro.f30.handler` (`account.report.custom.handler`): calculează rândurile Formularului 30 (rezultat, plăți restante, dobânzi/dividende, creanțe/datorii pe scadențe), gestionează butonul „Fill manual rows" și construiește XML-ul doar cu rândurile al căror număr oficial ANAF e confirmat pentru anul fiscal selectat.
- `l10n.ro.f40.handler` (`account.report.custom.handler`): calculează Situația activelor imobilizate (F40) pe categorii de conturi, cu solduri inițiale/finale și creșteri/reduceri pe perioadă.
- `l10n.ro.fs.validator` (model abstract): pre-validarea corelațiilor formularului împotriva regulilor extrase din validatorul ANAF (`ANAF_RULES` / `ANAF_RULES_UNPARSED` din `l10n_ro_fs_rules.py`), cu toleranță de 1 leu la rotunjiri.
- `l10n.ro.fs.layout` (model abstract): sursa unică a numerotării oficiale ANAF pe (tip bilanț, an) — `REPORT_PAIR_BY_TIP`, `FORMS_WITH_VERIFIED_ROWS` și maparea cod intern → (formular, rând oficial), cu moștenire de la o versiune `default` pentru anii care doar renumerotează câteva rânduri.
- `l10n.ro.f30.manual.value`: stochează valorile introduse manual pentru rândurile statistice ale Formularului 30, cheie unică pe companie + perioadă + cod de rând.
- `res.company` (extins): câmpurile de antet ale documentului ANAF care nu se pot deriva din contabilitate (CAEN de rezervă, formă de proprietate, administrator, întocmitor, entitate de interes public, steaguri fără etichetă în validator).

**Vizualizări / Date**

- `data/l10n_ro_fs_report_setup.xml`: leagă handlerul `l10n.ro.fs.handler` de raportul F10 Bilanț (`l10n_ro_reports.account_financial_report_ro_bs_smle`) și de toate variantele F20 CPP (smle / micro-entitate / internațional).
- `data/l10n_ro_f40_report.xml`: definește raportul Enterprise „Code 40 - Statement of Fixed Assets" (coloane Opening Balance/Increases/Reductions/Closing Balance), acțiunea client și intrarea de meniu în Rapoartele contabile.
- `data/l10n_ro_f30_report.xml`: definește raportul Enterprise „Code 30 - Informative Data (auto-fill)" grupat pe `f30_line`, acțiunea client și intrarea de meniu în Rapoartele contabile.
- `views/l10n_ro_f30_manual_views.xml`: vizualizarea listă pentru editarea rândurilor manuale ale Formularului 30, deschisă din butonul „Fill manual rows".
- `views/res_config_settings_views.xml`: blocul „Romanian Annual Financial Statements" în Setări → Contabilitate, cu câmpurile de antet ANAF ale companiei.
- `static/src/warnings.xml`: șabloanele QWeb ale bannerelor de avertizare afișate pe rapoarte (rânduri F30 neexportate, coloane parțiale F30, coloana de deschidere lipsă la F10/F20).

**Acțiuni Automate / Acțiuni Server**

- Butonul „Export ANAF submission (full set)" (F10) — generează documentul unic `<Bilant1003>`.
- Butonul „Export XML ANAF (pre-fill, single form)" (F10/F20/F30) — generează XML-ul per formular.
- Butonul „Fill manual rows" (F30), care seedează idempotent câte un rând manual pe companie/perioadă și deschide lista editabilă.

#### 5. Conexiuni

- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): note explicative la bilanț, complementare situațiilor financiare.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): document suport pentru patrimoniu.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): rezultatul exercițiului în contul 121.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): mixin-ul de handler ANAF pe care se construiește documentul unic, și infrastructura comună de declarații ANAF.
- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md): planul de conturi RO pe care se construiesc formularele.
- `l10n_ro_reports`: rapoartele Enterprise F10/F20 (Bilanț, CPP) pe care le extinde modulul; fără el butoanele de export nu au pe ce se afișa.
