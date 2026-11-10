# Fișă Modul: Conector Marketplace Odoo-la-Odoo

**Modul:** `deltatech_marketplace_odoo`
**Utilizator principal:** Administrator marketplace / Operator sincronizare produse și comenzi
**Prioritate:** 🟡 Medie (folosit doar de clienții care conectează două instanțe Odoo, nu la orice implementare)

---

## 1. Scop business

Modulul adaugă furnizorul **„Odoo"** în cadrul framework-ului `deltatech_marketplace`, permițând
conectarea a două instanțe Odoo (de exemplu instanța unui distribuitor/producător și instanța unui
partener/retailer) prin XML-RPC, ca și cum instanța la distanță ar fi un marketplace obișnuit.
Cu acest conector se pot **importa** din instanța la distanță produse, categorii, atribute, clienți,
liste de preț, țări/județe și imagini, și se pot **exporta** comenzi (comandă de vânzare devine
comandă de achiziție în cealaltă instanță, sau invers, în funcție de tipul de integrare). Este util
pentru companii cu mai multe firme/instanțe Odoo separate (de exemplu Moldova/România, sau
distribuitor/franciză) care vor un flux automat de date fără EDI sau fișiere de schimb.

## 2. Bază legală și context

Nu există temei legal specific — modulul este un conector tehnic. Contextul este operațional:
sincronizare de date comerciale (produse, prețuri, stocuri, comenzi) între două baze de date Odoo,
folosind API-ul XML-RPC standard al Odoo (`/xmlrpc/2/object`, `/xmlrpc/2/common`).

## 3. Utilizatori și roluri

Administrator marketplace (configurează backend-ul, credențialele de conectare), Operator
sincronizare (rulează import/export, monitorizează jurnalul de erori).

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul, configurează backend-ul „Odoo" și verifică meniurile
- Utilizator operațional: rulează sincronizările (import produse/clienți, export comenzi)
- Contabil/manager: validează faptul că prețurile, stocurile și comenzile ajung corect în cealaltă instanță

## 4. Conturi și date implicate

Modulul nu generează note contabile — este un conector de date, nu un document fiscal. Ce este
implicat:
- **date de conectare**: URL instanță, bază de date, utilizator, parolă (câmpuri moștenite din
  `marketplace.backend`) + câmpurile specifice `odoo_database`, `odoo_version`;
- **legături cu parteneri**: `odoo_supplier_id` (furnizorul, pentru integrare B2B unde comanda de
  vânzare a partenerului devine comandă de achiziție la noi) și `odoo_customer_id`;
- pentru integrarea B2B (`odoo_integration_b2b`) se folosesc și `odoo_id_partner` / `odoo_id_pricelist`
  — utilizatorul/lista de preț din instanța la distanță, citite automat la inițializare.

Date minime pentru demo: două instanțe Odoo accesibile (poate fi și aceeași bază, cu un al doilea
utilizator), un utilizator API valid pe instanța la distanță, câteva produse/parteneri de test acolo.

## 5. Configurare inițială

1. Instalați modulul `deltatech_marketplace_odoo` (instalează automat și dependențele:
   `deltatech_marketplace`, `deltatech_marketplace_website`, `deltatech_marketplace_sale`,
   `deltatech_marketplace_purchase`, `deltatech_marketplace_payment`).
2. Creați un backend nou în **Marketplace → Backends** și alegeți furnizorul **Odoo**.
3. Completați URL-ul instanței la distanță (câmpul `location`), numele bazei de date
   (`odoo_database`), utilizatorul și parola de conectare, versiunea Odoo a instanței la distanță
   (`odoo_version`).
4. Dacă integrarea este de tip B2B (comenzile clientului devin comenzi de vânzare pe instanța la
   distanță), bifați `odoo_integration_b2b` și completați `odoo_supplier_id`/`odoo_customer_id`.
5. Testați conexiunea (buton de test conexiune al backend-ului) — verifică credențialele prin login
   XML-RPC.
6. Configurați tipurile de articole de sincronizat (categorii, produse, clienți, comenzi) în tab-ul
   de articole al backend-ului, cu domeniile și câmpurile suplimentare dorite.

## 6. Flux de utilizare

### Pasul 1 — Configurarea backend-ului Odoo

Accesați **Marketplace → Backends**, creați o înregistrare cu furnizorul **Odoo** și completați
câmpurile adăugate de acest modul: bază de date, versiune Odoo, integrare B2B, furnizor/client
asociat. Aceste câmpuri apar în formularul standard de backend, în grupul „Provider details".

> Notă: fișa nu conține capturi de ecran deoarece acestea nu au fost încă generate — vezi
> secțiunea 10.

### Pasul 2 — Import date de bază (categorii, atribute, țări/județe, clienți)

Din backend rulați acțiunile de import pentru categorii de produs, atribute cu valori, țări/județe
și clienți. Fiecare tip de articol își creează automat, la nevoie, legăturile lipsă (de exemplu la
importul unui client cu partener-părinte, părintele este importat automat dacă lipsește).

### Pasul 3 — Import produse (șabloane + variante) și imagini

Rulați importul de șabloane de produs (`product.template`) — acesta importă automat categoria,
atributele/valorile și, pentru fiecare variantă, articolul corespunzător. Dacă integrarea este B2B,
se creează automat și un furnizor (`seller_ids`) cu prețul din instanța la distanță. Imaginile de
produs pot fi importate separat, legate de șablonul deja importat.

### Pasul 4 — Import listă de prețuri

Importul unei liste de preț (`product.pricelist`) aduce și liniile acesteia (`product.pricelist.item`),
rezolvând automat legăturile către produs/șablon/categorie sau altă listă de bază; liniile pentru
produse inactive în instanța locală sunt sărite.

### Pasul 5 — Export comenzi (flux B2B)

Când o comandă de achiziție locală este confirmată (`purchase.order.button_confirm`) și furnizorul
ei corespunde cu `odoo_supplier_id` al unui backend Odoo B2B, modulul creează automat, prin job
asincron, o comandă de vânzare în instanța la distanță (`sale.order` creat prin `create_api`),
cu liniile de produs mapate prin codul extern. Dacă produsul nu are încă legătură cu instanța la
distanță, este căutat și importat automat după cod (`default_code`) înainte de a fi folosit pe linia
comenzii. Similar, o comandă de vânzare locală confirmată (`sale.order.button_confirm`), pentru
partenerul-furnizor configurat, este exportată ca și comandă către backend.

### Pasul 6 — Sincronizarea mesajelor și a stării comenzii

Mesajele postate în chatter-ul comenzii (note, atașamente) sunt propagate către comanda
corespunzătoare din instanța la distanță prin joburi asincrone. Modificările de stare relevante
(`state`) sunt de asemenea trimise către cealaltă instanță prin metodele API expuse
(`write_api`/`message_post_api`), astfel încât ambele părți văd statusul actualizat al comenzii.

### Note de monografie și raportare

Modulul nu generează note contabile proprii — comenzile de vânzare/achiziție create în cealaltă
instanță urmează propria lor contabilizare, conform localizării fiecărei instanțe Odoo.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace` | framework de bază: modele `marketplace.backend`, `marketplace.product`, joburi, jurnal de sincronizare | dependență (manifest) |
| `deltatech_marketplace_website` | integrare cu categoriile publice / website pentru produsele importate | dependență (manifest) |
| `deltatech_marketplace_sale` | modelul `marketplace.sale.order`, extins de acest conector | dependență (manifest) |
| `deltatech_marketplace_purchase` | modelul `marketplace.purchase.order`, extins de acest conector | dependență (manifest) |
| `deltatech_marketplace_payment` | metode de plată marketplace, folosite la exportul comenzilor | dependență (manifest) |
| `queue_job` | execuția asincronă a importurilor/exporturilor (`with_delay`) | dependență indirectă (prin `deltatech_marketplace`) |
| `sale` / `purchase` | comenzile locale ale căror confirmări declanșează exportul către instanța la distanță | integrare prin hook pe `button_confirm` |

Ce este automat: importul cu rezolvarea automată a legăturilor lipsă (categorie, atribute, părinte),
exportul comenzilor la confirmare, sincronizarea mesajelor și a stării comenzii.
Ce rămâne manual: configurarea inițială a backend-ului (credențiale, tip integrare, furnizor/client
asociat), alegerea articolelor de sincronizat și verificarea periodică a jurnalului de erori
(`Marketplace → Logs`).

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori pe baza demo (împreună cu dependențele marketplace).
- [ ] Testul de conexiune al backend-ului „Odoo" reușește cu credențialele configurate.
- [ ] Importul de categorii/atribute/produse aduce datele așteptate din instanța la distanță.
- [ ] La confirmarea unei comenzi de achiziție/vânzare cu partenerul configurat ca
      furnizor/client marketplace, apare automat un job de export în coadă (`Marketplace → Crons`
      / jobul `queue_job`).
- [ ] Jurnalul marketplace (`Marketplace → Logs`) nu conține erori nerezolvate după rularea
      fluxului complet.
- [ ] Mesajele postate pe comandă apar și în instanța la distanță (flux B2B).

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Wrong credentials" | Utilizator/parolă/bază de date greșite pentru instanța la distanță | Verificați `location`, `odoo_database`, utilizatorul și parola pe backend |
| „Marketplace X login: …" | Autentificare XML-RPC eșuată (parolă schimbată, cont blocat) | Reintroduceți parola pe backend — la schimbare, conexiunea salvată (`odoo_id_connection`) este resetată automat |
| „Marketplace X error at call model.method: …" | Metoda apelată nu există sau nu are drepturi pe instanța la distanță (versiune API diferită) | Verificați versiunea Odoo a instanței la distanță (`odoo_version`) și drepturile utilizatorului API |
| „Product … not found in …" | Produsul de pe linia comenzii exportate nu are cod (`default_code`) recunoscut în instanța la distanță | Verificați că produsul are cod și există (sau poate fi creat) pe cealaltă instanță |
| Eroare de conexiune / timeout (job reîncercat automat) | Instanța la distanță este indisponibilă temporar sau rețeaua e instabilă | Așteptați reîncercarea automată a jobului (`queue_job`); verificați accesibilitatea URL-ului |

## 10. Capturi de ecran

Fișa nu are încă generate capturi de ecran — folderul `readme/screenshots/` nu există pentru acest
modul. Recomand rularea skill-ului `fisa-screenshots` pentru a genera capturile pașilor de mai sus
(configurare backend, import produse/liste de preț, jurnal de sincronizare, comandă exportată),
numite în ordine `01_...` … `06_...`, corespunzător pașilor din secțiunea 6.

## 11. Observații pentru manual

În manualul final, păstrați explicația orientată pe activitatea utilizatorului: modulul conectează
două instanțe Odoo ca și cum a doua ar fi un marketplace, cu import de date de referință/produse și
export automat de comenzi la confirmare. Evidențiați faptul că nu produce note contabile proprii —
contabilizarea comenzilor create rămâne responsabilitatea fiecărei instanțe Odoo în parte.
