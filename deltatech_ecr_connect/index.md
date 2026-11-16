# ECR Connect (shared) (localizat la `deltatech_ecr_connect/index.md`)

- **Nume Tehnic:** `deltatech_ecr_connect`
- **Versiune:** `19.0.1.3.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_ecr_connect
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ecr_connect`
- **Ultima Ingestie:** `2026-11-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă blocurile comune, de tip bibliotecă JavaScript, pentru trimiterea documentelor fiscale (bon fiscal, dispoziție de plată) către casele de marcat electronice (ECR — Electronic Cash Register), prin agentul local Terrabit Connect. Înainte de acest modul, cunoașterea formatelor de casă de marcat era duplicată — în JavaScript în `deltatech_pos` și în Python în `deltatech_sale_store` — iar orice corecție de protocol sau dispozitiv nou trebuia aplicată în două locuri. Acest modul centralizează logica astfel încât orice modul „producător" de documente fiscale (comandă POS, factură) să o poată reutiliza fără duplicare. Se instalează împreună cu modulele care îl folosesc și nu adaugă nimic în interfață de unul singur (nu are meniu; tipul casei de marcat, transportul și simularea se setează pe punctul de vânzare din `deltatech_pos_base`). Nu are cod Python, deci poate fi instalat și pe Odoo Online.

#### 2. Funcționalități Cheie

- **Document fiscal standardizat** (`ecr_document.esm.js`) — contract JSON neutru față de tipul casei de marcat (antet, linii, plăți, opțiuni), pe care modulele producătoare (comandă POS, factură) îl construiesc din propriile date, prin `emptyEcrDocument()`.
- **Convertor de format** (`ecr_format.esm.js`) — sursa unică de adevăr pentru șabloanele specifice fiecărui dispozitiv (Datecs/FiscalWire, FiscalNet, Incotex, Optima, Daisy, Succes); funcția `formatEcrDocument(doc, ecrType)` transformă documentul standardizat în conținutul specific casei de marcat.
- **Trimițător Terrabit Connect** (`ecr_connect.esm.js`) — funcția `sendEcrToConnect()` trimite conținutul către agentul local (`http://127.0.0.1:8765/print`), tratează rezultatul sincron, deschide dialogul de eroare (reîncercare / intervenție manuală / anulare) și, la agent inaccesibil, cade automat pe descărcarea fișierului (flote mixte de case de marcat continuă să funcționeze).
- **Mapare cote TVA post-reformă 2025** — cotele noi (21 %, 11 %) sunt mapate pe grupele fiscale ale cotelor vechi (19 %, 9 %), astfel încât programarea fiscală existentă a caselor de marcat rămâne validă, fără reprogramare; hărțile `cod_tva` nu mai conțin cotele vechi (19 %, 18 %, 9 %, 5 %).
- **Cod fiscal client pe antet** — `formatHeader()` tipărește CUI-ul clientului (`header.cui`) imediat după numele acestuia, pe toate dispozitivele; apariția e decisă de modulul apelant (ex. `print_cui` în `deltatech_pos`), în funcție de pragul facturii simplificate.
- **Corecție de vânzare cu cantitate negativă** — pe `datecs18`/`dxprint` (FiscalWire 2018), o linie cu preț unitar pozitiv și cantitate negativă (ex. casierul tastează „-2" pentru a corecta o vânzare fără ecranul de Refund) se tipărește acum cu numele produsului și cantitatea negativă, în loc să cadă pe linia anonimă „subtotal + discount valoric".
- **Linie de discount recunoscută după valoare totală** — `formatLine()` identifică o linie de discount la nivel de document după valoarea totală (`preț × cantitate`), nu doar după prețul unitar negativ, astfel încât liniile de discount introduse cu preț unitar pozitiv și cantitate negativă (convenția uzuală pe facturi, ex. `deltatech_sale_store`) nu mai sunt omise de pe bonul fiscal.
- **Dialog de eroare fiscală partajat** (`ecr_error_dialog.esm.js`) — componentă OWL (`FiscalErrorDialog`) reutilizată de toate fluxurile fiscale (POS și backend) pentru a prezenta operatorului mesajul de eroare venit de la casa de marcat; casierul poate alege **Reîncearcă** (același identificator de bon, fără dublă tipărire), **Descarcă și procesează manual** sau **Anulează** (vânzarea rămâne validată în Odoo). Textele dialogului sunt traduse.
- **Fallback pe fișier** — dacă agentul nu răspunde în 40 de secunde (timeout-ul acoperă și citirea răspunsului), fișierul de comenzi se descarcă, iar casele fără agent continuă să funcționeze.
- **Transport DxPrint** (`ecr_dxprint.esm.js`) — alternativă la Terrabit Connect: driverul DxPrint în mod embedded primește JSON pe API-ul local (implicit `http://127.0.0.1:8080`, autentificare Basic opțională) și răspunde imediat cu numărul bonului și al raportului Z. Documentul standard devine corpul `POST /receipts` (produse cu cota TVA sau *Cod ECR* al taxei, discount unitar/procentual, tipuri de plată din *Cod ECR* al metodei de plată, CUI client, comentarii, cod de bare); o linie cu total negativ devine discount valoric pe tot bonul; dispoziția de plată este o retragere de numerar (`/money/withdraw`), iar rapoartele X / Z și intrările/ieșirile de numerar au cereri proprii. Contractul de rezultat este același ca la `sendEcrToConnect()`; la timeout sau conexiune pierdută după prima cerere, dialogul avertizează că bonul poate fi deja tipărit, iar **Reîncearcă** reia de la cererea eșuată.
- **Casă de marcat simulată** (`ecr_simulator.esm.js`) — pentru teste, demonstrații, instruirea casierilor și suport, fără dispozitiv: citește și validează conținutul Datecs FiscalWire ca o casă reală (plăți, grupe TVA programate A 21 %, B 11 %, C/D/E 0 %, lungimea denumirii, prețuri pozitive), cu zi fiscală proprie (numere Z, NR, BF, totaluri pe grupe și tipuri de plată), rolă de hârtie cu antet `*** SIMULARE ***` și rapoarte X / Z. Simularea se setează pe punctul de vânzare (**Punct de vânzare → Configurare → Setări**, secțiunea **ECR**, sub transportul Terrabit Connect): *Simulated in Odoo (no agent)* sau *Simulated through the agent* (agentul pornit cu `TERRABIT_FISCAL_DRIVER=simulated`; altfel Odoo refuză trimiterea). Ziua fiscală e păstrată în browser. Nimic tipărit în simulare nu este bon fiscal; simularea se dezactivează pe toate punctele de vânzare înainte de punerea în funcțiune.
- **Panou „Virtual devices”** (`virtual_devices.esm.js`) — buton **Simulation** în bara POS (prin `deltatech_pos`) și în bara de sus din backend (cu o panglică roșie **SIMULATION** pe ecrane cât timp un dispozitiv e simulat): rola de hârtie, **Next answer** (implicit *By amount (automatic)* — cenții totalului aleg răspunsul: `,91` fără hârtie, `,92` deconectat, `,93` răspuns târziu, `,94` fără răspuns, `,95` bon anulat), **Until stopped**, **Delay**, rapoartele X / Z și **Reset the day**.
- **Cod ECR pe linie** — o linie de document poate purta `cod_ecr`, trimis ca atare drept cod de taxă (utile când două taxe cu același procent, ex. garanții SGR și taxare inversă, trebuie să ajungă pe categorii diferite); fără el se folosește maparea pe procent.
- **Cod de bare pe bon** — opțiunea `barcode_type` (`normal` sau `qr`) alege comanda; Datecs FiscalWire și Daisy au comandă QR, restul tipăresc codul normal.
- **Dispoziție de plată** — `formatEcrDocument()` tratează `type: "dp"` ca retragere din sertarul de numerar, folosind câmpul `amount` de nivel superior (liniile și plățile sunt ignorate).
- **Curățarea textelor libere** — client, cod fiscal, referință, note, denumire produs, unitate de măsură și cod de bare sunt curățate de caractere de control, separatori (`;` `,` `^`) și ghilimele, ca un nume cu rând nou să nu poată emite comenzi suplimentare în fișierul fiscal.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni server/cron Odoo — este o bibliotecă de cod JavaScript partajată, încărcată atât în asset bundle-ul POS (`point_of_sale._assets_pos`), cât și în backend (`web.assets_backend`).

**Componente JS**

- `ecr_document.esm.js`: definește contractul documentului fiscal standardizat și funcția `emptyEcrDocument()` care generează structura goală de pornire (antet, linii, plăți, opțiuni) pentru modulele producătoare.
- `ecr_format.esm.js`: conține șabloanele per-dispozitiv pentru protocoalele suportate (`datecs`, `datecs18`/`dxprint`, `fiscalnet`, `incotex`, `succes`, `daisy`, `optima`) și funcția `formatEcrDocument(doc, ecrType)` care produce comenzile specifice imprimantei fiscale; include și `unaccent()` pentru înlocuirea diacriticelor (casele de marcat nu acceptă UTF-8 cu diacritice). Doar `datecs18`/`dxprint` are momentan `ok_negative: true` (suport confirmat pentru cantități negative pe linia de vânzare); celelalte dispozitive rămân pe fallback-ul de discount valoric.
- `ecr_connect.esm.js`: funcțiile `ecrUuid(prefix)` (identificator unic per tipărire, folosit ca nume de fișier `.inp` și cheie de audit pe agent) și `sendEcrToConnect()` (transportul sincron către agentul Terrabit Connect, cu tratarea completă a ciclului de eroare și fallback la descărcare de fișier).
- `ecr_error_dialog.esm.js`: componenta OWL `FiscalErrorDialog`, dialogul de eroare cu opțiunile Reîncearcă / Descarcă și procesează manual / Anulează.
- `ecr_dxprint.esm.js`: transportul DxPrint (API local JSON), cu același contract de rezultat ca `sendEcrToConnect()`.
- `ecr_simulator.esm.js`: simulatorul casei de marcat Datecs FiscalWire (validări, zi fiscală, rolă, rapoarte X / Z); `sendEcrToConnect()` acceptă parametrul `simulation` (sau îl citește din configurarea POS): modul „odoo” răspunde fără agent, modul „agent” trimite scenariul la `/print` ca `simulate` și refuză trimiterea dacă `/fiscal/health` nu indică `simulated: true`.
- `virtual_devices.esm.js`: panoul „Virtual devices” (systray în backend, buton în bara POS); dispozitivele provin din furnizori și secțiuni înregistrate de alte module (casa de marcat aici, terminalul de card în `deltatech_payment_terminal`), iar butonul apare doar când un dispozitiv e în simulare.

Toate fișierele JS sunt listate explicit în manifest (fără wildcard-uri), fiindcă importul modulului ca zip pe Odoo Online refuză wildcard-urile; un fișier JS nou trebuie adăugat acolo.

**Teste**

- `static/tests/ecr_format.test.js`, `ecr_connect.test.js`, `ecr_dxprint.test.js`, `ecr_simulator.test.js`: teste hoot pentru convertor, transport, DxPrint și simulator, înregistrate în `web.assets_unit_tests`. Fișierele trebuie denumite cu sufixul `.test.js` — hoot nu execută fișiere `.spec.esm.js`, caz în care suita se raporta ca reușită fără să ruleze niciun test.

#### 5. Conexiuni

- [deltatech_pos_base](../deltatech_pos_base/index.md): pe punctul de vânzare se setează tipul casei de marcat, transportul și simularea folosite de această bibliotecă.
- [deltatech_pos](../deltatech_pos/index.md): modul producător — construiește documentul fiscal standardizat din comanda POS și delegă formatarea/trimiterea către acest modul.
- [deltatech_sale_store](../deltatech_sale_store/index.md): modul producător — construiește documentul fiscal standardizat din factură (vânzare din magazin) și delegă formatarea/trimiterea către acest modul.
- [deltatech_tc](../deltatech_tc/index.md): modulul de bază Terrabit Connect din Odoo (registru de stații, coadă de job-uri, endpoint-uri REST). Agentul local Terrabit Connect — componenta non-Odoo care rulează pe stația de lucru — primește fluxul de comenzi formatat prin HTTP local (`http://127.0.0.1:8765/print`) și îl transmite fizic casei de marcat (serial/USB/TCP).
- `deltatech_payment_terminal`: înregistrează terminalul de card în panoul „Virtual devices” (modul fără pagină wiki).
