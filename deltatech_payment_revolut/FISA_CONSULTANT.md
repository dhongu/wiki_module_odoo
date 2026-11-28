# Fișă Modul: Încasări online cu cardul prin Revolut

**Modul:** `deltatech_payment_revolut`
**Utilizator principal:** contabil / administratorul magazinului online (configurare, confirmarea încasărilor autorizate și urmărirea plăților)
**Prioritate:** 🟡 Medie (conector de plată opțional: se instalează doar la clienții care au cont Revolut Business cu comerciant activat)

## 1. Scop business

Magazinul online (și linkurile de plată trimise clienților) poate primi plata cu cardul sau cu contul Revolut prin
**Revolut Merchant**. Clientul plătește pe fereastra Revolut (flux **Direct**, popup în pagina magazinului) sau pe
pagina Revolut (flux **Redirecționare**), iar Odoo află rezultatul direct de la Revolut: comanda se confirmă și plata se
înregistrează fără ca cineva să verifice manual extrasul. Modulul vorbește cu Revolut direct, cu cheile proprii ale
firmei: nu există un server intermediar. Opțional, plata poate fi doar **autorizată** la finalizarea comenzii și
**încasată manual** de contabil (confirmarea comenzii, apoi încasarea efectivă; momentan indisponibil pe instalări noi, vezi limitarea cunoscută de la pasul 2).

Plățile primite pot fi **rambursate din Odoo**, integral sau parțial (de mai multe ori pe aceeași plată), fără
logare în portalul Revolut.

Se adresează firmelor cu cont Revolut Business și magazin online (sau facturi plătite prin link de plată) în Odoo.

## 2. Bază legală și context

Nu există o bază legală proprie modulului: Revolut este cel care procesează plata și autentifică clientul (SCA/3D
Secure). Contextul operațional pe care trebuie să-l cunoască consultantul:

- Odoo creează comanda la Revolut cu suma în unități minore (bani) și moneda tranzacției; după întoarcerea clientului
  sau la notificarea webhook, Odoo **citește starea comenzii de la Revolut** și verifică id-ul comenzii, suma și moneda
  înainte să confirme plata. O nepotrivire duce tranzacția în **Eroare**;
- Revolut virează banii în contul Revolut Business al firmei după regulile lui; **comisionul Revolut nu este calculat
  de modul**, iar extrasul nu este adus de el: contabilul reconciliază încasările și înregistrează comisionul la
  decontare, pe baza raportului sau a facturii Revolut;
- notificările webhook sunt acceptate doar dacă poartă o semnătură validă (secretul de semnare configurat pe provider),
  cu timestamp de cel mult 5 minute; fără secret configurat, webhook-ul este ignorat;
- metodele de plată oferite clientului (card, Revolut Pay, Apple Pay) depind de contul Revolut al comerciantului.

## 3. Utilizatori și roluri

| Rol | Ce face |
|---|---|
| Administrator (grup Setări) | introduce cheile Revolut și generează webhook-ul; secretul de semnare este vizibil doar acestui grup |
| Contabil (cu drepturi de administrator al contabilității și modul developer pentru meniul Tranzacții) | urmărește tranzacțiile, încasează (sau anulează) plățile autorizate, face rambursările și reconciliază încasările cu extrasul |
| Client (vizitator al magazinului) | alege Revolut la finalizarea comenzii și plătește în fereastra sau pe pagina Revolut |

## 4. Conturi și date implicate

- **Jurnalul providerului** (de tip bancă): încasările online se înregistrează pe el, ca plăți în curs, până la
  reconcilierea cu extrasul. În planul RO din Odoo contul implicit este 512102 „Încasări restante” (vezi captura notei
  contabile); contabilul poate alege pe jurnal un alt cont de încasări în curs, de exemplu 5125 „Sume în curs de
  decontare”.
- **Cont de client (411100 în planul RO din Odoo)**: se stinge prin plata înregistrată.
- **Comision Revolut**: se contabilizează pe 627 „Cheltuieli cu serviciile bancare și asimilate” la decontare, pe baza
  raportului Revolut; modulul nu îl calculează. Tratamentul TVA al comisionului (prestator din UE: taxare inversă dacă serviciul este taxabil, fără TVA dacă este scutit) se verifică cu
  contabilul.
- **Date necesare din contul Revolut Business:** cheia API secretă (**Secret key**, `r_prod_…`) și cheia publică
  (**Public key**, `pk_…`), generate din **API Console**; pentru testare, cheile din mediul **sandbox** (`r_test_…`).

## 5. Configurare inițială

1. În contul Revolut Business (sandbox pentru testare) generați cheile API din **API Console**. Cheii secrete îi dați, la
   produsul **Merchant**, permisiunile **Orders**, **Payments** și **Webhooks** (Read și Write) și, pentru Apple Pay,
   **Apple Pay** (Write); permisiunile de la produsul Business nu ajung.
2. În Odoo deschideți **Contabilitate → Configurare → Plăți online → Furnizori de plată → Revolut** (în lipsa
   modulului Enterprise de contabilitate, sub **Facturare**).
3. Pe tabul **Date autentificare** completați **Cheie API Revolut** (cheia secretă) și **Cheie publică Revolut** și alegeți
   **Flux Revolut**: **Direct (fereastră)** sau **Redirecționare** (vezi pasul 1 din fluxul de mai jos).
4. Cu cheia API completată și providerul accesibil public pe internet, apăsați **Generează webhook-ul**: Odoo creează la
   Revolut un webhook către `<adresa site>/payment/revolut/webhook` pentru evenimentele `ORDER_COMPLETED` și
   `ORDER_AUTHORISED` și salvează secretul de semnare în **Secret semnare webhook**. Dacă Revolut nu returnează secretul,
   Odoo anunță că trebuie copiat manual din portalul Revolut în acest câmp.
5. Pe tabul **Configurare** alegeți **Jurnal plată** (de tip bancă) și, la nevoie, bifați **Captați Valoarea Manual** (vezi pasul 2).
6. Publicați providerul, ca să apară clienților la finalizarea comenzii. Treceți-l pe **Mod testare** pentru încercări
   cu cheile sandbox, apoi pe **Activ** pentru plăți reale. Starea determină și mediul folosit: sandbox (Mod testare) sau
   producție (Activ).
7. Opțional, pentru Apple Pay (plată expres): pe același tab, dacă este permisă plata expres, încărcați **Fișier domeniu
   Apple Pay** (fișierul de validare descărcat din documentația Revolut) și apăsați **Înregistrează domeniul pentru Apple Pay**.
   Fișierul este servit la `/.well-known/apple-developer-merchantid-domain-association`.

## 6. Flux de utilizare

### Pasul 1 — Datele providerului Revolut

**Meniu:** Contabilitate (sau Facturare) → Configurare → Plăți online → Furnizori de plată → Revolut

Pe tabul **Date autentificare** se completează cheile din contul Revolut: **Cheie API Revolut** și **Cheie publică Revolut**.
**Flux Revolut** alege felul plății: **Direct (fereastră)** (clientul plătește într-o fereastră Revolut deschisă în pagina
magazinului) sau **Redirecționare** (clientul este trimis pe pagina de plată Revolut și revine în magazin). Câmpul **Secret semnare
webhook** se afișează mascat; butonul **Generează webhook-ul** apare doar cât timp secretul lipsește și cheia API
este completată.

![Formularul providerului Revolut, tabul Date autentificare: cheia API secretă și cheia publică Revolut, fluxul Direct (fereastră) și câmpul Secret semnare webhook încă gol, cu butonul Generează webhook-ul alături](screenshots/01_provider_revolut.png)

### Pasul 2 — Configurarea jurnalului și a capturării manuale

**Meniu:** același formular, tabul **Configurare**

Aici se alege **Jurnal plată** (de tip bancă), pe care se înregistrează încasările. Bifa **Captați Valoarea Manual** schimbă comportamentul: plata clientului este doar **autorizată** (suma este blocată pe card), iar contabilul o
încasează sau o anulează ulterior (pașii 4–5). Fără bifă, plata se încasează automat și tranzacția devine direct
**Confirmat**. Modulul acceptă doar încasarea integrală a sumei autorizate.

> **Limitare cunoscută:** metoda de plată Revolut livrată de modul nu declară suportul pentru captura manuală, iar
> Odoo refuză bifa cu mesajul „The following payment methods must be disabled in order to enable manual capture:
> Revolut”. Până la corectarea modulului, bifa nu poate fi activată pe o instalare nouă; capturile acestui pas și ale
> pasului 4 s-au făcut cu metoda declarată ca suportând captura manuală.

![Tabul Configurare al providerului Revolut: bifa Captați Valoarea Manual și câmpul Jurnal plată evidențiate](screenshots/02_configurare.png)

### Pasul 3 — Lista tranzacțiilor

**Meniu:** Contabilitate (sau Facturare) → Configurare → Plăți online → Tranzacții (meniul apare doar cu **modul developer** activ și cu drepturi de administrator al contabilității; alternativ, tranzacțiile se deschid din comanda de vânzare sau din factura plătită online)

Fiecare plată pornită din magazin creează o tranzacție cu **Furnizor** Revolut. Lista arată referința comenzii, suma,
starea și clientul. Tranzacțiile **Autorizat** așteaptă încasarea manuală; cele **Confirmat** au fost încasate.
Rambursările apar ca tranzacții separate, cu referința `R-` și suma negativă (pasul 8).

![Lista tranzacțiilor de plată: o tranzacție Revolut Autorizat, plăți Confirmat și rambursarea R-SO0043-1 cu suma negativă](screenshots/03_lista_tranzactii.png)

### Pasul 4 — Încasarea sau anularea unei plăți autorizate

**Meniu:** deschideți tranzacția în starea **Autorizat**

Pe formularul tranzacției apar butoanele **Captați Tranzacție** (încasează suma autorizată de la Revolut) și **Tranzacție nulă** (anulează autorizarea, iar suma se deblochează pe cardul clientului). După încasare, Odoo reciteşte starea
comenzii de la Revolut și trece tranzacția în **Confirmat**. Butonul de anulare cere o confirmare și nu poate fi
revocat.

![Tranzacție Revolut în starea Autorizat: butoanele Captați Tranzacție și Tranzacție nulă evidențiate](screenshots/04_tranzactie_autorizata.png)

### Pasul 5 — Tranzacția confirmată

**Meniu:** deschideți tranzacția în starea **Confirmat**

Tranzacția confirmată păstrează în **Referință furnizor** id-ul comenzii create la Revolut: pe el se potrivește orice
notificare ulterioară și îl folosiți pentru a găsi plata în portalul Revolut. Confirmarea vine fie din întoarcerea
clientului în magazin, fie din webhook; în ambele cazuri Odoo verifică la Revolut id-ul, suma și moneda înainte.

![Tranzacție Revolut Confirmat: referința tranzacției, id-ul comenzii Revolut la Referință furnizor, suma și clientul](screenshots/05_tranzactie_confirmata.png)

### Pasul 6 — Plata contabilă

**Meniu:** Contabilitate (sau Facturare) → Clienți → Plăți

La confirmare, Odoo creează plata contabilă pe jurnalul providerului, legată de tranzacție (câmpul **Plată** de pe
tranzacție). Dacă tranzacția plătește o factură, plata se asociază cu ea. Plata apare pe formular cu tipul **Primire**,
metoda Revolut, jurnalul providerului și starea **În proces** până la reconcilierea cu extrasul bancar (butonul
**Potrivirea plății**).

![Plata contabilă creată la confirmare: client Hipermag Distribuție SRL, jurnalul providerului, suma încasată și metoda Revolut](screenshots/06_plata_contabila.png)

### Pasul 7 — Nota contabilă a plății

**Meniu:** plata contabilă → butonul **Înregistrare jurnal**, tabul **Elemente jurnal**

Plata este înregistrată pe contul de încasări în curs al jurnalului, în așteptarea extrasului bancar.

![Nota contabilă a plății: debit cont Încasări restante, credit 411100 Clienți, pe suma încasată](screenshots/07_nota_contabila.png)

### Pasul 8 — Rambursarea din Odoo

**Meniu:** Contabilitate (sau Facturare) → Clienți → Plăți → plata încasată prin Revolut

Pe plata contabilă a unei încasări Revolut apare butonul **Retur** cât timp mai există sumă de rambursat. Asistentul
**Retur** arată **Valoare plată**, **Valoare rambursată** (rambursările făcute deja), **Maximul de rambursare permis** și
**Valoare de rambursare**, completată implicit cu tot restul. Se poate rambursa integral sau doar o parte; pe aceeași
plată se pot face mai multe rambursări parțiale, până la suma ei. La **Retur**, Odoo trimite rambursarea la Revolut,
fără ca cineva să intre în portalul Revolut. Butonul inteligent **Returnări** de pe plată deschide rambursările făcute. Dacă o rambursare anterioară este încă
**În așteptare**, asistentul afișează un avertisment.

![Plata contabilă a unei încasări Revolut: butonul Retur și butonul inteligent Returnări cu o rambursare făcută](screenshots/08_plata_rambursare.png)

![Asistentul Retur: valoarea plății 214,00 lei, 64,00 lei rambursați deja, maximum 150,00 lei și valoarea de rambursat](screenshots/09_asistent_rambursare.png)

Rambursarea devine o tranzacție nouă, cu referința `R-<referința plății>`, suma negativă și **Tranzacție Sursă** =
tranzacția inițială (SO0043-1); **Referință furnizor** este id-ul rambursării la Revolut. Dacă Revolut confirmă imediat, tranzacția
este **Confirmat** și Odoo creează plata de rambursare; dacă Revolut o are încă în procesare, tranzacția rămâne **În
așteptare** până o confirmă webhook-ul. Dacă Revolut refuză rambursarea, tranzacția trece în **Eroare**.

![Tranzacția de rambursare R-SO0043-1: Confirmat, -64,00 lei, tranzacția sursă SO0043-1 și id-ul rambursării Revolut la Referință furnizor](screenshots/10_tranzactie_rambursare.png)

### Pasul 9 — Nota contabilă a rambursării

**Meniu:** tranzacția de rambursare → **Plată** → butonul **Înregistrare jurnal**

Plata de rambursare (tip **Trimite**) stinge contul de încasări în curs al jurnalului și reface creanța pe client.
Dacă rambursarea corespunde unei facturi, contabilul emite nota de credit (factura storno) și o reconciliază cu plata
de rambursare; modulul nu creează nota de credit.

![Nota contabilă a rambursării: debit 411100 Clienți, credit 512102 Încasări restante, 64,00 lei](screenshots/11_nota_rambursare.png)

#### Note de monografie și raportare

Încasarea online a unei facturi de 380,50 RON (SO0041-1, capturile 06–07):

| Moment | Debit | Credit | Sumă |
|---|---|---|---|
| Confirmarea plății (plata contabilă, automat) | 512102 Încasări restante | 411100 Clienți | 380,50 |
| Decontarea de către Revolut (extras bancar, reconciliere) | 5121 Conturi la bănci în lei | 512102 Încasări restante | 380,50 |
| Comisionul Revolut, la decontare (manual) | 627 Cheltuieli cu serviciile bancare | 5121 Conturi la bănci în lei | după raportul Revolut |

Rambursarea parțială de 64,00 RON pe plata SO0043-1 de 214,00 RON (capturile 08–11), cu TVA 21%:

| Moment | Debit | Credit | Sumă |
|---|---|---|---|
| Rambursare din Odoo (plata de rambursare, automat) | 411100 Clienți | 512102 Încasări restante | 64,00 |
| Rambursarea pe extrasul Revolut (reconciliere) | 512102 Încasări restante | 5121 Conturi la bănci în lei | 64,00 |
| Nota de credit a facturii (manual, de contabil), venit stornat în roșu | 411100 Clienți | 707 Venituri din vânzarea mărfurilor (sau 701/704) | -52,89 |
| Nota de credit: TVA stornată în roșu | 411100 Clienți | 4427 TVA colectată | -11,11 |
| Dacă marfa se întoarce în stoc (recepția returului) | 607 Cheltuieli privind mărfurile | 371 Mărfuri | -cost, în roșu |

În Odoo, nota de credit apare inversat (Dr 707 și Dr 4427 = Cr 411100, cu sume pozitive), echivalentul stornării
în roșu; la fel, recepția returului apare ca Dr 371 = Cr 607, pe sumă pozitivă. Dacă rambursarea este o reducere de preț, nu un retur, tratamentul se stabilește cu contabilul. Revolut
poate scădea rambursarea din decontare: atunci decontarea se înregistrează net, pe suma rămasă.

La decontare în valută se folosește contul în valută (5124), cu diferențe de curs. Conturile pot diferi după jurnalul
ales și după planul de conturi al clientului. Modulul creează automat nota încasării și nota plății de rambursare;
celelalte sunt manuale.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `payment` | tranzacțiile, providerii și butoanele de capturare / anulare |
| `account` | plata contabilă și jurnalul providerului |
| `account_payment` | meniurile Plăți online din Contabilitate / Facturare |
| `website_sale` (dacă este instalat) | oferă clienților Revolut la finalizarea comenzii |

**Automat:** crearea comenzii la Revolut, trimiterea sumei, monedei și datelor clientului, verificarea plății (id comandă,
sumă, monedă), confirmarea prin webhook sau la întoarcerea clientului, crearea plății contabile, încasarea și anularea
la Revolut, rambursarea totală sau parțială trimisă la Revolut și plata de rambursare.

**Manual:** configurarea contului Revolut (cheile API), reconcilierea extrasului bancar, contabilizarea comisionului
Revolut, încărcarea fișierului Apple Pay și înregistrarea domeniului, nota de credit pentru factura rambursată.

## 8. Verificări pentru consultant

- [ ] Providerul are completate **Cheie API Revolut** și **Cheie publică Revolut** și starea corectă (**Mod testare** = sandbox,
  **Activ** = producție).
- [ ] **Generează webhook-ul** a completat **Secret semnare webhook** (sau secretul a fost copiat manual din portalul
  Revolut); fără secret, notificările webhook sunt ignorate.
- [ ] Providerul are **Jurnal plată** de tip bancă și moneda comenzii este acceptată de contul Revolut.
- [ ] O plată de test cu cardul de test Revolut ajunge în **Confirmat** și are **Referință furnizor** completată cu id-ul
  comenzii Revolut.
- [ ] Dacă **Captați Valoarea Manual** poate fi bifată (vezi limitarea cunoscută de la pasul 2), cu bifa activă, plata ajunge în **Autorizat**, iar **Captați Tranzacție** o trece în
  **Confirmat**; **Tranzacție nulă** o anulează.
- [ ] Închiderea ferestrei de plată înainte de final lasă tranzacția în **În așteptare**, iar webhook-ul o confirmă
  ulterior.
- [ ] Suma și moneda din Revolut coincid cu cele din Odoo; o nepotrivire duce tranzacția în **Eroare**.
- [ ] Plata contabilă apare în **Contabilitate → Clienți → Plăți**, pe jurnalul providerului.
- [ ] Pe plata unei încasări Revolut, **Retur** cu o sumă parțială creează tranzacția `R-...` legată de tranzacția
  inițială; după confirmare, **Maximul de rambursare permis** scade cu suma rambursată.
- [ ] O rambursare rămasă **În așteptare** trece în **Confirmat** după webhook-ul Revolut.
- [ ] **Secret semnare webhook** nu este vizibil utilizatorilor fără drepturi de Setări.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| Lipsește cheia API Revolut | cheia API lipsește de pe provider | completați **Cheie API Revolut** |
| Nu puteți crea un webhook Revolut dacă cheia API nu este setată. | s-a cerut webhook-ul fără cheia API | completați cheia API, apoi apăsați **Generează webhook-ul** |
| Webhook-ul Revolut este deja configurat. | secretul de semnare există deja | nu e nevoie de nicio acțiune; ștergeți secretul doar dacă recreați webhook-ul |
| Endpoint-ul webhook a fost creat în Revolut, dar nu a fost returnat niciun secret de semnare. … | Revolut nu a returnat secretul | copiați secretul din portalul Revolut în **Secret semnare webhook** |
| Crearea webhook-ului Revolut a eșuat: … | adresa site-ului nu este publică, cheia API este greșită / din alt mediu sau (401 Unauthorized) cheia nu are permisiunea **Webhooks** la produsul Merchant | verificați cheia, permisiunile ei din API Console, mediul (sandbox sau producție) și accesibilitatea site-ului |
| Sumă Revolut nepotrivită / Monedă Revolut nepotrivită / ID comandă Revolut nepotrivit | suma, moneda sau id-ul comenzii din Revolut nu corespund tranzacției | tranzacția rămâne în **Eroare**; verificați plata în portalul Revolut |
| Încărcați mai întâi fișierul de validare a domeniului Apple Pay. … | s-a cerut înregistrarea domeniului fără fișier | încărcați **Fișier domeniu Apple Pay** din documentația Revolut |
| The following payment methods must be disabled in order to enable manual capture: Revolut | se bifează **Captați Valoarea Manual**, dar metoda de plată Revolut nu declară suportul pentru captura manuală (limitare cunoscută a modulului) | lăsați bifa nefolosită; plata se încasează automat |
| Rambursarea a fost respinsă de Revolut. | Revolut a refuzat rambursarea (de pildă suma depășește restul nerambursat) | tranzacția de rambursare rămâne în **Eroare**; verificați plata în portalul Revolut și reluați cu o sumă corectă |
| Comanda Revolut de rambursat este necunoscută. | plata inițială nu are id-ul comenzii Revolut (**Referință furnizor**) | rambursarea nu se trimite; faceți-o din portalul Revolut |
| Numai tranzacțiile confirmate pot fi rambursate. | plata inițială nu este încă **Confirmat** | așteptați confirmarea plății |
| Erori HTTP de la Revolut (de pildă 401 sau 400) | cheie API greșită sau din alt mediu, cerere respinsă | verificați cheia și starea providerului; detaliul este în mesaj și în jurnalul serverului |

## 10. Capturi de ecran

Capturile sunt **generate automat** din `tests/test_screenshots.py` (mixinul `ScreenshotCase`), în RO, pe planul
RO, cu date fictive (firma „Cafea Trading SRL", clientul „Hipermag Distribuție SRL") și chei Revolut fictive, fără
cont Revolut real. Lista, în ordinea pașilor:

- `01_provider_revolut.png`: formularul providerului Revolut cu cheile, fluxul și secretul webhook;
- `02_configurare.png`: tabul Configurare cu capturarea manuală și jurnalul de plată;
- `03_lista_tranzactii.png`: lista tranzacțiilor (autorizată și confirmată);
- `04_tranzactie_autorizata.png`: tranzacția autorizată, cu butoanele Captați / Tranzacție nulă;
- `05_tranzactie_confirmata.png`: tranzacția confirmată, cu id-ul comenzii Revolut;
- `06_plata_contabila.png`: plata contabilă creată la confirmare;
- `07_nota_contabila.png`: nota contabilă a plății (512102 Încasări restante / 411100 Clienți);
- `08_plata_rambursare.png`: plata cu butonul Retur și rambursarea făcută;
- `09_asistent_rambursare.png`: asistentul Retur, cu suma rambursată deja și restul;
- `10_tranzactie_rambursare.png`: tranzacția de rambursare, legată de plata inițială;
- `11_nota_rambursare.png`: nota contabilă a rambursării (411100 Clienți / 512102 Încasări restante).

Revolut nu este apelat în teste: răspunsul lui la rambursare este simulat. Același test face și GIF-ul demo al
paginii Apps (`static/description/en/demo.gif`, în engleză, ca descrierea): checkout-ul cu Revolut în magazin și o
rambursare parțială; are nevoie de `website_sale` instalat.

Regenerare:

```
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_payment_revolut,l10n_ro,l10n_ro_doc_screenshots,website_sale \
    --without-demo=all --test-tags=/deltatech_payment_revolut:TestRevolutScreenshots --stop-after-init
```

Fereastra și pagina de plată Revolut sunt ale Revolut, nu pași ai operatorului, și nu se capturează.

## 11. Observații pentru manual

- Insistați pe faptul că plata se confirmă prin verificarea la Revolut (id, sumă, monedă), nu prin simpla revenire a
  clientului în magazin.
- Explicați diferența dintre **Mod testare** (sandbox Revolut, chei de test) și **Activ** (producție).
- Explicați diferența dintre încasarea automată și **Captați Valoarea Manual** (autorizare, apoi **Captați Tranzacție**
  sau **Tranzacție nulă**); încasarea parțială nu este disponibilă, iar bifa nu poate fi activată momentan (limitarea de la pasul 2).
- Precizați că modulul nu calculează comisionul Revolut și nu aduce extrasul: reconcilierea rămâne la contabil.
- Arătați rambursarea din plata contabilă (**Retur**): integral sau parțial, de mai multe ori, fără portalul Revolut;
  nota de credit pentru factură rămâne la contabil.
