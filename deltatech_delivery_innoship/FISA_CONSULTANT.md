# Fișă Modul: Expedierea prin Innoship — AWB, etichetă, ramburs, lockere și urmărire cu mai mulți curieri printr-o singură conexiune

**Modul:** `deltatech_delivery_innoship`
**Utilizator principal:** Operator expediții / responsabil depozit (emite AWB-ul și tipărește eticheta); Administrator (configurează metoda de livrare și cheia API)
**Prioritate:** 🟡 Medie (esențial pentru clienții care expediază prin contul Innoship; nu atinge contabilitatea)

---

## 1. Scop business

Un magazin care lucrează cu mai mulți curieri (Cargus, DPD, FAN Courier, GLS, Sameday și alții) are de obicei câte o integrare și câte un portal pentru fiecare. Innoship este un agregator: o singură cheie API acoperă toți curierii din contul clientului, iar Innoship rezervă expedierea, întoarce AWB-ul și eticheta și raportează starea.

Modulul aduce acest flux în livrarea din Odoo:

- **o metodă de livrare Innoship**, cu un curier ales din cei pe care contul îi are efectiv (citiți de la Innoship, nu introduși de mână) sau cu alegerea lăsată pe seama regulilor contului (**Innoship (best price)**);
- **tariful** pe comanda de vânzare, cerut de la Innoship: cel mai mic dintre tarifele curierilor din cont devine prețul livrării;
- **AWB-ul și eticheta** din livrare (PDF, ZPL sau HTML, format A6, A4 sau formatul curierului), cu ramburs, valoare declarată, mai multe colete, livrare sâmbăta, deschiderea coletului și returul coletului;
- **lockerele și punctele de ridicare** din catalogul Innoship, restrânse la curierul și țara configurate;
- **urmărirea**: istoricul stărilor scris pe livrare și **Stare livrare** ținută la zi;
- **anularea** expedierii la Innoship și la curier.

Când Innoship direcționează coletul la alt curier decât cel configurat, Odoo reține curierul real, astfel încât retipărirea etichetei și anularea merg la curierul care duce efectiv coletul.

## 2. Bază legală și context

Nu are bază legală fiscală proprie. AWB-ul (scrisoarea de transport) este documentul curierului, nu un document contabil; nu înlocuiește factura sau avizul care însoțesc marfa.

Context operațional:

- **Nu există server de test la Innoship.** O cheie de test și una reală se folosesc la aceeași adresă; doar cheia decide contul. Butonul **Test / Producție Mediu** de pe metoda de livrare **nu** ține apelurile departe de contul real: tratați o cheie reală ca reală de la primul apel.
- **Rezultatul incert.** Dacă se pierde răspunsul Innoship la crearea sau anularea unui AWB, Odoo raportează operația ca *incertă*, nu ca eșuată. O nouă apăsare ar putea rezerva un al doilea AWB pentru același colet, iar curierul le facturează pe amândouă. Verificați întâi expedierea în portalul Innoship.
- **Date personale trimise la Innoship** la fiecare tarif și expediere: numele, adresa, telefonul și e-mailul destinatarului, coletele (greutate, valoare declarată), suma rambursului și adresa de ridicare sau referința ei Innoship.

## 3. Utilizatori și roluri

- **Administratorul** (grupul **Administrare / Setări**) creează metoda de livrare și completează **Innoship API Key**; câmpul cheii este vizibil doar acestui grup.
- **Inventar / Administrator** are meniul **Inventar → Configurare → Livrare → Metode de livrare** și pornește importurile (curieri, localități, lockere).
- **Inventar / Utilizator** emite AWB-ul din livrare, tipărește eticheta, reîmprospătează istoricul și anulează AWB-ul.
- **Vânzări / Utilizator** adaugă metoda de livrare și tariful pe comanda de vânzare.

Roluri recomandate pentru testare:
- Administrator: secțiunea 5 și pașii 1–4.
- Utilizator Vânzări: pasul 5.
- Utilizator Inventar fără drepturi de administrator: pașii 6–10; confirmă că nu vede cheia API.

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile: modulul nu creează note contabile (vezi „Note de monografie și raportare").

Date minime pentru demo:
- o cheie API Innoship (de la Innoship), cu cel puțin un curier activ în cont;
- compania cu adresă completă (stradă, localitate din nomenclator, județ, telefon), folosită ca adresă de ridicare;
- un produs de tip serviciu pentru linia de transport și câteva produse stocabile **cu greutate**;
- un client cu adresă în România (localitate aleasă din nomenclator, telefon, e-mail);
- pentru ramburs: o comandă fără plată înregistrată sau cu plată la livrare (rambursul se calculează din plata comenzii, vezi pasul 6); opțional, metoda de plată la livrare în **Plată ramburs**, ca tranzacția ei să primească numărul AWB;
- pentru lockere: modulul `deltatech_delivery_locker` instalat.

## 5. Configurare inițială

1. Instalați `deltatech_delivery_innoship` (aduce `deltatech_delivery`). Pentru lockere instalați și `deltatech_delivery_locker` (și `deltatech_delivery_locker_website` pentru magazinul online).
2. Cereți de la Innoship cheia API.
3. **Inventar → Configurare → Livrare → Metode de livrare → Nou**: **Furnizor** = *Innoship*, un produs de livrare de tip serviciu și **Nivel de integrare** (*Obține preț și creează livrare* ca AWB-ul să se emită la validarea livrării).
4. În fila **Innoship Configuration**: **Innoship API Key**, **Label Type** (PDF, ZPL, HTML) și **Label Format** (A6, A4, A6 10x9, A6 300dpi). A6 PDF este formatul tipărit de majoritatea curierilor din România.
5. Apăsați **Inițializare**, apoi alegeți **Serviciu** (pasul 1 și pasul 2).
6. Apăsați **Preia localitățile** și asociați localitățile rămase *De asociat* (pasul 3).
7. Fila **Locație de ridicare**: **Sursa locației de ridicare** și, după caz, **Adresa de ridicare** (o adresă de livrare a companiei). Lăsată goală, se folosește adresa companiei. Câmpul **Referință** al adresei folosite la ridicare (al adresei de ridicare sau, pe ramura implicită, al companiei) și coloana **Referință** din lista **Locații de ridicare** se trimit la Innoship ca locație de ridicare înregistrată la curier. Lăsați-l gol dacă nu aveți o locație înregistrată la Innoship.
8. Opțional, pe fila principală a metodei: **Preț fix** „dacă prețul calculat este mai mic decât” un prag, **Necesită greutate reală**, **Serviciu sâmbătă**, **Plătitorul expedierii** (Expeditor sau Destinatar; **Terț** se trimite la Innoship ca Expeditor). Cu **Destinatar**, **Obține preț** dă transport 0 cu mesajul „Valoarea transportului este plătită de destinatar”: nu puneți manual un preț pe linia de transport (sau un preț fix), altfel clientul plătește transportul de două ori, o dată curierului și o dată în ramburs.
9. Produsul de transport al metodei: configurați-i taxa **inclusă în preț**, pentru că tariful și costul primite de la Innoship conțin TVA (pasul 5).

> Modulul nu are traducere în limba română pentru câmpurile proprii: fila **Innoship Configuration**, câmpurile **Innoship API Key**, **Label Type**, **Label Format**, **Locker Country**, **Locker Catalog** și grupul **Lockers and Pickup Points** apar în engleză și în interfața în română. Câmpurile comune ale suitei (**Serviciu**, **Plată ramburs**, **Plătitorul expedierii**, butoanele din antet) apar în română.

## 6. Flux de utilizare

### Pasul 1 — Metoda de livrare Innoship și inițializarea curierilor

**Inventar → Configurare → Livrare → Metode de livrare**, deschideți metoda Innoship, fila **Innoship Configuration**. Completați cheia API, tipul și formatul etichetei, apoi apăsați **Inițializare** în antet.

![Metoda de livrare Innoship, fila Innoship Configuration: cheia API mascată, Label Type PDF, Label Format A6, Plată ramburs cu metoda de plată la livrare, Plătitorul expedierii Expeditor, Serviciu și grupul Lockers and Pickup Points; în antet butoanele Inițializare, Preia localitățile, Preia locațiile de ridicare și Preia lockere](screenshots/01_metoda_innoship.png)

**Inițializare** verifică cheia și înregistrează curierii pe care contul îi are efectiv, fiecare cu id-ul lui Innoship. Serviciile existente se actualizează, nu se dublează; niciun serviciu nu se șterge (un curier scos din cont are încă livrări în Odoo). La instalare, modulul aduce o listă de pornire (Cargus, DPD, Fan Courier, GLS, Sameday, Team Courier, DHL Express, Posta Romana, TNT), pe care inițializarea o completează cu curierii reali ai contului. **Preia locațiile de ridicare** din antet nu are efect la Innoship (modulul nu importă locații de ridicare).

### Pasul 2 — Alegerea curierului (Serviciu)

Pe aceeași filă, deschideți lista **Serviciu**.

![Lista derulantă Serviciu de pe metoda Innoship: Innoship (best price) și curierii contului, de exemplu Cargus, DPD, Fan Courier, Sameday](screenshots/02_serviciu_curier.png)

- **Innoship (best price)**: curierul nu se trimite, iar Innoship alege după regulile contului. Tariful de pe comandă este cel mai mic dintre curieri, dar AWB-ul poate pleca cu alt curier, deci costul real poate diferi. Pentru a refactura clientului costul efectiv, setați **Politică de facturare** = *Cost real*.
- Un curier anume: toate expedierile metodei pleacă cu el. Pentru a oferi clientului mai mulți curieri, creați câte o metodă de livrare pentru fiecare.

Alegeți serviciul **după** **Inițializare**: retipărirea etichetei și anularea se adresează prin id-ul numeric al curierului, care nu se poate ghici din nume.

### Pasul 3 — Localitățile Innoship

Apăsați **Preia localitățile**. Județele și localitățile Innoship se potrivesc cu nomenclatorul Odoo, fără să conteze diacriticele („Maramures" găsește „Maramureș"). Nu se creează nici județe, nici localități noi. Rezultatul se vede în butonul **De asociat din N** de pe metodă sau în **Inventar → Configurare → Localitățile transportatorului**.

![Lista Localitățile transportatorului filtrată pe De asociat: coloanele Nume la curier, Județ și Localitate, cu Localitate goală la rândurile nepotrivite](screenshots/03_localitati_de_asociat.png)

**Găsește pe ecran.** Filtrul **De asociat**, coloana **Nume la curier** (numele Innoship) și coloana **Localitate** (localitatea Odoo asociată, goală la cele nepotrivite).

**Verifică.** Rândurile *De asociat* sunt localități Innoship fără corespondent sigur în nomenclator. Nu sunt blocante: o localitate neasociată se trimite la Innoship după nume, fără id, iar Innoship încearcă potrivirea singur. Un județ Innoship fără corespondent în Odoo apare doar în jurnalul tehnic, iar localitățile lui rămân fără județ.

**Treci mai departe.** Completați **Localitate** pe rândurile importante (orașele în care livrați des), alegând din nomenclator; nu creați localități noi.

### Pasul 4 — Lockere și puncte de ridicare (opțional)

Cu `deltatech_delivery_locker` instalat, bifați **Utilizează locker** pe metoda de livrare, completați **Locker Country** (implicit RO) și, opțional, **Locker Catalog** (*Lockers only* sau *Pickup points only*), apoi apăsați **Preia lockere**. Catalogul se vede în **Inventar → Configurare → Livrare → Lockere de livrare**.

![Lista Lockere de livrare cu locațiile Innoship importate: nume, adresă, localitate și tipul locației, locker sau punct de ridicare](screenshots/04_lockere_innoship.png)

**Găsește pe ecran.** Locațiile importate pentru metoda Innoship, cu tipul lor (locker sau punct cu personal).

**Verifică.** Catalogul este restrâns la curierul din **Serviciu** și la țara din **Locker Country**. O metodă lăsată pe **Innoship (best price)** importă locațiile **tuturor** curierilor, ceea ce rar e de dorit la checkout: clientul ar putea alege un locker al altui curier. O locație dispărută din catalog la următorul import se arhivează, nu se șterge: comenzile vechi o păstrează. Acțiunea programată „Delivery: Refresh locker catalogs" nu reîmprospătează catalogul Innoship (sare metodele fără **Utilizator** și **Parolă**, iar Innoship folosește cheia API): reimportați periodic, manual.

**Treci mai departe.** Clientul alege lockerul pe hartă, în magazin, sau operatorul îl alege în **Detalii transportator** (pasul 6). AWB-ul se adresează lockerului, cu localitatea lockerului, nu a clientului.

### Pasul 5 — Tariful pe comanda de vânzare

Pe comanda de vânzare, **Adăugați transportul**, alegeți metoda Innoship și apăsați **Obține preț**, apoi **Adaugă**.

![Fereastra de alegere a transportului pe comanda de vânzare: metoda Innoship selectată și costul primit de la Innoship](screenshots/05_tarif_comanda.png)

Innoship răspunde cu câte un tarif pentru fiecare curier din cont; cel mai mic devine prețul livrării. Dacă metoda are **Preț fix** fără prag, Innoship nu este întrebat. Dacă Innoship nu întoarce niciun tarif, Odoo afișează eroarea „Innoship returned no rate for this order.” în loc să pună livrarea gratuită.

**Tariful include TVA.** Innoship întoarce un total (`rateTotalAmount`; la emitere, costul are baza, TVA-ul și totalul, iar Odoo îl ia pe total). Configurați produsul de transport cu taxa inclusă în preț, altfel TVA-ul se adaugă a doua oară. Faptul că și tariful de ofertă include TVA reiese din numele câmpului și din testele modulului; de confirmat cu documentația Innoship.

### Pasul 6 — Detaliile expedierii pe livrare

Pe livrarea de ieșire (**Inventar → Operații → Transferuri → Livrări**), butonul **Detalii transportator** deschide fereastra cu datele care pleacă la curier.

![Fereastra Detalii metodă de livrare: adresa clientului, Metodă de livrare Innoship, Serviciu, Număr de colete, Greutate totală, Valoare asigurată, Total comandă și Sumă de încasat; butonul Aplică](screenshots/06_detalii_transportator.png)

**Găsește pe ecran.** Adresa de livrare (stradă, localitate, județ, telefon), **Serviciu**, **Număr de colete**, **Greutate totală**, **Valoare asigurată**, **Total comandă**, **Sumă de încasat** și **Opțiuni de livrare**; la o metodă cu locker, câmpul **Locker**. Din **Opțiuni de livrare**, Innoship trimite doar Saturday Delivery, Open Package și Package Return; Personal Delivery și SMS Notification apar în listă, dar sunt ignorate.

**Verifică.**
- **Sumă de încasat** se calculează din ultima plată a comenzii. Fără plată înregistrată sau cu plată la livrare, este totalul comenzii, inclusiv transportul. După facturare devine restul de plată de pe facturile postate, deci avansul sau voucherul nu se mai cer o dată. Cu orice altă plată (card, transfer bancar), suma este 0, chiar dacă banii nu au intrat încă. Lista **Plată ramburs** de pe metoda de livrare nu decide rambursul: adaugă **Preț adițional pentru ramburs** la tarif și stabilește ce tranzacții primesc numărul AWB. Dacă suma propusă nu e corectă (de exemplu, comanda e plătită prin OP înainte de facturare), bifați **Sumă de încasat stabilită manual** și corectați-o. Câmpul **Preț adițional pentru ramburs** nu apare pe formularul metodei Innoship, deci rămâne 0. Un banner roșu avertizează când suma este negativă sau diferă de comandă.
- Greutatea vine din produse; un avertisment „nu vine din produse" arată că se folosește **Greutate implicită**. Greutatea totală se împarte egal pe colete.

**Treci mai departe.** **Aplică** salvează detaliile pe livrare.

### Pasul 7 — Emiterea AWB-ului

Apăsați **Trimite la curier** (sau validați livrarea, dacă metoda are **Nivel de integrare** = *Obține preț și creează livrare*).

![Livrarea după emiterea AWB-ului: Referință de urmărire completată, Stare livrare Avizat, butoanele Tipărire AWB și Anulează AWB, eticheta atașată și mesajul de expediere în istoric](screenshots/07_livrare_cu_awb.png)

Ce se întâmplă:
- AWB-ul se rezervă la Innoship; numărul se scrie pe livrare în **Referință de urmărire** **înainte** de cererea etichetei, ca o eroare la etichetă să nu-l piardă.
- Eticheta se atașează livrării și se publică în istoric, împreună cu costul primit de la Innoship.
- **Stare livrare** devine **Avizat**.
- Dacă metoda are **Politică de facturare** = *Cost real*, costul primit de la Innoship actualizează linia de transport de pe comanda de vânzare.
- La ramburs, tranzacția comenzii făcută cu o metodă din **Plată ramburs** primește numărul AWB ca referință, doar dacă este în starea în așteptare sau autorizată.

### Pasul 8 — Eticheta

**Tipărire AWB** deschide eticheta.

![Eticheta AWB în format PDF A6: curierul, numărul AWB cu cod de bare, expeditorul, destinatarul, numărul de colete și rambursul](screenshots/08_eticheta_awb.png)

Dacă atașamentul etichetei a fost șters, eticheta se aduce din nou după AWB; nimic nu se rezervă din nou. Pentru mai multe livrări odată, din listă: **Tipărire → Tipărire AWB-uri**. O etichetă ZPL se convertește în PDF pentru vizualizare prin serviciul public Labelary, deci conținutul etichetei pleacă și acolo.

### Pasul 9 — Urmărirea stării

Fila **Istoric** a livrării arată evenimentele primite de la Innoship; **Reîmprospătează** le cere imediat. Acțiunea programată „Delivery: Update delivery status" o face automat, la 12 ore, pentru livrările care nu sunt încă livrate sau refuzate.

![Fila Istoric a livrării: evenimentele Innoship cu data și descrierea, Stare livrare În tranzit și butonul Reîmprospătează](screenshots/09_istoric_stare.png)

**Găsește pe ecran.** Coloanele **Data** și **Descriere** din fila **Istoric** și câmpul **Stare livrare**.

**Verifică.** Starea urmează tabelul de stări Innoship: Avizat, În tranzit, În depozit curier, În livrare, Livrat, Refuzat. O stare Innoship necunoscută modulului lasă **Stare livrare** neschimbată, în loc s-o ghicească. Un AWB la care Innoship nu răspunde nu oprește verificarea celorlalte.

**Treci mai departe.** Pentru mai multe livrări, din listă: **Acțiuni → Preia istoricul AWB**.

### Pasul 10 — Anularea AWB-ului

**Anulează AWB** pe livrare, cu confirmare („Sigur doriți să anulați AWB-ul?").

![Livrarea după anulare: Referință de urmărire goală, butonul Detalii transportator din nou disponibil și mesajul de anulare în istoric](screenshots/10_anulare_awb.png)

Expedierea se anulează la Innoship și la curierul care o duce (cel reținut pe livrare la emitere). Referința de urmărire și eticheta se scot de pe livrare, iar detaliile transportatorului trebuie aplicate din nou înainte de o nouă trimitere.

### Note de monografie și raportare

Modulul **nu generează note contabile**. AWB-ul, eticheta și istoricul sunt date operaționale de livrare.

Legăturile reale cu partea comercială, verificate în cod:
- **Costul transportului**: tariful Innoship, cu TVA inclus, devine prețul liniei de transport pe comanda de vânzare (pasul 5). Cu **Politică de facturare** = *Cost real*, costul primit la emiterea AWB-ului actualizează linia (pasul 7). Factura se emite prin fluxul standard al comenzii.
- **Rambursul**: suma de încasat (calculată din ultima plată a comenzii, vezi pasul 6) se trimite la Innoship pe AWB; tranzacția comenzii în așteptare sau autorizată, făcută cu o metodă din **Plată ramburs**, primește numărul AWB. Încasarea și decontarea rambursului de la curier nu se fac în acest modul (vezi `deltatech_delivery_cod`).

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_delivery` | fereastra Detalii transportator, butoanele din livrare, istoricul, localitățile transportatorului, rezultatul incert | dependență (manifest) |
| `deltatech_delivery_status` | câmpul **Stare livrare** | dependență indirectă |
| `delivery`, `stock_delivery` (Odoo) | metoda de livrare, tariful pe comandă, costul real | dependență |
| `deltatech_delivery_locker`, `deltatech_delivery_locker_website` | catalogul de lockere, alegerea pe hartă | opțional |
| `deltatech_delivery_handover` | predarea coletelor la curier, proces-verbal | opțional |
| `deltatech_delivery_dashboard` | tabloul de urmărire și de expediere | opțional |
| `deltatech_delivery_cod` (bitshop_ent) | decontarea rambursului încasat de curier | opțional |

Ce este automat: tariful pe comandă, emiterea AWB-ului la validare (cu nivelul *Obține preț și creează livrare*), atașarea etichetei, curierul real reținut pe livrare, starea și istoricul la 12 ore, arhivarea lockerelor dispărute din catalog.
Ce rămâne manual: inițializarea curierilor, asocierea localităților *De asociat*, importul și reîmprospătarea lockerelor, verificarea rambursului în Detalii transportator, anularea AWB-ului, verificarea în portalul Innoship după un rezultat incert.

**Nu sunt suportate:** crearea locațiilor de ridicare la Innoship (se trimit doar prin referință), manifestul, comanda de ridicare, decontul rambursurilor, AWB-urile de retur, notificările automate de stare (starea se citește periodic) și linkul public de urmărire.

## 8. Verificări pentru consultant

- [ ] Un utilizator fără **Administrare / Setări** nu vede câmpul **Innoship API Key**.
- [ ] **Inițializare** cu o cheie validă adaugă sau actualizează curierii contului în lista **Serviciu**, fără dubluri; cu o cheie greșită, apare eroarea Innoship cu id-ul de corelare.
- [ ] **Preia localitățile** nu creează localități sau județe noi; localitățile nepotrivite apar *De asociat*.
- [ ] Pe comandă, **Obține preț** întoarce un preț; cu **Preț fix** fără prag, Innoship nu e întrebat.
- [ ] **Detalii transportator**: o comandă din backend fără nicio plată are **Sumă de încasat** = totalul comenzii, cu transportul.
- [ ] O comandă cu transfer bancar încă neîncasat are **Sumă de încasat** = 0; bifați **Sumă de încasat stabilită manual** dacă trebuie încasat la livrare.
- [ ] După facturare cu un avans, **Sumă de încasat** este restul de plată al facturii.
- [ ] Produsul de transport are taxa inclusă în preț: linia de transport de pe comandă are același total ca tariful Innoship, fără TVA adăugat a doua oară.
- [ ] Cu **Plătitorul expedierii** = **Destinatar**, **Obține preț** dă 0 cu mesajul „Valoarea transportului este plătită de destinatar”.
- [ ] **Trimite la curier** completează **Referință de urmărire**, atașează eticheta și trece **Stare livrare** pe **Avizat**.
- [ ] Ștergeți atașamentul etichetei: **Tipărire AWB** aduce eticheta din nou, fără un AWB nou.
- [ ] **Reîmprospătează** completează fila **Istoric** și actualizează **Stare livrare**.
- [ ] **Anulează AWB** golește **Referință de urmărire** și eticheta; **Trimite la curier** emite apoi un AWB nou, după **Detalii transportator → Aplică**.
- [ ] Cu **Locker Country** = RO și un curier ales, **Preia lockere** aduce doar locațiile curierului respectiv; un al doilea import nu dublează locațiile.
- [ ] O livrare la locker pleacă cu adresa și localitatea lockerului.

## 9. Mesaje de eroare frecvente

Mesajele proprii modulului apar în engleză (modulul nu are traducere în română).

| Mesaj | Cauză | Remediere |
|-------|-------|-----------|
| „The Innoship API key is not set on this delivery method." | Cheia API lipsește de pe metoda de livrare | Administratorul completează **Innoship API Key** |
| „Innoship: … (correlation id …)" | Innoship a refuzat cererea (cheie greșită, adresă incompletă, curier indisponibil) | Citiți mesajul; dacă nu e clar, trimiteți id-ul de corelare la suportul Innoship |
| „Innoship error …" (cu un cod HTTP) | Innoship a răspuns cu eroare fără mesaj | Reîncercați; dacă persistă, contactați Innoship |
| „Innoship returned no rate for this order." | Niciun curier din cont nu are tarif pentru adresă sau greutate | Verificați adresa clientului, greutatea și curierii activi din cont |
| „Innoship did not generate the awb" | Innoship a răspuns fără număr de AWB | Verificați expedierea în portalul Innoship înainte de a reîncerca |
| „The Innoship courier of this shipment is unknown, so the request cannot be addressed. Set the Innoship Courier ID on the service of delivery method …" | Serviciul metodei nu are id de curier Innoship (de exemplu *Innoship (best price)* la o expediere veche) | Apăsați **Inițializare** pe metodă |
| „Innoship answered … to a request that changes a shipment, so it is unknown whether it was applied." | Eroare de server la crearea sau anularea AWB-ului | **Nu** reîncercați: verificați expedierea în portalul Innoship |
| „The Innoship answer was lost. The remote result is unknown." | Răspunsul s-a pierdut pe drum (rețea, timp depășit) | La fel: verificați în portalul Innoship înainte de orice altă apăsare |
| „Innoship error: …" | Conexiunea nu s-a putut stabili; nimic nu a ajuns la Innoship | Reîncercarea este sigură după ce revine conexiunea |
| „Innoship returned an answer that could not be read: …" | Răspuns Innoship în alt format decât cel așteptat | Reîncercați; dacă persistă, contactați suportul |
| „Innoship refused the location catalog: …" | Innoship a refuzat cererea de lockere (țară sau curier invalid) | Corectați **Locker Country** sau **Serviciu** și reimportați |
| „The Romanian country record was not found." | Țara România lipsește din baza de date | Reactivați țara România |
| „Expedierea … a fost creată la …, dar eticheta ei nu a putut fi preluată: …" (în istoric) | AWB-ul există, eticheta nu a venit | Folosiți **Tipărire AWB**; nu retrimiteți expedierea |
| „Coletul cântărește … kg, peste cele … kg acceptate de …" | Greutate peste **Greutate maximă colet (kg)** | Împărțiți pe mai multe colete sau corectați greutatea |
| „Livrarea … este amânată. Eliberați-o pe comanda de vânzare înainte de a o trimite la curier." | Livrare amânată | Eliberați livrarea pe comanda de vânzare |

## 10. Capturi de ecran

**Capturile nu sunt încă generate.** Numele de mai jos sunt cele planificate, în ordinea pașilor din secțiunea 6. Ele se vor genera automat din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în limba română, pe o companie RO, cu răspunsurile Innoship simulate (fără apeluri reale). Rulați skill-ul `fisa-screenshots` pentru a le crea în `static/description/`.

1. `01_metoda_innoship.png` — metoda de livrare Innoship, fila **Innoship Configuration**, cu butoanele din antet.
2. `02_serviciu_curier.png` — lista **Serviciu** cu **Innoship (best price)** și curierii contului.
3. `03_localitati_de_asociat.png` — **Localitățile transportatorului**, filtrul **De asociat**.
4. `04_lockere_innoship.png` — **Lockere de livrare** cu locațiile Innoship importate.
5. `05_tarif_comanda.png` — alegerea transportului pe comanda de vânzare, cu costul Innoship.
6. `06_detalii_transportator.png` — fereastra **Detalii transportator** a livrării.
7. `07_livrare_cu_awb.png` — livrarea cu AWB, **Stare livrare** Avizat și eticheta atașată.
8. `08_eticheta_awb.png` — eticheta PDF a AWB-ului.
9. `09_istoric_stare.png` — fila **Istoric** cu evenimentele Innoship.
10. `10_anulare_awb.png` — livrarea după **Anulează AWB**.

Regenerare, după ce testul există (baza cu limba română încărcată):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_delivery_innoship,deltatech_delivery_locker,l10n_ro,l10n_ro_doc_screenshots \
    --load-language=ro_RO --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Păstrați trei idei. Întâi, **Innoship este un agregator**: o cheie, mai mulți curieri; curierul se alege pe metoda de livrare dintre cei citiți cu **Inițializare**, sau se lasă pe seama Innoship cu **Innoship (best price)**. Apoi, **nu există mediu de test**: cheia decide contul, iar comutatorul de mediu din Odoo nu protejează nimic. În al treilea rând, **un rezultat incert nu este o eroare**: după „The Innoship answer was lost", operatorul nu apasă din nou, ci verifică în portalul Innoship, pentru că o a doua apăsare poate rezerva și factura un al doilea AWB.

Explicați și diferența dintre **Detalii transportator** (ce pleacă la curier: colete, greutate, ramburs) și **Trimite la curier** (rezervarea efectivă), plus faptul că lockerele se importă pe curierul metodei, nu pe tot contul.
