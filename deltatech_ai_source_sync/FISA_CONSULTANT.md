# Fișă Modul: Colecții de surse pentru agenții AI (GitHub, ZIP, RSS)

**Modul:** `deltatech_ai_source_sync`
**Utilizator principal:** Administrator Odoo / consultant care configurează agenții AI
**Prioritate:** 🟡 Medie (modul de configurare, folosit la punerea în funcțiune a agenților și la întreținerea documentației lor)

---

## 1. Scop business

Agenții AI din Odoo 19 Enterprise răspund pe baza unor surse (documente) încărcate pe agent. Încărcarea
fișierelor unul câte unul nu e practică pentru o documentație întreagă: un wiki de module, legislația
sau știrile fiscale. Modulul introduce **colecția de surse**: o colecție se leagă de un agent și îi
ține sursele la zi pornind de la un depozit **GitHub**, o arhivă **ZIP** sau o listă de **fluxuri RSS**.
Sincronizarea este incrementală (se reiau doar fișierele schimbate), iar documentele mari se pot
împărți pe secțiuni, ca citările agentului să trimită la secțiunea potrivită. Pe agent se pot regla și
căutarea în surse (glosar de termeni, numărul de fragmente date modelului).

## 2. Bază legală și context

Modulul nu generează operațiuni contabile și nu are o bază legală proprie. Contextul operațional:

- Colecțiile din fluxuri RSS păstrează doar ce publică fluxul pentru sindicalizare: titlul, data,
  linkul și rezumatul din flux, niciodată articolul întreg. Sursa trimite la articol, nu îl copiază.
- Pentru legislație sau știri, sursele sunt documente de referință, nu sfat fiscal: recomandați
  păstrarea știrilor pe un agent separat de cel care folosește textele legilor.
- **Legăturile publice** se activează numai pentru pagini publice (un depozit GitHub public, un site
  public), pentru că citările devin vizibile tuturor utilizatorilor, inclusiv vizitatorilor
  site-ului care discută cu un agent livechat.

## 3. Utilizatori și roluri

| Rol | Acțiune |
|---|---|
| Administrator Odoo (grupul **Administrare / Setări**) | creează și sincronizează colecțiile, completează glosarul și setările de căutare ale agentului |
| Consultant | alege originea, filtrele și nivelul de împărțire potrivite documentației clientului |
| Utilizator al agentului AI | pune întrebări și vede citările; nu are acces la colecții |

Colecțiile, meniul lor și fila **Source Search** de pe agent sunt vizibile doar administratorilor
(`base.group_system`). Pentru testare e nevoie de un utilizator cu acest drept.

## 4. Conturi și date implicate

Modulul nu postează nicio notă contabilă și nu folosește conturi contabile.

Date minime pentru demo:

- un agent AI creat în **AI** (modulul `ai_app`);
- un depozit GitHub public cu fișiere Markdown (sau o arhivă ZIP cu fișiere `.md`);
- pentru RSS: cel puțin un flux accesibil, de exemplu `https://www.contzilla.ro/feed/`;
- un furnizor de embeddings configurat pe agent, pentru ca sursele să fie indexate de cronul standard AI.

## 5. Configurare inițială

1. Instalați modulul `deltatech_ai_source_sync` (depinde de `ai_app`).
2. Verificați că aveți dreptul de administrator: fără el nu apar meniul **Source Collections** și
   fila **Source Search**.
3. Verificați că agentul are un model și un furnizor AI configurate, altfel sursele nu pot fi
   transformate în embeddings.
4. Verificați în **Settings → Technical → Automation → Scheduled Actions** acțiunea **AI: synchronize
   the source collections** (rulează zilnic). Sincronizarea pornită manual folosește aceeași acțiune.

## 6. Flux de utilizare

### Pasul 1 — Crearea colecției

Accesați **AI → Configuration → Source Collections** și apăsați **New**. Alternativ, deschideți
agentul și folosiți butonul **Collections** din partea de sus a formularului. În acest caz agentul e
precompletat.

Completați **Name** (de exemplu „Wiki module”) și alegeți **Agent**.

### Pasul 2 — Alegerea originii

În grupul **Origin** alegeți una dintre variante; câmpurile se schimbă după alegere:

| Origine | Câmpuri |
|---|---|
| **GitHub repository** | **Github Repository** (`owner/name`, obligatoriu), **Github Branch**, **Github Token** (doar pentru depozit privat, cu drept de citire a conținutului) |
| **ZIP archive** | **ZIP Archive** (obligatoriu); un singur folder de la rădăcina arhivei este ignorat |
| **RSS feeds** | **Feeds** (un URL de flux RSS sau Atom pe linie, obligatoriu), **Pages per Feed** (pagini citite dintr-un flux paginat, WordPress `?paged=N`), **Retention (days)** (implicit 90) |

Pentru RSS, formularul ascunde **Root Path**, **Page URL** și grupul **Files**: nu se aplică.

**Ce intră dintr-un flux RSS.** Fiecare articol devine o sursă cu site-ul, data, titlul, linkul și
rezumatul publicat în flux. Sunt păstrate **doar articolele cu link http sau https**: articolele fără
link, cu link relativ sau cu o schemă ca `javascript:` ori `data:` sunt sărite. Motivul: linkul vine de la un terț și devine adresa din citări și din **Open source**, vizibile
și vizitatorilor livechat când e bifat **Public links**. Dacă un articol nu apare ca sursă, verificați
întâi linkul lui în flux.

### Pasul 3 — Selecția și prelucrarea fișierelor (GitHub și ZIP)

În grupul **Files** (și în **Origin**, pentru **Root Path**) reglați:

- **Root Path** — se citesc doar fișierele de sub acest director;
- **Include Patterns** / **Exclude Patterns** — câte un șablon pe linie, aplicat pe calea relativă;
  `*` acoperă și `/` (de exemplu `*/index.md`);
- **Split Level** — **Do not split** sau **Heading 1…4**: un fișier mare (o lege, un manual) devine o
  sursă pe secțiune, iar numele sursei păstrează titlurile de deasupra;
- **Strip Section Titles** — titluri de secțiuni eliminate cu tot conținutul (de exemplu secțiunile
  tehnice dintr-o documentație pentru clienți);
- **Prefix with Folder** — numele sursei începe cu folderul fișierului (de exemplu numele tehnic al
  modulului), ca agentul să-l numească în răspunsuri;
- **Page URL** — linkul citat în loc de pagina GitHub, cu `{path}` pentru calea fără extensie;
- fișierele `*.rst` (documentația Odoo) sunt convertite în Markdown și împărțite la fel.

### Pasul 4 — Legături publice, sincronizare zilnică, fragmente rezervate

- **Public links** — linkul fișierului se scrie sub titlul fiecărei surse, iar citările se arată
  tuturor utilizatorilor. Bifați numai pentru pagini publice.
- **Daily Synchronization** — vizibil la origine GitHub și RSS (nu pentru ZIP).
- **Reserved Fragments** — numărul de fragmente din contextul agentului care vin întotdeauna din
  această colecție, util când o colecție mică e acoperită de una mare. Valoarea nu poate fi negativă.

### Pasul 5 — Sincronizarea

Apăsați **Synchronize**. Apare mesajul că sincronizarea rulează în fundal; formularul nu se
actualizează imediat, rezultatul apare după rularea cronului.

**Găsește pe ecran.** După rularea cronului, redeschideți colecția și uitați-vă la grupul **Last
Synchronization**: **Last Sync Date** și **Last Sync Message** (`Files added: …, updated: …, removed:
…, unchanged: …, failed: …`; sub rezumat apar până la 20 de erori, câte una pe linie).

**Verifică:**

- data ultimei sincronizări e cea de azi, iar câmpul **Sync Requested** a dispărut;
- `failed` este 0; dacă nu, fiecare eroare indică fișierul sau fluxul cu problemă;
- pentru un depozit mare, mesajul **The GitHub tree is truncated: no source was removed** înseamnă că
  nu s-au șters surse; restrângeți **Root Path**;
- la a doua sincronizare, fără modificări, toate fișierele apar la `unchanged`.

**Treci mai departe.** Butonul **Sources** (în partea de sus a colecției) deschide lista surselor
create; acestea sunt transformate în embeddings de cronul standard AI.

Pentru sincronizări lungi, cronul se reia de unde a rămas; la rate limit-ul furnizorului, cererile
sunt reluate după așteptarea cerută, iar sursele eșuate sunt puse înapoi în coadă (de cel mult 3 ori).

**Comportament RSS la sincronizare.** Un articol care iese din flux își păstrează sursa până depășește
perioada **Retention (days)**; articolele mai vechi decât perioada nu se adaugă, iar sursele lor se
șterg.

### Pasul 6 — Setările de căutare pe agent

Deschideți agentul (**AI → Agents**) și fila **Source Search**:

- **Fragments in Context** — câte fragmente primește modelul la fiecare întrebare (1–30, implicit 5);
- **One Fragment per Source** — păstrează doar cel mai bun fragment al fiecărei surse; util pentru
  întrebări de tip listă („ce module avem pentru X”);
- **Search Glossary** — o intrare pe linie, `termen[, variantă...] = înțeles`; liniile care încep cu
  `#` sunt comentarii. Înțelesul termenilor găsiți în întrebare se adaugă la ea înainte de căutare;
  răspunsul se scrie tot pe baza întrebării originale.

### Note de monografie și raportare

Modulul nu generează note contabile și nu alimentează declarații sau rapoarte contabile.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `ai_app` (Odoo Enterprise) | agenții, sursele și meniul **AI → Configuration** pe care se montează colecțiile |
| cronul standard AI | transformă sursele create în embeddings |

**Ce e automat:** citirea fișierelor sau fluxurilor, împărțirea pe secțiuni, curățarea textului
(imaginile rămân doar cu textul alternativ, linkurile cu textul lor), omiterea fișierelor
neschimbate, ștergerea surselor fișierelor dispărute, reluarea după rate limit, sincronizarea zilnică
la GitHub și RSS.

**Ce rămâne manual:** crearea colecției și alegerea filtrelor, completarea glosarului, apăsarea
**Synchronize** pentru o actualizare imediată, reîncărcarea ZIP-ului când se schimbă arhiva.

Modulul corectează și extragerea textului din fișierele Markdown și text pentru **toate** atașamentele:
indexarea standard păstra doar caracterele ASCII, iar cuvintele cu diacritice se deformau înainte de
embeddings. Fișierele încărcate înainte de instalare își păstrează vechiul index până sunt încărcate
din nou.

## 8. Verificări pentru consultant

- [ ] Meniul **AI → Configuration → Source Collections** apare pentru administrator și nu apare pentru
      un utilizator fără drept de administrator.
- [ ] La origine **GitHub repository** apar câmpurile depozit, ramură și token (token-ul e mascat); la
      **ZIP archive**, câmpul arhivă; la **RSS feeds**, fluxurile, paginile și retenția.
- [ ] La **RSS feeds** dispar **Root Path**, **Page URL** și grupul **Files**; la **ZIP archive**
      dispare **Daily Synchronization**.
- [ ] După **Synchronize** și rularea cronului, **Last Sync Message** arată fișierele adăugate și
      `failed: 0`.
- [ ] A doua sincronizare, fără modificări, arată toate fișierele la `unchanged`.
- [ ] Pe un flux RSS de test care conține articole cu linkuri `javascript:`, `data:` sau relative,
      acestea nu apar printre surse; articolele cu link `https://` apar.
- [ ] Fiecare sursă RSS are în text rândul `Link:` cu adresa articolului.
- [ ] La **Split Level** = **Heading 2**, un fișier cu mai multe secțiuni dă mai multe surse, cu
      numele de forma `Titlu document › Titlu secțiune`.
- [ ] Cu **Public links** bifat, sub titlul fiecărei surse apare rândul `Link:`.
- [ ] **Reserved Fragments** cu valoare negativă este refuzat cu mesajul „The reserved fragments
      cannot be negative.”
- [ ] **Fragments in Context** în afara intervalului 1–30 este refuzat.
- [ ] Un termen din glosar, scris în întrebarea unui agent, aduce în rezultate documentul care folosește
      denumirea completă.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| `GitHub answered 404 for …` (sau 401/403) | depozit sau ramură greșite, depozit privat fără token sau token fără drept de citire | corectați depozitul și ramura; adăugați un token cu drept de citire a conținutului |
| `Set the GitHub repository of the collection …` | origine GitHub fără depozit | completați **Github Repository** |
| `Upload the ZIP archive of the collection …` | origine ZIP fără arhivă | încărcați arhiva |
| `The file of the collection … is not a ZIP archive.` | fișierul încărcat nu e un ZIP valid | încărcați o arhivă ZIP corectă |
| `Set the feeds of the collection …` | origine RSS fără fluxuri | completați **Feeds**, câte un URL pe linie |
| `No feed of the collection … could be read.` | niciun flux nu răspunde sau nu e RSS/Atom valid | verificați adresele; fiecare eroare e listată în **Last Sync Message** |
| `The feed answered … for …` | fluxul răspunde cu un cod diferit de 200 | verificați adresa fluxului sau reîncercați mai târziu |
| `Synchronization failed: …` | sincronizarea a fost oprită de o eroare de rețea sau de configurare | citiți mesajul din **Last Sync Message**, corectați cauza și apăsați din nou **Synchronize** |
| `The GitHub tree is truncated: no source was removed.` | depozitul e prea mare pentru o listare completă | restrângeți **Root Path** sau folosiți șabloane de include |
| `The number of fragments in context must be between 1 and 30.` | valoare în afara intervalului pe agent | introduceți o valoare între 1 și 30 |
| `The reserved fragments cannot be negative.` | **Reserved Fragments** negativ | introduceți 0 sau o valoare pozitivă |

## 10. Capturi de ecran

Modulul nu are `tests/test_screenshots.py`, deci fișa nu conține capturi de ecran. Ecranele
descrise în secțiunea 6 (lista colecțiilor, formularul colecției, fila **Source Search** a agentului)
sunt standard Odoo, iar etichetele apar în engleză, pentru că modulul nu are traducere în română.

## 11. Observații pentru manual

- Redactorul manualului păstrează explicația fluxului **origine → filtre → sincronizare → verificarea
  mesajului**; este singura parte pe care consultantul o repetă la fiecare client.
- Păstrați avertismentul despre **Public links**: se bifează numai pentru pagini publice, pentru că
  citările devin vizibile vizitatorilor livechat.
- Păstrați regula pentru RSS: doar articole cu link http sau https; sursa conține rezumatul din flux,
  nu articolul întreg.
- Exemple de configurare (din `USAGE.md`) utile în manual: wiki de module cu două colecții pe același
  depozit și **Prefix with Folder**; legislație cu **Root Path** `references` și **Split Level** =
  **Heading 2**; știri legislative pe un agent separat, 5 pagini per flux, retenție 90 de zile.
