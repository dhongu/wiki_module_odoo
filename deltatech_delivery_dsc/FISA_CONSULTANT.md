# Fișă Modul: Expediere cu Dragon Star Curier — tarif, AWB, etichetă, borderou și urmărire

**Modul:** `deltatech_delivery_dsc`
**Utilizator principal:** Operator expediții / depozit (emite și tipărește AWB-urile), Administrator Inventar (configurează curierul)
**Prioritate:** 🟡 Medie (necesar doar firmelor care expediază cu Dragon Star Curier; pentru ele, fără modul AWB-urile se introduc de mână în aplicația web DSC)

---

## 1. Scop business

Firmele care lucrează cu Dragon Star Curier (DSC) emit altfel fiecare AWB în aplicația web DSC, copiind adresa clientului, numărul de colete, greutatea și rambursul din comanda din Odoo. Modulul face legătura direct, prin API-ul Dragon Star:

- **tariful** transportului se cere de la DSC pe comanda de vânzare, pentru punctul de lucru din care pleacă marfa (sau se folosește un preț fix);
- **AWB-ul** se emite din livrare, cu **eticheta** în PDF (A4 sau A6) sau ZPL atașată;
- **rambursul**, valoarea declarată, numărul de colete și opțiunile (livrare sâmbăta, deschidere la livrare, notificare SMS) pleacă din Odoo, fără reintroducere;
- seara, o acțiune planificată creează **borderoul** zilei și trimite **comenzile de ridicare**, așa că AWB-urile pot fi anulate din Odoo până atunci (în limita celor 30 de minute permise de DSC);
- **starea** expedierii se citește de la DSC și se scrie în istoricul livrării.

Modulul funcționează cu noul **API v1** Dragon Star (cheie API) și, până la retragerea lui de către DSC, cu API-ul vechi (utilizator și parolă).

## 2. Bază legală și context

Nu are bază legală fiscală proprie: este un conector operațional cu un curier. Contextul relevant:

- AWB-ul este documentul de transport al curierului; nu înlocuiește factura sau avizul care însoțesc marfa și nu este document contabil.
- **Anularea unui AWB** e permisă de Dragon Star doar în primele **30 de minute** de la emitere și doar cât AWB-ul nu a intrat într-un borderou. După aceea, anularea se cere la Dragon Star, pe e-mail (adresa apare în mesajul din Odoo).
- **Borderoul** DSC cuprinde toate AWB-urile încă neincluse într-un borderou; de aceea modulul nu îl creează la fiecare AWB, ci o dată pe zi, la ora 18:00 a serverului (UTC), adică 20:00 iarna și 21:00 vara, ora României.
- **Date personale trimise curierului:** la fiecare cerere de tarif și la fiecare expediere, Odoo trimite la DSC numele, persoana de contact, adresa, județul, localitatea, codul poștal, telefonul și e-mailul destinatarului, numărul de colete și greutatea, rambursul, valoarea declarată, observațiile livrării și punctul de lucru. Comanda de ridicare conține și adresa și telefonul de ridicare.
- Dragon Star **nu are server de test**: pentru încercări folosiți o cheie API separată. Orice AWB, borderou sau comandă de ridicare făcută la încercări este reală la DSC. Tarifele se pot cere doar dacă DSC le-a activat pe contul firmei.

## 3. Utilizatori și roluri

- **Administrator Inventar** configurează metoda de livrare (**Inventar → Configurare → Livrare → Metode de expediere**). Câmpurile de acces (**DSC API Key**, **Utilizator**, **Parolă**) sunt vizibile doar utilizatorilor cu drept de **Administrare / Setări**.
- **Operatorul de vânzări** (**Vânzări / Utilizator** și **Inventar / Utilizator**) alege metoda de livrare pe comandă și obține tariful.
- **Operatorul de depozit / expediții** completează detaliile expedierii, validează livrarea, tipărește eticheta, anulează la nevoie AWB-ul și urmărește starea.

Roluri recomandate pentru testare:
- Administrator (Setări + Inventar): configurează metoda și apasă **Inițializare**.
- Utilizator Vânzări + Inventar: parcurge fluxul din secțiunea 6 de la Pasul 3 încolo (comanda, apoi livrarea).
- Utilizator Inventar fără drept de Setări: verifică faptul că nu vede cheia API.

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile: modulul nu creează note contabile (vezi „Note de monografie și raportare” din secțiunea 6).

Date minime pentru demo:
- o cheie API Dragon Star de test, emisă în aplicația web DSC, cu adresa IP a serverului Odoo înscrisă;
- compania cu adresa completă (stradă, localitate, județ) și cel puțin un punct de lucru DSC;
- un produs de livrare de tip serviciu pentru metoda de livrare;
- un produs stocabil cu greutate și stoc disponibil;
- un client cu adresă din România (stradă, localitate, județ), telefon și e-mail;
- o comandă de vânzare creată din backend, fără plată înregistrată, ca livrarea să aibă ramburs (totalul comenzii), și una cu plată prin transfer bancar, fără ramburs.

## 5. Configurare inițială

1. Instalați `deltatech_delivery_dsc` (aduce `deltatech_delivery`).
2. În aplicația web DSC, la *Settings → API access* (cu autentificare în doi pași), creați o cheie API și înscrieți adresele IP publice ale serverului Odoo.
3. **Inventar → Configurare → Livrare → Metode de expediere** → **Nou**: **Furnizor** = *Dragon Star Curier*, produsul de livrare de tip serviciu.
4. În fila **Configurare DSC**: **DSC API Version** = *API v1 (API key)* și **DSC API Key** (cheia de la pasul 2). O metodă rămasă pe API-ul vechi (*Legacy API*) folosește **Utilizator** și **Parolă**; Dragon Star păstrează acel API cel puțin până la 31 martie 2027.
5. Tot în **Configurare DSC**: **Tip etichetă DSC** (pdf sau zpl), **Format de pagină DSC** (A4 sau A6, doar pentru pdf) și **Plată ramburs** (metodele de plată la livrare). **Atenție:** câmpul **Preț adițional pentru ramburs** nu apare în formularul metodei DSC, deci momentan nu se poate seta un supliment de ramburs pe tariful DSC.
6. Apăsați **Inițializare**, apoi **Preia localitățile** (antetul formularului), descrise la Pasul 1 și Pasul 2 din secțiunea 6. **Preia locațiile de ridicare** face doar importul punctelor de lucru (partea din **Inițializare** care le aduce), util când DSC adaugă un punct de lucru nou.
7. Opțional, preț fix: **Preț fix** și pragul din rândul „dacă prețul calculat este mai mic decât”. Doar cu **Preț fix** completat (fără prag), DSC nu mai este întrebat de tarif.
8. Verificați că acțiunea planificată **DSC: creează borderoul și comenzile de ridicare** este activă (**Setări → Tehnic → Automatizare → Acțiuni planificate**, mod dezvoltator). Ora rulării (18:00 UTC) se poate schimba din acțiune, dar se reface la ora inițială la fiecare actualizare a modulului.

## 6. Flux de utilizare

### Pasul 1 — Configurarea metodei de livrare Dragon Star

Din **Inventar → Configurare → Livrare → Metode de expediere**, deschideți metoda Dragon Star și completați fila **Configurare DSC**.

![Formularul metodei de livrare Dragon Star Curier, fila Configurare DSC: DSC API Version pe API v1 (API key), cheia API mascată, Tip etichetă DSC pdf, Format de pagină DSC A4 și Plată ramburs completat; în antet butoanele Inițializare și Preia localitățile](screenshots/01_configurare_dsc.png)

**Găsește pe ecran.** Fila **Configurare DSC** apare doar când **Furnizor** este *Dragon Star Curier*. Pe *API v1* se vede doar **DSC API Key**; pe *Legacy API* se văd **Utilizator** și **Parolă**. **Format de pagină DSC** apare doar pentru eticheta pdf.

**Verifică.** Cheia API este lipită fără spații în plus; adresa IP a serverului este înscrisă în aplicația web DSC (altfel DSC refuză cererile, vezi secțiunea 9). În colțul formularului, butonul de mediu (**Test / Producție**) nu schimbă nimic la DSC: există un singur server, iar diferența dintre test și producție o face cheia API.

**Treci mai departe.** Salvați și apăsați **Inițializare**.

### Pasul 2 — Inițializarea: punctele de lucru și localitățile

**Inițializare** citește de la DSC punctele de lucru ale contului și le adaugă în fila **Locație de ridicare**, ca locații de ridicare, fiecare cu o adresă de livrare a companiei. **Preia localitățile** adaugă în nomenclatorul de localități ale României pe cele din DSC care lipsesc.

![Fila Locație de ridicare a metodei Dragon Star după Inițializare: Sursa locației de ridicare Din curier și lista punctelor de lucru DSC, cu numele, adresa companiei și referința punctului de lucru](screenshots/02_locatii_ridicare.png)

**Găsește pe ecran.** În fila **Locație de ridicare**, câte un rând pentru fiecare punct de lucru: nume, adresă, depozit și **Referință** (codul punctului de lucru DSC).

**Verifică.** Fiecare punct de lucru din contul DSC apare o singură dată (o nouă **Inițializare** nu dublează rândurile). Punctul din care pleacă AWB-ul depinde de **Sursa locației de ridicare**:
- pe **Din curier** (implicit) contează **Adresa de ridicare** de pe metodă; depozitul de pe rânduri nu are efect;
- pe **Din depozit** se folosește rândul al cărui depozit este depozitul livrării, deci completați coloana depozitului pentru fiecare punct de lucru;
- pe o livrare anume, punctul se poate alege și în fereastra de detalii, câmpul **Locație de ridicare** (Pasul 4), care are prioritate;
- câmpul **Referință** al adresei de ridicare se trimite la DSC drept cod al punctului de lucru. Adresele create de **Inițializare** au deja codul DSC. Fără **Adresa de ridicare** pe metodă (sau pe **Din companie**), se trimite **Referință** de pe fișa companiei: lăsați-o goală sau puneți codul unui punct de lucru DSC. Pe API v1, o referință care nu este număr (de exemplu un cod intern) face ca tariful și emiterea AWB-ului să eșueze.

**Treci mai departe.** Metoda e gata de folosit pe comenzi.

### Pasul 3 — Tariful pe comanda de vânzare

Din **Vânzări → Comenzi → Comenzi**, pe comandă, **Adăugați transportul** → alegeți metoda Dragon Star → **Obține preț** → **Adaugă**.

![Comanda de vânzare cu linia de transport Dragon Star Curier adăugată și costul transportului primit de la DSC, fără TVA](screenshots/03_comanda_tarif_dsc.png)

**Găsește pe ecran.** Linia de transport cu produsul de livrare și prețul calculat de DSC.

**Verifică.** Prețul este tariful DSC fără TVA pentru punctul de lucru al expedierii. Un supliment de ramburs s-ar adăuga doar dacă furnizorul tranzacției de plată a comenzii (în practică, comenzile din magazinul online plătite la livrare) este în **Plată ramburs**; cum **Preț adițional pentru ramburs** nu apare în formularul DSC, suplimentul nu se poate seta momentan. Dacă metoda are doar **Preț fix**, apare prețul fix. Dacă DSC nu are tarifele activate pe cont, apare mesajul de eroare din secțiunea 9.

**Treci mai departe.** Confirmați comanda: se creează livrarea de ieșire.

### Pasul 4 — Detaliile expedierii

Pe livrare (**Inventar → Operații → Livrări**, sau butonul **Livrare** de pe comandă), **Detalii transportator** deschide fereastra **Detalii metodă de livrare**.

![Fereastra Detalii metodă de livrare pentru Dragon Star: adresa destinatarului, Locație de ridicare, Număr de colete, Greutate totală, Valoare asigurată, Total comandă, Sumă de încasat și Opțiuni de livrare Saturday Delivery, Open Package, SMS Notification](screenshots/04_detalii_expediere.png)

**Găsește pe ecran.** Adresa destinatarului (stradă, localitate, județ, cod poștal, telefon), **Locație de ridicare**, **Număr de colete**, **Greutate totală**, **Valoare asigurată** (valoarea declarată), **Total comandă**, **Sumă de încasat** și **Opțiuni de livrare**.

**Verifică.**
- **Sumă de încasat** se calculează din ultima plată a comenzii. Fără plată înregistrată sau cu plată la livrare, este totalul comenzii, inclusiv transportul. După facturare devine restul de plată de pe facturile postate, deci avansul sau voucherul nu se mai cer o dată. Cu orice altă plată (card, transfer bancar), suma este 0, chiar dacă banii nu au intrat încă. Lista **Plată ramburs** de pe metoda de livrare nu decide rambursul: adaugă **Preț adițional pentru ramburs** la tarif și stabilește ce tranzacții primesc numărul AWB. Dacă suma propusă nu e corectă (de exemplu, comanda e plătită prin OP înainte de facturare), bifați **Sumă de încasat stabilită manual** și corectați-o. La DSC, **Preț adițional pentru ramburs** nu apare pe formular, deci lista influențează doar numărul AWB scris pe tranzacții.
- Greutatea se rotunjește la kilogram întreg (minimum 1 kg) când pleacă la DSC.
- Opțiunile disponibile la DSC sunt livrarea sâmbăta, deschiderea la livrare și notificarea prin SMS.

**Treci mai departe.** **Aplică** salvează detaliile; **Trimite la curier** emite direct AWB-ul.

### Pasul 5 — Emiterea AWB-ului

AWB-ul se emite la validarea livrării sau cu **Trimite la curier** (antetul livrării, după aplicarea detaliilor).

![Livrarea validată cu AWB-ul Dragon Star în Referință de urmărire, butoanele Tipărire AWB și Anulează AWB în antet și mesajul din istoric despre trimiterea la curier, cu eticheta atașată](screenshots/05_livrare_awb_emis.png)

**Găsește pe ecran.** **Referință de urmărire** (numărul AWB), butoanele **Tipărire AWB** și **Anulează AWB**, butonul **Urmărire** (deschide expedierea pe site-ul Dragon Star) și, în istoric, mesajul cu eticheta atașată.

**Verifică.** Numărul AWB apare pe livrare. Dacă eticheta nu a putut fi descărcată, AWB-ul rămâne totuși pe livrare (nu se emite altul), iar eticheta se cere din nou cu **Tipărire AWB**. Dacă răspunsul DSC s-a pierdut pe drum, livrarea primește „rezultat incert”: verificați în aplicația web DSC dacă AWB-ul există înainte de a retrimite.

**Treci mai departe.** Tipăriți eticheta (Pasul 6).

### Pasul 6 — Eticheta AWB

**Tipărire AWB** descarcă eticheta (fișierul `LabelDSC-<AWB>.pdf` sau `.zpl`).

![Eticheta AWB Dragon Star în format PDF A4, în macheta curierului: numărul AWB, expeditorul, destinatarul, coletele și suma de încasat](screenshots/06_eticheta_awb.png)

**Găsește pe ecran.** Eticheta este generată de Dragon Star, în macheta lor: numărul AWB, expeditorul (punctul de lucru), destinatarul, coletele și suma de încasat.

**Verifică.** Rambursul de pe etichetă este cel din **Sumă de încasat**; formatul (A4/A6 sau ZPL) corespunde setării de pe metodă.

**Treci mai departe.** Lipiți eticheta pe colet. Pentru mai multe livrări odată, bifați-le în lista de livrări și alegeți **Tipărire AWB-uri** din meniul de tipărire al listei (**Tipăriți**, lângă **Acțiuni**), din `deltatech_delivery`.

### Pasul 7 — Anularea AWB-ului

**Anulează AWB** (antetul livrării) cere confirmare („Sigur doriți să anulați AWB-ul?”) și șterge AWB-ul la DSC.

![Mesajul de eroare la Anulează AWB pentru un AWB emis de mai mult de 30 de minute: Dragon Star permite ștergerea doar în primele 30 de minute, cu adresa de e-mail la care se cere anularea](screenshots/07_anulare_refuzata.png)

**Găsește pe ecran.** În primele 30 de minute și înainte de borderou, după confirmare, **Referința de urmărire** se golește, iar istoricul livrării spune că expedierea a fost anulată. În afara acestor condiții apare mesajul din captură.

**Verifică.** Odoo refuză singur anularea pe care DSC ar refuza-o și spune ce condiție nu e îndeplinită: AWB-ul e deja într-un borderou (cu numărul borderoului) sau au trecut mai mult de 30 de minute. În acest caz anularea se cere la Dragon Star, la adresa din mesaj.

**Treci mai departe.** După o anulare reușită, livrarea poate fi retrimisă la curier, cu un AWB nou.

### Pasul 8 — Borderoul și comanda de ridicare

În fiecare zi, la ora 18:00 UTC (20:00 iarna, 21:00 vara, ora României), acțiunea planificată **DSC: creează borderoul și comenzile de ridicare** creează borderoul cu AWB-urile zilei și trimite la DSC comanda de ridicare pentru fiecare expediere (pe punctul de lucru al expedierii; pe API v1, cu intervalul de ridicare 9–17).

![Acțiunea planificată DSC: creează borderoul și comenzile de ridicare, activă, cu intervalul de 1 zi, Ora Urmatoarei Executii afișată în ora României și butonul Rulează manual](screenshots/08_actiune_borderou.png)

**Găsește pe ecran.** **Setări → Tehnic → Automatizare → Acțiuni planificate** (mod dezvoltator): acțiunea DSC, intervalul (1 zi), **Ora Urmatoarei Executii** (afișată în fusul orar al utilizatorului) și butonul **Rulează manual**. Ora se poate muta din acțiune, dar revine la 18:00 UTC la fiecare actualizare a modulului.

**Atenție.** **Rulează manual** creează un borderou real și comenzi de ridicare reale la DSC (nu există server de test): după borderou, AWB-urile zilei nu mai pot fi anulate din Odoo.

**Verifică.** Acțiunea este activă. Dacă borderoul nu poate fi creat, fiecare livrare implicată primește în istoric mesajul „Dragon Star: borderoul nu a putut fi creat, deci comanda de ridicare nu a fost trimisă”; dacă doar comanda de ridicare eșuează, mesajul este „Dragon Star: comanda de ridicare nu a putut fi creată”. Livrările rămase fără comandă de ridicare sunt reluate la rularea următoare.

**Treci mai departe.** După borderou, AWB-urile nu mai pot fi anulate din Odoo (Pasul 7).

### Pasul 9 — Urmărirea stării expedierii

În fila **Istoric** a livrării, **Reîmprospătează** citește de la DSC evenimentele expedierii. Pentru mai multe livrări odată: din listă, **Acțiuni → Preia istoricul AWB**. Starea se actualizează și automat, prin acțiunea planificată **Livrare: actualizează starea livrării** (din modulele de bază).

![Fila Istoric a livrării Dragon Star: evenimentele expedierii în ordine cronologică, cu data, descrierea și locația, ultimul eveniment fiind livrarea la destinatar](screenshots/09_istoric_livrare.png)

**Găsește pe ecran.** Coloanele **Dată**, **Descriere** și **Locație**, în ordine cronologică; starea livrării se schimbă în *livrat* când DSC raportează expedierea ca livrată.

**Verifică.** Ultimul eveniment din Odoo este același cu cel de pe site-ul DSC (butonul **Urmărire**). O eroare la un AWB nu oprește actualizarea celorlalte livrări.

**Treci mai departe.** Livrările cu ramburs livrate intră în decontarea rambursurilor (`deltatech_delivery_cod`, dacă este instalat).

### Note de monografie și raportare

Modulul **nu generează note contabile**. Legăturile reale cu partea financiară sunt:

- **costul transportului** se adaugă pe comanda de vânzare ca linie cu produsul de livrare al metodei (preț DSC fără TVA sau preț fix) și se facturează clientului prin fluxul standard de vânzare;
- **rambursul** (Sumă de încasat) este suma pe care DSC o încasează de la client, calculată din ultima plată a comenzii (regula din Pasul 4); nu se înregistrează nimic în contabilitate la emiterea AWB-ului;
- decontarea rambursurilor încasate de curier se face cu `deltatech_delivery_cod` (bitshop_ent), dacă este instalat; factura de transport emisă de DSC intră pe fluxul obișnuit de factură de furnizor.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_delivery` | detaliile expedierii, butoanele de pe livrare, etichete, istoricul stării, „rezultat incert” | dependență (manifest) |
| `delivery` / `stock_delivery` (Odoo) | metoda de livrare, linia de transport pe comandă, trimiterea la validare | dependență indirectă |
| `deltatech_delivery_handover` | procesul-verbal de predare a coletelor la curier | extindere opțională |
| `deltatech_delivery_cod` (bitshop_ent) | decontarea rambursurilor încasate de curier | extindere opțională |

**Ce e automat:** tariful pe comandă, emiterea AWB-ului la validare, atașarea etichetei, borderoul și comenzile de ridicare (zilnic, la 18:00 UTC), actualizarea stării.
**Ce rămâne manual:** cheia API și înscrierea IP-ului în aplicația DSC, **Inițializare** și **Preia localitățile**, corectarea detaliilor expedierii, anularea în afara celor 30 de minute (prin e-mail la DSC), verificarea rezultatelor incerte în aplicația DSC.

## 8. Verificări pentru consultant

- [ ] Fila **Configurare DSC** apare doar pentru furnizorul *Dragon Star Curier*; pe *API v1* se vede doar cheia API, pe *Legacy API* utilizatorul și parola.
- [ ] Un utilizator fără drept de Setări nu vede **DSC API Key**, **Utilizator** și **Parolă**.
- [ ] **Inițializare** aduce punctele de lucru în fila **Locație de ridicare**; o a doua apăsare nu le dublează.
- [ ] Pe **Din curier**, cu **Adresa de ridicare** = o adresă importată, AWB-ul pleacă din acel punct de lucru; fără adresă de ridicare, **Referință** de pe fișa companiei este goală sau este un cod DSC valid.
- [ ] **Obține preț** pe comandă întoarce tariful DSC; cu **Preț fix** fără prag, apare prețul fix.
- [ ] O comandă creată din backend, fără nicio plată înregistrată, are **Sumă de încasat** egală cu totalul comenzii (inclusiv transportul).
- [ ] O comandă cu o plată prin transfer bancar încă neîncasată are **Sumă de încasat** = 0.
- [ ] La validarea livrării se completează **Referință de urmărire** și eticheta e atașată în formatul ales.
- [ ] **Anulează AWB** reușește în primele 30 de minute și golește referința; după 30 de minute sau după borderou apare mesajul cu motivul și adresa de e-mail DSC.
- [ ] Rularea manuală a acțiunii **DSC: creează borderoul și comenzile de ridicare** marchează expedierile zilei ca trimise la ridicare; o a doua rulare nu le retrimite. **Atenție:** rularea creează un borderou real și comenzi de ridicare reale la DSC; faceți-o doar pe expedieri reale sau cu acordul DSC.
- [ ] **Reîmprospătează** din fila **Istoric** aduce evenimentele DSC, iar butonul **Urmărire** deschide expedierea pe site-ul Dragon Star.

## 9. Mesaje de eroare frecvente

Unele mesaje ale API-ului v1 nu sunt încă traduse și apar în engleză; sunt redate mai jos exact cum apar.

| Mesaj | Cauză probabilă | Remediere |
|-------|-----------------|-----------|
| „The Dragon Star API key is not set. Create one in the DSC web application (Settings > API access).” | Metoda e pe *API v1*, fără cheie API | Creați cheia în aplicația web DSC și completați **DSC API Key** |
| „Dragon Star refused the API key. …” | Cheie greșită, expirată sau revocată | Verificați cheia în aplicația DSC și lipiți-o din nou |
| „The server IP address is not allowed for this Dragon Star API key. …” | Adresa IP a serverului Odoo nu e înscrisă la cheia API | Înscrieți IP-ul public al serverului în aplicația DSC, la *Settings → API access* |
| „Rate estimation is not enabled on the Dragon Star account. …” | DSC nu a activat tarifele pe contul firmei | Cereți activarea la DSC sau folosiți **Preț fix** |
| „Dragon Star request limit reached. Try again in … seconds.” | Prea multe cereri într-un interval scurt | Reîncercați după numărul de secunde indicat |
| „AWB-ul … este deja inclus într-un borderou Dragon Star (…) și nu mai poate fi șters prin API. Cereți anularea la Dragon Star, la comenzi@curierdragonstar.ro.” | Borderoul de seară a fost deja creat | Cereți anularea la DSC pe e-mail |
| „AWB-ul … a fost creat acum … minute, iar Dragon Star permite ștergerea doar în primele 30 minute. Cereți anularea la Dragon Star, la comenzi@curierdragonstar.ro.” | Fereastra de anulare a trecut | Cereți anularea la DSC pe e-mail |
| „Răspunsul Dragon Star s-a pierdut. Rezultatul de la curier este necunoscut.” | Conexiunea s-a întrerupt după trimiterea cererii (AWB, anulare, borderou) | Verificați în aplicația web DSC dacă operația s-a făcut, înainte de a reîncerca |
| „DSC server error. …” (fără traducere, API v1, conexiune eșuată) | Conexiunea la DSC a eșuat înainte de răspuns | Reîncercați mai târziu; verificați accesul la internet al serverului |
| „Eroare la serverul DSC. …” | DSC a răspuns cu o eroare de server sau conexiunea a eșuat | Reîncercați mai târziu; dacă persistă, contactați DSC |
| „Timp de așteptare depășit la conectarea la serverul DSC: …” (API vechi) | Serverul DSC nu a răspuns la timp | Reîncercați mai târziu |
| „DSC did not return a label for AWB …: …” | DSC a refuzat eticheta la **Tipărire AWB** | Verificați AWB-ul în aplicația DSC; reîncercați |
| Eroare tehnică la **Obține preț** sau la trimiterea la curier, pe API v1, fără mesaj DSC | **Referință** de pe adresa de ridicare (sau de pe fișa companiei) nu este număr, deci nu poate fi cod de punct de lucru | Goliți referința companiei sau alegeți **Adresa de ridicare** importată la **Inițializare** |
| Mesajul DSC despre un câmp (adresă, localitate, telefon) | Date de livrare respinse de DSC | Corectați adresa în **Detalii transportator** (localitatea și județul așa cum le are DSC) |
| „Dragon Star: borderoul nu a putut fi creat, deci comanda de ridicare nu a fost trimisă. Eroare: …” (în istoricul livrării) | Eroare DSC la crearea borderoului de seară | Rulați din nou acțiunea planificată sau creați borderoul în aplicația DSC |
| „Dragon Star: comanda de ridicare nu a putut fi creată. Eroare: …” (în istoricul livrării) | DSC a refuzat comanda de ridicare | Corectați cauza; expedierea e reluată la rularea următoare |

## 10. Capturi de ecran

Capturile **nu sunt încă generate**: trebuie rulat skill-ul `fisa-screenshots`, care le va genera automat din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în limba română, pe o companie RO, cu apelurile către Dragon Star simulate (fără cont real). Numele planificate, în ordinea pașilor din secțiunea 6 (folderul `static/description/`):

1. `01_configurare_dsc.png` — metoda de livrare Dragon Star, fila **Configurare DSC**.
2. `02_locatii_ridicare.png` — fila **Locație de ridicare** după **Inițializare**.
3. `03_comanda_tarif_dsc.png` — comanda de vânzare cu linia de transport și tariful DSC.
4. `04_detalii_expediere.png` — fereastra **Detalii metodă de livrare**, cu suma de încasat și opțiunile.
5. `05_livrare_awb_emis.png` — livrarea cu AWB, butoanele **Tipărire AWB** și **Anulează AWB**.
6. `06_eticheta_awb.png` — eticheta AWB în PDF.
7. `07_anulare_refuzata.png` — mesajul de anulare refuzată după fereastra de 30 de minute.
8. `08_actiune_borderou.png` — acțiunea planificată de borderou și ridicare.
9. `09_istoric_livrare.png` — fila **Istoric** cu evenimentele DSC.

Comanda de regenerare, după ce testul există (baza trebuie să aibă limba română încărcată):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_delivery_dsc,l10n_ro,l10n_ro_doc_screenshots \
    --load-language=ro_RO --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Păstrați trei idei. Întâi, **cheia API și IP-ul serverului** sunt condiția de pornire: DSC nu are server de test, iar refuzurile de la început vin aproape mereu din cheie sau din IP-ul neînscris. Apoi, **anularea are o fereastră scurtă**: 30 de minute de la emitere și numai până la borderoul de seară; după aceea anularea se cere pe e-mail la Dragon Star, iar Odoo spune exact de ce refuză. În al treilea rând, **borderoul și comanda de ridicare se fac singure, seara, la 18:00 UTC (20:00 sau 21:00 ora României)**, nu la fiecare AWB: operatorul nu are nimic de comandat, dar trebuie să verifice istoricul livrărilor dacă DSC refuză borderoul. Explicați și diferența dintre o eroare (se corectează și se reîncearcă) și un „rezultat incert” (se verifică întâi în aplicația DSC, ca să nu iasă două AWB-uri pentru același colet).
