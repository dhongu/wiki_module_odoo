# Fișă Modul: Expediere cu Poșta Română — AWB, etichetă PDF, ramburs și anulare din livrare

**Modul:** `deltatech_delivery_pr`
**Utilizator principal:** Operator expediții / responsabil depozit (emite și tipărește AWB-urile); administratorul configurează contul Poștei Române
**Prioritate:** 🟡 Medie (necesar doar firmelor care expediază cu Poșta Română; fără el, AWB-ul se introduce manual în portalul Poștei Române)

---

## 1. Scop business

Firmele care trimit colete prin Poșta Română emit AWB-ul în portalul `awb.posta-romana.ro`, copiind de mână destinatarul, adresa, greutatea și rambursul din comandă. Modulul face legătura direct din Odoo: la validarea livrării, AWB-ul se emite prin serviciul AWB al Poștei Române cu datele din livrare, numărul AWB-ului se scrie pe livrare ca referință de urmărire, iar eticheta PDF se atașează livrării, gata de tipărit. Rambursul (suma de încasat de la destinatar) și valoarea declarată pleacă pe AWB, iar rambursul se returnează prin **mandat poștal**. Un AWB emis greșit se anulează din livrare.

Modulul acoperă doar emiterea, eticheta și anularea. **Nu** calculează tarife (costul transportului este prețul fix al metodei de livrare), **nu** citește starea coletului de la Poșta Română și **nu** lucrează cu lockere, puncte de ridicare, colete multiple pe același AWB sau servicii opționale (livrare sâmbăta, deschiderea coletului, nota de restituire).

## 2. Bază legală și context

Modulul nu are bază legală fiscală proprie. AWB-ul este documentul de transport al curierului: nu înlocuiește factura sau avizul care însoțesc marfa și nu este document contabil.

Context operațional:

- **Ramburs prin mandat poștal.** Pe AWB se trimite tipul de mandat „POSTAL": Poșta Română încasează rambursul de la destinatar și îl returnează expeditorului prin mandat poștal, nu prin virament grupat cum fac curierii privați.
- **Fără mediu de test.** Conectorul lucrează întotdeauna cu serverul de producție `awb.posta-romana.ro`; butonul **Mediu** (Producție/Test) din colțul formularului metodei de livrare nu schimbă nimic. Orice AWB emis din Odoo este un AWB real: la teste, anulați-l imediat (Pasul 7).
- **Referința comenzii.** Pe AWB pleacă, ca identificator al comenzii, numărul comenzii de vânzare (originea livrării), fără sufix, și la o reemitere după anulare.
- **Date personale.** La fiecare expediere, Odoo trimite Poștei Române numele, adresa, telefonul și e-mailul expeditorului și destinatarului, persoana de contact, greutatea, rambursul, valoarea declarată și referința comenzii. Este transmiterea necesară executării transportului; informarea clienților despre ea ține de politica de confidențialitate a firmei.

## 3. Utilizatori și roluri

- **Administratorul** (rolul **Administrator** pe fișa utilizatorului, grupul tehnic **Rol / Administrator**) completează **Utilizator** și **Parolă** ale contului AWB: câmpurile sunt vizibile doar acestui grup.
- **Inventar / Administrator** creează și modifică metoda de livrare (**Inventar → Configurare → Livrare → Metode de livrare**).
- **Vânzări / Utilizator** adaugă metoda de livrare pe comanda de vânzare.
- **Inventar / Utilizator** verifică detaliile expedierii, validează livrarea, tipărește și anulează AWB-ul.

Roluri recomandate pentru testare:
- un administrator care configurează contul Poștei Române (Pasul 1);
- un utilizator de vânzări care pune metoda de livrare pe comandă (Pasul 2);
- un utilizator de inventar care parcurge pașii 3–7;
- un utilizator de inventar fără rolul de administrator: confirmă că nu vede **Utilizator** și **Parolă** pe metoda de livrare.

## 4. Conturi și date implicate

Modulul **nu folosește conturi contabile** și nu creează note contabile.

Date minime pentru demo:
- un cont AWB Poșta Română (utilizator și parolă de la Poșta Română); nu există cont de test, deci AWB-urile emise la demo trebuie anulate;
- o metodă de livrare cu **Furnizor** = **Poșta Română**, un produs de livrare de tip serviciu și un **Preț fix**;
- compania cu adresă completă (stradă, localitate, județ, cod poștal), telefon și e-mail: sunt datele expeditorului de pe AWB;
- un client cu adresă completă, telefon și e-mail, cu strada, numărul, blocul și apartamentul pe **primul rând** al adresei;
- produse cu greutate pe fișa produsului (altfel se trimite o greutate estimată);
- o comandă de vânzare fără plată înregistrată (ramburs = total) și una plătită cu transfer bancar (ramburs 0), pentru cele două cazuri de ramburs.

## 5. Configurare inițială

1. Instalați `deltatech_delivery_pr` (aduce `deltatech_delivery`, `delivery` și `mail`).
2. **Inventar → Configurare → Livrare → Metode de livrare → Nou**: **Furnizor** = **Poșta Română**, **Livrare produs** = un produs de tip serviciu (de exemplu „Transport Poșta Română"), cu taxele de vânzare corecte (transportul refacturat intră în baza TVA).
3. **Nivel de integrare**: **Obține preț și creează livrare** emite AWB-ul automat la validarea livrării; **Obține preț** lasă emiterea pe seama operatorului (din **Detalii transportator**, apoi **Trimite la curier**). Emiterea la validare cere și ca tipul de operație al livrărilor să aibă bifat **Generează etichete de expediere** (**Inventar → Configurare → Tip operație**; bifat implicit la livrări).
4. Completați **Preț fix**: Poșta Română nu calculează tarife prin această integrare, deci costul transportului de pe comandă este acest preț.
5. Fila **Configurare Poșta Română** (vizibilă doar când furnizorul este Poșta Română): **Utilizator**, **Parolă**, **Plată ramburs**, **Plătitorul expedierii** și **Serviciu**.
6. **Plătitorul expedierii**: lăsați **Expeditor**. Valoarea nu se transmite Poștei Române, iar **Destinatar** pune transportul pe comandă la 0, deci firma pierde venitul din refacturarea transportului, fără ca AWB-ul să se schimbe.
7. **Plată ramburs** nu decide rambursul (vezi Pasul 3): adaugă **Preț adițional pentru ramburs** la tarif (câmpul nu apare în formularul Poștei Române, deci rămâne 0) și stabilește ce tranzacții de plată primesc numărul AWB.
8. **Serviciu** este codul de trimitere al Poștei Române. Nu există import al serviciilor: în câmpul **Serviciu**, scrieți numele și alegeți **Creați și editați…**, apoi completați **Cod** cu codul primit de la Poșta Română. Un serviciu fără cod sau o metodă fără serviciu trimit codul implicit `3,1,10`.
9. Butoanele **Inițializare** și **Preia localitățile** din antetul formularului sunt comune tuturor curierilor; la Poșta Română nu au efect (nu există servicii sau localități de importat).

## 6. Flux de utilizare

### Pasul 1 — Metoda de livrare Poșta Română

**Inventar → Configurare → Livrare → Metode de livrare**, deschideți metoda Poșta Română, fila **Configurare Poșta Română**.

![Formularul metodei de livrare: Furnizor Poșta Română, Nivel de integrare Obține preț și creează livrare, Preț fix completat și fila Configurare Poșta Română cu Utilizator, Parolă afișată mascat, Plată ramburs, Plătitorul expedierii Expeditor și Serviciu](screenshots/01_metoda_livrare_pr.png)

Ce se întâmplă: metoda de livrare devine utilizabilă pe comenzi și pe livrări. **Parola** se afișează mascat în formular.

### Pasul 2 — Transportul pe comanda de vânzare

Pe comanda de vânzare, **Adăugați transportul** deschide fereastra **Adăugați o metodă de expediere**; alegeți metoda Poșta Română și apăsați **Adaugă**.

![Fereastra Adăugați o metodă de expediere: metoda Poșta Română selectată și costul egal cu prețul fix al metodei](screenshots/02_adauga_transport_pr.png)

Ce se întâmplă: pe comandă apare linia de transport cu prețul fix al metodei (cu **Plătitorul expedierii** = **Expeditor**). La confirmarea comenzii, livrarea preia metoda de livrare.

### Pasul 3 — Detaliile expedierii pe livrare

Pe livrare (**Inventar → Operații → Livrări**), înainte de validare, **Detalii transportator** deschide fereastra **Detalii metodă de livrare**.

![Fereastra Detalii metodă de livrare: destinatarul și adresa, Număr de colete 1, Greutate totală, Valoare asigurată, Total comandă, Sumă de încasat și butoanele Aplică și Anulează](screenshots/03_detalii_transportator_pr.png)

**Găsește pe ecran.** Adresa destinatarului (primul rând, localitate, județ, cod poștal) și **Telefon**; **Greutate totală**; **Valoare asigurată** (valoarea declarată); **Total comandă** și **Sumă de încasat** (rambursul).

**Verifică.**
- Poșta Română primește **doar primul rând al adresei**: strada, numărul, blocul, scara și apartamentul trebuie să fie toate pe primul rând. Ce e scris pe al doilea rând nu ajunge pe AWB. Localitatea, județul și codul poștal sunt obligatorii.
- **Sumă de încasat** se calculează din ultima plată a comenzii. Fără plată înregistrată sau cu plată la livrare, este totalul comenzii, inclusiv transportul. După facturare devine restul de plată de pe facturile postate, deci avansul sau voucherul nu se mai cer o dată. Cu orice altă plată (card, transfer bancar), suma este 0, chiar dacă banii nu au intrat încă. Lista **Plată ramburs** de pe metoda de livrare nu decide rambursul: adaugă **Preț adițional pentru ramburs** la tarif și stabilește ce tranzacții primesc numărul AWB. Dacă suma propusă nu e corectă (de exemplu, comanda e plătită prin OP înainte de facturare), bifați **Sumă de încasat stabilită manual** și corectați-o.
- **Greutate totală** vine din greutatea produselor; dacă nicio linie nu are greutate, se trimite o greutate estimată.
- **Număr de colete** rămâne 1: integrarea emite un singur colet pe AWB.

**Treci mai departe.** **Aplică** salvează detaliile pe livrare. Dacă nu le aplicați, ele se calculează din livrare în momentul emiterii.

### Pasul 4 — Validarea livrării și emiterea AWB-ului

Pe livrare, **Validează**. Cu nivelul de integrare **Obține preț și creează livrare**, AWB-ul se emite în același pas; altfel, după **Aplică** din Pasul 3, apăsați **Trimite la curier** înainte de validare.

![Livrarea validată: Referință de urmărire cu numărul AWB Poșta Română, butoanele Tipărire AWB și Anulează AWB în antet și mesajul din istoric cu eticheta atașată](screenshots/04_livrare_cu_awb_pr.png)

Ce se întâmplă: Odoo trimite Poștei Române expeditorul (compania), destinatarul, greutatea, rambursul, valoarea declarată și numărul comenzii. Numărul AWB-ului primit se scrie în **Referință de urmărire**, **Stare livrare** devine **Avizat**, iar eticheta PDF se atașează livrării. La ramburs, numărul AWB-ului se scrie și pe tranzacția de plată la livrare a comenzii, dacă metoda ei de plată este în **Plată ramburs**.

Numărul AWB-ului se salvează primul: dacă eticheta nu poate fi descărcată imediat, AWB-ul rămâne pe livrare, iar istoricul spune că eticheta trebuie descărcată din nou din livrare (Pasul 5), **fără** a retrimite expedierea. O livrare care are deja AWB nu se mai trimite a doua oară la Poșta Română.

### Pasul 5 — Eticheta PDF

Pe livrare, **Tipărire AWB** descarcă eticheta. Dacă eticheta nu a fost salvată la emitere, butonul o cere din nou de la Poșta Română.

![Livrarea cu eticheta AWB Poșta Română deschisă în panoul de previzualizare a atașamentelor, lângă formular](screenshots/05_eticheta_awb_pr.png)

Verificați pe etichetă numărul AWB-ului (același cu **Referință de urmărire**), destinatarul și rambursul, apoi lipiți-o pe colet. Pentru mai multe livrări odată: în lista de livrări, selectați-le și alegeți din meniul de tipărire **Descărcare livrări**, apoi **Aplică**; etichetele se adună într-un singur PDF. Acțiunea **Tipărire AWB-uri** din același meniu lucrează pe o singură livrare selectată.

### Pasul 6 — Lista AWB-urilor: găsește → verifică → acționează

**Inventar → Operații → AWB de livrare → Listă AWB de livrare**, filtrați după **Transportator** = Poșta Română.

Atenție: un AWB Poșta Română **nu apare singur** în această listă. Rândul se creează la interogarea stării, iar Poșta Română nu are urmărire, deci nici acțiunea programată, nici butonul **Reîmprospătează** din listă nu îl aduc. AWB-ul ajunge în listă doar după:
- **Istoric → Reîmprospătează** pe livrare (fila **Istoric** apare după emiterea AWB-ului), sau **Acțiuni → Preia istoricul AWB** pe mai multe livrări selectate în lista de livrări;
- crearea procesului-verbal de predare la curier, dacă este instalat `deltatech_delivery_handover`.

![Lista AWB de livrare filtrată pe Poșta Română, după Preia istoricul AWB: coloanele Număr, Dată, Transportator, Comandă de vânzare, Stare livrare Avizat și Valoare ramburs](screenshots/06_lista_awb_pr.png)

**Găsește pe ecran.** Fiecare rând este un AWB: **Număr** (AWB-ul), **Dată** (data validării livrării), **Comandă de vânzare**, **Stare livrare** și **Valoare ramburs**. Coloanele **Expeditor** și **Destinatar** rămân goale pentru aceste AWB-uri: destinatarul se vede pe comandă.

**Verifică.**
- Fiecare livrare expediată și adusă în listă are un singur AWB; o livrare emisă, dar lipsă din listă, înseamnă doar că nu s-a rulat **Preia istoricul AWB** pe ea, nu că AWB-ul lipsește (verificați **Referință de urmărire** pe livrare).
- **Valoare ramburs** corespunde sumei de încasat de pe livrare.
- **Stare livrare** rămâne **Avizat**: conectorul nu citește starea de la Poșta Română, deci nu treceți livrarea drept livrată pe baza acestei liste.

**Acționează.** **Vizualizare comandă** deschide comanda AWB-ului; din livrare puteți tipări din nou eticheta sau anula AWB-ul (Pasul 7).

### Pasul 7 — Anularea AWB-ului

Pe livrare, **Anulează AWB** cere confirmare: „Sigur doriți să anulați AWB-ul?".

![Dialogul de confirmare Sigur doriți să anulați AWB-ul? deschis peste livrarea cu AWB Poșta Română](screenshots/07_anulare_awb_pr.png)

La confirmare, AWB-ul se anulează la Poșta Română, iar de pe livrare se șterg referința de urmărire și eticheta.

![Livrarea după anulare: Referință de urmărire goală, Stare livrare tot Avizat, butonul Detalii transportator vizibil din nou și mesajul de anulare în istoric](screenshots/08_livrare_awb_anulat_pr.png)

Verificați în istoric mesajul de anulare. **Stare livrare** rămâne **Avizat** după anulare: nu o luați drept un AWB activ. O reemitere trimite din nou același număr de comandă ca referință.

### Note de monografie și raportare

Modulul **nu generează note contabile**. AWB-ul, eticheta și anularea sunt operații logistice.

Legăturile reale cu partea financiară sunt două, ambele prin fluxul standard:
- **costul transportului** este linia de transport adăugată pe comanda de vânzare (Pasul 2), la prețul fix al metodei; se facturează odată cu comanda, pe contul de venit configurat pe produsul de livrare. Transportul refacturat intră în baza de impozitare a TVA a livrării, la cota produsului de livrare (cota standard, 21%);
- **rambursul** trimis pe AWB este suma de încasat calculată din comandă și facturi (Pasul 3); Poșta Română îl returnează prin mandat poștal, iar încasarea se înregistrează în contabilitate prin fluxul obișnuit de încasări, nu de acest modul.

Factura de transport primită de la Poșta Română se înregistrează ca orice factură de furnizor; taxa mandatului poștal este o cheltuială pe aceeași factură de furnizor. Modulul nu preia aceste facturi.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_delivery` | detaliile expedierii, butoanele de pe livrare, lista AWB, eticheta, tipărirea în masă | dependență (manifest) |
| `deltatech_delivery_status` | câmpul **Stare livrare** (Avizat, Livrat etc.) | dependență indirectă (prin `deltatech_delivery`) |
| `delivery` | metoda de livrare, linia de transport pe comandă | dependență (manifest) |
| `stock_delivery` | emiterea la validarea livrării | dependență indirectă (se instalează odată cu `delivery` și `stock`) |
| `mail` | mesajele din istoric (AWB emis, etichetă nedescărcată, anulare) | dependență (manifest) |
| `deltatech_delivery_handover` | procesul-verbal de predare a coletelor la curier; aduce AWB-urile în listă | opțional |
| `deltatech_delivery_dashboard` | urmărirea livrărilor și tabloul de expediere | opțional |

Ce este automat: emiterea AWB-ului la validare (cu nivelul **Obține preț și creează livrare**), calculul rambursului, scrierea AWB-ului pe livrare și pe tranzacția de ramburs, descărcarea etichetei, refuzul de a retrimite o livrare care are deja AWB.
Ce rămâne manual: completarea contului și a serviciului, verificarea adresei și a rambursului, tipărirea și lipirea etichetei, aducerea AWB-urilor în listă (**Preia istoricul AWB**), anularea, urmărirea coletului (în portalul Poștei Române), verificarea în portal după un rezultat necunoscut și înregistrarea mandatului poștal la încasare.

## 8. Verificări pentru consultant

- [ ] Fila **Configurare Poșta Română** apare doar când **Furnizor** = Poșta Română.
- [ ] Un utilizator fără rolul **Administrator** nu vede **Utilizator** și **Parolă**.
- [ ] Pe comandă, cu **Plătitorul expedierii** = **Expeditor**, costul transportului este exact **Preț fix** al metodei; cu **Destinatar** devine 0.
- [ ] Un serviciu creat cu **Cod** pleacă pe AWB cu acel cod; fără serviciu, AWB-ul pleacă cu `3,1,10`.
- [ ] Comandă creată din backend, fără nicio plată înregistrată: **Sumă de încasat** = totalul comenzii, inclusiv transportul.
- [ ] Comandă cu plată prin transfer bancar încă neîncasată: **Sumă de încasat** = 0; corectați cu **Sumă de încasat stabilită manual** dacă marfa pleacă totuși cu ramburs.
- [ ] Comandă facturată, cu avans: **Sumă de încasat** = restul de plată de pe factură.
- [ ] Un bloc și un apartament scrise pe al doilea rând al adresei nu apar pe etichetă; mutate pe primul rând, apar.
- [ ] La validare, **Referință de urmărire** primește numărul AWB, **Stare livrare** devine **Avizat** și eticheta PDF se atașează livrării.
- [ ] Eticheta are același număr AWB ca livrarea, destinatarul și rambursul corecte.
- [ ] **Tipărire AWB** pe o livrare fără etichetă salvată descarcă eticheta din nou, fără a emite alt AWB.
- [ ] O a doua apăsare pe **Validează** sau **Trimite la curier** pe o livrare care are deja AWB nu emite un al doilea AWB.
- [ ] AWB-ul apare în **Listă AWB de livrare** abia după **Preia istoricul AWB** (sau **Istoric → Reîmprospătează**), cu **Valoare ramburs** corectă.
- [ ] **Anulează AWB** cere confirmare, golește referința și eticheta și lasă un mesaj în istoric; **Stare livrare** rămâne **Avizat**; AWB-ul nu mai apare activ în portalul Poștei Române.
- [ ] Toate AWB-urile emise la testare au fost anulate (nu există mediu de test).

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Răspunsul Poșta Română s-a pierdut. Rezultatul de la curier este necunoscut." | La emiterea AWB-ului: răspunsul s-a pierdut pe drum **sau** Poșta Română a răspuns cu o eroare de server ori de autentificare (de exemplu utilizator sau parolă greșite, cont inactiv). AWB-ul poate exista sau nu | **Nu** reapăsați butonul: verificați în portalul Poștei Române dacă AWB-ul există. Dacă nu există, verificați **Utilizator** și **Parolă**, apoi trimiteți din nou |
| Mesajul Poștei Române afișat ca atare (de exemplu o adresă sau un cod poștal invalid) | Poșta Română a respins datele AWB-ului | Corectați adresa în **Detalii transportator** sau pe client, apoi trimiteți din nou |
| „Eroare Poșta Română. …: …" | La descărcarea etichetei sau la anulare: eroare a serverului ori credențiale greșite; la orice operație: serverul nu poate fi contactat (conexiune refuzată, rețea) | Verificați **Utilizator** și **Parolă**; reîncercați mai târziu. După o anulare eșuată, verificați în portal dacă AWB-ul a fost totuși anulat |
| „Timp de așteptare depășit la conectarea la serverul Poșta Română: …" | Serverul Poștei Române nu a răspuns în 30 de secunde (la etichetă sau anulare), sau conexiunea nu s-a putut stabili | Reîncercați după câteva minute; după o anulare eșuată, verificați în portal |
| „Curierul nu a generat AWB-ul" | Poșta Română a răspuns fără număr de AWB | Verificați datele expedierii și contul, apoi încercați din nou |
| Mesaj în istoric: „Expedierea … a fost creată la …, dar eticheta ei nu a putut fi preluată: … AWB-ul este valid -- tipăriți din nou eticheta din livrare, nu retrimiteți expedierea." | AWB-ul a fost emis, dar eticheta nu s-a descărcat | **Tipărire AWB** pe livrare |
| „Niciun produs din … nu are greutate, deci expedierea ar pleca la … declarată la …" | Pe metoda de livrare este bifat **Necesită greutate reală**, iar produsele nu au greutate | Completați greutatea produselor sau debifați opțiunea |
| „Livrarea … este amânată. Eliberați-o pe comanda de vânzare înainte de a o trimite la curier." | Livrarea este marcată ca amânată | Eliberați-o pe comanda de vânzare |
| „Nu există etichete de tipărit" | **Descărcare livrări** pe livrări fără etichetă | Emiteți întâi AWB-urile sau folosiți **Tipărire AWB** pe fiecare livrare |
| AWB-ul emis nu apare în **Listă AWB de livrare** | Poșta Română nu are urmărire, deci rândul nu se creează automat | **Acțiuni → Preia istoricul AWB** în lista de livrări |

## 10. Capturi de ecran

Capturile **nu sunt încă generate**. Numele de mai jos sunt planificate și corespund pașilor din secțiunea 6; ele trebuie generate cu skill-ul `fisa-screenshots`, automat, din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în limba română, pe o companie RO, cu apelurile către Poșta Română simulate (fără AWB-uri reale). Fișierele se scriu în `static/description/`.

1. `01_metoda_livrare_pr.png` — metoda de livrare Poșta Română, fila **Configurare Poșta Română**.
2. `02_adauga_transport_pr.png` — fereastra **Adăugați o metodă de expediere** pe comanda de vânzare, cu prețul fix.
3. `03_detalii_transportator_pr.png` — fereastra **Detalii metodă de livrare**, cu greutatea și suma de încasat.
4. `04_livrare_cu_awb_pr.png` — livrarea validată, cu numărul AWB și butoanele **Tipărire AWB** / **Anulează AWB**.
5. `05_eticheta_awb_pr.png` — eticheta PDF în panoul de previzualizare al livrării.
6. `06_lista_awb_pr.png` — **Listă AWB de livrare** filtrată pe Poșta Română, după **Preia istoricul AWB**.
7. `07_anulare_awb_pr.png` — dialogul de confirmare a anulării AWB-ului.
8. `08_livrare_awb_anulat_pr.png` — livrarea după anulare, cu mesajul din istoric.

Comanda de regenerare, după ce testul există (cere `l10n_ro` pentru compania RO și limba română încărcată):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_delivery_pr,l10n_ro,l10n_ro_doc_screenshots \
    --load-language=ro_RO --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Păstrați trei idei. Întâi, **AWB-ul pleacă la validarea livrării**, cu datele din livrare: adresa (toată pe primul rând) și rambursul se verifică în **Detalii transportator** înainte de validare, nu după. Apoi, **conectorul lucrează doar în producție**: fiecare AWB emis la instruire sau la teste este real și trebuie anulat. În al treilea rând, **Poșta Română nu se urmărește din Odoo**: starea rămâne **Avizat** (și după anulare), AWB-urile intră în listă doar cu **Preia istoricul AWB**, iar livrarea efectivă și mandatul poștal al rambursului se verifică în portalul Poștei Române. Explicați și mesajul „rezultat necunoscut": la emitere poate ascunde și o parolă greșită, deci butonul nu se reapasă până nu ați verificat în portal dacă AWB-ul există.
