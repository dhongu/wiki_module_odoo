# Fișă Modul: Situații Financiare Anuale

**Poziție plan:** B2.3
**Modul:** `l10n_ro_financial_statements`
**FR:** FR-31
**Capitol manual:** Cap 11.2
**Utilizator principal:** Contabil șef, Responsabil fiscal
**Prioritate:** 🔴 Ridicată (termen legal: 150 de zile de la încheierea exercițiului)

---

## 1. Scop business

Modulul produce **fișierul de depunere a situațiilor financiare anuale** în formatul cerut de ANAF,
pornind de la rapoartele financiare românești din `l10n_ro_reports` (Enterprise). Consultantul
folosește documentul pentru reproducerea fluxului în baza demo și pentru pregătirea capitolului
Cap 11.2 din manualul utilizator.

Fără modul, rapoartele există pe ecran, dar fișierul de depus nu se poate genera din Odoo.

Pe lângă bilanț, modulul acoperă două documente din același dosar anual:

- **Declarația de inactivitate** (formularul ANAF S1046). O depun, în locul situațiilor financiare,
  entitățile care nu au desfășurat activitate de la constituire până la sfârșitul exercițiului.
- **Raportul administratorilor**, care însoțește situațiile financiare. Indicatorii se precompletează
  din aceleași rânduri ca documentul de depunere, iar secțiunile narative le redactează administratorul.

## 2. Bază legală și context

- **OMFP 1802/2014** — Reglementări contabile privind situațiile financiare anuale; definește
  **structura** Bilanțului (F10) și a Contului de Profit și Pierdere (F20). **Numerotarea de
  depunere** nu vine de aici: ea se ia din ordinul MF al anului și se verifică pe grila
  validatorului — numerele din etichetele rapoartelor Enterprise nu coincid cu cele oficiale.
- **Ordinul MF de depunere** pentru exercițiul raportat — aprobă anual structura formularelor.
  Structura efectiv acceptată se verifică pe validatorul publicat de ANAF pentru anul respectiv.
- **Legea 82/1991**, art. 36 — obligativitatea depunerii, în **150 de zile** de la încheierea
  exercițiului financiar pentru societăți (120 de zile pentru celelalte entități); arhivare 10 ani.

- **Anexa ordinului MF de închidere a exercițiului, pct. 3.3**. Entitățile care nu au desfășurat
  activitate de la constituire până la sfârșitul exercițiului nu întocmesc situații financiare. Ele
  depun, în **60 de zile** de la încheierea exercițiului, o **declarație de inactivitate** pe propria
  răspundere a persoanei care are obligația gestionării entității. Același ordin, la pct. 3.5, cere
  ca situațiile financiare să fie însoțite de raportul administratorilor.
- **OMFP 1802/2014, pct. 489–492**: conținutul raportului administratorilor (vezi Pasul 10).

> A nu se confunda declarația de inactivitate (contabilă, anuală) cu starea fiscală de
> „contribuabil inactiv” (Codul de procedură fiscală) sau cu suspendarea activității la Registrul
> Comerțului. Cele două nu scutesc de situații financiare o entitate care a avut activitate vreodată.

Modulul acoperă **bilanțul prescurtat** (`tipBIL = BS`, validator ANAF S1003), adică perechea de
rapoarte „Cod 10 - Bilanț" + „Cod 20 - Cont de Profit și Pierdere". Bilanțul complet și cel
simplificat pentru microentități nu sunt încă acoperite.

## 3. Utilizatori și roluri

Contabil șef, Director financiar.

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul, completează antetul de depunere pe companie;
- Contabil/manager: verifică rândurile formularelor și validează fișierul înainte de depunere;
- Administratorul entității: semnează declarația de inactivitate și redactează secțiunile narative
  ale raportului administratorilor.

## 4. Conturi și date implicate

Modulul **nu generează note contabile** — citește soldurile prin rapoartele `l10n_ro_reports`.
Conturile implicate sunt cele din planul RO care alimentează rândurile de bilanț și de cont de
profit și pierdere (clasele 1–7), plus, pentru Formularul 30:

| Rând F30 | Conturi citite |
|---|---|
| Rezultatul exercițiului | clasa 7 − clasa 6 |
| Plăți restante — furnizori | 401, 403, 404, 408 cu scadență depășită |
| Plăți restante — buget | 44x cu scadență depășită (vezi nota de mai jos) |
| Plăți restante — împrumuturi | 162, 167, 519 cu scadență depășită |
| Dobânzi și dividende | 666, 766, 457 |
| Creanțe / datorii pe scadențe | conturi de tip creanță / datorie, împărțite la 1 an |

> **Două limite de citit înainte de a valida cifrele.** Rândul „plăți restante — buget" caută
> conturile care încep cu `44`, deci include și conturile de TVA (4426/4427/4428); în practică
> acestea sunt eliminate de filtrul pe sold nereconciliat, dar verificați-le. Iar **plățile
> restante și creanțele/datoriile pe scadențe folosesc soldul rezidual de astăzi**, nu pe cel de
> la 31 decembrie: dacă depuneți în mai, încasările din ianuarie–mai reduc retroactiv cifrele.

Pentru **declarația de inactivitate**, singurele conturi pe care le poate atinge o entitate fără
activitate sunt cele ale capitalului social: 1011/1012 (capital subscris), 104 (prime de capital),
456 (decontări cu asociații), 512/531 (vărsarea capitalului) și 581 (viramente interne). Capitalul
declarat se precompletează din soldul creditor 1011 + 1012.

Date minime pentru demo:
- companie românească cu localizarea contabilă instalată și exercițiul închis;
- facturi client și furnizor postate în exercițiul raportat;
- antetul de depunere completat pe companie (vezi Pasul 1).

## 5. Configurare inițială

1. Instalați modulul `l10n_ro_financial_statements` pe baza demo (aduce după el `l10n_ro_reports`
   și `l10n_ro_anaf_base`).
2. Completați **antetul de depunere** pe companie — vezi Pasul 1; fără el exportul se oprește.
3. Verificați că adresa fiscală a companiei e completă (stradă, oraș, cod poștal, județ, țară) și
   că are CUI și număr de înregistrare la Registrul Comerțului.
4. Postați toate documentele exercițiului. **Generați situațiile financiare ÎNAINTE de nota
   anuală de închidere prin 121** — vezi avertismentul de la Pasul 6.
5. Verificați că utilizatorul de test are grupul **Contabilitate / Consilier**.

## 6. Flux de utilizare

### Pasul 1 — Completarea antetului de depunere

Accesați **Contabilitate → Configurare → Setări**, secțiunea **„Situații financiare anuale
România"**.

Documentul cerut de ANAF are în antet 22 de atribute obligatorii. O parte se deduc singure (luna,
bifa de aprobare), o parte se iau din datele companiei (CUI, Registrul Comerțului, CAEN, județ),
iar restul — cele de aici — nu se pot deduce din contabilitate:

![Configurarea antetului de depunere în setările de contabilitate](screenshots/01_configurare_antet.png)

- **Formă de proprietate** ① — nomenclatorul ANAF (ex. „SC cu raspundere limitata").
- **Administrator** și **Întocmitor** — numele așa cum apar pe situațiile depuse, plus calitatea
  întocmitorului (director economic, contabil șef, membru CECCAR etc.).
- **Cod CAEN** — se completează doar dacă modulul OCA `l10n_ro_config` nu e instalat; când e
  instalat, codul de pe partenerul companiei are prioritate.
- **Entitate de interes public** și **bifele din antetul ANAF** — validatorul ANAF nu poartă
  semnificația acestor bife; se completează după formularul oficial. Excepție: **bifaMC** =
  mare contribuabil; când e bifată, județul de depunere (`codJJ`) devine 41 (DGAMC).
- **Județul de depunere (`codJJ`)** nu se configurează: este județul sediului (`codTT`) sau 41
  pentru marii contribuabili.

> **Șase câmpuri opresc exportul dacă lipsesc:** codul CAEN, numărul de la Registrul Comerțului,
> forma de proprietate, numele administratorului, numele și calitatea întocmitorului. Mesajul de
> eroare le enumeră exact. Restul (bifele, entitate de interes public, nr. CECCAR) nu
> blochează, dar se completează după formularul oficial.

### Pasul 2 — Verificarea Bilanțului (F10)

Accesați **Contabilitate → Raportare → Rapoarte de extras → Situații financiare anuale**. Raportul
are patru tab-uri ①, în ordinea din documentul de depunere: **Cod 10 - Bilanț**, **Cod 20 - Contul de
profit și pierdere**, **Cod 30 - Date informative (pre-completare)** și **Cod 40 - Situația activelor
imobilizate**. Rămâneți pe primul tab, **Cod 10 - Bilanț**.

**Găsiți pe ecran:** fiecare rând poartă la final numărul din formular (`| 01`, `| 04`, …), iar
coloana „Soldul" arată valoarea la data selectată. Rândurile de total sunt îngroșate.

**Verificați:** raportul se deschide la data curentă — **setați 31 decembrie** a exercițiului
raportat din filtrul de dată (în captura de mai jos raportul e la data implicită). Apoi confirmați
că „ACTIVE IMOBILIZATE – TOTAL | 04", „ACTIVE CIRCULANTE – TOTAL | 11" și „CAPITALURI - TOTAL | 51"
corespund balanței de verificare de închidere.

![Bilanțul F10 cu butonul de depunere](screenshots/02_bilant_f10.png)

Sub bara de butoane apare o notă: formularul ANAF are **două coloane pe rând** (sold la începutul și
la sfârșitul exercițiului), iar fișierul de pre-completare duce doar coloana de închidere.

Butonul **„Export depunere ANAF (set complet)"** ② este cel care produce fișierul de depus; îl
folosiți la Pasul 6, după ce verificați toate formularele.

### Pasul 3 — Verificarea Contului de Profit și Pierdere (F20)

În același raport, deschideți tab-ul **Cod 20 - Contul de profit și pierdere**. Tab-ul arată exact
varianta din care se construiește documentul de depunere.

> ⚠️ Din meniul separat **Raportare → Profit și Pierdere**, Odoo poate deschide implicit varianta
> **micro-entitate** (8 rânduri). Documentul de depunere se construiește **exclusiv** din varianta
> din tab — dacă verificați pe cea micro, validați alte cifre decât cele depuse.

**Găsiți pe ecran:** rândurile numerotate `| 01` … `| 68`, cu „VENITURI TOTALE", „CHELTUIELI
TOTALE" și rezultatul net (profit sau pierdere) la final.

**Verificați:** perioada e exercițiul întreg, nu o lună; rezultatul net din F20 coincide cu
rezultatul afișat pe Formularul 30 la Pasul 4 și cu profitul care va ajunge pe contul 121 la
închidere.

![Contul de Profit și Pierdere F20](screenshots/03_cpp_f20.png)

### Pasul 4 — Formularul 30 „Date informative"

Deschideți tab-ul **Cod 30 - Date informative (pre-completare)**.

**Găsiți pe ecran:** rândurile derivate automat din contabilitate (rezultat, plăți restante,
dobânzi, dividende, creanțe și datorii pe scadențe) și, deasupra lor, **două bannere**:

![Formularul 30 cu bannerele de avertisment](screenshots/04_date_informative_f30.png)

- **Bannerul galben** enumeră rândurile care **nu ajung în fișier**, pentru că numărul lor oficial
  de rând nu e confirmat pentru anul fiscal. Listează doar rândurile **cu valoare nenulă** — cele pe
  zero nu induc în eroare, deci nu apar. Se completează manual în formularul ANAF.
- **Bannerul albastru** enumeră rândurile care se exportă, dar cu o parte din coloanele oficiale
  goale — de exemplu plățile restante către furnizori, unde putem deriva totalul, dar nu și
  defalcarea pe vechime.

**Verificați:** rezultatul de pe primele rânduri coincide cu F20; plățile restante corespund
facturilor cu scadență depășită la 31 decembrie; ați citit ambele bannere și știți ce aveți de
completat manual.

### Pasul 5 — Rândurile statistice, completate manual

Rândurile care nu se pot deriva din contabilitate (număr de salariați, structura capitalului
social, cheltuieli de cercetare-dezvoltare) se introduc manual. Apăsați, pe tab-ul Cod 30, butonul
**„Completează rânduri manuale"**.

Butonul creează, dacă nu există deja, câte un rând pentru fiecare poziție statistică, pe companie
și perioadă, și deschide lista editabilă:

![Rândurile statistice ale Formularului 30](screenshots/05_randuri_manuale_f30.png)

**Verificați:** numărul mediu de salariați corespunde statelor de plată / REVISAL; apăsarea
repetată a butonului nu creează duplicate. Valorile sunt legate de o **perioadă** — afișați
coloanele „Începutul perioadei" / „Sfârșitul perioadei" din selectorul de coloane (⚙) dacă vreți să
confirmați pe ecran că editați exercițiul corect.

### Pasul 6 — Generarea fișierului de depunere

Reveniți pe tab-ul **Cod 10 - Bilanț** și apăsați **„Export depunere ANAF (set complet)"**.

Înainte de a produce fișierul, modulul rulează **pre-validarea corelațiilor** — 290 din cele 303
reguli ANAF (totaluri = suma componentelor, inegalități, rândurile de profit/pierdere). Printre ele
e și ecuația bilanțieră (capitaluri = active − datorii), deci un bilanț dezechilibrat e prins aici.
Dacă formularul se contrazice, exportul se oprește și enumeră neconcordanțele, cu valoarea
așteptată și cea găsită.

> Mesajul separat „Bilanț dezechilibrat…" apare pe **exportul de pre-completare**, nu pe acest buton.

> Verificarea corelațiilor e necesară pentru că **validatorul ANAF pentru anul 2025 nu le mai
> aplică** — un formular cu totaluri greșite ar trece DUKIntegrator și ar rămâne greșit legal.

Fișierul rezultat este un singur document, cu formularele ca elemente și valorile ca atribute:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Bilant1003 xmlns="mfp:anaf:dgti:s1003:declaratie:v15"
            an="2025" luna="12" cui="14399840" den="SITUAȚII FINANCIARE SRL"
            regCom="J33/1234/2010" caen="6201" caenE="6201" AN_CAEN="2025"
            tipBIL="BS" codTT="33" codPP="35" interes_public="0"
            nume_admin="POPESCU ION" nume_intocmit="IONESCU MARIA" calit_intocmit="12"
            bifa_aprob="1" bifa_art27="0" totalPlata_A="0">
  <F10 F10_0041="0" F10_0042="133600" F10_0091="0" F10_0092="133600" …/>
  <F20 F20_0011="0" F20_0012="100000" F20_0692="40000" …/>
  <F30 F30_0011="1" F30_0012="40000" F30_0192="12" …/>
</Bilant1003>
```

Numele atributului e `F<formular>_<rând pe 3 cifre><coloană pe 1 cifră>`: `F30_0192` înseamnă
Formularul 30, rândul 019, coloana 2 — numărul mediu de salariați.

### Pasul 7 — Validarea la ANAF și depunerea

Încărcați fișierul în **DUKIntegrator** cu validatorul de bilanț corespunzător (S1003 pentru
bilanțul prescurtat) și depuneți-l prin SPV.

> Jar-urile de bilanț **nu vin** în kitul DUKIntegrator: se descarcă separat de pe site-ul ANAF,
> se copiază în folderul `lib/` al instalării și se șterge `config/versiuniCurente.txt`.

### Pasul 8 — Declarația de inactivitate: completarea și verificarea activității

Folosiți acest pas **numai** pentru o entitate care nu a desfășurat activitate de la constituire până
la sfârșitul exercițiului. Ea nu parcurge pașii 2–7, ci depune declarația în locul bilanțului.

**Contabilitate → Raportare → Rapoarte de extras → Declarație de inactivitate → Nou.**

![Declarația de inactivitate, cu avertismentul de activitate](screenshots/06_declaratie_inactivitate.png)

1. **Completați** *Sfârșitul exercițiului financiar*: 31.12 sau, la exercițiul diferit de anul
   calendaristic, data aleasă. Fișierul are oricum `luna="12"`, singura valoare pe care o admite
   validatorul S1046. *Tipul entității* este implicit „Operatori economici”.
2. **Găsiți pe ecran** *Capitalul social*, precompletat din 1011 + 1012, și *Administratorul*, preluat
   din antetul de la Pasul 1. Dacă subscrierea nu e înregistrată, completați capitalul după actul
   constitutiv. În captură, compania demo nu are notă de subscriere, așa că capitalul de 200 lei
   e introdus manual.
3. **Verificați avertismentul.** Banda galbenă și butonul **Linii de activitate** (marcate 1 și 2 în
   captură) apar când există linii contabile, din orice an până la sfârșitul exercițiului, pe alte
   conturi decât cele ale capitalului social. Fiecare linie e un **indiciu de activitate**, de
   analizat. Deschideți butonul și citiți liniile:
   - un comision bancar (627 = 5121), un onorariu (622 = 401), o amortizare (6811) sau cheltuielile de
     constituire plătite de asociat (6xx/201 = 4551) sunt, în practica uzuală, **activitate**.
     Entitatea depune atunci situațiile financiare (pașii 2–7), nu declarația;
   - un aport în natură sau o diferență de curs pe capitalul în valută nu e activitate în sine.
     Analizați-l, apoi continuați.

   Ordinul nu definește „activitatea”, iar avertismentul nu blochează exportul. Decizia și
   răspunderea sunt ale administratorului, luate împreună cu contabilul. În captură, compania demo
   are facturi, deci avertismentul arată 6 linii contabile, din 2 facturi. Exact acesta e cazul în
   care declarația **nu** trebuie depusă.
4. **Exportați** cu **Export XML ANAF (S1046)**. Fișierul se descarcă și rămâne atașat în chatter.
   Exemplul de mai jos e fixture-ul validat cu DUKIntegrator, nu compania din capturi:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<s1046 xmlns="mfp:anaf:dgti:s1046:declaratie:v1" luna="12" an="2025" Tip_soc="1"
       data_S="31.12.2025" cui="14399840" den="RO Company"
       adresa="Str. Test 1, Suceava SV 720001, Romania" telefon="0230123456"
       regCom="J33/1234/2010" bifaMC="0" tipBIL="DI" codTT="33" codJJ="33"
       capital="200" nume_declarant="POPESCU ION" totalPlata_A="200"/>
```

Pe ce să vă uitați în fișier:
- `codJJ` este egal cu `codTT` (județul sediului), sau 41 la marii contribuabili;
- `totalPlata_A`, suma de control, este egală cu `capital`;
- data are formatul `zz.ll.aaaa`.

Validatorul ANAF verifică aceste reguli (R11.1, R11.2, R16).

### Pasul 9 — Declarația de inactivitate: confirmarea, tipărirea și depunerea

Ordinea recomandată: export, confirmare, tipărire.

**Confirmă** verifică din nou datele obligatorii (nr. Registrului Comerțului, administratorul, județul)
și blochează editarea. Dacă există linii de activitate, confirmarea e permisă, dar lasă în chatter
nota „Confirmată deși există … înregistrări contabile…”. Așa decizia administratorului rămâne
documentată.

**Tipărește PDF** produce exemplarul de semnat, cu textul declarației pe propria răspundere.

![Declarația de inactivitate tipărită](screenshots/07_declaratie_inactivitate_pdf.png)

**Verificați** datele de identificare (CUI, nr. Registrul Comerțului, adresa, capitalul) față de
certificatul de înmatriculare. Apoi validați XML-ul în DUKIntegrator, care generează și PDF-ul de
depunere:

```bash
java -jar DUKIntegrator.jar -v S1046 declaratie.xml erori.txt
java -jar DUKIntegrator.jar -p S1046 declaratie.xml erori.txt
```

Ca la bilanț, `S1046Validator.jar` și `S1046Pdf.jar` se descarcă separat de pe site-ul ANAF, se
copiază în `lib/` și se șterge `config/versiuniCurente.txt`. Termenul de depunere este de 60 de zile
de la încheierea exercițiului.

### Pasul 10 — Raportul administratorilor: indicatorii

**Contabilitate → Raportare → Rapoarte de extras → Raportul administratorilor → Nou**, cu perioada
exercițiului, apoi **Calculează indicatorii**.

![Raportul administratorilor, tab-ul Indicatori](screenshots/08_raport_administratori_indicatori.png)

1. **Găsiți pe ecran** tab-ul **Indicatori**. Fiecare rând are valoarea pe exercițiul precedent și pe
   cel curent. Două coloane arată de unde vine valoarea:
   - **Sursa**: rândul oficial ANAF din documentul de depunere (de exemplu, „F10 rd. 009”);
   - **Rânduri pe raport**: același rând cu numărul de pe ecranul Cod 10 / Cod 20 (de exemplu,
     „Cod 10: | 11”).

   Cele două numerotări diferă: rândul oficial 009 (active circulante) apare pe ecran ca „| 11”.
   Verificați întotdeauna după coloana **Rânduri pe raport**.
2. **Verificați** pe ecranele de la pașii 2–4:

   | Indicator | Rând oficial (Sursa) | Pe ecran (Rânduri pe raport) |
   |---|---|---|
   | Cifra de afaceri netă | F20 rd.001 | Cod 20: \| 01 |
   | Venituri / Cheltuieli totale | F20 rd.062 / 063 | Cod 20: \| 60 / \| 61 |
   | Impozitul pe profit | F20 rd.066 | Cod 20: \| 64 |
   | Profit / (pierdere) net(ă) | F20 rd.069 − 070 | Cod 20: \| 67 − \| 68 |
   | Active circulante | F10 rd.009 | Cod 10: \| 11 |
   | Creanțe / Casa și conturi la bănci | F10 rd.006 / 008 | Cod 10: \| 08 / \| 10 |
   | Total active | F10 rd.004 + 009 + 010 | Cod 10: \| 04 + \| 11 + \| 12 |
   | Datorii ≤ 1 an / > 1 an | F10 rd.013 / 016 | Cod 10: \| 15 / \| 18 |
   | Capitaluri – total | F10 rd.049 | Cod 10: \| 51 |
   | Număr mediu de salariați | F30 rd.019 | rândul manual F30 de la Pasul 5 |

   *Profit / (pierdere) net(ă)* trebuie să coincidă cu rezultatul din Cod 20 și cu rândul
   „Profitul sau pierderea exercițiului” din Cod 10 (| 45 sold C / | 46 sold D). Cu soldul 121
   coincide doar după nota de închidere.
   Pentru numărul de salariați al exercițiului precedent, completați rândul manual F30 al anului
   respectiv.
3. **Citiți ratele** cu atenție: sunt orientative (lichiditate, îndatorare globală, solvabilitate
   patrimonială, marjă, ROE, ROA, CA pe salariat), iar OMFP nu le prescrie formula. Când numitorul e
   zero, rata apare 0.

> Rândurile sunt cele ale **bilanțului prescurtat** (S1003). La o microîntreprindere, „Impozitul pe
> profit” (rândul oficial 066, pe ecran „20. Impozitul pe profit | 64”) este 0. Impozitul pe veniturile
> microîntreprinderilor apare pe ecran pe „22. Alte impozite neprezentate la elementele de mai sus | 66”,
> deci la o microîntreprindere rezultatul brut minus „Impozitul pe profit” nu dă rezultatul net.

### Pasul 11 — Raportul administratorilor: secțiunile narative, confirmarea și tipărirea

Tab-urile **Dezvoltare și riscuri**, **Indicatori de performanță** și **Alte informații** conțin
secțiunile din OMFP 1802/2014. Prima secțiune se precompletează cu cifrele principale, **numai dacă
e goală**.

![Secțiunile narative de la pct. 489](screenshots/09_raport_administratori_sectiuni.png)

| Secțiune | Obligatorie |
|---|---|
| Dezvoltare, performanță și poziție (pct. 489) | da: o analiză, nu doar cifrele precompletate |
| Riscuri și incertitudini (pct. 489) | da |
| Indicatori-cheie (pct. 491 alin. 1) | în măsura necesară; cei nefinanciari sunt opționali la entitățile mici și micro (pct. 492) |
| Resurse necorporale esențiale (pct. 491 alin. 1^1) | entități mijlocii și mari |
| a) Dezvoltare previzibilă · b) Cercetare-dezvoltare · d) Sucursale | da; dacă nu e cazul, se scrie expres |
| c) Acțiuni proprii · e) Instrumente financiare | dacă au existat / dacă sunt semnificative |

**Confirmă** refuză raportul cât timp lipsește o secțiune obligatorie sau cât timp prima secțiune
conține doar textul precompletat. **Tipărește PDF** produce raportul de semnat de președintele
consiliului de administrație (pct. 490). La entitățile fără consiliu semnează, în practică,
administratorul.

![Raportul administratorilor tipărit](screenshots/10_raport_administratori_pdf.png)

**Verificați** în PDF că tabelul de indicatori corespunde situațiilor financiare depuse și că
secțiunile obligatorii nu apar cu mențiunea „(de completat)”. Raportul se scanează și se atașează,
alături de celelalte documente însoțitoare, la PDF-ul de depunere a bilanțului.

### Note de monografie și raportare

Modulul **nu generează note contabile**, nici pentru bilanț, nici pentru declarația de inactivitate
sau raportul administratorilor. El citește soldurile deja înregistrate și le transpune pe
rândurile formularelor. Ce salvează în bază nu are efect contabil: rândurile statistice F30,
declarațiile de inactivitate, rapoartele administratorilor și fișierele XML atașate.

> ⚠️ **Ordinea față de închiderea prin 121.** Contul de profit și pierdere și rândurile de rezultat
> din F30 se calculează din **rulajele** conturilor din clasele 6 și 7 pe perioada raportată. Nota
> anuală de închidere generată de `l10n_ro_account_return_pl_closing` se datează la **sfârșitul
> perioadei închise**, adică *în interiorul* exercițiului raportat, și golește tocmai aceste conturi.
> Dacă o postați înainte de a genera situațiile, F20 și rândurile de rezultat din F30 ies pe zero,
> în timp ce bilanțul arată profitul pe 121 — iar pre-validarea oprește exportul cu eroare de
> corelație între F10 și F20. Generați și arhivați documentul de depunere **înainte** de nota de
> închidere anuală, sau asigurați-vă că aceasta nu cade în perioada raportată.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `l10n_ro_reports` (Enterprise) | furnizează rapoartele „Cod 10 - Bilanț" și „Cod 20 - CPP" cu rândurile numerotate |
| `l10n_ro_anaf_base` | datele de identificare a companiei folosite în antet și validarea completitudinii lor |
| `l10n_ro_account_return_pl_closing` | închiderea 6xx/7xx prin 121, pre-condiție a rezultatului |
| `l10n_ro_financial_notes` | notele explicative 1–10, complementare formularelor; Nota 3 acoperă repartizarea profitului, document separat de raportul administratorilor |
| `l10n_ro_config` (OCA, opțional) | codul CAEN de pe partener; dacă lipsește, se folosește câmpul de rezervă de pe companie |

**Ce e automat:**
- valorile rândurilor F10, F20 și rândurile derivabile din F30;
- numerotarea oficială a rândurilor și antetul documentului;
- verificarea echilibrului și a corelațiilor;
- avertismentele despre ce nu ajunge în fișier;
- XML-ul S1046 al declarației de inactivitate, cu capitalul precompletat și verificarea liniilor de
  activitate;
- indicatorii raportului administratorilor, cu rândurile corespunzătoare de pe ecran, și prima
  secțiune precompletată.

**Ce rămâne manual:** decizia de eligibilitate pentru declarația de inactivitate; secțiunile narative
ale raportului administratorilor; rândurile statistice din F30; cele **14 poziții F30** fără număr oficial
confirmat; Formularul 40; validarea în DUKIntegrator și depunerea prin SPV.

> A nu se confunda cu cele **13 reguli** de corelație ANAF pe care pre-validarea nu le acoperă —
> sunt două numere diferite, despre lucruri diferite.

## 8. Verificări pentru consultant

- [ ] Antetul de depunere e completat pe companie (formă de proprietate, administrator, întocmitor).
- [ ] Adresa fiscală, CUI-ul și numărul de la Registrul Comerțului sunt complete.
- [ ] Documentul de depunere e generat **înainte** de nota anuală de închidere prin 121 (sau aceasta nu cade în perioada raportată).
- [ ] Pe Bilanț, data selectată e 31 decembrie a exercițiului raportat.
- [ ] Total Activ = Total Pasiv pe raportul Bilanț.
- [ ] Rezultatul net din F20 coincide cu rândul „Profitul sau pierderea exercițiului” din Cod 10
      (| 45 sold C / | 46 sold D) și cu rândurile de rezultat din F30; cu soldul 121 doar după nota de închidere.
- [ ] Ambele bannere de pe F30 au fost citite, iar rândurile enumerate sunt notate pentru
      completare manuală în formularul ANAF.
- [ ] Rândurile statistice F30 sunt completate (număr de salariați cel puțin).
- [ ] Exportul „Export depunere ANAF (set complet)" se termină fără eroare de corelație.
- [ ] Fișierul generat trece validatorul ANAF în DUKIntegrator.
- [ ] Fișierul XML e arhivat împreună cu PDF-ul raportului (Legea 82/1991 — 10 ani).
- [ ] Declarația de inactivitate: butonul „Linii de activitate” lipsește sau liniile listate sunt doar
      operațiuni de capital analizate; altfel se depun situații financiare, nu declarație.
- [ ] Declarația de inactivitate: capitalul social coincide cu actul constitutiv, iar XML-ul S1046 trece
      DUKIntegrator fără erori.
- [ ] Raportul administratorilor: cifra de afaceri, total active și rezultatul net din tab-ul Indicatori
      coincid cu rândurile din coloana „Rânduri pe raport” pe ecranele Cod 10 / Cod 20.
- [ ] Raportul administratorilor: secțiunile pct. 489 și pct. 491 alin. (2) a), b), d) sunt completate,
      iar raportul e confirmat.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| „Antetul depunerii ANAF e incomplet pentru compania … Completați, în setările de contabilitate: …" | Lipsesc câmpuri obligatorii de antet | Completați câmpurile enumerate în mesaj (Pasul 1) |
| „Bilanț dezechilibrat: Total Activ … ≠ Total Pasiv …" | Balanța de verificare nu se închide | Verificați balanța și închiderea prin 121 înainte de export |
| „Situațiile financiare își contrazic propriile totaluri…" | Un total nu corespunde componentelor lui | Mesajul enumeră regulile încălcate, cu valoarea așteptată și cea găsită; verificați formulele raportului și balanța |
| „Compania … nu are configurat un cod CAEN" | Lipsește codul CAEN | Completați-l pe partenerul companiei (`l10n_ro_config`) sau în câmpul de rezervă din setări |
| „Declarația de inactivitate nu poate fi generată pentru compania … Completați: …" | Lipsește nr. Registrului Comerțului sau administratorul | Completați câmpurile enumerate (antetul de la Pasul 1) |
| „Compania … nu are configurat un județ/stat valid din România." | Adresa companiei fără județ | Completați județul pe compania (adresa fiscală) |
| „ANAF respinge valorile mai lungi decât permite formularul: …" | Denumirea/adresa > 200 caractere, telefonul > 15, nr. ORC > 18, administratorul > 75 | Scurtați valoarea indicată |
| „Există deja o declarație de inactivitate pentru această companie și acest exercițiu financiar." | Al doilea record pe același exercițiu | Deschideți declarația existentă |
| „Raportul administratorilor trebuie să prezinte: …" | Lipsește o secțiune obligatorie | Completați secțiunile enumerate; dacă nu e cazul, scrieți expres („Entitatea nu are sucursale”) |
| „Secțiunea privind dezvoltarea conține doar cifrele precompletate…" | Prima secțiune n-a fost redactată | Adăugați analiza propriu-zisă a activității |
| „Calculați indicatorii înainte de confirmarea raportului." | Confirmare fără indicatori | Apăsați **Calculează indicatorii** |
| „Niciun validator ANAF nu e mapat pentru tipul de bilanț …" | S-a cerut bilanț complet (BL) sau simplificat (UU) | Deocamdată e acoperit doar bilanțul prescurtat (BS / S1003) |

## 10. Capturi de ecran

Capturile sunt **generate automat** din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din
`l10n_ro_doc_screenshots`, import defensiv), în limba română, pe planul de conturi RO.

| Fișier | Conținut |
|---|---|
| `01_configurare_antet.png` | Setările de contabilitate, blocul „Situații financiare anuale România" |
| `02_bilant_f10.png` | Bilanțul F10 cu butonul de depunere și nota despre coloana de deschidere |
| `03_cpp_f20.png` | Contul de Profit și Pierdere F20 |
| `04_date_informative_f30.png` | Formularul 30 cu cele două bannere de avertisment |
| `05_randuri_manuale_f30.png` | Lista rândurilor statistice completate manual |
| `06_declaratie_inactivitate.png` | Declarația de inactivitate, cu avertismentul și butonul „Linii de activitate” |
| `07_declaratie_inactivitate_pdf.png` | Declarația de inactivitate tipărită (PDF) |
| `08_raport_administratori_indicatori.png` | Raportul administratorilor: tab-ul Indicatori, cu rândul oficial și rândul de pe ecran pentru fiecare valoare |
| `09_raport_administratori_sectiuni.png` | Raportul administratorilor — secțiunile narative de la pct. 489 |
| `10_raport_administratori_pdf.png` | Raportul administratorilor tipărit (PDF) |

Regenerare:

```bash
FISE_SCREENSHOTS=1 ./odoo/odoo-bin -c odoo.conf -d <db> \
    -i l10n_ro_financial_statements,l10n_ro_doc_screenshots --without-demo=all \
    --test-tags=/l10n_ro_financial_statements:TestFinancialStatementsScreenshots --stop-after-init
```

> Rulați pe o bază curată, nu pe una cu toată suita instalată: pagina de setări se randează cu
> toate blocurile de configurare din baza respectivă, iar un modul nerelevant cu o eroare de view
> face captura să eșueze.

## 11. Observații pentru manual

- Insistați pe **Pasul 1**: antetul de depunere e o configurare unică, dar blochează tot fluxul
  dacă lipsește. Merită un tabel cu cele 11 câmpuri și de unde se ia fiecare valoare, marcând clar
  care șase sunt blocante.
- Explicați diferența dintre **cele două butoane**: „Export depunere ANAF (set complet)" produce
  fișierul de depus; „Export XML ANAF (pre-completare, un formular)" produce un fișier de lucru pe
  un singur formular, **care nu se depune**.
- Cele două bannere de pe F30 nu sunt decor: ele sunt singurul loc în care se vede diferența dintre
  ce arată ecranul și ce ajunge în fișier. Manualul ar trebui să ceară explicit citirea lor.
- Menționați că numerotarea rândurilor și regulile de corelație se **regenerează din validatorul
  ANAF** la fiecare republicare; e o sarcină recurentă de mentenanță, nu una de implementare.
- Declarația de inactivitate: subliniați că eligibilitatea curge **de la constituire**. Cea mai
  frecventă greșeală e depunerea ei de o firmă care a avut activitate într-un an anterior. Captura
  de la Pasul 8 arată tocmai avertismentul pentru acest caz.
- Raportul administratorilor: manualul ar trebui să dea un exemplu de analiză pentru pct. 489, nu
  doar cifrele precompletate. Confirmarea le refuză, iar PDF-ul marchează secțiunile obligatorii
  goale cu „(de completat)”.
