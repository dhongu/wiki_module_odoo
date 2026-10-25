# Fișă Modul: Conector marketplace Doraly (ylarod.ro)

**Modul:** `deltatech_marketplace_doraly`
**Utilizator principal:** Operator marketplace / administrator vânzări online
**Prioritate:** 🟡 Medie (conector în uz activ, dar cu limitări cunoscute — vezi secțiunea 8)

---

## 1. Scop business

Modulul conectează Odoo la platforma de marketplace **Doraly** (ylarod.ro), prin API-ul
`/api/vendors`. Este un conector „subțire" peste framework-ul generic
`deltatech_marketplace`: adaugă furnizorul „Doraly" în lista de backend-uri, autentificarea
proprie (email/parolă → token Bearer) și maparea câmpurilor specifice Doraly pentru import
produse, import categorii, import comenzi și trimiterea facturii PDF către marketplace.
Este util pentru un comerciant care vinde pe Doraly și vrea comenzile, clienții și produsele
sincronizate automat în Odoo, fără introducere manuală.

## 2. Bază legală și context

Nu există bază legală specifică — este o integrare tehnică comercială (API marketplace),
nu un flux fiscal. Contextul operațional: comenzile importate din Doraly devin comenzi de
vânzare Odoo normale, facturate și raportate ca orice altă vânzare a companiei (TVA, RO
e-Factura etc. se aplică prin modulele de contabilitate/localizare instalate separat, nu prin
acest conector).

> Conform `readme/ROADMAP.md` din modul, conectorul are mai multe **defecte de corectitudine
> confirmate în cod** (import categorii cu date fictive, brand fix la export produse, marcaj
> retryable pierdut la erori temporare de rețea etc.) — vezi secțiunea 8. Consultantul trebuie
> să cunoască aceste limitări înainte de a promite clientului un flux „complet automat".

## 3. Utilizatori și roluri

- Operator marketplace — configurează backend-ul, urmărește importurile de comenzi.
- Administrator vânzări — verifică maparea client/produs/categorie și corectitudinea comenzilor
  importate.

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul, configurează backend-ul Doraly și meniurile.
- Utilizator operațional: rulează importul de produse/categorii/comenzi și verifică rezultatul.
- Contabil/manager: validează factura trimisă către Doraly și comanda de vânzare rezultată.

## 4. Conturi și date implicate

Modulul nu generează el însuși note contabile — comenzile importate devin `sale.order`
Odoo standard, care urmează fluxul contabil obișnuit de facturare al companiei (conturile de
venituri, TVA colectată etc. se determină prin produsele/taxele configurate, nu prin acest
conector).

Date minime pentru demo:
- un backend de marketplace de tip **Doraly**, cu credențiale (email/parolă) valide pe
  `https://ylarod.ro/api/vendors` sau un mediu de test echivalent;
- o categorie de produse mapată (`marketplace.product.category`) sau o categorie implicită
  setată pe backend (`marketplace_category_id`), altfel exportul de produse eșuează;
- un transportator implicit (`Default Carrier`) setat pe backend, pentru linia de transport a
  comenzilor importate (Doraly nu transmite metoda de livrare, doar suma);
- cel puțin un produs cu `default_code` completat (Doraly identifică produsele după cod).

## 5. Configurare inițială

1. Instalați modulul `deltatech_marketplace_doraly` (instalează automat dependențele:
   `deltatech_marketplace`, `deltatech_marketplace_delivery`, `deltatech_marketplace_sale`,
   `deltatech_marketplace_sale_stage`, `deltatech_website_short_description`, `delivery`).
2. Deschideți **Marketplace → Backends** și creați un backend nou cu furnizorul **Doraly**.
   La selectarea furnizorului, câmpul „Adresă" se precompletează automat cu
   `https://ylarod.ro/api/vendors` (poate fi suprascris pentru un mediu de test).
3. Completați **Utilizator** (email) și **Parolă** cu credențialele contului de comerciant
   Doraly.
4. Setați **Transportator implicit** (`carrier_id`) — vizibil doar pe backend-urile Doraly —
   folosit pentru linia de transport a comenzilor importate.
5. Rulați acțiunea de test conexiune de pe backend, pentru a confirma autentificarea
   (`doraly_test_connection`).
6. Mapați cel puțin o categorie de produse Odoo pe o categorie Doraly (sau setați o categorie
   implicită pe backend), altfel exportul de produse va da eroare de mapare lipsă.

## 6. Flux de utilizare

### Pasul 1 — Configurarea backend-ului Doraly

Accesați **Marketplace → Backends**, creați/deschideți un backend cu furnizorul **Doraly** și
completați adresa API, email-ul, parola și transportatorul implicit.

![Formularul backend-ului Doraly, cu furnizorul selectat și transportatorul implicit](screenshots/01_backend_doraly.png)

### Pasul 2 — Import categorii de produse

Din backend, rulați acțiunea de import categorii. Modulul apelează `/categories` și creează
înregistrări `marketplace.product.category`, cu caracteristicile aferente.

> Atenție consultant: la data acestei fișe, metoda de import categorii **ignoră răspunsul real
> al API-ului** și creează mereu aceeași categorie de test („Termometre") — defect cunoscut,
> documentat în `readme/ROADMAP.md` (punctul P0.1). Nu folosiți acest pas ca dovadă a
> maparii reale de categorii până la corectare.

![Lista categoriilor de marketplace importate din Doraly](screenshots/02_import_categorii.png)

### Pasul 3 — Import produse

Rulați importul de produse (`/products`, GET). Fiecare produs Doraly devine o legătură
`marketplace.product`, cu codul intern (`productCode`), codul Doraly (`doralyCode`) și numele.

![Lista produselor de marketplace legate la produsele Odoo](screenshots/03_import_produse.png)

### Pasul 4 — Import comenzi

Rulați importul de comenzi (`/orders`, GET). Pentru fiecare comandă, modulul creează/actualizează:
clientul (după telefon sau email), adresa de livrare, adresa de facturare (cu CIF, dacă există),
comanda de vânzare (`marketplace.sale.order`) cu stadiul mapat din statusul Doraly, linia de
transport (pe transportatorul implicit al backend-ului) și liniile de produs.

![Comanda de vânzare importată din Doraly, cu client, adresă de livrare și linii de produs](screenshots/04_comanda_importata.png)

### Pasul 5 — Trimiterea facturii către Doraly

La postarea facturii comenzii marketplace, metoda `doraly_after_invoice_post` trimite către
Doraly URL-ul portalului facturii (PDF), pentru fiecare factură în stare „Postată" a comenzii.

![Factura postată, cu apelul de trimitere către Doraly în jurnalul tehnic](screenshots/05_trimitere_factura.png)

### Note de monografie și raportare

Acest modul **nu generează note contabile proprii** — comanda și factura rezultate urmează
monografia standard de vânzare a companiei (Dr 4111 = Cr 707 + Cr 4427, la postarea facturii),
determinată de produsele, taxele și jurnalele configurate în Odoo, nu de conector.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace` | framework generic de backend-uri, joburi asincrone, jurnal de sincronizare | dependență (manifest) |
| `deltatech_marketplace_delivery` | integrare transportatori de marketplace | dependență (manifest) |
| `deltatech_marketplace_sale` | comenzi de vânzare de marketplace (`marketplace.sale.order`) | dependență (manifest) |
| `deltatech_marketplace_sale_stage` | mapare stadii/status comandă | dependență (manifest) |
| `deltatech_website_short_description` | descrierea scurtă trimisă la exportul de produs | dependență (manifest) |
| `delivery` | transportator implicit + tip livrare „Doraly" pe `delivery.carrier` | dependență (manifest) |
| `queue_job` | reîncercare automată la erori temporare de rețea (HTTP 429/5xx) | dependență tehnică (framework marketplace) |

Ce este automat: autentificarea, importul de produse/categorii/comenzi, crearea clientului și
adreselor, trimiterea facturii PDF către Doraly după postare.
Ce rămâne manual: maparea categoriilor Doraly (până la corectarea defectului P0.1), maparea
brandului real la exportul de produse (în prezent brandul trimis este fix „Philips"), generarea
AWB-ului de curierat (integrarea de livrare este momentan un stub fără preț/etichetă reale) și
exportul de comenzi/stoc către Doraly (nu sunt implementate).

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori, cu toate dependențele.
- [ ] Backend-ul Doraly se salvează și testul de conexiune (login) reușește.
- [ ] Transportatorul implicit este setat pe backend înainte de primul import de comenzi.
- [ ] Importul de produse creează legăturile `marketplace.product` cu codul corect.
- [ ] Importul de comenzi creează comanda, clientul și adresele de livrare/facturare corect.
- [ ] Linia de transport apare pe comanda importată, cu suma din payload-ul Doraly.
- [ ] La postarea facturii, apelul către Doraly nu generează erori (verificați log-ul tehnic).
- [ ] Clientul a fost avertizat explicit că importul de categorii este momentan simulat
      (P0.1 din `ROADMAP.md`) și nu reflectă categoriile reale Doraly.
- [ ] Clientul a fost avertizat că brandul exportat pe produse este fix „Philips" (P0.5), dacă
      exportul de produse este folosit în producție.
- [ ] Nu s-a promis clientului generare AWB sau export de stoc/comenzi — nu sunt implementate.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| Eroare de autentificare la testul de conexiune | Email/parolă greșite sau adresă API incorectă | Verificați credențialele și câmpul „Adresă" pe backend |
| „No mapping for Doraly Category" | Produsul exportat nu are o categorie mapată și backend-ul nu are categorie implicită | Mapați categoria produsului la o `marketplace.product.category` sau setați `marketplace_category_id` pe backend |
| Importul de comenzi eșuează la crearea liniei de transport | Backend-ul nu are `carrier_id` (transportator implicit) setat | Setați „Transportator implicit" pe backend înainte de import |
| Job blocat definitiv la erori HTTP 429/5xx | Eroarea temporară de rețea nu este mereu reîncercată automat (limitare cunoscută, P0.3) | Reporniți manual jobul din **Marketplace → Configuration → Logs**, sau reîncercați importul |
| Produsele importate nu au descriere/preț | Importul Doraly mapează doar cod și nume produs; celelalte câmpuri nu sunt sincronizate din API | Completați manual sau prin alt flux datele lipsă (preț, descriere) |
| Toate categoriile importate ies identice („Termometre") | Defect cunoscut — importul de categorii ignoră răspunsul real al API-ului (P0.1) | Nu folosiți acest flux în producție până la corectarea în cod |

## 10. Capturi de ecran

Capturile pentru acest flux **nu există încă** în `readme/screenshots/` — modulul nu are un
`tests/test_screenshots.py` propriu. Lista de fișiere planificate, în ordinea pașilor din
secțiunea 6:

1. `01_backend_doraly.png` — formularul backend-ului Doraly (adresă, credențiale, transportator implicit).
2. `02_import_categorii.png` — lista categoriilor de marketplace importate.
3. `03_import_produse.png` — lista produselor de marketplace legate la produsele Odoo.
4. `04_comanda_importata.png` — comanda de vânzare importată din Doraly.
5. `05_trimitere_factura.png` — factura postată și confirmarea trimiterii către Doraly.

Recomandare: rulați skill-ul `fisa-screenshots` pentru a genera aceste capturi (test Playwright
dedicat, Preview MCP sau pluginul Chrome), apoi actualizați această secțiune și pașii din
secțiunea 6 cu fișierele reale.

## 11. Observații pentru manual

În manualul final, precizați clar că acest conector este **funcțional pentru fluxul de bază**
(autentificare, import produse/comenzi, trimitere factură), dar are **limitări cunoscute și
documentate** (import categorii simulat, brand fix la export, livrare nefuncțională, fără
export de stoc/comenzi) — listate integral în `readme/ROADMAP.md` al modulului. Redactorul
manualului trebuie să evite formulări care promit un flux „complet automat" până la corectarea
acestor puncte.
