# Joburi în coadă (Queue Job Enhancements) (localizat la `deltatech_queue_job/index.md`)

- **Nume Tehnic:** `deltatech_queue_job`
- **Versiune:** `19.0.1.4.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_queue_job`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_queue_job`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul aduce îmbunătățiri specifice peste funcționalitatea standard de cozi de joburi din Odoo (`queue_job`), concentrându-se pe performanță, fiabilitate și flexibilitate în execuția sarcinilor de fundal. Prin blocare optimizată a bazei de date și procesare tranzacțională sigură, permite mai multor lucrători (worker) să proceseze coada în paralel, fără blocaje reciproce. Este gândit special pentru a depăși limitările platformei Odoo.sh: ocolește limita de 5 minute a cron-ului prin procesare declanșată extern (la fiecare minut) și previne expirarea (timeout) lucrătorilor prin bugete de timp configurabile. Pe scurt, asigură că sarcinile de fundal sunt procesate cât mai rapid posibil, cu un consum minim de resurse și fiabilitate maximă.

#### 2. Funcționalități Cheie

- **Concurență și blocare optimizate:** metodă specializată (`_acquire_specific_job`) cu clauza SQL `FOR NO KEY UPDATE SKIP LOCKED`, care permite mai multor lucrători (cron intern sau API extern) să proceseze coada simultan, crescând semnificativ debitul.
- **Procesare tranzacțională robustă:** execuția joburilor este încapsulată în savepoint-uri de bază de date; dacă un job eșuează, doar modificările sale sunt anulate (rollback), păstrând starea pentru joburile următoare din același lot. Include tratarea automată a erorilor tipice de concurență (precum eșecuri de serializare), cu reprogramarea grațioasă a joburilor.
- **Runner-e flexibile pentru joburi:**
  - *Runner cron intern:* un `_job_runner` îmbunătățit care respectă limite configurabile de dimensiune a lotului și timp de execuție, prevenind timeout-urile lucrătorilor pe platforme precum Odoo.sh.
  - *Runner API extern:* un endpoint dedicat (`/api/v1/queue/process`) pentru servicii externe de declanșare (ex. cron-job.org), permițând intervale de procesare la fiecare minut, ocolind limita standard de 5 minute a cron-ului Odoo.
  - *Procesare în fir de execuție (thread):* posibilitatea de a lansa un runner în stil API într-un fir de fundal dedicat, direct din interfața Odoo, util pentru procesare manuală imediată fără a bloca interfața web.
- **Auto-declanșare inteligentă și debounce real:** creează automat declanșatori cron (`ir.cron.trigger`) ori de câte ori un job este creat sau i se actualizează ora programată (`eta`); `_cron_trigger` acceptă acum și liste de ETA (cazul joburilor amânate din runner-ul OCA), le tratează individual, de la cea mai apropiată, și evită declanșatori redundanți verificând corect dacă un trigger existent acoperă deja intervalul cerut.
- **Deduplicare inclusiv pentru joburi eșuate:** la crearea unui job nou, joburile mai vechi rămase în starea `failed` cu același `identity_key` sunt mutate automat în `cancelled` (deduplicarea standard verifică doar stările active); înregistrarea și traceback-ul rămân pentru diagnostic, iar `autovacuum` standard le șterge ulterior după `removal_interval` al canalului.
- **Curățare completă la autovacuum:** joburile anulate în lanț prin `cancel_dependent_jobs()` (care scria doar `state`, fără `date_cancelled`) primesc acum data de anulare, astfel încât cron-ul standard de autovacuum le poate colecta; suplimentar, `autovacuum()` extins șterge și joburile terminale (`done`/`cancelled`) rămase fără nicio dată de finalizare, pe baza `date_created`, curățând reziduul acumulat înainte de acest fix (joburile `failed` nu sunt niciodată atinse, fiind singurele utile pentru diagnostic).
- **Configurare centralizată:** o pagină de setări dedicată sub `Queue Job > Settings` permite administratorilor să genereze și să gestioneze chei API securizate, să definească `Batch Size` (numărul maxim de joburi per rulare) și `Max Seconds` (bugetul de timp per execuție).
- **Monitorizare și interfață îmbunătățite:** notificări integrate (Client Actions) cu feedback în timp real la declanșarea sau procesarea joburilor; vizualizări de listă îmbunătățite cu date de creare și acces facil la procesarea manuală; butoanele „Cron Trigger", „Process" și „Process Background" sunt mereu accesibile din antetul listei de joburi.

#### 3. Dependențe

- `queue_job`
- `queue_job_cron_jobrunner`

#### 4. Componente Cheie

**Modele**

- `queue.job`: model extins cu metodele de procesare optimizate — `_acquire_specific_job` (blocare `FOR NO KEY UPDATE SKIP LOCKED`), runner-ul cron intern îmbunătățit (`_job_runner`), auto-crearea declanșatorilor `ir.cron.trigger` la crearea sau actualizarea `eta` cu debounce corect (`_cron_trigger`), deduplicarea joburilor `failed` cu același `identity_key` (`_remove_failed_duplicates`) și `autovacuum()` extins pentru joburile terminale fără dată de finalizare.
- `res.config.settings`: extins pentru pagina de setări centralizate (cheie API, `Batch Size`, `Max Seconds`).

**Patch-uri (non-ORM)**

- `models/job_patch.py`: înlocuiește `Job.cancel_dependent_jobs` (clasa `queue_job.job.Job`, care nu e model ORM și nu poate fi extinsă prin `_inherit`) pentru a scrie `date_cancelled = now()` printr-un `UPDATE SQL` direct pe joburile anulate în lanț, imediat după anularea originală.

**Vizualizări**

- `queue_job_views`: vizualizări de listă îmbunătățite pentru joburi (câmp `identity_key` opțional, grupare după `model_name`) cu butoanele „Cron Trigger", „Process" și „Process Background"/„Process (Thread)" în antetul listei și al formularului.
- `res_config_settings_views`: pagina de setări `Queue Job > Settings` pentru generarea cheii API și configurarea loturilor, cu instrucțiuni integrate pentru configurarea unui cron extern (cron-job.org).

**Controlere / API**

- `/api/v1/queue/process` (POST, `jsonrpc`, `auth="public"`): endpoint pentru servicii externe de declanșare; parametri `api_key` (obligatoriu, verificat cu `secrets.compare_digest`), `batch_size` și `max_seconds` (opționali, cu valori implicite din configurare); răspunde cu numărul de joburi procesate/eșuate și starea cozii.
- `/api/v1/queue/stats` (GET/POST, `jsonrpc`, `auth="public"`): statistici curente ale cozii (pending, started, done, failed, total), protejate tot prin `api_key`.
- `/run_jobs` (POST, `auth="user"`): endpoint simplu, autentificat ca utilizator, care declanșează rularea joburilor pendinte.

**Acțiuni Automate / Acțiuni Server**

- Declanșatori `ir.cron.trigger`: creați automat la crearea unui job sau la actualizarea câmpului `eta`, pentru a porni procesarea imediat ce jobul devine eligibil; debounce-ul evită inserții redundante (măsurate anterior la peste 4.300 în 13 ore pe o instanță de producție).
- Parametri de configurare în `data/ir_config_parameter.xml`: valori implicite pentru cheia API și pentru setările de lot/timp.

#### 5. Conexiuni

- `queue_job`: modulul OCA de bază peste care se aplică toate îmbunătățirile de concurență, tranzacționalitate și runner.
- `queue_job_cron_jobrunner`: runner-ul bazat pe cron pe care acest modul îl extinde și optimizează.
