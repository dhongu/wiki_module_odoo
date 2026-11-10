# Fișă Modul: Importul facturii de furnizor din PDF, citită cu AI

**Modul:** `deltatech_ai_purchase_pdf`
**Versiune:** 19.0.1.0.4
**Suită:** bitshop_ent (necesită Odoo Enterprise, pentru aplicația AI)
**Dependențe:** `deltatech_purchase_ubl`, `ai`
**Utilizator principal:** responsabilul de achiziții care introduce facturile furnizorilor pe comenzi
**Prioritate:** 🟡 Medie (scutește tastarea liniilor la furnizorii fără XML, dar fluxul de achiziție funcționează și fără el)

---

## 1. Scop business

Furnizorii din România trimit factura și în format XML (e-Factura), pe care *Purchase UBL* o importă pe comanda de
achiziție. Furnizorii din afara țării, și o parte din cei mici, trimit **doar PDF-ul**. Pentru ei, liniile se
tastau de mână pe comandă, rând cu rând, cu riscul de greșeală la cantități și prețuri.

Modulul face ca **același buton de import** să primească și PDF-ul: un agent AI citește antetul, liniile și
totalurile facturii, iar asistentul *Purchase UBL* face restul, ca pentru un XML: găsește produsele (cod de bare,
cod de furnizor, nume), actualizează prețurile furnizorului, completează comanda, validează recepția și creează
factura de furnizor.

**AI-ul doar transcrie; Odoo decide.** Un PDF nu se importă niciodată direct: se deschide întotdeauna
previzualizarea, cu un banner și cu lista diferențelor găsite (valoare de linie, totaluri, TVA, CUI furnizor),
iar operatorul confirmă fiecare linie înainte de import.

## 2. Bază legală și context

Modulul nu are temei fiscal propriu: factura de furnizor rămâne documentul justificativ, iar înregistrarea ei
urmează fluxul standard de achiziție. Două lucruri contează la punerea în funcțiune:

- **Datele trimise furnizorului AI.** PDF-ul facturii (pagină cu pagină), numele și CUI-ul companiei cumpărătoare
  pleacă la furnizorul modelului (OpenAI, Google sau Anthropic), cu cheia companiei. Factura conține date
  comerciale ale furnizorului (prețuri, eventual persoane de contact). Recomandare: menționați furnizorul AI ca
  persoană împuternicită în registrul de prelucrări al clientului (GDPR, Regulamentul UE 2016/679).
- **Documentul e tratat ca date.** Agentul are instrucțiunea să nu execute nimic din ce scrie în PDF; un text de
  tipul „ignoră instrucțiunile” tipărit pe factură nu schimbă rezultatul.

Pentru furnizorii români obligați la e-Factura, **XML-ul din SPV rămâne sursa corectă**: importați XML-ul, nu
PDF-ul. PDF-ul cu AI este pentru facturile care nu au XML.

## 3. Utilizatori și roluri

| Rol | Ce face |
|---|---|
| Administrator (**Setări**) | pune cheia furnizorului AI, alege modelul agentului, parametrii de sistem |
| Administrator (**Setări**) cu rolul **Achiziții / Administrator** | activează importul PDF cu AI pe companie și stabilește limita zilnică (setările achizițiilor cer ambele roluri) |
| **Achiziții / Utilizator** | importă PDF-ul pe comandă, verifică previzualizarea, confirmă importul |
| **Contabilitate / Facturare** | verifică și confirmă factura de furnizor creată în ciornă |

La testare folosiți un utilizator **Achiziții / Utilizator**, nu administratorul: așa vedeți drepturile reale
ale operatorului (bifa din setări se vede doar cu rolurile **Setări** și **Achiziții / Administrator**).

## 4. Conturi și date implicate

Modulul **nu generează note contabile**. Factura de furnizor se creează din comandă, prin fluxul standard de
achiziție (*Purchase UBL* apelează crearea facturii din comandă), în **ciornă**.

Ce adaugă în bază:

- agentul **Purchase Invoice PDF Reader AI** (meniul **AI → Agenți → Agenți**), cu instrucțiunile de citire în engleză și
  în română (se folosește limba companiei);
- pe companie: bifa **Import facturi PDF cu AI** și **Limită zilnică PDF cu AI** (implicit 50), plus contorul
  intern al citirilor din ziua curentă;
- pe asistentul de import: răspunsul AI păstrat până la import (un singur apel pe document) și părțile citite
  de dialogul de progres.

Date minime pentru demo:

- o companie RO cu planul de conturi RO, o cheie OpenAI sau Google (sau Claude cu `deltatech_ai_anthropic`);
- un furnizor cu CUI, două-trei produse stocabile cu **cod de furnizor** pe lista de prețuri a furnizorului
  (fila **Achiziții** a produsului) și un produs fără cod, pentru o linie găsită doar după nume;
- o comandă de achiziție confirmată către furnizor și **PDF-ul facturii** lui: unul de o pagină și, pentru
  dialogul de progres, unul de cel puțin două pagini.

## 5. Configurare inițială

1. Instalați `deltatech_ai_purchase_pdf` (aduce `deltatech_purchase_ubl` și aplicația `ai`).
2. **AI → Configurare → Setări**: activați furnizorul și introduceți cheia API (sau variabila de mediu a
   serverului `ODOO_AI_CHATGPT_TOKEN`, respectiv `ODOO_AI_GEMINI_TOKEN`).
3. **Achiziții → Configurare → Setări**, secțiunea **Facturare**: bifați **Import facturi PDF cu AI** și
   stabiliți **Limită zilnică PDF cu AI** (implicit 50 de documente pe zi pentru companie; 0 = fără limită).
   Salvați. Bifa este pe companie: în bazele cu mai multe companii, se activează pe fiecare.

   ![Activarea importului PDF cu AI în setările achizițiilor](screenshots/01_setari_import_pdf_ai.png)

4. Opțional, **AI → Agenți → Agenți → Purchase Invoice PDF Reader AI**: alegeți **Modelul LLM**. Modelul trebuie să
   citească fișiere PDF (OpenAI GPT-4o sau mai nou, Google Gemini, Claude). Implicit este *gpt-4o*. Nu
   modificați **Promptul de sistem** decât dacă știți ce faceți: de el depinde forma răspunsului.

   ![Agentul care citește facturile PDF](screenshots/02_agent_ai.png)

5. Opțional, în modul dezvoltator, **Setări → Tehnic → Parametri de sistem**:
   - `deltatech_ai_purchase_pdf.timeout`: câte secunde se așteaptă un răspuns (implicit 300);
   - `deltatech_ai_purchase_pdf.pages_per_call`: câte pagini se trimit într-o cerere (implicit 1; mai multe pagini
     pe cerere pierd linii la facturile lungi);
   - `deltatech_ai_purchase_pdf.parallel_calls`: câte pagini citește dialogul de progres în același timp
     (implicit 3).

## 6. Flux de utilizare

### Pasul 1 — Atașați PDF-ul facturii pe comanda de achiziție

**Achiziții → Comenzi → Comenzi de achiziție**, deschideți comanda confirmată a furnizorului. Atașați PDF-ul
facturii în jurnalul de discuții (agrafa **Atașați fișiere**) sau trimiteți-l pe e-mail pe comandă.

Pasul e opțional: fișierul se poate alege și direct în asistent (pasul 2). Dacă îl atașați, asistentul îl ia
singur.

![Comanda de achiziție cu PDF-ul facturii atașat și butonul Import factură](screenshots/03_comanda_cu_pdf.png)

### Pasul 2 — Deschideți asistentul de import

Pe comandă, butonul **Import factură** din antet. Nu-l confundați cu **Încarcă factură**, butonul standard Odoo
de lângă el, care creează direct o factură de furnizor, fără previzualizare și fără să actualizeze comanda.

Câmpul **Fișier factură** este deja completat cu ultimul PDF atașat comenzii, dacă pe comandă nu există un XML UBL.
Altfel, alegeți PDF-ul cu **Încarcă fișier**.

Opțiunile **Actualizează prețurile furnizorului** și **Creează factură furnizor** sunt bifate implicit;
**Validează recepția din XML** se bifează la pasul 5, dacă marfa a sosit. Apăsați **Previzualizare**.

Pe o comandă care are deja linii, asistentul afișează sus avertismentul *„Comanda de achiziție are deja linii…”*.
Ignorați partea *„noile linii din documentul sursă nu vor fi adăugate”*: mesajul e vechi. Liniile existente se
actualizează cu cantitatea și prețul din factură, iar articolele care nu sunt pe comandă **se adaugă** ca linii noi
(vezi **Rezultat**, pasul 6).

Spre deosebire de un XML, un PDF **nu se importă direct**, chiar dacă toate liniile s-ar potrivi: se deschide
întotdeauna previzualizarea.

![Asistentul de import cu PDF-ul ales și opțiunile](screenshots/04_asistent_fisier_pdf.png)

### Pasul 3 — Așteptați citirea paginilor

Un PDF de **o pagină** se citește direct, în câteva secunde, și se deschide previzualizarea.

Un PDF de **mai multe pagini** deschide dialogul **Citirea facturii PDF cu AI**: paginile se citesc câte trei
deodată, cu bara de progres, numărul de pagini și de linii citite și timpul rămas (o factură de 19 pagini durează
aproximativ 80 de secunde). La final, previzualizarea se deschide singură.

![Dialogul de progres al citirii, cu paginile și liniile citite](screenshots/05_progres_citire.png)

**Găsiți pe ecran.** Contorul *„N / M părți citite (P pagini) — L linii”* și starea de deasupra barei.

**Verificați.**

- Numărul de pagini din contor este cel al PDF-ului.
- Starea ajunge la **Gata** fără mesaje de eroare.
- Dacă apare **Neterminat**, cu lista *Partea N: …*, apăsați **Citește părțile rămase**: se recitesc doar paginile
  eșuate, nu tot documentul.

**Treceți mai departe** abia când toate paginile sunt citite: previzualizarea nu se deschide pe o factură citită
parțial. **Oprește după părțile în lucru** oprește citirea; la o nouă **Previzualizare**, se continuă de unde a
rămas.

Fiecare document citit consumă **o unitate** din limita zilnică a companiei, oricâte pagini ar avea și oricâte
reîncercări ar fi.

### Pasul 4 — Verificați previzualizarea față de PDF

Deasupra liniilor, banda albastră a *Purchase UBL* explică culorile; sub ea, bannerul galben **„Datele au fost
citite cu AI din PDF.”** și, dacă ceva nu se leagă, lista diferențelor.

![Previzualizarea importului, cu bannerul AI și lista diferențelor](screenshots/06_previzualizare_pdf.png)

**Găsiți pe ecran.**

- în banner, avertismentele, câte unul pe rând;
- în tabel, câte un rând pe linie de factură: **Cod furnizor**, **Descriere furnizor** (textul tipărit pe
  factură), **Cantitate**, **Preț unitar**, **Produs**, **Acțiune**, **Tip potrivire**;
- culoarea rândului: **verde** = găsit după codul de furnizor sau codul de bare, **galben** = găsit doar după
  nume, **roșu** = negăsit.

**Verificați**, cu PDF-ul deschis alături:

- Numărul de rânduri = numărul de articole facturate. Rândurile de subtotal, de transport de pe pagină și
  **avansul dedus** pe factură nu trebuie să apară ca linii.
- Cantitatea și prețul unitar al fiecărui rând sunt cele tipărite (prețul este **fără TVA**, înainte de discountul
  de linie).
- Avertismentele din banner, dacă există:
  - *„Linia N (…): cantitate × preț înseamnă X, valoarea liniei este Y.”* — o cifră citită greșit sau un discount
    nevăzut pe acea linie; comparați rândul cu PDF-ul;
  - *„Liniile însumează X, factura declară Y fără TVA.”* — lipsește sau e în plus o linie;
  - *„Valoarea fără TVA plus TVA înseamnă X, totalul de plată este Y: verificați dacă s-a plătit deja un avans.”* —
    la o factură cu avans dedus, diferența este avansul și e normală;
  - *„CUI-ul furnizorului nu a fost citit: furnizorul este cel de pe comandă.”* — confirmați că PDF-ul e al
    furnizorului comenzii;
  - *„Nicio linie de factură nu a fost citită din PDF.”* — PDF scanat ilizibil sau alt document decât o factură.
- Rândurile **galbene**: produsul propus după nume este cel corect.

**Treceți mai departe** doar când fiecare avertisment are o explicație. Dacă o cifră e greșită, nu importați:
închideți și corectați după import pe comandă, sau importați XML-ul, dacă furnizorul îl are.

### Pasul 5 — Alegeți acțiunea pe fiecare linie și importați

Pe fiecare rând, coloana **Acțiune**:

- **Folosește produsul** — produsul din coloana **Produs** (îl puteți schimba pe orice rând);
- **Creează produs nou** — pentru un articol nou; produsul primește descrierea **tradusă în limba companiei**
  (română pentru o companie RO), iar textul original al furnizorului rămâne ca denumire la furnizor, ca facturile
  următoare să-l găsească;
- **Ignoră** — linia nu se importă.

Dacă marfa a sosit odată cu factura, bifați **Validează recepția din XML**: recepția comenzii se validează cu
cantitățile din factură, inclusiv pentru produsele create acum. Fără recepție, factura de furnizor preia doar
cantitățile deja recepționate (produsele se facturează, de regulă, la recepție), iar o linie nouă apare pe
factură cu cantitatea 0.

În captură, linia *Teu PVC 110 mm* devine produs nou, linia *Mufă PVC 110 mm* (cea cu valoarea citită greșit)
rămâne pe **Ignoră** și se înregistrează de mână după verificarea PDF-ului, iar recepția se validează.

Apăsați **Importă**.

![Previzualizarea cu acțiunea aleasă pe rândurile roșii](screenshots/07_previzualizare_actiuni.png)

### Pasul 6 — Citiți rezultatul importului

Asistentul afișează secțiunea **Rezultat**: liniile actualizate sau adăugate pe comandă, produsele create,
prețurile furnizorului actualizate, recepția validată, factura de furnizor creată și verificarea totalului și a
TVA-ului față de comandă.

![Rezultatul importului, cu factura de furnizor creată](screenshots/08_rezultat_import.png)

**Găsiți pe ecran.** Mesajele colorate din **Rezultat** și câmpul **Factură furnizor**.

**Verificați.**

- *„Verificare total OK”* pe comandă; altfel, diferența afișată are o explicație. În captură, totalul comenzii e
  mai mic cu 75,00 lei fără TVA (90,75 lei cu TVA): exact linia ignorată. Alte explicații obișnuite: avansul dedus,
  o linie corectată de mână.
- *„Recepție actualizată: …”*, dacă ați bifat validarea recepției.
- Nu apare avertismentul *„Cota TVA diferă pe N linie(i) …”*. Cota citită pe fiecare linie se compară cu
  TVA-ul liniei din comandă (care vine din produs și din poziția fiscală a furnizorului); o linie la 0% dintr-o
  factură intracomunitară cere pe comandă poziția fiscală intracomunitară (taxare inversă). O cotă netipărită pe
  factură rămâne necitită și nu se compară, nu devine 0%. Dacă apare avertismentul, corectați poziția fiscală
  înainte de a confirma factura.
- *„Linii neasociate în comandă: …”* (roșu) enumeră liniile lăsate pe **Ignoră**; în captură, *PVC-MUF-110*. Nu e o
  eroare de import, ci lista liniilor de înregistrat de mână.
- Mesajele de avertisment (unitate necunoscută, recepție nevalidată, factură necreată) au o cauză cunoscută.

Apoi **Deschide comanda de achiziție** sau **Vezi factura furnizor**.

### Pasul 7 — Verificați factura de furnizor în ciornă

**Vezi factura furnizor** deschide factura creată din comandă, în **ciornă**: furnizorul, **Referință factură**
(numărul citit din PDF), **Data facturii** și **Data scadenței** citite, liniile din comandă.

![Factura de furnizor creată din comandă, în ciornă](screenshots/09_factura_furnizor.png)

**Verificați** față de PDF: numărul și data facturii, liniile, totalul fără TVA, TVA-ul și totalul de plată. Dacă ați
ignorat o linie la import (ca în captură, unde factura are 961,22 lei față de 1.051,97 lei pe PDF), adăugați-o pe
comandă, recepționați-o (recepția comenzii a fost validată la import, linia nouă are recepția ei), apoi adăugați-o pe
factură prin **Completare automată** din comandă, înainte de confirmare. Operatorul verifică factura și atașează
PDF-ul, dacă nu e deja; contabilul apasă **Confirmă**.

Contul de pe linii vine din categoria produsului. În captură, categoria demo nu are evaluare automată a stocului, deci
liniile merg pe 607; cu evaluare automată (inventar permanent), liniile facturii merg pe 408, care închide recepția înregistrată pe contul de stoc, ca în
notele de mai jos.

### Pasul 8 (variantă) — Încărcați PDF-ul direct din lista comenzilor

**Achiziții → Comenzi → Cereri de ofertă**, butonul **Încărcare** din listă, cu **un singur PDF** de factură pe
care Odoo nu-l poate citi singur: în loc de o cerere de ofertă goală, se deschide direct previzualizarea
importului pentru noua comandă, citită cu AI. Furnizorul se ia din PDF (după CUI sau nume).

În captură, linia *Teu PVC 110 mm* e acum verde, găsită după codul furnizorului: produsul creat la importul
anterior (pasul 5) a primit codul furnizorului pe lista lui de prețuri. Opțiunea **Creează factură furnizor** e
debifată, pentru că noua comandă este încă cerere de ofertă.

![Previzualizarea deschisă direct după încărcarea PDF-ului din lista comenzilor](screenshots/10_incarcare_din_lista.png)

Dacă citirea eșuează, asistentul rămâne deschis pe PDF; o nouă **Previzualizare** afișează eroarea. Cu mai multe
fișiere deodată sau cu importul PDF cu AI dezactivat, butonul **Încărcare** are comportamentul standard. Comanda
creată astfel este o cerere de ofertă: factura de furnizor se creează după confirmarea comenzii.

### Note de monografie și raportare

Modulul nu generează note contabile. Notele rezultă din fluxul standard de achiziție, după validarea recepției și
confirmarea facturii de furnizor create din comandă (mărfuri, TVA 21%; primele trei rânduri cu inventar permanent, ultimul cu inventar
intermitent):

| Operațiune | Debit | Credit |
|---|---|---|
| Recepția mărfii, înainte de factură | 371 Mărfuri | 408 Furnizori - facturi nesosite |
| Factura de furnizor după recepție | 408 Furnizori - facturi nesosite | 401 Furnizori |
| TVA din factura de furnizor | 4426 TVA deductibilă | 401 Furnizori |
| Factura de furnizor, inventar intermitent (ca în captura 09) | 607 Cheltuieli privind mărfurile | 401 Furnizori |

Când recepția și factura sunt în aceeași zi, contul 408 se închide imediat; contul de stoc depinde de categoria
produsului (301, 302, 371 etc.). La o achiziție intracomunitară, TVA-ul se înregistrează prin taxare inversă
(4426 = 4427), după poziția fiscală a comenzii. TVA-ul se înregistrează la factură, nu la recepție.

Factura ajunge în jurnalul de cumpărări și în D300; în D394 la furnizorii din România, în D390 la achizițiile
intracomunitare de bunuri, iar importurile din afara UE se declară prin DVI. Modulul nu schimbă raportarea.

## 7. Legături cu alte module / declarații

| Modul | Legătura |
|---|---|
| `deltatech_purchase_ubl` | asistentul de import: potrivirea produselor, previzualizarea, prețurile furnizorului, recepția, factura de furnizor, verificarea totalului și a TVA-ului |
| `ai` (Enterprise) | agentul, furnizorul AI și cheia lui |
| `deltatech_ai_anthropic` | opțional: modelele Claude pentru agent |
| `deltatech_purchase_ubl_ai` (*Purchase UBL AI Product Matching*) | opțional: pentru liniile rămase negăsite, propune un produs cu AI, ca la XML |
| `purchase`, `stock`, `account` | comanda, recepția și factura de furnizor |

**Ce e automat.** Alegerea PDF-ului de pe comandă, împărțirea pe pagini și citirea lor, unirea paginilor (liniile
în ordine, antetul din prima pagină, totalurile din ultima), verificările aritmetice, potrivirea produselor,
traducerea denumirii pentru produsele noi, actualizarea comenzii, a prețurilor, a recepției și crearea facturii în
ciornă.
**Ce rămâne manual.** Activarea pe companie, verificarea previzualizării față de PDF, acțiunea pe liniile negăsite,
confirmarea importului, verificarea și confirmarea facturii de furnizor.

## 8. Verificări pentru consultant

- [ ] Cheia furnizorului AI e bună și modelul agentului citește PDF.
- [ ] **Import facturi PDF cu AI** e bifat pe compania testată; limita zilnică e stabilită.
- [ ] Pe o comandă cu PDF atașat, **Import factură** completează singur **Fișier factură** cu PDF-ul.
- [ ] Pe o comandă cu XML UBL atașat, asistentul ia XML-ul, nu PDF-ul, și nu se face niciun apel AI.
- [ ] Un PDF de o pagină deschide previzualizarea cu bannerul **„Datele au fost citite cu AI din PDF.”**
- [ ] Un PDF de mai multe pagini deschide dialogul de progres; contorul arată toate paginile, starea ajunge la
      **Gata**.
- [ ] Numărul de rânduri din previzualizare = numărul de articole din PDF; subtotalurile și avansul nu apar ca linii.
- [ ] Cantitatea și prețul fără TVA ale fiecărui rând sunt cele din PDF.
- [ ] O cifră modificată intenționat (sau o factură cu o linie greșită) produce avertismentul *„Linia N …”*.
- [ ] La o factură cu avans dedus, avertismentul de total sugerează avansul.
- [ ] Un PDF importat nu trece niciodată direct la import, chiar cu toate liniile verzi.
- [ ] Un produs creat din linie are denumirea în română; denumirea furnizorului rămâne pe lista lui de prețuri.
- [ ] **Rezultat**: verificarea totalului și a TVA-ului față de comandă e OK sau are o explicație.
- [ ] Factura de furnizor e în ciornă, cu numărul, data și scadența din PDF; totalurile corespund PDF-ului.
- [ ] Cu bifa debifată, **Previzualizare** pe un PDF afișează mesajul că citirea nu e activată.
- [ ] După atingerea limitei zilnice, următorul PDF primește mesajul de limită; a doua zi contorul pornește de la 0.
- [ ] **Încărcare** din lista cererilor de ofertă, cu un singur PDF, deschide previzualizarea noii comenzi.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| „Citirea facturilor PDF cu AI nu este activată pentru *companie*. Activați-o în Setări > Achiziții > Import facturi PDF cu AI.” | bifa nu e activă pe compania comenzii | activați-o (secțiunea 5, pasul 3) pe compania respectivă |
| „S-a atins limita zilnică de N facturi PDF citite cu AI pentru *companie*.” | s-au citit deja N documente azi | așteptați ziua următoare sau măriți limita în setări (0 = fără limită) |
| „Factura PDF nu a putut fi citită cu AI: …” | cheie greșită, credit epuizat la furnizor, model care nu citește PDF, timp depășit | verificați cheia și contul furnizorului AI și modelul agentului; la timp depășit, măriți `deltatech_ai_purchase_pdf.timeout` |
| „Răspunsul AI pentru acest PDF nu este valid. Încercați din nou sau importați XML-ul.” | modelul a întors un text care nu e în forma cerută | apăsați din nou **Previzualizare**; dacă se repetă, alegeți alt model pe agent |
| „Lipsește agentul AI pentru citirea facturilor PDF.” | agentul *Purchase Invoice PDF Reader AI* a fost șters | actualizați modulul, ca agentul să fie recreat |
| *„Partea N: …”* în dialogul de progres, starea **Neterminat** | o pagină nu a putut fi citită (timp depășit, eroare la furnizor) | **Citește părțile rămase**; dacă eșuează mereu, scădeți `parallel_calls` |
| „Nicio linie de factură nu a fost citită din PDF.” | PDF scanat ilizibil, sau alt document (aviz, ofertă) | folosiți un PDF cu text sau o scanare mai clară; verificați că e factura |
| Linii lipsă la o factură lungă, fără avertisment de linie | `pages_per_call` a fost mărit și modelul a sărit linii | readuceți `deltatech_ai_purchase_pdf.pages_per_call` la 1 |
| „Atenție: documentul … este o notă de credit; notele de credit nu se importă.” | PDF-ul e o notă de credit (storno) | înregistrați manual rambursarea de la furnizor |
| „Crearea facturii de furnizor a fost sărită: … comanda nu este încă confirmată …” | comanda e încă cerere de ofertă | confirmați comanda și creați factura din ea |

## 10. Capturi de ecran

Capturile, în ordinea din secțiunile 5 și 6, în `readme/screenshots/`:

| Fișier | Pasul | Ce arată |
|---|---|---|
| `01_setari_import_pdf_ai.png` | 5 (configurare) | **Achiziții → Setări → Facturare**: bifa **Import facturi PDF cu AI** și limita zilnică |
| `02_agent_ai.png` | 5 (configurare) | agentul *Purchase Invoice PDF Reader AI*: modelul LLM și promptul de sistem în română |
| `03_comanda_cu_pdf.png` | 1 | comanda de achiziție confirmată, cu PDF-ul atașat (agrafa din jurnal) și butonul **Import factură** |
| `04_asistent_fisier_pdf.png` | 2 | asistentul de import cu **Fișier factură** = PDF-ul comenzii și butonul **Previzualizare** |
| `05_progres_citire.png` | 3 | dialogul **Citirea facturii PDF cu AI**, la 2 / 3 părți citite |
| `06_previzualizare_pdf.png` | 4 | previzualizarea cu bannerul AI, cele două avertismente și rânduri verzi, galbene și roșii |
| `07_previzualizare_actiuni.png` | 5 | **Creează produs nou** și **Ignoră** pe rândurile roșii, **Validează recepția din XML** bifat |
| `08_rezultat_import.png` | 6 | secțiunea **Rezultat**: produs creat, linie adăugată, recepție validată, factură creată |
| `09_factura_furnizor.png` | 7 | factura de furnizor în ciornă, cu referința, data și scadența din PDF |
| `10_incarcare_din_lista.png` | 8 | previzualizarea deschisă direct după **Încărcare** din lista cererilor de ofertă |

Capturile sunt **generate automat** din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din
`l10n_ro_doc_screenshots`, import defensiv), în română, pe planul de conturi RO, pe *RO Company* în RON. Factura
furnizorului este un PDF generat de test, iar răspunsul agentului AI este simulat, ca rezultatul să fie același la
fiecare rulare și să nu se consume credit. Furnizorul demo e din România doar pentru simplitate; în practică, la un
furnizor român importați XML-ul din SPV, iar PDF-ul cu AI rămâne pentru furnizorii fără e-Factura. Regenerare:

```bash
./odoo/odoo-bin -c odoo.conf -d test19 -i deltatech_ai_purchase_pdf,ai_app,l10n_ro,l10n_ro_doc_screenshots --test-tags=fise_screenshots/deltatech_ai_purchase_pdf --stop-after-init
```

## 11. Observații pentru manual

- **AI-ul transcrie, operatorul confirmă.** Mesajul de bază pentru utilizator: previzualizarea se verifică față de
  PDF de fiecare dată, chiar dacă toate rândurile sunt verzi. Verificările aritmetice prind cifrele citite greșit
  care nu se leagă, nu și o linie citită greșit „consecvent” (cantitate și valoare greșite deopotrivă).
- **XML înainte de PDF.** Pentru furnizorii români, importați XML-ul din SPV; PDF-ul cu AI e pentru furnizorii
  fără e-Factura (de regulă cei externi). Pe o comandă cu ambele atașate, asistentul ia XML-ul.
- **Codul de furnizor face diferența.** Liniile se găsesc sigur (verde) după codul de furnizor de pe lista de
  prețuri a furnizorului. Când factura nu are coloană de cod, agentul ia codul din descriere (ex. *„car mats
  AP1109”* → *AP1109*); dimensiunile, modelele și anii nu sunt luate drept cod.
- **Costul.** Un document = o unitate din limita zilnică, oricâte pagini ar avea. Costul real la furnizorul AI
  crește cu numărul de pagini (o cerere pe pagină). Limita zilnică e plasa de siguranță, nu bugetul.
- **Produse noi în română.** Un produs creat din linie se numește cu descrierea tradusă în limba companiei;
  denumirea furnizorului (ex. în poloneză) rămâne pe lista lui de prețuri, de unde o găsesc facturile următoare.
- **Avansul.** Avansul dedus pe factură nu devine linie; diferența dintre total și totalul de plată apare ca
  avertisment, cu sugestia avansului, și se reglează la plată.
- Numele agentului (*Purchase Invoice PDF Reader AI*) rămâne în engleză în interfață.
- Butonul **Import factură** (din `deltatech_purchase_ubl` 19.0.1.4.19; înainte, **Importă UBL**) primește atât XML-ul
  UBL, cât și PDF-ul; butonul standard **Încarcă factură** e alt flux.
