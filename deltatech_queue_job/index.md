# Queue Job Enhancements (localizat la `deltatech_queue_job/index.md`)

- **Nume Tehnic:** `deltatech_queue_job`
- **Versiune:** `19.0.1.4.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_queue_job
- **Cale Locală:** `odoo-addons/deltatech/deltatech_queue_job`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce îmbunătățiri peste coada standard de joburi din Odoo (`queue_job`), concentrate pe performanță, fiabilitate și flexibilitate în execuția sarcinilor de fundal. Prin blocare optimizată a bazei de date și procesare tranzacțională sigură, mai mulți lucrători (worker) pot procesa coada în paralel, fără să se blocheze reciproc. Este gândit pentru limitările platformei Odoo.sh: ocolește limita de 5 minute a cron-ului prin procesare declanșată extern (la fiecare minut) și previne expirarea lucrătorilor prin bugete de timp configurabile. Pe scurt, sarcinile de fundal sunt procesate cât mai rapid, cu consum minim de resurse și fiabilitate ridicată.

#### 2. Funcționalități Cheie

- **Concurență și blocare optimizate:** metoda `_acquire_specific_job` folosește clauza SQL `FOR NO KEY UPDATE SKIP LOCKED`, astfel încât mai mulți lucrători (cron intern sau API extern) procesează coada simultan, fără blocaje.
- **Procesare tranzacțională robustă:** execuția joburilor este încapsulată în savepoint-uri; dacă un job eșuează, doar modificările lui sunt anulate. Erorile tipice de concurență (de exemplu eșecurile de serializare) sunt tratate automat, cu reprogramarea jobului.
- **Runner-e flexibile:**
  - *Runner cron intern:* un `_job_runner` îmbunătățit, care respectă limite configurabile de dimensiune a lotului și de timp, prevenind timeout-urile pe platforme precum Odoo.sh;
  - *Runner API extern:* endpoint-ul `/api/v1/queue/process` pentru servicii externe de declanșare (ex. cron-job.org), cu intervale de procesare de un minut;
  - *Procesare în fir de execuție:* lansarea unui runner în stil API într-un fir de fundal, direct din interfață, pentru procesare manuală imediată fără blocarea interfeței web.
- **Auto-declanșare și debounce:** se creează automat declanșatori cron (`ir.cron.trigger`) la crearea unui job sau la actualizarea orei programate (`eta`); `_cron_trigger` acceptă și liste de ETA, le tratează de la cea mai apropiată și evită declanșatorii redundanți.
- **Deduplicare inclusiv pentru joburi eșuate (nou în 19.0):** când apare un job nou cu același `identity_key`, joburile mai vechi rămase în `failed` trec în `cancelled`, astfel încât lista de erori arată problemele reale, nu istoricul aceleiași operațiuni reluate; înregistrarea și traceback-ul rămân pentru diagnostic.
- **Curățare completă la autovacuum:** joburile anulate în lanț primesc data de anulare, iar `autovacuum()` șterge și joburile terminale (`done`/`cancelled`) rămase fără dată de finalizare; joburile `failed` nu sunt atinse.
- **Configurare centralizată:** **Job Queue → Settings** permite generarea cheii API (**Generate Key**), **Batch Size** (implicit 20) și **Max Seconds** (implicit 50).
- **Configurarea unui serviciu extern (cron-job.org):** URL `https://<domeniul-odoo>/api/v1/queue/process`, metoda POST, programare la fiecare minut, antet `Content-Type: application/json`, corp JSON-RPC cu `params.api_key`. Parametri: `api_key` (obligatoriu), `batch_size` și `max_seconds` (opționali).
- **Răspunsul API:** rezultatul este împachetat de două ori (în `result` → `result`), cu `status`, `processed`, `done`, `failed`, `postponed`, `pending_count`, `time_elapsed`, `timestamp`. Statusul HTTP este întotdeauna 200, chiar și pentru cheie invalidă sau eroare, care apar în corp ca `"status": "error"`; alertele bazate pe statusul HTTP din serviciul extern nu le vor prinde.
- **Statistici:** `POST /api/v1/queue/stats`, cu aceeași cheie, doar numără joburile (pending, started, done, failed, total); este o verificare sigură a cheii înainte de activarea procesării.
- **Procesare manuală** din **Job Queue → Queue → Jobs**, butoane în antetul listei (și al formularului):
  - **Cron Trigger**: activează cron-ul cozii, care pornește în câteva secunde; notificare verde (programat), galbenă „CRON Trigger already exists" sau roșie „No CRON Trigger found";
  - **Process Background** (pe formular **Process (Thread)**): procesează imediat un lot, într-un fir separat (fix până la 20 de joburi în 50 de secunde, nu valorile din setări);
  - **Process**: apare după selectarea a cel puțin unui job; acționează doar dacă măcar unul este pending și pornește cron-ul, care procesează toată coada, nu doar joburile selectate. Un job eșuat se repune mai întâi în coadă cu **Requeue Job**.

Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `queue_job`
- `queue_job_cron_jobrunner`

#### 4. Componente Cheie

**Modele**

- `queue.job` (extins): `_acquire_specific_job` (blocare `SKIP LOCKED`), `_job_runner` îmbunătățit, `_cron_trigger` cu debounce, `_remove_failed_duplicates` (anulează duplicatele `failed` cu același `identity_key`) și `autovacuum()` extins.
- `res.config.settings` (extins): setările centralizate (cheie API, `Batch Size`, `Max Seconds`).

**Patch-uri (non-ORM)**

- `models/job_patch.py`: înlocuiește `Job.cancel_dependent_jobs` (clasa `queue_job.job.Job` nu este model ORM și nu poate fi extinsă prin `_inherit`) pentru a scrie `date_cancelled` printr-un `UPDATE` SQL direct pe joburile anulate în lanț.

**Vizualizări**

- `queue_job_views`: liste îmbunătățite pentru joburi (`identity_key` opțional, grupare după `model_name`), cu butoanele **Cron Trigger**, **Process**, **Process Background** / **Process (Thread)**.
- `res_config_settings_views`: pagina **Queue Job Settings**, cu instrucțiuni integrate pentru cron-job.org.

**Controlere / API**

- `/api/v1/queue/process` (POST, `jsonrpc`, `auth="public"`): procesează un lot; `api_key` verificat cu `secrets.compare_digest`.
- `/api/v1/queue/stats` (GET/POST, `jsonrpc`, `auth="public"`): statistici ale cozii, protejate tot prin `api_key`.
- Ruta veche `/run_jobs` a fost eliminată (apela un runner inexistent și eșua mereu); este acoperită de un test de regresie.

**Acțiuni Automate / Acțiuni Server**

- Declanșatori `ir.cron.trigger`: creați automat la crearea unui job sau la actualizarea `eta`; debounce-ul evită inserțiile redundante.
- `data/ir_config_parameter.xml`: valorile implicite pentru cheia API și setările de lot/timp.

#### 5. Conexiuni

- `queue_job`: modulul OCA de bază peste care se aplică îmbunătățirile de concurență, tranzacționalitate și runner.
- `queue_job_cron_jobrunner`: runner-ul bazat pe cron, extins și optimizat de acest modul.
