# Fișă Modul: Expediere cu TNT Express — tarif, consignație și etichetă

**Modul:** `deltatech_delivery_tnt`
**Utilizator principal:** Operator expediții / depozit (emite și tipărește consignațiile), Administrator Inventar (configurează curierul)
**Prioritate:** 🟢 Scăzută (necesar doar firmelor care expediază cu TNT, în țară sau internațional)

---

## 1. Scop business

TNT Express (parte a grupului FedEx) primește expedierile prin ExpressConnect. Fără modul, fiecare consignație se introduce de mână în portalul TNT. Modulul face legătura din Odoo:

- **tariful** transportului se cere de la TNT pe comanda de vânzare, după greutatea, dimensiunile și serviciul expedierii; dintre variantele întoarse de TNT se alege automat cea potrivită (standard sau cu ramburs) sau se folosește un preț fix;
- **consignația** (AWB-ul TNT) se creează din livrare, iar numărul ei se scrie ca referință de urmărire;
- **eticheta** se generează din datele TNT, în PDF, HTML sau ZPL, și se atașează livrării;
- expedierile **interne și internaționale** sunt tratate la fel: linia de business TNT (intern sau internațional) se alege după țara expeditorului și a destinatarului, iar telefoanele se despart în prefix și număr, cum cere TNT;
- un răspuns pierdut la crearea consignației este raportat ca „rezultat incert”, ca o nouă apăsare să nu creeze a doua consignație.

TNT ExpressConnect **nu permite anularea** unei consignații, iar modulul **nu citește starea** expedierii: anularea și urmărirea se fac în portalul TNT. Nu sunt acoperite nici localitățile, județele, lockerele, punctele de ridicare, livrarea sâmbăta, deschiderea coletului, documentele vamale sau instrucțiunile speciale de livrare.

## 2. Bază legală și context

Nu are bază legală fiscală proprie: este un conector operațional cu un curier. Contextul relevant:

- Consignația TNT este documentul de transport al curierului; nu înlocuiește factura sau avizul care însoțesc marfa și nu este document contabil.
- Pentru expedierile în afara Uniunii Europene, documentele vamale **nu** se transmit prin modul: se pregătesc separat, după cerințele TNT.
- Odată creată, consignația rămâne la TNT: numărul ei se salvează pe livrare chiar dacă eticheta nu poate fi descărcată, iar anularea se cere în portalul TNT.
- **Adresele serviciilor TNT sunt fixe, pe producție**, iar consignația nu se poate anula prin API: orice consignație creată la încercări este reală. Testați doar cu acordul TNT.
- **Date personale trimise curierului:** la fiecare cerere de tarif și expediere, Odoo trimite la TNT numărul de cont, numele, adresa, localitatea, codul poștal, țara, persoana de contact și telefonul expeditorului și ale destinatarului, coletele (număr, greutate, dimensiuni, volum), valoarea declarată, rambursul și referința comenzii.

## 3. Utilizatori și roluri

- **Administrator Inventar** configurează metoda de livrare (**Inventar → Configurare → Livrare → Metode de expediere**). **Utilizator** și **Parolă** sunt vizibile doar utilizatorilor cu drept de **Administrare / Setări**.
- **Operatorul de vânzări** alege metoda de livrare pe comandă și obține tariful.
- **Operatorul de depozit / expediții** completează detaliile expedierii, validează livrarea și tipărește eticheta.

Roluri recomandate pentru testare:
- Administrator (Setări + Inventar): configurează metoda.
- Utilizator Vânzări + Inventar: parcurge fluxul din secțiunea 6 de la Pasul 2 încolo (comanda, apoi livrarea).
- Utilizator Inventar fără drept de Setări: verifică faptul că nu vede utilizatorul și parola ExpressConnect.

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile: modulul nu creează note contabile (vezi „Note de monografie și raportare” din secțiunea 6).

Date minime pentru demo:
- un cont TNT ExpressConnect (utilizator, parolă) și numărul de cont TNT;
- compania cu adresă completă și **telefon valid** (TNT cere prefixul și numărul);
- un produs de livrare de tip serviciu;
- un produs stocabil cu greutate și stoc disponibil;
- doi clienți cu telefon valid: unul din România (expediere internă) și unul din altă țară (expediere internațională);
- o comandă de vânzare creată din backend, fără plată înregistrată, ca livrarea să aibă ramburs (totalul comenzii), și una cu plată prin transfer bancar, fără ramburs.

## 5. Configurare inițială

1. Instalați `deltatech_delivery_tnt` (aduce `deltatech_delivery`). Serviciile TNT (Express 09/10/12/15 pentru documente și colete, **48N Economy Express**, **12 Economy Express**) se încarcă la instalare.
2. **Inventar → Configurare → Livrare → Metode de expediere** → **Nou**: **Furnizor** = *TNT*, produsul de livrare de tip serviciu.
3. În fila **Configurare TNT**: **Utilizator** și **Parolă** ExpressConnect (obligatorii), **Cont TNT**, **Tip etichetă TNT** (pdf, html sau ZPL) și **Serviciu**. **Atenție:** în această filă **Parola** se vede în clar, nu mascată; formularul trebuie deschis doar de cine are voie să vadă accesul TNT.
   Modulul trimite toate expedierile ca **non-document** (colete): alegeți un serviciu „nondoc” sau Economy Express, nu o variantă „doc”.
4. Tot acolo, **Plată ramburs**: metodele de plată la livrare ale căror tranzacții primesc numărul consignației. **Preț adițional pentru ramburs** nu apare în formularul metodei TNT, deci momentan nu se poate seta un supliment de ramburs pe tariful TNT.
5. Opțional, preț fix: **Preț fix** și pragul din rândul „dacă prețul calculat este mai mic decât”. Doar cu **Preț fix** completat (fără prag), TNT nu mai este întrebat de tarif.
6. Dacă livrați colete cu dimensiuni, bifați **Folosește dimensiunile coletului**; dacă TNT facturează în altă monedă decât comenzile, completați **Monedă curier** (tariful se convertește în moneda comenzii).

## 6. Flux de utilizare

### Pasul 1 — Configurarea metodei de livrare TNT

Din **Inventar → Configurare → Livrare → Metode de expediere**, deschideți metoda TNT și completați fila **Configurare TNT**.

![Formularul metodei de livrare TNT, fila Configurare TNT: Utilizator completat, Parolă vizibilă în clar, Partener companie, Plată ramburs, Cont TNT, Tip etichetă TNT pdf și Serviciu 15 Express nondoc](screenshots/01_configurare_tnt.png)

**Găsește pe ecran.** Fila **Configurare TNT** apare doar când **Furnizor** este *TNT*: accesul (**Utilizator**, **Parolă**), **Partener companie** (expeditorul), **Plată ramburs**, **Cont TNT**, **Tip etichetă TNT** și **Serviciu**.

**Verifică.** **Serviciu** este o variantă „nondoc” sau Economy Express: modulul declară mereu expedierea ca non-document, deci un serviciu „doc” nu se potrivește cu ce se trimite. **Cont TNT** este numărul de client din contractul TNT. Partenerul companiei are telefonul completat și valid. **Parola** apare în clar pe ecran (nu e mascată).

**Treci mai departe.** Salvați; metoda poate fi folosită pe comenzi.

### Pasul 2 — Tariful pe comanda de vânzare

Din **Vânzări → Comenzi → Comenzi**, pe comandă, **Adăugați transportul** → alegeți metoda TNT → **Obține preț** → **Adaugă**.

![Comanda de vânzare către un client din altă țară, cu linia de transport TNT și costul calculat de TNT fără TVA](screenshots/02_comanda_tarif_tnt.png)

**Găsește pe ecran.** Linia de transport cu produsul de livrare și prețul calculat de TNT.

**Verifică.** Prețul este tariful TNT fără TVA, în moneda comenzii: varianta standard la o comandă plătită online (card, transfer), varianta cu ramburs (opțiunea CO) la o comandă cu sumă de încasat, inclusiv o comandă creată din backend fără nicio plată. Cu **Preț fix** fără prag, apare prețul fix. Un telefon invalid la client sau la companie oprește calculul cu mesajul din secțiunea 9. Taxele liniei de transport urmează poziția fiscală a comenzii (de exemplu, la un client din altă țară UE cu cod de TVA valid).

**Treci mai departe.** Confirmați comanda: se creează livrarea de ieșire.

### Pasul 3 — Detaliile expedierii

Pe livrare (**Inventar → Operații → Livrări**, sau butonul **Livrare** de pe comandă), **Detalii transportator** deschide fereastra **Detalii metodă de livrare**.

![Fereastra Detalii metodă de livrare pentru TNT: adresa destinatarului cu țara și telefonul, Serviciu, Număr de colete, Greutate totală, dimensiunile coletului în centimetri, Valoare asigurată, Total comandă și Sumă de încasat](screenshots/03_detalii_expediere_tnt.png)

**Găsește pe ecran.** Adresa și telefonul destinatarului, **Serviciu**, **Număr de colete**, **Greutate totală**, **Dimensiune** (lungime × lățime × înălțime, în cm, doar cu **Folosește dimensiunile coletului**), **Valoare asigurată**, **Total comandă** și **Sumă de încasat**.

**Verifică.**
- **Sumă de încasat** se calculează din ultima plată a comenzii. Fără plată înregistrată sau cu plată la livrare, este totalul comenzii, inclusiv transportul. După facturare devine restul de plată de pe facturile postate, deci avansul sau voucherul nu se mai cer o dată. Cu orice altă plată (card, transfer bancar), suma este 0, chiar dacă banii nu au intrat încă. Lista **Plată ramburs** de pe metoda de livrare nu decide rambursul: adaugă **Preț adițional pentru ramburs** la tarif și stabilește ce tranzacții primesc numărul AWB. Dacă suma propusă nu e corectă (de exemplu, comanda e plătită prin OP înainte de facturare), bifați **Sumă de încasat stabilită manual** și corectați-o. La TNT, **Preț adițional pentru ramburs** nu apare pe formular, deci lista influențează doar numărul consignației scris pe tranzacții. O comandă din backend fără plată primește deci ramburs, iar tariful este cel al variantei cu ramburs (CO); dacă clientul plătește altfel, bifați **Sumă de încasat stabilită manual** și puneți 0.
- **Referința adresei de ridicare** nu se trimite la TNT: expeditorul este adresa de ridicare (nume, adresă, persoană de contact, telefon), alături de **Cont TNT**.
- Telefonul destinatarului are prefixul țării sau aparține țării din adresă (altfel TNT nu îl poate despărți în prefix și număr).
- Dimensiunile sunt în centimetri. Volumul calculat din ele se trimite doar la cererea de tarif. La crearea consignației, volumul total pleacă fix 0,1 m³ și numărul total de articole fix 1, indiferent de colete și dimensiuni (numărul de colete apare doar pe rândul de pachet). Verificați pe prima consignație, în portalul TNT, că datele coletelor sunt cele așteptate.

**Treci mai departe.** **Aplică** salvează detaliile; **Trimite la curier** creează direct consignația.

### Pasul 4 — Crearea consignației

Consignația se creează la validarea livrării sau cu **Trimite la curier** (antetul livrării, după aplicarea detaliilor).

![Livrarea validată cu numărul consignației TNT în Referință de urmărire și butonul Tipărire AWB în antet, fără butonul Anulează AWB](screenshots/04_livrare_awb_tnt.png)

**Găsește pe ecran.** **Referință de urmărire** (numărul consignației TNT), butonul **Tipărire AWB** și, în istoric, mesajul cu eticheta atașată.

**Verifică.**
- Butonul **Anulează AWB** nu apare: TNT nu permite anularea prin ExpressConnect. Pentru o consignație greșită, anularea se cere în portalul TNT.
- Nu există link de urmărire, iar **Reîmprospătează** din fila **Istoric** nu aduce evenimente de la TNT: starea se urmărește în portalul TNT.
- Dacă eticheta nu a putut fi descărcată, numărul consignației rămâne totuși pe livrare (nu se creează alta), iar eticheta se cere din nou cu **Tipărire AWB**.
- Dacă răspunsul TNT s-a pierdut pe drum, livrarea primește „rezultat incert”: verificați în portalul TNT dacă consignația există înainte de a retrimite.

**Treci mai departe.** Tipăriți eticheta (Pasul 5).

### Pasul 5 — Eticheta TNT

**Tipărire AWB** descarcă eticheta (fișierul `LabelTNT-<număr>.pdf`, `.html` sau `.zpl`, după **Tip etichetă TNT**). Dacă livrarea nu are încă eticheta, aceasta se cere din nou de la TNT.

![Eticheta TNT în format PDF, în macheta de rutare TNT: numărul consignației cu cod de bare, expeditorul, destinatarul, serviciul și numărul coletului](screenshots/05_eticheta_tnt.png)

**Găsește pe ecran.** Eticheta de rutare TNT, generată din datele trimise de TNT: numărul consignației, expeditorul, destinatarul, serviciul și coletul.

**Verifică.** Serviciul de pe etichetă este cel ales; la mai multe colete, eticheta acoperă fiecare colet al consignației.

**Treci mai departe.** Lipiți eticheta pe colet și predați coletul curierului.

### Note de monografie și raportare

Modulul **nu generează note contabile**. Legăturile reale cu partea financiară sunt:

- **costul transportului** se adaugă pe comanda de vânzare ca linie cu produsul de livrare al metodei (tarif TNT fără TVA, convertit în moneda comenzii, sau preț fix), cu taxele stabilite de poziția fiscală a comenzii, și se facturează clientului prin fluxul standard de vânzare;
- **rambursul** (Sumă de încasat) se trimite la TNT ca opțiune de ramburs a consignației; nu se înregistrează nimic în contabilitate la crearea consignației;
- decontarea rambursurilor și factura de transport a TNT se tratează în afara acestui modul.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_delivery` | detaliile expedierii, butoanele de pe livrare, păstrarea consignației la eșecul etichetei, „rezultat incert” | dependență (manifest) |
| `delivery` / `stock_delivery` (Odoo) | metoda de livrare, linia de transport pe comandă, trimiterea la validare | dependență (manifest) |
| `mail` | mesajele din istoricul livrării | dependență (manifest) |
| `deltatech_delivery_handover` | procesul-verbal de predare a coletelor la curier | extindere opțională |

**Ce e automat:** tariful pe comandă (cu alegerea variantei standard sau cu ramburs), linia de business internă sau internațională, despărțirea telefoanelor, crearea consignației la validare, generarea etichetei.
**Ce rămâne manual:** accesul ExpressConnect și numărul de cont, alegerea serviciului, corectarea detaliilor și a telefoanelor, anularea și urmărirea în portalul TNT, documentele vamale, verificarea rezultatelor incerte.

## 8. Verificări pentru consultant

- [ ] Fila **Configurare TNT** apare doar pentru furnizorul *TNT*; **Utilizator** și **Parolă** sunt obligatorii (parola se vede în clar).
- [ ] Testele creează consignații reale, care nu se pot anula din Odoo: doar cu acordul TNT.
- [ ] Un utilizator fără drept de Setări nu vede **Utilizator** și **Parolă**.
- [ ] **Obține preț** întoarce tariful TNT fără TVA, atât pentru un client din România, cât și pentru unul din altă țară.
- [ ] La o comandă cu ramburs, tariful este cel al variantei cu ramburs (diferit de cel al aceleiași comenzi plătite online).
- [ ] O comandă creată din backend, fără nicio plată înregistrată, are **Sumă de încasat** egală cu totalul comenzii (inclusiv transportul).
- [ ] O comandă cu o plată prin transfer bancar încă neîncasată are **Sumă de încasat** = 0.
- [ ] La validarea livrării se completează **Referință de urmărire**, eticheta este atașată, iar butonul **Anulează AWB** nu apare.
- [ ] Un client cu telefon invalid oprește tariful și expedierea cu mesajul „Număr invalid…”.
- [ ] Dacă eticheta lipsește de pe livrare, **Tipărire AWB** o cere din nou de la TNT.

## 9. Mesaje de eroare frecvente

Mesajele TNT despre consignație vin direct de la curier, în engleză, precedate de codul erorii.

| Mesaj | Cauză probabilă | Remediere |
|-------|-----------------|-----------|
| „Număr invalid: … (…)” | Telefonul clientului sau al companiei nu poate fi interpretat | Corectați telefonul (cu prefixul țării) pe partener sau în **Detalii transportator** |
| „Număr invalid sau neacceptat: …” | Telefonul nu este un număr valid pentru țara din adresă | Corectați telefonul |
| „Error …: …” / „<cod>: <descriere>” | TNT a respins consignația sau eticheta (date lipsă, serviciu indisponibil, cont greșit) | Citiți descrierea TNT și corectați datele sau serviciul |
| Mesajul TNT afișat la **Obține preț** | TNT nu poate calcula tariful pentru expedierea respectivă | Verificați adresa, greutatea, dimensiunile și serviciul |
| „Niciun CONNUMBER găsit în răspuns” | TNT a răspuns fără numărul consignației | Verificați în portalul TNT dacă s-a creat consignația, apoi reîncercați |
| „Răspunsul TNT s-a pierdut. Rezultatul de la curier este necunoscut.” | Conexiunea s-a întrerupt după trimiterea consignației | Verificați în portalul TNT înainte de a reîncerca |
| „Eroare la conectarea la serverul TNT: …” / „Timp de așteptare depășit la conectarea la serverul TNT: …” | Serverul TNT nu răspunde sau refuză autentificarea | Verificați utilizatorul și parola; reîncercați mai târziu |

## 10. Capturi de ecran

Capturile **nu sunt încă generate**: trebuie rulat skill-ul `fisa-screenshots`, care le va genera automat din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în limba română, pe o companie RO, cu apelurile către TNT simulate (fără cont real). Numele planificate, în ordinea pașilor din secțiunea 6 (folderul `static/description/`):

1. `01_configurare_tnt.png` — metoda de livrare TNT, fila **Configurare TNT**.
2. `02_comanda_tarif_tnt.png` — comanda de vânzare cu linia de transport și tariful TNT.
3. `03_detalii_expediere_tnt.png` — fereastra **Detalii metodă de livrare** pentru TNT.
4. `04_livrare_awb_tnt.png` — livrarea cu numărul consignației și butonul **Tipărire AWB**, fără **Anulează AWB**.
5. `05_eticheta_tnt.png` — eticheta TNT în PDF.

Comanda de regenerare, după ce testul există (baza trebuie să aibă limba română încărcată):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_delivery_tnt,l10n_ro,l10n_ro_doc_screenshots \
    --load-language=ro_RO --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Păstrați trei idei. Întâi, **modulul face un singur lucru la TNT: creează consignația și îi aduce eticheta**; anularea și urmărirea se fac în portalul TNT, iar operatorul trebuie să știe asta înainte să caute butonul **Anulează AWB**. Apoi, **telefoanele trebuie să fie valide**: TNT cere prefixul și numărul separat, iar un telefon greșit la client sau la companie oprește și tariful, și expedierea. În al treilea rând, **tariful depinde de ramburs**: aceeași comandă are alt preț de transport cu plată la livrare decât cu plată online. Explicați și diferența dintre o eroare (se corectează și se reîncearcă) și un „rezultat incert” (se verifică întâi în portalul TNT, ca să nu iasă două consignații pentru același colet).
