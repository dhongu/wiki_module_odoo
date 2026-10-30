# Fișă Modul: Încărcarea balanței de verificare din PDF cu AI, la intrarea în Odoo

**Modul:** `deltatech_ai_trial_balance_import`
**Utilizator principal:** Contabil șef / consultant de implementare (preluarea soldurilor la go-live)
**Prioritate:** 🟡 Medie (scurtează preluarea soldurilor; soldurile se postează tot prin sincronizarea planului de conturi, după verificare)

---

## 1. Scop business

La intrarea în Odoo, soldurile trebuie să fie exact cele din balanța de verificare a programului
anterior la data trecerii. Balanța vine de obicei ca **PDF** tipărit din celălalt program, iar
transcrierea ei de mână în sincronizarea planului de conturi (modulul
`deltatech_chart_of_accounts`) durează și produce greșeli.

Modulul citește PDF-ul balanței cu un agent AI și scrie rândurile ca **sume externe** în
sincronizare. Agentul doar transcrie rândurile. Restul îl face Odoo, determinist: potrivește
conturile și partenerii, verifică fiecare rând, fiecare total tipărit și egalitatea debit = credit,
apoi caută sumele în textul PDF-ului. Contabilul revizuiește rândurile și abia apoi le aplică.
Nimic nu se postează automat: diferența se postează din sincronizare, ca la un import manual.

## 2. Bază legală și context

- **Legea contabilității nr. 82/1991, art. 6 alin. (1):** orice operațiune se consemnează într-un
  document justificativ. Pentru nota de ajustare postată din sincronizare, documentul justificativ
  rămâne **balanța de verificare a programului anterior** la data trecerii, semnată. PDF-ul încărcat
  rămâne atașat importului, pe sincronizare (tabul **Importuri PDF**), cu cine l-a aplicat și când.
- **OMFP 1802/2014, pct. 54 alin. (1) (intangibilitatea):** bilanțul de deschidere al exercițiului
  corespunde bilanțului de închidere al exercițiului precedent. Preluarea nu schimbă valori, ci le
  transferă: balanța din Odoo la data trecerii trebuie să fie identică cu cea din PDF.
- **Context operațional:** PDF-ul (conturi, parteneri, coduri fiscale, sume) se trimite
  furnizorului AI configurat în **Setări → AI**. Verificați termenii lui de prelucrare a datelor
  înainte de activare. Modulul e **dezactivat implicit** pe fiecare companie.

## 3. Utilizatori și roluri

| Rol | Ce face | Drept recomandat la test |
|---|---|---|
| Contabil șef / consultant de implementare | activează importul, încarcă PDF-ul, revizuiește rândurile, aplică balanța și postează diferența | Contabilitate: Administrator |
| Administrator Odoo | setează cheia furnizorului AI și, opțional, modelul agentului | Administrare: Setări |

Sincronizarea planului de conturi (meniul și butonul **Încarcă balanța din PDF (AI)**) cere grupul
**Contabilitate: Administrator** (`account.group_account_manager`).

## 4. Conturi și date implicate

| Cont | Rol |
|---|---|
| orice cont din balanța PDF | primește soldul din PDF ca sumă externă a liniei de sincronizare |
| 411100 Clienți / 401100 Furnizori | pe parteneri, dintr-o balanță analitică pe parteneri, pe o sincronizare cu **Detaliu pe partener** |
| 121000 Profit sau pierdere | **Cont de echilibrare** implicit al sincronizării; primește linia „Diferență” când nota nu se închide sau când balanța are sold pe 121 (vezi „Soldul contului 121 la data trecerii”) |
| 473000 Decontări din operațiuni în curs de clarificare | cont de echilibrare recomandat pentru sincronizările pe un singur cont de terți |
| jurnal de tip Diverse | jurnalul notei de ajustare (în exemplu *Solduri inițiale*, cod SOLD) |

Date pentru demo (aceleași în toate capturile). Firma intră în Odoo la 01.01.2026. În Odoo există
deja o notă cu soldurile preluate parțial, iar balanța PDF a programului anterior la 31.12.2025 are
trei pagini:

| Cont din PDF | Cont Odoo | Sold Odoo | Sold în PDF | Diferență |
|---|---|---|---|---|
| 1012 Capital subscris vărsat | 101200 | 14.000,00 C | 14.000,00 C | — |
| 1171 Rezultatul reportat | 117100 Rezultatul reportat reprezentând profitul nerepartizat sau pierderea neacoperită | — | 550,00 C | 550,00 C |
| 371 Mărfuri | 371000 | 2.000,00 D | 1.800,00 D | 200,00 C |
| 401 Furnizori | 401100 Furnizori - reluate într-o perioadă de până la un an (ales de utilizator) | 3.000,00 C | 3.200,00 C | 200,00 C |
| 4111 Clienți | 411100 | 5.000,00 D | 5.950,00 D | 950,00 D |
| — (lipsește din PDF) | 461000 Debitori diverși | 300,00 D | 0 | 300,00 C |
| 5121 Conturi la bănci în lei | 512100 | 9.700,00 D | 10.000,00 D | 300,00 D |
| **Total** | | **17.000 = 17.000** | **17.750 = 17.750** | |

Planul de conturi RO din Odoo are coduri de 6 cifre. Compania de test are mai multe conturi pe
prefixele 401, 4111 și 5121 (de exemplu 401100 și 401200, 411100 și 411101), deci aceste rânduri
cer o alegere sau o confirmare (Pasul 6). Rândul sintetic 401 merge pe 401100 (4011, datorii
curente față de furnizori); datoriile cu scadență peste un an se separă pe 401200 (4012).

Pentru balanța analitică pe parteneri a contului 4111 (Pasul 7), partenerii din Odoo sunt: Client
Alfa SRL (CUI RO12345674), Beta Distribuție SRL (fără CUI), Ion Popescu, Client Omega SRL (CUI
RO31987654). În PDF apar și GAMA CONSTRUCT S.R.L. (CUI 28765437), care nu există în Odoo, și CLIENT
OMEGA S.R.L. cu CUI-ul transcris greșit (31987645). Cele două exemple folosesc sincronizări separate
și nu se cumulează.

## 5. Configurare inițială

1. Instalați `deltatech_ai_trial_balance_import`. Cere Odoo Enterprise cu modulul **AI** și
   modulul `deltatech_chart_of_accounts` (instalat automat ca dependență).
2. În **Setări → AI**, setați cheia furnizorului AI.
3. În **Facturare → Configurare → Setări** (cu modulul Accountant, aplicația se numește
   **Contabilitate**), secțiunea **Intrare în Odoo**, bifați **Import balanță PDF cu AI** și
   ajustați **Limită zilnică AI balanțe** (implicit 20 de balanțe pe zi pe companie; 0 = fără
   limită). Salvați.

   ![Setarea Import balanță PDF cu AI, în secțiunea Intrare în Odoo](screenshots/01_setari_import_balanta_ai.png)

4. Opțional, în **AI → Agenți → Trial Balance PDF Reader AI**, alegeți **Model LLM**. Modelul
   trebuie să accepte fișiere PDF (implicit GPT-4o). Numele și subtitlul agentului sunt în engleză. Instrucțiunile agentului spun că documentul e
   doar date: agentul nu execută instrucțiuni scrise în PDF.

   ![Agentul AI care citește balanța, cu modelul ales](screenshots/02_agent_ai.png)

5. Opțional, parametrii de sistem (**Setări → Tehnic → Parametri de sistem**):
   `deltatech_ai_trial_balance_import.timeout` (secunde de așteptare pentru un răspuns, implicit
   300), `deltatech_ai_trial_balance_import.pages_per_call` (pagini citite într-o cerere, implicit
   1) și `deltatech_ai_trial_balance_import.parallel_calls` (pagini citite simultan, implicit 3).
6. Pregătiți jurnalul de tip Diverse pentru nota de ajustare și verificați că toate conturile din
   balanța PDF există în Odoo (vezi fișa modulului `deltatech_chart_of_accounts`).

## 6. Flux de utilizare

### Pasul 1 — Crearea sincronizării

**Facturare → Configurare → Contabilitate → Sincronizare plan de conturi**, butonul **Nou(ă)**.
Completați **Nume**, **Data** (data balanței, aici 31.12.2025), **Jurnal** și **Mod de postare**
(**Doar solduri de deschidere** pentru go-live). Pentru o balanță sintetică lăsați **Detaliu pe
partener** nebifat. Pentru o balanță pe parteneri bifați-l și, de regulă, completați **Cont**
(Pasul 7). Salvați și apăsați **Generează liniile**: sincronizarea primește soldurile din Odoo la
dată, iar importul poate arăta, înainte de aplicare, ce linii lipsesc din PDF și primesc 0. Fără
linii generate, bannerul albastru al importului spune doar că liniile se vor genera la aplicare.
Apoi apăsați **Încarcă balanța din PDF (AI)**, vizibil doar cât sincronizarea e în **Ciornă**.

![Sincronizarea în ciornă: Generează liniile, apoi Încarcă balanța din PDF (AI)](screenshots/03_sincronizare_incarca_pdf.png)

### Pasul 2 — Alegerea PDF-ului și a coloanei de încărcat

Se deschide formularul **Import balanță PDF**, în starea **De citit**. Completați:

- **Balanța de verificare (PDF)**: fișierul tipărit din celălalt program. Un fișier care nu e PDF
  e refuzat; o balanță CSV sau Excel se importă din lista liniilor sincronizării.
- **Încarcă**: perechea de coloane scrisă ca debit / credit extern. **Solduri finale** pentru
  go-live la data balanței (implicit). **Sume totale** când sincronizarea are modul **Potrivește
  totalurile debit/credit** (propus automat). **Solduri inițiale** pentru o balanță la începutul
  anului. Data sincronizării este atunci ziua dinaintea perioadei balanței, deci avertizarea de
  dată (Pasul 4) este de așteptat: bifați-o după verificare.
- **Pune 0 când lipsește**: liniile sincronizării care nu apar în PDF primesc 0 ca sume externe.
  **Toate liniile sincronizării** pentru o balanță completă (implicit), **Doar conturile citite din
  PDF** pentru o balanță pe parteneri (propus automat), **Niciuna**.

Apăsați **Citește cu AI**. Bannerul albastru amintește că nimic nu se scrie în sincronizare
înainte de aplicare și că nimic nu se postează.

![Importul de citit: PDF-ul, coloana încărcată și liniile puse pe 0](screenshots/04_import_pdf_de_citit.png)

### Pasul 3 — Citirea pagină cu pagină

O balanță de mai multe pagini se citește pe părți (implicit o pagină pe cerere), cu dialogul
**Citirea balanței de verificare cu AI**: bara de progres, părțile citite, rândurile găsite și
timpul rămas. **Oprește după părțile în curs** oprește citirea; o parte care eșuează se reia cu
**Citește părțile rămase**. La final, rândurile se deschid în formularul importului.

Un document citit consumă o unitate din limita zilnică. Recitirea doar a unor pagini nu se
numără. Recitirea tuturor paginilor se numără ca un document nou.

![Dialogul de progres: 2 din 3 pagini citite](screenshots/05_progres_citire.png)

### Pasul 4 — Citirea rezultatului și erorile

Importul trece în **Citit**. Citiți ecranul de sus în jos:

1. **Găsiți pe ecran:**
   - în dreapta, ce a citit agentul din antet: **Tip balanță** (Sintetică / Analitică), **Firma
     (PDF)**, **Cod fiscal (PDF)**, perioada și totalurile **Debit de aplicat** / **Credit de
     aplicat**;
   - bannerul **roșu** **Erori (blochează aplicarea balanței)**, bannerul **galben** **Avertizări**
     și bannerul **albastru** cu liniile care vor primi 0. Bannerul galben spune doar câte rânduri
     au avertizări; textul avertizării de rând se citește în coloana **Avertizare** a tabului
     **Rânduri** (sau în lista **De verificat**, cu filtrul **Cu avertizări**), de exemplu
     „Negăsit în PDF, de verificat: …” (suma sau codul nu se găsește în textul paginii);
   - tabul **Rânduri**: fiecare rând tipărit, cu **Pagina**, **Cod (PDF)**, **Denumire (PDF)**,
     soldurile, **Cont** potrivit, **Stare**, **Potrivire** și **Eroare**. Rândurile de total
     (gri) doar verifică; se aplică doar rândul cel mai detaliat al fiecărui cont.
2. **Verificați:**
   - **Firma (PDF)** și **Cod fiscal (PDF)** sunt ale companiei, iar **Sfârșitul perioadei** este
     data sincronizării (altfel apare o avertizare);
   - **Debit de aplicat** = **Credit de aplicat** pe o balanță sintetică;
   - nu există erori. În exemplu, agentul a citit pe pagina 2 soldul lui 4111 ca 5.590,00 în loc
     de 5.950,00: rândul 4111 are eroarea „Sumele totale D - C (5.950,00) diferă de soldul final
     D - C (5.590,00).”, totalul clasei 4 și totalul general nu se închid, iar bannerul roșu arată
     „Sold final: debitul 17.390,00 nu este egal cu creditul 17.750,00.”. Rândul are și
     avertizarea „Negăsit în PDF, de verificat: Sold final D 5.590,00.”,
     pentru că 5.590,00 nu este tipărit pe pagina 2.
3. **Corectați:** apăsați **Recitește paginile cu erori**: doar pagina 2 se citește din nou, iar
   alegerile de pe celelalte pagini se păstrează. Alternativ, corectați suma direct în rând și
   apăsați **Verifică din nou**, sau alegeți paginile în **Pagini de recitit** și apăsați
   **Recitește paginile selectate**. **Recitește** citește tot PDF-ul și pierde corecturile.

![Balanța citită cu erori: rândul 4111 citit greșit pe pagina 2](screenshots/06_balanta_cu_erori.png)

### Pasul 5 — Balanța fără erori: ce mai e de verificat

După recitire, bannerul roșu dispare.

1. **Găsiți pe ecran:** butonul **De verificat** din colțul de sus (aici 3 rânduri), bannerul
   albastru și coloana **Stare**: **Potrivit** (verde), **De confirmat** și **Ambiguu**
   (portocaliu), **Cont lipsă** / **Partener lipsă** / **Eroare** (roșu), **Total** și **Exclus**
   (gri).
2. **Verificați:**
   - bannerul albastru listează liniile sincronizării care lipsesc din PDF și primesc 0. În
     exemplu: 461000 (300,00 în Odoo, absent din balanța programului anterior) și 401100, doar
     pentru că rândul 401 nu are încă un cont ales. Fiecare cont din listă trebuie să fie, într-adevăr,
     fără sold în balanța PDF;
   - **Debit de aplicat** = **Credit de aplicat** = totalul general din PDF (17.750,00).

![Balanța fără erori, cu rândurile de verificat și liniile puse pe 0](screenshots/07_balanta_de_verificat.png)

### Pasul 6 — Rezolvarea rândurilor de verificat

Apăsați **De verificat**. Lista **Rânduri balanță** se deschide filtrată pe rândurile de rezolvat.
Conturile se potrivesc astfel:

- un cod reținut la o balanță aplicată anterior (aceeași companie) se folosește direct;
- codul identic din Odoo se folosește direct;
- un cod care este prefixul unui singur cont (1012 → 101200) se folosește direct;
- dacă mai multe conturi încep cu codul, contul completat cu zerouri (4111 → 411100) este doar
  **propus** (**De confirmat**); dacă nu există, rândul rămâne **Ambiguu** și contul se alege;
- un cont analitic al celuilalt program (5121.01) se alege o dată.

Pe fiecare rând:

- **Ambiguu** sau **Cont lipsă**: alegeți contul în coloana **Cont** (lista propune candidații).
  Aici: 401 → 401100 Furnizori - reluate într-o perioadă de până la un an.
- **De confirmat**: verificați contul propus și apăsați bifa **Confirmă** de pe rând, sau
  **Confirmă propunerile** pe import pentru toate. Alegerea altui cont confirmă și ea rândul.
- un rând care nu trebuie aplicat se scoate cu comutatorul **Exclude**.

Alegerile se rețin la aplicare pentru balanțele următoare ale aceleiași companii. Reveniți pe
import (calea de navigare) și apăsați **Verifică din nou**: bannerul albastru se recalculează (aici
rămâne doar 461000).

![Rândurile de verificat: 401 ambiguu, 4111 și 5121 propuse](screenshots/08_randuri_de_verificat.png)

### Pasul 7 — Varianta: balanța analitică pe parteneri

Pentru conturile de terți, încărcați balanța analitică pe parteneri a contului pe o sincronizare cu
**Detaliu pe partener** bifat și **Cont** completat (aici 411100, cu **Cont de echilibrare**
473000). Ordinea dintre sincronizările pe parteneri și sincronizarea globală este cea din fișa
modulului `deltatech_chart_of_accounts`. **Pune 0 când lipsește** trece automat pe **Doar conturile
citite din PDF**. În exemplu, balanța sintetică a fost aplicată înainte, deci 4111 se potrivește
direct cu 411100 din alegerea reținută atunci. Dacă balanța pe parteneri se încarcă prima, 4111
apare **De confirmat**, ca la Pasul 6.

Partenerii se potrivesc după regulile modulului `deltatech_partner_match`, în ordinea:

- **codul fiscal** (CUI, CNP, cod de TVA UE), fără prefixul de țară și fără zerourile din față,
  doar dacă cifra de control e corectă. Exemplu: CUI 12345674 → Client Alfa SRL. Dacă mai mulți
  parteneri au același cod fiscal, se departajează după nume; altfel rândul rămâne **Ambiguu**;
- **numele exact**, fără diacritice, punctuație și formă juridică, cu **ordinea cuvintelor
  păstrată**. Exemplu: BETA DISTRIBUTIE S.R.L. → Beta Distribuție SRL. Dacă partenerul găsit are
  în Odoo alt cod fiscal decât cel din PDF, rândul devine **De confirmat** („Același nume, alt cod
  fiscal în Odoo.”);
- un **nume apropiat** (cuvintele în orice ordine, cu mici greșeli) este doar **propus**. Exemplu:
  POPESCU ION → Ion Popescu, **De confirmat**. Mai multe nume apropiate lasă rândul **Ambiguu**;
- altfel, **Partener lipsă**. Partenerul nu se creează automat.

Pe ecran:

1. **Găsiți pe ecran:** bannerul galben, bifa **Am verificat avertizările** și coloanele **Partener
   (PDF)**, **Cod fiscal (PDF)**, **Partener**, **Stare**, **Potrivire** și **Avertizare**
   (**Avertizare** e afișată implicit; **Cod fiscal (PDF)** se activează din selectorul de coloane).
2. **Verificați:**
   - avertizarea „Sincronizarea are detaliu pe partener, dar 411100 sunt citite fără parteneri”
     apare cât timp un rând de partener nu are partener (aici GAMA CONSTRUCT); dispare după
     rezolvarea lui și **Verifică din nou**;
   - avertizarea de rând (aici CLIENT OMEGA S.R.L., în coloana **Avertizare**: „Codul fiscal
     31987645 nu este valid: partenerul este potrivit doar după nume.”):
     CUI-ul citit nu trece de cifra de control, deci nu e folosit; partenerul s-a potrivit după
     nume. Comparați CUI-ul cu PDF-ul;
   - suma rândurilor de parteneri este egală cu totalul contului 4111 (5.950,00).

   După verificare, bifați **Am verificat avertizările**. Fără bifă, balanța cu avertizări nu se
   aplică.

![Balanța pe parteneri a contului 4111: potriviri după CUI și nume, cu avertizări](screenshots/09_balanta_parteneri.png)

Apăsați **De verificat**: rămân POPESCU ION (**De confirmat**, bifa **Confirmă** pe rând) și GAMA
CONSTRUCT S.R.L. (**Partener lipsă**). Iconița **Creează partener** creează partenerul din numele
și CUI-ul din PDF (dacă CUI-ul e refuzat de validarea Odoo, partenerul se creează doar cu numele).
Partenerul se creează mereu ca firmă și fără țară: verificați-i fișa (tipul, pentru o persoană
fizică, și țara).
Alternativ, alegeți un partener existent în coloana **Partener**.

![Rândurile de verificat pe parteneri: nume apropiat și partener lipsă](screenshots/10_parteneri_de_verificat.png)

### Pasul 8 — Aplicarea pe sincronizare

Pe import, apăsați **Aplică pe sincronizare**. Butonul refuză aplicarea dacă există erori, rânduri
de verificat sau avertizări nebifate. Modulul:

- generează liniile sincronizării cu soldurile din Odoo (dacă nu există);
- scrie rândurile aplicate ca **Debit Extern** / **Credit Extern**, pe cont (și partener); două
  rânduri pe același cont și partener se adună;
- pune 0 pe liniile care lipsesc din PDF, după **Pune 0 când lipsește**;
- reține conturile alese pentru următoarele balanțe;
- trece importul în **Aplicat** și deschide lista liniilor sincronizării.

1. **Găsiți pe ecran:** coloanele **Sold** (din Odoo) și **Sold Extern** (din PDF). Sumele externe
   diferite de cele din Odoo apar cu roșu, cele egale cu albastru.
2. **Verificați:** totalurile **Debit Extern** și **Credit Extern** sunt egale cu totalul general
   din PDF (17.750,00), totalul **Sold Extern** este 0,00, iar fiecare rând roșu este o diferență
   explicată (aici 117100, 371000, 401100, 411100, 461000 pus pe 0 și 512100).

![Liniile sincronizării după aplicare (în captură, doar liniile cu sume)](screenshots/11_linii_sincronizare.png)

În captură sunt ascunse liniile planului fără nicio sumă; lista reală le conține pe toate.

### Pasul 9 — Verificarea și postarea diferenței

Reveniți pe sincronizare.

1. **Găsiți pe ecran:** **Sold Odoo**, **Sold Extern**, bifa **Echilibrat** și tabul **Importuri
   PDF** cu importul aplicat: fișierul, tipul balanței, data, debitul și creditul aplicate, **Aplicat
   de** și **Data aplicării**.
2. **Verificați:** **Echilibrat** este bifat. Fără bifă, sumele externe nu sunt echilibrate și nota
   ar primi o linie „Diferență” pe contul de echilibrare. Corectați înainte de postare.
3. Apăsați **Postează diferența**: se creează și se validează nota de ajustare în jurnalul ales, la
   data sincronizării, iar sincronizarea trece în **Postat**.

![Sincronizarea echilibrată, cu importul PDF aplicat](screenshots/12_sincronizare_aplicata.png)

![Nota de ajustare postată din sincronizare](screenshots/13_nota_diferenta.png)

### Note de monografie și raportare

Modulul nu postează note. Nota de mai jos este generată de `deltatech_chart_of_accounts` la
**Postează diferența**, în modul **Doar solduri de deschidere**, din sumele externe scrise de
import (exemplul din secțiunea 4, la 31.12.2025, jurnalul SOLD):

| Cont | Debit | Credit |
|---|---|---|
| 371000 Mărfuri | | 200,00 |
| 401100 Furnizori - reluate într-o perioadă de până la un an | | 200,00 |
| 411100 Clienți | 950,00 | |
| 461000 Debitori diverși | | 300,00 |
| 512100 Conturi la bănci în lei | 300,00 | |
| 117100 Rezultatul reportat reprezentând profitul nerepartizat sau pierderea neacoperită | | 550,00 |
| **Total** | **1.250,00** | **1.250,00** |

Regula: diferența dintre soldul din PDF și cel din Odoo; spre debit, se înregistrează în debit,
spre credit, în credit. Ambele balanțe sunt echilibrate, deci nu apare linia „Diferență” pe 121000.

**Soldul contului 121 la data trecerii.** În modul **Doar solduri de deschidere**, contul de tip
„rezultat curent” (121000) nu se ajustează direct. O balanță reală la 31.12, înainte de
repartizarea profitului, are de obicei sold pe 121: atunci nota primește o linie „Diferență” pe
121000, egală cu diferența de sold a lui 121, chiar cu **Echilibrat** bifat. Linia este corectă
dacă suma ei este egală cu diferența dintre soldul lui 121 din PDF și cel din Odoo.

Pe o sincronizare fără **Detaliu pe partener**, liniile pe 401100 și 411100 nu au partener;
soldurile pe parteneri se aliniază dintr-o balanță analitică (Pasul 7).

După postare, balanța de verificare din Odoo la 31.12.2025 trebuie să fie identică cu balanța PDF.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `deltatech_chart_of_accounts` | sincronizarea planului de conturi: liniile, sumele externe, postarea diferenței |
| `ai` (Enterprise) | agentul AI și furnizorul (cheia din **Setări → AI**) |
| `deltatech_ai_pdf_base` | textul paginilor PDF, căutarea sumelor și a codurilor, cifra de control a codurilor fiscale |
| `deltatech_partner_match` | regulile de potrivire a partenerilor (cod fiscal, nume normalizat) |
| `deltatech_ai_anthropic` (opțional) | furnizorul Claude pentru agent |

**Ce e automat:** citirea PDF-ului (pe pagini), potrivirea conturilor și a partenerilor,
verificarea rândurilor, a totalurilor tipărite și a egalității debit = credit, căutarea sumelor în
textul PDF-ului, scrierea sumelor externe, punerea pe 0 a liniilor lipsă, reținerea conturilor
alese.

**Ce rămâne manual:** alegerea și confirmarea conturilor și a partenerilor propuși, crearea
partenerilor lipsă (la cerere), corectarea rândurilor citite greșit, bifarea avertizărilor,
verificarea sincronizării și **Postează diferența**.

## 8. Verificări pentru consultant

- [ ] Fără **Import balanță PDF cu AI** bifat, **Citește cu AI** refuză citirea cu mesajul despre activare.
- [ ] Un fișier care nu e PDF este refuzat la citire.
- [ ] O balanță de 3 pagini deschide dialogul de progres și consumă o singură unitate din limita zilnică.
- [ ] **Firma (PDF)**, **Cod fiscal (PDF)** și **Sfârșitul perioadei** corespund companiei și datei sincronizării.
- [ ] O sumă citită greșit blochează aplicarea (banner roșu) și se corectează cu **Recitește paginile cu erori**, fără pierderea alegerilor de pe celelalte pagini.
- [ ] Pe o balanță sintetică, **Debit de aplicat** = **Credit de aplicat** = totalul general din PDF.
- [ ] Cu **Generează liniile** apăsat înainte, bannerul albastru listează doar conturi care, într-adevăr, nu au sold în PDF (după **Verifică din nou**).
- [ ] Rândurile **Ambiguu** / **De confirmat** nu se aplică până la alegere sau confirmare.
- [ ] Un partener se potrivește după CUI, apoi după numele exact; un nume apropiat e doar propus; un CUI cu cifra de control greșită dă avertizare și nu se folosește.
- [ ] Un partener lipsă nu se creează fără clic pe **Creează partener**.
- [ ] O balanță cu avertizări nu se aplică fără **Am verificat avertizările**.
- [ ] După aplicare, totalurile **Debit Extern** / **Credit Extern** sunt egale cu totalul general din PDF și **Echilibrat** e bifat.
- [ ] Importul aplicat apare în tabul **Importuri PDF**, cu **Aplicat de** și **Data aplicării**.
- [ ] Nota postată are liniile din secțiunea „Note de monografie”; o linie „Diferență” apare doar pe 121000 și doar egală cu diferența de sold a lui 121 (în demo, niciuna).
- [ ] La o a doua balanță a aceleiași companii, conturile alese anterior se potrivesc fără revizuire.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| Citirea balanțelor de verificare cu AI nu este activată pentru … | importul nu e activat pe companie | bifați **Import balanță PDF cu AI** în setări (Pasul de configurare 3) |
| Limita zilnică de N balanțe citite cu AI este atinsă pentru … | limita zilnică a companiei a fost consumată | așteptați ziua următoare sau măriți **Limită zilnică AI balanțe** |
| Fișierul nu este un PDF. Importați o balanță CSV sau Excel din lista liniilor. | fișierul ales nu e PDF | încărcați PDF-ul sau importați fișierul din lista liniilor sincronizării |
| Balanța nu a putut fi citită cu AI: … | eroare a furnizorului AI (cheie, model, timp depășit) | verificați cheia din **Setări → AI**, modelul agentului și parametrul `timeout`; citiți din nou |
| Răspunsul AI pentru această balanță nu este valid. Recitiți-o. | răspunsul agentului nu are forma cerută | **Recitește** sau alegeți alt model care acceptă PDF |
| Balanța are erori: … | rânduri sau totaluri care nu se închid, debit ≠ credit | corectați rândul, **Recitește paginile cu erori** sau **Recitește paginile selectate** |
| N rând(uri) sunt încă de verificat (cont sau partener nepotrivit, propunere neconfirmată, eroare). … | rânduri fără cont/partener, propuneri neconfirmate | rezolvați-le din **De verificat** sau excludeți-le |
| Verificați avertizările și bifați „Am verificat avertizările” mai întâi. | balanța are avertizări | citiți bannerul galben, apoi bifați **Am verificat avertizările** |
| Sincronizarea este postată. Resetați-o mai întâi la ciornă. | sincronizarea e în **Postat** | **Resetare la ciornă** pe sincronizare, apoi aplicați |
| Balanța nu are coloana …: alegeți altă coloană de încărcat. | PDF-ul nu are coloana aleasă în **Încarcă** | alegeți coloana tipărită (de ex. **Solduri finale**) și **Verifică din nou** |
| Un import aplicat nu mai poate fi recitit. Creați un import nou. | importul e deja **Aplicat** | creați un import nou din sincronizare |

## 10. Capturi de ecran

Capturile sunt generate automat de `tests/test_screenshots.py` (mixinul `ScreenshotCase` din
`l10n_ro_doc_screenshots`, import defensiv), în română, pe planul de conturi RO, compania „RO
Company SRL” în RON. Răspunsul agentului AI este simulat; PDF-urile balanțelor sunt generate cu
strat de text. Nu se face niciun apel real la un furnizor AI.

| Fișier | Ce arată |
|---|---|
| `01_setari_import_balanta_ai.png` | setarea **Import balanță PDF cu AI** și limita zilnică, secțiunea **Intrare în Odoo** |
| `02_agent_ai.png` | agentul **Trial Balance PDF Reader AI** (nume și subtitlu în engleză), cu **Model LLM** |
| `03_sincronizare_incarca_pdf.png` | sincronizarea în ciornă, cu **Generează liniile** și **Încarcă balanța din PDF (AI)** |
| `04_import_pdf_de_citit.png` | importul de citit: PDF-ul, **Încarcă**, **Pune 0 când lipsește**, **Citește cu AI** |
| `05_progres_citire.png` | dialogul de progres al citirii, 2 din 3 pagini |
| `06_balanta_cu_erori.png` | balanța citită cu eroarea de pe pagina 2 și butonul **Recitește paginile cu erori** |
| `07_balanta_de_verificat.png` | balanța fără erori: **De verificat**, bannerul cu liniile puse pe 0 |
| `08_randuri_de_verificat.png` | rândurile de verificat: cont ambiguu și conturi propuse |
| `09_balanta_parteneri.png` | balanța pe parteneri a contului 4111, cu avertizări (inclusiv coloana **Avertizare**) și potriviri |
| `10_parteneri_de_verificat.png` | nume apropiat de confirmat și partener lipsă |
| `11_linii_sincronizare.png` | liniile sincronizării după aplicare (doar cele cu sume) |
| `12_sincronizare_aplicata.png` | sincronizarea echilibrată, cu tabul **Importuri PDF** |
| `13_nota_diferenta.png` | nota de ajustare postată |

Regenerare:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> \
    -i deltatech_ai_trial_balance_import,ai_app,l10n_ro,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

- Insistați pe ideea „AI-ul citește, Odoo verifică și decide”: agentul nu alege conturi și nu
  postează nimic; postarea rămâne gestul contabilului, pe sincronizare.
- Păstrați sub-fluxul „găsește → verifică → corectează” din Pașii 4–7: bannerul roșu blochează,
  cel galben cere confirmare, cel albastru arată liniile puse pe 0.
- Balanța PDF semnată rămâne documentul justificativ al notei de ajustare; PDF-ul rămâne și pe
  import, în tabul **Importuri PDF**.
- Un PDF scanat (fără strat de text) se citește, dar sumele nu pot fi căutate în textul lui:
  formularul spune asta într-un banner albastru. Verificați atunci mai atent rândurile.
- Menționați că PDF-ul ajunge la furnizorul AI configurat (date despre parteneri, inclusiv CNP-uri
  ale persoanelor fizice).
