# Fișă Modul: Expedierea cu Sameday — AWB, etichetă, easybox și urmărire din livrarea Odoo

**Modul:** `deltatech_delivery_sd`
**Utilizator principal:** Operator expediții / depozit (emite AWB-ul și tipărește eticheta), Administrator Inventar (configurează metoda de livrare)
**Prioritate:** 🔴 Ridicată (la magazinele care livrează cu Sameday, fiecare colet trece prin acest modul: fără el AWB-ul se face de mână în portalul Sameday)

---

## 1. Scop business

Un magazin care livrează cu Sameday are de făcut, pentru fiecare comandă, același lucru: tariful pentru client, AWB-ul, eticheta lipită pe colet, apoi urmărirea până la livrare. Fără integrare, operatorul copiază adresa, telefonul și rambursul din Odoo în portalul Sameday și înapoi numărul AWB-ului, cu riscul unei greșeli la fiecare colet.

Modulul leagă metoda de livrare din Odoo de API-ul Sameday:

- **tariful** se cere de la Sameday pe comanda de vânzare (sau se folosește un preț fix, cu prag);
- **AWB-ul** se emite din livrare, cu numărul scris pe livrare și **eticheta** (PDF sau HTML, A4 sau A6) atașată;
- **rambursul** (suma de încasat la livrare) pleacă pe AWB din comandă sau din factură;
- livrarea la **easybox** și la **Sameday Point** folosește catalogul de locații importat din Sameday, cu verificarea serviciului și a încasării pe fiecare locație;
- **starea** coletului se citește periodic de la Sameday și se scrie pe livrare; un AWB se poate **anula** din Odoo.

Funcționează cu serverele Sameday din România, Ungaria și Bulgaria.

## 2. Bază legală și context

Modulul nu are bază legală fiscală proprie și nu emite documente fiscale. AWB-ul este documentul de transport al curierului; factura sau avizul care însoțesc marfa se emit prin fluxul standard Odoo.

Context operațional:

- La fiecare cerere de tarif și de expediere, Odoo trimite la Sameday date personale ale destinatarului (nume, adresă, telefon, e-mail; la o firmă, denumirea și codul fiscal). Sameday le prelucrează ca împuternicit al magazinului; informarea clienților despre acest transfer ține de politica de confidențialitate a magazinului.
- Sameday păstrează AWB-urile anulate și nu acceptă de două ori aceeași referință de client. De aceea, la o livrare retrimisă, modulul încearcă singur o referință nouă și notează în istoricul livrării sub ce referință a plecat coletul.
- Rambursul încasat de Sameday nu se decontează prin acest modul, ci prin `deltatech_delivery_cod` (vezi secțiunea 7).

## 3. Utilizatori și roluri

Meniul **Inventar → Configurare → Livrare** (metode de livrare, servicii, lockere) este vizibil doar grupului **Inventar / Administrator**; **Inventar / Utilizator** nu îl vede. Pe pași:

| Pași | Cine | Grup |
|---|---|---|
| Configurarea (secțiunea 5), Pașii 1, 2 și 7 | Administratorul de Inventar | **Inventar / Administrator**; pentru **Utilizator** și **Parolă** Sameday, și drept de **Setări** |
| Pasul 3 | Agentul de vânzări | orice rol din **Vânzări** |
| Pașii 4–6, 8–10 | Operatorul de expediții | **Inventar / Utilizator** |

Roluri recomandate pentru testare:
- un administrator (Setări + Inventar / Administrator) pentru configurare și Pașii 1, 2, 7;
- un utilizator Inventar / Utilizator fără drept de Setări, care parcurge Pașii 4–6 și 8–10 și confirmă că nu vede meniul **Configurare → Livrare** și nici credențialele;
- un utilizator Vânzări pentru Pasul 3.

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile: modulul nu creează note contabile.

Date minime pentru demo:
- un cont Sameday de test (utilizator și parolă API pentru mediul demo Sameday);
- un produs de livrare de tip **Serviciu** („Transport Sameday”), cu TVA 21% la vânzare (preț fără TVA);
- județele și localitățile României în nomenclator (modulul aduce codurile Sameday ale județelor; localitățile se potrivesc la **Preia localitățile**);
- un furnizor de plată pentru plata la livrare (de exemplu „Plată la livrare”), trecut în **Plată ramburs**;
- o comandă de vânzare către un client cu adresă completă (stradă, localitate, județ, telefon), cu produse care au greutate;
- pentru easybox: `deltatech_delivery_locker` instalat și câteva locații importate, una care încasează și una care nu încasează ramburs.

## 5. Configurare inițială

1. Instalați `deltatech_delivery_sd` (aduce `deltatech_delivery`). Pentru easybox și Sameday Point instalați și `deltatech_delivery_locker`.
2. **Inventar → Configurare → Livrare → Metode de livrare → Nou**: numele metodei, **Furnizor** = *Sameday*, **Livrare produs** = produsul de tip serviciu. **Nivel de integrare** = *Obține preț și creează livrare* dacă AWB-ul trebuie emis automat la validarea livrării.
3. Fila **Configurare Sameday**: **Utilizator**, **Parolă**, **Server Sameday** (România, Ungaria, Bulgaria), **Tip de pachet**, **Tip etichetă Sameday** (pdf/html), **Format etichetă Sameday** (A4/A6) și, în **Plată ramburs**, furnizorii de plată (nu metode de plată) folosiți pentru plata la livrare. Lista nu decide suma rambursului (vezi Pasul 4).
4. Mediul de lucru: butonul din colțul formularului comută între mediul de **test** (serverul demo Sameday) și **producție**. Lucrați întâi pe test.
5. **Inițializare** (antetul formularului): importă serviciile contului Sameday, cu taxele opționale; serviciul marcat implicit la Sameday se completează în **Serviciu**.
6. **Preia localitățile**: leagă județele și localitățile Sameday de nomenclatorul Odoo. Cele care nu se potrivesc rămân de asociat (butonul inteligent **De asociat**).
7. **Preia locațiile de ridicare**: importă punctele de ridicare ale contului Sameday în fila **Locație de ridicare** și creează pentru fiecare o adresă de livrare a companiei, cu **Referință** = ID-ul punctului Sameday. Pe fiecare AWB și cerere de tarif, Sameday primește ca punct de ridicare **Referință** a adresei de ridicare alese, după **Sursa locației de ridicare**:
   - *Din curier*: **Adresa de ridicare** = adresa creată de import (fără ea se folosește adresa companiei);
   - *Din depozit*: rândul din listă legat de depozitul livrării (**Depozit**), cu **Referință** completată; un depozit fără rând trimite referința adresei depozitului;
   - *Din companie*: **Referință** a companiei, care de regulă nu este un ID de punct Sameday; Sameday refuză atunci punctul de ridicare.

   Bifa **Folosește locațiile de ridicare Sameday** nu are efect în versiunea actuală: nu o folosiți pentru a alege punctul.
8. Pentru easybox / Sameday Point: bifați **Utilizează locker** și apăsați **Preia lockere**. Serviciile 15, 24, 30, 31 (easybox) și 57, 58 (Sameday Point) primesc automat bifa **Serviciu de locker** când sunt importate prima dată la **Inițializare**; verificați-o în **Inventar → Configurare → Livrare → Serviciile transportatorului**. O corectură manuală nu mai e suprascrisă la importurile următoare.
9. Opțional, pe fila de detalii a metodei: **Preț fix**, cu **Limită preț** (prețul fix se aplică doar când tariful calculat este sub limită).

## 6. Flux de utilizare

### Pasul 1 — Configurarea metodei de livrare Sameday

**Inventar → Configurare → Livrare → Metode de livrare**, metoda Sameday, fila **Configurare Sameday**.

![Formularul metodei de livrare Sameday, fila Configurare Sameday: Utilizator și Parolă completate, Server Sameday = România, Tip de pachet = Pachet, Tip etichetă pdf, Format A6; în antet butoanele Inițializare, Preia localitățile, Preia locațiile de ridicare, iar în colț indicatorul de mediu Test](screenshots/01_sd_configurare_metoda.png)

**Găsește pe ecran.** Fila **Configurare Sameday**, cu credențialele, serverul, tipul de pachet, tipul și formatul etichetei; indicatorul de mediu (Test / Producție) în zona butoanelor inteligente.

**Verifică.** Credențialele corespund mediului ales: contul de test merge doar pe serverul demo, contul de producție doar pe producție. **Plată ramburs** conține furnizorul de plată la livrare al magazinului (lista nu decide suma rambursului).

**Treci mai departe.** Salvați și apăsați **Inițializare**.

### Pasul 2 — Serviciile și localitățile Sameday

După **Inițializare** și **Preia localitățile**, metoda are serviciul implicit și localitățile Sameday legate de nomenclator.

![Metoda Sameday după inițializare: câmpul Serviciu completat cu serviciul implicit al contului și butonul inteligent De asociat, care arată câte localități Sameday nu au fost potrivite din totalul importat](screenshots/02_sd_servicii_localitati.png)

**Găsește pe ecran.** Câmpul **Serviciu** (de exemplu *24H*) și butonul inteligent **De asociat … din …**.

**Verifică.** **Serviciu** nu e gol. Numărul de localități de asociat e mic; deschideți butonul și asociați manual localitățile în care livrați des: o adresă dintr-o localitate neasociată pleacă fără codul Sameday al localității.

**Treci mai departe.** Metoda e gata de folosit pe comenzi.

### Pasul 3 — Tariful Sameday pe comanda de vânzare

**Vânzări → Comenzi → Comenzi**, comanda clientului, **Adăugați transportul**, alegeți metoda Sameday.

![Fereastra de adăugare a transportului pe comanda de vânzare: metoda Sameday selectată și costul calculat de Sameday afișat înainte de adăugare](screenshots/03_sd_tarif_comanda.png)

**Găsește pe ecran.** Metoda de livrare și costul primit de la Sameday.

**Verifică.** Costul vine de la Sameday pentru serviciul, tipul de pachet și opțiunile metodei. Dacă metoda are **Preț fix** fără **Limită preț**, costul este prețul fix; dacă are și limită, prețul fix se aplică doar când tariful Sameday e sub limită. Comparați tariful cu contractul Sameday ca să știți dacă e cu sau fără TVA: modulul îl preia așa cum îl întoarce Sameday.

**Treci mai departe.** Adăugați transportul și confirmați comanda: se creează livrarea.

### Pasul 4 — Detaliile expedierii pe livrare

**Inventar → Operații → Transferuri → Livrări**, livrarea comenzii, butonul **Detalii transportator**.

![Fereastra Metodă de livrare deschisă din Detalii transportator: adresa destinatarului, Serviciu, Număr de colete = 1, Greutate totală, Valoare asigurată, Sumă de încasat egală cu totalul comenzii și Opțiuni de livrare; jos butoanele Aplică și Anulează](screenshots/04_sd_detalii_transportator.png)

**Găsește pe ecran.** Adresa (stradă, localitate, județ, telefon), **Serviciu**, **Număr de colete**, **Greutate totală**, **Valoare asigurată**, **Total comandă**, **Sumă de încasat**, **Opțiuni de livrare** (*Open Package*, *Package Return*, *Personal Delivery*) și, cu `deltatech_delivery_locker`, câmpul **Locker**.

**Verifică.**
- Localitatea și județul sunt completate: Sameday refuză o adresă fără ele.
- **Sumă de încasat** se calculează din ultima plată a comenzii. Fără plată înregistrată sau cu plată la livrare, este totalul comenzii, inclusiv transportul. După facturare devine restul de plată de pe facturile postate, deci avansul sau voucherul nu se mai cer o dată. Cu orice altă plată (card, transfer bancar), suma este 0, chiar dacă banii nu au intrat încă. Lista **Plată ramburs** de pe metoda de livrare nu decide rambursul: stabilește ce tranzacții primesc numărul AWB (iar **Preț adițional pentru ramburs**, adăugat la tarif pentru acești furnizori, nu apare pe formularul Sameday). Dacă suma propusă nu e corectă (de exemplu, comanda e plătită prin OP înainte de facturare), bifați **Sumă de încasat stabilită manual** și corectați-o.
- Greutatea vine din produse; avertizarea „not from products” arată că e o valoare de rezervă.

**Treci mai departe.** **Aplică** salvează detaliile; pe livrare apare butonul **Trimite la curier**.

### Pasul 5 — Emiterea AWB-ului

Apăsați **Trimite la curier** (sau **Validează**, dacă metoda are nivelul de integrare *Obține preț și creează livrare*).

![Livrarea după emiterea AWB-ului: Referință de urmărire completată cu numărul AWB Sameday, Stare livrare = Avizat, în antet butoanele Tipărire AWB și Anulează AWB, iar în istoric mesajul de expediere cu eticheta atașată](screenshots/05_sd_livrare_awb.png)

**Găsește pe ecran.** **Referință de urmărire** (numărul AWB), **Stare livrare** = *Avizat*, butoanele **Tipărire AWB** și **Anulează AWB**, eticheta în istoric.

**Verifică.**
- Dacă în istoric apare „Sameday are deja o expediere sub referința …, deci această livrare a fost trimisă sub …”, coletul a plecat cu o referință nouă: căutați-l în portalul Sameday după aceasta.
- Dacă AWB-ul s-a emis, dar eticheta nu a putut fi preluată, istoricul spune „AWB-ul este valid -- tipăriți din nou eticheta din livrare, nu retrimiteți expedierea”. Nu trimiteți din nou.

**Treci mai departe.** Tipăriți eticheta (Pasul 6).

### Pasul 6 — Eticheta AWB

**Tipărire AWB** descarcă eticheta. Dacă livrarea nu o are încă, ea se cere din nou de la Sameday.

![Eticheta Sameday în format A6: numărul AWB cu cod de bare, expeditorul, destinatarul cu adresa și telefonul, numărul de colete, greutatea și suma ramburs](screenshots/06_sd_eticheta_awb.png)

**Găsește pe ecran.** Numărul AWB și codul de bare, destinatarul, rambursul.

**Verifică.** Suma ramburs de pe etichetă este cea din **Sumă de încasat**; numărul de colete corespunde cu ce se predă. Fișierul se numește `LabelSD-<AWB>.pdf` (sau `.html`).

**Treci mai departe.** Lipiți eticheta pe colet.

### Pasul 7 — Livrarea la easybox sau Sameday Point

**Inventar → Configurare → Livrare → Lockere de livrare**, filtrat pe Sameday: catalogul importat cu **Preia lockere**. Locația aleasă de client la checkout (sau setată în câmpul **Locker** din **Detalii transportator**) pleacă pe AWB.

![Lista Lockere de livrare pentru Sameday: coloanele Nume, Cod, Tip de locker (Locker automat sau Punct de ridicare) și Încasare la ridicare, cu o locație Acceptat și una Nu se acceptă](screenshots/07_sd_lockere.png)

Ecranul cere **Inventar / Administrator**; operatorul vede locația direct în câmpul **Locker** al livrării.

**Găsește pe ecran.** **Tip de locker** (*Locker automat* = easybox, *Punct de ridicare* = Sameday Point), **Încasare la ridicare** (*Acceptat* / *Nu se acceptă*) pe fiecare rând, localitatea și județul.

**Verifică.**
- Serviciul livrării este unul de livrare în afara domiciliului (bifat **Serviciu de locker**: Locker NextDay, PUDO NextDay); altfel expedierea e refuzată înainte de a ajunge la Sameday.
- O livrare cu ramburs nu merge la o locație cu **Încasare la ridicare** = *Nu se acceptă*: modulul o refuză și cere altă locație sau încasarea în avans. O locație cu câmpul gol nu e refuzată de Odoo; decide Sameday.

**Treci mai departe.** Emiteți AWB-ul ca la Pasul 5.

### Pasul 8 — Urmărirea stării

Starea se actualizează automat (acțiunea planificată **Livrare: actualizează starea livrării**, la 12 ore) sau la cerere: fila **Istoric** a livrării, butonul **Reîmprospătează**.

![Fila Istoric a livrării: evenimentele Sameday cu data, descrierea și locația, iar Stare livrare actualizată, de exemplu În livrare](screenshots/08_sd_istoric_stare.png)

**Găsește pe ecran.** Evenimentele cu **Dată**, descriere și locație; **Stare livrare** în antet.

**Verifică.** Ultimul eveniment corespunde stării afișate. Dacă Sameday nu a ridicat coletul, istoricul primește nota „Sameday nu a ridicat …”: verificați că pachetul e pregătit, se va încerca o nouă ridicare.

**Treci mai departe.** Nimic de făcut până la livrare sau refuz.

### Pasul 9 — Lista AWB-urilor

**Inventar → Operații → AWB de livrare → Listă AWB de livrare**: toate AWB-urile, inclusiv cele emise direct din portalul Sameday (aduse la **Reîmprospătează**, pe ultimele 7 zile).

![Lista AWB de livrare: AWB-urile Sameday cu Număr, Dată, Referință, Transportator, Comandă de vânzare, Destinatar, Stare livrare și Valoare ramburs](screenshots/09_sd_lista_awb.png)

**Găsește pe ecran.** Coloanele **Referință** (comanda), **Transportator**, **Destinatar**, **Stare livrare**, **Valoare ramburs**; filtrul pe transportator sau gruparea **Transportator**.

**Verifică.** Fiecare AWB Sameday are comanda de vânzare legată; un AWB din portal fără referință de comandă rămâne fără legătură. Coletele vechi blocate în *Avizat* sunt cele încă neridicate.

**Treci mai departe.** **Vizualizare comandă** deschide comanda AWB-ului selectat; **Reia interogarea stării** repornește urmărirea unui AWB la care interogarea fusese oprită după erori repetate.

### Pasul 10 — Anularea AWB-ului

Pe livrare, **Anulează AWB** cere confirmarea „Sigur doriți să anulați AWB-ul?” și anulează AWB-ul la Sameday.

![Dialogul de confirmare Sigur doriți să anulați AWB-ul? deschis peste livrarea cu AWB Sameday](screenshots/10_sd_anulare_awb.png)

**Găsește pe ecran.** Dialogul de confirmare; după confirmare, **Referință de urmărire** se golește și butonul **Detalii transportator** reapare.

**Verifică.** Anulați doar un colet care nu a fost predat. Detaliile expedierii trebuie aplicate din nou înainte de o nouă trimitere; noua trimitere pleacă automat cu o referință nouă.

**Treci mai departe.** Corectați datele și emiteți un AWB nou (Pașii 4–5).

### Note de monografie și raportare

Modulul **nu generează note contabile**. Legăturile cu contabilitatea sunt indirecte și le fac alte fluxuri:

- **Costul transportului** ajunge pe comanda de vânzare ca linie cu produsul de livrare al metodei (Pasul 3), apoi pe factura clientului, prin fluxul standard de vânzări.
- **Rambursul** este doar o sumă trimisă pe AWB (**Sumă de încasat**); modulul nu înregistrează încasarea. Factura rămâne deschisă până la decontarea curierului, făcută cu `deltatech_delivery_cod`, într-un jurnal de clearing; notele contabile sunt cele din monografia acelui modul (fișa lui, secțiunea 6, „Note de monografie și raportare”).
- Factura Sameday pentru transport se înregistrează ca orice factură de furnizor.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `deltatech_delivery` | baza comună: **Detalii transportator**, **Trimite la curier**, **Tipărire AWB**, **Anulează AWB**, lista AWB, urmărirea stării |
| `deltatech_delivery_locker` | catalogul de easybox / Sameday Point, harta din checkout, câmpul **Locker** |
| `deltatech_delivery_handover` | procesul-verbal de predare la curier; la Sameday nu e nimic de comandat (ridicarea vine odată cu AWB-ul) |
| `deltatech_delivery_dashboard` | cardurile de urmărire deasupra listei AWB |
| `deltatech_delivery_status` | **Stare livrare** pe livrare (Avizat, În tranzit, Livrat, Refuzat …) |
| `deltatech_delivery_cod` | decontarea rambursurilor Sameday într-un jurnal de clearing: din borderoul Sameday (fișier, importat cu `deltatech_ai_cod_borderou_import`) sau, fără borderou, cu **Potrivește viramentul fără borderou** din jurnal; Sameday nu publică decontul prin API, deci **Preia decontarea** nu funcționează pentru el |

**Ce e automat:** tariful, AWB-ul, eticheta, referința nouă la retrimitere, starea coletului (la 12 ore), reimportul serviciilor când Sameday respinge taxele opționale memorate, actualizarea periodică a catalogului de lockere.

**Ce rămâne manual:** asocierea localităților nepotrivite, alegerea serviciului de locker potrivit, tipărirea și lipirea etichetei, anularea unui AWB greșit, verificarea în portal la un „rezultat necunoscut”.

## 8. Verificări pentru consultant

- [ ] Pe mediul de test, **Inițializare** completează **Serviciu**, iar **Preia localitățile** afișează butonul **De asociat**.
- [ ] Un utilizator fără drept de Setări nu vede **Utilizator** și **Parolă** pe metodă.
- [ ] Pe comandă, **Adăugați transportul** cu metoda Sameday afișează un cost de la Sameday; cu **Preț fix** fără limită, afișează prețul fix.
- [ ] O comandă din backend fără nicio plată înregistrată primește **Sumă de încasat** = totalul comenzii, inclusiv transportul.
- [ ] O comandă cu tranzacție prin transfer bancar, încă neîncasată, primește **Sumă de încasat** = 0.
- [ ] După facturare, **Sumă de încasat** = restul de plată de pe factura postată.
- [ ] Cu **Sursa locației de ridicare** = Din curier și **Adresa de ridicare** = adresa importată, tariful și AWB-ul trec fără eroare de punct de ridicare.
- [ ] **Trimite la curier** scrie AWB-ul în **Referință de urmărire**, **Stare livrare** = Avizat și atașează eticheta.
- [ ] **Tipărire AWB** descarcă eticheta în formatul ales (A4/A6).
- [ ] O livrare cu ramburs către o locație cu **Încasare la ridicare** = Nu se acceptă este refuzată cu mesaj care numește locația și suma.
- [ ] Un serviciu de livrare la domiciliu cu o locație setată (sau invers) este refuzat înainte de apelul la Sameday.
- [ ] **Reîmprospătează** din fila **Istoric** aduce evenimentele și actualizează **Stare livrare**.
- [ ] **Anulează AWB** golește referința; retrimiterea pleacă sub o referință nouă, notată în istoric.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| „Livrarea … este către o locație de ridicare (ID locație …), dar serviciul Sameday selectat … nu livrează în locații fixe…” | Locație setată, dar serviciul e de livrare la domiciliu | Alegeți Locker NextDay sau PUDO NextDay în **Detalii transportator** |
| „Livrarea … folosește serviciul Sameday cu livrare în locație fixă …, dar pe expediere nu este setată nicio locație de ridicare…” | Serviciu de locker fără locație | Setați **Locker** sau alegeți un serviciu la domiciliu |
| „Livrarea … are … de încasat la livrare, dar „…” nu încasează bani…” | Ramburs către o locație care nu încasează (după catalog) | Altă locație sau încasarea sumei înainte de expediere |
| „Sameday a refuzat livrarea …: „…” nu încasează cei … datorați la livrare…” | Sameday a refuzat rambursul la acea locație | La fel; reimportați lockerele (**Preia lockere**) |
| „Opțiunile de livrare … nu sunt disponibile pentru serviciul Sameday … (tip de colet …)…” | Opțiunea nu există în contract pentru serviciu și tipul de pachet | Activați-o la Sameday, apoi **Inițializare**; sau scoateți opțiunea |
| „Sameday a respins opțiunile de livrare pentru metoda „…”. Lista memorată de servicii opționale este învechită…” | Id-urile taxelor opționale s-au schimbat la Sameday și reimportul automat n-a ajutat | **Inițializare** pe metodă și încercați din nou |
| „Sameday a respins punctul de ridicare trimis pentru metoda „…”…” | **Referință** a adresei de ridicare nu este ID-ul unui punct Sameday al contului (de exemplu, sursa e *Din companie* sau adresa nu e cea importată) | Pe fila **Locație de ridicare**, sursa *Din curier* cu adresa importată sau *Din depozit* cu rândul depozitului; **Preia locațiile de ridicare** dacă punctul e nou |
| „Sameday are deja o expediere pentru referința …. Verificați AWB-ul existent înainte de a retrimite…” | Toate referințele încercate sunt deja folosite la Sameday | Căutați AWB-ul în portalul Sameday; nu retrimiteți până nu e lămurit |
| „Răspunsul Sameday s-a pierdut. Rezultatul de la curier este necunoscut.” | Rețeaua a căzut după trimiterea cererii | Verificați în portalul Sameday dacă AWB-ul există înainte de altă încercare |
| „Sameday a răspuns … la o cerere care modifică o expediere, deci nu se știe dacă a fost aplicată.” | Eroare de server la emitere sau anulare | La fel: verificați în portal |
| „Curierul nu a generat AWB-ul” | Sameday a răspuns fără număr de AWB | Reîncercați; dacă se repetă, verificați datele livrării |
| „Serviciul Sameday nu este disponibil momentan” | API-ul Sameday e indisponibil | Reîncercați mai târziu |
| „Acces interzis: …” | Credențiale greșite sau cont de test folosit pe producție | Verificați **Utilizator**, **Parolă**, serverul și mediul |
| „Livrarea … este amânată. Eliberați-o pe comanda de vânzare înainte de a o trimite la curier.” | Livrare marcată amânată | Eliberați-o pe comandă |

## 10. Capturi de ecran

Capturile **nu sunt încă generate**. Numele de mai jos sunt planificate, în ordinea pașilor din secțiunea 6; se generează cu skill-ul `fisa-screenshots`, din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în limba română, pe o companie RO, cu Sameday simulat (fără apeluri reale). Fișierul `tests/test_screenshots.py` existent produce acum doar capturile `pudo_*` ale manualului din `doc/media`; capturile fișei se adaugă alături, în `static/description/`.

1. `01_sd_configurare_metoda.png` — metoda Sameday, fila **Configurare Sameday**, mediu Test.
2. `02_sd_servicii_localitati.png` — metoda după **Inițializare**: **Serviciu** completat și butonul **De asociat**.
3. `03_sd_tarif_comanda.png` — adăugarea transportului pe comandă, cu costul Sameday.
4. `04_sd_detalii_transportator.png` — fereastra **Metodă de livrare**, deschisă cu **Detalii transportator** pe livrare.
5. `05_sd_livrare_awb.png` — livrarea cu AWB, **Stare livrare** = Avizat.
6. `06_sd_eticheta_awb.png` — eticheta Sameday A6.
7. `07_sd_lockere.png` — lista **Lockere de livrare** Sameday.
8. `08_sd_istoric_stare.png` — fila **Istoric** cu evenimentele.
9. `09_sd_lista_awb.png` — **Listă AWB de livrare**.
10. `10_sd_anulare_awb.png` — confirmarea **Anulează AWB**.

Comanda de regenerare, după adăugarea shot-urilor:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_delivery_sd,deltatech_delivery_locker,l10n_ro,l10n_ro_doc_screenshots \
    --load-language=ro_RO --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Păstrați patru idei. Întâi, **AWB-ul e documentul curierului, nu al contabilității**: modulul nu atinge conturile, iar rambursul de pe AWB doar spune curierului cât să încaseze. Apoi, **retrimiterea e sigură**: Sameday nu acceptă de două ori aceeași referință, iar modulul alege singur alta și o notează pe livrare; în schimb, la un „rezultat necunoscut” operatorul verifică întâi în portal. În al treilea rând, **easybox și Sameday Point cer un serviciu de locker și o locație care acceptă rambursul**: verificarea se face înainte de a trimite ceva la Sameday. În al patrulea rând, **mediul de test** se comută pe metodă: un cont de test nu funcționează pe producție și invers.
