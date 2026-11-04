# Fișă Modul: AWB emis în afara Odoo — atașarea etichetei primite de la client sau de la alt sistem

**Modul:** `deltatech_delivery_relay`
**Utilizator principal:** Operator vânzări / expediții (primește eticheta AWB și o leagă de comandă și de livrare)
**Prioritate:** 🟢 Scăzută (folosit doar când AWB-ul nu se emite din Odoo, ci vine gata făcut)

---

## 1. Scop business

Uneori AWB-ul nu îl emite firma: clientul își trimite propriul curier și vine cu eticheta lui, sau comanda vine dintr-un sistem extern (de exemplu un marketplace) care a generat deja AWB-ul. Depozitul are nevoie de etichetă lângă livrare, ca să o tipărească și să o lipească pe colet, fără să o caute prin e-mailuri sau portaluri.

Modulul adaugă un tip de metodă de livrare care **nu apelează niciun curier**. Eticheta AWB (fișier PDF) se atașează comenzii de vânzare:
- direct, la alegerea metodei de livrare pe comandă;
- automat, dintr-un fișier `awb_…` primit pe comandă (răspunsul clientului la e-mail sau un atașament pus în istoricul comenzii);
- pe livrare, din **Detalii transportator**.

Eticheta trece apoi pe livrare, se tipărește cu **Tipărire AWB**, iar clientul o poate descărca din portal. La confirmarea unei comenzi fără etichetă, clientul primește automat un e-mail care îi cere fișierul AWB.

## 2. Bază legală și context

Modulul nu are bază legală fiscală proprie și nu creează documente fiscale. AWB-ul atașat este documentul de transport al curierului ales de client sau de sistemul extern; firma doar îl păstrează lângă livrare.

Context operațional:
- **Numele fișierului contează, în două feluri.** Un fișier atașat într-un **mesaj** pe comandă (răspunsul clientului sau un mesaj din istoric) este recunoscut doar dacă numele **începe** cu `awb_` (fără deosebire de majuscule). La **confirmarea comenzii** și la **deschiderea ferestrei Adăugați transportul**, Odoo caută însă printre atașamentele comenzii orice fișier al cărui nume **conține** `awb_` (de fapt „awb" urmat de orice caracter), deci și un fișier precum `factura_awb_2.pdf` poate fi preluat ca etichetă. Numărul AWB-ului se ia din nume: pentru `awb_1234567890.pdf`, numărul este `1234567890`.
- **Un fișier `awb_…` schimbă metoda de livrare a comenzii.** Dacă comanda are altă metodă de livrare (sau niciuna), Odoo pune pe ea metoda de acest tip și **înlocuiește linia de transport** cu una la preț 0: linia existentă se șterge, cu preț cu tot, iar totalul comenzii scade. Dacă transportul a fost deja facturat, operația se oprește cu o eroare (secțiunea 9).
- **Starea coletului nu vine de la un curier.** Odoo nu are de unde citi starea: o livrare validată, cu AWB, este considerată **Livrat** după 5 zile de la crearea ei.
- **Fără anulare din Odoo.** AWB-ul aparține curierului clientului sau sistemului extern; anularea se face acolo.

## 3. Utilizatori și roluri

Modulul nu are roluri proprii:
- **Inventar / Administrator** sau **Vânzări / Administrator** creează metoda de livrare;
- **Vânzări / Utilizator** alege metoda pe comandă, atașează eticheta și confirmă comanda;
- **Inventar / Utilizator** verifică eticheta pe livrare și o tipărește;
- **clientul**, ca utilizator de portal, descarcă eticheta din comenzile lui.

Roluri recomandate pentru testare: un utilizator de vânzări (pașii 2–4), un utilizator de inventar (pașii 5–6, 8) și un client cu acces la portal (Pasul 7).

## 4. Conturi și date implicate

Modulul **nu folosește conturi contabile** și nu creează note contabile.

Date minime pentru demo:
- o metodă de livrare cu **Furnizor** = **Livrare la punct de ridicare**, un produs de livrare de tip serviciu și, de regulă, **Preț fix** 0 (transportul îl plătește clientul la curierul lui);
- un client cu e-mail și acces la portal;
- un fișier PDF cu eticheta, numit de exemplu `awb_1234567890.pdf`;
- o comandă de vânzare cu un singur transfer de livrare;
- pentru verificarea efectului asupra totalului, o a doua comandă cu o altă metodă de livrare și transport cu preț.

## 5. Configurare inițială

1. Instalați `deltatech_delivery_relay` (aduce `deltatech_delivery`, `delivery` și `sale`).
2. **Inventar → Configurare → Livrare → Metode de livrare → Nou**: **Furnizor** = **Livrare la punct de ridicare**. Este traducerea românească a tipului „Relay Delivery"; numele nu are legătură cu punctele de ridicare: tipul înseamnă „AWB primit din afara Odoo".
3. **Livrare produs**: un produs de tip serviciu. **Preț fix**: costul transportului pe comandă (de obicei 0).
4. **Nivel de integrare**: lăsați valoarea implicită **Obține preț și creează livrare**; cu ea, livrarea primește numărul AWB scris de operator (Pasul 2). Cu **Obține preț**, livrarea primește ca număr AWB numărul comenzii.
5. Creați o singură metodă de acest tip: când un fișier `awb_…` sosește pe o comandă care are altă metodă de livrare, modulul pune pe comandă **prima** metodă de acest tip găsită. Căutarea se face fără filtru pe companie: într-o bază cu mai multe companii, metoda găsită poate fi a altei companii. Lăsați metoda fără companie (vizibilă tuturor) sau verificați comanda după preluare.
6. Verificați că e-mailurile de ieșire funcționează: cererea de AWB către client pleacă imediat, la confirmarea comenzii.

## 6. Flux de utilizare

### Pasul 1 — Metoda de livrare pentru AWB-uri primite

**Inventar → Configurare → Livrare → Metode de livrare**, metoda cu **Furnizor** = **Livrare la punct de ridicare**.

![Formularul metodei de livrare: Furnizor Livrare la punct de ridicare, Nivel de integrare Obține preț și creează livrare, produsul de livrare de tip serviciu și Preț fix 0, fără filă de configurare a unui curier](screenshots/01_metoda_livrare_relay.png)

Ce se întâmplă: metoda nu are cont, servicii sau credențiale; costul transportului pe comandă este prețul fix.

### Pasul 2 — Eticheta atașată la alegerea metodei pe comandă

Pe comanda de vânzare, **Adăugați transportul**, alegeți metoda de mai sus. În fereastră apar **Atașament etichetă** și **Referință de urmărire la transportator**: încărcați PDF-ul și scrieți numărul AWB-ului, apoi **Adaugă**.

![Fereastra Adăugați o metodă de expediere cu metoda Livrare la punct de ridicare: câmpul Atașament etichetă cu fișierul awb_1234567890.pdf încărcat și Referință de urmărire la transportator 1234567890](screenshots/02_adauga_transport_relay.png)

Ce se întâmplă: eticheta se salvează pe comandă. Dacă printre atașamentele comenzii există deja un fișier al cărui nume conține `awb_`, fereastra îl preia singură în **Atașament etichetă**, chiar la deschidere; dacă metoda de livrare a comenzii era alta, deschiderea ferestrei înlocuiește deja linia de transport (vezi secțiunea 2).

La confirmarea comenzii, eticheta trece pe livrare, iar livrarea primește AWB-ul și starea **Avizat**. Cu nivelul implicit **Obține preț și creează livrare**, **Referință de urmărire** pe livrare este referința scrisă în fereastră sau, dacă nu ați scris-o, **numele fișierului** încărcat, cu extensie cu tot (de exemplu `eticheta.pdf`). De aceea, completați întotdeauna **Referință de urmărire la transportator**. Cu nivelul **Obține preț**, livrarea primește ca număr AWB numărul comenzii.

### Pasul 3 — Comanda confirmată fără etichetă: cererea către client

Dacă metoda de livrare este de acest tip și comanda nu are etichetă, la **Confirmă** clientul primește pe e-mail mesajul „Răspundeți la acest e-mail cu un fișier awb al cărui nume începe cu awb_".

![Istoricul comenzii confirmate: mesajul trimis clientului „Răspundeți la acest e-mail cu un fișier awb al cărui nume începe cu awb_”, cu clientul ca destinatar](screenshots/03_cerere_awb_client.png)

Ce se întâmplă: mesajul pleacă imediat, ca e-mail către client. **Abia după trimitere**, Odoo caută pe comandă un fișier al cărui nume conține `awb_` și, dacă îl găsește, îl atașează: un fișier deja primit nu oprește deci e-mailul.

### Pasul 4 — AWB-ul primit pe comandă

Clientul răspunde la e-mail cu fișierul `awb_1234567890.pdf`, sau un utilizator atașează fișierul într-un mesaj din istoricul comenzii.

![Istoricul comenzii cu răspunsul clientului și atașamentul awb_1234567890.pdf; pe comandă, linia de transport cu metoda Livrare la punct de ridicare și totalul comenzii](screenshots/04_awb_primit_pe_comanda.png)

Ce se întâmplă, automat (doar dacă numele fișierului **începe** cu `awb_`):
- fișierul devine eticheta comenzii;
- dacă metoda de livrare a comenzii era alta (sau lipsea), comanda primește metoda de tip **Livrare la punct de ridicare**, iar linia de transport existentă se **șterge** și se înlocuiește cu una la preț 0; totalul comenzii scade cu valoarea transportului;
- numărul AWB se ia din numele fișierului (`1234567890`);
- dacă comanda are o singură livrare (sau o singură livrare încă nevalidată), eticheta și numărul AWB se scriu și pe livrare.

Verificați totalul comenzii după preluare: dacă transportul trebuia facturat clientului, adăugați-l din nou. Un fișier pus din greșeală cu un nume `awb_…` schimbă metoda de livrare și transportul comenzii.

### Pasul 5 — Eticheta pusă direct pe livrare

Pe o livrare fără AWB, **Detalii transportator** deschide fereastra **Detalii metodă de livrare**, cu aceleași câmpuri **Atașament etichetă** și **Referință de urmărire la transportator**.

![Fereastra Detalii metodă de livrare pentru metoda Livrare la punct de ridicare: Atașament etichetă cu eticheta preluată de pe comandă și Referință de urmărire la transportator](screenshots/05_detalii_transportator_relay.png)

**Găsește pe ecran.** **Atașament etichetă** (preluat de pe comandă, dacă există) și **Referință de urmărire la transportator**.

**Verifică.** Eticheta este cea a acestei comenzi (destinatarul de pe PDF este clientul livrării); referința este numărul AWB de pe etichetă.

**Treci mai departe.** **Aplică**: eticheta și numărul AWB se scriu pe livrare.

**Atenție la validarea fără etichetă.** Dacă apăsați **Validează** pe o livrare care nu are nici etichetă, nici AWB, Odoo „emite" totuși un AWB: **Referință de urmărire** devine numărul comenzii, **Stare livrare** devine **Avizat**, iar după 5 zile livrarea trece singură în **Livrat**, fără ca vreun colet să fi plecat cu o etichetă. Puneți eticheta înainte de validare.

### Pasul 6 — Livrarea cu AWB și tipărirea etichetei

Pe livrare, **Referință de urmărire** arată numărul AWB, iar **Tipărire AWB** descarcă eticheta.

![Livrarea cu Referință de urmărire completată, butonul Tipărire AWB în antet și eticheta AWB în panoul de previzualizare a atașamentelor](screenshots/06_livrare_cu_awb_relay.png)

Ce se întâmplă: **Tipărire AWB** apare doar pe o livrare cu AWB; dacă livrarea nu are încă etichetă, o preia de pe comandă. **Descărcare livrări** (din meniul de tipărire al listei de livrări) preia și ea eticheta de pe comandă, iar unei livrări fără număr AWB îi dă ca număr numărul comenzii. **Anulează AWB** nu apare: AWB-ul nu se anulează din Odoo.

### Pasul 7 — Eticheta în portalul clientului

Clientul intră în portal, la comenzile sau ofertele lui.

![Portalul clientului, lista comenzilor: coloana AWB cu pictograma de atașament pe comanda care are etichetă](screenshots/07_portal_comenzi_awb.png)

Ce se vede: în listele de oferte și comenzi, coloana **AWB** are linkul de descărcare a etichetei (**Descarcă** la oferte, pictograma de atașament la comenzi). Pe pagina comenzii apare „Are AWB: Da", cu linkul, sau „Are AWB: Nu".

### Pasul 8 — Lista AWB-urilor: găsește → verifică → acționează

**Inventar → Operații → AWB de livrare → Listă AWB de livrare**, filtrați după **Transportator** = metoda de tip **Livrare la punct de ridicare**.

![Lista AWB de livrare filtrată pe metoda Livrare la punct de ridicare: coloanele Număr, Dată, Comandă de vânzare și Stare livrare, cu AWB-urile vechi de peste 5 zile în starea Livrat](screenshots/08_lista_awb_relay.png)

**Găsește pe ecran.** **Număr** (AWB-ul, numele fișierului sau numărul comenzii), **Comandă de vânzare**, **Stare livrare**. Coloanele **Expeditor** și **Destinatar** rămân goale pentru aceste AWB-uri.

**Verifică.**
- Fiecare comandă expediată are AWB; un **Număr** egal cu numărul comenzii înseamnă o livrare validată fără etichetă (nota de la Pasul 5), nivelul **Obține preț** sau **Descărcare livrări** fără referință; un **Număr** cu extensie (`.pdf`) înseamnă o etichetă încărcată fără referință (Pasul 2).
- **Livrat** nu este o confirmare de la curier. Acțiunea programată „Livrare: actualizează starea livrării" îl pune pe livrările validate, cu AWB, create de mai mult de 5 zile (și de cel mult 30), care nu sunt în starea **Ciornă**; o livrare care a primit AWB-ul direct din fișierul `awb_…` poate rămâne în **Ciornă** și nu e atinsă de ea. În schimb, **Istoric → Reîmprospătează** pe livrare sau **Acțiuni → Preia istoricul AWB** în lista de livrări trec în **Livrat** **orice** livrare validată mai veche de 5 zile, indiferent de starea ei.

**Acționează.** **Vizualizare comandă** deschide comanda; pentru o etichetă greșită, puneți pe comandă fișierul `awb_…` corect (Pasul 4).

### Note de monografie și raportare

Modulul **nu generează note contabile** și nu calculează ramburs: nu trimite nimic unui curier.

Legăturile cu partea financiară:
- **linia de transport** de pe comanda de vânzare, la prețul fix al metodei (de obicei 0), facturată odată cu comanda prin fluxul standard. Atenție: preluarea unui fișier `awb_…` poate înlocui o linie de transport cu preț printr-una la 0 și scade totalul comenzii (Pasul 4);
- **curierul clientului**: transportul și eventualul ramburs se decontează între client și curierul lui; firma nu are nimic de decontat;
- **marketplace**: dacă marketplace-ul încasează de la cumpărător (inclusiv ramburs), suma este creanța firmei față de marketplace și se reconciliază la decontarea marketplace-ului, prin fluxul de încasări, nu de acest modul.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_delivery` | **Detalii transportator**, **Tipărire AWB**, **Descărcare livrări**, lista AWB, actualizarea periodică a stării | dependență (manifest) |
| `deltatech_delivery_status` | câmpul **Stare livrare** | dependență indirectă (prin `deltatech_delivery`) |
| `delivery`, `sale` | metoda de livrare, fereastra de alegere a transportului, linia de transport, portalul comenzilor | dependență (manifest) |
| `mail` | e-mailul către client și preluarea fișierelor `awb_…` din mesaje | dependență indirectă |
| module de marketplace | comenzile importate cu AWB-ul generat de marketplace | opțional |

Ce este automat: cererea de AWB pe e-mail la confirmare, recunoașterea fișierelor `awb_…`, schimbarea metodei de livrare și a liniei de transport pe comandă, copierea etichetei pe livrare, numărul AWB din numele fișierului, trecerea în **Livrat** după 5 zile.
Ce rămâne manual: obținerea etichetei de la client sau din sistemul extern, completarea referinței AWB, verificarea că eticheta e a comenzii corecte, verificarea totalului comenzii după preluare, tipărirea și lipirea etichetei, anularea AWB-ului la curier.

## 8. Verificări pentru consultant

- [ ] Metoda cu **Furnizor** = **Livrare la punct de ridicare** nu cere credențiale și pune pe comandă prețul fix.
- [ ] În **Adăugați o metodă de expediere**, **Atașament etichetă** și **Referință de urmărire la transportator** apar doar pentru metodele de acest tip.
- [ ] Etichetă încărcată în fereastră cu referința `1234567890`: după confirmare, livrarea are **Referință de urmărire** = `1234567890` și **Stare livrare** = **Avizat**.
- [ ] Etichetă încărcată fără referință: livrarea primește ca referință numele fișierului.
- [ ] La confirmarea unei comenzi fără etichetă, clientul primește e-mailul cu cererea fișierului `awb_…`.
- [ ] Un răspuns cu `awb_1234567890.pdf` pune eticheta pe comandă și pe livrare, cu **Referință de urmărire** = `1234567890`.
- [ ] Un fișier `awb_…` pus pe o comandă cu altă metodă de livrare și transport cu preț: metoda devine **Livrare la punct de ridicare**, linia de transport devine 0, iar **Total** al comenzii scade cu valoarea transportului.
- [ ] Același fișier pe o comandă cu transportul deja facturat: apare eroarea „Nu puteți actualiza costurile de livrare…", iar comanda rămâne neschimbată.
- [ ] Într-un mesaj, un fișier `eticheta.pdf` nu este preluat; un fișier `factura_awb_2.pdf` nu este preluat din mesaj, dar poate fi preluat la confirmare sau la deschiderea ferestrei de transport.
- [ ] **Validează** pe o livrare fără etichetă dă **Referință de urmărire** = numărul comenzii și **Stare livrare** = **Avizat**.
- [ ] **Tipărire AWB** descarcă eticheta de pe comandă; **Anulează AWB** nu apare.
- [ ] În portal, coloana **AWB** are link de descărcare pentru comenzile cu etichetă, iar pagina comenzii arată „Are AWB: Da".
- [ ] O livrare validată, cu AWB și starea **Avizat**, creată de peste 5 zile, trece în **Livrat** la următoarea rulare a acțiunii programate; **Preia istoricul AWB** trece în **Livrat** orice livrare validată mai veche de 5 zile.
- [ ] Într-o bază cu mai multe companii, metoda pusă automat pe comandă este a companiei comenzii (sau fără companie).

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Nu puteți actualiza costurile de livrare pentru o comandă unde acestea au fost deja facturate! …" | Pe o comandă cu transportul deja facturat a sosit un fișier `awb_…` sau s-a deschis **Adăugați transportul**, iar modulul a încercat să înlocuiască linia de transport | Puneți eticheta direct pe livrare, din **Detalii transportator** (Pasul 5) |
| Totalul comenzii a scăzut, transportul a devenit 0 | Un fișier `awb_…` a înlocuit linia de transport | Comportament actual al modulului; adăugați din nou transportul dacă trebuie facturat |
| Clientul a trimis eticheta, dar ea nu apare pe comandă | Numele fișierului din mesaj nu începe cu `awb_` | Redenumiți fișierul `awb_<număr AWB>.pdf` și atașați-l din nou în istoricul comenzii |
| A fost preluat ca etichetă un alt fișier al comenzii | La confirmare și la deschiderea ferestrei de transport se caută orice fișier care conține `awb_` în nume | Redenumiți fișierul greșit și încărcați eticheta corectă din **Detalii transportator** |
| Eticheta e pe comandă, dar nu și pe livrare | Comanda are mai multe livrări deschise | Pe livrarea corectă, **Detalii transportator** → **Atașament etichetă** → **Aplică** |
| **Referință de urmărire** = numărul comenzii | Livrare validată fără etichetă, nivel **Obține preț** sau **Descărcare livrări** pe o livrare fără AWB | Puneți pe comandă fișierul `awb_<număr>`; pentru o livrare deja cu AWB, corectați referința manual |
| **Referință de urmărire** = un nume de fișier (`….pdf`) | Etichetă încărcată fără **Referință de urmărire la transportator** | Corectați referința manual pe livrare |
| Livrarea apare **Livrat** fără să fi plecat cu etichetă | Validată fără etichetă (AWB = numărul comenzii), apoi trecută în **Livrat** după 5 zile | Puneți eticheta înainte de validare; corectați starea manual |
| Metoda de livrare a comenzii s-a schimbat singură | Pe comandă a sosit un fișier `awb_…` | Comportament voit; dacă nu era un AWB, reveniți la metoda inițială și redenumiți fișierul |
| Clientul nu primește cererea de AWB | Clientul nu are e-mail sau serverul de e-mail de ieșire nu funcționează | Completați e-mailul clientului; verificați e-mailurile de ieșire |
| „Nu există etichete de tipărit" | **Descărcare livrări** pe livrări fără etichetă și fără etichetă pe comandă | Obțineți întâi eticheta de la client |

## 10. Capturi de ecran

Capturile **nu sunt încă generate**. Numele de mai jos sunt planificate și corespund pașilor din secțiunea 6; ele trebuie generate cu skill-ul `fisa-screenshots`, automat, din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în limba română, pe o companie RO, cu un PDF de etichetă de test (`awb_1234567890.pdf`). Fișierele se scriu în `static/description/`.

1. `01_metoda_livrare_relay.png` — metoda de livrare de tip **Livrare la punct de ridicare**.
2. `02_adauga_transport_relay.png` — fereastra **Adăugați o metodă de expediere** cu eticheta încărcată și referința completată.
3. `03_cerere_awb_client.png` — istoricul comenzii cu e-mailul de cerere a AWB-ului.
4. `04_awb_primit_pe_comanda.png` — istoricul comenzii cu fișierul `awb_…` primit și totalul comenzii.
5. `05_detalii_transportator_relay.png` — fereastra **Detalii metodă de livrare** cu eticheta.
6. `06_livrare_cu_awb_relay.png` — livrarea cu AWB și eticheta în previzualizare.
7. `07_portal_comenzi_awb.png` — portalul clientului, lista comenzilor cu coloana **AWB**.
8. `08_lista_awb_relay.png` — **Listă AWB de livrare** filtrată pe această metodă.

Comanda de regenerare, după ce testul există (cere `l10n_ro` pentru compania RO și limba română încărcată):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_delivery_relay,l10n_ro,l10n_ro_doc_screenshots \
    --load-language=ro_RO --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Păstrați patru idei. Întâi, **tipul de metodă se numește în interfață „Livrare la punct de ridicare"**, dar înseamnă „AWB primit din afara Odoo": explicați asta de la început, ca să nu fie confundat cu lockerele. Apoi, **numele fișierului este cheia**: `awb_<număr>` face legătura automată cu comanda și dă numărul AWB-ului, dar **schimbă și metoda de livrare și linia de transport a comenzii**, cu efect asupra totalului; verificați totalul după fiecare preluare. În al treilea rând, **completați referința AWB** la încărcarea etichetei: altfel livrarea primește numele fișierului sau numărul comenzii. În al patrulea rând, **„Livrat" este o presupunere**, pusă după 5 zile, nu o confirmare a curierului, și apare și pe livrări validate fără etichetă. Spuneți clar și că la confirmarea unei comenzi fără etichetă clientul primește imediat un e-mail.
