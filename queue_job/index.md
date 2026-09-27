# Job Queue (localizat la `queue_job/index.md`)

- **Nume Tehnic:** `queue_job`
- **Versiune:** `20.0.2.0.1`
- **Cale:** `https://github.com/dhongu/queue/tree/20.0/queue_job`
- **Cale Locală:** `odoo-addons/queue/queue_job`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Modulul adaugă în Odoo o coadă de joburi integrată, care permite ca anumite apeluri de metode să fie amânate și executate asincron, în fundal, în loc să blocheze utilizatorul în timpul unei operațiuni. Joburile sunt stocate în PostgreSQL și procesate de un „Jobrunner" dedicat, fiecare într-o tranzacție proprie, cu reîncercări automate în caz de eșec temporar. Este modulul de bază (OCA) peste care se construiesc majoritatea automatizărilor de fundal — sincronizări, generări de documente, integrări externe — fără a încetini interfața pentru utilizator.

#### 2. Funcționalități Cheie

- Vizualizări dedicate pentru joburi (listă, formular, kanban), toate persistate în baza de date PostgreSQL.
- Jobrunner: proces care execută joburile eficient, folosind mecanismul `NOTIFY` din PostgreSQL pentru a porni joburile aproape instantaneu, fără polling.
- Canale (`queue.job.channel`): permit segregarea joburilor pe canale ierarhice (canal rădăcină `root` + subcanale) și limitarea capacității de procesare paralelă pe fiecare canal (ex: joburile grele pe un canal cu un singur worker, cele ușoare pe un canal cu 4).
- Reîncercări automate: joburile eșuate cu un tip de excepție reîncercabil sunt reprogramate automat, cu un tipar de reîncercare configurabil (`retry_pattern`) — ex: primele 3 încercări la 10 secunde distanță, următoarele 5 la 1 minut, etc.
- Proprietăți de job: prioritate, dată estimată de execuție (ETA), descriere personalizată, număr de reîncercări, `identity_key` pentru a preveni duplicarea unui job încă neexecutat.
- Acțiuni asociate (Related Actions): un buton pe formularul jobului care poate deschide, de exemplu, înregistrarea vizată de job (implicit deschide formularul/lista aferentă); comportamentul poate fi personalizat pe `queue.job.function` (`enable`, `func_name`, `kwargs`).
- Grafuri de joburi cu dependențe: prin API-ul `delayable()`, joburile pot fi înlănțuite (`chain()`, `on_done()`) sau grupate pentru execuție paralelă (`group()`); un job aflat în `wait_dependencies` așteaptă ca joburile părinte să se termine cu succes înainte de a porni.
- Împărțirea unui job mare în mai multe joburi mai mici, cu `.split(n)` (opțional `chain=True` pentru execuție secvențială), utilă la procesarea unor seturi mari de înregistrări.
- Configurare fără cod prin înregistrări XML `queue.job.function` (model + metodă, canal, acțiune asociată, tipar de reîncercare) și `queue.job.channel` (ierarhie de canale), fără a mai fi nevoie de decoratorul `@job` (obsolet).
- Meniu `Job Queue` (`Queue > Job Queue / Channels / Job Functions`), accesibil grupului „Job Queue Manager", cu wizard-uri pentru marcarea în masă a joburilor ca „Done" sau „Cancelled" și pentru reprogramarea (`requeue`) joburilor eșuate.
- Facilități pentru dezvoltatori/testare: `with_delay()` / `delayable()` pentru amânarea metodelor; `trap_jobs()` pentru a testa joburile fără să le execute efectiv; execuție sincronă (bypass) prin variabila de mediu `QUEUE_JOB__NO_DELAY=1` sau, în teste, prin cheia de context `queue_job__no_delay=True`.
- Configurare runner prin variabile de mediu sau fișierul `.conf` (secțiunea `[queue_job]`: `channels`, `scheme`, `host`, `port`, `http_auth_user`, `http_auth_password`); necesită `--workers` > 1 (sau `server_wide_modules = web,queue_job`) pentru ca joburile să pornească în paralel.
- Curățare automată: `ir.cron` zilnic („AutoVacuum Job Queue") care șterge periodic joburile terminate vechi.

#### 3. Dependențe

- `mail`
- `base_sparse_field`
- `web`

#### 4. Componente Cheie

**Modele**

- `queue.job` (`models/queue_job.py`): înregistrarea propriu-zisă a unui job — metodă, argumente, stare (`pending`, `enqueued`, `started`, `done`, `failed`, `cancelled`, `wait_dependencies`), prioritate, ETA, reîncercări, dependențe și rezultatul execuției.
- `queue.job.channel` (`models/queue_job_channel.py`): definește canalele ierarhice folosite pentru a segrega și limita capacitatea de procesare paralelă a joburilor.
- `queue.job.function` (`models/queue_job_function.py`): configurarea per model+metodă a canalului implicit, acțiunii asociate și tiparului de reîncercare pentru joburile generate din acea metodă.
- `queue.job.lock` (`models/queue_job_lock.py`): mecanism de blocare la nivel de bază de date, folosit de Jobrunner pentru a evita execuția concurentă a aceluiași job.
- `base` (`models/base.py`): adaugă tuturor modelelor metodele `with_delay()` / `delayable()`, punctul de intrare pentru amânarea asincronă a apelurilor de metode.
- `ir.model.fields` (`models/ir_model_fields.py`): extindere tehnică legată de câmpurile sparse folosite de `queue.job`.

**Vizualizări**

- `queue_job_views.xml`: formular, listă și kanban pentru `queue.job`, cu butoane de acțiune (Requeue, Cancel, Done) și afișarea acțiunii asociate.
- `queue_job_channel_views.xml`: gestionarea ierarhiei de canale și a capacității lor.
- `queue_job_function_views.xml`: configurarea funcțiilor de job (model, metodă, canal, acțiune asociată, tipar de reîncercare).
- `queue_jobs_to_done_views.xml` / `queue_jobs_to_cancelled_views.xml` / `queue_requeue_job_views.xml`: wizard-uri pentru operațiuni în masă asupra joburilor selectate.
- `queue_job_menus.xml`: meniul `Job Queue` (rădăcină) cu submeniurile Queue > Job Queue / Channels / Job Functions, restricționat grupului `group_queue_job_manager`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_autovacuum_queue_jobs`: rulează zilnic (`model.autovacuum()` pe `queue.job`) și curăță joburile vechi terminate, conform intervalului de păstrare configurat pe canal.

#### 5. Conexiuni

- [deltatech_queue_job](../deltatech_queue_job/index.md): extinde `queue_job` cu blocare optimizată (`SKIP LOCKED`), un runner API extern pentru Odoo.sh, deduplicare avansată și curățare completă la autovacuum.
- `base_import_async`: modul OCA menționat în documentația de configurare ca exemplu tipic de generator de joburi prin `queue_job`.
