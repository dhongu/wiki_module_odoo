# Fișă Modul: Expediere cu Nemo Express — tarif, AWB, etichetă, urmărire și anulare din livrare

**Modul:** `deltatech_delivery_ne`
**Utilizator principal:** Operator expediții / responsabil depozit (emite AWB-urile și urmărește coletele); administratorul configurează contul Nemo Express
**Prioritate:** 🟡 Medie (necesar doar firmelor care expediază cu Nemo Express)

---

## 1. Scop business

Firmele care lucrează cu Nemo Express emit AWB-ul în aplicația curierului, copiind de mână adresa, greutatea și rambursul. Modulul leagă Odoo direct de API-ul Nemo Express: costul transportului se cere de la Nemo Express pe comanda de vânzare, AWB-ul se emite la validarea livrării și se confirmă pentru ridicare, eticheta PDF se atașează livrării, starea coletului se citește periodic, iar un AWB se poate anula din livrare.

Nemo Express funcționează pe platforma **Courier Manager**, așa că modulul folosește conectorul `deltatech_delivery_cm` și completează singur adresa API a Nemo Express. Nu sunt suportate lockerele și punctele de ridicare, etichetele ZPL, dimensiunile coletului, livrarea sâmbăta, deschiderea coletului, nota de restituire și linkul de urmărire pe site-ul Nemo Express.

## 2. Bază legală și context

Modulul nu are bază legală fiscală proprie. AWB-ul este documentul de transport al curierului: nu înlocuiește factura sau avizul care însoțesc marfa și nu este document contabil.

Context operațional:

- **Ramburs în cont.** Rambursul se trimite pe AWB ca ramburs virat în contul bancar al expeditorului: Nemo Express încasează de la destinatar și virează ulterior.
- **Valoare declarată.** Valoarea asigurată a coletului pleacă pe AWB ca asigurare.
- **Fără mediu de test separat.** Adresa API este cea de producție (`https://app.nemoexpress.ro/nemo/API`, completată automat în **Punct final**). Orice AWB emis la teste este real și trebuie anulat.
- **Date personale.** La fiecare cerere de tarif și expediere, Odoo trimite la Nemo Express numele, strada, numărul, localitatea, județul, codul poștal și telefonul expeditorului și destinatarului, numărul de colete, greutatea, valoarea declarată și rambursul. Este transmiterea necesară transportului; informarea clienților ține de politica de confidențialitate a firmei.

## 3. Utilizatori și roluri

- **Administratorul** (rolul **Administrator** pe fișa utilizatorului, grupul tehnic **Rol / Administrator**) completează **Cheie API**, **Utilizator** și **Parolă**: câmpurile sunt vizibile doar acestui grup.
- **Inventar / Administrator** creează metoda de livrare, rulează **Inițializare** și **Preia localitățile**.
- **Vânzări / Utilizator** adaugă metoda de livrare pe comandă și cere tariful.
- **Inventar / Utilizator** verifică detaliile expedierii, validează livrarea, tipărește, urmărește și anulează AWB-ul.

Roluri recomandate pentru testare: un administrator pentru configurare (pașii 1–2), un utilizator de vânzări pentru Pasul 3, un utilizator de inventar pentru pașii 4–9.

## 4. Conturi și date implicate

Modulul **nu folosește conturi contabile** și nu creează note contabile.

Date minime pentru demo:
- un cont Nemo Express cu cheie API;
- o metodă de livrare cu **Furnizor** = **Nemo Express** și un produs de livrare de tip serviciu;
- compania cu adresă completă (stradă, număr, localitate, județ, cod poștal) și telefon;
- un client cu adresă completă și telefon;
- produse cu greutate pe fișa produsului;
- o comandă de vânzare fără plată înregistrată (ramburs = total) și una plătită cu transfer bancar (ramburs 0).

## 5. Configurare inițială

1. Instalați `deltatech_delivery_ne`, direct sau din **Inventar → Configurare → Setări → Conectori de transport**, bifa **Nemo Express** (linkul **Metode de livrare Nemo Express** deschide metodele lui). Modulul aduce `deltatech_delivery_cm` și `deltatech_delivery`.
2. **Inventar → Configurare → Livrare → Metode de livrare → Nou**: **Furnizor** = **Nemo Express**, **Livrare produs** = un produs de tip serviciu. **Punct final** se completează automat cu adresa API Nemo Express. Cu **Nivel de integrare** = **Obține preț și creează livrare**, AWB-ul se emite la validarea livrării, dacă tipul de operație al livrărilor are bifat **Generează etichete de expediere** (**Inventar → Configurare → Tip operație**; bifat implicit la livrări).
3. Fila **Configurare Nemo Express**: **Cheie API**; **Utilizator** și **Parolă** sunt obligatorii în formular, dar API-ul folosește doar cheia (completați-le cu datele contului). Atenție: în această filă cheia API și parola se văd în clar, nu sunt mascate; ele sunt vizibile doar administratorilor. **Partener companie** este doar informativ: arată partenerul companiei metodei de livrare (sau al companiei curente) și servește la alegerea adresei de ridicare; nu se completează.
4. **Inițializare** importă serviciile contului Nemo Express; apoi alegeți **Serviciu**.
5. **Preia localitățile** adaugă în nomenclatorul de localități ale României localitățile Nemo Express care lipsesc, fără dubluri ale celor existente deja în Odoo (doar pe județele găsite în Odoo).
6. **Format etichetă CM**: **A4**, **A6** sau **A4_4xA6** (patru etichete A6 pe o pagină A4).
7. **Plată ramburs** nu decide rambursul (vezi Pasul 4): adaugă **Preț adițional pentru ramburs** la tarif (câmpul nu apare în formularul Nemo Express, deci rămâne 0) și stabilește ce tranzacții de plată primesc numărul AWB.
8. Tariful: cu câmpul **Preț fix** gol, costul transportului este cel întors de Nemo Express. Cu **Preț fix** și **Limită preț**, se cere tariful Nemo Express, iar dacă acesta e mai mic decât limita se aplică prețul fix. Cu **Preț fix** fără limită, sau cu **Omite calculul tarifului** bifat, se aplică direct prețul fix.

## 6. Flux de utilizare

### Pasul 1 — Metoda de livrare Nemo Express

**Inventar → Configurare → Livrare → Metode de livrare**, deschideți metoda Nemo Express, fila **Configurare Nemo Express**.

![Formularul metodei de livrare: Furnizor Nemo Express, butoanele Inițializare și Preia localitățile în antet și fila Configurare Nemo Express cu Punct final, Cheie API, Utilizator, Parolă, Partener companie, Plată ramburs și Format etichetă CM A4](screenshots/01_metoda_livrare_ne.png)

Ce se întâmplă: metoda este gata de folosit după ce are cheia API și serviciul (Pasul 2).

### Pasul 2 — Importul serviciilor și alegerea serviciului

Pe metoda de livrare, **Inițializare**, apoi deschideți câmpul **Serviciu**.

![Câmpul Serviciu deschis pe metoda Nemo Express, cu lista serviciilor importate din contul Nemo Express](screenshots/02_servicii_ne.png)

Ce se întâmplă: serviciile contului (principale și suplimentare) se creează în Odoo o singură dată; o nouă inițializare adaugă doar serviciile noi. Alegeți serviciul cu care pleacă implicit coletele; el se poate schimba pe fiecare livrare (Pasul 4).

### Pasul 3 — Tariful pe comanda de vânzare

Pe comanda de vânzare, **Adăugați transportul**, alegeți metoda Nemo Express; costul se cere de la Nemo Express. Apăsați **Adaugă**.

![Fereastra Adăugați o metodă de expediere: metoda Nemo Express selectată și costul transportului întors de Nemo Express](screenshots/03_adauga_transport_ne.png)

Ce se întâmplă: pe comandă apare linia de transport cu tariful Nemo Express (sau cu prețul fix, după regula din secțiunea 5). Dacă Nemo Express nu poate calcula tariful, fereastra afișează eroarea curierului.

### Pasul 4 — Detaliile expedierii pe livrare

Pe livrare, înainte de validare, **Detalii transportator** deschide fereastra **Detalii metodă de livrare**.

![Fereastra Detalii metodă de livrare pentru Nemo Express: adresa destinatarului, Serviciu, Număr de colete, Greutate totală, Valoare asigurată, Total comandă, Sumă de încasat și butonul Aplică](screenshots/04_detalii_transportator_ne.png)

**Găsește pe ecran.** Adresa destinatarului și **Telefon**, **Serviciu**, **Număr de colete**, **Greutate totală**, **Valoare asigurată**, **Sumă de încasat**.

**Verifică.**
- Adresa are două rânduri: Nemo Express primește strada din primul rând și numărul din al doilea; un număr scris doar în primul rând ajunge pe AWB lipit de stradă, cu câmpul număr gol.
- **Număr de colete** corespunde coletelor fizice: Nemo Express acceptă mai multe colete pe un AWB.
- **Greutate totală** se trimite în kilograme întregi (partea zecimală se taie); pentru colete sub 1 kg, verificați cu Nemo Express cum se tratează.
- **Sumă de încasat** se calculează din ultima plată a comenzii. Fără plată înregistrată sau cu plată la livrare, este totalul comenzii, inclusiv transportul. După facturare devine restul de plată de pe facturile postate, deci avansul sau voucherul nu se mai cer o dată. Cu orice altă plată (card, transfer bancar), suma este 0, chiar dacă banii nu au intrat încă. Lista **Plată ramburs** de pe metoda de livrare nu decide rambursul: adaugă **Preț adițional pentru ramburs** la tarif și stabilește ce tranzacții primesc numărul AWB. Dacă suma propusă nu e corectă (de exemplu, comanda e plătită prin OP înainte de facturare), bifați **Sumă de încasat stabilită manual** și corectați-o.

**Treci mai departe.** **Aplică** salvează detaliile pe livrare.

### Pasul 5 — Validarea livrării: AWB emis și confirmat pentru ridicare

Pe livrare, **Validează** (sau **Trimite la curier** înainte de validare, când nivelul de integrare este **Obține preț**).

![Livrarea validată: Referință de urmărire cu numărul AWB Nemo Express, Stare livrare Avizat, butoanele Tipărire AWB și Anulează AWB și mesajul din istoric cu eticheta atașată](screenshots/05_livrare_cu_awb_ne.png)

Ce se întâmplă: Odoo creează AWB-ul la Nemo Express, scrie numărul în **Referință de urmărire**, apoi confirmă AWB-ul pentru ridicare (starea „neridicat" la Nemo Express) și descarcă eticheta PDF în formatul ales. **Stare livrare** devine **Avizat**. La ramburs, numărul AWB-ului se scrie și pe tranzacția de plată la livrare a comenzii, dacă metoda ei de plată este în **Plată ramburs**.

Numărul AWB-ului se salvează primul: dacă confirmarea sau eticheta eșuează, AWB-ul rămâne pe livrare, iar istoricul spune ce a eșuat. În acest caz **nu** retrimiteți livrarea; finalizați AWB-ul și descărcați eticheta din aplicația Nemo Express.

### Pasul 6 — Eticheta PDF

Pe livrare, **Tipărire AWB** descarcă eticheta salvată la emitere.

![Eticheta AWB Nemo Express în format A4 deschisă în panoul de previzualizare a atașamentelor livrării](screenshots/06_eticheta_awb_ne.png)

Verificați pe etichetă numărul AWB-ului, destinatarul, numărul de colete și rambursul, apoi lipiți-o pe colet. Eticheta nu se cere din nou de la Nemo Express: dacă nu a fost salvată la emitere, **Tipărire AWB** nu descarcă nimic.

### Pasul 7 — Urmărirea coletului

Fila **Istoric** a livrării (apare după emiterea AWB-ului) arată evenimentele citite de la Nemo Express; **Reîmprospătează** le cere imediat. Altfel, acțiunea programată „Livrare: actualizează starea livrării" le citește periodic.

![Fila Istoric a livrării Nemo Express: evenimentele cu dată și descriere, butonul Reîmprospătează și Stare livrare În livrare](screenshots/07_istoric_livrare_ne.png)

**Găsește pe ecran.** **Stare livrare** și rândurile din **Istoric** (dată, descriere).

**Verifică.** Starea urmează starea Nemo Express: „neridicat" → **Avizat**, „avizat" → **În depozit curier**, „în curs" → **În livrare**, „livrat" → **Livrat**. Orice altă stare Nemo Express (de exemplu un refuz sau un retur) face citirea să eșueze: livrarea își păstrează starea anterioară, iar eșecul se numără pe AWB. După 5 eșecuri și cel puțin 48 de ore, AWB-ul este marcat **Nu poate fi interogat** și nu mai este citit (până la **Reia interogarea stării** din lista AWB). Un colet refuzat nu ajunge deci niciodată în starea **Refuzat** și nici în lista **Ramburs refuzat - factură deschisă**: coletele blocate pe **Avizat**, **În depozit curier** sau **În livrare** se verifică manual în aplicația Nemo Express.

### Pasul 8 — Lista AWB-urilor: găsește → verifică → acționează

**Inventar → Operații → AWB de livrare → Listă AWB de livrare**, filtrați după **Transportator** = Nemo Express.

![Lista AWB de livrare filtrată pe Nemo Express: coloanele Număr, Dată, Transportator, Comandă de vânzare, Stare livrare și Valoare ramburs](screenshots/08_lista_awb_ne.png)

**Găsește pe ecran.** **Număr**, **Dată**, **Comandă de vânzare**, **Stare livrare**, **Valoare ramburs**. Rândurile se creează la citirea stării (acțiunea programată sau **Reîmprospătează**); coloanele **Expeditor** și **Destinatar** rămân goale pentru aceste AWB-uri. Coloana opțională **Nu poate fi interogat** arată AWB-urile scoase din citire.

**Verifică.**
- Coletele expediate acum câteva zile au trecut de **Avizat**; un AWB rămas **Avizat**, **În depozit curier** sau **În livrare** mai mult decât de obicei înseamnă un colet neridicat, refuzat sau o stare necitită: verificați-l în aplicația Nemo Express.
- **Valoare ramburs** corespunde sumei de încasat.
- Coletele cu **Stare livrare** = **Livrat** și ramburs sunt cele pe care Nemo Express trebuie să le vireze.

**Acționează.** **Reîmprospătează** citește din nou stările; **Reia interogarea stării** repune în citire un AWB **Nu poate fi interogat**; **Vizualizare comandă** deschide comanda; din livrare, anulați un AWB neridicat (Pasul 9).

### Pasul 9 — Anularea AWB-ului

Pe livrare, **Anulează AWB** cere confirmare: „Sigur doriți să anulați AWB-ul?".

![Dialogul de confirmare Sigur doriți să anulați AWB-ul? deschis peste livrarea cu AWB Nemo Express](screenshots/09_anulare_awb_ne.png)

La confirmare, AWB-ul se anulează la Nemo Express, iar referința de urmărire și eticheta se șterg de pe livrare. **Stare livrare** rămâne cea dinainte (de obicei **Avizat**).

### Note de monografie și raportare

Modulul **nu generează note contabile**. Tariful, AWB-ul, eticheta, urmărirea și anularea sunt operații logistice.

Legăturile reale cu partea financiară, prin fluxul standard:
- **costul transportului** este linia de transport de pe comanda de vânzare (Pasul 3), cu tariful Nemo Express sau prețul fix; se facturează odată cu comanda, pe contul de venit configurat pe produsul de livrare;
- **rambursul** trimis pe AWB este suma de încasat calculată din comandă și facturi (Pasul 4); viramentul Nemo Express se înregistrează în contabilitate prin fluxul de încasări (de exemplu cu `deltatech_delivery_cod` pentru decontarea rambursurilor), nu de acest modul.

Factura de transport Nemo Express se înregistrează ca orice factură de furnizor; modulul nu o preia.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_delivery_cm` | conectorul Courier Manager: tarif, AWB, confirmare, etichetă, servicii, localități, stare, anulare | dependență (manifest) |
| `deltatech_delivery` | detaliile expedierii, butoanele de pe livrare, lista AWB, urmărirea periodică | dependență (manifest) |
| `deltatech_delivery_status` | câmpul **Stare livrare** | dependență indirectă (prin `deltatech_delivery`) |
| `delivery`, `mail` | metoda de livrare, linia de transport, mesajele din istoric | dependență (manifest) |
| `stock_delivery` | emiterea la validarea livrării | dependență indirectă (se instalează odată cu `delivery` și `stock`) |
| `deltatech_delivery_handover` | procesul-verbal de predare a coletelor la curier | opțional |
| `deltatech_delivery_dashboard` | carduri de urmărire și tabloul de expediere | opțional |
| `deltatech_delivery_cod` (bitshop_ent) | decontarea rambursului virat de curier | opțional |

Ce este automat: adresa API, tariful pe comandă, emiterea și confirmarea AWB-ului la validare, eticheta, rambursul, scrierea AWB-ului pe tranzacția de ramburs, citirea periodică a stării pentru cele patru stări cunoscute.
Ce rămâne manual: cheia API, inițializarea serviciilor și importul localităților, verificarea adresei, a greutății și a rambursului, tipărirea etichetei, anularea, urmărirea refuzurilor și retururilor în aplicația Nemo Express și reconcilierea viramentului de ramburs.

## 8. Verificări pentru consultant

- [ ] La alegerea furnizorului **Nemo Express**, **Punct final** se completează cu `https://app.nemoexpress.ro/nemo/API`.
- [ ] **Inițializare** creează serviciile Nemo Express; o a doua apăsare nu le dublează.
- [ ] **Preia localitățile** adaugă localitățile lipsă, fără dubluri ale celor existente deja în Odoo.
- [ ] Pe comandă, costul transportului este tariful Nemo Express (fără preț fix) sau prețul fix (după regula cu **Limită preț**).
- [ ] Comandă creată din backend, fără nicio plată înregistrată: **Sumă de încasat** = totalul comenzii, inclusiv transportul.
- [ ] Comandă cu plată prin transfer bancar încă neîncasată: **Sumă de încasat** = 0; corectați cu **Sumă de încasat stabilită manual** dacă marfa pleacă totuși cu ramburs.
- [ ] Comandă facturată, cu avans: **Sumă de încasat** = restul de plată de pe factură.
- [ ] La validare, livrarea primește AWB-ul, **Stare livrare** = **Avizat**, iar eticheta PDF, în formatul ales, este atașată.
- [ ] O a doua apăsare pe **Validează** sau **Trimite la curier** nu emite un al doilea AWB.
- [ ] **Reîmprospătează** din fila **Istoric** aduce evenimentele Nemo Express și actualizează **Stare livrare**.
- [ ] În **Listă AWB de livrare**, AWB-urile Nemo Express au **Valoare ramburs** corectă și stări actualizate.
- [ ] **Anulează AWB** cere confirmare, golește referința și eticheta; AWB-ul apare anulat în aplicația Nemo Express.
- [ ] Un AWB cu o stare Nemo Express necunoscută (refuz, retur) rămâne pe starea anterioară și, după 5 eșecuri în minimum 48 de ore, apare cu **Nu poate fi interogat**.
- [ ] O greutate cu zecimale (de exemplu 2,7 kg) apare pe AWB ca 2 kg; dacă nu este acceptabil, rotunjiți greutatea în **Detalii transportator**.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| Mesajul Nemo Express afișat ca atare (de exemplu cheie API invalidă, adresă sau serviciu invalid) | Nemo Express a răspuns, dar a respins cererea; o cheie API greșită produce cel mai probabil acest mesaj | Verificați **Cheie API**; corectați datele în **Detalii transportator** sau pe metoda de livrare |
| „Eroare Courier Manager. …" | Eroare de conexiune sau eroare HTTP la o operație care nu schimbă nimic (tarif, servicii, localități, etichetă, stare): server indisponibil, **Punct final** greșit | Verificați **Punct final**; reîncercați mai târziu |
| „Cererea de tarif la Courier Manager a eșuat" / eroarea curierului la **Adăugați transportul** | Tariful nu a putut fi calculat | Verificați adresa clientului și serviciul; folosiți temporar un preț fix |
| „Răspuns neașteptat de la Courier Manager" | Răspunsul de tarif nu are prețul | Verificați serviciul ales; contactați Nemo Express |
| „Răspunsul Courier Manager s-a pierdut. Rezultatul de la curier este necunoscut." | La emiterea sau anularea AWB-ului: răspunsul s-a pierdut pe drum sau Nemo Express a răspuns cu o eroare HTTP (inclusiv de autentificare). Operația poate fi făcută sau nu la Nemo Express | **Nu** reapăsați butonul: verificați în aplicația Nemo Express dacă AWB-ul există (sau a fost anulat) |
| Mesaj în istoric: „Expedierea … a fost creată la …, dar eticheta ei nu a putut fi preluată: …" | AWB-ul a fost creat, dar confirmarea pentru ridicare sau eticheta a eșuat | Finalizați AWB-ul și descărcați eticheta din aplicația Nemo Express; nu retrimiteți livrarea |
| Mesaj Nemo Express „Shipment is not finalized yet" | Eticheta a fost cerută pentru un AWB neconfirmat | Confirmați AWB-ul în aplicația Nemo Express |
| „Niciun produs din … nu are greutate, deci expedierea ar pleca la … declarată la …" | **Necesită greutate reală** este bifat, iar produsele nu au greutate | Completați greutatea produselor sau debifați opțiunea |
| „Livrarea … este amânată. Eliberați-o pe comanda de vânzare înainte de a o trimite la curier." | Livrare amânată | Eliberați-o pe comanda de vânzare |

## 10. Capturi de ecran

Capturile **nu sunt încă generate**. Numele de mai jos sunt planificate și corespund pașilor din secțiunea 6; ele trebuie generate cu skill-ul `fisa-screenshots`, automat, din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în limba română, pe o companie RO, cu API-ul Nemo Express simulat (fără AWB-uri reale). Fișierele se scriu în `static/description/`.

1. `01_metoda_livrare_ne.png` — metoda de livrare Nemo Express, fila **Configurare Nemo Express**.
2. `02_servicii_ne.png` — câmpul **Serviciu** cu serviciile importate după **Inițializare**.
3. `03_adauga_transport_ne.png` — fereastra **Adăugați o metodă de expediere**, cu tariful Nemo Express.
4. `04_detalii_transportator_ne.png` — fereastra **Detalii metodă de livrare**.
5. `05_livrare_cu_awb_ne.png` — livrarea validată, cu AWB-ul și starea **Avizat**.
6. `06_eticheta_awb_ne.png` — eticheta PDF în panoul de previzualizare.
7. `07_istoric_livrare_ne.png` — fila **Istoric** cu evenimentele Nemo Express.
8. `08_lista_awb_ne.png` — **Listă AWB de livrare** filtrată pe Nemo Express.
9. `09_anulare_awb_ne.png` — dialogul de confirmare a anulării AWB-ului.

Comanda de regenerare, după ce testul există (cere `l10n_ro` pentru compania RO și limba română încărcată):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_delivery_ne,l10n_ro,l10n_ro_doc_screenshots \
    --load-language=ro_RO --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Păstrați trei idei. Întâi, **Nemo Express este un curier pe platforma Courier Manager**: configurarea are o cheie API, nu utilizator și parolă, iar mesajele de eroare vorbesc despre „Courier Manager". Apoi, **la validare AWB-ul este și creat, și confirmat pentru ridicare**: dacă istoricul spune că un pas ulterior a eșuat, AWB-ul există deja și nu se retrimite. În al treilea rând, **starea coletului vine de la Nemo Express**, periodic sau la **Reîmprospătează**, pe patru trepte (Avizat, În depozit curier, În livrare, Livrat); refuzurile și retururile nu se văd în Odoo și se urmăresc în aplicația Nemo Express. Atrageți atenția asupra greutății, care pleacă în kilograme întregi.
