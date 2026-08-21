# Deltatech ECR Connect (shared) (localizat la `deltatech_ecr_connect/index.md`)

- **Nume Tehnic:** `deltatech_ecr_connect`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_ecr_connect
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ecr_connect`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul oferă blocurile comune, de tip bibliotecă JavaScript, pentru trimiterea documentelor fiscale (bon fiscal, dispoziție de plată) către casele de marcat electronice (ECR — Electronic Cash Register), prin agentul local Terrabit Connect. Înainte de acest modul, cunoașterea formatelor de casă de marcat era duplicată — în JavaScript în `deltatech_pos` și în Python în `deltatech_sale_store` — iar orice corecție de protocol sau dispozitiv nou trebuia aplicată în două locuri. Acest modul centralizează logica astfel încât orice modul „producător" de documente fiscale (comandă POS, factură) să o poată reutiliza fără duplicare.

#### 2. Funcționalități Cheie

- **Document fiscal standardizat** (`ecr_document.esm.js`) — contract JSON neutru față de tipul casei de marcat (antet, linii, plăți, opțiuni), pe care modulele producătoare (comandă POS, factură) îl construiesc din propriile date, prin `emptyEcrDocument()`.
- **Convertor de format** (`ecr_format.esm.js`) — sursa unică de adevăr pentru șabloanele specifice fiecărui dispozitiv (Datecs/FiscalWire, FiscalNet, Incotex, Optima, Daisy, Succes); funcția `formatEcrDocument(doc, ecrType)` transformă documentul standardizat în conținutul specific casei de marcat.
- **Trimițător Terrabit Connect** (`ecr_connect.esm.js`) — funcția `sendEcrToConnect()` trimite conținutul către agentul local (`http://127.0.0.1:8765/print`), tratează rezultatul sincron, deschide dialogul de eroare (reîncercare / intervenție manuală / anulare) și, la agent inaccesibil, cade automat pe descărcarea fișierului (flote mixte de case de marcat continuă să funcționeze).
- **Mapare cote TVA post-reformă 2025** — cotele noi (21 %, 11 %) sunt mapate pe grupele fiscale ale cotelor vechi (19 %, 9 %), astfel încât programarea fiscală existentă a caselor de marcat rămâne validă, fără reprogramare; hărțile `cod_tva` nu mai conțin cotele vechi (19 %, 18 %, 9 %, 5 %).
- **Cod fiscal client pe antet** — `formatHeader()` tipărește CUI-ul clientului (`header.cui`) imediat după numele acestuia, pe toate dispozitivele; apariția e decisă de modulul apelant (ex. `print_cui` în `deltatech_pos`), în funcție de pragul facturii simplificate.
- **Corecție de vânzare cu cantitate negativă** — pe `datecs18`/`dxprint` (FiscalWire 2018), o linie cu preț unitar pozitiv și cantitate negativă (ex. casierul tastează „-2" pentru a corecta o vânzare fără ecranul de Refund) se tipărește acum cu numele produsului și cantitatea negativă, în loc să cadă pe linia anonimă „subtotal + discount valoric".
- **Linie de discount recunoscută după valoare totală** — `formatLine()` identifică o linie de discount la nivel de document după valoarea totală (`preț × cantitate`), nu doar după prețul unitar negativ, astfel încât liniile de discount introduse cu preț unitar pozitiv și cantitate negativă (convenția uzuală pe facturi, ex. `deltatech_sale_store`) nu mai sunt omise de pe bonul fiscal.
- **Dialog de eroare fiscală partajat** (`ecr_error_dialog.esm.js`) — componentă OWL (`FiscalErrorDialog`) reutilizată de toate fluxurile fiscale (POS și backend) pentru a prezenta operatorului mesajul de eroare venit de la casa de marcat.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni server/cron Odoo — este o bibliotecă de cod JavaScript partajată, încărcată atât în asset bundle-ul POS (`point_of_sale._assets_pos`), cât și în backend (`web.assets_backend`).

**Componente JS**

- `ecr_document.esm.js`: definește contractul documentului fiscal standardizat și funcția `emptyEcrDocument()` care generează structura goală de pornire (antet, linii, plăți, opțiuni) pentru modulele producătoare.
- `ecr_format.esm.js`: conține șabloanele per-dispozitiv pentru protocoalele suportate (`datecs`, `datecs18`/`dxprint`, `fiscalnet`, `incotex`, `succes`, `daisy`, `optima`) și funcția `formatEcrDocument(doc, ecrType)` care produce comenzile specifice imprimantei fiscale; include și `unaccent()` pentru înlocuirea diacriticelor (casele de marcat nu acceptă UTF-8 cu diacritice). Doar `datecs18`/`dxprint` are momentan `ok_negative: true` (suport confirmat pentru cantități negative pe linia de vânzare); celelalte dispozitive rămân pe fallback-ul de discount valoric.
- `ecr_connect.esm.js`: funcțiile `ecrUuid(prefix)` (identificator unic per tipărire, folosit ca nume de fișier `.inp` și cheie de audit pe agent) și `sendEcrToConnect()` (transportul sincron către agentul Terrabit Connect, cu tratarea completă a ciclului de eroare și fallback la descărcare de fișier).
- `ecr_error_dialog.esm.js`: componenta OWL `FiscalErrorDialog`, dialogul de eroare cu opțiunile Reîncearcă / Descarcă și procesează manual / Anulează.

**Teste**

- `static/tests/ecr_format.test.js`: teste hoot pentru convertorul de format, înregistrate în `web.assets_unit_tests`. De la 19.0.1.1.1 fișierul e denumit corect cu sufixul `.test.js` (anterior `.spec.esm.js`), astfel încât hoot chiar execută suita — înainte se raporta succes fără să ruleze niciun test.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): modul producător — construiește documentul fiscal standardizat din comanda POS și delegă formatarea/trimiterea către acest modul.
- [deltatech_sale_store](../deltatech_sale_store/index.md): modul producător — construiește documentul fiscal standardizat din factură (vânzare din magazin) și delegă formatarea/trimiterea către acest modul.
- [deltatech_tc](../deltatech_tc/index.md): modulul de bază Terrabit Connect din Odoo (registru de stații, coadă de job-uri, endpoint-uri REST). Agentul local Terrabit Connect — componenta non-Odoo care rulează pe stația de lucru — primește fluxul de comenzi formatat prin HTTP local (`http://127.0.0.1:8765/print`) și îl transmite fizic casei de marcat (serial/USB/TCP).
